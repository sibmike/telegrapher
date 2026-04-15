"""
QA benchmark orchestrator.

Processes compressed JSONL files: generates QA pairs, creates MC
choices, tests models on both original and compressed text, and
saves results.  Extracted from qa_bench_key.ipynb / qa_bench_fine.ipynb.
"""

from __future__ import annotations

import glob
import json
import logging
import os
import random
from pathlib import Path
from typing import List, Optional

import pandas as pd
from tqdm import tqdm

import config
from telegrapher.benchmark.distractors import create_distractors
from telegrapher.benchmark.mc_evaluation import ask_mc
from telegrapher.benchmark.qa_generation import create_qa
from telegrapher.clients import get_openai_client
from telegrapher.io_utils import count_lines

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Single-file processing
# ------------------------------------------------------------------

def process_single_file(
    src_file: Path,
    out_file: Path,
    client,
    *,
    variant: str = "key",
    mc_model: str = config.MC_MODEL_KEY,
    original_field: str = "chunk",
    compressed_field: str = "compressed_context",
) -> Optional[dict]:
    """
    Process one JSONL file: generate QA, distractors, run MC test.

    Returns a summary dict for the last record processed, or ``None``
    if nothing was processed.
    """
    out_file.parent.mkdir(parents=True, exist_ok=True)
    last_stats: Optional[dict] = None

    with open(src_file, "r", encoding="utf-8") as inp, \
         open(out_file, "w", encoding="utf-8") as out:

        for line_num, line in enumerate(inp):
            try:
                example = json.loads(line)

                original_text = example.get(original_field, "")
                compressed_text = example.get(compressed_field, "")
                if not original_text or not compressed_text:
                    logger.warning(
                        "%s line %d: missing %s or %s — skipping.",
                        src_file.name, line_num + 1, original_field, compressed_field,
                    )
                    continue

                # 1. Generate QA pair from original text
                question, verbatim_answer, modified_answer = create_qa(
                    original_text, client, config.QA_MODEL, variant,
                )

                # 2. Generate distractors for the modified answer
                wrong_answers = create_distractors(
                    question, modified_answer, client,
                    config.QA_MODEL, config.N_WRONG, variant,
                )

                # 3. Shuffle choices
                choices = wrong_answers + [modified_answer]
                random.shuffle(choices)
                gold_idx = choices.index(modified_answer)

                # 4. Test on original text
                orig_idx = ask_mc(original_text, question, choices, client, mc_model)

                # 5. Test on compressed text
                te_idx = ask_mc(compressed_text, question, choices, client, mc_model)

                # 6. Write result record
                record = {
                    "id": example.get("_id", f"unknown_{hash(original_text) % 10000}"),
                    "question": question,
                    "verbatim_answer": verbatim_answer,
                    "modified_answer": modified_answer,
                    "choices": choices,
                    "gold_idx": gold_idx,
                    "orig_idx": orig_idx,
                    "te_idx_mc_model": te_idx,
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")

                last_stats = {
                    "_id": example.get("_id", "unknown"),
                    "original_tokens": example.get("original_tokens", 0),
                    "compressed_tokens": example.get("compressed_tokens", 0),
                    "gold_idx": gold_idx,
                    "orig_idx": orig_idx,
                    "te_idx_mc_model": te_idx,
                }

            except Exception as exc:
                logger.error("Error on %s line %d: %s", src_file.name, line_num + 1, exc)
                continue

    return last_stats


# ------------------------------------------------------------------
# Full benchmark run
# ------------------------------------------------------------------

def run_qa_benchmark(
    input_dir: Path,
    output_dir: Path,
    *,
    variant: str = "key",
    mc_model: Optional[str] = None,
    limit: Optional[int] = None,
    seed: int = config.SEED,
) -> pd.DataFrame:
    """
    Run the QA benchmark across all JSONL files in *input_dir*.

    Parameters
    ----------
    input_dir : Path
        Directory containing compressed JSONL files.
    output_dir : Path
        Directory for benchmark result files.
    variant : str
        ``"key"`` or ``"fine"`` — controls QA/distractor prompt style.
    mc_model : str, optional
        MC answering model.  Defaults to ``MC_MODEL_KEY`` for key,
        ``MC_MODEL_FINE`` for fine.
    limit : int, optional
        Process at most *limit* files.
    seed : int
        Random seed for file ordering and choice shuffling.

    Returns
    -------
    pd.DataFrame
        Aggregated results across all processed files.
    """
    if mc_model is None:
        mc_model = config.MC_MODEL_FINE if variant == "fine" else config.MC_MODEL_KEY

    random.seed(seed)
    client = get_openai_client()

    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.jsonl"))
    random.shuffle(files)
    if limit is not None:
        files = files[:limit]

    logger.info(
        "Running QA benchmark: variant=%s, mc_model=%s, files=%d",
        variant, mc_model, len(files),
    )

    results: List[dict] = []
    for fp in tqdm(files, desc=f"Benchmark ({variant})"):
        out_file = output_dir / fp.name
        stats = process_single_file(
            fp, out_file, client,
            variant=variant, mc_model=mc_model,
        )
        if stats is not None:
            results.append(stats)

    df = pd.DataFrame(results)
    if not df.empty:
        orig_acc = (df["gold_idx"] == df["orig_idx"]).mean()
        te_acc = (df["gold_idx"] == df["te_idx_mc_model"]).mean()
        logger.info(
            "Results (%d files): original_acc=%.4f  te_acc=%.4f",
            len(df), orig_acc, te_acc,
        )
    return df
