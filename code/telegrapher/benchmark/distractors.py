"""
Distractor generation — KEY and FINE variants.

Produces plausible-but-incorrect multiple-choice alternatives for a
given question + correct answer.
"""

from __future__ import annotations

import logging
from typing import List

import config
from telegrapher.api_utils import api_call_with_retry, parse_json_array_response
from telegrapher.io_utils import load_prompt

logger = logging.getLogger(__name__)


def _fallback_distractors(n: int) -> List[str]:
    return [f"Alternative answer {i + 1}" for i in range(n)]


def create_distractors(
    question: str,
    correct_answer: str,
    client,
    model: str = config.QA_MODEL,
    n_wrong: int = config.N_WRONG,
    variant: str = "key",
) -> List[str]:
    """
    Generate *n_wrong* plausible but incorrect answers.

    Parameters
    ----------
    question : str
        The question to distract from.
    correct_answer : str
        The correct (modified) answer text.
    client
        An OpenAI client instance.
    model : str
        Model for generation.
    n_wrong : int
        Number of distractors to produce.
    variant : str
        ``"key"`` or ``"fine"`` — selects the prompt template.

    Returns
    -------
    list of str
        Exactly *n_wrong* distractor strings.
    """
    prompt = load_prompt(
        f"distractor_{variant}.txt",
        variables={
            "n_wrong": str(n_wrong),
            "question": question,
            "correct_answer": correct_answer,
        },
    )

    response = api_call_with_retry(
        client.chat.completions.create,
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=config.TEMPERATURE_DISTRACTORS,
    )

    if response is None:
        return _fallback_distractors(n_wrong)

    content = response.choices[0].message.content
    arr = parse_json_array_response(content)

    if arr is None:
        logger.warning("Failed to parse distractor array.")
        return _fallback_distractors(n_wrong)

    # Pad or trim to exactly n_wrong
    wrong = [str(a) for a in arr]
    if len(wrong) < n_wrong:
        wrong.extend(_fallback_distractors(n_wrong - len(wrong)))
    return wrong[:n_wrong]
