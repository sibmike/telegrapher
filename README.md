# Telegrapher

This repository releases two complementary artefacts:

1. **Telegraph English (TE)** — a structured semantic-compression protocol that rewrites text into a symbol-rich, line-atomic dialect. At ~50% token reduction it preserves 99.1% accuracy on key facts (GPT-4.1) and outperforms LLMLingua-2 at matched compression ratios on every model and task we tested.
2. **CKPB** — the *Compression Knowledge-Preservation Benchmark*, a dual-suite MC QA benchmark explicitly designed to differentiate lossless from lossy compression. Compression-agnostic: plug in any `compress_fn(str) -> str`.

Unlike token-deletion methods, TE performs a full semantic rewrite — each output line is one atomic fact, so the compressed text is simultaneously a semantic index.

## Paper

The full preprint, abstract, methodology, and results are in [`paper/telegraph_english.md`](paper/telegraph_english.md). Shorter overviews:

- [`paper/approach.md`](paper/approach.md) — high-level approach
- [`paper/benchmark_outcomes.md`](paper/benchmark_outcomes.md) — results summary
- [`paper/benchmark_analysis.md`](paper/benchmark_analysis.md) — detailed analysis

## Benchmark

[`benchmark/`](benchmark/) contains the **frozen** CKPB test sets, the generation prompts, and a compression-agnostic evaluation harness. Run the 10-item smoke test:

```bash
pip install -r code/requirements.txt
export OPENAI_API_KEY=sk-...
python -m benchmark.harness.example_run
```

Evaluate your own compressor:

```python
from benchmark.harness import run_benchmark

summary = run_benchmark(
    compress_fn=my_compressor,      # str -> str
    suite="fine_facts",
    mc_model="gpt-4.1-nano",
)
```

See [`benchmark/README.md`](benchmark/README.md) for details, [`benchmark/results/leaderboard.md`](benchmark/results/leaderboard.md) for current standings, and [`benchmark/PAPER_OUTLINE.md`](benchmark/PAPER_OUTLINE.md) for the standalone-paper outline.

## Telegraph English — Quickstart

```bash
cd code
pip install -r requirements.txt
cp .env.example .env          # add your OpenAI / Anthropic keys
python -m cli.compress --help
```

The canonical grammar specification is [`code/prompts/compression_v5.txt`](code/prompts/compression_v5.txt) (~430 lines). CLI commands: `cli.compress`, `cli.bench`, `cli.review`, `cli.eval_llml2`, `cli.errors`. See [`code/README.md`](code/README.md).

## Results

[`results/`](results/) contains the aggregate TE-specific artefacts cited in the paper:

- `compression_stats.csv` — per-document compression ratios
- `benchmark_41.csv`, `benchmark_4omini.csv` — QA accuracy (coupled TE-vs-original rows; the **frozen**, uncoupled test sets live in [`benchmark/data/`](benchmark/data/))
- `compression_rate_histogram.png`, `compression_ratio_histogram.png`

## Repository layout

```
telegrapher/
├── paper/        # preprint + supporting documents
├── code/         # TE compression pipeline (MIT)
├── benchmark/    # CKPB — frozen test sets, prompts, harness (CC-BY-SA 4.0 / MIT)
└── results/      # aggregated figures and TE-submission CSVs cited in the paper
```

## License

- Code (`code/`, `benchmark/harness/`): **MIT** — see [`LICENSE`](LICENSE)
- Paper, grammar, and benchmark QA data (`paper/`, `code/prompts/`, `benchmark/prompts/`, `benchmark/data/`): **CC-BY-SA 4.0** — see [`LICENSE-docs`](LICENSE-docs)

## Citation

If you use Telegraph English or CKPB in your work, please cite the preprint in [`paper/telegraph_english.md`](paper/telegraph_english.md) and this repository (`github.com/sibmike/telegrapher`).
