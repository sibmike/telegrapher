## The promotion loop in the industry: how far an edit travels, and who lets it {#sec:design}

The promotion loop exists in the industry only in parts, each built inside one operator, and no surveyed system carries a promotion out of its operator under lineage, access control, and rollback. That matters because the promotion loop is what lets a fix earned in one deployment reach another; without it, every customer relearns the same lesson. The section follows an edit upward, from a crossing inside one operator to the top rung, and ends on the grid that sets the local gate beside the promotion gate.

### Inside one operator: what crosses, and the check where it arrives

Every kind of crossing below the tenant boundary is occupied, each by a system of one operator, the organization that runs both sides with no customer boundary between them. Where such a system checks the arriving edit decides whether the receiving deployment ever learns that the edit helps there.

The crossings run up the ladder of Section REF(sec:loop). Between users, ShareMem consolidates one user's memories for another and evaluates them there [@hu2026sharemem]. Between repositories, a rule in XRepoSkill survives only if it is verified in at least two of them [@guo2026xreposkill]. Between teams, at the STACK rung, Evo2Team promotes routing skills and confirms them at the target [@wang2026evo2team]. The data-local clients of a federated run are partitions rather than deployments and so sit on no rung; across them, EvolveNet merges a shared harness only when the merge fixes at least as many held-out items as it breaks [@nie2026evolvenet], and FederatedSkill's server agent applies, adapts, or rejects each client's edit and logs the decision [@yang2026federatedskill].

A promotion differs from a push in having a check at all, and these systems differ in where the check sits. ShareMem, XRepoSkill, and Evo2Team check where the edit arrives; EvolveNet checks at the aggregator and nowhere else; FederatedSkill records a decision taken at the server. The receiving-side evaluation that Section REF(sec:loop) places at every rung is therefore present in the corpus and rare. Where it is present it is necessary rather than sufficient: nearly a fifth of Evo2Team's confirmed transfers still fail on graphs the confirmation never saw.

None of these leaves its operator: no system promotes across customers or organizations with evidence. That is the thesis of this article. Because the failure log and the trace of Section REF(sec:findings) are hardly built, a system that tried would have few failure-driven edits to promote and no way to trace a failure on arrival back to the edit that caused it.

### Who lets it climb: a program, a person, or nothing

Who lets an edit climb is set by the feedback the crossing can get, so the corpus sorts into systems where a program admits the edit, systems where a person does, and one production system where nothing does. The sorting tells a team which promotion gate its own signal allows.

A program lets an edit climb where a check travels with it, as Section REF(sec:signal) predicted. The research systems that promote into a shared bank or archive work this way: in NanoResearch, SkillOpt, DGM, ADAS, Voyager, and SAGE [@xu2026nanoresearch; @yang2026skillopt; @zhang2025darwin; @hu2024adas; @wang2023voyager; @wang2025sage] the same program that kept an edit admits it to the pool every later run draws from. In AlphaEvolve, as in FunSearch before it, the evaluator cascade that scores every candidate is the only thing that admits a program to the archive; AlphaEvolve is a research loop run inside Google rather than a product, and the programs kept in that archive went on to production gains [@alphaevolve2025; @romeraparedes2024funsearch]. That pool is as far as any of them travels, and none has access control, audited promotion, or a gate at a receiving organization.

A person lets an edit climb where the signal is an observed outcome or a judgment. CASCADE consolidates memory under a human-and-agent gate [@huang2025cascade]. Sierra routes agent-generated insights through human-authored expert answers [@sierra2025os20]. In Devin one event serves both halves: the merge of a pull request is the outcome the local loop reads, and the reviewer's decision to merge is also what lets the edit stand in the repository every later session uses [@cognition2025devinreview]. Spotify's automatically optimized prompts and plans go live only after an online A/B test and a launch decision [@palumbo2026spotify]. In every one of them the person at the promotion gate stands in for the exact signal production lacks, which makes the pairing of a program on the local gate with a person on the promotion gate the production-viable one rather than a compromise.

Nothing lets an edit climb in one production system, and nothing promotes at all in most research systems. Letta's Context Repositories push every edit to shared memory with lineage and no check; the ledger records what crossed, and nothing asks whether it should have. In the far larger group whose accepted edits never leave the deployment that made them, a program keeps the edit and nothing carries it anywhere; AutoAgent, whose analyzer revises one agent's own tool and peer descriptions, is among them [@wang2026autoagent].

### The top rung: CORE exists, and everything in it is admitted by hand

Above the tenant boundary the scope exists and the promotion does not. CORE, the scope every tenant shares, exists today in two forms, a format and a registry, and an edit promoted into it on evidence is not one of them. CORE is the rung where cross-tenant promotion would happen, so what fills it now shows how much of the promotion loop the industry has built at the top.

The first form is a format. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit all keep a git-tracked markdown artifact attached to a workspace, with an MCP-style tool layer beside it [@galster2026harnessconfig; @barbaste2026harnessengineering], so an artifact written for one deployment can be carried to any other. Even where a repository runs an autonomous loop, the runtime state of that loop sits outside version control [@lulla2026loopengineering], so what the format versions is the artifact and not the process that edits it.

