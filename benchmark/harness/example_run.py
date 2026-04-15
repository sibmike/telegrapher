"""
Minimal end-to-end smoke test.

Runs the `identity` baseline (no compression) on the first 10 items of the
key_facts suite. Expected accuracy: very close to 1.0 — if it isn't, something
is wrong with the MC model, the chunk lookup, or the QA pairs.

Requires OPENAI_API_KEY. Run from the repo root:

    python -m benchmark.harness.example_run
"""
from __future__ import annotations

import logging
import os

from .baselines import identity
from .evaluate import run_benchmark

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set. Skipping live smoke test.")
        return

    summary = run_benchmark(
        compress_fn=identity,
        suite="key_facts",
        limit=10,
    )
    print(summary)


if __name__ == "__main__":
    main()
