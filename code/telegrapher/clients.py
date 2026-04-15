"""
API client factories for OpenAI and Anthropic.

Reads credentials from config (environment variables) and returns
configured client instances.
"""

from __future__ import annotations

import logging

import config

logger = logging.getLogger(__name__)


def get_openai_client():
    """
    Return a configured :class:`openai.OpenAI` client.

    Raises :class:`ValueError` if ``OPENAI_API_KEY`` is not set.
    """
    import openai

    if not config.OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Export it as an environment variable or add it to your .env file."
        )
    return openai.OpenAI(api_key=config.OPENAI_API_KEY)


def get_anthropic_client():
    """
    Return a configured :class:`anthropic.Anthropic` client.

    Raises :class:`ValueError` if ``ANTHROPIC_API_KEY`` is not set.
    """
    from anthropic import Anthropic

    if not config.ANTHROPIC_API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY is not set. "
            "Export it as an environment variable or add it to your .env file."
        )
    return Anthropic(api_key=config.ANTHROPIC_API_KEY)
