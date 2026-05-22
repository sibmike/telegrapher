# The Architecture of Errors

> *From Universal Impossibility to Patch-Local LLM Reliability*
>
> Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei
>
> Part 2 of a series. Follow-on to *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)).

## The argument

Universal LLM reliability is not a finite-library problem. Across all possible tasks, tools, schemas, knowledge sources, and evaluator expectations, new intervention-distinguishable failure modes can appear without bound, so no finite intervention dictionary can guarantee bounded residual error universally.

But deployed systems do not operate over the whole universe. They operate inside *bounded patches* — legal review, medical RAG, code repair, customer-support agents, contract extraction — with recurring tasks, schemas, tools, and evaluator expectations. Inside such patches, empirical evidence suggests that failures are sparse, repetitive, and concentrated in a small recurring catalogue, so reliability becomes a local catalogue-discovery and intervention-coverage problem rather than an exponential token-length problem.

The paper formalises this transition with two propositions. A **negative result**: no universal finite intervention dictionary can cover an unbounded domain. A **positive result**: under logarithmic or capped mode discovery, the patch-local intervention budget grows polylogarithmically in sequence length and becomes domain-constant once the patch catalogue saturates. The framework relocates rather than dissolves long-context difficulty: where the number of hard decisions itself grows with task length, reliability remains hard; the contribution is to identify the on-axis intervention rather than to make those regimes easy.

## Read the paper

- **PDF**: [`paper_architecture_of_errors.pdf`](paper_architecture_of_errors.pdf)
- **Source (Markdown)**: [`paper_architecture_of_errors.md`](paper_architecture_of_errors.md)
- **LaTeX source**: [`paper_architecture_of_errors.tex`](paper_architecture_of_errors.tex)

To rebuild the PDF locally: `bash build.sh`.

## Series

| Part | Paper | Status |
|---|---|---|
| 1 | *Beyond Exponential Decay: Rethinking Error Accumulation in LLMs* | [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) |
| 2 | *The Architecture of Errors* (this paper) | preprint |
| 3 | *Frontier and Localhost: How Production AI Learns Outside the Weights* | [`../frontier_and_localhost/`](../frontier_and_localhost/) |

## Citation

```bibtex
@misc{arbuzov2026architecture,
  title  = {The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability},
  author = {Arbuzov, Mikhail L. and Shvets, Alexey A. and Bei, Sisong},
  year   = {2026},
  note   = {Follow-on to arXiv:2505.24187}
}
```

## License

Paper text and figures: **CC-BY-4.0**.
