# S4. Contrast set, matrix membership, and closest approaches (May 2026 corpus)

The tables in this section describe the first-pass corpus, which closed in May 2026; the second-pass systems that occupy a cell of the Section VII matrix are named in the cell-by-cell discussion that follows the matrix.

## S4.1 Contrast set

Two tables mark the two boundaries of the survey. The first lists representative members of the first-pass contrast corpus: 31 systems that fail the patch-local discriminator, scoring below 3 on every substrate. The second lists core systems, each scoring at least 3 on some substrate, that still fail the stricter composite two-loop criterion, so that the asterisked entries of the matrix in Section S4.2.1 can be checked.

Two marks recur. An asterisk, used in the matrix, marks a system that fails at least one criterion of the composite audit and is included for contrast. A dagger has two uses: in the two contrast tables it marks a system classified from its paper because the score table has no row for it (ReAct, MetaGen, MetaReflection, CLIN, ACE); in the matrix it marks an industry exemplar evaluated with vendor documentation as the primary evidence (Sierra Agent OS 2.0, Cognition Devin).

### S4.1.1 Contrast corpus: fails the patch-local discriminator

| System | Year | Discriminator failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Self-Refine [@madaan2023selfrefine] | 2023 | No persistent artifact | In-context iteration only |
| ReAct [@yao2023react]† | 2023 | No persistent artifact | Thought-act-observe loop is intra-session |
| TextGrad [@yuksekgonul2024textgrad] | 2024 | No artifact distinct from optimizer state | Textual-gradient optimization; SkillOpt [@yang2026skillopt] (Section VIII; Section S5) adds the persistent `best_skill.md`, held-out validation gate, rejected-edit memory, and textual learning-rate schedule that TextGrad lacks. |
| OPRO, Toolformer | 2023 | No persistent deployment artifact | Optimization or tool use inside a single training or inference run |
| Aider conventions, Lovable knowledge | 2024 | No feedback loop | Engineer-authored convention files |
| AGENTS.md (as a standard) | 2025 | No feedback loop | Cross-vendor artifact format as a workspace file; adoption measured, adaptation absent (Section VI). The specification's governance under the AAIF is a separate S6 entry, "AGENTS.md / AAIF" |
| LangChain Skills, HuggingFace Agent Skills, CrewAI Skills | 2025–2026 | No feedback loop | Curated skill packs without failure-triggered update |
| Tran & Kiela [@tran2026singleagent] | 2026 | Not a system | Single-agent baselines match or beat multi-agent under matched thinking-token budgets; constrains S5 claims (see Section VI) |

### S4.1.2 Core corpus, fails the composite two-loop criterion

| System | Year | Composite-criterion failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Reflexion [@shinn2023reflexion] | 2023 | No Loop 2 | Per-agent episodic memory without promotion |
| Generative Agents | 2023 | No Loop 2 | Per-agent reflection + importance memory |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks |
| Mem0 (vanilla) | 2024 | No Loop 2 | Per-user memory; no cross-context promotion |
| Zep | 2024 | No Loop 2 | Per-agent/session knowledge graph |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent |
| DSPy | 2023 | No artifact distinct from optimizer state | Prompt-template optimization; SkillOpt [@yang2026skillopt] (Section VIII; Section S5) realizes the artifact-bearing form. |
| MetaGen† | 2026 | No Loop 2; no cross-session persistence | Role pool dynamic within single inference call |
| MAE (Multi-Agent Evolve) | 2025 | No Loop 2 | Co-evolution within Proposer/Solver/Judge triplet |
| MetaReflection† | 2024 | No Loop 2 | Per-agent semantic memory |
| CLIN† | 2023 | No cross-instance promotion | Causal abstractions per-agent-per-environment |
| LangGraph, AutoGen, CrewAI | 2023–2024 | Framework only | Orchestration frameworks; not deployed systems |
| W&B Weave, Agenta, Langfuse | 2024 | No Loop 1 | Observability / eval-as-code |
| Mobile-Agent-E, Cradle, OS-Copilot | 2024–2025 | No Loop 2 | Self-evolving but per-session/per-deployment |
| Agent S, Agent S2 | 2024–2025 | No Loop 2 | Computer-use agentic framework |
| ACE [@ace2025agentic]† | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook |
| Cursor Rules (vanilla) | 2024 | No Loop 2 | Per-project artifacts |
| GitHub Copilot custom instructions, Windsurf, Continue.dev, Zed AI rules | 2024 | No Loop 1 | Engineer-authored at repo base branch |
| Replit `replit.md` | 2025 | Loop 2 absent | Self-writing scaffold but per-workspace |
| SkillForge [@skillforge2026] | 2026 | No Loop 2 | A judge flags failed replies that drive each skill rewrite; the rewrite is committed without an acceptance test, versions stay in the scenario deployment, and engineers review replies, not skill versions |
| AutoAgent [@wang2026autoagent] | 2026 | No Loop 2 | Per-agent tool and peer descriptions revised on an uncalibrated consistency judgment; never promoted or versioned |
| SkillRL [@skillrl2026] | 2026 | No gate on either loop | A success rate below 0.4 triggers skill proposals; the skill bank takes each one as an unconditional union |

