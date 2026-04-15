"""
Multiple-choice evaluation — shared across all benchmark variants.

Extracted from the identical ``ask_mc`` implementations in
qa_bench_key.ipynb, qa_bench_fine.ipynb, qa_llml2.ipynb.
"""

from __future__ import annotations

import logging
import re
from typing import List

import config
from telegrapher.api_utils import api_call_with_retry
from telegrapher.io_utils import load_prompt

logger = logging.getLogger(__name__)

# Word-to-number fallback map
_WORD_NUMBERS = {
    "zero": 0, "one": 1, "first": 1,
    "two": 2, "second": 2,
    "three": 3, "third": 3,
}


def ask_mc(
    context: str,
    question: str,
    choices: List[str],
    client,
    model: str,
) -> int:
    """
    Ask *model* to pick the best answer from *choices* given *context*.

    Returns the integer index of the selected choice (0-based).
    Falls back to ``0`` on failure.
    """
    formatted_choices = "\n".join(f"{i}. {c}" for i, c in enumerate(choices))
    max_idx = len(choices) - 1

    prompt = load_prompt(
        "mc_selection.txt",
        variables={
            "max_idx": str(max_idx),
            "context": context,
            "question": question,
            "formatted_choices": formatted_choices,
        },
    )

    response = api_call_with_retry(
        client.chat.completions.create,
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=config.TEMPERATURE_MC,
    )

    if response is None:
        return 0

    try:
        content = response.choices[0].message.content.strip()

        # Try regex first
        m = re.search(r"\d+", content)
        if m:
            idx = int(m.group(0))
        else:
            # Word-number fallback
            lower = content.lower()
            idx = 0
            for word, num in _WORD_NUMBERS.items():
                if word in lower:
                    idx = num
                    break

        return idx if 0 <= idx <= max_idx else 0

    except Exception as exc:
        logger.warning("Failed to parse MC answer: %s", exc)
        return 0
