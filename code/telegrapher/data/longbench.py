"""
Dataset loading and filtering for LongBench-v2.

Loads the THUDM/LongBench-v2 dataset and filters to the categories
used in the Telegrapher benchmarks.
"""

from __future__ import annotations

import logging
from typing import Optional, Set

from datasets import load_dataset

import config

logger = logging.getLogger(__name__)


def load_longbench(
    categories: Optional[Set[str]] = None,
) -> list[dict]:
    """
    Load LongBench-v2 and filter to the specified QA categories.

    Parameters
    ----------
    categories : set of str, optional
        Category names to keep.  Defaults to
        :data:`config.ALLOWED_CATEGORIES`.

    Returns
    -------
    list of dict
        Filtered records.  Each dict contains at least ``_id``,
        ``context``, ``domain``, ``sub_domain``, ``question``, etc.
    """
    cats = categories or config.ALLOWED_CATEGORIES

    logger.info(
        "Loading dataset %s (split=%s) …", config.DATASET_NAME, config.DATASET_SPLIT,
    )
    ds = load_dataset(config.DATASET_NAME, split=config.DATASET_SPLIT)

    filtered = [
        row for row in ds
        if row.get("domain") in cats or row.get("sub_domain") in cats
    ]

    logger.info(
        "Loaded %d records, filtered to %d matching categories %s",
        len(ds), len(filtered), cats,
    )
    return filtered
