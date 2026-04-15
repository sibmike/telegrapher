"""
Batch API compression pipeline.

Submits compression jobs via the OpenAI Batch API for cost-effective
async processing.  Extracted from batch_batch_1.ipynb.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from tqdm import tqdm

import config
from telegrapher.chunking import chunk_text
from telegrapher.clients import get_openai_client
from telegrapher.data.longbench import load_longbench
from telegrapher.io_utils import load_prompt

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Batch request helpers
# ------------------------------------------------------------------

def create_batch_requests(
    doc_id: str,
    chunks: List[str],
    model: str,
    system_prompt: str,
) -> List[dict]:
    """Build OpenAI Batch API request bodies for each chunk."""
    requests = []
    for i, chunk in enumerate(chunks):
        requests.append({
            "custom_id": f"chunk-{doc_id}-{i}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": chunk},
                ],
                "max_tokens": config.MAX_TOKENS_COMPLETION,
            },
        })
    return requests


def submit_batch(
    client,
    requests: List[dict],
    doc_id: str,
    work_dir: Path,
) -> str:
    """
    Write a batch JSONL, upload it, and submit a batch job.

    Returns the batch ID.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    batch_file = work_dir / f"batch_{doc_id}.jsonl"

    with open(batch_file, "w", encoding="utf-8") as fh:
        for req in requests:
            fh.write(json.dumps(req, ensure_ascii=False) + "\n")

    logger.info("Uploading batch file for document %s …", doc_id)
    with open(batch_file, "rb") as fh:
        uploaded = client.files.create(file=fh, purpose="batch")

    batch = client.batches.create(
        input_file_id=uploaded.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )
    logger.info("Submitted batch %s for document %s.", batch.id, doc_id)
    return batch.id


def poll_batch(
    client,
    batch_id: str,
    interval: int = config.BATCH_STATUS_CHECK_INTERVAL,
) -> Any:
    """
    Poll the batch until it reaches a terminal state.

    Returns the final batch status object.
    """
    terminal_states = {"completed", "failed", "expired", "cancelled"}

    while True:
        status = client.batches.retrieve(batch_id)
        logger.info("Batch %s status: %s", batch_id, status.status)
        if status.status in terminal_states:
            return status
        time.sleep(interval)


def download_and_parse_results(
    client,
    batch_status: Any,
    doc_id: str,
    output_dir: Path,
) -> List[dict]:
    """
    Download the batch output and parse per-chunk results.

    Returns a list of dicts, one per chunk.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    if batch_status.status != "completed":
        logger.error("Batch %s ended with status %s.", batch_status.id, batch_status.status)
        if batch_status.error_file_id:
            err_content = client.files.content(batch_status.error_file_id)
            err_path = output_dir / f"batch_errors_{doc_id}.jsonl"
            err_path.write_text(err_content.text, encoding="utf-8")
            logger.error("Error file saved to %s.", err_path)
        return []

    content = client.files.content(batch_status.output_file_id)
    raw_path = output_dir / f"batch_output_{doc_id}.jsonl"
    raw_path.write_text(content.text, encoding="utf-8")

    results: List[dict] = []
    for line in content.text.strip().splitlines():
        rec = json.loads(line)
        custom_id = rec.get("custom_id", "")
        # custom_id format: "chunk-{doc_id}-{chunk_idx}"
        parts = custom_id.rsplit("-", 1)
        chunk_idx = int(parts[-1]) if len(parts) > 1 and parts[-1].isdigit() else 0

        try:
            compressed_text = (
                rec["response"]["body"]["choices"][0]["message"]["content"]
            )
        except (KeyError, IndexError):
            logger.warning("Could not extract text for %s", custom_id)
            continue

        result = {
            "doc_id": doc_id,
            "chunk_id": chunk_idx,
            "compressed_text": compressed_text.strip(),
        }
        results.append(result)

        # Persist per-chunk file
        out_path = output_dir / f"compressed_{doc_id}_{chunk_idx}.jsonl"
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(result, ensure_ascii=False) + "\n")

    logger.info("Document %s: parsed %d results.", doc_id, len(results))
    return results


# ------------------------------------------------------------------
# Mapping file for resume capability
# ------------------------------------------------------------------

def save_batch_mapping(mapping: Dict[str, str], path: Path) -> None:
    """Persist the doc_id → batch_id mapping."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(mapping, fh, indent=2)


def load_batch_mapping(path: Path) -> Dict[str, str]:
    """Load an existing doc_id → batch_id mapping, or return empty dict."""
    if path.exists():
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return {}


# ------------------------------------------------------------------
# Full pipeline
# ------------------------------------------------------------------

def run_batch_pipeline(
    output_dir: Path,
    mapping_file: Path,
    *,
    max_chunks: int = config.MAX_CHUNKS_BATCH,
    n_samples: Optional[int] = None,
) -> None:
    """
    Run the batch API compression pipeline on LongBench-v2.

    Parameters
    ----------
    output_dir : Path
        Directory for compressed output.
    mapping_file : Path
        JSON file mapping doc_id → batch_id (for resume).
    max_chunks : int
        Maximum chunks per document.
    n_samples : int, optional
        Process only the first *n_samples* documents.
    """
    client = get_openai_client()
    system_prompt = load_prompt("compression_v5.txt")
    docs = load_longbench()
    mapping = load_batch_mapping(mapping_file)

    if n_samples is not None:
        docs = docs[:n_samples]

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for doc in tqdm(docs, desc="Batch compressing"):
        doc_id = doc.get("_id", "unknown")

        if doc_id in mapping:
            logger.debug("Skipping %s — already submitted.", doc_id)
            continue

        context = doc.get("context") or doc.get("source", "")
        if not context:
            logger.warning("Document %s has no context — skipping.", doc_id)
            continue

        chunks = chunk_text(context, max_words=config.CHUNK_MAX_WORDS)
        chunks = chunks[:max_chunks]
        if not chunks:
            continue

        requests = create_batch_requests(doc_id, chunks, config.COMPRESSION_MODEL, system_prompt)
        batch_id = submit_batch(client, requests, doc_id, output_dir)

        mapping[doc_id] = batch_id
        save_batch_mapping(mapping, mapping_file)

        batch_status = poll_batch(client, batch_id)
        download_and_parse_results(client, batch_status, doc_id, output_dir)
