"""
Compression-agnostic evaluation harness.

Users provide a `compress_fn(original_text: str) -> compressed_text: str` and
pick a suite (`"key_facts"` or `"fine_facts"`). The harness:

  1. Loads the frozen QA JSONL from `benchmark/data/`.
  2. For each item, looks up the original chunk from LongBench-v2.
  3. Calls `compress_fn` on the chunk.
  4. Asks an MC model (default `gpt-4.1-nano`) to pick the correct choice
     given the compressed context.
  5. Reports per-item correctness + aggregate accuracy.

The harness depends on `code/` at import time because it reuses the
`ask_mc`, `load_prompt`, and LongBench loader utilities there. Run from
the repo root so both `code` and `benchmark` are importable.
"""
from __future__ import annotations

import csv
import json
import logging
import sys
from pathlib import Path
from typing import Callable, Iterator, Literal, Optional

# Make sibling `code/` importable when running from repo root.
_REPO = Path(__file__).resolve().parent.parent.parent
_CODE = _REPO / "code"
if str(_CODE) not in sys.path:
    sys.path.insert(0, str(_CODE))

import config  # noqa: E402  (from code/)
from telegrapher.benchmark.mc_evaluation import ask_mc  # noqa: E402
from telegrapher.clients import get_openai_client  # noqa: E402

logger = logging.getLogger(__name__)

Suite = Literal["key_facts", "fine_facts"]


def load_suite(suite: Suite, data_dir: Optional[Path] = None) -> list[dict]:
    """Load the frozen JSONL test set for a suite."""
    data_dir = data_dir or (_REPO / "benchmark" / "data")
    path = data_dir / f"{suite}.jsonl"
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def _load_longbench_chunks() -> dict[str, list[str]]:
    """
    Load LongBench-v2 and return a mapping doc_id -> list of 1000-word chunks.

    Imported lazily because the dataset download is heavy and only needed
    when `compress_fn` wants the original chunk text.
    """
    from telegrapher.data.longbench import load_longbench  # noqa: E402
    from telegrapher.chunking import chunk_text  # noqa: E402

    docs = load_longbench(filter_qa_categories=True)
    out: dict[str, list[str]] = {}
    for d in docs:
        out[d["_id"]] = chunk_text(d["context"], max_words=config.CHUNK_MAX_WORDS)
    return out


def run_benchmark(
    compress_fn: Callable[[str], str],
    suite: Suite = "key_facts",
    mc_model: Optional[str] = None,
    limit: Optional[int] = None,
    output_path: Optional[Path] = None,
    chunks: Optional[dict[str, list[str]]] = None,
    progress: bool = True,
) -> dict:
    """
    Run the benchmark with a user-provided compression function.

    Parameters
    ----------
    compress_fn
        A function that takes the original chunk text and returns a compressed
        string. Use `benchmark.harness.identity` as a sanity check.
    suite
        Either "key_facts" (4,080 QA pairs) or "fine_facts" (801 QA pairs).
    mc_model
        OpenAI model used for multiple-choice answering. Defaults to
        `gpt-4.1-nano` (cheapest and most commonly cited in the paper).
    limit
        Optional cap on number of items to evaluate — useful for smoke runs.
    output_path
        If provided, writes per-item results as CSV to this path.
    chunks
        Optional pre-loaded {doc_id: [chunk, ...]} dict. Pass this in when
        running multiple benchmarks back-to-back to avoid reloading LongBench.
    progress
        Print a small progress counter every 50 items.

    Returns
    -------
    dict
        {"accuracy": float, "n": int, "correct": int, "suite": str, ...}
    """
    items = load_suite(suite)
    if limit is not None:
        items = items[:limit]

    if chunks is None:
        chunks = _load_longbench_chunks()

    client = get_openai_client()
    model = mc_model or "gpt-4.1-nano"

    per_item: list[dict] = []
    correct = 0
    missing = 0

    for i, item in enumerate(items):
        doc_id = item["longbench_doc_id"]
        doc_chunks = chunks.get(doc_id)
        if not doc_chunks:
            missing += 1
            continue
        # Match the chunk by original token count when available, else first.
        original = doc_chunks[0]
        if len(doc_chunks) > 1 and item.get("original_tokens"):
            # Pick the chunk whose token count is closest to original_tokens.
            from telegrapher.tokens import count_tokens  # noqa: E402
            target = item["original_tokens"]
            original = min(
                doc_chunks,
                key=lambda c: abs(count_tokens(c) - target),
            )

        compressed = compress_fn(original)
        predicted = ask_mc(
            context=compressed,
            question=item["question"],
            choices=item["choices"],
            client=client,
            model=model,
        )
        is_correct = predicted == item["gold_idx"]
        correct += int(is_correct)
        per_item.append({
            "qid": item["qid"],
            "gold_idx": item["gold_idx"],
            "predicted_idx": predicted,
            "correct": is_correct,
        })
        if progress and (i + 1) % 50 == 0:
            logger.info("  %s/%s  acc=%.3f", i + 1, len(items), correct / (i + 1 - missing))

    n = len(per_item)
    summary = {
        "suite": suite,
        "mc_model": model,
        "n": n,
        "correct": correct,
        "accuracy": correct / n if n else 0.0,
        "missing_chunks": missing,
    }

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["qid", "gold_idx", "predicted_idx", "correct"])
            w.writeheader()
            w.writerows(per_item)
    return summary
