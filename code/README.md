# Telegrapher AI — Code

Structured codebase for the Telegraph English compression and benchmarking pipeline.
Extracted and refactored from the original Jupyter notebooks.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API keys
cp .env.example .env
# Edit .env with your actual keys

# 3. Run compression
python -m cli.compress --mode sync --output-dir compressed_output

# 4. Run QA benchmark
python -m cli.bench --variant key --input-dir compressed_output --output-dir benchmark_key

# 5. Analyze errors
python -m cli.errors --input-dir benchmark_key --output-file errors.md
```

## Project Structure

```
code/
├── config.py                      # All constants, model IDs, env var loading
├── prompts/                       # Telegraph English prompts
│   ├── compression_v5.txt         # TE compression system prompt
│   └── review.txt                 # Claude quality review
│   # Benchmark prompts (qa_generation_*, distractor_*, mc_selection) live in
│   # ../benchmark/prompts/. load_prompt() transparently resolves both.
├── telegrapher/                   # Core library
│   ├── clients.py                 # OpenAI + Anthropic client factories
│   ├── tokens.py                  # tiktoken counting + compression stats
│   ├── chunking.py                # NLTK sentence-based text chunking
│   ├── api_utils.py               # Retry wrapper, JSON response parsing
│   ├── io_utils.py                # JSONL I/O, prompt loading, file merging
│   ├── compression/
│   │   ├── sync.py                # Sequential compression via Chat API
│   │   └── batch.py               # Async compression via Batch API
│   ├── review/
│   │   └── reviewer.py            # Claude-based quality review + scoring
│   ├── benchmark/
│   │   ├── mc_evaluation.py       # Shared MC answer evaluation
│   │   ├── qa_generation.py       # QA pair generation (key + fine)
│   │   ├── distractors.py         # Distractor generation (key + fine)
│   │   ├── qa_bench.py            # QA benchmark orchestrator
│   │   ├── llml2_eval.py          # LLMLingua2 comparison evaluation
│   │   └── error_analysis.py      # Error aggregation + markdown reports
│   └── data/
│       └── longbench.py           # LongBench-v2 dataset loading
└── cli/                           # Command-line entry points
    ├── compress.py                # python -m cli.compress
    ├── review.py                  # python -m cli.review
    ├── bench.py                   # python -m cli.bench
    ├── eval_llml2.py              # python -m cli.eval_llml2
    └── errors.py                  # python -m cli.errors
```

## CLI Commands

### Compress

```bash
# Synchronous (one chunk at a time)
python -m cli.compress --mode sync --output-dir compressed_output --max-chunks 55

# Batch API (async, cheaper)
python -m cli.compress --mode batch --output-dir compressed_output --mapping batch_map.json
```

### Review (via Claude)

```bash
# Run quality reviews
python -m cli.review run --input-dir compressed_output --output-dir reviews

# Aggregate scores
python -m cli.review analyze --review-dir reviews
```

### QA Benchmark

```bash
# Key facts (headline concepts, 4081 QA pairs)
python -m cli.bench --variant key --input-dir compressed_output --output-dir benchmark_key

# Fine facts (adversarial details, typically 800 sample)
python -m cli.bench --variant fine --input-dir compressed_output --output-dir benchmark_fine --limit 800
```

### LLMLingua2 Evaluation

```bash
python -m cli.eval_llml2 --compressed-dir compressed_llml2_50 \
                         --qa-dir benchmark_key \
                         --output-dir benchmark_llml2_50
```

### Error Analysis

```bash
python -m cli.errors --input-dir benchmark_key \
                     --output-file errors.md \
                     --copy-to error_files \
                     --compressed-dir compressed_output
```

## Configuration

All settings are in `config.py`. Key values:

| Setting | Default | Description |
|---------|---------|-------------|
| `COMPRESSION_MODEL` | `o4-mini-2025-04-16` | Model for TE compression |
| `QA_MODEL` | `gpt-4.1` | Model for QA generation |
| `MC_MODEL_KEY` | `gpt-4.1-nano` | MC model for key_facts benchmark |
| `MC_MODEL_FINE` | `gpt-4o-mini-2024-07-18` | MC model for fine_facts benchmark |
| `LLML2_MC_MODEL` | `gpt-4o-2024-08-06` | MC model for LLMLingua2 eval |
| `REVIEW_MODEL` | `claude-3-7-sonnet-20250219` | Claude model for quality review |
| `CHUNK_MAX_WORDS` | `1000` | Max words per chunk |
| `N_WRONG` | `3` | Number of distractor answers |
| `MAX_RETRIES` | `3` | API retry attempts |

## Deduplication from Notebooks

| Function | Notebook copies | Now in |
|----------|----------------|--------|
| `ask_mc` | 4 (key, fine, llml2, errors) | `benchmark/mc_evaluation.py` |
| `chunk_text` | 2 (batch_1, batch_batch_1) | `chunking.py` |
| `api_call_with_retry` | 4 | `api_utils.py` |
| JSON parsing | 6+ | `api_utils.py` (2 functions) |
| `calculate_token_compression` | 3 (batch_1, review×2) | `tokens.py` |
| `aggregate_error_files` | 3 (key, fine, errors) | `benchmark/error_analysis.py` |

## Source Notebooks → Modules Mapping

| Notebook | Module(s) |
|----------|-----------|
| `batch_1.ipynb` | `compression/sync.py`, `tokens.py`, `chunking.py` |
| `batch_batch_1.ipynb` | `compression/batch.py` |
| `review_batch_1.ipynb` | `review/reviewer.py` |
| `analysis_batch_1.ipynb` | `review/reviewer.py` (aggregate_scores) |
| `qa_bench_key.ipynb` | `benchmark/qa_bench.py`, `qa_generation.py`, `distractors.py`, `mc_evaluation.py` |
| `qa_bench_fine.ipynb` | Same modules with `variant="fine"` |
| `qa_llml2.ipynb` | `benchmark/llml2_eval.py` |
| `qa_errors.ipynb` / `errors.ipynb` | `benchmark/error_analysis.py` |
