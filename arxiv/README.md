# arXiv preprints

Preprints from this repository, each with its own subdirectory containing source, build script, and PDF.

| Paper | Subdirectory | Status |
|---|---|---|
| *Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting* | [`paper_telegraph_english/`](paper_telegraph_english/) | Preprint |
| *Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models* | [`beyond exponential decay/`](./beyond%20exponential%20decay/) | Published as [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) |
| *The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability* | [`architecture_of_errors/`](architecture_of_errors/) | Preprint |
| *Frontier and Localhost: How Production AI Learns Outside the Weights* | [`frontier_and_localhost/`](frontier_and_localhost/) | Preprint |

## The error-clustering series

Three of the four papers form an ongoing series on long-context LLM reliability:

- **Part 1** — *Beyond Exponential Decay* (published as arXiv:2505.24187): errors concentrate at a sparse subset of *key tokens* rather than accumulating uniformly, so the standard $(1-e)^n$ exponential framing of long-context reliability is the wrong model.
- **Part 2** — *The Architecture of Errors*: no universal finite intervention dictionary can cover an unbounded domain, but inside a bounded deployment patch the required intervention budget grows polylogarithmically in sequence length and becomes domain-constant once the patch catalogue saturates.
- **Part 3** — *Frontier and Localhost*: production LLM systems learn outside the weights via instructions, skills, memories, tools, and governance pipelines — a deployment-time scaffold layer that adapts a frozen frontier model to the recurring failure topology of its patch.

## Telegraph English

*Telegraph English* sits outside the series. It introduces a structured compression grammar that rewrites natural-language text into symbol-rich atomic-fact lines, cutting token count by about half while preserving fact-level accuracy. See the [main repository README](../README.md) for the project overview, benchmarks, and reference implementation.
