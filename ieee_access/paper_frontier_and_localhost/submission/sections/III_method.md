## Corpus and method {#sec:method}

We read each system's public method or documentation for four things: the persistent artifact it changes, the feedback that prompts the change, the decision that accepts it, and the scope in which the result is used. This allows systems with different names and application domains to be compared by their behavior.

### Scope and selection

The corpus contains 256 unique systems from January 2023 through the October 2026 cutoff. The first search pass identified 130 systems by May 2026; the second added 126. Sources include research papers, public repositories, product documentation, and supported production reports; the search families, evidence tiers, and inclusion rules are recorded with the released data (Supplementary Material S2).

A system enters the survey if it adapts a foundation model through a persistent artifact updated from deployment signal, or if it is publicly described as self-improving, scaffolded, or agentic. Including the latter group provides a contrast set: the survey can test whether those descriptions correspond to persistent adaptation. Systems whose only update mechanism is weight-level training are excluded, as are systems without public evidence of release or deployment.

We apply two filters. The first admits a system to the **core corpus** if it scores at least 3 on at least one scaffold substrate under the rubric below. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus. A system may have one integrated row or several substrate-specific rows, so the 256 systems occupy 269 scored rows.

The second filter is a **two-loop audit**. It asks whether session feedback changes a persistent artifact and whether that artifact is subsequently promoted beyond the deployment that produced it, with versioning or lineage. Applied to the core systems and the additional paper-based classifications (Supplementary Material S2), it admits 11 research systems and 3 industry exemplars. Fig. REF(fig:corpus) summarizes the selection.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus selection. The 256 systems occupy 269 scored rows. The first filter separates core from contrast systems; the two-loop audit then checks persistent local adaptation and promotion with lineage. The audit includes the additional paper-based classifications described in the text.}
\label{fig:corpus}
\end{figure}
```

The research systems passing the audit are NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual, and CASCADE. The industry exemplars are Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories. SkillOpt is classified from its paper and is not a row in the 256-system score table. The remaining paper-based systems are identified in the data notes (Supplementary Material S2) and the audit's boundary cases in the contrast set (Supplementary Material S4).

Passing this audit does not establish governed sharing across organizations. All passing systems promote within one operator, into a shared bank or archive that later runs draw from, or across the agents and sessions of one deployment. Letta passes on the lineage of its shared-memory updates even though those updates have no acceptance gate. Six further systems promote across contexts without lineage on the promoted artifact; their treatment under relaxed audit rules is reported separately.

### Substrates and scoring

The scaffold has six substrates: instructions, skills, memory, tools, orchestration, and governance. These are the possible targets of a proposed edit. Table REF(tab:V-1) describes them; the episodic, semantic, and procedural memory categories follow Sumers et al. [@sumers2023coala].

| Substrate | What persists | A score of 5 requires |
|-----------|----------------------------|----------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned rules promoted under an automatic gate |
| S2 Skills | Procedures, as code or text, loaded on demand | A skill bank that edits itself on failure, test-gated, versioned, and promoted |
| S3 Memory | Experience kept across sessions: episodic, semantic, procedural | Provenance, versions, and a correction path for every entry |
| S4 Tools | The vetted action surface and its schemas | Evaluation-gated tool versions; a curated bundle as the product |
| S5 Orchestration | The multi-role graph and its routing | Topology updated from deployment feedback by a loop outside the agent's own run |
| S6 Governance | Versioning, promotion, audit, rollback | Staged promotion with evaluation thresholds, an audit log, and rollback |

Table V-1. The six scaffold substrates, what each holds, and what a system must do on it to score 5.

The common scoring scale runs from 0 to 5. At 0 an artifact is ephemeral. At 1 it persists locally; at 2 it persists with tool attachment but without feedback. At 3 it either spans scopes without a gate or is updated from feedback by a person. At 4 a program updates it from feedback. The score-5 requirement depends on the substrate, as specified in the table.

This last distinction is important when interpreting the scores. Instructions and skills require both loops to reach 5. Orchestration requires a topology updated from deployment feedback by a loop outside the agent's own execution. Memory, tools, and governance are scored for their corresponding governance capabilities, so a registry can score 5 without generating local edits. Integrated rows measure breadth and depth of adaptation, not closure of either loop. The scale therefore supports substrate-specific comparisons; a top score is not a universal certificate of complete optimization.

Table REF(tab:V-2) gives the corpus distribution. Research systems hold the top marks on skills, memory, and the integrated row. Production platforms and standards hold them on tools and governance. No system reaches the top score across all six substrates, and none reaches it on instructions or orchestration.

| Substrate | $n$ | Mean | Score-5 systems | What the corpus holds on it |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents and nothing measures them; no system closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | The local loop closes under a program in the research systems; the production repositories merge by hand |
| S3 Memory | 50 | 3.06 | Cuadros et al. | The ledger ships in products; the correction a gate would enforce is absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | The most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies change under an evaluation gate; one structurally gated instance; no two-loop system with lineage |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md under the Agentic AI Foundation (AAIF) | Prompts-as-code mature; registries add lineage and rollback; no local loop generates a candidate |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | Breadth and depth of adaptation, not the loop; reached only by research systems without enterprise governance |

Table V-2. Substrate maturity across the 256-system corpus. Column n counts scored rows on each substrate, Mean is the average score, and Score-5 systems reach the substrate's top mark; the integrated row counts systems scored across several substrates as one row. Of the 126 most recently added systems, 105 are core and 32 are skill systems; 89 of those core systems close the local loop under a program, and none of the 126 scores 5 on any substrate.

For the 126 most recently added systems, gate types, feedback classes, and governance properties are recorded as explicit columns of the released table, so counts based on those columns apply to those systems. For example, 89 of their 105 core systems close the local loop under a program. This is not a gate count over all 256 systems.

### Evidence and limitations

The evidence ranges from peer-reviewed studies and open-source artifacts to vendor claims. Every classification carries its evidence tier and a one-line justification in the released table. Peer-reviewed papers and open-source artifacts receive the greatest weight. A production claim must name a benchmark or integration target, and a blog or interview is counted only when stronger evidence corroborates it. Production claims are not pooled with peer-reviewed evidence in corpus-level statistics; vendor-based exemplars are identified as such.

One author scored all systems. Ambiguous cases were rounded down, and half-scores were used only when one criterion was clearly met and another partly met. Independent re-rating remains future work. The classifications should be read as an auditable interpretation of public evidence, not a complete inventory of private production behavior.

We also test the audit under alternative boundaries: counting rollback as sufficient promotion governance, allowing promotion without governance, and admitting loops that persist only optimizer state. Membership changes under these relaxations, but the principal structural findings remain: [Auto × Auto] stays well populated, the human-local cells hold only curation and registries, Letta alone passes with an ungated promotion, and no relaxation adds governed promotion across organizations (Section REF(sec:gap)). The sensitivity analysis is released with the data notes (Supplementary Material S2) and the full score table with the released table (Supplementary Material S1).
