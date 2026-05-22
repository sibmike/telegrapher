# Frontier and Localhost

> *How Production AI Learns Outside the Weights*
>
> Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei
>
> Part 3 of a series. Follow-on to *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)) and *The Architecture of Errors* (Part 2).

## The argument

Reliability has moved from the weights to the scaffold. Surveying production and research LLM systems from 2023–2026, the paper shows that practitioners repeatedly wrap frozen frontier models in local, persistent, feedback-updated artifacts: instructions, skills, memories, tools, orchestration graphs, and governance pipelines.

These artifacts form a *deployment-time learning layer* — a localhost scaffold — that adapts a general model to the recurring failure topology of a specific patch. The paper formalises this as **artifact-layer descent**: failures provide noisy loss signals, candidate scaffold deltas are generated, gates accept or reject them, accepted deltas persist and may be promoted across contexts.

The resulting two-loop architecture explains the convergence of modern agent systems across IDE plugins, vertical-bundle vendors, and self-evolving research agents. It also reveals an unfilled design corner: automated local scaffold evolution combined with governed, auditable, cross-organisation promotion — a DP-FedAvg-style aggregator with an automated eval gate at the scaffold layer.

The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation.

## Read the paper

- **PDF**: [`paper_frontier_and_localhost.pdf`](paper_frontier_and_localhost.pdf)
- **Source (Markdown)**: [`paper_frontier_and_localhost.md`](paper_frontier_and_localhost.md)
- **LaTeX source**: [`paper_frontier_and_localhost.tex`](paper_frontier_and_localhost.tex)

To rebuild the PDF locally: `bash build.sh`.

## Series

| Part | Paper | Status |
|---|---|---|
| 1 | *Beyond Exponential Decay: Rethinking Error Accumulation in LLMs* | [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) |
| 2 | *The Architecture of Errors* | [`../architecture_of_errors/`](../architecture_of_errors/) |
| 3 | *Frontier and Localhost* (this paper) | preprint |
| 4 | Practitioner-facing companion (reference architectures, maturity ladders, design principles, full failure taxonomy) | planned |

## Citation

```bibtex
@misc{arbuzov2026frontier,
  title  = {Frontier and Localhost: How Production AI Learns Outside the Weights},
  author = {Arbuzov, Mikhail L. and Shvets, Alexey A. and Bei, Sisong},
  year   = {2026},
  note   = {Survey of 142 production and research LLM systems. Part 3 in series following arXiv:2505.24187.}
}
```

## License

Paper text: **CC-BY-4.0**.
