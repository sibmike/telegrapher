"""
Synchronous compression pipeline.

Compresses documents one chunk at a time via the OpenAI Chat Completions
API.  Extracted from batch_1.ipynb.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import List, Optional

from tqdm import tqdm

import config
from telegrapher.api_utils import api_call_with_retry
from telegrapher.chunking import chunk_text
from telegrapher.clients import get_openai_client
from telegrapher.data.longbench import load_longbench
from telegrapher.io_utils import load_prompt
from telegrapher.tokens import calculate_token_compression

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Core compression function
# ------------------------------------------------------------------

def compress_text(
    context: str,
    client,
    model: str = config.COMPRESSION_MODEL,
    system_prompt: str | None = None,
) -> str:
    """
    Compress a single text chunk into Telegraph English.

    Returns the compressed text, or an empty string on failure.
    """
    if system_prompt is None:
        system_prompt = load_prompt("compression_v5.txt")

    response = api_call_with_retry(
        client.chat.completions.create,
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context},
        ],
    )

    if response is None:
        logger.warning("Compression returned None — skipping chunk.")
        return ""

    return response.choices[0].message.content.strip()


# ------------------------------------------------------------------
# Document-level compression
# ------------------------------------------------------------------

def compress_document(
    doc: dict,
    output_dir: Path,
    *,
    system_prompt: str | None = None,
    max_chunks: int = config.MAX_CHUNKS_SYNC,
    client=None,
    model: str = config.COMPRESSION_MODEL,
) -> List[dict]:
    """
    Chunk and compress a single LongBench document.

    Each chunk is saved as an individual JSONL file in *output_dir* and
    the list of result dicts is returned.
    """
    if client is None:
        client = get_openai_client()
    if system_prompt is None:
        system_prompt = load_prompt("compression_v5.txt")

    doc_id = doc.get("_id", "unknown")
    context = doc.get("context") or doc.get("source", "")
    if not context:
        logger.warning("Document %s has no context — skipping.", doc_id)
        return []

    chunks = chunk_text(context, max_words=config.CHUNK_MAX_WORDS)
    if len(chunks) > max_chunks:
        logger.info(
            "Document %s has %d chunks (> %d) — skipping.", doc_id, len(chunks), max_chunks,
        )
        return []

    results: List[dict] = []
    for idx, chunk in enumerate(chunks):
        compressed = compress_text(chunk, client, model, system_prompt)
        if not compressed:
            continue

        stats = calculate_token_compression(chunk, compressed)
        record = {
            "_id": doc_id,
            "chunk_id": idx,
            "chunk": chunk,
            "compressed_context": compressed,
            **stats,
        }
        results.append(record)

        # Persist per-chunk file
        out_path = output_dir / f"compressed_longbench_{doc_id}_{idx}.jsonl"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    logger.info("Document %s: compressed %d/%d chunks.", doc_id, len(results), len(chunks))
    return results


# ------------------------------------------------------------------
# Full pipeline
# ------------------------------------------------------------------

def run_sync_pipeline(
    output_dir: Path,
    *,
    max_chunks: int = config.MAX_CHUNKS_SYNC,
    n_samples: Optional[int] = None,
    resume: bool = True,
) -> None:
    """
    Run the full synchronous compression pipeline on LongBench-v2.

    Parameters
    ----------
    output_dir : Path
        Directory to store compressed JSONL files.
    max_chunks : int
        Skip documents with more chunks than this.
    n_samples : int, optional
        Process only this many documents (for testing).
    resume : bool
        If True, skip documents whose output files already exist.
    """
    client = get_openai_client()
    system_prompt = load_prompt("compression_v5.txt")
    docs = load_longbench()

    if n_samples is not None:
        docs = docs[:n_samples]

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for doc in tqdm(docs, desc="Compressing"):
        doc_id = doc.get("_id", "unknown")

        if resume:
            existing = list(output_dir.glob(f"compressed_longbench_{doc_id}_*.jsonl"))
            if existing:
                logger.debug("Skipping %s — already processed.", doc_id)
                continue

        compress_document(
            doc,
            output_dir,
            system_prompt=system_prompt,
            max_chunks=max_chunks,
            client=client,
            model=config.COMPRESSION_MODEL,
        )
