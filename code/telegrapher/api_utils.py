"""
Shared API helpers — retry logic and LLM response parsing.

Consolidates the 4+ slightly-different retry wrappers and 6+ JSON-parsing
blocks from the original notebooks into two robust, shared implementations.
"""

from __future__ import annotations

import json
import logging
import re
import time
from typing import Any, Callable, List, Optional

import config

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Retry wrapper
# ---------------------------------------------------------------------------

def api_call_with_retry(
    func: Callable[..., Any],
    *args: Any,
    max_retries: Optional[int] = None,
    retry_delay: Optional[float] = None,
    **kwargs: Any,
) -> Any:
    """
    Call *func* with exponential back-off.

    On the last failed attempt the exception is logged and ``None`` is
    returned so that callers can degrade gracefully.
    """
    retries = max_retries if max_retries is not None else config.MAX_RETRIES
    delay = retry_delay if retry_delay is not None else config.RETRY_DELAY

    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            wait = delay * (attempt + 1)
            if attempt < retries - 1:
                logger.warning(
                    "Attempt %d/%d failed (%s). Retrying in %.1fs ...",
                    attempt + 1, retries, exc, wait,
                )
                time.sleep(wait)
            else:
                logger.error(
                    "API call failed after %d attempts: %s", retries, exc,
                )
    return None


# ---------------------------------------------------------------------------
# JSON response parsing
# ---------------------------------------------------------------------------

def _strip_code_fence(content: str) -> str:
    """Remove markdown code fences (```json ... ``` or ``` ... ```)."""
    m = re.search(r"```(?:json)?\s*(.*?)\s*```", content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return content.strip()


def parse_json_response(content: str) -> Optional[dict]:
    """
    Best-effort extraction of a JSON **object** from an LLM response.

    Handles markdown code fences, leading/trailing junk, and control chars.
    Returns ``None`` on failure.
    """
    text = _strip_code_fence(content)

    # Find outermost { ... }
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        logger.warning("No JSON object found in response: %.120s", text)
        return None

    candidate = text[start : end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as exc:
        logger.warning("JSON parse error: %s — content: %.200s", exc, candidate)
        return None


def parse_json_array_response(content: str) -> Optional[List[Any]]:
    """
    Best-effort extraction of a JSON **array** from an LLM response.

    Returns ``None`` on failure.
    """
    text = _strip_code_fence(content)

    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1 or end <= start:
        logger.warning("No JSON array found in response: %.120s", text)
        return None

    candidate = text[start : end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as exc:
        logger.warning("JSON array parse error: %s — content: %.200s", exc, candidate)
        return None
