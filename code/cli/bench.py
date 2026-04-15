#!/usr/bin/env python3
"""
CLI: Run QA benchmark on compressed text.

Usage:
    python -m cli.bench --variant key --input-dir compressed_output --output-dir benchmark_key
    python -m cli.bench --variant fine --input-dir compressed_output --output-dir benchmark_fine --limit 800
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
        description="Run QA benchmark on original vs. compressed text.",
    )
    parser.add_argument(
        "--variant",
        choices=["key", "fine"],
        default="key",
        help="Benchmark variant: 'key' (headline facts) or 'fine' (adversarial details).",
    )
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--mc-model",
        default=None,
        help="MC answering model (default: per-variant default).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process at most N files.",
    )
    parser.add_argument("--seed", type=int, default=config.SEED)
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    from telegrapher.benchmark.qa_bench import run_qa_benchmark

    df = run_qa_benchmark(
        args.input_dir,
        args.output_dir,
        variant=args.variant,
        mc_model=args.mc_model,
        limit=args.limit,
        seed=args.seed,
    )

    if not df.empty:
        csv_path = args.output_dir / f"benchmark_{args.variant}.csv"
        df.to_csv(csv_path, index=False)
        print(f"\nResults saved to {csv_path}")
        print(f"Total: {len(df)}")
        print(f"Original accuracy: {(df['gold_idx'] == df['orig_idx']).mean():.4f}")
        print(f"TE accuracy:       {(df['gold_idx'] == df['te_idx_mc_model']).mean():.4f}")


if __name__ == "__main__":
    main()
