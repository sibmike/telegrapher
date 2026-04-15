"""Compression-agnostic evaluation harness for the key_facts / fine_facts suites."""
from .evaluate import run_benchmark, load_suite
from .baselines import identity, truncate_head, truncate_tail, random_sample

__all__ = [
    "run_benchmark",
    "load_suite",
    "identity",
    "truncate_head",
    "truncate_tail",
    "random_sample",
]
