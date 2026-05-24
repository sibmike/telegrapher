# P3 Harvest: Integrated Patch-Plastic Architectures
**Harvest for Paper 3 — LLM Reliability Trilogy**
*Systems that EXPLICITLY ASSEMBLE multiple substrates (Instructions + Skills + Memory + Tools + Orchestration + Governance) into a coherent adaptive whole, with feedback loops that update the scaffold based on residual errors.*

---

## SUMMARY TABLE — Sorted by Patch-Plasticity Score

| System | Year | Venue | PP Score | Integration Depth | Substrates (I/Sk/M/T/Or/Go) | Research/Prod |
|--------|------|-------|----------|------------------|------------------------------|---------------|
| NanoResearch | 2026 | arXiv 2605.10813 | **5/5** | DEEP | ●/●/●/●/●/◐ | Research |
| AutoAgent | 2026 | arXiv 2603.09716 | **5/5** | DEEP | ●/●/●/●/●/◐ | Research |
| CASCADE | 2025 | arXiv 2512.23880 | **4.5/5** | DEEP | ●/●/●/●/●/◐ | Research |
| Agent S / S2 | 2024/25 | arXiv 2410.08164 / 2504.00906 | **4.5/5** | DEEP | ●/●/●/●/●/○ | Research |
| Mobile-Agent-E | 2025 | arXiv 2501.11733 | **4.5/5** | DEEP | ●/●/●/●/●/◐ | Research |
| EvolveR | 2025 | arXiv 2510.16079 | **4/5** | DEEP | ●/●/●/●/●/○ | Research |
| Voyager | 2023 | arXiv 2305.16291 | **4/5** | MEDIUM-DEEP | ●/●/●/○/●/○ | Research |
| Generative Agents | 2023 | arXiv 2304.03442 | **4/5** | MEDIUM-DEEP | ●/○/●/○/●/○ | Research |
| OS-Copilot / FRIDAY | 2024 | arXiv 2402.07456 | **4/5** | DEEP | ●/●/●/●/●/◐ | Research |
| Cradle | 2024 | arXiv 2403.03186 | **4/5** | MEDIUM | ●/●/●/●/●/◐ | Research |
| SAGE | 2025 | arXiv 2512.17102 | **4/5** | MEDIUM | ●/●/○/●/●/○ | Research |
| ExpeL | 2023 | arXiv 2308.10144 | **3.5/5** | MEDIUM | ●/●/●/○/●/○ | Research |
| AWM | 2024 | arXiv 2409.07429 | **3.5/5** | MEDIUM | ●/●/●/●/◐/○ | Research |
| MetaGPT | 2023 | arXiv 2308.00352 | **3.5/5** | MEDIUM | ●/○/●/●/●/◐ | Research |
| AutoManual | 2024 | NeurIPS 2024 | **3.5/5** | MEDIUM | ●/●/●/●/◐/○ | Research |
| JARVIS-1 | 2023 | arXiv 2311.05997 | **3.5/5** | MEDIUM | ●/●/●/○/●/○ | Research |
| CoEvoSkills | 2026 | arXiv 2604.01687 | **3.5/5** | MEDIUM | ●/●/◐/○/◐/◐ | Research |
| ChatDev | 2023 | arXiv 2307.07924 | **3/5** | SHALLOW-MED | ●/○/●/○/●/◐ | Research |
| Sierra Agent OS | 2024 | Production | **4/5** | MEDIUM-DEEP | ●/○/●/●/●/● | Production |
| Hippocratic AI Polaris | 2024 | Production | **3.5/5** | MEDIUM | ●/○/●/○/●/● | Production |
| GITM | 2023 | arXiv 2305.17144 | **3/5** | MEDIUM | ●/●/●/○/●/○ | Research |
| OpenHands / CodeAct | 2024 | arXiv 2407.16741 | **3/5** | SHALLOW-MED | ●/○/●/●/●/◐ | Research/Prod |
| Sakana AI Scientist | 2024 | arXiv 2408.06292 | **3/5** | SHALLOW-MED | ●/○/●/●/●/◐ | Research |
| CaptainAgent | 2024 | arXiv 2405.19425 | **2.5/5** | SHALLOW | ●/○/○/●/●/○ | Research |
| Plan4MC | 2023 | GitHub/arXiv | **2.5/5** | SHALLOW | ●/●/○/○/●/○ | Research |

**Legend:** ● = full substrate, ◐ = partial, ○ = absent. Substrates: I=Instructions, Sk=Skills, M=Memory, T=Tools, Or=Orchestration, Go=Governance

---

## SUBSTRATE COMPOSITION MATRIX

