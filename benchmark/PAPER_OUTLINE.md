# CKPB — Paper Outline (DRAFT)

> **Status.** This is a scaffolding outline for a possible standalone paper on CKPB. It is **not** a publishable draft. The current TE preprint in [`../paper/telegraph_english.md`](../paper/telegraph_english.md) cites CKPB as infrastructure; the standalone framing would be a separate contribution.

## Working title

*Measuring Knowledge Preservation in Text Compression: A Dual-Suite QA Benchmark*

## 1. Motivation

Text compression for LLMs is currently evaluated along two axes that poorly proxy what practitioners actually care about:

- **Compression ratio** — easy to measure, says nothing about whether the downstream model can still answer questions.
- **Perplexity / reconstruction loss** — a surface-form metric that penalises paraphrases and rewards verbose reconstruction.

Neither axis captures the practitioner's real question: *can the next stage in my pipeline still recover the facts it needs?* This is especially acute for agentic and multi-step pipelines, where compression is compounded and where the failure mode is not "slightly degraded output" but "wrong answer, confidently stated."

## 2. Gap in existing benchmarks

| Benchmark | Measures | Gap for compression |
|---|---|---|
| LongBench (Bai et al., 2024) | Long-context reasoning on full documents | No compression axis — measures the model, not the preprocessor |
| ZeroSCROLLS | Long-context zero-shot reasoning | Same — document-level, not preprocessor-level |
| HELM-long-context | Comprehensive LLM evaluation | Orthogonal — compressors aren't a first-class dimension |
| MeetingBank (used to train LLMLingua-2) | Transcription + summarisation | Training distribution, not a compression-fidelity benchmark |
| Perplexity on WikiText, C4 | Language modelling | Indirect; rewards surface reconstruction over factual preservation |

Nothing existing lets a researcher ask: *"my compressor hits 50% ratio — what fraction of the facts in the source did it actually keep?"*

## 3. Proposed benchmark

**Dual-suite MC QA** over LongBench-v2 chunks:

- **key_facts** (4,080 pairs) — core concepts, generic distractors. Measures gist preservation.
- **fine_facts** (801 pairs) — buried details, near-miss distractors (e.g., 4.8% ↔ 4.3%). Measures detail preservation.

A `compress_fn(str) -> str` API keeps the benchmark compression-agnostic: extractive, abstractive, rule-based, and neural methods can all be evaluated on identical items.

Core metrics:

- **Accuracy-at-ratio** — MC accuracy of an MC model given compressed context, at matched compression ratios across compressors.
- **key–fine gap** — delta between the two suites. A gap indicates the compressor is selectively dropping detail while preserving gist — a qualitative fingerprint of lossy compression.

## 4. Evaluation protocol

1. User implements `compress_fn(original_chunk: str) -> str`.
2. Harness loads frozen JSONL, matches chunks by `longbench_doc_id` + `original_tokens`, applies `compress_fn`, scores MC accuracy against a fixed evaluator model.
3. Results reported as a CSV with uniform schema so submissions are directly comparable.
4. A public leaderboard tracks accuracy-at-ratio by (compressor, eval_model, suite).

## 5. Reference submissions (this release)

- Telegraph English at ~50% compression
- LLMLingua-2 at 50% retention
- LLMLingua-2 at 33% retention
- Trivial baselines (identity, truncate_head, truncate_tail, random_sample) — harness provides these out of the box.

## 6. Limitations

- English only.
- GPT-4.1 produced all QA pairs — generator bias is a known risk. Future work: multi-generator subset, human-authored subset.
- MC evaluator is OpenAI-only in v1. Harness needs a pluggable evaluator for open-weight replication.
- QA pairs are generated from the uncompressed source, which biases the benchmark towards "preserve everything in the source" rather than, e.g., "prioritise task-critical facts." This is explicit by design but worth naming.

## 7. Future work

1. **Open-weight evaluator stack** — Llama-3.1, Mistral, Gemma — to remove the OpenAI dependency.
2. **Human-authored QA subset** — 200–500 items to cross-validate against the GPT-generated set.
3. **Non-chunked variant** — full-document QA for compressors that handle unbounded context natively.
4. **Multilingual extension** — Chinese, Arabic, and an agglutinative language (Finnish / Turkish).
5. **Agentic / multi-hop variant** — measure how compression compounds across a 5-step pipeline, not just a single preprocessing step. Motivated by TE's "compress-once, manage-continuously" design.
6. **Retrieval-quality companion metric** — chunk-level retrieval precision/recall when compressed text is used as the index.

## 8. Relationship to the TE paper

The TE preprint uses CKPB as its primary evaluation instrument. The standalone paper would flip the framing: TE becomes one of several reference submissions, and the contribution is the benchmark design itself — the dual-suite split, the near-miss distractor methodology, and the compression-agnostic harness.

## Target venue (tentative)

NeurIPS Datasets & Benchmarks, or EMNLP findings.
