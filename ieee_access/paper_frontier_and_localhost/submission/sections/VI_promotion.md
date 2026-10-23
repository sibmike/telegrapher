## When a local improvement is shared {#sec:design}

A rule can be useful in one repository and inappropriate in the next. Copying the file transfers the instruction but not the evidence that justified it, so the recipient must either share the relevant evaluation conditions or test the change on its own workload. Whether to adopt the edit is the additional decision that separates promotion from local adaptation. Place each system on a grid whose rows are its local gate, from a program at the top to no gate at the bottom, and whose columns are its promotion gate: no surveyed system has both the learning of the top row and the governance of the bottom row, which holds registries and prompt platforms but no local gate.

### Scope and receiving-side evaluation

We distinguish five nested scopes (Fig. REF(fig:scope)). **USER** covers one person's account or fork. **PROJECT** covers a repository, workflow, or product workspace. **STACK** covers a team's curated bundle of projects. A **TENANT** is an organization or customer, and **CORE** is the scope shared by all tenants. A wider scope aggregates the losses of the deployments it contains, so promotion changes which population the edit is intended to improve.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{Promotion scopes, from a user account to the shared core. Wider adoption changes the population on which an edit acts. Receiving-side evaluation checks whether the improvement is supported for the recipient.}
\label{fig:scope}
\end{figure}
```

A lower average loss at a broad scope can therefore conceal harm to an individual recipient. For this reason, the architecture proposed in Section REF(sec:gap) includes a held-out check at the receiving tenant. Versioning and access control govern whether an edit may be delivered and reversed; receiving-side evaluation tests whether the recipient should use it.

Several systems already evaluate transfers within one operator. ShareMem consolidates memories from one user for another and evaluates them in the receiving context [@hu2026sharemem]. XRepoSkill verifies a rule in at least two repositories [@guo2026xreposkill]. Evo2Team promotes routing skills between teams and confirms them at the target [@wang2026evo2team].

Federated systems place the check at an aggregator or a server. EvolveNet checks at the aggregator, merging a shared harness only when the merge fixes at least as many held-out items as it breaks [@nie2026evolvenet]. FederatedSkill's server agent applies, adapts, or rejects each client's edit and records the decision [@yang2026federatedskill]. Their clients are partitions or agent instances under one operator, not independently governed customer organizations, so neither system instantiates a receiving-organization gate.

Where the check runs matters, and so does what it covers. Even in Evo2Team, nearly a fifth of confirmed transfers fail on graphs not covered by confirmation. A receiving-side check provides necessary evidence for adoption, but its finite cases do not guarantee performance on all future tasks.

### Automatic, human, and unchecked promotion

Research systems often promote by admitting a candidate to a bank or archive that later runs draw on. SkillOpt, DGM, ADAS, Voyager, and SAGE make these admission decisions by program [@yang2026skillopt; @zhang2025darwin; @hu2024adas; @wang2023voyager; @wang2025sage]. AlphaEvolve and its predecessor FunSearch score candidates before admitting them to the archive [@alphaevolve2025; @romeraparedes2024funsearch]. AlphaEvolve has produced gains used within Google, but it is a research loop within one operator, rather than a product for governed sharing between organizations. No candidate travels beyond the archive, and none of these systems has access control, audited promotion, or a gate at a receiving organization.

Automatic admissions differ in what they establish. NanoResearch merges semantically, AutoManual rewrites and consolidates by judgment, and ShareMem consolidates by judgment; each decision is programmatic, but none estimates a candidate's reduction in patch loss. The feedback classes anticipated this distinction: a program can decide promotion where no per-edit estimate of improvement exists.

Production systems more often retain a person at the promotion decision. Sierra routes generated insights through human-authored expert answers [@sierra2025os20]. In Devin, the same pull-request merge serves two roles: it supplies an observed outcome to local adaptation and records the reviewer's approval for the persistent repository [@cognition2025devinreview]. Spotify's optimized prompts and plans enter production after online A/B testing and a launch decision [@palumbo2026spotify]. CASCADE combines human and agent approval for memory consolidation [@huang2025cascade]. In each, the person at the promotion gate stands in for the exact signal production lacks. That substitution makes a program on the local gate with a person on the promotion gate the production-viable pairing rather than a compromise.

A None at the promotion gate has two meanings: sharing without a check, or no sharing at all. Letta's Context Repositories illustrate the first: background reflection writes local memory edits. In the released evidence, the only check on a local edit is an optional agent review before the edit is applied, and the edits then merge back automatically. That review is the basis for Letta's Auto local gate; with the option off, the system would sit in [None × None]. Letta then pushes shared-memory changes with git lineage but without an acceptance check, so the record explains what was shared without settling whether it should have been. AutoAgent illustrates the second, as do many other systems in which promotion is absent altogether: it revises the tool and peer descriptions of one agent without propagating those revisions to another deployment [@wang2026autoagent].

### What formats, registries, and release platforms provide

Much of the infrastructure needed for sharing already exists independently of these learning loops. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit use git-tracked Markdown artifacts attached to workspaces, with a tool layer organized around MCP-style interfaces [@galster2026harnessconfig; @barbaste2026harnessengineering]. This convergence makes artifacts easier to carry between runtimes. A study of repository-level loops nevertheless finds that the runtime state of the adaptation process remains outside version control [@lulla2026loopengineering], so the portable file does not necessarily carry the history that produced it.

Public repositories provide a shared scope with human admission. In a study of five skill repositories, every substantive change was committed under a named human account and merged by a person; only one of 254 edits deprecated a skill [@shen2026whomaintains]. EDDOps gates promotion on evaluation thresholds before a human sign-off. MCP registries record namespaces and versions, and control planes add scanning, access control, or quarantine [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. Governance registries add lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed]; none of these registries generates candidate artifacts from failures.

Braintrust, Vellum, and LangSmith Hub likewise provide immutable versions, evaluation thresholds, and rollback [@braintrust2026docs; @vellum2026docs; @langsmith2026hub]. Engineers author the candidates, and evaluations can block a regressing release. In the surveyed descriptions, however, session feedback triggers neither candidate generation nor the release process, so these platforms supply much of the machinery for controlled change without closing the failure-driven local loop.

### The two decisions viewed together

Fig. REF(fig:design) places the local and promotion gates on a common grid, and Table REF(tab:VII-1) summarizes the occupants and their signals. The grid separates a system that generates and tests improvements from one that distributes human-authored artifacts under admission control, and it sets their complementary capabilities side by side.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=0.95\columnwidth]{fig3_design_space_ieee}
\caption{Local and promotion gates. Each axis records who accepts a change: a program, a person, or no gate. None includes both absent promotion and unchecked sharing; the text distinguishes these cases.}
\label{fig:design}
\end{figure}
```

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

