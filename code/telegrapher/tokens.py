"""
Token counting utilities.

Provides tiktoken-based token counting and compression statistics.
Extracted from batch_1.ipynb.
"""

from __future__ import annotations

import tiktoken

from config import TOKEN_ENCODING


def n_tokens(text: str) -> int:
    """Rough token estimate via word splitting (fallback when tiktoken unavailable)."""
    return len(text.split())


def calculate_token_compression(
    original_text: str,
    compressed_text: str,
    encoding_name: str = TOKEN_ENCODING,
) -> dict:
    """
    Compute token-level compression statistics.

    Returns a dict with:
        original_tokens      – token count of original text
        compressed_tokens    – token count of compressed text
        token_reduction      – absolute difference
        compression_rate_pct – percentage reduction (0-100)
        compression_ratio    – original / compressed  (e.g. 2.0 = 50% reduction)
    """
    enc = tiktoken.get_encoding(encoding_name)
    original_tokens = len(enc.encode(original_text))
    compressed_tokens = len(enc.encode(compressed_text))
    token_reduction = original_tokens - compressed_tokens

    compression_rate_pct = (
        (token_reduction / original_tokens * 100) if original_tokens > 0 else 0.0
    )
    compression_ratio = (
        (original_tokens / compressed_tokens) if compressed_tokens > 0 else float("inf")
    )

    return {
        "original_tokens": original_tokens,
        "compressed_tokens": compressed_tokens,
        "token_reduction": token_reduction,
        "compression_rate_pct": round(compression_rate_pct, 2),
        "compression_ratio": round(compression_ratio, 4),
    }
