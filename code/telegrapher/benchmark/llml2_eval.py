"""
LLMLingua2 comparison evaluation.

Tests LLMLingua2-compressed texts against the same QA benchmark data
generated for Telegraph English, allowing direct accuracy comparison.
Extracted from qa_llml2.ipynb.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import List, Optional

import pandas as pd
from tqdm import tqdm

import config
from telegrapher.benchmark.mc_evaluation import ask_mc
from telegrapher.clients import get_openai_client

logger = logging.getLogger(__name__)


def find_qa_file(
    compressed_file: Path,
    qa_dir: Path,
    prefix: str = "llmlingua2_",
) -> Optional[Path]:
    """
    Match a LLMLingua2-compressed file to its QA benchmark file.

    Removes *prefix* from the filename to find the corresponding
    file in *qa_dir*.
    """
    name = compressed_file.name
    if name.startswith(prefix):
        name = name[len(prefix):]
    candidate = qa_dir / name
    return candidate if candidate.exists() else None


def process_file(
    compressed_file: Path,
    qa_dir: Path,
    output_dir: Path,
    client,
    mc_model: str = config.LLML2_MC_MODEL,
) -> Optional[dict]:
    """
    Evaluate a single LLMLingua2-compressed file against its QA data.

    Returns a result dict, or ``None`` if skipped.
    """
    qa_file = find_qa_file(compressed_file, qa_dir)
    if qa_file is None:
        logger.debug("No QA file for %s — skipping.", compressed_file.name)
        return None

    # Load compressed data
    with open(compressed_file, "r", encoding="utf-8") as fh:
        comp_data = json.loads(fh.readline())

    compressed_text = comp_data.get("compressed_context") or comp_data.get("compressed_text", "")
    original_tokens = comp_data.get("original_tokens", 0)
    compressed_tokens = comp_data.get("compressed_tokens", 0)
    compression_rate = comp_data.get("compression_rate_pct", 0.0)

    # Load QA data
    with open(qa_file, "r", encoding="utf-8") as fh:
        qa_data = json.loads(fh.readline())

    question = qa_data.get("question", "")
    choices = qa_data.get("choices", [])
    gold_idx = qa_data.get("gold_idx", 0)

    if not compressed_text or not question or not choices:
        logger.warning("Incomplete data for %s — skipping.", compressed_file.name)
        return None

    # Run MC evaluation on compressed text
    comp_idx = ask_mc(compressed_text, question, choices, client, mc_model)

    result = {
        "id": comp_data.get("_id", compressed_file.stem),
        "original_tokens": original_tokens,
        "compressed_tokens": compressed_tokens,
        "compression_rate_pct": compression_rate,
        "question": question,
        "choices": choices,
        "gold_idx": gold_idx,
        "comp_idx": comp_idx,
        "compressed_correct": comp_idx == gold_idx,
    }

    # Save result
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / compressed_file.name
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(result, ensure_ascii=False) + "\n")

    return result


def run_llml2_evaluation(
    compressed_dir: Path,
    qa_dir: Path,
    output_dir: Path,
    *,
    mc_model: Optional[str] = None,
    prefix: str = "llmlingua2_",
) -> pd.DataFrame:
    """
    Evaluate all LLMLingua2-compressed files against QA benchmarks.

    Parameters
    ----------
    compressed_dir : Path
        Directory with LLMLingua2-compressed JSONL files.
    qa_dir : Path
        Directory with QA benchmark JSONL files (from TE benchmarking).
    output_dir : Path
        Directory for evaluation results.
    mc_model : str, optional
        Model for MC answering.  Defaults to :data:`config.LLML2_MC_MODEL`.
    prefix : str
        Filename prefix to strip when matching to QA files.

    Returns
    -------
    pd.DataFrame
        Aggregated results.
    """
    if mc_model is None:
        mc_model = config.LLML2_MC_MODEL

    client = get_openai_client()
    compressed_dir = Path(compressed_dir)
    qa_dir = Path(qa_dir)
    output_dir = Path(output_dir)

    files = sorted(compressed_dir.glob("*.jsonl"))
    logger.info("Found %d LLMLingua2 files to evaluate.", len(files))

    results: List[dict] = []
    for fp in tqdm(files, desc="LLML2 eval"):
        result = process_file(fp, qa_dir, output_dir, client, mc_model)
        if result is not None:
            results.append(result)

    df = pd.DataFrame(results)
    if not df.empty:
        acc = df["compressed_correct"].mean()
        logger.info("LLML2 accuracy (%d files): %.4f", len(df), acc)
    return df
