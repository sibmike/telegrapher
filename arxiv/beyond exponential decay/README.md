# Beyond Exponential Decay

> *Rethinking Error Accumulation in Large Language Models*
>
> Mikhail L. Arbuzov, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey A. Shvets
>
> **Published as [arXiv:2505.24187](https://arxiv.org/abs/2505.24187)**.

## What this paper argues

Long-context LLM reliability is usually framed as exponential decay: if every token has independent error probability $e$, then after $n$ tokens the probability of a fully correct output collapses as $(1-e)^n$. Empirically, this is not what happens. Many production systems sustain coherence across tens of thousands of tokens.

The paper argues the exponential framing rests on a false uniformity assumption. Only roughly 5–10% of tokens are *key* (genuinely dependent on long-range context); the rest become near-deterministic once enough context accumulates. Replacing the uniform-rate model with a two-rate model $(1-e_{\text{key}})^k (1-e_{\text{non}})^{n-k}$, with $k$ scaling sublinearly in $n$, recovers the observed long-context behaviour. The question is no longer "how does $n$ grow?" but "how does $k$ grow?"

This is Part 1 of an ongoing series; Parts 2 and 3 build on the same key-token framing to derive intervention budgets and to study how production systems learn outside the model weights.

## Read the paper

- [`2505.24187v1 (1).pdf`](./2505.24187v1%20(1).pdf) — the announced version, mirrored locally.
- [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) — canonical link.

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

- [`../architecture_of_errors/`](../architecture_of_errors/) — Part 2: from key-token sparsity to a polylogarithmic intervention budget inside bounded deployment patches.
- [`../frontier_and_localhost/`](../frontier_and_localhost/) — Part 3: how production LLM systems learn outside the model weights, via instructions, skills, memories, and tools.
