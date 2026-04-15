#!/usr/bin/env python3
"""
CLI: Evaluate LLMLingua2-compressed text against QA benchmarks.

Usage:
    python -m cli.eval_llml2 --compressed-dir compressed_llml2_50 \
                             --qa-dir benchmark_key \
                             --output-dir benchmark_llml2_50
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate LLMLingua2 compression against QA benchmarks.",
    )
    parser.add_argument("--compressed-dir", type=Path, required=True)
    parser.add_argument("--qa-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--mc-model",
        default=None,
        help=f"MC model (default: {config.LLML2_MC_MODEL}).",
    )
    parser.add_argument(
        "--prefix",
        default="llmlingua2_",
        help="Filename prefix to strip when matching QA files.",
    )
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    from telegrapher.benchmark.llml2_eval import run_llml2_evaluation

    df = run_llml2_evaluation(
        args.compressed_dir,
        args.qa_dir,
        args.output_dir,
        mc_model=args.mc_model,
        prefix=args.prefix,
    )

    if not df.empty:
        csv_path = args.output_dir / "llml2_results.csv"
        df.to_csv(csv_path, index=False)
        print(f"\nResults saved to {csv_path}")
        print(f"Total: {len(df)}")
        print(f"Compressed accuracy: {df['compressed_correct'].mean():.4f}")


if __name__ == "__main__":
    main()
