## Substrates, corpus, and scoring {#sec:method}

### Six substrates

A deployment's scaffold is composed of six substrates (Table REF(tab:V-1)). They are the coordinates of $\theta_s$, and each can be edited independently of the others. The three kinds of memory on the memory substrate follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala].

| Substrate | What persists | Score-5 mark |
|------------|----------------------------|------------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned, two-loop, auto-gated promotion |
| S2 Skills | Procedural artifacts (code or text) loaded on demand | Skill bank self-modifies on failure, test-gated, versioned, promoted |
| S3 Memory | Cross-session experience (episodic, semantic, procedural) | Provenance, versioning, and correction pathways |
| S4 Tools | Vetted action surface and context schemas | Domain-curated bundle is the product; evaluation-gated tool versions |
| S5 Orchestration | Multi-role graph and routing | Population or policy updates from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Dev-to-staging-to-production with evaluation thresholds, audit log, and rollback |

Table V-1. The six scaffold substrates and the mark a system must reach to score 5.

The 0 to 5 rubric is the same on every substrate: 0, ephemeral; 1, persistent and local; 2, persistent with tool attachment but no feedback; 3, multi-scope or feedback-driven but without automated promotion; 4, automated feedback updates the scaffold, so one loop is closed; 5, the substrate's own top mark in Table REF(tab:V-1). Systems that adapt several substrates at once receive an additional integrated row.

The top mark means different things on two kinds of substrate. On those that hold adaptable content (S1, S2, S5) it requires both loops. On those that hold governance machinery (S3 provenance and correction, S4 evaluation-gated tool versions, S6 evaluation-gated promotion with audit and rollback) it requires the machinery a second loop would need, not the loop itself. That is why MCP and the prompts-as-code platforms score 5 on S4 and S6 with no inner loop at all and still sit outside the two-loop cells of the design space.

Other partitions are possible, for instance separating evaluation suites from governance; the argument of Section REF(sec:loop) is invariant to the partition so long as the coordinates stay independently editable. This one recurs in practice: every integrated system in the corpus has a recognizable instance of each substrate, under different names.

### How the corpus was assembled

The corpus holds systems that either wrap a foundation model with at least one persistent artifact updated from deployment signal or are described in public as self-improving, scaffolded, or agentic. They were found in arXiv, vendor documentation, and public repositories between January 2023 and the October 2026 cutoff. The corpus was assembled in two passes, the second adding 126 systems up to the cutoff (Supplementary Material S2). Each was scored from its own method section or documentation, never from a secondary summary.

Two filters structure the corpus (Fig. REF(fig:corpus)). The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate, that is, when some artifact persists across scope or is updated from feedback. Systems that carry the labels but fail it form a contrast corpus, kept so that the boundary can be audited rather than asserted. A stricter composite two-loop audit then asks whether Loop 1 modifies a persisted artifact from session signal and whether Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage; only systems that pass both are counted as occupying the design space, and systems that fail it appear in the matrix as contrast entries, marked as such. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus; 14 research systems (13 of them rows of the released table, and SkillOpt) and 3 industry exemplars (Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories) pass the composite audit. The text also treats ten further systems at mechanism level: SkillOpt, GEPA, Meta-Harness, CORAL, PACE, MOSS, RCL, FederatedSkill, SkillClaw, and ChronoMem. They were classified from their papers after the first pass closed and are not rows of the released table, so the corpus counts above exclude them. SkillOpt is the only one of them in the design matrix.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus flow. Every system is scored on the substrates it adapts, with an integrated row for systems that adapt several, giving 269 substrate-level rows for 256 systems; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

Two kinds of system are excluded: those whose only update mechanism is weight-level fine-tuning or reinforcement learning, which are model-side and belong to the self-evolution literature this survey positions against; and those with no public evidence of deployment or release.

### Evidence and scoring discipline

Every classification rests on public evidence of uneven strength and on one rater. Each system carries one or more evidence tiers (T1 to T5 in the released table: peer-reviewed publication, arXiv preprint, production claim with metrics, open-source artifact, industry blog or interview). Peer-reviewed papers and open-source artifacts weigh most in cluster-level statements; a production claim counts when it names a benchmark or integration target; a blog post or interview counts only when a higher tier corroborates it; and production claims are never pooled with peer-reviewed evidence in a cluster-level statistic. Industry systems evaluated from vendor documentation rather than a paper are flagged wherever they appear. Scoring is single-rater: one author scored every system, used half-scores only when one criterion was clearly met and another partially, and rounded ambiguous cases down. The complete score table, with a one-line justification per row, is released so that every scored classification can be re-derived (Supplementary Material S1).

The counts of the findings move under two natural relaxations of the composite audit: counting any of versioning, lineage, or rollback as Loop-2 governance, or admitting as Loop 1 an update that persists only optimizer state. The qualitative findings survive both (Supplementary Material S2).
