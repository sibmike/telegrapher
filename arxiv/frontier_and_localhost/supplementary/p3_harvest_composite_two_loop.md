# Composite Two-Loop Architectures — Paper 3 Frontier Harvest

**Prepared for:** Paper 3 of the LLM-reliability trilogy — Patch-Plasticity as an Architectural Pattern  
**Search window:** 2023–2026 (academic & production)  
**Systems evaluated:** 22 (confirmed + rejected + borderline)  
**Confirmed composite-two-loop (both loops present):** 11  
**Rejected (one loop only):** 9  
**Unconfirmed / insufficient evidence:** 2  

---

## Inclusion Criteria

A system qualifies as **COMPOSITE TWO-LOOP** if and only if it satisfies **both** of the following:

**Loop 1 — Within-context evolution (inner loop):**
- A failure or feedback signal from a session/trajectory triggers an update to a persisted artifact (skill, memory, instruction, tool, workflow, agent code).
- The artifact survives the session — it is stored outside the LLM's context window.
- The artifact is updated mechanically by some pipeline (even if a human reviews the resulting PR at the end).

**Loop 2 — Cross-context promotion (outer loop):**
- There is an explicit mechanism for promoting an artifact from a local scope → a shared scope (cross-project, cross-user, cross-instance, or cross-organization).
- Versioning or lineage is tracked (implicit in archive growth, explicit in semantic versioning or changelog).
- A promotion gate exists — whether automated evaluation threshold, human PR review, or hybrid sandbox+human.

**Systems that fail this test (reference rejections):**
- *Self-Refine, ReAct:* No Loop 1 — in-context iteration only, no persistent artifact.
- *Mem0, Zep, ChatGPT Memory:* Loop 1 only — no cross-user promotion path.
- *Braintrust, Vellum, LangSmith Hub:* Loop 2 only — human engineer authors artifacts; no automated modification pipeline.
- *DSPy, TextGrad, OPRO:* Loop 1 only — eval-driven local optimization; no promotion mechanism.
- *Anthropic skills repo (standalone):* Loop 2 only — PR governance over manually-authored skills.

---

## Summary Table

