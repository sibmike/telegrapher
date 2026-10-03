## The two-loop design space {#sec:design}

Systems that pass the composite audit sit in a 3×3 matrix indexed by the gate type on each loop (Fig. REF(fig:design)); Supplementary Material S4 lists the named membership of every cell.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=0.9\columnwidth]{fig3_design_space_ieee}
\caption{The two-loop design space. Three cells hold every system that passes the composite audit; the human-authored cells are occupied only by registries and curation workflows that have no session-signal loop. No populated system adds governed cross-tenant promotion.}
\label{fig:design}
\end{figure}
```

Three cells hold every system that passes the composite audit. [Auto × Auto] holds the research full-auto systems, twelve from the May corpus with machine-evaluated criteria on both loops. [Auto × Human] is the production-viable cell: Loop 1 fires at machine speed under an algorithmic criterion and Loop 2 waits for a person. [None × Auto] holds the governance-first platforms with evaluation-gated promotion and no failure-triggered candidate generation. The 2026 sweep did not add a cell: its seven cross-context promoters land in [Auto × Auto] without versioning or lineage and so enter the strict audit only under relaxation, and its one production loop lands in [Auto × Human].

The other cells are not empty, but they are occupied only by systems that fail the composite audit, and the pattern of occupancy is itself a finding. [Human × Auto] remains empty: nobody authors candidates by hand and promotes them automatically, because manual authorship offers automated promotion little leverage. [Human × Human] is occupied by MCP registries and a community hub [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway; @jiang2026buildrix], where a person registers an artifact and a person approves its use; the field study of five public skill repositories finds the same shape in practice, with every substantive edit human-merged and one deprecation in 254 edits [@shen2026whomaintains]. [Human × None] is the curation cell: an agent drafts, a person fact-checks, and the result is frozen [@nguyen2025verificagent]. These are single-loop by construction. Read by signal class, the occupancy is what Section REF(sec:signal) predicts: automatic gates on both loops appear only where the signal is exact or cheaply observable, and the human cells fill where it is not.

Two cross-cutting findings sharpen the picture. *Evidence is now batched before acceptance.* In the May corpus nearly every automatic gate fired on a single evaluation, absorbing estimator noise through the per-edit margin alone. By mid-2026 statistical acceptance is common: a paired per-item test that commits an edit only when its wins are reliable [@wang2026sagegate], a merge accepted only when the held-out items it fixes outnumber those it breaks [@nie2026evolvenet], three heterogeneous critics that must all pass [@shang2026vag], and mini-batch failure signals with validation-based selection [@park2026autosaddler]. The agreement form of batching, where $k$ independent proposals must converge, shrinks the false-accept rate as $p^k$ rather than shrinking variance as $1/k$, and the two should not be conflated (Appendix REF(app:gates)). *Multi-layer hierarchies remain rare.* AlphaEvolve is still the only system that combines a cascade evaluator with a diversity archive; the 2026 systems that keep archives use them for lineage, not for staged evaluation.