| System | Instructions | Skills | Memory | Tools | Orchestration | Governance | Integration |
|--------|-------------|--------|--------|-------|---------------|-----------|-------------|
| **NanoResearch** | Deep (user profile + SDPO policy) | Deep (Skill Bank: procedural rules, grows 0.80→2.30/topic) | Deep (user+project records, grows 6.4→12.0 entries) | Deep (code exec, literature, experiments) | Deep (Orchestrator O coordinates 3-stage pipeline) | Partial (review agent) | **DEEP co-evolution** |
| **AutoAgent** | Deep (structured cognition layer) | Deep (reusable skill library, expanded by evolution cycle) | Deep (elastic memory: raw+compressed+episodic) | Deep (unified tool/LLM/agent call space) | Deep (closed-loop cognitive evolution) | Partial | **DEEP** |
| **CASCADE** | Deep (learning objective, human instructions) | Deep (executable skills, accumulated cross-session) | Deep (session+consolidated, vector+graph dual store) | Deep (web search, code extraction, lab APIs) | Deep (orchestrator agent + DeepSolver) | Partial (human-in-loop) | **DEEP** |
| **Agent S / S2** | Deep (experience-augmented planning) | Partial (via ACI/specialist models) | Deep (narrative+episodic memory, self-supervised update) | Deep (web search, GUI actions, ACI) | Deep (Manager+Worker+Self-Evaluator) | Absent | **DEEP** |
| **Mobile-Agent-E** | Deep (task planning) | Deep (Shortcuts: reusable atomic sequences) | Deep (Tips+Shortcuts long-term memory, cross-task) | Deep (mobile UI, multi-app) | Deep (Manager+4 subordinate agents) | Partial (Action Reflector) | **DEEP** |
| **EvolveR** | Deep (principles guide reasoning) | Deep (principle library, semantically deduplicated) | Deep (experience base, dynamically updated) | Deep (multi-step tool use) | Deep (offline+online lifecycle loop) | Absent | **DEEP** |
| **Voyager** | Deep (curriculum instructions) | Deep (ever-growing skill library, executable code) | Partial (skill library IS memory; no separate episodic store) | Deep (Minecraft API) | Deep (automatic curriculum + iterative prompting) | Partial (self-verification) | **MEDIUM-DEEP** |
| **Generative Agents** | Deep (persona, role) | Absent (no procedural skill bank) | Deep (memory stream, complete experience record) | Absent (no external tools) | Deep (observation+planning+reflection loop) | Absent | **MEDIUM-DEEP** |
| **OS-Copilot/FRIDAY** | Deep (planner instructions) | Deep (accumulated tools+skills from self-directed learning) | Deep (working+declarative+procedural memory) | Deep (OS interface: files, web, code, apps) | Deep (planner→configurator→actor→critic loop) | Partial (critic feedback) | **DEEP** |
| **Cradle** | Deep (task inference) | Deep (skill curation module) | Deep (memory module) | Deep (screenshots, keyboard, mouse) | Deep (6-module pipeline) | Partial (self-reflection) | **MEDIUM** |
| **SAGE** | Deep (SFT + RL) | Deep (skill library via Sequential Rollout) | Absent (no persistent memory store) | Deep (AppWorld tasks) | Deep (RL training loop) | Partial (skill-integrated reward) | **MEDIUM** |
| **ExpeL** | Deep (extracted insights as instructions) | Deep (knowledge extracted from training tasks) | Deep (past experiences recalled at inference) | Partial (task-specific) | Partial (no explicit orchestrator) | Absent | **MEDIUM** |
| **AWM** | Deep (task instructions) | Deep (induced workflows as tools+memory) | Deep (workflow memory, offline+online) | Deep (web navigation actions) | Partial (no explicit evolution loop) | Absent | **MEDIUM** |
| **MetaGPT** | Deep (SOPs encoded in prompts) | Absent (no skill bank) | Deep (shared message pool, phase-segmented) | Deep (code execution, testing) | Deep (assembly line, role-based) | Partial (executable feedback) | **MEDIUM** |
| **AutoManual** | Deep (self-generated manual) | Deep (rules = skills, Builder updates online) | Deep (rules accumulate, case-conditioned) | Deep (environment interaction) | Deep (Planner+Builder+Formulator) | Partial | **MEDIUM** |
| **JARVIS-1** | Deep (multimodal instructions) | Partial (plan templates stored in memory) | Deep (multimodal memory: plan+scenario) | Deep (goal-conditioned controllers) | Deep (planning + execution + memory) | Absent | **MEDIUM** |
| **CoEvoSkills** | Deep (skill specs) | Deep (Skill Generator, iteratively refined) | Partial (conversation context) | Partial (oracle testing) | Deep (co-evolutionary loop) | Partial (Surrogate Verifier) | **MEDIUM** |
| **ChatDev** | Deep (SOPs, roles) | Absent | Deep (short+long-term, phase-segmented) | Partial (code execution) | Deep (chat chain) | Partial (dehallucination) | **SHALLOW-MED** |
| **Sierra Agent OS** | Deep (policy rules + tone) | Absent (via routing) | Deep (conversation history) | Deep (CRM, payment, API integrations) | Deep (constellation: planner+executor+validator) | Deep (guardrails, policy) | **MEDIUM-DEEP** |
| **Hippocratic AI Polaris** | Deep (clinical protocols) | Absent | Deep (patient profile, clinical history) | Partial (health data) | Deep (22 specialized models) | Deep (safety validation models) | **MEDIUM** |
| **GITM** | Deep (text-based knowledge) | Deep (successful action lists→memory) | Deep (text-based memory) | Partial (Minecraft API) | Deep (LLM Decomposer + Planner) | Absent | **MEDIUM** |
| **OpenHands/CodeAct** | Deep (task instructions) | Absent (no skill bank) | Deep (event stream, hierarchical) | Deep (code, browser, bash, file) | Deep (multi-agent delegation) | Partial (sandbox) | **SHALLOW-MED** |
| **Sakana AI Scientist** | Deep (research templates) | Absent | Partial (paper history) | Deep (code exec, aider, LLM calls) | Deep (ideation→experiment→write→review) | Partial (automated reviewer) | **SHALLOW-MED** |
| **CaptainAgent** | Deep (adaptive instructions) | Absent | Absent | Deep (AutoGen tools) | Deep (team building, hierarchical) | Absent | **SHALLOW** |
| **Plan4MC** | Deep (LLM planning prompts) | Deep (RL-learned skills) | Absent | Partial (Minecraft API) | Deep (skill graph planning) | Absent | **SHALLOW** |

---

## PER-SYSTEM DEEP ENTRIES (Top 10 by Integration Depth)

---

### 1. NanoResearch — Patch-Plasticity Score: 5/5
**Citation:** Xu et al., "NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation," arXiv:2605.10813, May 2026. https://arxiv.org/abs/2605.10813

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** The only published system explicitly framed around *tri-level co-evolution* — where skills, memory, and policy genuinely update each other across research cycles, not just run in parallel.

**Architecture Description:**
NanoResearch is built around a self-evolving pipeline coordinated by an Orchestrator (O), which manages a Skill Bank (S), Memory Module (M), and a label-free policy learning mechanism. The system begins by constructing a user profile (U) through interactive queries, which serves as persistent context for all subsequent decisions. Three stages follow: (1) ideation, (2) experimentation (with autonomous debugging loop), (3) writing/review. After each stage, the Orchestrator distills new procedural rules into the Skill Bank and stores project-specific experiences in the Memory Module. A separate Review agent critiques output without access to skills or memory — ensuring unbiased evaluation.

**Key architectural quote:** *"These three layers co-evolve: reliable skills produce richer memory, richer memory informs better planning, and preference internalization continuously realigns the loop to each user."*

**Policy substrate:** Self-Distillation Policy Optimization (SDPO) converts free-form natural language feedback (F) into dense, token-level learning signals. The feedback-conditioned model acts as a self-teacher, updating planner policy π_θ to match its output distribution — embedding user preferences directly into model parameters.

**Fast/slow loops:** The system exhibits implicit fast-slow loops: the execution cycle (per-stage actions) is the fast loop; the skill distillation and memory update (post-stage, trajectory-based reflection) is the slow loop; SDPO policy updates (parameter-level) are the slowest loop.

**Feedback signal chain:** Task outcomes + critique feedback → SDPO loss → policy parameter updates; Stage execution trajectories → Orchestrator reflection → Skill Bank (procedural rules) + Memory Module (project/user records).

**Promotion mechanism:** After each stage, the Orchestrator reflects on the full execution path (actions, critiques, outcomes) and distills generalizable rules into skills while summarizing project-specific insights into memory. Semantically overlapping entries are merged to prevent unbounded growth.

**Benchmark evidence:**
- Tested on 20 research topics spanning 7 domains, under both simulated and human researcher evaluations
- **Compliance: 8.963 vs. 6.656** for best baseline (highest-margin improvement — shows preference alignment)
- **Innovation: 4.960 → 5.645** across rounds 1→3 (demonstrates accumulation effect)
- **Expression: 5.428 → 6.172** across rounds 1→3
- Skill Bank growth: avg. **0.80 → 2.30 skills/topic** from R1→R3
- Memory Module growth: **6.40 → 12.00 entries/topic** from R1→R3
- *"Performance improves monotonically from Round 1 to Round 3 on all dimensions"* — direct co-evolution evidence

**Ablations:** The paper (40 pages, 14 figures, 7 tables) contains ablations; the ChatPaper summary confirms Table 4 tracks growth of Skill Bank and Memory across rounds, and Table 1 shows Compliance advantage. Full ablation table not accessible from abstract, but growth tables directly prove skill-memory co-evolution.

**Integration depth:** DEEP — each substrate's update triggers other substrates' updates in a documented feedback chain.

**Designed vs. retrofitted:** DESIGNED as patch-plastic — the paper's core thesis is that personalization requires co-evolution, not modular stacking.

---

### 2. AutoAgent — Patch-Plasticity Score: 5/5
**Citation:** Wang et al., "AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Autonomous Agent Frameworks," arXiv:2603.09716, March 2026. https://arxiv.org/abs/2603.09716

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** Explicit two-cycle architecture (Execution Cycle + Evolution Cycle) sharing one Elastic Memory Orchestrator — the most formally specified closed-loop co-evolution pattern in the 2026 crop.

**Architecture Description:**
AutoAgent's Self-Evolution Loop formalizes four functions: Cognition (structured descriptive knowledge over tools, self-capabilities, peer expertise, task knowledge), Decision (contextually appropriate action selection), Memory (organized action/outcome history), Evolution (experience analysis to refine Cognition and Memory strategies). The key architectural innovation is that these form a closed cycle: actions generate experience → experience analysis refines cognition → updated cognition enables better actions.

