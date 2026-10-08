## The survey: substrates, corpus, and scoring {#sec:method}

Every claim in Section REF(sec:findings) rests on a released table, and this section says how that table was made so that any row of it can be rechecked; a reader who takes the scoring on trust can skip ahead to the findings.

### Six substrates

A deployment's scaffold is composed of six substrates (Table REF(tab:V-1)). They are the coordinates of $\theta_s$, and each can be edited independently of the others; the three kinds of memory on the memory substrate follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala]. Other partitions are possible, for instance separating evaluation suites from governance. The argument of Section REF(sec:loop) is invariant to the partition so long as the coordinates stay independently editable. This partition is the one that recurs in practice: every integrated system in the corpus has a recognizable instance of each substrate under some name.

| Substrate | What persists | A score of 5 requires |
|-----------|----------------------------|----------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned rules promoted under an automatic gate |
| S2 Skills | Procedures, as code or text, loaded on demand | A skill bank that edits itself on failure, test-gated, versioned, and promoted |
| S3 Memory | Experience kept across sessions: episodic, semantic, procedural | Provenance, versions, and a correction path for every entry |
| S4 Tools | The vetted action surface and its schemas | Evaluation-gated tool versions; a curated bundle as the product |
| S5 Orchestration | The multi-role graph and its routing | Topology updated from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Staged promotion with evaluation thresholds, an audit log, and rollback |

Table V-1. The six scaffold substrates, what each holds, and what a system must do on it to score 5.

Every substrate is scored on the same 0 to 5 scale: 0, ephemeral; 1, persistent and local; 2, persistent with tool attachment but no feedback; 3, multi-scope or feedback-driven but without automated promotion; 4, automated feedback updates the scaffold, so one half of the loop is closed; 5, the substrate's own top mark in Table REF(tab:V-1). Systems that adapt several substrates at once receive an additional integrated row. The top mark means different things on two kinds of substrate. On those that hold adaptable content (S1, S2, S5) it requires both halves of the loop. On those that hold governance machinery (S3 provenance and correction, S4 evaluation-gated tool versions, S6 evaluation-gated promotion with audit and rollback) it requires the machinery a second loop would need, not the loop itself. That is why tool registries and the prompt-management platforms of Section REF(sec:findings) can score 5 with no inner loop at all and still sit outside the two-loop cells of the design space.

### How the corpus was assembled

A system enters the corpus if it wraps a foundation model with at least one persistent artifact updated from deployment signal, or if it is described in public as self-improving, scaffolded, or agentic. The systems were found in public sources through the October 2026 cutoff and scored from their own method sections or documentation, never from a secondary summary (Supplementary Material S2). Systems whose only update mechanism is weight-level training, and systems with no public evidence of deployment or release, are excluded.

Two filters structure the corpus (Fig. REF(fig:corpus)). The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate, that is, when some artifact persists across scope or is updated from feedback; systems that carry the labels but fail it form a contrast corpus, kept so that the boundary can be audited rather than asserted. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus.

A stricter composite two-loop audit then asks two questions of each core system: does Loop 1 modify a persisted artifact from session signal, and does Loop 2 promote the artifact beyond the deployment that produced it, with versioning or lineage? Applied to the 204 core systems and to ten systems treated at mechanism level, which were classified from their papers and are not rows of the released table, it admits 14 research systems (13 table rows and SkillOpt) and 3 industry exemplars (Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories). Only these are placed in the design space. Passing the audit is a weaker thing than having the governed second loop of the thesis: every passing system promotes across users, teams, or repositories inside one operator, none reaches another organization, and one of them, Letta, promotes with no gate at all (Section REF(sec:gap)).

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus flow. Every system is scored on the substrates it adapts, with an integrated row for systems that adapt several, giving 269 substrate-level rows for 256 systems; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

### Evidence and scoring discipline

Every classification rests on public evidence of uneven strength and on one rater. Each system carries one or more evidence tiers (T1 to T5 in the released table: peer-reviewed publication, arXiv preprint, production claim with metrics, open-source artifact, industry blog or interview). Peer-reviewed papers and open-source artifacts weigh most in cluster-level statements; a production claim counts when it names a benchmark or integration target; a blog post or interview counts only when a higher tier corroborates it; and production claims are never pooled with peer-reviewed evidence in a cluster-level statistic. Industry systems evaluated from vendor documentation rather than a paper are flagged wherever they appear. One author scored every system, used half-scores only when one criterion was clearly met and another partially, and rounded ambiguous cases down; the scores have not been independently re-rated, and that check is future work. The complete score table, with a one-line justification per row, is released so that every scored classification can be re-derived (Supplementary Material S1). The counts do move under natural relaxations of the composite audit (for instance, counting rollback alone as Loop-2 governance, asking for a promotion mechanism with no governance at all, or admitting a Loop 1 that persists only optimizer state); the qualitative findings survive every one of them (Supplementary Material S2).
