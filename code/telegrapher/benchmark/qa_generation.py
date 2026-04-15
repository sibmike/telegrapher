"""
QA pair generation — KEY and FINE variants.

Generates a (question, verbatim_answer, modified_answer) triple from a
passage using the appropriate prompt template.
"""

from __future__ import annotations

import logging
from typing import Tuple

import config
from telegrapher.api_utils import api_call_with_retry, parse_json_response
from telegrapher.io_utils import load_prompt

logger = logging.getLogger(__name__)

_FALLBACK = (
    "What is mentioned in the passage?",
    "Information about the topic",
    "Information presented in the text",
)


def create_qa(
    passage: str,
    client,
    model: str = config.QA_MODEL,
    variant: str = "key",
) -> Tuple[str, str, str]:
    """
    Generate a QA pair from *passage*.

    Parameters
    ----------
    passage : str
        The source text to generate a question from.
    client
        An OpenAI client instance.
    model : str
        Model to use for generation.
    variant : str
        ``"key"`` for generic factual questions,
        ``"fine"`` for adversarial detail-targeting questions.

    Returns
    -------
    tuple of (question, verbatim_answer, modified_answer)
    """
    prompt = load_prompt(
        f"qa_generation_{variant}.txt",
        variables={"passage": passage},
    )

    response = api_call_with_retry(
        client.chat.completions.create,
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=config.TEMPERATURE_QA,
    )

    if response is None:
        return _FALLBACK

    content = response.choices[0].message.content
    obj = parse_json_response(content)

    if obj is None:
        logger.warning("Failed to parse QA response.")
        return _FALLBACK

    question = obj.get("question", _FALLBACK[0])
    answer = obj.get("answer", _FALLBACK[1])
    modified = obj.get("modified_answer")
    if not modified:
        modified = "Alternate version: " + answer

    return question, answer, modified