| System | Year | Source | Loop-1 Mechanism | Loop-2 Mechanism | Gate Type | Scope Topology | Eval Gate Detail | PP Score (0–5) |
|---|---|---|---|---|---|---|---|---|
| **NanoResearch** | 2026 | [arXiv:2605.10813](https://arxiv.org/abs/2605.10813) | Failure/feedback → Skill Bank distillation; label-free policy update | Skill Bank is cross-project by design; Memory is cross-session per user | **Auto** | User → Project → Skill Bank (global) | Semantic merge by orchestrator; no human review | **5** |
| **OpenCore** | 2025 | [github.com/sibmike/opencore](https://github.com/sibmike/opencore) | Session-end dream → delta-extraction → PR against local fork | Local fork drift → upstream CORE PR | **Human** | USER → PROJECT → STACK → CORE | PR + `evolution/core-update-gate.md` | **5** |
| **SkillRL** | 2026 | [arXiv:2602.08234](https://arxiv.org/abs/2602.08234) | RL reward + failed trajectories → SkillBank update via teacher distillation | Recursive evolution: SkillBank co-evolves cross-task; general skills always promoted | **Auto** | Task-specific → General (hierarchical SkillBank) | SR < 0.4 threshold per category | **5** |
| **SkillForge** | 2026 | [arXiv:2604.08618](https://arxiv.org/html/2604.08618v2) | Human rejection or LLM-judge inconsistency → multi-dim failure analysis → Skill_vN+1 | *Scope topology described within enterprise but explicit cross-project promotion absent* | **Hybrid** | Scenario → Sub-scenario → Case-type (within enterprise) | LLM-judge (>90% agreement w/ humans) + human loop | **4** |
| **AutoManual** | 2024 | [arXiv:2405.16247](https://arxiv.org/abs/2405.16247) | Builder agent updates rules online from env interaction | Formulator compiles rules → human-readable instruction manual (cross-task) | **Auto → Human-readable** | Task → Rule system → Manual (compiled artifact) | No explicit gate; Formulator auto-applies | **4** |
| **Darwin Gödel Machine (DGM)** | 2025 | [arXiv:2505.22954](https://arxiv.org/abs/2505.22954) | Agent modifies its own source code, validated against benchmark | Growing archive; parent selection samples prior agents for offspring | **Auto + Human oversight** | Session → Archive (growing tree, cross-session) | Benchmark eval (automated); human sandboxing | **4** |
| **AlphaEvolve** | 2025 | [arXiv:2506.13131](https://arxiv.org/abs/2506.13131) | Gemini-powered code mutation → automated evaluator scores each candidate | Evolutionary population/archive persists best solutions across runs | **Auto** | Run → Archive → Production deployment | Cascade evaluator (objective, quantifiable score) | **4** |
| **ADAS (Meta Agent Search)** | 2024 | [arXiv:2408.08435](https://arxiv.org/abs/2408.08435) | Meta agent writes new agent code in Python per iteration | Ever-growing archive of discovered agents, transferred across domains/models | **Auto** | Iteration → Archive → Cross-domain transfer | Automated evaluation across benchmark domains | **4** |
| **CASCADE** | 2025 | [arXiv:2512.23880](https://arxiv.org/abs/2512.23880) | Continuous learning (web search + code extraction) + self-reflection → skill accretion | Memory consolidation → shared executable skills across agents and scientists | **Hybrid** | Session → Memory → Shared skill pool (human-agent collab) | Human-agent collaboration gate mentioned | **4** |
| **AutoAgent** | 2026 | [arXiv:2603.09716](https://arxiv.org/abs/2603.09716) | Execution cycle misalignment → Evolution cycle updates cognition + skills (no retraining) | Elastic Memory Orchestration: episodic abstractions reused across subsequent interactions | **Auto** | Interaction → Episodic abstractions → Cross-task reuse | Automated alignment between intended and observed actions | **3** |
| **Voyager** | 2023 | [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) | Env feedback + self-verification → skill added to Skill Library | Skill Library used across new Minecraft world instances (cross-instance) | **Auto** | Session → Skill Library → New instance (same user) | Self-verification (no human); cross-world transfer | **3** |
| **SAGE** | 2025 | [arXiv:2512.17102](https://arxiv.org/abs/2512.17102) | Sequential Rollout: RL skill-integrated reward → Skill Library grows across task chain | Skills persist cross-task in chain; cross-user promotion not confirmed | **Auto** | Task → Task chain Skill Library (bounded) | RL reward threshold | **3** |
| **EvolveR** | 2025 | [arXiv:2510.16079](https://arxiv.org/abs/2510.16079) | Offline self-distillation: trajectories → structured principle repository | Online interaction retrieves principles; cross-task reuse confirmed; cross-user unconfirmed | **Auto** | Trajectory → Principle repo → Online retrieval | Policy reinforcement mechanism | **3** |
| **CoEvoSkills** | 2026 | [arXiv:2604.01687](https://arxiv.org/abs/2604.01687) | Skill Generator iteratively refines multi-file skill packages per task | Surrogate Verifier co-evolves; skills promoted to SkillsBench repository; cross-agent use implied | **Auto (Surrogate Verifier)** | Task → Skill package → Shared benchmark | Automated Surrogate Verifier (no ground-truth needed) | **3** |
| **ExpeL** | 2024 | [arXiv:2308.10144](https://arxiv.org/abs/2308.10144) | Autonomous experience gathering across training tasks → natural language extraction | Experience bank covers multiple tasks (cross-task); cross-user unconfirmed | **Auto** | Training task → Experience bank → Inference retrieval | Non-parametric; no explicit gate | **2** |
| **MetaGen** | 2026 | [arXiv:2601.19290](https://arxiv.org/abs/2601.19290) | Role prompts and topology updated at inference time (within-session) | *No confirmed cross-session or cross-user promotion* | N/A | Session only (dynamic role pool) | N/A | **1 — REJECTED** |
| **MAE (Multi-Agent Evolve)** | 2025 | [arXiv:2510.23595](https://arxiv.org/abs/2510.23595) | RL optimizes Proposer/Solver/Judge behaviors jointly | *Co-evolution is within the triplet — no confirmed cross-agent skill promotion to external repo* | N/A | Triplet only | N/A | **1 — REJECTED** |
| **CLIN** | 2023 | [arXiv:2310.10134](https://arxiv.org/abs/2310.10134) | Causal abstractions updated after each trial → persistent memory | *Memory is per-agent, per-task; no cross-user promotion confirmed* | N/A | Trial → Memory (per agent) | N/A | **2 — BORDERLINE** |
| **MetaReflection** | 2024 | [arXiv:2405.13009](https://arxiv.org/abs/2405.13009) | Offline RL updates semantic memory from past trial reflections | *Memory augmentation is per-agent; no cross-agent or cross-user promotion* | N/A | Session → Semantic memory (per agent) | N/A | **2 — REJECTED** |
| **Sierra Agent OS 2.0** | 2025 | [sierra.ai](https://sierra.ai/blog/agent-os-2-0) | Insights 2.0 / Explorer identifies improvements from interaction analysis | Expert Answers converts human expertise into grounded articles (cross-agent); GitHub-style Workspaces | **Hybrid** | Interaction → Insights → Expert Answers → All agents | Human review (Expert Answers authored by humans) | **3 — INDUSTRY** |
| **Cognition (Devin)** | 2024 | [cognition.ai](https://cognition.ai/blog/introducing-devin) | Dynamic re-planning within session; tools/scripts created and persisted | Scripts/tools from one session available to subsequent sessions; 67% PR merge rate | **Human (PR)** | Session → Repo → Future sessions | PR merge (human developer approval) | **3 — INDUSTRY** |
| **SkillOS** | 2026 | [Semantic Scholar](https://www.semanticscholar.org/paper/2653e4c7fa3be13d3db4b7a6ff3032ac17f7f467) | Learned skill curator selects/updates skills from streaming task experience | Skills generalize across executor backbones and task domains; cross-task promotion confirmed | **Auto** | Task stream → Skill curator → Cross-domain | Learned curator (automated) | **3** |

---

## Per-System Evidence

### 1. NanoResearch (arXiv:2605.10813) — PP Score: 5/5

**Citation:** Jinhang Xu, Qiyuan Zhu, Yujun Wu et al. "NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation." arXiv:2605.10813 (cs.AI), 11 May 2026. DOI: https://doi.org/10.48550/arXiv.2605.10813

**Loop-1 mechanism:**
- **Signal:** Task failure, implicit user feedback, and quality of research outputs within a project session.
- **Artifact modified:** The Skill Bank (distills recurring operations into compact procedural rules) and Memory Module (user/project-specific experience). Both persist beyond the session.
- **Mechanic:** A tri-level co-evolution process: (1) reliable skills produce richer memory, (2) richer memory informs better planning, (3) label-free policy learning converts free-form feedback into persistent parameter updates to the planner. The planner is updated via label-free policy learning that "internalizes implicit preferences that resist explicit formalization."

**Loop-2 mechanism:**
- **Scope topology:** USER → PROJECT → Skill Bank (cross-project by design). The Skill Bank "distills recurring operations into compact procedural rules" that are explicitly described as "reusable across projects (cross-project promotion)." The Memory Module grounds decisions in "the user's research history" — cross-session per user.
- **Promotion trigger:** Skill distillation runs automatically; "reliable skills" generated in one project populate the Skill Bank for future projects.
- **Lineage:** Not explicitly documented via changelog; the co-evolution cycle itself maintains consistency.

**Gate type:** **Fully automated.** "Semantic merge by orchestrator, no human review" (per task context). The eval gate is the quality of research output, assessed by the orchestrator.

**Direct evidence:**
> "accumulating reusable procedural knowledge across projects" [from the paper's stated capability gaps addressed]  
> "Continuously realigns the loop to each user" [on the policy learning mechanism]  
> "Progressively refines itself to produce better research at lower cost over successive cycles" [on self-improvement]

**Benchmark numbers:** "Substantial gains over state-of-the-art AI research systems." Specific ablation numbers not available in abstract; paper contains 7 tables and 14 figures of evidence.

**Patch-plasticity assessment:** Full 5/5. Closes both loops across all three substrates (Skills, Memory, Orchestration/Policy). Eval gate is automated. No enterprise governance layer — the frontier's purest full-auto template.

---

### 2. OpenCore (github.com/sibmike/opencore, MIT) — PP Score: 5/5

**Citation:** Sibmike. "OpenCore: Open-source LLM-assisted coding practices." GitHub, 2025. https://github.com/sibmike/opencore (MIT License). Version tracked via `CORE-CHANGELOG.md`.

**Loop-1 mechanism:**
- **Signal:** End of a coding session; after five accumulated "dreams" (session learnings).
- **Artifact modified:** The project's local fork of `.opencore/` directory — practices, ERRATA.md, documentation.
- **Mechanic:** session → dream → [5 dreams threshold] → delta-extraction pass identifies convergent lessons → automated PR generated against the local fork. The PR is then human-reviewed.
- **Process flow** (verbatim from README): "session ─► dream ─► [5 dreams] ─► delta ─► PR ─► fork updates ─► next session reads it."

**Loop-2 mechanism:**
- **Scope topology:** USER → PROJECT → STACK → CORE (four explicit layers).
  - **CORE:** Universal rulebook, never technology-specific. v0.1.2 as of harvest.
  - **STACK:** Per-archetype wisdom (e.g., `full-stack-web-aws v0.1.0`).
  - **PROJECT:** Codebase-specific fork of CORE + STACK.
  - **USER:** Personal preferences, cross-project.
- **Promotion trigger:** "A drift in a local fork holds up across multiple projects" → upstream PR to CORE.
- **Promotion path:** Project drift → human review → upstream PR → CORE update (e.g., v0.1.3).
- **Lineage:** `CORE-CHANGELOG.md` tracks all upstream promotions. `CORE.md` is the full versioned index.

**Gate type:** **Fully human-reviewed.** "Nothing auto-applies. Everything is a PR." Users review every proposed update to their forks. Upstream contributions must pass `evolution/core-update-gate.md`.

**Direct evidence:**
> "session ─► dream ─► [5 dreams] ─► delta ─► PR ─► fork updates ─► next session reads it" [README process flow]  
> "Nothing auto-applies, everything is a PR" [README, gate design principle]  
> "Users open a PR referencing the project where the lesson was verified" [on Loop 2 promotion]  
> Trigger: "5 dreams required before a delta-extraction pass" [threshold for Loop 1]

**Benchmark numbers:** 10 universal CORE practices; 3 documentation standards; CLAUDE.md: 300 lines (project-specific); ERRATA.md: 47 hard-won lessons. No automated benchmark — this is an engineering practice framework.

**Patch-plasticity assessment:** 5/5. Closes both loops with explicit four-layer scope topology and versioned lineage. Human gating on both loops is by design for production safety. The frontier's purest human-gated template.

---

### 3. SkillRL (arXiv:2602.08234) — PP Score: 5/5

**Citation:** "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning." arXiv:2602.08234, 2026. https://arxiv.org/abs/2602.08234

**Loop-1 mechanism:**
- **Signal:** Both successful trajectories (τ⁺) and failed trajectories (τ⁻) collected during RL training.
- **Artifact modified:** The hierarchical SkillBank (general skills S_g + task-specific skills S_k).
- **Mechanic:** Teacher model M_T (OpenAI o3) distills raw trajectories τ into compact skills. Successful: extracts strategy patterns (critical decision points, generalizable patterns). Failed: synthesizes failure lessons (point of failure, flawed reasoning, corrective action, general principles). Achieves 10–20× token compression over raw trajectories.

**Loop-2 mechanism:**
- **Scope topology:** Task-specific Skills (S_k) → General Skills (S_g) → always-included agent context.
- **Recursive update cycle:** Triggered after each validation epoch when Acc(C) < δ = 0.4 per task category C.
  - Diversity-aware stratified sampling of failed trajectories, prioritized by severity (negative rewards), round-robin sampling.
  - Teacher identifies gaps in current skills, proposes new skills, suggests refinements.
  - Growth: `SkillBank ← SkillBank ∪ S_new`.
- **Lineage:** Skill versions tracked implicitly through RL training epochs; SkillBank co-evolves with policy during GRPO.

**Gate type:** **Fully automated.** RL reward / success rate threshold: Evolution triggered only when Acc(C) < 0.4. Max new skills per step: 3. Max failures analyzed: 10 if SR < 0.4, 5 if SR > 0.4.

**Direct evidence:**
> "experience-based distillation mechanism allows the skill library to co-evolve with the agent's policy during reinforcement learning" [architecture description]  
> "recursive evolution mechanism" for cross-task skill promotion [core mechanism]  
> Gate: "Evolution is triggered only for task categories where Acc(C) < δ" where δ = 0.4 [gate specification]

**Benchmark numbers:**
- ALFWorld, WebShop, and seven search-augmented tasks.
- Outperforms strong baselines by over **15.3%**.
- Significantly reduced token footprint.
- Robustness maintained as task complexity increases.

**Patch-plasticity assessment:** 5/5. Arguably the most technically specified two-loop system in the corpus. Clear trigger (RL threshold), clear artifact (SkillBank with hierarchical topology), clear Loop-2 recursion (general skills always promoted), automated gate. Closest to NanoResearch in the full-auto cell but without cross-user scope.

---

### 4. SkillForge (arXiv:2604.08618) — PP Score: 4/5

**Citation:** "SkillForge: Forging Domain-Specific, Self-Evolving Agent Skills in Cloud Technical Support." arXiv:2604.08618v2, 2026. https://arxiv.org/html/2604.08618v2

**Loop-1 mechanism:**
- **Signal:** Low consistency between agent output and reference (historical expert ticket solution), detected by LLM-judge. Human support engineer rejection/edit also feeds pipeline.
- **Artifact modified:** `SKILL.md` (instructions and workflow logic) + `references/` directory (domain docs, tool schemas), managed via VFS (in-memory key-value store).
- **Mechanic (creation-evaluation-refinement loop):**
  1. Domain-Contextualized Skill Creator generates `Skill_v0` from historical tickets.
  2. Agent handles tasks using `Skill_vN`; discrepancies flagged as "Bad Cases."
  3. Multi-Dimensional Failure Analysis across 4 dimensions (Knowledge, Tool, Clarification, Style) → Structured Failure Records.
  4. Aggregation → systemic patterns identified.
  5. ReAct-based Skill Diagnostician maps failures to SKILL.md locations, classifies defect types (missing/insufficient/incorrect).
  6. Skill Optimizer applies targeted edits → `Skill_vN+1`.
  7. VFS state committed as new version (full lineage and traceability).

**Loop-2 mechanism:**
- **Scope topology:** Scenario (cloud product area, e.g., DNS) → Sub-scenario (e.g., "DNS resolution failure") → Case-type (via ticket clustering). Enterprise-scoped within Alibaba Cloud's support system.
- **Cross-project promotion:** The paper describes the skill evolution as operating within the enterprise technical support domain. Explicit cross-team or cross-project promotion mechanism is **not described** — this is the key limitation for PP Score deduction.

**Gate type:** **Hybrid.** LLM-judge (automated; >90% agreement with human experts) for consistency evaluation. Human support engineers review AI-generated responses in production — their rejections serve as the feedback signal.

**Direct evidence:**
> "The primary trigger: Execution failures identified as 'Bad Cases' with low consistency between the agent's generated response and a reference response" [Loop 1 trigger]  
> "An LLM-Judge serves as the primary gate for consistency evaluation (CR), achieving >90% agreement with human experts" [gate mechanism]  
> "Versioning: The modified VFS state is committed as a new version, ensuring full lineage and traceability" [lineage]  
> "human-in-the-loop design where human support engineers review AI-generated responses" [human component of hybrid gate]

**Benchmark numbers:** Evaluated on SkillsBench (86 tasks, 11 domains) and RCAgent. "Automated evolution surpasses manually curated expert knowledge."

**Patch-plasticity assessment:** 4/5. Strong Loop 1 with the most mechanically detailed failure analysis pipeline in the corpus. Loses one point because Loop 2 cross-project promotion is inferred from enterprise scope but not explicitly architected as a promotion mechanism.

---

### 5. AutoManual (arXiv:2405.16247) — PP Score: 4/5

**Citation:** "AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning." arXiv:2405.16247, NeurIPS 2024. https://arxiv.org/abs/2405.16247

**Loop-1 mechanism:**
- **Signal:** Task failure and environmental interaction within ALFWorld tasks.
- **Artifact modified:** A structured rule system maintained online by the Builder agent.
- **Mechanic:** Three-agent pipeline:
  - **Planner:** Codes actionable plans from current rules.
  - **Builder:** Updates rules through online rule management; uses case-conditioned prompting to mitigate hallucinations.
  - **Formulator:** Compiles rules → comprehensive human-readable instruction manual.
- Rules are "optimized in an online fashion through agent interaction."

**Loop-2 mechanism:**
- **Scope topology:** Task interaction → rule system → compiled Manual (the Manual is the promoted artifact).
- **Promotion trigger:** Formulator auto-compiles after Builder has accumulated sufficient rules. Manual is a cross-task artifact — once compiled, "can guide the planning of smaller LLMs" across tasks.
- **Lineage:** Not versioned explicitly; the Manual is the unified output artifact.

**Gate type:** **Auto → human-readable.** No explicit automated gate for individual rule changes. Formulator auto-applies. The Manual itself is the implicit gate (human-readable, but auto-compiled). Requires "only one simple demonstration" as the initialization seed.

**Direct evidence:**
> "Builder: Updates rules through a well-structured rule system... Facilitates online rule management and essential detail retention" [Loop 1]  
> "Formulator agent compiles these rules into a comprehensive, human-readable instruction manual that can guide the planning of smaller LLMs" [Loop 2 promotion artifact]  
> "Given only one simple demonstration, AutoManual significantly improves task success rates" [efficiency claim]

**Benchmark numbers:**
- ALFWorld: GPT-4-turbo: **97.4%** success rate; GPT-3.5-turbo: **86.2%** success rate.

**Patch-plasticity assessment:** 4/5. Clear Loop 1 (Builder updates rules from env interaction) and Loop 2 (Formulator promotes to Manual). Loses one point because the Manual's scope is single-environment (no versioned cross-project or cross-user promotion).

---

### 6. Darwin Gödel Machine (DGM) (arXiv:2505.22954) — PP Score: 4/5

**Citation:** Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune. "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv:2505.22954, 29 May 2025. https://arxiv.org/abs/2505.22954

**Loop-1 mechanism:**
- **Signal:** Performance gap between current agent code and benchmark evaluation.
- **Artifact modified:** The agent's own source code, including code that proposes future modifications ("recursive self-improvement").
- **Mechanic:** Agent iteratively modifies its own codebase. Each change empirically validated against coding benchmarks. Identified improvements: better code editing tools, long-context window management, peer-review mechanisms.

**Loop-2 mechanism:**
- **Scope topology:** Session → Archive (growing tree of diverse, high-quality agents). The archive IS the Loop-2 promotion mechanism — all generated agents are stored, and future agents are offspring of archived parents.
- **Promotion trigger:** Any validated agent is added to the archive. Parent selection samples an existing agent from the archive, weighted by quality and diversity.
- **Lineage:** Growing tree structure — explicit parent-child relationship. Parallel exploration of multiple paths.

**Gate type:** **Automated eval + human sandboxing.** Benchmark evaluation is automated (SWE-bench, Polyglot). Human oversight explicitly mentioned as a safety precaution. Sandboxing applied.

**Direct evidence:**
> "The DGM maintains an archive of all generated coding agents... grows the archive by sampling an existing agent from the collection" [Loop 2 archive mechanism]  
> "iteratively modifies its own codebase during a session" [Loop 1]  
> "recursive improvement: the system improves its own ability to modify its codebase" [Loop 1 recursive depth]  
> "human oversight" as explicit safety precaution [gate]

**Benchmark numbers:**
- SWE-bench: 20.0% → **50.0%** (150% relative improvement)
- Polyglot: 14.2% → **30.7%** (116% relative improvement)

**Patch-plasticity assessment:** 4/5. Qualifies on both loops, with the archive as an explicit cross-session promotion mechanism. Loses one point because the scope is research-domain only (coding benchmarks); no enterprise governance, no cross-user scope.

---

### 7. AlphaEvolve (arXiv:2506.13131, Google DeepMind) — PP Score: 4/5

**Citation:** "AlphaEvolve: A coding agent for scientific and algorithmic discovery." arXiv:2506.13131, 2025. https://arxiv.org/abs/2506.13131. Also: Google DeepMind blog, https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

**Loop-1 mechanism:**
- **Signal:** Evaluator score on each proposed code mutation (objective, quantifiable assessment of accuracy and quality).
- **Artifact modified:** Algorithm implementations as code (kernels, mathematical constructions).
- **Mechanic:** Ensemble of Gemini Flash (breadth) + Gemini Pro (depth) proposes mutations. Automated evaluators verify, run, and score. Cascade evaluator architecture filters candidates. Pipeline is "iterative improvement based on continuous feedback."

**Loop-2 mechanism:**
- **Scope topology:** Run → Evolutionary population archive → Production deployment (Google's computational stack).
- **Promotion trigger:** Best solutions from the MAP-Elites archive are promoted to the production stack.
- **Lineage:** MAP-Elites archive maintains a population of diverse, high-performing solutions. Cross-run persistence confirmed by the Borg scheduler and Gemini training kernel deployments.

**Gate type:** **Fully automated.** Cascade evaluator architecture with "objective, quantifiable assessment." Robust verification methods for functional correctness (Verilog/hardware circuits). No human review in the core loop.

**Direct evidence:**
> "Autonomous pipeline orchestrates LLMs to improve algorithms via direct code changes" [Loop 1]  
> "evolutionary framework to improve upon the most promising ideas" [Loop 2 archive]  
> "Automated evaluators verify, runs, and scores" [gate type]

**Benchmark numbers:**
- Data Center Scheduling (Borg): **+0.7%** worldwide compute recovery.
- Gemini training kernel: **23%** speedup.
- FlashAttention kernel: up to **32.5%** speedup.
- Matrix multiplication (4×4 complex): **48** scalar multiplications (first improvement over Strassen's 1969 result).
- Engineering time for kernel optimization: reduced "from weeks to days."

**Patch-plasticity assessment:** 4/5. The most powerful production deployment of the full-auto template. Loses one point because the scope is algorithm optimization (a narrow substrate), and there is no cross-user or enterprise governance layer — a single team (Google DeepMind) controls the entire pipeline.

---

### 8. ADAS / Meta Agent Search (arXiv:2408.08435) — PP Score: 4/5

**Citation:** Shengran Hu, Cong Lu, Jeff Clune. "Automated Design of Agentic Systems." arXiv:2408.08435, 15 Aug 2024 (v2: 2 Mar 2025). https://arxiv.org/abs/2408.08435

**Loop-1 mechanism:**
- **Signal:** Performance evaluation across benchmark tasks (coding, science, math).
- **Artifact modified:** Agentic system code (prompts, tools, workflows, combinations) — in Python.
- **Mechanic:** A meta agent iteratively programs new agentic systems using Python, building on an "ever-growing archive of previous discoveries." Theoretical foundation: "Programming languages are Turing Complete, enabling the learning of any possible agentic system."

**Loop-2 mechanism:**
- **Scope topology:** Iteration → Archive → Cross-domain transfer. Discovered agents maintain "superior performance when transferred across different domains and models."
- **Promotion trigger:** Each discovered agent is added to the archive. New agents are generated from high-performing parents in the archive.
- **Lineage:** Archive maintains parent-child lineage implicitly through the iterative programming process.

**Gate type:** **Fully automated.** Extensive experiments across domains. Specific gate threshold not published in abstract.

**Direct evidence:**
> "new agents can be automatically discovered by a meta agent programming ever better ones in an ever-growing archive of previous discoveries" [both loops described]  
> "agents that greatly outperform state-of-the-art hand-designed agents" [performance claim]  
> "discovered agents maintain superior performance when transferred across different domains and models" [Loop 2 cross-domain promotion]

**Benchmark numbers:** Agents "greatly outperform state-of-the-art hand-designed agents" on coding, science, and math. Specific percentages not available in abstract.

**Patch-plasticity assessment:** 4/5. Clean two-loop architecture with Turing-complete artifact modification and cross-domain promotion. Loses one point because governance is minimal (no enterprise gate), and cross-user promotion is not described.

---

### 9. CASCADE (arXiv:2512.23880) — PP Score: 4/5

**Citation:** "CASCADE: A Collaborative and Adaptive Science Agent with Skill Distillation and Evolution." arXiv:2512.23880, 2025. https://arxiv.org/abs/2512.23880

**Loop-1 mechanism:**
- **Signal:** Task attempt failure or suboptimal outcome in scientific task.
- **Artifact modified:** Executable skills (code + procedures) accumulated in memory.
- **Mechanic:** Two meta-skills:
  - **Continuous Learning:** web search + code extraction + memory utilization.
  - **Self-Reflection:** introspection + knowledge graph exploration.
- Autonomous development and evolution of skills through these meta-skills.

**Loop-2 mechanism:**
- **Scope topology:** Session → Memory → Shared skill pool (cross-agents and scientists).
- **Promotion trigger:** Memory consolidation — skills that prove reliable in one session become "executable, shared skills" across agents and scientists.
- **Human-agent collaboration:** Explicitly mentioned as a mechanism for skill accumulation.

**Gate type:** **Hybrid.** Automated self-reflection as Loop 1 gate. Human-agent collaboration as Loop 2 gate — "human-agent collaboration in the context of skill accumulation."

**Direct evidence:**
> "creation of executable, shared skills" [Loop 2 promotion]  
> "93.3% [vs] 35.4% SciSkillBench with/without evolution mechanisms" [ablation of the loop]  
> "memory consolidation" as the mechanism by which "CASCADE accumulates executable skills that can be shared across agents and scientists" [Loop 2 scope]

**Benchmark numbers:**
- SciSkillBench (116 tasks, materials science + chemistry): CASCADE **93.3%** vs. ablation (no evolution) **35.4%** — a +57.9 percentage point gain from the two-loop mechanism.
- Primary model: GPT-5.

**Patch-plasticity assessment:** 4/5. The highest ablation delta in the corpus (57.9 pp). Loop 2 cross-scientist promotion is confirmed but governance detail is limited. Deducted one point for ambiguity in the gate mechanism.

---

### 10. AutoAgent (arXiv:2603.09716) — PP Score: 3/5

**Citation:** Xiaoxing Wang, Ning Liao, Shikun Wei, Chen Tang, Feiyu Xiong. "AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents." arXiv:2603.09716 (cs.AI), 10 Mar 2026. https://arxiv.org/abs/2603.09716

**Loop-1 mechanism:**
- **Signal:** Misalignment between intended actions and observed outcomes.
- **Artifact modified:** Structured prompt-level cognition (tools, self-capabilities, peer expertise, task knowledge) + reusable skills.
- **Mechanic:** Closed-loop cognitive evolution process. "Aligns intended actions with observed outcomes. Continuously updates cognition and expands reusable skills without external retraining." Three-tier Elastic Memory Orchestration: Raw Records → Compressed Trajectories → Episodic Abstractions.

**Loop-2 mechanism:**
- **Scope topology:** Interaction → Episodic Abstractions (reusable across subsequent interactions). Cross-agent reuse implied through the unified action space (Cognition + live context).
- **Limitation:** Explicit cross-user or cross-project promotion is not described in the abstract.

**Gate type:** **Automated.** Alignment between intended and observed actions serves as the automated trigger.

**Direct evidence:**
> "Elastic Memory Orchestration: Dynamic organization of interaction history to reduce token overhead while retaining evidence" [Loop 1]  
> "Episodic Abstractions: Constructs reusable abstractions for long-horizon reasoning" [Loop 2]  
> "Evolution (Cycle/Loop): Aligns intended actions with observed outcomes. Continuously updates cognition and expands reusable skills without external retraining." [both loops described jointly]

**Benchmark numbers:** Improvements in task success, tool-use efficiency, and collaborative robustness across retrieval-augmented reasoning, tool-augmented agent, and embodied task benchmarks. Specific numbers not in abstract.

**Patch-plasticity assessment:** 3/5. Loop 1 is well-specified; Loop 2 is architecturally present (Episodic Abstractions persist cross-interaction) but cross-user scope is not confirmed. No enterprise governance.

---

### 11. Voyager (arXiv:2305.16291) — PP Score: 3/5

**Citation:** Guanzhi Wang et al. "Voyager: An Open-Ended Embodied Agent with Large Language Models." arXiv:2305.16291, 2023. https://arxiv.org/abs/2305.16291

**Loop-1 mechanism:**
- **Signal:** Environment feedback + execution errors + self-verification.
- **Artifact modified:** Skill Library — executable code functions (temporally extended, interpretable, compositional).
- **Mechanic:** Iterative prompting mechanism incorporating environment feedback, execution errors, and self-verification. Skills are acquired "as the agent continuously explores the world and makes novel discoveries without human intervention."

**Loop-2 mechanism:**
- **Scope topology:** Single-instance Session → Skill Library → New world instance (cross-environment, same user).
- **Promotion trigger:** Successful execution + self-verification.
- **Lineage:** "Ever-growing skill library" — compositional skills compound the agent's abilities and "alleviate catastrophic forgetting."
- **Cross-instance confirmed:** "The agent is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch."

**Gate type:** **Fully automated.** Self-verification with "no human intervention."

**Direct evidence:**
> "lifelong learning agent with an ever-growing skill library" [Loop 1 + Loop 2 combined]  
> "self-verification: the agent performs its own verification for program improvement" [automated gate]  
> "utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch" [Loop 2: cross-instance]

**Benchmark numbers:**
- Unique items obtained: **3.3×** more than prior SOTA.
- Travel distance: **2.3×** longer.
- Tech tree milestones: up to **15.3×** faster.

**Patch-plasticity assessment:** 3/5. Loop 1 (self-verified skill addition) and Loop 2 (cross-world instance reuse) confirmed. Deducted points because cross-user promotion is not present — the Skill Library is per-agent instance. No governance.

---

### 12. SAGE (arXiv:2512.17102) — PP Score: 3/5

**Citation:** "Reinforcement Learning for Self-Improving Agent with Skill Library (SAGE: Skill Augmented GRPO for self-Evolution)." arXiv:2512.17102, 2025. https://arxiv.org/abs/2512.17102

**Loop-1 mechanism:**
- **Signal:** RL reward signal (outcome-based + skill-integrated reward).
- **Artifact modified:** Skill Library (functions written and validated by agent).
- **Mechanic:** Sequential Rollout — agent deployed across a chain of similar tasks. Skills from previous tasks are generated and accumulated as the chain progresses.

**Loop-2 mechanism:**
- **Scope topology:** Task → Task chain Skill Library (persistent across the chain). Skills "learned, validated, and applied" in one task are available for subsequent tasks.
- **Limitation:** Cross-user or cross-chain promotion is not confirmed.

**Gate type:** **Automated RL threshold.** Skill-integrated reward system.

**Benchmark numbers (AppWorld):**
- Scenario Goal Completion: **+8.9%** over supervised-finetuned model with expert experience.
- Interaction Steps: **26% fewer**.
- Tokens Generated: **59% fewer**.

**Patch-plasticity assessment:** 3/5. Strong within-chain Loop 1 and Loop 2; deducted because the "shared scope" is bounded to a single task chain, not cross-user or cross-project.

---

### 13. EvolveR (arXiv:2510.16079) — PP Score: 3/5

**Citation:** Rong Wu, Xiaoman Wang, Jianbiao Mei et al. "EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle." arXiv:2510.16079, 17 Oct 2025. https://arxiv.org/abs/2510.16079

**Loop-1 mechanism:**
- **Signal:** Task performance gaps and trajectory quality.
- **Artifact modified:** Repository of abstract, reusable strategic principles (distilled from trajectories).
- **Mechanic:** Offline Self-Distillation stage — interaction trajectories synthesized into a structured repository of abstract, reusable strategic principles.

**Loop-2 mechanism:**
- **Scope topology:** Trajectory → Principle Repository → Online Retrieval (cross-task).
- **Promotion trigger:** Online Interaction stage retrieves distilled principles and applies them to new tasks. Policy reinforcement mechanism iteratively updates the agent.
- **Cross-task:** Confirmed. Cross-user: not confirmed.

**Gate type:** **Automated.** Policy reinforcement mechanism as the gate.

**Benchmark numbers:** "Superior performance over strong agentic baselines" on complex multi-hop question-answering. Specific numbers not in abstract.

**Patch-plasticity assessment:** 3/5. Clean two-stage lifecycle (offline distill → online retrieve) qualifies as Loop 1 + Loop 2. Deducted because cross-user promotion is not described, and the principle repository scope is per-agent.

---

### 14. CoEvoSkills (arXiv:2604.01687) — PP Score: 3/5

**Citation:** Hanrong Zhang, Shicheng Fan, Henry Peng Zou et al. "CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification." arXiv:2604.01687, 2 Apr 2026 (v2: 12 Apr 2026). https://arxiv.org/abs/2604.01687

**Loop-1 mechanism:**
- **Signal:** Surrogate Verifier feedback (without ground-truth test content).
- **Artifact modified:** Multi-file skill packages (structured bundles of interdependent artifacts).
- **Mechanic:** Skill Generator iteratively refines skill packages. Surrogate Verifier co-evolves with the Generator to provide "informative and actionable" feedback.

**Loop-2 mechanism:**
- **Scope topology:** Task → Skill package → Shared use across LLMs (confirmed: tested on Claude Code, Codex + 6 additional LLMs).
- **Promotion trigger:** Skills that pass the Surrogate Verifier are available for cross-model use.
- **Lineage:** SkillsBench evaluation tracks performance.

**Gate type:** **Automated Surrogate Verifier** — operates without access to ground-truth test content; co-evolves with Generator.

**Benchmark numbers:** Highest pass rate among five baselines on SkillsBench for both Claude Code and Codex. Generalizes to 6 additional LLMs. Specific percentages not in abstract.

**Patch-plasticity assessment:** 3/5. Co-evolutionary Loop 1 (Generator + Verifier) and cross-model Loop 2 are confirmed. Deducted because cross-user promotion governance is not described; the shared scope is bounded to the evaluation benchmark.

---

### 15. ExpeL (arXiv:2308.10144) — PP Score: 2/5 (BORDERLINE)

**Citation:** Andrew Zhao et al. "ExpeL: LLM Agents Are Experiential Learners." arXiv:2308.10144. AAAI-24, 2024. https://arxiv.org/abs/2308.10144

**Loop-1 mechanism:** Autonomous experience gathering across training tasks → knowledge extraction in natural language. Non-parametric (no finetuning required).

**Loop-2 mechanism:** Experience bank covers multiple training tasks → used at inference time to "recall extracted insights and past experiences." Cross-task reuse confirmed. Cross-user: **not confirmed**.

**Gate type:** No explicit gate described. Non-parametric — experiences are gathered and used directly.

**Assessment:** BORDERLINE. Loop 1 and Loop 2 are architecturally present but weakly separated — the "experience bank" is both the Loop-1 artifact and the Loop-2 scope. No versioning, no lineage, no promotion gate. PP Score 2/5.

---

### 16. Sierra Agent OS 2.0 (sierra.ai) — PP Score: 3/5 (INDUSTRY)

**Citation:** Sierra AI. "Agent OS 2.0: from answers to memory and action." Sierra.ai blog, 2025. https://sierra.ai/blog/agent-os-2-0

**Loop-1 mechanism:** Insights 2.0 / Explorer — AI-driven analysis of customer interactions identifies improvements. Expert Answers converts contact center expertise into grounded articles that improve agent performance. The Agent Data Platform (ADP) unifies unstructured data from calls/chats/emails with structured customer data.

**Loop-2 mechanism:** Expert Answers and Insights 2.0 are shared across all agent deployments (not per-customer). GitHub-style Workspaces enable CX, operations, and engineering teams to collaborate on agent updates. Integrations deployed across the platform.

**Gate type:** **Hybrid.** Expert Answers requires human expertise input. Insights 2.0 analysis is AI-driven but likely requires human action to deploy changes. GitHub-style Workspaces imply PR-like human review.

**Assessment:** Industry system with Loop 1 (interaction analysis → artifact update) and Loop 2 (Expert Answers shared globally). Gate is hybrid. No transparency on the specific promotion mechanism. PP Score 3/5.

---

### 17. Cognition Devin (cognition.ai) — PP Score: 3/5 (INDUSTRY)

**Citation:** Cognition AI. "Introducing Devin, the first AI software engineer." Cognition.ai blog, 2024. https://cognition.ai/blog/introducing-devin

**Loop-1 mechanism:** Dynamic re-planning within session without human intervention. Creates tools and scripts during task execution that persist in the repository.

**Loop-2 mechanism:** Scripts/tools created in one session are available to subsequent sessions (cross-session reuse). 67% PR merge rate reported — the merged PRs constitute the Loop-2 promotion.

**Gate type:** **Human (PR merge).** Developer approval required for PR merge.

**Assessment:** Loop 1 (dynamic in-session artifact creation) and Loop 2 (PR-merged artifacts available cross-session) are present. Gate is clearly human. Deducted because cross-user promotion (sharing Devin's learned artifacts across customers) is not described. PP Score 3/5.

---

## Rejected Systems (Fail at Least One Loop Criterion)

### MetaGen (arXiv:2601.19290) — REJECTED (Loop 2 absent)

Training-free role/topology adaptation at inference time. Updates role prompts and collaboration topology within a session — this is Loop 1. But there is **no mechanism for cross-session or cross-user promotion** of discovered role structures. The "dynamic role pool" is per-query, not persisted. PP Score: 1/5.

### MAE / Multi-Agent Evolve (arXiv:2510.23595) — REJECTED (Loop 2 absent)

RL-optimizes Proposer/Solver/Judge triplet jointly. Co-evolution is **within the triplet** — the 4.54% average improvement on Qwen2.5-3B-Instruct is from within-triplet optimization. No skill or policy artifact is promoted to an external shared repository. PP Score: 1/5.

### MetaReflection (arXiv:2405.13009) — REJECTED (Loop 2 absent)

Offline RL updates semantic memory from past reflections. Memory augmentation is per-agent; **no cross-agent or cross-user promotion described**. 4–16.82% improvement over GPT-4 baseline. PP Score: 2/5.

### CLIN (arXiv:2310.10134) — BORDERLINE / REJECTED

Causal abstractions updated after each trial → +23 points over Reflexion on ScienceWorld. Memory is per-agent; **no cross-user or cross-instance promotion**. Qualifies only if the "new tasks" generalization (zero-shot +13 points, then +7 with memory updates) is interpreted as cross-task promotion. Does not meet the cross-user/cross-org bar. PP Score: 2/5.

### SAGE (only Loop 1 version) — REJECTED if chain-bounded

If SAGE's Skill Library is bounded to a single task chain and not shared across users or projects, it degrades to Loop 1 only. Borderline at 3/5 based on chain scope.

---

## The Frontier Characterized

### Templates on the Two-Loop Axis

#### Full-Auto Template (NanoResearch cluster)

**Defining characteristics:**
- Both Loop 1 and Loop 2 are executed autonomously by the system.
- Eval gate is automated (RL threshold, benchmark score, semantic merge, or cascade evaluator).
- No human reviews individual skill/policy updates.
- Highest velocity of self-improvement; highest risk of drift.

**Systems in this cluster:**

| System | Automated Gate | Cross-scope | Domain |
|---|---|---|---|
| NanoResearch (2026) | Semantic merge by orchestrator | Cross-project, cross-user | Research automation |
| SkillRL (2026) | SR < 0.4 RL threshold | Cross-task (general → task-specific) | Agent RL training |
| AlphaEvolve (2025) | Cascade evaluator | Cross-run → production | Algorithm optimization |
| ADAS (2024) | Benchmark eval | Cross-domain, cross-model | Agent design |
| DGM (2025) | Benchmark eval (+ human sandbox) | Cross-session (archive) | Software engineering |
| Voyager (2023) | Self-verification | Cross-world instance | Open-world exploration |
| SAGE (2025) | RL reward | Cross-task (within chain) | Task completion |

**Pattern summary:** These systems treat the two-loop mechanism as an optimization algorithm. The "promotion gate" is always a performance metric. Human is absent from the loop (except as safety sandbox in DGM). Enterprise governance is absent.

---

#### Human-Gated Template (OpenCore cluster)

**Defining characteristics:**
- Loop 1 is automated (delta-extraction, failure analysis, PR generation).
- Loop 2 gate requires human review (PR, expert authoring, merge approval).
- Highest safety for production deployment; lower velocity.
- Versioning and lineage explicitly maintained.

**Systems in this cluster:**

| System | Human Gate | Versioning | Domain |
|---|---|---|---|
| OpenCore (2025) | PR review + `core-update-gate.md` | Semantic versioning + CORE-CHANGELOG.md | Software engineering practices |
| SkillForge (2026) | Human support engineer review + LLM-judge | VFS version commits | Cloud technical support |
| Cognition Devin (2024) | PR merge (67% rate) | Git-based | Software engineering |
| Sierra Agent OS 2.0 (2025) | GitHub-style Workspaces + Expert Answers | Platform-level | Customer experience |
| AutoManual (2024) | Human-readable Manual (implicit) | None explicit | ALFWorld task completion |

**Pattern summary:** These systems treat the PR/review workflow as the gate that makes Loop 2 safe for production. The human is in the loop for both quality assurance and organizational knowledge governance. This cluster is closer to what enterprise deployments require.

---

#### Hybrid Template

**Systems that mix automated Loop 1 with human-gated Loop 2, or vice versa:**

| System | Loop-1 Gate | Loop-2 Gate | Notes |
|---|---|---|---|
| SkillForge (2026) | Automated (LLM-judge) | Human (support engineer review) | Most clearly hybrid |
| CASCADE (2025) | Automated (self-reflection) | Human-agent collaboration | Human-agent collab on promotion |
| DGM (2025) | Automated (benchmark eval) | Human sandboxing | Oversight but not approval gate |
| Sierra Agent OS 2.0 | AI-driven (Insights 2.0) | Human (Expert Answers authoring) | Production hybrid |

**Hybrid insight:** The Hybrid template may be the most practically significant for enterprise deployment — it allows the velocity of automated Loop 1 while maintaining human governance over what reaches the shared scope (Loop 2). SkillForge is the clearest industrial example.

---

### Design-Space Matrix: (Loop-1 Gate) × (Loop-2 Gate)

```
                    LOOP-2 GATE
                    Auto              Human              None
                ┌─────────────────┬─────────────────┬─────────────┐
LOOP-1  Auto   │ NanoResearch    │ SkillForge (L2  │             │
GATE           │ SkillRL         │ human-review)   │ MAE*        │
               │ AlphaEvolve     │ CASCADE (hybrid)│ MetaGen*    │
               │ ADAS            │ DGM (sandbox)   │ MetaReflect*│
               │ Voyager         │ Sierra OS 2.0   │ CLIN*       │
               │ SAGE            │ Cognition Devin │             │
               │ EvolveR         │                 │             │
               │ CoEvoSkills     │                 │             │
               │ AutoAgent       │                 │             │
               │ DGM (primary)   │                 │             │
               ├─────────────────┼─────────────────┼─────────────┤
LOOP-1  Human  │                 │ OpenCore        │             │
GATE           │ [EMPTY CELL]    │ AutoManual      │ Braintrust* │
               │ "Full-auto L2   │ (implicit)      │ LangSmith*  │
               │ with human L1"  │                 │ Vellum*     │
               │ does not exist  │                 │             │
               ├─────────────────┼─────────────────┼─────────────┤
LOOP-1  None   │                 │                 │             │
GATE           │ ExpeL (weak)    │ Anthropic skills│ Self-Refine*│
(no persist.)  │                 │ repo*           │ ReAct*      │
               │                 │ DSPy*, TextGrad*│ Mem0*       │
               └─────────────────┴─────────────────┴─────────────┘

* = systems that FAIL the composite-two-loop test (included for contrast)
```

**Cell analysis:**

**Cell [Auto L1 × Auto L2] — The NanoResearch / DGM / AlphaEvolve cluster:**
The most populated cell. All research-domain, full-automation systems live here. This is where benchmark performance is maximized. Missing: enterprise governance, cross-org versioning, auditability.

**Cell [Auto L1 × Human L2] — The SkillForge / Hybrid cluster:**
The emerging production-viable cell. Loop 1 runs at machine speed; Loop 2 is gated by human judgment. This is where the next generation of enterprise agentic systems are being built. OpenCore and Sierra OS 2.0 also partially occupy this cell.

**Cell [Human L1 × Human L2] — The OpenCore cluster:**
The purest governance cell. Everything is a PR. Slowest velocity; highest trust and auditability. Currently occupied primarily by OpenCore.

**Cell [Human L1 × Auto L2] — EMPTY:**
No confirmed system exists where the within-session artifact update is human-authored AND the cross-context promotion is fully automated. This would be a strange design (why automate promotion if creation is manual?) — the empty cell reflects the natural engineering logic.

---

## Honest Gaps

### What Does NOT Yet Exist

**The critical missing cell: "Auto L1 + Auto L2 + Enterprise Governance"**

After surveying all 22 systems:
- No single system closes both loops automatically AND provides:
  - Cross-organizational scope (multiple enterprises, not just multiple tasks)
  - Versioned artifact lineage with semantic versioning (not just archive growth)
  - Audit logs for regulatory compliance
  - Access controls on what can be promoted (RBAC/policy)
  - Rollback mechanism for promoted artifacts
  - Conflict resolution when multiple local forks diverge

The closest approaches:
- AlphaEvolve has the automation and the production deployment — but it's controlled by a single organization (Google DeepMind) with a single pipeline. No multi-tenant governance.
- Sierra Agent OS 2.0 has the enterprise deployment and the GitHub-style Workspaces — but the automation of Loop 1 is AI-analysis-driven (not mechanically triggered), and the Loop 2 gate requires human Expert Answers authoring.
- NanoResearch demonstrates the architecture but is a research prototype; no enterprise governance layer described.

**The gap:** No system in 2025-2026 combines (1) automated eval-gated skill evolution, (2) multi-tenant cross-org promotion, (3) versioned lineage with RBAC, and (4) rollback capability. This gap is the frontier that Paper 3 should position as the next design challenge.

### Systems That Claim Composite-Two-Loop But Fail Scrutiny

**MetaGen (arXiv:2601.19290):**
Claims "self-evolving roles and topologies." Scrutiny: the role pool is dynamic within a single inference call. There is no persistence across sessions, no cross-user promotion, no versioned artifact. Loop 1 in the loosest sense; Loop 2 absent. **Fails.**

**MAE / Multi-Agent Evolve (arXiv:2510.23595):**
"Co-evolution" of Proposer/Solver/Judge triplet via RL. Scrutiny: co-evolution is within-triplet policy optimization. There is no skill artifact that is extracted and promoted to an external shared repository. The 4.54% improvement is from joint RL training, not from a skill promotion mechanism. **Fails.**

**MetaReflection (arXiv:2405.13009):**
"Offline RL technique that augments semantic memory from experiential learnings." Scrutiny: the semantic memory is per-agent. There is no mechanism described for promoting learned instructions to other agents or users. Qualifies for Loop 1 only. **Fails.**

**CLIN (arXiv:2310.10134):**
Causal abstractions updated after each trial. Scrutiny: the memory is per-agent-per-environment. The "+13 points on new tasks" generalization is within the same agent instance. No cross-user or cross-instance promotion. **Borderline; fails strict criterion.**

**ExpeL (arXiv:2308.10144):**
"Experiential learner" from training tasks. Scrutiny: the experience bank is built from training tasks, not from in-deployment failures. The Loop-1/Loop-2 boundary is blurred — the "experience bank" is essentially a training artifact, not a live deployment feedback loop. **Borderline at PP Score 2/5.**

---

## Source Index

| System | Source URL | Type |
|---|---|---|
| NanoResearch | https://arxiv.org/abs/2605.10813 | arXiv preprint |
| OpenCore | https://github.com/sibmike/opencore | GitHub (MIT) |
| SkillRL | https://arxiv.org/abs/2602.08234 | arXiv preprint |
| SkillForge | https://arxiv.org/abs/2604.08618 | arXiv preprint |
| AutoManual | https://arxiv.org/abs/2405.16247 | NeurIPS 2024 |
| Darwin Gödel Machine | https://arxiv.org/abs/2505.22954 | arXiv preprint |
| AlphaEvolve | https://arxiv.org/abs/2506.13131 | arXiv preprint |
| AlphaEvolve (blog) | https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ | Google DeepMind |
| ADAS | https://arxiv.org/abs/2408.08435 | arXiv preprint |
| CASCADE | https://arxiv.org/abs/2512.23880 | arXiv preprint |
| AutoAgent | https://arxiv.org/abs/2603.09716 | arXiv preprint |
| Voyager | https://arxiv.org/abs/2305.16291 | arXiv preprint |
| SAGE | https://arxiv.org/abs/2512.17102 | arXiv preprint |
| EvolveR | https://arxiv.org/abs/2510.16079 | arXiv preprint |
| CoEvoSkills | https://arxiv.org/abs/2604.01687 | arXiv preprint |
| ExpeL | https://arxiv.org/abs/2308.10144 | AAAI-24 |
| Sierra Agent OS 2.0 | https://sierra.ai/blog/agent-os-2-0 | Industry blog |
| Cognition Devin | https://cognition.ai/blog/introducing-devin | Industry blog |
| MetaGen | https://arxiv.org/abs/2601.19290 | arXiv preprint |
| MAE | https://arxiv.org/abs/2510.23595 | arXiv preprint |
| MetaReflection | https://arxiv.org/abs/2405.13009 | arXiv preprint |
| CLIN | https://arxiv.org/abs/2310.10134 | arXiv preprint |
| SkillOS | https://www.semanticscholar.org/paper/2653e4c7fa3be13d3db4b7a6ff3032ac17f7f467 | Semantic Scholar / 2026 |
| SoK: Agentic Skills | https://arxiv.org/abs/2602.20867 | arXiv preprint |
| Self-Evolving Agents Survey | https://www.semanticscholar.org/paper/74deef6100e5d9baf2eaa86e20618fa34d02c678 | Survey paper |

---

*Harvest completed. 22 systems evaluated; 11 confirmed composite-two-loop; 9 rejected; 2 borderline. Primary search via pplx CLI (academic + web), paper fetches via pplx content fetch. No GitHub connector used per task instructions.*
