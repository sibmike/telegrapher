"""
Error analysis — aggregates cases where compression caused failures.

Identifies benchmark items where the model answered correctly on
original text but incorrectly on compressed text, and generates
a detailed markdown report.  Extracted from errors.ipynb.
"""

from __future__ import annotations

import json
import logging
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


def aggregate_error_files(
    input_dir: Path,
    output_file: Path,
    *,
    copy_to_dir: Optional[Path] = None,
    compressed_output_dir: Optional[Path] = None,
) -> dict:
    """
    Find benchmark items where compression caused answer degradation.

    An **error** is defined as:
    ``gold_idx == orig_idx`` (correct on original)  AND
    ``gold_idx != te_idx_mc_model`` (wrong on compressed).

    Parameters
    ----------
    input_dir : Path
        Directory containing benchmark JSONL result files.
    output_file : Path
        Path for the markdown error report.
    copy_to_dir : Path, optional
        If given, copy error JSONL files here.
    compressed_output_dir : Path, optional
        If given, include original + compressed text in the report
        (looked up by filename from this directory).

    Returns
    -------
    dict
        ``{"total": int, "errors": int, "rate_pct": float}``
    """
    input_dir = Path(input_dir)
    output_file = Path(output_file)

    if copy_to_dir:
        Path(copy_to_dir).mkdir(parents=True, exist_ok=True)

    file_paths = sorted(input_dir.glob("*.jsonl"))
    logger.info("Found %d files to scan for errors.", len(file_paths))

    total = 0
    error_count = 0
    error_items: List[dict] = []

    for fp in file_paths:
        try:
            with open(fp, "r", encoding="utf-8") as fh:
                for line in fh:
                    data = json.loads(line.strip())
                    total += 1

                    gold = data.get("gold_idx")
                    orig = data.get("orig_idx")
                    te = data.get("te_idx_mc_model")

                    if gold == orig and gold != te:
                        error_count += 1

                        if copy_to_dir:
                            dest = Path(copy_to_dir) / fp.name
                            shutil.copy2(fp, dest)

                        item = {
                            "id": data.get("id"),
                            "file": fp.name,
                            "question": data.get("question"),
                            "verbatim_answer": data.get("verbatim_answer"),
                            "modified_answer": data.get("modified_answer"),
                            "choices": data.get("choices", []),
                            "gold_idx": gold,
                            "orig_idx": orig,
                            "te_idx_mc_model": te,
                        }

                        # Optionally look up original + compressed text
                        if compressed_output_dir:
                            comp_file = Path(compressed_output_dir) / fp.name
                            if comp_file.exists():
                                with open(comp_file, "r", encoding="utf-8") as cf:
                                    cdata = json.loads(cf.readline())
                                    item["original_text"] = cdata.get("chunk", "")
                                    item["compressed_text"] = cdata.get("compressed_context", "")

                        error_items.append(item)
        except Exception as exc:
            logger.error("Error processing %s: %s", fp.name, exc)

    # Write markdown report
    rate_pct = (error_count / total * 100) if total > 0 else 0.0
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# QA Error Analysis\n\n")
        f.write(f"Total files processed: {total}\n")
        f.write(f"Files with errors: {error_count} ({rate_pct:.2f}% failure rate)\n\n")

        for i, err in enumerate(error_items, 1):
            f.write(f"## Error {i}: {err['id']}\n\n")
            f.write(f"Source file: {err['file']}\n\n")
            f.write(f"### Question\n{err['question']}\n\n")
            f.write(f"### Original Answer (Correct)\n{err['verbatim_answer']}\n\n")
            f.write(f"### Modified/Compressed Answer\n{err['modified_answer']}\n\n")

            if "original_text" in err:
                f.write(f"### Original Text\n{err['original_text']}\n\n")
            if "compressed_text" in err:
                f.write(f"### Compressed Text\n{err['compressed_text']}\n\n")

            f.write("### Multiple Choice Options\n")
            for j, choice in enumerate(err["choices"]):
                if j == err["gold_idx"]:
                    marker = "\u2713"
                elif j == err["te_idx_mc_model"]:
                    marker = "\u274c"
                else:
                    marker = " "
                f.write(f"{j}. [{marker}] {choice}\n")
            f.write("\n")

            f.write(f"gold_idx: {err['gold_idx']}\n")
            f.write(f"orig_idx: {err['orig_idx']}\n")
            f.write(f"te_idx_mc_model: {err['te_idx_mc_model']}\n\n")
            f.write("---\n\n")

    logger.info(
        "Error analysis complete: %d errors in %d items (%.2f%%).",
        error_count, total, rate_pct,
    )
    return {"total": total, "errors": error_count, "rate_pct": round(rate_pct, 2)}
