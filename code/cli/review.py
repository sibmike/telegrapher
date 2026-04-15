#!/usr/bin/env python3
"""
CLI: Review compressed Telegraph English quality via Claude.

Usage:
    python -m cli.review --input-dir compressed_output --output-dir reviews
    python -m cli.review --analyze reviews
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Review TE compression quality via Claude.",
    )
    sub = parser.add_subparsers(dest="command")

    # --- review sub-command ---
    run_parser = sub.add_parser("run", help="Run reviews on compressed files.")
    run_parser.add_argument("--input-dir", type=Path, required=True)
    run_parser.add_argument("--output-dir", type=Path, required=True)
    run_parser.add_argument("--log-level", default="INFO")

    # --- analyze sub-command ---
    analyze_parser = sub.add_parser("analyze", help="Aggregate review scores.")
    analyze_parser.add_argument("--review-dir", type=Path, required=True)
    analyze_parser.add_argument("--log-level", default="INFO")

    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    if args.command == "run":
        from telegrapher.review.reviewer import run_review_pipeline

        run_review_pipeline(args.input_dir, args.output_dir)

    elif args.command == "analyze":
        from telegrapher.review.reviewer import aggregate_scores

        result = aggregate_scores(args.review_dir)
        print(f"Total reviews: {result['total']}")
        print(f"Scored:        {result['scored']}")
        print(f"Average score: {result['average']:.2f}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
