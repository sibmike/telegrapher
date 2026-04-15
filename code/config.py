"""
Central configuration for Telegrapher AI.

All magic numbers, model IDs, and environment-dependent values live here.
API keys are read exclusively from environment variables.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# API Keys (never hardcoded)
# ---------------------------------------------------------------------------
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY: str = os.environ.get("ANTHROPIC_API_KEY", "")

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
COMPRESSION_MODEL = "o4-mini-2025-04-16"
QA_MODEL = "gpt-4.1"
MC_MODEL_KEY = "gpt-4.1-nano"
MC_MODEL_FINE = "gpt-4o-mini-2024-07-18"
LLML2_MC_MODEL = "gpt-4o-2024-08-06"
REVIEW_MODEL = "claude-3-7-sonnet-20250219"

# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------
CHUNK_MAX_WORDS = 1000
CHUNK_OVERLAP_WORDS = 0
MAX_CHUNKS_SYNC = 55       # used by sync compression pipeline
MAX_CHUNKS_BATCH = 5       # used by batch API compression pipeline

# ---------------------------------------------------------------------------
# Token counting
# ---------------------------------------------------------------------------
TOKEN_ENCODING = "cl100k_base"
MAX_MODEL_TOKENS = 128_000

# ---------------------------------------------------------------------------
# Benchmark
# ---------------------------------------------------------------------------
N_WRONG = 3                # number of distractor answers
SEED = 42

# ---------------------------------------------------------------------------
# Retry / resilience
# ---------------------------------------------------------------------------
MAX_RETRIES = 3
RETRY_DELAY = 20.0         # base delay in seconds (multiplied by attempt)

# ---------------------------------------------------------------------------
# Temperature
# ---------------------------------------------------------------------------
TEMPERATURE_QA = 0.0
TEMPERATURE_MC = 0.0
TEMPERATURE_DISTRACTORS = 0.7
TEMPERATURE_REVIEW = 0.0

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
DATASET_NAME = "THUDM/LongBench-v2"
DATASET_SPLIT = "train"
ALLOWED_CATEGORIES = frozenset({
    "Single-Document QA",
    "Multi-Document QA",
    "Long-dialogue History Understanding",
})

# ---------------------------------------------------------------------------
# Batch API
# ---------------------------------------------------------------------------
BATCH_STATUS_CHECK_INTERVAL = 30   # seconds between status polls
MAX_TOKENS_COMPLETION = 4000

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
PROMPTS_DIR = PROJECT_ROOT / "prompts"

# Benchmark prompts (QA generation, distractors, MC selection) live in the
# standalone `benchmark/` folder at the repo root so they can be cited and
# reused independently of the Telegraph English pipeline.
REPO_ROOT = PROJECT_ROOT.parent
BENCHMARK_PROMPTS_DIR = REPO_ROOT / "benchmark" / "prompts"
BENCHMARK_DATA_DIR = REPO_ROOT / "benchmark" / "data"