The occupied cells match the feedback-based expectations once automatic admission is distinguished from loss estimation. Where an [Auto × Auto] promotion gate estimates a loss change, the operative signals are exact checks or simulated outcomes; the cell's judged and delayed cases prune, rewrite, or merge instead. [Auto × Human] contains observed outcomes and judgments, with no exact-signal system in the surveyed cell.

The [Human × Auto] and [Human × Human] cells are empty in the surveyed set: no system combines a human local gate on a failure-driven loop with subsequent promotion. Human local decisions occur in curation.

The bottom row, where no local gate operates, holds two kinds of system. It holds comparison systems without a failure-driven local loop, such as prompt platforms, registries, and community hubs including Buildrix [@jiang2026buildrix]. SkillRL and SkillForge occupy [None × None] because neither checks its failure-driven skill updates: new skills in SkillRL, rewrites in SkillForge.

The audit's boundary cases leave the grid unchanged. Six systems promote without artifact lineage. Five, including Spotify, have sufficient evidence under the evidence-tier rule and enter already occupied cells when the audit is relaxed; the sixth, Future AGI's prompt lifecycle, has only uncorroborated T5 evidence. No relaxation yields governed promotion across organizations. Across the grid, capabilities divide: no system has both the learning of the top row and the governance of the bottom row.
