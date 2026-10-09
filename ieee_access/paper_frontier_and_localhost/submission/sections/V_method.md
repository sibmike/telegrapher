## The corpus, and how it was read against the loop {#sec:method}

Every placement in Sections REF(sec:findings) to REF(sec:failure) is a reading of one system's own text in the vocabulary of Section REF(sec:loop): which scaffold coordinate the system edits, whether a measure gates the edit, who decides, and how far the edit travels. The reading was done from each system's method section or documentation, and it is released row by row with a one-line justification, so that any placement below can be checked against the system rather than against this survey.

### How the corpus was assembled

A system enters the corpus if it wraps a foundation model with at least one persistent artifact updated from deployment signal, or if it is described in public as self-improving, scaffolded, or agentic; systems whose only update mechanism is weight-level training, and systems with no public evidence of deployment or release, are excluded (Supplementary Material S2). The systems were found in public sources in two passes (130 by May 2026 and 126 more by the October 2026 cutoff), and the second pass records, for each system it added, the gate on each half of the loop, the signal class, and the governance properties as columns of the released table, so the counts that follow by gate are counts over the systems it added.

Two filters sort the systems (Fig. REF(fig:corpus)), and both are stricter than the field's own labels. The first keeps a system in the core corpus only when some artifact of it persists across scope or is updated from feedback, which is a score of at least 3 on at least one substrate on the ruler below; systems that carry the labels but fail it form a contrast corpus, kept so that the boundary can be audited rather than asserted. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus. Every system is scored on each substrate it adapts, and a system that adapts several gets one composite row as well, which is why 256 systems give 269 rows.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus flow. Every system is scored on the substrates it adapts, with an integrated row for systems that adapt several, giving 269 substrate-level rows for 256 systems; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

The second filter is the two-loop audit, which asks each core system the two questions of the loop's two halves: does Loop 1 modify a persisted artifact from session signal, and does Loop 2 promote the artifact beyond the deployment that produced it, with versioning or lineage? Applied to the 204 core systems, and to ten more classified from their papers alone (they are not rows of the released table), it admits 11 research systems, NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual, and CASCADE, of which all but SkillOpt are rows of the released table, and 3 industry exemplars (Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories). Section REF(sec:design) places them, with every other surveyed system, on the gate grid by who decides on each half. Passing the audit is a weaker thing than having the governed second loop of the thesis: every passing system promotes inside one operator, into a shared bank or archive that later runs draw from or from one agent, user, or repository to the next; none reaches another organization; and one of them, Letta, promotes with no gate at all (Section REF(sec:design)).

### Six coordinates and one ruler

Condition 3 of Section REF(sec:loop) asks that a failure be traced to the scaffold coordinate that caused it, and the corpus locates that coordinate on one of six substrates (Table REF(tab:V-1)); they are the coordinates of $\theta_s$, each editable independently of the others, and the three kinds of memory on the memory substrate follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala].

| Substrate | What persists | A score of 5 requires |
|-----------|----------------------------|----------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned rules promoted under an automatic gate |
| S2 Skills | Procedures, as code or text, loaded on demand | A skill bank that edits itself on failure, test-gated, versioned, and promoted |
| S3 Memory | Experience kept across sessions: episodic, semantic, procedural | Provenance, versions, and a correction path for every entry |
| S4 Tools | The vetted action surface and its schemas | Evaluation-gated tool versions; a curated bundle as the product |
| S5 Orchestration | The multi-role graph and its routing | Topology updated from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Staged promotion with evaluation thresholds, an audit log, and rollback |

Table V-1. The six scaffold substrates, what each holds, and what a system must do on it to score 5.

The ruler is the same on every substrate, 0 to 5, and it measures distance along the loop. At 0 the artifact is ephemeral; at 1 it is persistent and local; at 2 it is persistent with tool attachment but no feedback; up to that point an artifact persists and nothing measures it, which is the patchwork stage of Section REF(sec:loop). At 3 the artifact either spans scopes with no gate on the way or is updated from feedback by a person; at 4 a program updates it from feedback, so Loop 1 closes. The top mark, 5, is each substrate's own in Table REF(tab:V-1): both halves of the loop on the substrates that hold adaptable content (S1, S2, S5), and the machinery a second loop would need on those that hold governance (S3, S4, S6), which is why a registry or a prompt platform can score 5 with no Loop 1 at all.

### What was gathered, by substrate

No system matures all six substrates at once (Table REF(tab:V-2)). Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation. Each kind was built to satisfy one constraint (fast learning, safe change, or portability) and matured only the substrates that constraint touches, so the top marks fall on different substrates for different kinds of system: research systems on skills and memory and in the composite row, products and standards on tools and governance, and no system at all on instructions or orchestration.

| Substrate | $n$ | Mean | Score-5 systems | What the corpus holds on it |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents and nothing measures them; no system closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | Loop 1 closes under a program in the research systems; the production repositories merge by hand |
| S3 Memory | 50 | 3.06 | Cuadros et al. | The ledger ships in products; the correction a gate would enforce is absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | The most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies change under an evaluation gate; one structurally gated instance; no two-loop system |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | Prompts-as-code mature; registries add lineage and rollback; no Loop 1 generates a candidate |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | High-water mark; reached only by research systems without enterprise governance |

Table V-2. Substrate maturity across the 256-system corpus. Column n counts scored rows on each substrate, Mean is the average score, and Score-5 systems reach the substrate's top mark; the composite row counts systems scored across several substrates as one row. Of the 126 most recently added systems, 102 are core and 31 are skill systems; 92 of those core systems close Loop 1 under a program, and none of the 126 scores 5 on any substrate.

### Evidence and scoring discipline

Every classification rests on public evidence of uneven strength and on one rater. Each system carries one or more evidence tiers (T1 to T5 in the released table: peer-reviewed publication, arXiv preprint, production claim with metrics, open-source artifact, industry blog or interview); peer-reviewed papers and open-source artifacts weigh most in corpus-level statements, a production claim counts when it names a benchmark or integration target, a blog post or interview counts only when a higher tier corroborates it, and production claims are never pooled with peer-reviewed evidence in a corpus-level statistic. Industry systems evaluated from vendor documentation rather than a paper are flagged wherever they appear. One author scored every system, used half-scores only when one criterion was clearly met and another partially, and rounded ambiguous cases down; the scores have not been independently re-rated, and that check is future work. The complete score table, with a one-line justification per row, is released so that every scored classification can be re-derived (Supplementary Material S1); the counts move under natural relaxations of the audit (counting rollback alone as Loop-2 governance, asking for a promotion mechanism with no governance at all, admitting a Loop 1 that persists only optimizer state) while the qualitative findings survive every one of them (Supplementary Material S2).
