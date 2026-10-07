# Frontier and Localhost

> *How Production AI Learns Outside the Weights*
>
> Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey A. Shvets
>
> Part 3 of a series. Follow-on to *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)) and *The Architecture of Errors* (Part 2).

## The argument

Reliability has moved from the weights to the scaffold. Surveying production and research LLM systems from 2023–2026, the paper shows that practitioners repeatedly wrap frozen frontier models in local, persistent, feedback-updated artifacts: instructions, skills, memories, tools, orchestration graphs, and governance pipelines.

These artifacts form a *deployment-time learning layer* — a localhost scaffold — that adapts a general model to the recurring failure topology of a specific patch. The paper formalizes this as **artifact-layer descent**: failures provide noisy loss signals, candidate scaffold deltas are generated, gates accept or reject them, accepted deltas persist and may be promoted across contexts.

The resulting two-loop architecture explains the convergence of modern agent systems across IDE plugins, vertical-bundle vendors, and self-evolving research agents, and at least eighteen concurrent research threads from 2025–2026 (SkillOpt, GEPA, Meta-Harness, RCL, Ratchet, FederatedSkill, and others) converge on the same discipline from different substrates. It also reveals an unfilled design corner: automated local scaffold evolution combined with governed, auditable, cross-organization promotion with versioned lineage, access control, and rollback. FederatedSkill (June 2026) and EvolveNet (August 2026) are the closest approaches, each narrowing different properties; no public system crosses the organization boundary under such governance.

The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation.

## Read the paper

Three manuscripts share this directory. **v4 (October 2026) is the canonical text and the arXiv submission package**: the survey as prepared for IEEE Access (a 256-system corpus through October 2026, the feedback-signal classification of Section 4, a claims audit, an extended related work), set as a one-column article with the supplementary material as appendices. The **short** (v3.2, September 2026) and **long** versions are superseded and kept for history.

- **v4 (canonical; arXiv package), 71 pp.**: [`v4/paper_frontier_and_localhost.pdf`](v4/paper_frontier_and_localhost.pdf) — assembled from the IEEE package's section files by [`v4/build.sh`](v4/build.sh); upload bundle [`v4/paper_frontier_and_localhost.zip`](v4/paper_frontier_and_localhost.zip); [`v4/README.md`](v4/README.md) has the layout, the build, and the submission metadata.
- **IEEE Access article (source of truth for the text)**: [`../../ieee_access/paper_frontier_and_localhost/`](../../ieee_access/paper_frontier_and_localhost/) — edit the paper there; v4 is derived.
- **Short (v3.2, superseded), 42 pp.**: [`short/paper_frontier_and_localhost_short.pdf`](short/paper_frontier_and_localhost_short.pdf) — source [`short/paper_frontier_and_localhost_short.md`](short/paper_frontier_and_localhost_short.md); see [`short/README.md`](short/README.md) for its version history and body/appendix map.
- **Long (superseded), 43 pp.**: [`paper_frontier_and_localhost.pdf`](paper_frontier_and_localhost.pdf) — source [`paper_frontier_and_localhost.md`](paper_frontier_and_localhost.md), LaTeX [`paper_frontier_and_localhost.tex`](paper_frontier_and_localhost.tex).
- **Figures**: [`figures/`](figures/) — `make_figures.py` regenerates `fig1_descent`, `fig2_scope`, `fig3_design_space` from [`figures/FIGURE_SPEC.md`](figures/FIGURE_SPEC.md) (matplotlib; greyscale vector PDF); `make_figures.py --ieee` renders the four figures v4 and the IEEE article use, including the corpus-flow figure.
- **NeurIPS-formatted port**: [`../../neurips/paper_frontier_and_localhost/`](../../neurips/paper_frontier_and_localhost/) (format-only; lags by two revisions).

To rebuild: `bash v4/build.sh` (canonical; pdflatex + bibtex, numeric references from the IEEE package's `references.bib`, which is the single source of truth for references). `bash build.sh` (long) and `bash short/build.sh` (short) still build the superseded versions with pandoc `--citeproc` against their own `references.bib`.

## Series

| Part | Paper | Status |
|---|---|---|
| 1 | *Beyond Exponential Decay: Rethinking Error Accumulation in LLMs* | [arXiv:2505.24187](https://arxiv.org/abs/2505.24187) |
| 2 | *The Architecture of Errors* | [`../architecture_of_errors/`](../architecture_of_errors/) |
| 3 | *Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights* (this paper) | arXiv package ready in [`v4/`](v4/); IEEE Access version prepared |
| 4 | Practitioner-facing companion (reference architectures, maturity ladders, design principles, full failure taxonomy) | planned |

## Citation

```bibtex
@misc{arbuzov2026frontier,
  title  = {Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights},
  author = {Arbuzov, Mikhail L. and Mosbacker, Lee and Bei, Sisong and Dong, Ziwei and Kalaev, Dmitri and Shvets, Alexey A.},
  year   = {2026},
  note   = {Survey of 256 production and research LLM systems (January 2023 to October 2026). Part 3 in a series following arXiv:2505.24187 and arXiv:2605.30628.}
}
```

## License

Paper text: **CC-BY-4.0**.
