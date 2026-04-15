"""
Quality review of compressed Telegraph English via Claude.

Sends original + compressed text pairs to Claude for scoring and
critique.  Extracted from review_batch_1.ipynb.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Optional

from tqdm import tqdm

import config
from telegrapher.api_utils import api_call_with_retry, parse_json_response
from telegrapher.clients import get_anthropic_client
from telegrapher.io_utils import load_prompt, read_jsonl

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Single-pair review
# ------------------------------------------------------------------

def review_compression(
    original: str,
    compressed: str,
    client,
    model: str = config.REVIEW_MODEL,
) -> str:
    """
    Send an original/compressed pair to Claude for quality review.

    Returns the raw Claude response text (expected to contain JSON).
    """
    prompt = load_prompt(
        "review.txt",
        variables={"original_text": original, "compressed_text": compressed},
    )

    response = api_call_with_retry(
        client.messages.create,
        model=model,
        max_tokens=config.MAX_TOKENS_COMPLETION,
        temperature=config.TEMPERATURE_REVIEW,
        messages=[{"role": "user", "content": prompt}],
    )

    if response is None:
        logger.warning("Review returned None.")
        return ""

    return response.content[0].text


# ------------------------------------------------------------------
# Score extraction
# ------------------------------------------------------------------

def extract_review_score(review_text: str) -> Optional[int]:
    """
    Extract the ``summaryScore`` from a Claude review response.

    Handles JSON embedded in markdown code fences.
    Returns ``None`` if parsing fails.
    """
    obj = parse_json_response(review_text)
    if obj and "summaryScore" in obj:
        try:
            return int(obj["summaryScore"])
        except (ValueError, TypeError):
            pass

    # Fallback: regex on raw text
    m = re.search(r'"summaryScore"\s*:\s*(\d+)', review_text)
    if m:
        return int(m.group(1))

    logger.warning("Could not extract summaryScore from review.")
    return None


# ------------------------------------------------------------------
# Pipeline
# ------------------------------------------------------------------

def run_review_pipeline(
    input_dir: Path,
    output_dir: Path,
    *,
    model: str = config.REVIEW_MODEL,
) -> None:
    """
    Review all compressed JSONL files in *input_dir*.

    For each chunk, writes a review ``.txt`` file to *output_dir*.
    """
    client = get_anthropic_client()
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_files = sorted(input_dir.glob("*.jsonl"))
    logger.info("Found %d JSONL files to review.", len(jsonl_files))

    for jf in tqdm(jsonl_files, desc="Reviewing"):
        records = read_jsonl(jf)
        for line_num, data in enumerate(records, start=1):
            original = data.get("chunk", "")
            compressed = data.get("compressed_context", "")
            if not original or not compressed:
                logger.warning("Missing text in %s line %d — skipping.", jf.name, line_num)
                continue

            review = review_compression(original, compressed, client, model)

            stem = jf.stem
            out_path = output_dir / f"{stem}_review_line{line_num}.txt"
            out_path.write_text(review, encoding="utf-8")


def aggregate_scores(review_dir: Path) -> dict:
    """
    Read all review ``.txt`` files and compute aggregate statistics.

    Returns ``{"total": int, "scored": int, "average": float}``.
    """
    review_dir = Path(review_dir)
    txt_files = sorted(review_dir.glob("*.txt"))

    total = 0
    scores: list[int] = []

    for tf in txt_files:
        total += 1
        text = tf.read_text(encoding="utf-8")
        score = extract_review_score(text)
        if score is not None:
            scores.append(score)

    avg = sum(scores) / len(scores) if scores else 0.0
    result = {"total": total, "scored": len(scores), "average": round(avg, 2)}
    logger.info("Review scores — %s", result)
    return result
