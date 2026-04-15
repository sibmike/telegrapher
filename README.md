# Telegrapher

### Shrink tokens. Keep the facts, not the bloat.

**Telegraph English (TE)** is a structured compression grammar for LLM prompts. It rewrites natural language into symbol-rich atomic fact lines — a kind of semantic telegraphy — cutting token count in half while preserving 99.1% of factual accuracy on GPT-4.1. Every LLMLingua-2 configuration we tested came in behind it.

**[telegrapher.ai](https://telegrapher.ai)** — project site
**[Read the paper](paper/telegraph_english.md)** — preprint, methodology, benchmarks
**[Run the benchmark](benchmark/README.md)** — CKPB, a compression-agnostic evaluation harness

---

## See it working

**Original** — 68 tokens:

> *"According to research by Johnson and colleagues (2023), the application of machine learning techniques to medical diagnostics resulted in a 27.5% increase in early detection rates while simultaneously reducing false positives by approximately 12% compared to traditional methods."*

**Telegraph English** — 14 tokens:

```
ML→MEDICAL-DIAGNOSTICS: EARLY-DETECTION+27.5% ∧ FALSE-POSITIVE-12% [JOHNSON:2023]
```

Every fact survives. The causal direction (`→`), both quantitative claims, and the citation are each on record as separate, addressable units — and "application of… resulted in" has collapsed into a single symbol. That is the move: verbose framing gives up its tokens to a compact dialect, and what survives is fact-structured rather than token-structured.

---

## The numbers

|  |  |
|---|---|
| **~50%** | mean token reduction across LongBench-v2 |
| **99.1%** | key-fact QA accuracy preserved (GPT-4.1) |
| **96.5%** | fine-detail QA accuracy preserved (GPT-4o) |
| **Up to 11 pp** | lead over LLMLingua-2 on small models + hard tasks |
| **4,881** | frozen QA pairs released for reproducible evaluation |

Compression is document-adaptive — dense technical passages resist reduction, verbose framing collapses 5:1 — so the aggregate number hides a range from 16% on sparse text to 87% on dense content.

---

## Why this is different

Token-deletion methods like LLMLingua-2 treat compression as a one-time lossy reduction. The output is smaller, but it's still unstructured — a degraded copy of the input with no internal organisation. TE produces something else entirely.

**Compression IS chunking.** Every TE output line is one atomic fact. The compressed text is *already* a semantic index: no separate chunking stage, no overlap heuristics, no sliding windows. Each line is independently embeddable, retrievable, and prunable.

**Compress once, manage continuously.** The expensive LLM rewrite happens once per document. Everything after — retrieval, filtering, updating, pruning, merging — is cheap string manipulation with no further LLM calls. Context windows reflect the current state of knowledge, not a chronological log waiting for hard truncation.

**Full-pipeline format, not an input preprocessor.** Token-deletion compressors work on the prompt and stop. TE persists as a native format through every stage of a multi-agent pipeline. Savings compound.

---

## Quickstart

```bash
git clone https://github.com/sibmike/telegrapher.git
cd telegrapher/code

pip install -r requirements.txt
cp .env.example .env        # add your OpenAI / Anthropic keys
python -m cli.compress --help
```

The canonical Telegraph English grammar is [`code/prompts/compression_v5.txt`](code/prompts/compression_v5.txt) — 430 lines specifying ~40 symbols, atomic-line discipline, tagging, reversibility, and a 12-point quality gate.

CLI entry points: `cli.compress`, `cli.bench`, `cli.review`, `cli.eval_llml2`, `cli.errors`. See [`code/README.md`](code/README.md) for details.

---

## CKPB: a benchmark for compression fidelity

Most compression methods are evaluated by ratio or perplexity. Neither tells you whether the answer to a specific question survives. **CKPB — the Compression Knowledge-Preservation Benchmark** — does.

- **4,080 key-fact** QA pairs, generic distractors. Measures gist preservation.
- **801 fine-fact** QA pairs, near-miss distractors (`4.8%` vs `4.3%`). Measures *detail* preservation — the kind of nuance lossy methods silently drop.
- **Compression-agnostic.** Plug in any `compress_fn(str) -> str` — extractive, abstractive, neural, rule-based.

```python
from benchmark.harness import run_benchmark

summary = run_benchmark(
    compress_fn=my_compressor,   # your method: str -> str
    suite="fine_facts",
    mc_model="gpt-4.1-nano",
)
print(summary)   # {"accuracy": 0.87, "n": 801, ...}
```

Current leaderboard lives in [`benchmark/results/leaderboard.md`](benchmark/results/leaderboard.md). See [`benchmark/README.md`](benchmark/README.md) for the full spec, dataset card, and submission format.

---

## Repository layout

```
telegrapher/
├── paper/        preprint + approach + benchmark outcomes + analysis
├── code/         TE compression pipeline (MIT)
├── benchmark/    CKPB: frozen test sets, prompts, harness (CC-BY-SA 4.0 / MIT)
└── results/      aggregated figures and CSVs cited in the paper
```

---

## License

- **Code** (`code/`, `benchmark/harness/`) — **MIT**. See [`LICENSE`](LICENSE).
- **Paper, grammar, benchmark data** (`paper/`, `code/prompts/`, `benchmark/prompts/`, `benchmark/data/`) — **CC-BY-SA 4.0**. See [`LICENSE-docs`](LICENSE-docs).

We release the grammar open so it can be implemented, extended, and criticised by anyone. The benchmark is frozen and versioned so results stay comparable across submissions.

---

## Citation

If Telegraph English or CKPB informs your work, please cite the preprint in [`paper/telegraph_english.md`](paper/telegraph_english.md) and this repository:

```
@misc{telegrapher2025,
  title  = {Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting},
  author = {sibmike and contributors},
  year   = {2025},
  url    = {https://github.com/sibmike/telegrapher},
  note   = {See also https://telegrapher.ai}
}
```

---

## Get involved

Research collaborators, open-model evaluators, and extension authors welcome.
- Website: **[telegrapher.ai](https://telegrapher.ai)**
- Issues and discussions: this repository
- CKPB submissions: PR a CSV to [`benchmark/results/`](benchmark/results/) following the uniform schema

*Compression is one-time — every retrieval and generation that follows is permanently cheaper.*
