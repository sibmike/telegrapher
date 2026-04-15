#!/usr/bin/env python3
"""
CLI: Analyze benchmark errors — cases where compression caused failures.

Usage:
    python -m cli.errors --input-dir benchmark_key --output-file errors_key.md
    python -m cli.errors --input-dir benchmark_key --output-file errors_key.md \
                         --copy-to error_files --compressed-dir compressed_output
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze cases where compression degraded model answers.",
    )
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-file", type=Path, required=True)
    parser.add_argument(
        "--copy-to",
        type=Path,
        default=None,
        help="Copy error files to this directory.",
    )
    parser.add_argument(
        "--compressed-dir",
        type=Path,
        default=None,
        help="Include original + compressed text from this directory.",
    )
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    from telegrapher.benchmark.error_analysis import aggregate_error_files

    result = aggregate_error_files(
        args.input_dir,
        args.output_file,
        copy_to_dir=args.copy_to,
        compressed_output_dir=args.compressed_dir,
    )

    print(f"\nTotal items:  {result['total']}")
    print(f"Errors:       {result['errors']}")
    print(f"Failure rate: {result['rate_pct']:.2f}%")
    print(f"Report saved: {args.output_file}")


if __name__ == "__main__":
    main()
