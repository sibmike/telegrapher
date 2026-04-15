#!/usr/bin/env python3
"""
CLI: Compress LongBench-v2 documents into Telegraph English.

Usage:
    python -m cli.compress --mode sync --output-dir compressed_output
    python -m cli.compress --mode batch --output-dir compressed_output --mapping batch_mapping.json
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compress LongBench-v2 documents into Telegraph English.",
    )
    parser.add_argument(
        "--mode",
        choices=["sync", "batch"],
        default="sync",
        help="Compression mode: sync (sequential) or batch (OpenAI Batch API).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory to store compressed JSONL files.",
    )
    parser.add_argument(
        "--max-chunks",
        type=int,
        default=None,
        help="Max chunks per document (default: 55 for sync, 5 for batch).",
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=None,
        help="Process only the first N documents (for testing).",
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path("doc_batch_mapping.json"),
        help="Batch mapping file for resume (batch mode only).",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Do not skip already-processed documents.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    if args.mode == "sync":
        from telegrapher.compression.sync import run_sync_pipeline

        max_chunks = args.max_chunks or config.MAX_CHUNKS_SYNC
        run_sync_pipeline(
            args.output_dir,
            max_chunks=max_chunks,
            n_samples=args.n_samples,
            resume=not args.no_resume,
        )
    else:
        from telegrapher.compression.batch import run_batch_pipeline

        max_chunks = args.max_chunks or config.MAX_CHUNKS_BATCH
        run_batch_pipeline(
            args.output_dir,
            args.mapping,
            max_chunks=max_chunks,
            n_samples=args.n_samples,
        )


if __name__ == "__main__":
    main()
