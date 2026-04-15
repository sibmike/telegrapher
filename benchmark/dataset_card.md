# CKPB Dataset Card

## Overview

**Name.** Compression Knowledge-Preservation Benchmark (CKPB) — dual-suite MC QA for measuring factual preservation under text compression.

**Version.** 1.0 (May 2025).

**Format.** Two JSONL files in `benchmark/data/`.

| Suite | File | Rows |
|---|---|---|
| `key_facts` | `key_facts.jsonl` | 4,080 |
| `fine_facts` | `fine_facts.jsonl` | 801 |

## Source

QA pairs are generated from chunks of [LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2) (Bai et al., 2024), filtered to three QA-suitable categories: Single-Document QA, Multi-Document QA, and Long-Dialogue History Understanding. Of 503 source documents, 339 pass the filter; chunking at max 1,000 NLTK-sentence-tokenised words yields 4,081 chunks.

LongBench-v2 chunk text is **not** redistributed in this repo. The JSONL files include `longbench_doc_id` and `original_tokens` to enable chunk lookup against the upstream dataset.

## Generation

- **QA generation model.** `gpt-4.1`, temperature 0.7.
- **QA generation prompts.** [`prompts/qa_generation_key.txt`](prompts/qa_generation_key.txt), [`prompts/qa_generation_fine.txt`](prompts/qa_generation_fine.txt).
- **Distractor generation model.** `gpt-4.1`, temperature 0.7, 3 distractors per question.
- **Distractor prompts.** [`prompts/distractor_key.txt`](prompts/distractor_key.txt) (generic), [`prompts/distractor_fine.txt`](prompts/distractor_fine.txt) (near-miss variants).
- **Each QA pair.** One question, one verbatim answer, one "modified_answer" (semantically identical, lexically distinct — not used in the current MC evaluation but retained for future metrics), three distractors, shuffled; `gold_idx` marks the correct choice's index after shuffling.

## Suite design

**key_facts** targets core concepts, headline findings, and main claims. Distractors are generically plausible. Intent: measure whether the *gist* of the original text survives compression.

**fine_facts** is designed as an adversarial probe for lossy compression. The generation prompt instructs the model to target *information that is both non-negligible and likely to be dropped by lossy compressors*: precise numerical qualifiers, conditional statements, caveats, boundary conditions. Distractors are *near-miss* variants — numbers nudged by one decimal, qualifiers slightly reworded, units swapped — that can only be correctly eliminated with access to the exact original detail. Intent: measure whether *detail* survives.

## Known biases and limitations

1. **Single-model QA generation.** All QA pairs are produced by GPT-4.1. This introduces systematic patterns and likely biases the difficulty distribution. A future version should either (a) mix multiple generator models or (b) include a human-authored subset.
2. **Evaluation stack is OpenAI-only.** The current reference results use `gpt-4.1`, `gpt-4.1-nano`, `gpt-4o`, and `gpt-4o-mini` as MC models. Reproducibility requires OpenAI API access. Porting the harness to open-weight models is listed as future work.
3. **Question-generation-from-uncompressed bias.** QA pairs are generated from the uncompressed chunk. This explicitly frames compression fidelity as the benchmark's primary axis — correct, but it means CKPB does not measure other compression desiderata (latency, memory, pipeline compatibility).
4. **English only.** Grammar, prompts, distractors, and source documents are all English.
5. **MC vs generative.** Scoring is multiple-choice-accuracy; it does not measure free-form answer quality.
6. **Size asymmetry.** `key_facts` is ~5× larger than `fine_facts`. When comparing compressors, compare per-suite, not averaged.

## Reproducibility

- The prompts in [`prompts/`](prompts/) are the exact generation prompts.
- `original_tokens` in each JSONL row is the tiktoken count of the source chunk under `cl100k_base`, enabling deterministic chunk matching.
- LongBench-v2 upstream is versioned and publicly available.

## License

- **QA data (both JSONL files) and generation prompts:** CC-BY-SA 4.0 (see [`../LICENSE-docs`](../LICENSE-docs)).
- **Source chunks:** not included. Fetch from [LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2) under its own license (MIT).
- **Harness code:** MIT (see [`../LICENSE`](../LICENSE)).

## Citation

See [`README.md`](README.md#citation).
