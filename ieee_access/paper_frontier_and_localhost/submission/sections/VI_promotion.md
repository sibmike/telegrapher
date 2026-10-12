## When a local improvement is shared {#sec:design}

A rule can be useful in one repository and inappropriate in the next. Copying the file transfers the instruction, but not the evidence that justified it. The recipient must either share the relevant evaluation conditions or test the change on its own workload. This is the additional decision that separates local adaptation from promotion.

### Scope and receiving-side evaluation

We distinguish five nested scopes. **USER** covers one person's account or fork. **PROJECT** covers a repository, workflow, or product workspace. **STACK** is a team's curated bundle of projects. A **TENANT** is an organization or customer, and **CORE** is the scope shared by all tenants. A wider scope aggregates the losses of the deployments it contains. Promotion changes which population the edit is intended to improve, as shown in Fig. REF(fig:scope).

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{Promotion scopes, from a user account to the shared core. Wider adoption changes the population on which an edit acts. Receiving-side evaluation checks whether the improvement is supported for the recipient.}
\label{fig:scope}
\end{figure}
```

The nesting makes an important limit visible. A lower average loss at a broad scope can conceal harm to an individual recipient. The proposed architecture in Section REF(sec:gap) therefore includes a held-out check at the receiving tenant. Versioning and access control govern whether an edit may be delivered and reversed; receiving-side evaluation tests whether it should be used there.

Several systems already evaluate transfers within one operator. ShareMem consolidates memories from one user for another and evaluates them in the receiving context [@hu2026sharemem]. XRepoSkill verifies a rule in at least two repositories [@guo2026xreposkill]. Evo2Team promotes routing skills between teams and confirms them at the target [@wang2026evo2team]. These are concrete instances of evidence being gathered beyond the source deployment.

Federated systems place the check elsewhere. EvolveNet merges a shared harness only when the merge fixes at least as many held-out items as it breaks, but that check occurs at the aggregator [@nie2026evolvenet]. FederatedSkill's server agent applies, adapts, or rejects each client's edit and records the decision [@yang2026federatedskill]. Their clients are partitions or agent instances under one operator, not independently governed customer organizations. They do not instantiate a receiving-organization gate.

The location of the evaluation matters, and its coverage still matters after it is correctly located. ShareMem, XRepoSkill, and Evo2Team check the receiving context; EvolveNet checks the shared merge; FederatedSkill records a server decision. Even in Evo2Team, nearly a fifth of confirmed transfers fail on graphs not covered by confirmation. A receiving-side check provides necessary evidence for adoption, but finite evaluation does not guarantee performance on all future tasks.

### Automatic, human, and unchecked promotion

Research systems often promote by admitting a candidate to a bank or archive that later runs reuse. SkillOpt, DGM, ADAS, Voyager, and SAGE apply programmatic decisions within this shared environment [@yang2026skillopt; @zhang2025darwin; @hu2024adas; @wang2023voyager; @wang2025sage]. AlphaEvolve and its predecessor FunSearch score candidates before archive admission [@alphaevolve2025; @romeraparedes2024funsearch]. AlphaEvolve has produced gains used within Google, but it is a research loop within one operator, rather than a product for governed sharing between organizations. That pool is as far as any of them travels, and none has access control, audited promotion, or a gate at a receiving organization.

Not every automatic admission has the same evidentiary meaning. NanoResearch's semantic merge, AutoManual's judged rewriting and consolidation, and ShareMem's judged consolidation are programmatic decisions, but none of them estimates a candidate's reduction in patch loss. The distinction anticipated by the feedback classes is therefore essential: an automatic promotion decision can exist where a per-edit improvement estimate does not.

Production systems more often retain a person at the promotion decision. Sierra routes generated insights through human-authored expert answers [@sierra2025os20]. In Devin, the same pull-request merge serves two roles: it supplies an observed outcome to local adaptation and records the reviewer's approval for the persistent repository [@cognition2025devinreview]. Spotify's optimized prompts and plans enter production after online A/B testing and a launch decision [@palumbo2026spotify]. CASCADE also combines human and agent approval for memory consolidation [@huang2025cascade]. In each, the person at the promotion gate stands in for the exact signal production lacks, which makes a program on the local gate with a person on the promotion gate the production-viable pairing rather than a compromise.

Letta's Context Repositories take a different path. Locally, background reflection writes memory edits and merges them back automatically; the only check on a local edit in the released evidence is an optional agent review before the edit is applied, which is the basis for its Auto local gate, and with that option off the system would sit in [None × None]. Shared-memory changes are then pushed with git lineage but without an acceptance check. The record explains what was shared, while leaving whether it should have been shared unresolved. In many other systems, promotion is absent altogether. AutoAgent, for example, revises the tool and peer descriptions of one agent without propagating those revisions to another deployment [@wang2026autoagent]. Both cases receive None at the promotion gate, but for different reasons: one shares without checking; the other does not share.

### What formats, registries, and release platforms provide

Much of the infrastructure needed for sharing already exists independently of these learning loops. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit use git-tracked markdown artifacts attached to workspaces, with a tool layer organized around MCP-style interfaces [@galster2026harnessconfig; @barbaste2026harnessengineering]. This convergence makes artifacts easier to carry between runtimes. A study of repository-level loops nevertheless finds that the runtime state of the adaptation process remains outside version control [@lulla2026loopengineering]. The portable file does not necessarily carry the history that produced it.

Public repositories provide a shared scope with human admission. In a study of five skill repositories, every substantive change was committed under a named human account and merged by a person; only one of 254 edits deprecated a skill [@shen2026whomaintains]. MCP registries provide namespaces and version records, while control planes add scanning, access control, or quarantine [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. Governance registries add lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed]. EDDOps gates promotion on evaluation thresholds before a human sign-off, but none of these registries generates candidate artifacts from failures.

Braintrust, Vellum, and LangSmith Hub likewise provide immutable versions, evaluation thresholds, and rollback [@braintrust2026docs; @vellum2026docs; @langsmith2026hub]. Engineers author the candidates, and evaluations can block a regressing release. In the surveyed descriptions, session feedback does not trigger candidate generation or the release process. These platforms supply much of the machinery for controlled change without closing the failure-driven local loop.

### The two decisions viewed together

Fig. REF(fig:design) places the local and promotion gates on a common grid. Table REF(tab:VII-1) summarizes the occupants and their signals. The grid distinguishes a system that generates and tests improvements from one that distributes human-authored artifacts under admission control, while allowing their complementary capabilities to be compared.

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

Among [Auto × Auto] systems whose promotion gate estimates a loss change, the operative signals are exact checks or simulated outcomes. The judged and delayed cases use pruning, rewriting, or merging rather than that estimate. [Auto × Human] contains observed outcomes and judgments, with no exact-signal system in the surveyed cell. These patterns match the feedback-based expectations once the meaning of automatic admission is made explicit.

The [Human × Auto] and [Human × Human] cells are empty in the surveyed set: no system combines a human local gate on a failure-driven loop with subsequent promotion. Human local decisions occur in curation. The bottom row includes comparison systems without a failure-driven local loop, such as prompt platforms, registries, and community hubs including Buildrix [@jiang2026buildrix]. SkillRL and SkillForge occupy [None × None] because their failure-driven skill updates, new skills in SkillRL and rewrites in SkillForge, are kept unchecked.

The audit's boundary cases do not change this structure. Of six systems that promote without artifact lineage, five have sufficient evidence under the tier rule and enter already occupied cells when the audit is relaxed; Spotify is one of them. The sixth, Future AGI's prompt lifecycle, has only uncorroborated T5 evidence. No relaxation yields governed promotion across organizations. What the grid reveals is a division of capabilities: no system has both the learning of the top row and the governance of the bottom row.