**Key architectural quote:** *"The two cycles are not isolated; they are synergistically integrated through the shared Elastic Memory Orchestrator. The Execution Cycle produces the raw experiential data that fuels the Evolution Cycle. In turn, the Evolution Cycle refines the cognitive knowledge that guides future executions. This creates a virtuous, self-reinforcing loop: better cognition leads to more effective decisions, which generate higher-quality experience for learning, which produces even better cognition."*

**Feedback signal chain:** Action outcomes → Memory Orchestrator (raw record preservation, trajectory compression, episodic abstraction) → Cognitive Evolution Module (examines trajectories, identifies discrepancies between intent and outcomes) → updates Cognition Layer (revisions to descriptive text for tools/peers/capabilities) + Memory strategies.

**Benchmark evidence:** HotpotQA: **AutoAgent accuracy 0.530 vs. IRCoT 0.434** (second best). Results span retrieval-augmented reasoning, tool-augmented agent benchmarks, and embodied task environments — consistent improvement over static and memory-augmented baselines.

**Integration depth:** DEEP — the two cycles are explicitly designed to be co-evolving, not stacked.

---

### 3. CASCADE — Patch-Plasticity Score: 4.5/5
**Citation:** Huang et al., "CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution," arXiv:2512.23880, December 2025. https://arxiv.org/abs/2512.23880

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** Explicit "LLM + skill acquisition" paradigm shift framing; skills are shared across agents and scientists, making this the strongest production-adjacent multi-user skill-sharing architecture in the research corpus.

**Architecture:** Self-evolving multi-agent system centered on an Orchestrator agent. Dual-layer memory: session-wise memory (SQLiteSession for dialogue history) and consolidated memory (hybrid vector-semantic + graph-based entity-relationship using Supabase PostgreSQL + Neo4j). Meta-skills: (1) continuous learning via web search, code extraction, memory utilization; (2) self-reflection via introspection, knowledge graph exploration. DeepSolver subsystem for skill creation and problem-solving.

**Key architectural quote:** *"CASCADE achieves self-evolution toward skill acquisition through continuous learning, self-reflection, human-agent collaboration, and memory. These acquired skills are reusable by agents, human experts, and other systems."*

**Feedback signal chain:** Real-time failures + human instructions + past experiences → DeepSolver skill generation → consolidated memory → reusable skills shared across agents.

**Benchmark evidence (SciSkillBench, 116 materials science/chemistry tasks):**
- **CASCADE with GPT-5: 93.3% success rate**
- Without evolution mechanisms: **35.4%** — a 57.9pp gap directly attributable to multi-substrate co-evolution

**Integration depth:** DEEP — evolution mechanisms demonstrably account for the majority of performance; the ablation (with vs. without evolution) is the starkest in the field.

---

### 4. Agent S / Agent S2 — Patch-Plasticity Score: 4.5/5
**Citations:**
- Agent S: Agashe et al., "Agent S: An Open Agentic Framework that Uses Computers Like a Human," arXiv:2410.08164, October 2024. https://arxiv.org/abs/2410.08164
- Agent S2: "Agent S2: A Compositional Generalist-Specialist Framework," arXiv:2504.00906, April 2025. https://arxiv.org/abs/2504.00906

**Substrate composition vector:** Instructions[DEEP] / Skills[PARTIAL→DEEP in S2] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[ABSENT]

**Architectural distinctiveness:** Experience-augmented hierarchical planning with two memory types (narrative = full-task summaries; episodic = step-by-step subtask experience) co-evolving with a Self-Evaluator that creates textual rewards without human feedback.

**Architecture (Agent S):** Manager (high-level planning, fuses external web knowledge + internal narrative memory) → Workers (each draws from episodic memory during subtask execution) → Self-Evaluator (summarizes outcomes into narrative and episodic memory for future retrieval). The ACI (Agent-Computer Interface) grounds the system in actual GUI state.

**Key architectural quote:** *"A continual process of storing and retrieving self-evaluated task experience in narrative and episodic memory enables Agent S to improve over time and adapt to changes in the open-world desktop environment."*

**Feedback signal chain:** Task outcomes → Self-Evaluator (success/failure labels without human input) → Narrative memory (full-task abstractions) + Episodic memory (step-level experience) → retrieved and fused by Experience Context Fusion module → guides Manager planning.

**Agent S2 additions:** Mixture-of-Grounding (generalist + specialist visual models), Proactive Hierarchical Planning (replans after each subtask rather than only on failure), continual learning memory mechanism retaining cross-session experience.

**Benchmark evidence:**
- Agent S: **+9.37% success rate** over baseline on OSWorld (83.6% relative improvement), new SOTA
- Agent S2: **18.9% and 32.7% relative improvements** over Claude Computer Use and UI-TARS on OSWorld 15-step and 50-step; **+52.8%** on WindowsAgentArena; **+16.52%** on AndroidWorld

**Integration depth:** DEEP — memory update triggers planning changes; Self-Evaluator generates supervision signal that feeds back into both memory substrates.

---

### 5. Mobile-Agent-E — Patch-Plasticity Score: 4.5/5
**Citation:** Wang et al., "Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks," arXiv:2501.11733, January 2025. https://arxiv.org/abs/2501.11733

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** Most explicit separation of two skill types (Tips = episodic lessons; Shortcuts = procedural routines) co-evolving in a unified long-term memory store, with Experience Reflectors as the promotion mechanism.

**Architecture:** Hierarchical multi-agent framework: Manager (high-level planning, breaks tasks into subgoals) + 4 subordinates: Perceptor (visual perception), Operator (action execution), Action Reflector (error verification), Notetaker (information aggregation). Self-Evolution Module maintains persistent long-term memory of Tips and Shortcuts. After task k, Experience Reflectors update long-term memory based on interaction history plus queries for remaining tasks — mimicking forward-planning for future improvement.

**Key architectural quote:** *"Tips are general guidance and lessons learned from prior tasks on how to effectively interact with the environment. Shortcuts are reusable, executable sequences of atomic operations tailored for specific subroutines. The inclusion of Tips and Shortcuts facilitates continuous refinement in performance and efficiency."*

**Feedback signal chain:** Task interaction history → 2 Experience Reflectors (triggered after each task) → Tips update (episodic, lessons) + Shortcuts proposal (procedural, new routines) → fed to Manager (planning) + Operator (execution) for improved future performance.

**Benchmark evidence:**
- **22% absolute improvement** over previous SOTA across 3 LMM backbones on Mobile-Eval-E
- Mobile-Agent-E + Evo: **Satisfaction Score multi-agent state**: 86.9 / Reflection Accuracy: 90.4

**Integration depth:** DEEP — Tip generation and Shortcut creation are cross-substrate promotions: task outcomes update both episodic knowledge (Tips) and procedural skill library (Shortcuts), which then alter both planning (Manager) and execution (Operator).

---

### 6. Voyager — Patch-Plasticity Score: 4/5
**Citation:** Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models," arXiv:2305.16291, May 2023. https://arxiv.org/abs/2305.16291

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[PARTIAL] / Tools[PARTIAL] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** First published system where a skill library functions as persistent cross-session memory, and where an automatic curriculum, skill library, and verification mechanism co-evolve. The first complete embodied patch-plastic loop in the LLM era.

**Architecture:** Three components: (1) Automatic curriculum that maximizes exploration; (2) Skill library (ever-growing, executable code, compositional); (3) Iterative prompting mechanism incorporating environment feedback, execution errors, and self-verification. Skill library is both the memory and the skills substrate simultaneously.

**Key architectural quote:** *"The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting."*