The second form is a registry that admits artifacts for everyone, and admission is by hand. In the five public skill repositories of one field study, every substantive edit is written and merged by a person, with one deprecation in 254 edits [@shen2026whomaintains]. The MCP registries split into catalogues (namespaces and version records, no scanning) and control planes (scanning, access control, quarantine) [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. The governance registries bring lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed]. One of them, EDDOps, gates promotion on evaluation thresholds before a human sign-off [@kang2026registry], but none generates the candidate from a failure.

The prompts-as-code platforms hold the rest of the machinery the promotion loop would need, and nothing feeds it. Braintrust, Vellum, and LangSmith Hub [@braintrust2026docs; @vellum2026docs; @langsmith2026hub] keep immutable versions, evaluation thresholds, and rollback. But engineers author the candidates at a desk, an evaluation blocks a release on regression, and session feedback never triggers either, which makes them MLOps for scaffolds rather than for weights.

So tools and governance reach the top mark of Section REF(sec:method) with no local loop at all.

### The two halves together: the gate grid

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=0.95\columnwidth]{fig3_design_space_ieee}
\caption{The two-loop design space. Rows give the local gate and columns the promotion gate, with None for a step that is absent or runs unchecked; a cell [local gate $\times$ promotion gate] such as [Auto $\times$ Human] pairs an algorithmic local gate with a human promotion gate. Darker cells mark the three populated kinds of system; lighter cells hold curation, the MCP registries and community hubs, and the systems whose promotion is ungated or absent.}
\label{fig:design}
\end{figure}
```

Set side by side, the local gate and the promotion gate show an industry that has converged on the first and is sorted on the second by the feedback it can get. The loop makes exactly two decisions, whether a local edit enters the scaffold and whether an accepted edit leaves the deployment, so a grid of the two gates places every system by both at once.

The grid of Fig. REF(fig:design) puts the local gate in the rows and the promotion gate in the columns, each one of the three gate kinds of Section REF(sec:loop). Every system whose local gate is a program sits in the top row, and what tells them apart is the column: a program, a person, or nothing. The column is not a free choice; it follows the signal as Section REF(sec:signal) predicted, with one qualification the data adds for three systems.

Every [Auto × Auto] system whose promotion gate estimates the loss change runs on an exact signal or a simulated outcome, as EvolveNet's held-out merge and XRepoSkill's second repository do. Those on delayed or judged signals, NanoResearch, AutoManual, and ShareMem, decide by program on both halves, but by pruning, a judged rewrite, or a judged merge rather than by estimating a loss change. That is the degenerate gate Section REF(sec:signal) describes for a loop without a per-edit estimate, and it is the qualification. [Auto × Human] holds observed outcomes and judgments and no exact-signal system. Nor does any system calibrate a judge under edit. Table REF(tab:VII-1) reads the grid cell by cell, with the signal found in each.

| Cell | Who keeps the local edit, who lets it climb | Who is there | Signal found there |
|--------------------|------------------------------------|--------------------------------------|------------------------------|
| [Auto × Auto] | A program keeps it; a program lets it climb | Research systems that close both halves inside one environment or one operator | Exact and simulated outcomes; delayed and judged only under pruning or merging |
| [Auto × Human] | A program keeps it; a person lets it climb | Production systems with a reviewer on promotion, and CASCADE | Observed outcomes and judgments |
| [Auto × None] | A program keeps it; nothing lets it climb | Letta's ungated push; systems that promote nothing | As on the local gate |
| [Human × None] | A person keeps it; nothing lets it climb | Curation | Judged |
| [None × Auto] | No failure triggers a candidate; a threshold gates release | Prompts-as-code platforms and governance registries | No failure-driven loop |
| [None × Human] | No failure triggers a candidate; a person admits | Open standards, MCP registries, community hubs | No failure-driven loop |
| [None × None] | Nothing checks or promotes the edit | SkillRL and SkillForge, unchecked skill loops | Outcomes and judgments |

Table VII-1. The gate grid read cell by cell: who keeps a local edit and who lets it climb, which systems sit in the cell, and the feedback signal they gate on. [Human × Auto] and [Human × Human] hold no surveyed system.

[Human × Auto] and [Human × Human] are empty: no surveyed system puts a person on the local gate of a failure-driven loop and then promotes the result. The human-gated row holds curation alone, where an agent drafts and a person decides what is kept.

The bottom row holds the systems with no failure-driven loop, which enter the grid for comparison rather than through the audit (Supplementary Material S4). They are the prompts-as-code platforms, which gate release on evaluation but generate no candidates, and the registries and community hubs, Buildrix among them [@jiang2026buildrix], in which a person registers an artifact and a person, or an admission scan, approves its use. SkillRL and SkillForge, the two failure-driven skill loops that run unchecked, sit in the row's last cell.

Of the six systems that promote without lineage on the promoted artifact (Fig. REF(fig:corpus)), the tier rule of Section REF(sec:method) admits the evidence for five, Spotify among them, and these join cells already occupied and open no new one (Supplementary Material S2). No system has both the learning of the top row and the governance of the bottom, and what no cell contains is governed cross-tenant promotion, which Section REF(sec:gap) specifies.
