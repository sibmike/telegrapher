## Substrates, corpus, and scoring {#sec:method}

### Six substrates

A deployment's scaffold is composed of six substrates. They are the coordinates of $\theta_s$, and each can be edited independently of the others. The three kinds of memory on S3 follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala].

| Substrate | What persists | Score-5 mark |
|------------|----------------------------|------------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned, two-loop, auto-gated promotion |
| S2 Skills | Procedural artifacts (code or text) loaded on demand | Skill bank self-modifies on failure, test-gated, versioned, promoted |
| S3 Memory | Cross-session experience (episodic, semantic, procedural) | Provenance, versioning, and correction pathways |
| S4 Tools | Vetted action surface and context schemas | Domain-curated bundle is the product; evaluation-gated tool versions |
| S5 Orchestration | Multi-role graph and routing | Population or policy updates from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Dev-to-staging-to-production with evaluation thresholds, audit log, and rollback |

Table V-1. The six scaffold substrates and the mark a system must reach to score 5.

The 0 to 5 rubric is the same on every substrate: 0, ephemeral; 1, persistent and local; 2, persistent with tool attachment but no feedback; 3, multi-scope or feedback-driven but without automated promotion; 4, automated feedback updates the scaffold, so one loop is closed; 5, the substrate's own top mark in Table REF(tab:V-1). On the substrates that hold adaptable content (S1, S2, S5) the top mark requires both loops; on the substrates that hold governance machinery (S3 provenance and correction, S4 evaluation-gated tool versions, S6 evaluation-gated promotion with audit and rollback) it requires the machinery a second loop would need, which is why a registry or a prompts-as-code platform can score 5 on S6 while having no inner loop at all. Systems that adapt several substrates at once receive an additional integrated row. Other partitions are possible, for instance separating evaluation suites from governance; the argument of Section REF(sec:loop) is invariant to the partition so long as the coordinates stay independently editable.

### How the corpus was assembled

The corpus was built in two passes with one rubric. The first pass (January 2023 to May 2026) searched arXiv, vendor documentation, and public repositories for systems described as self-improving, scaffolded, or agentic, and kept those that wrap a foundation model with at least one persistent artifact updated from deployment signal. The second pass (June to October 2026) ran query families for self-evolving skills and skill lifecycle, harness and context optimization, agent memory governance, prompt-as-code and evaluation-gated promotion, federated or multi-tenant skill sharing, and multi-agent topology evolution, and it followed the citations of the systems the first pass had identified as closest to the gap of Section REF(sec:gap). Every system admitted in either pass was scored from its own method section or documentation, never from a secondary summary. The first pass scored 130 systems; the second added 126, for 256 unique systems and 269 substrate-level rows. The cutoff is October 2026.

Two filters structure the corpus (Fig. REF(fig:corpus)). The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate, that is, when some artifact persists across scope or is updated from feedback; systems that carry the labels but fail it are kept as a contrast corpus so the boundary is auditable rather than rhetorical. A stricter composite two-loop audit then asks whether Loop 1 modifies a persisted artifact from session signal and Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage; only systems passing both enter the design space of Section REF(sec:design). Of the 256 systems, 204 pass the discriminator and 52 form the contrast corpus; 14 research systems and 3 industry exemplars pass the composite audit, and 7 systems added in 2026 promote across contexts without versioning or lineage and enter only under the relaxations below. Industry systems evaluated from vendor documentation rather than from a paper are flagged as such wherever they appear.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus flow. Every system is scored on the six substrates; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

Two kinds of system are excluded. Those whose only update mechanism is weight-level fine-tuning or reinforcement learning are model-side and belong to the self-evolution literature this survey positions against; those with no public evidence of deployment or release are not scored at all.

### Evidence and scoring discipline

Each system carries one or more evidence tiers: T1 peer-reviewed publication; T2 arXiv preprint; T3 production claim with metrics; T4 open-source artifact; T5 industry blog or interview. T1 and T4 carry the most weight in cluster-level statements; T3 is admissible when the claim is concrete (a named benchmark or integration target); T5 only when corroborated by a higher tier. Production claims are never pooled with peer-reviewed evidence when a cluster-level statistic is computed. Scoring is single-rater. One author scored every system, half-scores were used only when one criterion was clearly met and another partially, and ambiguous cases were rounded down. The complete score table, with a one-line justification per row, is released as Supplementary Material S1 so that every classification can be re-derived. The counts reported in Section REF(sec:findings) move under two natural relaxations of the composite criterion, counting any of versioning, lineage, or rollback as Loop-2 governance, or admitting updates that persist only optimizer state as Loop 1; the qualitative findings survive both (Supplementary Material S2).