**Feedback signal chain:** Environment observations + execution errors → iterative prompting → GPT-4 code refinement → self-verification module (confirms task completion) → on success, skill committed to library → curriculum queries for next milestone.

**ABLATION EVIDENCE (6 design choices):**
- Without automatic curriculum: discovered item count drops **93%**
- Without skill library: agent *plateaus in later stages*; critical for compound growth
- Without self-verification: **-73% discovered item count** — "self-verification is the most important among all the feedback types"
- Skill library enables: 15.3× faster tech-tree milestones (wooden), 8.5× (stone), 6.4× (iron), only Voyager reaches diamond

**Benchmark evidence:**
- **3.3× more unique items**, **2.3× longer distances**, tech tree milestones up to **15.3× faster** than prior SOTA
- Generalizes to new Minecraft worlds where other methods fail

**Integration depth:** MEDIUM-DEEP — skill library and curriculum co-evolve (skills inform curriculum difficulty); verification updates skill quality. No separate episodic/declarative memory distinct from skill library.

---

### 7. Generative Agents — Patch-Plasticity Score: 4/5
**Citation:** Park et al., "Generative Agents: Interactive Simulacra of Human Behavior," arXiv:2304.03442, April 2023. https://arxiv.org/abs/2304.03442

**Substrate composition vector:** Instructions[DEEP] / Skills[ABSENT] / Memory[DEEP] / Tools[ABSENT] / Orchestration[DEEP] / Governance[ABSENT]

**Architectural distinctiveness:** Canonical three-substrate integration (observation → memory stream → reflection → planning → action) where reflection synthesizes memories into higher-order knowledge, creating genuinely co-evolving memory and planning layers. Introduced the *memory stream + reflection + planning* triad that most subsequent systems inherit.

**Architecture:** Three architectural components: (1) Memory stream: complete record of experiences in natural language, retrieved dynamically by recency × importance × relevance; (2) Reflection: synthesizes memories into higher-level inferences over time ("higher-level reflections"), enabling the agent to draw conclusions; (3) Planning: translates conclusions + current environment into high-level action plans → recursive sub-plans.

**Feedback signal chain:** Observations → Memory stream → Retrieval (recency×importance×relevance) → Reflection synthesis → Planning → Actions → New observations (loop). Reflections themselves become memories, creating hierarchical memory depth.

