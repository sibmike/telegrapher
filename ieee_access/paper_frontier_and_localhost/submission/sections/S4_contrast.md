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

The contrast systems fail the discriminator in three main ways: they iterate in context only, they have no feedback loop, or they are not systems at all. Core systems fail the composite criterion mostly for want of a Loop 2.

---

## S4.2 Matrix membership and closest approaches

### S4.2.1 Two-loop matrix: cell-by-cell discussion

The table keeps the first-pass convention, under which an engineer-authored artifact with no failure trigger has Loop 1 None; second-pass scoring, like Section VII, counts a person registering an artifact as a human local gate, and under that convention the Anthropic skills repository sits with the registries in [Human × Human].

The first-pass matrix, with the marks of Section S4.1:

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, Sierra Agent OS 2.0†, Cognition Devin† | MAE\*, MetaGen\*, MetaReflection\*, CLIN\*, DSPy\*, TextGrad\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in the first pass]** | *(none)* |
| **Loop-1 None** | ExpeL\* (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repository\* | Self-Refine\*, ReAct\*, Mem0\* |

The matrix places the first-pass systems audited under the composite criterion, with SkillOpt, and the contrast entries marked with an asterisk. Every matrix entry that passes the audit sits in [Auto × Auto] or [Auto × Human]: the twelve research systems of the first cell, with SkillForge and CASCADE, are the fourteen research systems of Section V, and Sierra Agent OS 2.0 and Cognition Devin are two of its three industry exemplars. The third exemplar, Letta's Context Repositories, is a second-pass system.

Two placements need a word. DSPy and TextGrad sit in [Auto × None] because their Loop 1 is automated but persists only optimizer state, which only the optimizer-state relaxation of Section S2 would count as a persisted artifact. DGM runs in two modes depending on deployment configuration, archive-based evolution in [Auto × Auto] and sandboxed code-modification review in [Auto × Human], and is listed once, in the dominant cell.

COSPLAY and Cuadros et al., which are first-pass rows, and PACE, CORAL, GEPA, Meta-Harness, MOSS, and RCL, which were classified from their papers after the first pass closed, carry no composite audit, so they are neither placed in the matrix nor counted in Section V. Second-pass systems record their gate pairs in the released score table, and the paragraphs below name those that occupy a cell.

**[Auto × Auto]** is the most populated cell: twelve systems, each with a machine-evaluated criterion on both loops. Speed on both loops is what its members share; cross-organization governance is what every one of them lacks. One second-pass system joins them under the strict audit: Letta's Context Repositories, which push shared memory across agents automatically, with git lineage and no evaluation gate (Section VII). The push is unconditional, an algorithmic promotion with no evaluation threshold, so it sits in the Auto column of Loop 2; the composite audit admits it on its lineage, not on a gate.

**[Auto × Human]** is the production-viable cell. Loop 1 fires at machine speed under an algorithmic criterion, and Loop 2 waits for a person before an edit propagates; the pairing reconciles the speed of automation with a reviewer's accountability. SkillForge is the clearest instance: an LLM judge gates each skill diff on Loop 1, and reviewers decide on Loop 2 whether it ships. CASCADE, Sierra Agent OS 2.0, and Cognition Devin are variants of the same pairing.

Seven second-pass systems promote across users, clients, teams, or repositories without versioning or lineage, so they sit outside the strict audit: EvolveNet, Evo2Team, XRepoSkill, ShareMem, RASO, Spotify's recommendation loop, and Future AGI's prompt lifecycle. Six of them would enter under the governance relaxation, all landing in [Auto × Auto] except Spotify's loop in [Auto × Human], without opening a new cell; the seventh, Future AGI's prompt lifecycle, rests on T5 evidence alone and is not admitted under any rule (Section S2).

**[None × Auto]** holds the governance-first prompts-as-code systems: Braintrust, LangSmith Hub, and Vellum. Their Loop 2 is real, since evaluation-gated CI blocks a promotion on regression. They have no Loop 1 in the patch-local sense, because engineers author the candidate artifacts at their desks and session feedback never triggers one, and the asterisks record exactly that: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated. ExpeL, starred and also marked weak, sits here for a different reason: its experience bank is built from training tasks, which blurs the boundary of its loop, so it fails the audit (Section S4.1.2).

**[Human × Auto]** is empty in both passes, for an engineering reason: when people author the candidates by hand, automated promotion adds little leverage. A plausible occupant would ship expert-authored skills through an automatic held-out evaluation; no published system does.

**[Human × Human]** holds MCP registries and a community hub, second-pass systems in which a person registers an artifact and a person approves its use (Section VII), and, under the same convention, the Anthropic skills repository. None of its occupants has a loop that fires from session signal.

**[Human × None]** is the curation cell, also filled only from the second pass and single-loop by construction. In VerificAgent and similar workflows an agent drafts, a person fact-checks, and the result is frozen (Section VII). Curation stays patch-local, rather than collapsing into an engineer editing a configuration file, because the agent writes each edit and the person only checks it.

### S4.2.2 Closest approaches to governed cross-tenant scaffold optimization

Section IX defines the four properties: (a) an auto-gated Loop 1, (b) cross-organization promotion, (c) versioned lineage with access control, and (d) rollback. The closest approaches split them among themselves:

- **AlphaEvolve** has (a) and a partial (b) confined to one organization; it has no mechanism for promotion across organizations.
- **NanoResearch** has (a) at the research level, and its paper describes no enterprise governance layer.
- **SkillOpt** has (a) fully and a partial (c), through its exported `best_skill.md` artifact and protected slow-update field. Its reported positive transfer across models, harnesses, and benchmarks is an empirical measurement of evidence radius. It implements neither (b) nor explicit rollback (d). The walkthrough in Section S5 maps each of its design decisions onto the loop.
- **CORAL** [@qu2026coral] has a partial (a) through reflection-written shared memory and an automatic Loop 2 through heartbeat-based promotion; it has no (b), no formal access control for (c), and no (d). It is the only system classified before the second pass whose Loop 2 runs asynchronously across multiple agents inside one organization, through shared persistent memory. Evo2Team and ShareMem, second-pass systems, promote across teams and across users without versioning.
- **PACE** [@ling2026pace] has (a) at small-model production timescales and a fast/slow two-timescale pair of loops that consolidates across one deployment's own episodes, not across deployments; it has no (b) and no formal (c) or (d). It is the closest demonstration that the two-loop architecture runs under small-frozen-model constraints.
- **Meta-Harness** [@lee2026metaharness] has (a) over the harness (substrate S5), with a filesystem of candidates that records credit assignment and serves as the accumulated history $H_t$ of Appendix XII. It has no cross-organization promotion, no access control, and no rollback.
- **SkillForge** has (a), a partial (b) that is cross-team within one enterprise, and a partial (c) through VFS commits; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has a partial (a). Its cross-organization promotion is claimed in vendor documentation only and not counted as evidence under the tier rule of Section V, and its GitHub-style Workspaces give some lineage but not access control with rollback in the strict sense.
- **FederatedSkill** [@yang2026federatedskill] has (a) and, with EvolveNet (Table IX-1), the strongest partial (b) among the surveyed systems: heterogeneous clients, each a backbone-plus-harness profile under one federation operator, exchange semantic skill diffs, and a server-side evolution agent applies, adapts, or rejects each patch per client. An auditable decision log, recording source patch, reward, and justification for each modified path, gives a partial (c); there is no access control and no (d).
- **SkillClaw** [@ma2026skillclaw] has a partial (a), through a nightly validation step, and a partial (b) across the users of one shared, synchronized skill repository; it reports no (c) or (d).
- **ChronoMem** [@su2026chronomem] has (d) and the versioning half of (c) for the memory substrate alone: whole-memory snapshots, version histories, and natural-language rollback inside Google's Agent Development Kit. It has no Loop 1, no (b), and no access control.
- **Vellum, Braintrust, and LangSmith Hub** have (c) and (d) explicitly but neither (a) nor (b) in the strict sense; they are governance-first by construction.

No surveyed system combines (b), (c), and (d) under any gate type. The cross-organization governance triad is unfilled on its own, whether or not Loop 1 is auto-gated.

### S4.2.3 Whether the missing architecture should be built

Whether the missing architecture should be built depends on the feedback-signal class, not on the application domain: safety-critical domains such as medical decision support, legal advice, and financial advice, where a reviewer's gate on promotion is a design feature rather than a defect, are judged or delayed domains with high stakes. Section IX gives the argument class by class.

---
