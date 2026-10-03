# Beyond Exponential Decay

> *Rethinking Error Accumulation in Large Language Models*
>
> Mikhail L. Arbuzov, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey A. Shvets
>
> **Published as [arXiv:2505.24187](https://arxiv.org/abs/2505.24187)** (v1 May 2025, v2 May 2026; v3 prepared here, see [`CHANGELOG.md`](./CHANGELOG.md)).

## What this paper argues

Long-context LLM reliability is usually framed as exponential decay: if every token has independent error probability $e$, then after $n$ tokens the probability of a fully correct output collapses as $(1-e)^n$. Empirically, this is not what happens. Many production systems sustain coherence across tens of thousands of tokens.

The paper argues the exponential framing rests on a false uniformity assumption. Only a small minority of tokens are *key* (genuinely dependent on long-range context or carrying a decision); the rest become near-deterministic once enough context accumulates. Replacing the uniform-rate model with a two-rate model $(1-e_{\text{key}})^k (1-e_{\text{non}})^{n-k}$, with $k$ scaling sublinearly in $n$, recovers the observed long-context behaviour. The question is no longer "how does $n$ grow?" but "how does $k$ grow?" The paper also marks where the argument stops: when the number of decisions grows with the task, as in long-horizon agentic work, the same model predicts the exponential decay in task length that agent evaluations report.

This is Part 1 of an ongoing series; Parts 2 and 3 build on the same key-token framing to derive intervention budgets and to study how production systems learn outside the model weights.

## Source layout

| File | Role |
|---|---|
| `main.tex` | arXiv preprint wrapper: `\usepackage[preprint]{neurips_2026}` + five-author block. |
| `body.tex` | The paper body (abstract through appendices). **Canonical.** Copied verbatim into `../../neurips/paper_beyond_exponential_decay/submission/`. |
| `references.bib` | Bibliography (29 entries). |
| `figures/` | Fig. 1 source (`fig1_decay_regimes.tex`, pgfplots) and its data generator (`make_fig1_data.py`, pure Python). |
| `build.sh` | `pdflatex → bibtex → pdflatex ×2`; produces `main.pdf`. |
| `CHANGELOG.md` | What changed between versions, with sources for every corrected number. |
| `legacy_v1/` | The original v1 template source. Superseded; kept for the record. |

Rebuild: `bash build.sh` (MiKTeX or TeX Live with `pgfplots`; the figure PDF is pre-built so `pgfplots` is only needed to regenerate it).

## Read the paper

- [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) — canonical link.
- `main.pdf` — the locally built current version.
- [`2505.24187v1 (1).pdf`](./2505.24187v1%20(1).pdf) — the announced v1, mirrored locally.

## Citation

```bibtex
@article{arbuzov2025beyond,
  title   = {Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models},
  author  = {Arbuzov, Mikhail L. and Bei, Sisong and Dong, Ziwei and Kalaev, Dmitri and Shvets, Alexey A.},
  journal = {arXiv preprint arXiv:2505.24187},
  year    = {2025}
}
```

## Related work in this repository

- [`../architecture_of_errors/`](../architecture_of_errors/) — Part 2: from key-token sparsity to a polylogarithmic intervention budget inside bounded deployment patches ([arXiv:2605.30628](https://arxiv.org/abs/2605.30628)).
- [`../frontier_and_localhost/`](../frontier_and_localhost/) — Part 3: how production LLM systems learn outside the model weights, via instructions, skills, memories, and tools.