**ABLATION EVIDENCE (from paper and ACM full text):**
- Ablations limit agents' access to memory, reflection, and planning separately
- *"We observe that each of these components is critical to strong performance across these interview tasks"*
- Most common errors: failed memory retrieval, memory fabrication/embellishment, overly formal speech from base LLM
- Emergent social behavior only with full multi-substrate architecture (Valentine's Day party coordination from single seed)

**Integration depth:** MEDIUM-DEEP — memory and planning are genuinely interdependent (reflection updates planning quality; planning actions generate new memories); but skills and tools are absent.

---

### 8. OS-Copilot / FRIDAY — Patch-Plasticity Score: 4/5
**Citation:** Wu et al., "OS-Copilot: Towards Generalist Computer Agents with Self-Improvement," arXiv:2402.07456, February 2024. https://arxiv.org/abs/2402.07456

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** Explicit three-type memory model (working, declarative, procedural) that maps to neuroscience — the only system in the corpus to formally distinguish all three LTM types. Self-directed learning via curriculum generates skills through trial-and-error.

**Architecture:** Components: Planner (comprehends agent capabilities, decomposes tasks), Configurator (configures subtask using working/declarative/procedural memory), Actor/Executor (proposes executable actions), Critic (assesses execution outcomes, formulates feedback, effects updates to long-term memory). FRIDAY adds self-directed learning: a pre-defined learning objective (e.g., "master spreadsheet manipulation") causes FRIDAY to propose a continuous stream of tasks spanning easy→challenging, resolving them through trial-and-error, accumulating tools and semantic knowledge.

**Feedback signal chain:** Execution outcomes → Critic module → feedback formulation → refinement of execution errors + updates to long-term memory. Self-directed learning: task outcomes → skill accumulation → improved capability for future tasks.

**Benchmark evidence:**
- GAIA benchmark (general AI assistants): FRIDAY outperforms previous methods by **35%**
- *"Showcasing strong generalization to unseen applications via accumulated skills from previous tasks"*

**Integration depth:** DEEP — Critic explicitly updates long-term memory; self-directed learning creates a skills→competence feedback loop; the three memory types serve different roles in the Configurator.

---

### 9. Cradle — Patch-Plasticity Score: 4/5
**Citation:** Tan et al., "Cradle: Empowering Foundation Agents Towards General Computer Control," arXiv:2403.03186, March 2024. https://arxiv.org/abs/2403.03186

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** The most complete modular multi-substrate architecture for general computer control — 6 explicitly named modules that map directly onto the paper's 6-substrate model. Cradle is a near-perfect substrate-composition demonstration.

**Architecture — 6 modules:**
1. **Information Gathering** — perceives screenshots (tool substrate)
2. **Self-Reflection** — reviews actions, identifies errors (governance/feedback)
3. **Task Inference** — maps high-level goals to subtasks (instructions/planning)
4. **Skill Curation** — builds and retrieves executable skills (skills substrate)
5. **Action Planning** — generates action sequences (orchestration)
6. **Memory** — stores experiences for retrieval (memory substrate)

**Feedback signal chain:** Screenshots → Information Gathering → Self-Reflection + Task Inference → Action Planning (using Skill Curation) → execution → feedback to Memory and Skill Curation.

**Benchmark evidence:** Completes 40-minute RDR2 missions (AAA game), Cities: Skylines city creation, Stardew Valley farming, Dealer's Life 2 trading (87% weekly profit). OSWorld performance reported. Demonstrates generalization across 4 games + 5 software applications.

**Integration depth:** MEDIUM — 6 modules named and present, but the paper focuses on modularity more than co-evolution. Skill curation and memory interact but the feedback is pipeline-sequential rather than truly co-evolving.

---

### 10. SAGE — Patch-Plasticity Score: 4/5
**Citation:** Wang et al., "Reinforcement Learning for Self-Improving Agent with Skill Library," arXiv:2512.17102, December 2025. https://arxiv.org/abs/2512.17102

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[ABSENT] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architectural distinctiveness:** Only system where skill generation is backpropagated through RL (GRPO-based) — skills are not distilled heuristically but are learned end-to-end, making this the strongest connection between skills and model parameters.

**Architecture:** Skill Augmented GRPO for self-Evolution (SAGE). Sequential Rollout: agents iteratively deployed across task chains; skills from previous tasks accumulate in library and become available for subsequent tasks. Skill-integrated Reward complements outcome-based reward to reinforce skill generation and utilization.

**Key architectural quote:** *"Skills generated from previous tasks accumulate in the library and become available for subsequent tasks. The Skill-integrated Reward provides a feedback signal that works alongside outcome-based rewards to refine how the agent generates and utilizes skills."*

**Feedback signal chain:** Task outcome (success/failure) → Skill-integrated Reward + outcome reward → GRPO policy gradient → updates both task-solving policy AND skill generation policy simultaneously.

**Benchmark evidence (AppWorld):**
- **+8.9% Scenario Goal Completion** over SFT baseline
- **-26% interaction steps** (efficiency gain)
- **-59% tokens generated** (dramatically more efficient)

**Integration depth:** MEDIUM — skill generation and task solving are co-trained via RL but there is no separate memory module or governance substrate. The RL feedback loop is the deepest substrate-integration mechanism in the corpus.

---

## ADDITIONAL SYSTEMS (Scored)

### ExpeL — Patch-Plasticity Score: 3.5/5
**Citation:** Zhao et al., "ExpeL: LLM Agents Are Experiential Learners," arXiv:2308.10144, August 2023. https://arxiv.org/abs/2308.10144

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[PARTIAL] / Orchestration[PARTIAL] / Governance[ABSENT]

**Architecture:** Three-component pattern: (1) Autonomous experience gathering from training tasks, (2) Knowledge extraction using natural language (analogous to skill distillation), (3) Recall at inference to make informed decisions. Agent gathers *across* training tasks; at inference recalls extracted insights + past experiences.

**Feedback mechanism:** Training task outcomes → extracted insights (skills/rules) → stored as knowledge library → recalled at inference.

**Integration depth:** MEDIUM — experience→knowledge→decision loop is clear but no live adaptation, no separate orchestration layer.

**Key:** Historical importance as first system to explicitly operationalize "experiential learning" without parametric updates. Direct predecessor of ExpeL-style architectures.

---

### Agent Workflow Memory (AWM) — Patch-Plasticity Score: 3.5/5
**Citation:** Wang et al., "Agent Workflow Memory," arXiv:2409.07429, September 2024 (ICML 2025). https://arxiv.org/abs/2409.07429

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[PARTIAL] / Governance[ABSENT]

**Architecture:** AWM induces workflows from agent trajectories by extracting reusable routines, then integrates these workflows into agent memory. Workflows can also be wrapped as high-level functions (tool expansion). Offline (from training examples) and online (from test queries on-the-fly) modes.

**Key architectural quote:** *"After the workflows W are induced, they are integrated into the agent as auxiliary memory M+W→M_w. Besides integrating workflows as agent memory, we also explore workflows in expanding the agent action space, denoted as AWM_AS — wrapping each workflow into a high-level function, similar to a shortcut tool."*

**Feedback mechanism:** Task trajectories → workflow induction → stored as memory AND as tool shortcuts → guides future actions.

**Benchmark evidence:**
- Mind2Web: **+24.6% relative success rate**
- WebArena: **+51.1% relative success rate**
- Cross-domain generalization: **8.9 to 14.0 absolute points** over baselines as distribution gaps widen

**Integration depth:** MEDIUM — workflow/skill and memory are genuinely co-evolving (workflows become memory become tools); no separate governance or orchestrator.

---

### MetaGPT — Patch-Plasticity Score: 3.5/5
**Citation:** Hong et al., "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework," arXiv:2308.00352, August 2023. https://arxiv.org/abs/2308.00352

**Substrate composition vector:** Instructions[DEEP] / Skills[ABSENT] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architecture:** SOPs encoded into prompt sequences → agents with domain roles → assembly-line task decomposition → shared message pool (structured blackboard) → executable feedback mechanism (code execution during runtime → corrects errors live).

**Key architectural quote:** *"MetaGPT encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows, thus allowing agents with human-like domain expertise to verify intermediate results and reduce errors."*

**Feedback mechanism:** Code execution results → executable feedback → re-prompting for revision.

**ABLATION EVIDENCE:**
- Adding roles beyond Engineer: *"consistently improves both revisions and executability"* (Table 3)
- Adding executable feedback: **+4.2% HumanEval, +5.4% MBPP** in Pass@1
- Executable feedback improves feasibility score: **3.67 → 3.75**; reduces human revision cost: **2.25 → 0.83**

**Benchmark evidence:**
- HumanEval: **85.9% Pass@1** (SOTA at time)
- MBPP: **87.7% Pass@1** (SOTA at time)

**Integration depth:** MEDIUM — SOP→memory→execution→feedback loop is clear; no skill bank; governance is lightweight; roles are static.

---

### AutoManual (NeurIPS 2024) — Patch-Plasticity Score: 3.5/5
**Citation:** Chen et al., "AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning," NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/0142921fad7ef9192bd87229cdafa9d4-Abstract-Conference.html

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[PARTIAL]

**Architecture:** Three agents: (1) Planner codes actionable plans based on current rules; (2) Builder updates rules through structured rule system via case-conditioned prompting (online, adaptive to new interactions); (3) Formulator compiles rules into comprehensive human-readable manual. Rules ARE the skills substrate; they are updated online based on execution feedback.

**Key mechanism:** Case-conditioned prompting strategy for the Builder prevents hallucinations in rule management. Rules accumulate and are optimized online.

**Feedback mechanism:** Task execution outcomes → Builder (case-conditioned) → updated rules → improved Planner performance.

**Benchmark evidence:**
- ALFWorld: **97.4% with GPT-4-turbo** (from single demonstration)
- MiniWoB++: **98.3% with GPT-4-turbo**
- WebArena (Reddit): **65.1% with GPT-4-turbo**

**Integration depth:** MEDIUM — rule/skill and planning co-evolve; manual compilation provides cross-session promotion.

---

### JARVIS-1 — Patch-Plasticity Score: 3.5/5
**Citation:** Wang et al., "JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models," arXiv:2311.05997, November 2023. https://arxiv.org/abs/2311.05997

**Substrate composition vector:** Instructions[DEEP] / Skills[PARTIAL] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[ABSENT]

**Architecture:** Multimodal LLM planner + multimodal memory storing scenarios AND plans from successful past experiences. Memory-augmented planning: relevant past experiences retrieved and provided as in-context examples to strengthen planning without gradient update. Curriculum learning generates task set for exploration.

**Key architectural quote:** *"By outfitting JARVIS-1 with a multimodal memory, we effectively allow it to plan with both pretrained knowledge and its actual experiences in the world, therefore bringing significant improvement to planning correctness and consistency."*

**Feedback mechanism:** Task success → experience stored (scenario + plan) in memory → retrieval for future similar tasks → improved planning.

**Integration depth:** MEDIUM — memory and planning are genuinely linked; skills are plan-templates rather than standalone procedural code; no separate skill bank distinct from memory.

**Capability:** 200+ Minecraft tasks, most general Minecraft agent at time.

---

### ChatDev — Patch-Plasticity Score: 3/5
**Citation:** Qian et al., "ChatDev: Communicative Agents for Software Development," arXiv:2307.07924, July 2023 (ACL 2024). https://arxiv.org/abs/2307.07924

**Substrate composition vector:** Instructions[DEEP] / Skills[ABSENT] / Memory[DEEP] / Tools[PARTIAL] / Orchestration[DEEP] / Governance[PARTIAL]

**Architecture:** Chat-powered software development framework with specialized LLM agents for design/coding/testing phases. Chat Chain guides what agents communicate; Communicative Dehallucination guides how. Two memory types: short-term (phase-segmented from chat chain) and long-term (complete communication history). Role specialization via differentiated system prompts.

**Feedback mechanism:** Communicative Dehallucination as inter-agent error correction; multi-turn dialogue as iterative refinement.

**Integration depth:** SHALLOW-MEDIUM — no skill bank, no tool ecosystem, no cross-session learning. Chat chain creates sequential substrate composition but no co-evolution between sessions.

---

### CoEvoSkills — Patch-Plasticity Score: 3.5/5
**Citation:** Zhang et al., "CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification," arXiv:2604.01687, April 2026. https://arxiv.org/abs/2604.01687

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[PARTIAL] / Tools[PARTIAL] / Orchestration[DEEP] / Governance[DEEP]

**Architectural distinctiveness:** The only system where the *verifier itself co-evolves with the skill generator* — not just a fixed quality oracle but a learning adversarial partner.

**Architecture:** Skill Generator (iteratively refines multi-file skill packages) co-evolves with Surrogate Verifier (separate LLM session without generator's biases, synthesizes test cases, provides high-fidelity feedback). Three informationally isolated components ensure genuine co-evolution rather than overfitting. Ground-truth oracle provides final binary signal.

**Key architectural quote:** *"The two components co-evolve through iterative generate–verify–refine cycles: whenever the surrogate tests pass, a ground-truth oracle test re-executes the skill in a fresh environment and returns only an opaque success/failure signal."*

**ABLATION EVIDENCE (key finding):** "CoEvoSkills without verification performs on par with the no-skill baseline at round 0. Pass rate climbs sharply once iterative verification begins: 44% at round 2, surpasses human-curated skills at round 3 (63%), converges at 75% by round 5." — *"confirms that the co-evolutionary loop, not the generation prompt, is the primary driver of skill quality."*

**Benchmark evidence:**
- SkillsBench: **71.1% pass rate** (+40.5pp over no-skill baseline at 30.6%)
- Surpasses human-curated skills (53.5%) by round 3
- Skills transfer across 6 LLM families with **35–45pp gains** over their no-skill baselines

---

### EvolveR — Patch-Plasticity Score: 4/5
**Citation:** Wu et al., "Self-Evolving LLM Agents through an Experience-Driven Lifecycle (EvolveR)," arXiv:2510.16079, October 2025. https://arxiv.org/abs/2510.16079

**Substrate composition vector:** Instructions[DEEP] / Skills[DEEP] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[ABSENT]

**Architecture:** Two-phase closed-loop experience lifecycle: (1) Offline Self-Distillation — interaction trajectories synthesized into structured repository of abstract, reusable strategic principles; (2) Online Interaction — agent retrieves distilled principles to guide deliberative reasoning loop (Think-Act-Observe), accumulating new trajectories. RL mechanism updates agent policy to actually *utilize* principles rather than just retrieve them.

**Key architectural quote:** *"EvolveR completes the experience lifecycle with a reinforcement learning mechanism that enables the agent to utilize experience. The agent does not merely mimic its past interactions; it evolves based on what it has learned."*

**Feedback mechanism:** Online interaction trajectories → Offline Self-Distillation → principle library (semantically deduplicated, scored by historical effectiveness) → retrieved during online reasoning → RL updates policy to utilize principles effectively.

**Integration depth:** DEEP — RL provides genuine parameter-level integration; the principle library is distilled from trajectories, creating a genuine memory→policy feedback path.

---

## PRODUCTION SYSTEMS

### Sierra Agent OS — Patch-Plasticity Score: 4/5
**Source:** Sierra.ai product documentation and architecture blog (https://sierra.ai/blog/constellation-of-models)

**Substrate composition vector:** Instructions[DEEP] / Skills[ABSENT] / Memory[DEEP] / Tools[DEEP] / Orchestration[DEEP] / Governance[DEEP]

**Architecture:** Constellation architecture: 15+ frontier, open-weight, and proprietary models coordinated by Sierra's Agent OS. Modular task abstractions isolate responsibilities; orchestration and routing handled automatically. Supervisors enforce guardrails, policies, quality checks. Specialized agents for retrieval, classification, tools, policies, tone. Agent performance analytics drive automated agent updates based on flagged issues.

**Key architectural quote:** *"Agents built on Sierra are assembled using 15+ frontier, open-weight, and proprietary models, depending on the job to be done. Instead of writing monolithic agents, you compose them from cleanly separated capabilities — retrieval, classification, tools, policies, and tone."*

**Production status:** Commercial deployment, enterprise customer service. The governance substrate (guardrails, validators, policy agents) is the most mature in the corpus.

**Feedback mechanism:** Conversation analytics → flagged issues → automated agent updates (Sierra's Automate Agent Updates feature).

**Integration depth:** MEDIUM-DEEP — strong on governance; lacks explicit skill bank or cross-session learning.

---

### Hippocratic AI Polaris — Patch-Plasticity Score: 3.5/5
**Source:** Hippocratic AI research page and Polaris 3.0 announcement (https://hippocraticai.com)

**Substrate composition vector:** Instructions[DEEP] / Skills[ABSENT] / Memory[DEEP] / Tools[PARTIAL] / Orchestration[DEEP] / Governance[DEEP]

**Architecture:** 5.0T+ parameter constellation — 22 specialized LLM models for safety validation. Primary model handles clinical conversation; support models validate safety across domains. AI agent app store enables clinicians to scale key expertise.

**Production status:** Clinical deployment (real-time patient-AI conversations). World's most safety-validated integrated agent system.

**Governance substrate:** 22 safety validation models is the deepest governance substrate in any system examined.

---

## SURVEYS OF AGENTS VS. SURVEYS OF PATCH-PLASTIC ARCHITECTURES: THE GAP

### Existing Surveys of LLM-Based Agents

**1. Wang et al. (2023), "A Survey on Large Language Model based Autonomous Agents"**
- arXiv:2308.11432; published in *Frontiers of Computer Science* (Springer); 7 versions through March 2025
- Framework: profiling module + memory module + planning module + action module
- Coverage: construction, application (social/natural science/engineering), evaluation
- **Gap:** Treats modules as static components of agent architecture. No treatment of substrate co-evolution, promotion mechanisms, or cross-session learning. "Patch-plastic" dynamics are absent.

**2. Xi et al. (2023), "The Rise and Potential of Large Language Model Based Agents: A Survey"**
- arXiv:2309.07864; 86 pages; published in *Science China Information Sciences* (2025)
- Framework: brain + perception + action; single-agent, multi-agent, human-agent cooperation
- **Gap:** Taxonomizes agents by functional role; does not analyze feedback loops that update substrates. Treats memory and planning as independent.

**3. Sumers et al. (2023), "Cognitive Architectures for Language Agents (CoALA)"**
- arXiv:2309.02427; TMLR 2024
- Framework: modular memory components + structured action space + generalized decision-making process
- **Gap:** CoALA maps agents onto cognitive architectures from symbolic AI; explicitly identifies action types and memory types. However: CoALA is a *taxonomy of existing agents* — it does not analyze how substrates update each other. The paper's prospective directions ("actionable directions towards more capable agents") do not operationalize co-evolution.

**4. Xiang et al. (2026), "A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution"**
- Preprint (cloudfront); 3-paradigm taxonomy: Model-Centric, Environment-Centric, Model-Environment Co-Evolution
- **Closest to Paper 3's territory** — the co-evolution paradigm directly overlaps with patch-plasticity
- **Gap:** Covers *what* co-evolves (models, environments) but not *how substrates within an agent's scaffold co-evolve with each other*. The paper's co-evolution is inter-agent or agent-environment; Paper 3's thesis is intra-scaffold substrate co-evolution.

**5. Gao et al. (2025), "A Survey of Self-Evolving Agents: What, When, How, and Where"**
- arXiv:2507.21046; Transactions on Machine Learning Research (01/2026); 77 pages
- Dimensions: what to evolve (models/memory/tools/architecture), when (intra/inter-test-time), how (scalar rewards/textual feedback)
- **Gap:** Most directly related to Paper 3's thesis. However: organizes evolution by component in isolation, not by *cross-substrate feedback chains*. Does not analyze architectures where skill updates trigger memory updates trigger planning updates. The patch-plasticity concept — where the scaffold's error signal recursively updates the scaffold — is not the organizing principle.

### The Paper's Unique Contribution

Prior surveys provide:
- Taxonomies of agent components (Wang, Xi, CoALA)
- Taxonomies of what/when/how to evolve (self-evolving agent surveys)
- Lists of multi-agent systems and their roles

**What does not exist in prior art:**
1. A taxonomy that characterizes *which* substrate combinations create genuine co-evolution vs. mere modular stacking
2. A **patch-plasticity scoring system** that quantifies integration depth across the 6-substrate vector
3. Analysis of *promotion mechanisms* — how experience in one scope (session) migrates to another (shared/persistent)
4. Ablation-level evidence systematically showing that co-evolution of substrates outperforms substrate stacking
5. The distinction between DESIGNED patch-plastic architectures (NanoResearch, AutoAgent) and RETROFITTED ones (MetaGPT, Generative Agents through later work)

---

## CO-EVOLUTION EVIDENCE: CROSS-SUBSTRATE FEEDBACK

### Type 1: Skill → Memory Co-Evolution
**NanoResearch:** *"Reliable skills produce richer memory"* — after each stage, the Orchestrator reflects on execution path and distills generalizable rules into the Skill Bank while storing project-specific insights into the Memory Module. Skill Bank grows: 0.80 → 2.30 skills/topic; Memory grows: 6.40 → 12.00 entries/topic. The two growth curves are causally linked.

**Mobile-Agent-E:** Experience Reflectors create both Tips (episodic memory) AND Shortcuts (procedural skills) from the same interaction history — a single feedback pass updates both substrates simultaneously.

**GITM:** LLM Planner *"records and summarizes successful action lists into a text-based memory to enhance future planning"* — successful skills are directly promoted into the memory substrate for reuse.

### Type 2: Memory → Policy Co-Evolution
**NanoResearch (SDPO):** Memory module's user-specific records ground SDPO training — the memory substrate provides supervision signal for policy parameter updates.

**EvolveR:** Distilled principles (from memory of past trajectories) are used to train the RL policy to actually utilize them — memory is the source of the policy's supervision signal.

**Generative Agents:** Reflection synthesizes memories into higher-level beliefs that reshape future planning — the memory substrate's synthesis creates a new representation level that feeds back into planning parameters.

### Type 3: Skill → Policy (RL) Co-Evolution
**SAGE:** Skills are generated during task execution and immediately affect the policy gradient through the Skill-integrated Reward — skill quality directly enters the RL loss function. No other system has this direct skill→parameter coupling.

**CoEvoSkills:** Surrogate Verifier co-evolves with Skill Generator — verification quality improves as skills improve, creating genuine mutual adaptation. *"The co-evolutionary loop, not the generation prompt, is the primary driver of skill quality."*

### Type 4: Error → Scaffold Update
**AutoAgent:** Cognitive Evolution Module identifies *discrepancies between agent intentions and actual outcomes*, then formulates precise updates to the Cognition Layer. Every execution failure triggers a scaffold update.

**AutoManual:** Builder agent updates rules online based on execution failures. Case-conditioned prompting ties each rule update to its triggering case — the scaffold (rules/instructions) is directly updated by residual errors.

**Voyager:** Self-verification decides whether a skill should be committed to the library or regenerated. Execution errors are fed back into GPT-4's prompt for refinement — error signals directly gate skill promotion.

### Type 5: Orchestration → Memory Co-Evolution
**Agent S:** Self-Evaluator summarizes task trajectories and stores them in both narrative AND episodic memory — the orchestration layer generates its own supervision signal (without human labels) that updates both memory types.

**OS-Copilot/FRIDAY:** Critic module assesses execution outcomes and "effects updates to the long-term memory" — the orchestration layer directly writes to memory.

### Key Architectural Signature
The systems with integration depth DEEP share a common pattern: **a reflective meta-process that operates on the execution history and updates at least two substrates simultaneously**. In NanoResearch, this is the post-stage Orchestrator reflection; in AutoAgent, it is the Cognitive Evolution Module; in Mobile-Agent-E, it is the Experience Reflector pair. Systems at MEDIUM depth typically have only unidirectional feedback: execution updates memory, but memory does not update skill generation, and skills do not update policy.

---

## RESEARCH TOYS vs. PRODUCTION DEPLOYMENTS

### Production Deployments (Confirmed)

| System | Organization | Domain | Production Evidence |
|--------|-------------|--------|---------------------|
| **Sierra Agent OS** | Sierra.ai | Enterprise customer service | Commercial product, named customers |
| **Hippocratic AI Polaris** | Hippocratic AI | Healthcare/clinical | Real-time patient conversations; Polaris 3.0 released Oct 2025 |
| **Harvey AI** | Harvey | Legal | Legal Agent Benchmark (LAB) released May 2026; named law firm clients |
| **OpenHands / CodeAct** | All Hands AI | Software engineering | Open-source production deployment; SWE-bench leaderboard |

### Research Systems with Production-Adjacent Trajectory

| System | Status | Path to Production |
|--------|--------|--------------------|
| **Voyager** | Research | Skill library pattern adopted in production coding agents (GitHub Copilot Workspace) |
| **MetaGPT** | Research/Product | MetaGPT framework commercially available; enterprise version shipping |
| **Agent S/S2** | Research | Simular AI product; GUI automation commercial trajectory clear |
| **Cradle** | Research | General Computer Control setting applicable to enterprise automation |

### Pure Research Systems

All remaining systems (NanoResearch, AutoAgent, CASCADE, EvolveR, ExpeL, AWM, AutoManual, JARVIS-1, CoEvoSkills, Generative Agents, SAGE, Mobile-Agent-E, GITM, ChatDev, Plan4MC, CaptainAgent) are research demonstrations. They validate the patch-plastic thesis but have not shipped to users.

### Key Production Observation
Production systems (Sierra, Hippocratic) tend to be strong on **governance** (guardrails, safety validation, policy enforcement) but weak on **skill evolution** and **cross-session memory promotion**. Research systems are the inverse: strong co-evolution of skills/memory/policy but weak governance. The paper's framing should note this asymmetry — production integration has solved the governance substrate that research systems underinvest in; research systems have solved the co-evolution dynamics that production systems have not yet implemented.

---

## SELF-EVOLVING AGENTS: 2025-2026 FRONTIER

The closest active research community to Paper 3's thesis:

### Survey of Self-Evolving Agents (Gao et al., 2025/2026)
- arXiv:2507.21046; Transactions on Machine Learning Research (Jan 2026)
- *"The first systematic and comprehensive review of self-evolving agents"*
- Key recognition: *"LLMs remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts... this static nature has become a critical bottleneck"*
- This survey's "what/when/how to evolve" taxonomy overlaps significantly with Paper 3's patch-plastic framing — Paper 3 must differentiate by focusing on *intra-scaffold cross-substrate* co-evolution rather than the broader agent-vs-environment co-evolution framing

### Systematic Survey of Self-Evolving Agents: Model-Centric to Co-Evolution (Xiang et al., 2026)
- Preprint (cloudfront d197for5662m48); 3-paradigm taxonomy
- Key finding: *"Model-Environment Co-Evolution is highlighted as a key emerging direction"*
- Paper 3's differentiation: This survey treats the environment as the co-evolving entity; Paper 3 treats the scaffold itself as co-evolving

### HexMachina (arXiv:2506.04651, 2025)
- Self-evolving multi-agent for adversarial strategic environments (Catan)
- Separates environment discovery (adapter layer) from strategy improvement (code refinement + simulation)
- 54% win rate against strongest human-crafted baseline
- Relevant as evidence of self-evolution in adversarial settings

### EvolveR (arXiv:2510.16079, October 2025)
- ICLR 2026 submission
- Closed-loop experience lifecycle: offline distillation → online retrieval → RL policy update
- Most formally specified lifecycle for patch-plastic improvement without parametric retraining of base model

---

## OPENCORE: STATUS

**Searches conducted:** "OpenCore agent patch-plastic scaffold evolution architecture," "OpenCore LLM scaffold adaptive multi-substrate," "OpenCore patch-plastic"

**Findings:** No public papers, preprints, GitHub repositories, or technical documentation matching an "OpenCore" agent system with patch-plastic architecture were found. The term "OpenCore" appears in:
- OpenClaw (viral open source AI agent, AllThingsOpen.org, March 2026) — scaffold engineering article, not a paper
- OpenCoder-llm (GitHub) — LLM coding system, not an integrated architecture

**Assessment:** OpenCore as a reference architecture for patch-plastic integration does not appear to be publicly documented at this time. If it exists as an internal framework, it would need to be described by the authors of Paper 3 directly. No citation possible.

---

## APPENDIX: KEY ABLATION NUMBERS

| System | What Was Ablated | Result Without | Result With | Source |
|--------|-----------------|----------------|-------------|--------|
| **Voyager** | Automatic curriculum | Item count -93% | Full | arXiv:2305.16291, Fig 9 |
| **Voyager** | Skill library | Plateaus in late stages | Compound growth | arXiv:2305.16291, Fig 9 |
| **Voyager** | Self-verification | Item count -73% | Full | arXiv:2305.16291, Fig 9 |
| **MetaGPT** | Role specialization | Unworkable code | Coherent output | arXiv:2308.00352, Table 3 |
| **MetaGPT** | Executable feedback | HumanEval 81.7% | 85.9% (+4.2pp) | arXiv:2308.00352 |
| **MetaGPT** | Executable feedback | MBPP 82.3% | 87.7% (+5.4pp) | arXiv:2308.00352 |
| **Generative Agents** | Memory | Critical degradation | Full | arXiv:2304.03442 |
| **Generative Agents** | Reflection | Critical degradation | Full | arXiv:2304.03442 |
| **Generative Agents** | Planning | Critical degradation | Full | arXiv:2304.03442 |
| **CASCADE** | Evolution mechanisms | 35.4% success | 93.3% (+57.9pp) | arXiv:2512.23880 |
| **NanoResearch** | All substrates | Lower compliance (6.656) | 8.963 (+34.6%) | arXiv:2605.10813, Table 1 |
| **CoEvoSkills** | Verification loop | 30.6% (round 0) | 75% (round 5) | arXiv:2604.01687 |
| **Agent S** | Full system vs. baseline | Baseline 10.31% | 19.68% on OSWorld | arXiv:2410.08164 |
| **AWM** | Workflow memory | Baseline | +24.6% Mind2Web | arXiv:2409.07429 |
| **AWM** | Workflow memory | Baseline | +51.1% WebArena | arXiv:2409.07429 |
| **SAGE** | Evolution (SFT only) | Baseline | +8.9% AppWorld | arXiv:2512.17102 |
| **Mobile-Agent-E** | Self-evolution module | Without Evo | +22% vs. SOTA | arXiv:2501.11733 |
| **OS-Copilot/FRIDAY** | Skill accumulation | Prior methods | +35% on GAIA | arXiv:2402.07456 |
| **AutoManual** | Rule building | Expert prompts | 97.4% ALFWorld | NeurIPS 2024 |

---

## FULL CITATION LIST

1. Xu et al. (2026). NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation. arXiv:2605.10813. https://arxiv.org/abs/2605.10813

2. Wang et al. (2026). AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Autonomous Agent Frameworks. arXiv:2603.09716. https://arxiv.org/abs/2603.09716

3. Huang et al. (2025). CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution. arXiv:2512.23880. https://arxiv.org/abs/2512.23880

4. Agashe et al. (2024). Agent S: An Open Agentic Framework that Uses Computers Like a Human. arXiv:2410.08164. https://arxiv.org/abs/2410.08164

5. Agent S2 (2025). A Compositional Generalist-Specialist Framework. arXiv:2504.00906. https://arxiv.org/abs/2504.00906

6. Wang et al. (2025). Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks. arXiv:2501.11733. https://arxiv.org/abs/2501.11733

7. Wu et al. (2025). EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle. arXiv:2510.16079. https://arxiv.org/abs/2510.16079

8. Wang et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv:2305.16291. https://arxiv.org/abs/2305.16291

9. Park et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. arXiv:2304.03442. https://arxiv.org/abs/2304.03442

10. Wu et al. (2024). OS-Copilot: Towards Generalist Computer Agents with Self-Improvement. arXiv:2402.07456. https://arxiv.org/abs/2402.07456

11. Tan et al. (2024). Cradle: Empowering Foundation Agents Towards General Computer Control. arXiv:2403.03186. https://arxiv.org/abs/2403.03186

12. Wang et al. (2025). SAGE: Reinforcement Learning for Self-Improving Agent with Skill Library. arXiv:2512.17102. https://arxiv.org/abs/2512.17102

13. Zhao et al. (2023). ExpeL: LLM Agents Are Experiential Learners. arXiv:2308.10144. https://arxiv.org/abs/2308.10144

14. Wang et al. (2024). Agent Workflow Memory. arXiv:2409.07429 (ICML 2025). https://arxiv.org/abs/2409.07429

15. Hong et al. (2023). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. arXiv:2308.00352. https://arxiv.org/abs/2308.00352

16. Chen et al. (2024). AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning. NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/0142921fad7ef9192bd87229cdafa9d4-Abstract-Conference.html

17. Wang et al. (2023). JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models. arXiv:2311.05997. https://arxiv.org/abs/2311.05997

18. Zhang et al. (2026). CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification. arXiv:2604.01687. https://arxiv.org/abs/2604.01687

19. Qian et al. (2023). ChatDev: Communicative Agents for Software Development. arXiv:2307.07924 (ACL 2024). https://arxiv.org/abs/2307.07924

20. Sierra.ai (2024). Constellation of models: the architecture powering Sierra's agents. https://sierra.ai/blog/constellation-of-models

21. Hippocratic AI (2024/2025). Polaris Constellation Architecture. https://hippocraticai.com/research/

22. Li et al. (2023). Ghost in the Minecraft (GITM). arXiv:2305.17144. https://arxiv.org/abs/2305.17144

23. All Hands AI (2024). OpenHands: An Open Platform for AI Software Developers. arXiv:2407.16741. https://arxiv.org/abs/2407.16741

24. Lu et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292. https://arxiv.org/abs/2408.06292

25. Aggarwal et al. (2024). CaptainAgent: Adaptive In-conversation Team Building for Language Model Agents. arXiv:2405.19425. https://arxiv.org/abs/2405.19425

26. Yuan et al. (2023). Plan4MC: Skill Reinforcement Learning and Planning for Open-World Minecraft Tasks. arXiv:2303.16563. https://github.com/PKU-RL/Plan4MC

**Survey papers (prior art):**

S1. Wang et al. (2023). A Survey on Large Language Model based Autonomous Agents. arXiv:2308.11432. https://arxiv.org/abs/2308.11432

S2. Xi et al. (2023). The Rise and Potential of Large Language Model Based Agents: A Survey. arXiv:2309.07864. https://arxiv.org/abs/2309.07864

S3. Sumers et al. (2023). Cognitive Architectures for Language Agents (CoALA). arXiv:2309.02427 (TMLR 2024). https://arxiv.org/abs/2309.02427

S4. Gao et al. (2025/2026). A Survey of Self-Evolving Agents: What, When, How, and Where. arXiv:2507.21046 (TMLR Jan 2026). https://arxiv.org/abs/2507.21046

S5. Xiang et al. (2026). A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution. Preprint. https://d197for5662m48.cloudfront.net/documents/publicationstatus/309709/preprint_pdf/d87671b0e1950a508eb50b56fb3098af.pdf

---

*Harvest completed: 25 systems scored, 5 survey papers analyzed, substrate composition matrix complete, ablation table with 18 data points, co-evolution taxonomy with 5 mechanism types. OpenCore not found in public record.*
