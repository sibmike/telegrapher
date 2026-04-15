"""
Trivial non-ML compression baselines. Useful as calibration points:

  * `identity` sets the upper bound (no compression -> full accuracy).
  * `truncate_head` / `truncate_tail` are lossy baselines that any serious
    compressor must beat.
  * `random_sample` is a naive token-dropout baseline at a target ratio.

Each baseline is a pure function `str -> str`. To pass parameters, use
`functools.partial` or a closure, e.g.:

    from functools import partial
    compress = partial(truncate_head, ratio=0.5)
    run_benchmark(compress, suite="key_facts")
"""
from __future__ import annotations

import random
import re


def identity(text: str) -> str:
    """No-op baseline. Upper bound on MC accuracy for this setup."""
    return text


def _word_tokens(text: str) -> list[str]:
    # Whitespace + punctuation-preserving split, good enough for baselines.
    return re.findall(r"\S+\s*", text)


def truncate_head(text: str, ratio: float = 0.5) -> str:
    """Keep the first `ratio` fraction of whitespace tokens."""
    toks = _word_tokens(text)
    keep = max(1, int(len(toks) * ratio))
    return "".join(toks[:keep])


def truncate_tail(text: str, ratio: float = 0.5) -> str:
    """Keep the last `ratio` fraction of whitespace tokens."""
    toks = _word_tokens(text)
    keep = max(1, int(len(toks) * ratio))
    return "".join(toks[-keep:])


def random_sample(text: str, ratio: float = 0.5, seed: int = 0) -> str:
    """Randomly keep `ratio` fraction of whitespace tokens (deterministic per seed)."""
    toks = _word_tokens(text)
    rng = random.Random(seed)
    keep_n = max(1, int(len(toks) * ratio))
    idxs = sorted(rng.sample(range(len(toks)), keep_n))
    return "".join(toks[i] for i in idxs)
