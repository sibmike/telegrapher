# Frontier and Localhost

> *How Production AI Learns Outside the Weights*
>
> Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey A. Shvets
>
> Part 3 of a series. Follow-on to *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)) and *The Architecture of Errors* (Part 2).

## The argument

Reliability has moved from the weights to the scaffold. Surveying production and research LLM systems from 2023–2026, the paper shows that practitioners repeatedly wrap frozen frontier models in local, persistent, feedback-updated artifacts: instructions, skills, memories, tools, orchestration graphs, and governance pipelines.

These artifacts form a *deployment-time learning layer* — a localhost scaffold — that adapts a general model to the recurring failure topology of a specific patch. The paper formalizes this as **artifact-layer descent**: failures provide noisy loss signals, candidate scaffold deltas are generated, gates accept or reject them, accepted deltas persist and may be promoted across contexts.

The resulting two-loop architecture explains the convergence of modern agent systems across IDE plugins, vertical-bundle vendors, and self-evolving research agents, and at least eighteen concurrent research threads from 2025–2026 (SkillOpt, GEPA, Meta-Harness, RCL, Ratchet, FederatedSkill, and others) converge on the same discipline from different substrates. It also reveals an unfilled design corner: automated local scaffold evolution combined with governed, auditable, cross-organization promotion with versioned lineage, access control, and rollback. FederatedSkill (June 2026) is the closest approach, federating skill patches across clients under one operator; no public system crosses the organization boundary under such governance.

The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation.

## Read the paper

Two manuscripts share this directory. The **short** version is the canonical text for reading and citation (v3.2, September 2026: figures, a literature refresh through September 2026, and a consistency pass); the **long** version is the earlier superset with extra survey breadth (§2.5, §6.1–6.3, §9.1) and carries the v3.2 mechanical fixes but not the refresh or the figures.

- **Short (canonical), 42 pp.**: [`short/paper_frontier_and_localhost_short.pdf`](short/paper_frontier_and_localhost_short.pdf) — source [`short/paper_frontier_and_localhost_short.md`](short/paper_frontier_and_localhost_short.md); see [`short/README.md`](short/README.md) for the version history and body/appendix map.
- **Long, 43 pp.**: [`paper_frontier_and_localhost.pdf`](paper_frontier_and_localhost.pdf) — source [`paper_frontier_and_localhost.md`](paper_frontier_and_localhost.md), LaTeX [`paper_frontier_and_localhost.tex`](paper_frontier_and_localhost.tex).
- **Figures**: [`figures/`](figures/) — `make_figures.py` regenerates `fig1_descent`, `fig2_scope`, `fig3_design_space` from [`figures/FIGURE_SPEC.md`](figures/FIGURE_SPEC.md) (matplotlib; greyscale vector PDF).
- **NeurIPS-formatted port**: [`../../neurips/paper_frontier_and_localhost/`](../../neurips/paper_frontier_and_localhost/) (format-only; lags the short by one revision).

To rebuild either PDF locally: `bash build.sh` here (long) or `bash short/build.sh` (short). Both run pandoc `--citeproc` against the directory's `references.bib`, which is the single source of truth for references.

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
  author = {Arbuzov, Mikhail L. and Mosbacker, Lee and Bei, Sisong and Dong, Ziwei and Kalaev, Dmitri and Shvets, Alexey A.},
  year   = {2026},
  note   = {Survey of 130 production and research LLM systems (2023--2026, refreshed through September 2026). Part 3 in series following arXiv:2505.24187.}
}
```

## License

Paper text: **CC-BY-4.0**.