The contrast systems fail the discriminator in three main ways: they iterate in context only, they have no feedback loop, or they are not systems at all. Core systems fail the composite criterion mostly for want of a Loop 2.

---

## S4.2 Matrix membership and closest approaches

### S4.2.1 Two-loop matrix: cell-by-cell discussion

Both axes record who decides, as Section III defines: a gate is Auto when a program applies a check, Human when a person decides, and None when the step is absent or runs unchecked. An engineer-authored or registrant-supplied artifact with no failure trigger therefore has Loop 1 None in both passes, and who supplies each candidate is listed separately in the occupant table at the end of this section.

The first-pass matrix, with the marks of Section S4.1:

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual | CASCADE, Sierra Agent OS 2.0†, Cognition Devin† | SkillForge\*, AutoAgent\*, MAE\*, MetaGen\*, MetaReflection\*, CLIN\*, DSPy\*, TextGrad\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in the first pass]** | *(none)* |
| **Loop-1 None** | ExpeL\* (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repository\* | Self-Refine\*, ReAct\*, Mem0\*, SkillRL\* |

The matrix places the first-pass systems audited under the composite criterion, with SkillOpt, and the contrast entries marked with an asterisk. Every matrix entry that passes the audit sits in [Auto × Auto] or [Auto × Human]: the ten research systems of the first cell, with CASCADE, are the eleven research systems of Section V, and Sierra Agent OS 2.0 and Cognition Devin are two of its three industry exemplars. The third exemplar, Letta's Context Repositories, is a second-pass system.

Three placements need a word. DSPy and TextGrad sit in [Auto × None] because their Loop 1 is automated but persists only optimizer state, which only the optimizer-state relaxation of Section S2 would count as a persisted artifact. DGM sits in [Auto × Auto] although its local gate is a validity check rather than a loss estimate: the archive admits every child that compiles and can still edit code, the benchmark score weights parent selection rather than deciding retention, and no person decides anything in the loop, since self-modifications are evaluated without human intervention [@zhang2025darwin]. SkillRL sits in [None × None] although its loop is failure-driven: a per-category success rate below 0.4 triggers new skill proposals, and the skill bank takes each proposal as an unconditional union, so the step that keeps an edit runs unchecked, and the bank never leaves its run.

COSPLAY and Cuadros et al., which are first-pass rows, and PACE, CORAL, GEPA, Meta-Harness, MOSS, and RCL, which were classified from their papers after the first pass closed, carry no composite audit, so they are neither placed in the matrix nor counted in Section V. Second-pass systems record their gate pairs in the released score table, and the paragraphs below name those that occupy a cell.

**[Auto × Auto]** is the most populated cell: ten systems, each with a machine-evaluated criterion on both loops. Speed on both loops is what its members share; cross-organization governance is what every one of them lacks.

**[Auto × None]** holds the systems whose local loop is gated and whose promotion has no gate, whether because nothing is promoted or because everything is. One audit passer sits here: Letta's Context Repositories push shared memory across agents automatically, with git lineage and no evaluation of any kind, so the composite audit admits them on lineage and the matrix records a promotion that nothing decides (Section VII). Mem0 Platform, TOKI, Learning on the Job, and RASO sit here with no promotion at all; RASO retrieves skills from a read-only public corpus, which is inbound retrieval rather than promotion [@chu2026raso]. Two first-pass systems join them, each starred because it has no Loop 2. SkillForge's judge flags the failed replies that drive each skill rewrite, the rewrite is committed without an acceptance test, and every version stays in the scenario deployment; its support engineers review replies, not skill versions. AutoAgent's analyzer accepts revisions to one agent's tool and peer descriptions on an uncalibrated consistency judgment, and nothing leaves that agent's store. VACE belongs here too although its gate is a held-out check: it compares a candidate harness with the incumbent against the freshly trained checkpoint of the same run, so the edit is made and kept inside one training run [@qi2026vace].

**[Auto × Human]** is the production-viable cell. Loop 1 fires at machine speed under an algorithmic criterion, and Loop 2 waits for a person before an edit propagates; the pairing reconciles the speed of automation with a reviewer's accountability. CASCADE, Sierra Agent OS 2.0, and Cognition Devin occupy it: a human-and-agent consolidation gate, human-authored expert answers, and a reviewer's merge of a pull request each put a person on promotion.

Six second-pass systems promote across users, clients, teams, or repositories with no versioning or lineage on the promoted artifact, so they sit outside the strict audit: EvolveNet, Evo2Team, XRepoSkill, ShareMem, Spotify's recommendation loop, and Future AGI's prompt lifecycle. Were the audit to ask for a promotion mechanism and no governance property at all, five of them would enter, all landing in [Auto × Auto] except Spotify's loop in [Auto × Human], without opening a new cell; the sixth, Future AGI's prompt lifecycle, rests on T5 evidence alone and is not admitted under any rule (Section S2).

**[None × Auto]** holds the governance-first prompts-as-code systems: Braintrust, LangSmith Hub, and Vellum. Their Loop 2 is real, since evaluation-gated CI blocks a promotion on regression. They have no Loop 1 in the patch-local sense, because engineers author the candidate artifacts at their desks and session feedback never triggers one, and the asterisks record exactly that: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated. ExpeL, starred and also marked weak, sits here for a different reason: its experience bank is built from training tasks, which blurs the boundary of its loop, so it fails the audit (Section S4.1.2).

**[Human × Auto]** is empty in both passes: no surveyed system puts a person on the local gate of a failure-driven loop and then promotes the result by program. A plausible occupant would ship person-approved skills through an automatic held-out evaluation; no published system does.

**[Human × Human]** is empty too. The registries that a first reading puts here (Azure API Center, the agentic-community MCP Gateway and Registry, TrueFoundry, Buildrix) have no failure-driven loop: a person registers an artifact and a person, or an admission scan, approves its use, which is a promotion gate on a registrant-supplied artifact. They sit in **[None × Human]** with the Anthropic skills repository and Agentic Configuration Management, whose lifecycle states a governance role assigns, and the five public skill repositories of the field study (Section VII) show the same shape in practice. Enoch's checkpoint-and-validate protocol moves one agent's state between hosts and is neither loop. The released table records these re-codings (Section S6.7).

**[Human × None]** is the curation cell, also filled only from the second pass and single-loop by construction. In VerificAgent an agent drafts, a person fact-checks, and the result is frozen; in SkillChain a judge filters the candidate edits and a person decides, at a reflection gate, which refined skills are deployed; in the Davis et al. case study one engineer both writes and accepts the governance mechanisms that failures call for (Section VII). Curation stays patch-local, rather than collapsing into an engineer editing a configuration file, because the candidate answers a failure and a person decides whether it stays.

The occupants, with the variable the matrix does not show:

| Cell | Systems | Candidate source | Loop 1 gate | Promotion mechanism | Loop 2 gate |
|--------|----------------------|----------------|--------------|------------------|---------------|
| [Auto × Auto] | NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual | agent proposals from trajectories or failures | evaluator, verifier, or threshold | merge into a shared bank or archive | the same evaluator, on the shared bank |
| [Auto × Human] | CASCADE, Sierra Agent OS 2.0, Cognition Devin | agent proposals | calibrated judge or outcome threshold | release to the team or product | reviewer, domain expert, or merge approval |
| [Auto × None] | Letta Context Repositories; Mem0 Platform, TOKI, Learning on the Job, RASO, VACE; SkillForge, AutoAgent | agent (Letta: sleep-time subagents) | automatic write gate (RASO: validation-set acceptance; VACE: held-out comparison against the incumbent harness; SkillForge: a calibrated judge that flags failed replies; AutoAgent: an uncalibrated consistency judgment) | Letta: unconditional git push to shared memory; the others: none | none |
| [None × Auto] | Braintrust, LangSmith Hub, Vellum, Governed Capability Evolution; EDDOps, with a sign-off after the threshold | engineers | none (no failure-driven loop) | evaluation-gated release | evaluation threshold |
| [None × Human] | Azure API Center, MCP Gateway and Registry, TrueFoundry, Buildrix, Anthropic skills repository, Agentic Configuration Management | registrants, contributors, engineers | none | admission to a registry, merge into a shared repository, or a lifecycle state | approval by a person (the MCP Gateway adds an automated admission scan) |
| [Human × None] | VerificAgent, SkillChain, Davis et al. | agent drafts (VerificAgent; SkillChain after a judge); the engineer (Davis et al.) | a person | none | none |

### S4.2.2 Closest approaches to governed cross-tenant scaffold optimization

Section IX defines the four properties: (a) an auto-gated Loop 1, (b) cross-organization promotion, (c) versioned lineage with access control, and (d) rollback. The closest approaches split them among themselves:

- **AlphaEvolve** has (a) and a partial (b) confined to one organization; it has no mechanism for promotion across organizations.
- **NanoResearch** has (a) at the research level, and its paper describes no enterprise governance layer.
- **SkillOpt** has (a) fully and a partial (c), through its exported `best_skill.md` artifact and protected slow-update field. Its reported positive transfer across models, harnesses, and benchmarks is an empirical measurement of evidence radius. It implements neither (b) nor explicit rollback (d). The walkthrough in Section S5 maps each of its design decisions onto the loop.
- **CORAL** [@qu2026coral] has a partial (a) through reflection-written shared memory and an automatic Loop 2 through heartbeat-based promotion; it has no (b), no formal access control for (c), and no (d). It is the only system classified before the second pass whose Loop 2 runs asynchronously across multiple agents inside one organization, through shared persistent memory. Evo2Team and ShareMem, second-pass systems, promote across teams and across users without versioning.
- **PACE** [@ling2026pace] has (a) at small-model production timescales and a fast/slow two-timescale pair of loops that consolidates across one deployment's own episodes, not across deployments; it has no (b) and no formal (c) or (d). It is the closest demonstration that the two-loop architecture runs under small-frozen-model constraints.
- **Meta-Harness** [@lee2026metaharness] has (a) over the harness (substrate S5), with a filesystem of candidates that records credit assignment and serves as the accumulated history $H_t$ of Appendix XII. It has no cross-organization promotion, no access control, and no rollback.
- **SkillForge** has a partial (a), a calibrated judge that selects failures with no acceptance test on the rewrite, and a partial (c) through VFS commits, but no (b): each rewritten skill version stays in the scenario deployment that produced it, and its support engineers review replies, not skill versions; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has a partial (a). Its cross-organization promotion is claimed in vendor documentation only and not counted as evidence under the tier rule of Section V, and its GitHub-style Workspaces give some lineage but not access control with rollback in the strict sense.
- **FederatedSkill** [@yang2026federatedskill] has (a) and, with EvolveNet (Table IX-1), the strongest partial (b) among the surveyed systems: heterogeneous clients, each a backbone-plus-harness profile under one federation operator, exchange semantic skill diffs, and a server-side evolution agent applies, adapts, or rejects each patch per client. An auditable decision log, recording source patch, reward, and justification for each modified path, gives a partial (c); there is no access control and no (d).
- **SkillClaw** [@ma2026skillclaw] has a partial (a), through a nightly validation step, and a partial (b) across the users of one shared, synchronized skill repository; it reports no (c) or (d).
- **ChronoMem** [@su2026chronomem] has (d) and the versioning half of (c) for the memory substrate alone: whole-memory snapshots, version histories, and natural-language rollback inside Google's Agent Development Kit. It has no Loop 1, no (b), and no access control.
- **Vellum, Braintrust, and LangSmith Hub** have (c) and (d) explicitly but neither (a) nor (b) in the strict sense; they are governance-first by construction.

No surveyed system combines (b), (c), and (d) under any gate type. The cross-organization governance triad is unfilled on its own, whether or not Loop 1 is auto-gated.

### S4.2.3 Whether the missing architecture should be built

Whether the missing architecture should be built depends on the feedback-signal class, not on the application domain: safety-critical domains such as medical decision support, legal advice, and financial advice, where a reviewer's gate on promotion is a design feature rather than a defect, are judged or delayed domains with high stakes. Section IX gives the argument class by class.

---
