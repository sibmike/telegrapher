"""
Text chunking with NLTK sentence tokenisation.

Splits a document into chunks of roughly *max_words* words, respecting
sentence boundaries and tagging each chunk with a CHUNK:NNN/MMM header.
Extracted from batch_1.ipynb and batch_batch_1.ipynb.
"""

from __future__ import annotations

import logging
from typing import List

import nltk

logger = logging.getLogger(__name__)

# Ensure the punkt tokeniser data is available.
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


def chunk_text(
    text: str,
    max_words: int = 1000,
    overlap_words: int = 0,
) -> List[str]:
    """
    Split *text* into sentence-aligned chunks of at most *max_words* words.

    Each returned chunk is prefixed with a ``CHUNK:001/050`` tag.
    When *overlap_words* > 0, sentences from the tail of the previous chunk
    are prepended to the next chunk (up to *overlap_words* words).
    """
    sentences = nltk.sent_tokenize(text)
    if not sentences:
        return []

    # --- first pass: group sentences into chunks ---
    raw_chunks: List[List[str]] = []
    current_chunk: List[str] = []
    current_words = 0

    for sent in sentences:
        sent_words = len(sent.split())
        if current_words + sent_words > max_words and current_chunk:
            raw_chunks.append(current_chunk)
            # overlap: carry trailing sentences whose total ≤ overlap_words
            if overlap_words > 0:
                overlap_sents: List[str] = []
                overlap_count = 0
                for s in reversed(current_chunk):
                    s_words = len(s.split())
                    if overlap_count + s_words > overlap_words:
                        break
                    overlap_sents.insert(0, s)
                    overlap_count += s_words
                current_chunk = list(overlap_sents)
                current_words = overlap_count
            else:
                current_chunk = []
                current_words = 0
        current_chunk.append(sent)
        current_words += sent_words

    if current_chunk:
        raw_chunks.append(current_chunk)

    # --- second pass: tag each chunk ---
    total = len(raw_chunks)
    tagged: List[str] = []
    for idx, chunk_sents in enumerate(raw_chunks, start=1):
        tag = f"CHUNK:{idx:03d}/{total:03d}"
        body = " ".join(chunk_sents)
        tagged.append(f"{tag}\n{body}")

    return tagged
