"""
File I/O utilities — JSONL read/write, prompt loading, text merging.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from string import Template
from typing import Any, Dict, List, Optional

import config

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# JSONL
# ---------------------------------------------------------------------------

def read_jsonl(path: Path) -> List[dict]:
    """Read all records from a JSONL file."""
    records: List[dict] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl(records: List[dict], path: Path) -> None:
    """Write a list of dicts to a JSONL file (overwrites)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def append_jsonl(record: dict, path: Path) -> None:
    """Append a single record to a JSONL file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Line counting
# ---------------------------------------------------------------------------

def count_lines(path: Path) -> int:
    """Count lines in a file (for progress bars)."""
    with open(path, "r", encoding="utf-8") as fh:
        return sum(1 for _ in fh)


# ---------------------------------------------------------------------------
# Prompt loading
# ---------------------------------------------------------------------------

def load_prompt(
    name: str,
    variables: Optional[Dict[str, Any]] = None,
    prompts_dir: Optional[Path] = None,
) -> str:
    """
    Read a prompt template from *prompts_dir* / *name* and substitute
    ``$variable`` placeholders via :class:`string.Template`.

    If *variables* is ``None`` the raw text is returned unchanged.
    """
    if prompts_dir is not None:
        path = prompts_dir / name
    else:
        # Try the Telegraph English prompt dir first, then fall back to the
        # standalone benchmark prompts directory. This lets callers load any
        # prompt by name without caring which folder owns it.
        path = config.PROMPTS_DIR / name
        if not path.exists():
            fallback = config.BENCHMARK_PROMPTS_DIR / name
            if fallback.exists():
                path = fallback
    text = path.read_text(encoding="utf-8")
    if variables:
        return Template(text).safe_substitute(variables)
    return text


# ---------------------------------------------------------------------------
# Text file merging
# ---------------------------------------------------------------------------

def merge_txt_files(input_dir: Path, output_file: Path) -> int:
    """
    Concatenate all ``.txt`` files in *input_dir* into *output_file*.

    Returns the number of files merged.
    """
    txt_files = sorted(input_dir.glob("*.txt"))
    output_file.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with open(output_file, "w", encoding="utf-8") as out:
        for tf in txt_files:
            out.write(f"--- {tf.name} ---\n")
            out.write(tf.read_text(encoding="utf-8"))
            out.write("\n\n")
            count += 1

    logger.info("Merged %d text files into %s", count, output_file)
    return count
