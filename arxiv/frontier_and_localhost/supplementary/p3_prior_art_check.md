# Prior-Art Check: Has Paper 3's Slot Been Filled?

**Paper under review:** "Frontier and Localhost: Patch-Plastic Architectures for LLM Reliability"  
**Check conducted:** June 2026  
**Analyst note:** All verdicts are based on direct arXiv fetches or verified summaries. No verdict relies solely on title similarity.

---

## Methodology

**Search queries executed (pplx CLI, web + academic, 2023–2026):**

*Direct framing:*
- "patch-plastic architecture LLM" / "patch plasticity neural scaffold"
- "two-loop agent architecture survey"
- "agent scaffold survey LLM 2024 2025" / "versioned scaffold agent"
- "scaffold-based LLM reliability"

*Substrate-spanning surveys:*
- "LLM agent survey 2025 2026" / "self-evolving agent survey 2025"
- "self-improving LLM agent survey" / "cognitive architecture LLM agent survey"
- "agentic AI architecture taxonomy" / "agent skill memory tool survey LLM"

*Landmark surveys evaluated by direct arXiv fetch:*
- Wang et al. 2023 (arXiv:2308.11432) — LLM autonomous agents
- Xi et al. 2023 (arXiv:2309.07864) — Fudan rise and potential
- Sumers et al. 2023 (arXiv:2309.02427) — CoALA
- Masterman et al. 2024 (arXiv:2404.11584) — Landscape of AI agent architectures
- Tao et al. 2024 (arXiv:2404.14387) — Self-evolution of LLMs
- Gao et al. 2025/2026 (arXiv:2507.21046) — Self-evolving agents (TMLR 2026)
- Fang et al. 2025 (arXiv:2508.07407) — Comprehensive self-evolving AI agents
- Arunkumar et al. 2026 (arXiv:2601.12560) — Architectures, taxonomies, evaluation
- Jiang et al. 2025 (arXiv:2512.16301) — Adaptation of agentic AI
- Du 2026 (arXiv:2603.07670) — Memory for autonomous LLM agents
- Zhou et al. 2026 (arXiv:2605.07358) — Comprehensive survey on agent skills
- Yehudai et al. 2025 (arXiv:2503.16416) — Survey on evaluation of LLM-based agents
- ACE paper 2025 (arXiv:2510.04618) — Agentic context engineering
- AgentSquare 2025 (OpenReview, ICLR 2025) — Modular LLM agent design space

*Industry/practitioner:*
- LangChain State of Agent Engineering (2025 report)
- Latent Space 2024-in-Agents (NeurIPS 2024 live)
- Sequoia AI 50 / AI in 2025 reports
- a16z agent architecture posts

*Adjacent corners:*
- Agentic RAG surveys / tool-use surveys (arXiv:2405.17935, arXiv:2501.09136)
- Context engineering / prompt engineering surveys
- arXiv:2510.04618 — ACE (Agentic Context Engineering)

**Inclusion criteria:** Any survey, overview, framework, or position paper covering two or more of Paper 3's six substrates, OR specifically addressing feedback-driven scaffold persistence, OR proposing a two-tier (base model + wrapper) reliability architecture. Papers from 2023–2026.

**What was NOT found:** No paper uses the term "patch-plastic." No paper proposes the specific two-loop (Loop 1: within-session compounding; Loop 2: cross-project promotion) framing. No paper organizes the six specific substrates as a unified reliability architecture. The parent trilogy paper (arXiv:2505.24187) confirmed as existing and real.

---

## Verdict (one paragraph)

**The slot is open, but the neighborhood is increasingly crowded.** No paper in the 2023–2026 literature uses the "patch-plastic" framing, proposes the specific six-substrate taxonomy as a joint reliability architecture, articulates the two-loop (within-session + cross-project-promotion) design space, or frames industry vertical bundles (Harvey, Hippocratic AI, Sierra) as commercial evidence for the same architectural pattern. The closest competitors — the self-evolving agent surveys (arXiv:2507.21046, arXiv:2508.07407), the adaptation survey (arXiv:2512.16301), and the agent skills survey (arXiv:2605.07358) — each cover one or two substrates deeply but do not attempt the composite six-substrate unified framing. The memory survey (arXiv:2603.07670) independently develops closely analogous concepts (promotion, versioning, dual-buffer consolidation, cross-session persistence) but restricts its scope entirely to the memory substrate. Paper 3's most distinctive contribution — the 2×2 design-space matrix on automated vs. human gate for each loop, the NanoResearch/OpenCore composite templates, and the explicit bridge to the arXiv:2505.24187 error-math layer — appears fully unoccupied. Paper 3 should be framed as a synthesis successor to CoALA (2023) rather than a rival to any of the self-evolution surveys, which address a different question (how do agents *learn* vs. how do they *reliably deploy*).

---

## Overlap Matrix

| Paper | Year | Six-substr | Two-loop | Versioning/ Promotion | Vertical thesis | Reliability bridge | Composite 2-loop design | Verdict |
|---|---|---|---|---|---|---|---|---|
| Wang et al. — Autonomous Agents Survey | 2023 | No | No | No | No | No | No | DIFFERENT |
| Xi et al. (Fudan) — Rise and Potential | 2023 | No | No | No | No | No | No | DIFFERENT |
| Sumers et al. — CoALA | 2023 | Partial | No | No | No | No | No | ADJACENT |
| Masterman et al. — AI Agent Landscapes | 2024 | No | No | No | No | No | No | DIFFERENT |
| Tao et al. — Self-Evolution of LLMs | 2024 | No | No | No | No | No | No | DIFFERENT |
| AgentSquare (ICLR 2025) | 2025 | Partial | No | No | No | No | No | TANGENTIAL |
| Gao et al. — Self-Evolving Agents (TMLR) | 2025/26 | Partial | No | No | Partial | No | No | ADJACENT |
| Fang et al. — Comprehensive Self-Evolving | 2025 | Partial | No | No | Partial | No | No | ADJACENT |
| Jiang et al. — Adaptation of Agentic AI | 2025 | Partial | No | No | Partial | No | No | ADJACENT |
| Du — Memory for Autonomous LLM Agents | 2026 | Partial* | Partial* | Partial* | No | No | No | ADJACENT |
| Zhou et al. — Agent Skills Survey | 2026 | Partial | No | No | No | No | No | ADJACENT |
| ACE (Agentic Context Engineering) | 2025 | Partial | No | No | Partial | No | No | TANGENTIAL |
| Arunkumar et al. — Architectures Taxonomies | 2026 | Partial | No | No | No | No | No | DIFFERENT |
| Yehudai et al. — Evaluation of LLM Agents | 2026 | No | No | No | No | No | No | DIFFERENT |
| LangChain State of Agent Engineering | 2025 | No | No | No | No | No | No | DIFFERENT |

*Du 2026 covers memory substrate only, but within that substrate develops versioning, promotion, and cross-session concepts independently.

---

## Per-Paper Detailed Analysis

### 1. Wang et al. — "A Survey on Large Language Model based Autonomous Agents"

**Citation:**  
Lei Wang, Chengbang Ma, Xueyang Feng, et al. (2023). *Frontiers of Computer Science*, DOI: 10.1007/s11704-024-40231-1. arXiv preprint 2308.11432 (Aug 2023).  
URL: https://link.springer.com/10.1007/s11704-024-40231-1

**Abstract / TL;DR:**  
Comprehensive survey of LLM-based autonomous agents. Proposes a unified construction framework, surveys applications in social science, natural science, and engineering, and reviews evaluation strategies.

**What it covers:**  
- Construction taxonomy: perception, memory, action, planning
- Application survey: social simulation, code generation, research
- Evaluation: task success, generalization, efficiency

**What it does NOT cover that Paper 3 would:**  
- No versioning or promotion of scaffold artifacts
- No cross-session persistence as a design axis
- No two-tier (frontier + localhost) architecture
- No feedback-driven outer loop modifying persisted artifacts
- No industry vertical bundling thesis
- No governance layer
- No error-residual bridge to token-level reliability math

**Direct quote on scope:**  
> "In this paper, we present a comprehensive survey of these studies, delivering a systematic review of LLM-based autonomous agents from a holistic perspective. We first discuss the construction of LLM-based autonomous agents, proposing a unified framework that encompasses much of previous work."

**Verdict: DIFFERENT.** Wang 2023 surveys what agents *are* and what they can *do*. Paper 3 is about how the scaffold wrapper around a frozen frontier model *reliably evolves* over deployment time. These are orthogonal questions.

---

### 2. Xi et al. (Fudan) — "The Rise and Potential of Large Language Model Based Agents"

**Citation:**  
Zhiheng Xi, Wenxiang Chen, Xin Guo, et al. (Fudan NLP Group, 2023). arXiv:2309.07864 [cs.AI], 86 pages.  
URL: https://arxiv.org/abs/2309.07864

**Abstract / TL;DR:**  
Comprehensive survey of LLM-based agents framed around brain/perception/action. Explores single-agent, multi-agent, and human-agent cooperation scenarios, plus agent societies.

**What it covers:**  
- Brain (memory, knowledge, reasoning), perception, action framework
- Single-agent, multi-agent, human-agent cooperation
- Agent societies and emergent phenomena
- Key topics: safety, evaluation, trustworthiness

**What it does NOT cover that Paper 3 would:**  
- No persistence across sessions as architectural design dimension
- No versioning/promotion/governance layer
- No scaffold-update feedback loop
- No industry vertical bundling
- No two-tier reliability architecture
- "Brain/perception/action" triad differs fundamentally from Paper 3's six-substrate framing

**Direct quote on scope:**  
> "Building upon this, we present a general framework for LLM-based agents, comprising three main components: brain, perception, and action, and the framework can be tailored for different applications."

**Verdict: DIFFERENT.** Xi et al. 2023 is the canonical "what are agents" survey for the pre-production era. Paper 3 addresses the post-deployment reliability architecture question, which this paper does not reach.

---

### 3. Sumers et al. — "Cognitive Architectures for Language Agents" (CoALA)

**Citation:**  
Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths (2023). TMLR camera ready (Mar 2024). arXiv:2309.02427 [cs.AI].  
URL: https://arxiv.org/abs/2309.02427

**Abstract / TL;DR:**  
Draws on cognitive science and symbolic AI to propose CoALA: a language agent architecture with modular memory components, structured action space, and generalized decision-making process. Retrospectively surveys existing work and prospectively identifies directions toward more capable agents.

**What it covers:**  
- Modular memory (working, episodic, semantic, procedural)
- Action space: retrieval, reasoning, learning, decision
- Connection to classical cognitive architectures (ACT-R, SOAR)
- Decision-making cycle: planning + execution

**What it does NOT cover that Paper 3 would:**  
- No versioning or promotion of scaffold artifacts
- No cross-session persistence operationalized as deployment design axis
- No outer feedback loop modifying persisted system artifacts
- No governance layer
- No industry vertical bundling thesis
- No two-tier (frontier model vs. localhost scaffold) framing
- No error-residual bridge
- Memory taxonomy does not map to Paper 3's six substrates (CoALA's procedural memory ≈ Paper 3's skill library substrate only)

**Direct quote on scope:**  
> "CoALA describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments, and a generalized decision-making process to choose actions. We use CoALA to retrospectively survey and organize a large body of recent work, and prospectively identify actionable directions towards more capable agents."

**Verdict: ADJACENT.** CoALA is the closest prior architecture framework to Paper 3's spirit, and Paper 3 should cite it explicitly as a predecessor. But CoALA's memory taxonomy is a static snapshot of agent internals; Paper 3's six-substrate stack is a dynamic deployment architecture with feedback loops and governance. CoALA does not reach cross-session versioning, promotion, or the frontier/localhost split.

---

### 4. Masterman et al. — "The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling"

**Citation:**  
Tula Masterman, Sandi Besen, Mason Sawtell, Alex Chao (2024). arXiv:2404.11584 [cs.AI], 13 pages.  
URL: https://arxiv.org/abs/2404.11584

**Abstract / TL;DR:**  
Short survey focused on single-agent vs. multi-agent architecture patterns for reasoning, planning, and tool execution. Identifies feedback, task decomposition, and role definition as key performance drivers.

**What it covers:**  
- Single-agent patterns (ReAct, planning)
- Multi-agent patterns (supervisor, parallelization)
- Reflection/feedback as quality mechanism
- Key themes: leadership, communication styles, planning/execution/reflection phases

**What it does NOT cover that Paper 3 would:**  
- No persistent scaffold across sessions
- No versioning or governance
- No industry vertical bundles
- No error-residual math
- No six-substrate taxonomy
- No two-loop outer-loop framing
- 13-page paper; not a comprehensive survey

**Direct quote on scope:**  
> "Our contribution outlines key themes when selecting an agentic architecture, the impact of leadership on agent systems, agent communication styles, and key phases for planning, execution, and reflection that enable robust AI agent systems."

**Verdict: DIFFERENT.** A brief practitioner survey of single vs. multi-agent patterns. Overlaps with Paper 3 only in acknowledging reflection, but has no cross-session or versioning dimension.

---

### 5. Tao et al. — "A Survey on Self-Evolution of Large Language Models"

**Citation:**  
Zhengwei Tao, Ting-En Lin, Xiancai Chen, et al. (2024). arXiv:2404.14387 [cs.CL]. Submitted Apr 2024.  
URL: https://arxiv.org/abs/2404.14387

**Abstract / TL;DR:**  
Proposes a conceptual framework for LLM self-evolution: iterative cycles of (1) experience acquisition, (2) experience refinement, (3) updating, (4) evaluation. Surveys training-time self-improvement methods.

**What it covers:**  
- Self-evolution via the model itself (weight updating)
- Four-phase cycle: acquire, refine, update, evaluate
- Training and fine-tuning paradigms

**What it does NOT cover that Paper 3 would:**  
- Self-evolution here is *training-time* (weight updates); Paper 3 addresses *scaffold-time* evolution (artifact updates with frozen weights)
- No scaffold substrates
- No versioning/promotion/governance of artifacts
- No cross-session persistence of external artifacts
- No industry vertical thesis
- No two-tier architecture

**Direct quote on scope:**  
> "We first propose a conceptual framework for self-evolution and outline the evolving process as iterative cycles composed of four phases: experience acquisition, experience refinement, updating, and evaluation."

**Verdict: DIFFERENT.** Self-evolution surveys (Tao 2024 and the 2025–2026 successors) address how models *learn* by updating weights or internal representations. Paper 3 addresses how the *scaffold around a frozen model* evolves. These are architecturally and conceptually distinct.

---

### 6. Gao et al. — "A Survey of Self-Evolving Agents: What, When, How" (TMLR 2026)

**Citation:**  
Huan-ang Gao, Jiayi Geng, Wenyue Hua, et al. (2025/2026). arXiv:2507.21046, Transactions on Machine Learning Research (01/2026). 77 pages.  
URL: https://arxiv.org/abs/2507.21046

**Abstract / TL;DR:**  
First systematic review of self-evolving agents organized around three dimensions: what to evolve, when to evolve, how to evolve. Covers evolution of models, memory, tools, and architecture. Discusses intra-test-time and inter-test-time adaptation categories.

**What it covers:**  
- Three-dimension framework: what/when/how to evolve
- Agent components: models, memory, tools, architecture
- Adaptation stages: intra-test-time vs. inter-test-time (close to Paper 3's Loop 1 / Loop 2 concept)
- Applications: coding, education, healthcare (partial industry verticals)
- Evaluation, safety, scalability challenges

**What it does NOT cover that Paper 3 would:**  
- "Inter-test-time" is not equivalent to Paper 3's Loop 2 (cross-project promotion with governance)
- No versioning, governance, or promotion mechanism
- No six-substrate unified framing (treats components separately)
- No two-tier frontier+localhost architecture
- No 2×2 design-space matrix on gate automation
- No error-residual bridge
- No industry vertical bundling as commercial evidence pattern
- Industry domains (coding, education, healthcare) not linked to specific companies' architectural choices

**Direct quote on scope:**  
> "This survey provides the first systematic and comprehensive review of self-evolving agents, organizing the field around three foundational dimensions: what to evolve, when to evolve, and how to evolve. We examine evolutionary mechanisms across agent components (e.g., models, memory, tools, architecture), categorize adaptation methods by stages (e.g., intra-test-time, inter-test-time), and analyze the algorithmic and architectural designs that guide evolutionary adaptation."

**Pre-emption check:** The intra/inter-test-time distinction is structurally similar to Paper 3's Loop 1 / Loop 2 distinction. Paper 3 should cite this and explicitly differentiate: Gao et al.'s "inter-test-time" covers any update between test episodes, whereas Paper 3's Loop 2 specifically requires a *promotion* event (local artifact → governed shared artifact) with an optional human gate — a governance concept absent from Gao et al.

**Verdict: ADJACENT.** Closest single-dimension overlap with Paper 3's temporal framing, but lacks the governance/promotion apparatus, the six-substrate unified framing, and the reliability-bridge motivation.

---

### 7. Fang et al. — "A Comprehensive Survey of Self-Evolving AI Agents"

**Citation:**  
Jinyuan Fang, Yanwen Peng, Xi Zhang, et al. (2025). arXiv:2508.07407 [cs.AI]. Submitted Aug 2025.  
URL: https://arxiv.org/abs/2508.07407

**Abstract / TL;DR:**  
Reviews self-evolving agentic systems. Introduces a unified framework with four key components: System Inputs, Agent System, Environment, and Optimisers. Covers evolution techniques for agent components: core LLM, prompt strategies, memory, tool integration, workflow topologies.

**What it covers:**  
- Feedback loop framework (System Inputs → Agent System → Environment → Optimisers)
- Evolution targets: LLM behavior, prompt strategies, memory, tool integration, workflow
- Domain-specific evolution: biomedicine, programming, finance
- Evaluation, safety, ethics

**What it does NOT cover that Paper 3 would:**  
- Prompt strategies treated as one component, not as the "persistent instructions" substrate with version history
- No versioning or promotion artifacts
- No governance layer distinguishing local from shared artifacts
- No two-tier frontier+localhost architecture
- No two-loop design-space matrix with gate automation
- No error-residual bridge
- Industry verticals (bio, programming, finance) not organized around a vertical-bundle thesis

**Direct quote on scope:**  
> "We first introduce a unified conceptual framework that abstracts the feedback loop underlying the design of self-evolving agentic systems. The framework highlights four key components: System Inputs, Agent System, Environment, and Optimisers... These components include the core LLM's behavior, prompt strategies, memory mechanisms, tool integration, and in multi-agent settings, workflow topologies and communication protocols."

**Verdict: ADJACENT.** Covers overlapping evolutionary territory. Stronger on the what/how of evolution mechanics; weaker on governance architecture and deployment reliability. Paper 3's contribution is the *structured substrate-by-substrate reliability architecture*, not just the existence of feedback loops.

---

### 8. Jiang et al. — "Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills"

**Citation:**  
Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi, et al. (2025). arXiv:2512.16301 [cs.AI]. 18 Dec 2025 (v1); revised 9 Mar 2026.  
URL: https://arxiv.org/abs/2512.16301

**Abstract / TL;DR:**  
Surveys adaptation of agentic AI across four paradigms: A1/A2 (agent self-improvement) and T1/T2 (tool adaptation). Reviews post-training methods, adaptive memory architectures, and agent skills. Evaluates trade-offs in cost, flexibility, and generalization.

**What it covers:**  
- Four-paradigm framework: agent-centric (A1/A2) vs. tool-centric (T1/T2)
- Post-training (fine-tuning, RL with verifiable rewards)
- Memory adaptation
- Skill libraries (T2 paradigm)
- Applications: deep research, software development, computer use, drug discovery
- Open problems: continual learning, safety

**What it does NOT cover that Paper 3 would:**  
- No versioning or governance of artifacts
- No promotion from local to shared/governed state
- No cross-session persistence as explicit design axis
- No two-loop framing
- No two-tier frontier+localhost architecture
- No error-residual bridge
- No 2×2 design-space matrix
- No industry vertical bundling (domains mentioned but not as architectural thesis)
- A1/A2 paradigms focus on *weight-updating* adaptation; T1/T2 is closer but does not address governance

**Direct quote on scope:**  
> "We organize the field with a four-paradigm framework spanning agent adaptation and tool adaptation... This survey studies these developments under a single notion of adaptation: improving an agent, its tools, or their interaction after pretraining."

**Verdict: ADJACENT.** Covers the adaptation dimension of Paper 3's concern, but entirely from a training/architecture perspective. Does not address the deployment governance layer, versioning, or the explicit two-tier reliability architecture. The T2 paradigm (agent-supervised tool adaptation) is the closest overlap — Paper 3's skill libraries and memory substrates live there — but Paper 3 adds the governance/promotion apparatus T2 omits.

---

### 9. Du — "Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers"

**Citation:**  
Pengfei Du (2026). arXiv:2603.07670 [cs.AI]. Submitted 8 Mar 2026.  
URL: https://arxiv.org/abs/2603.07670

**Abstract / TL;DR:**  
Structured account of memory design, implementation, and evaluation for LLM agents, 2022–2026. Proposes three-dimensional taxonomy (temporal scope, representational substrate, control policy) and five mechanism families. Notably discusses versioning, promotion, dual-buffer consolidation, and cross-session persistence.

**What it covers:**  
- Three-dimensional taxonomy: temporal scope, representational substrate (text/vector/SQL-graph/code-skills), control policy
- Five mechanism families: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, policy-learned management
- **Temporal versioning** (prefer newest record, contradiction detection)
- **Promotion/graduation** from episodic to semantic status, dual-buffer consolidation with quality gates
- **Cross-session persistence** as explicit design axis (LoCoMo, MemoryArena benchmarks)
- **Schema versioning** for tool-use records
- Applications: personal assistants, coding agents, scientific reasoning, multi-agent teamwork

**What it does NOT cover that Paper 3 would:**  
- Scope is the *memory substrate only* — does not unify with persistent instructions, skill libraries, tools, orchestration, or governance as a joint six-substrate architecture
- No two-tier frontier+localhost architecture framing
- No two-loop (within-session vs. cross-project-promotion) design space
- No governance layer distinguishing local from shared artifacts at the *system* level
- No industry vertical bundling thesis
- No error-residual bridge to token reliability math
- No 2×2 design-space matrix
- "Promotion" in Du 2026 is memory-internal (episodic→semantic); Paper 3's "promotion" is cross-boundary (individual project → governed shared repo)

**Direct quote on scope:**  
> "This survey offers a structured account of how memory is designed, implemented, and evaluated in modern LLM-based agents... We formalize agent memory as a write–manage–read loop tightly coupled with perception and action, then introduce a three-dimensional taxonomy spanning temporal scope, representational substrate, and control policy."

**Pre-emption check:** Du 2026 is the paper most likely to cause a reviewer objection for Paper 3's memory substrate section. The concepts of temporal versioning, dual-buffer consolidation, and promotion within a memory system appear here. Paper 3 must acknowledge this paper and clearly distinguish: Du addresses memory-internal lifecycle management; Paper 3 addresses the cross-substrate governance architecture in which memory is one of six layers, each with its own feedback loop and promotion pathway.

**Verdict: ADJACENT** (strongest overlap candidate on individual substrate). Not a duplicate because its scope is deliberately restricted to memory, does not touch the other five substrates, and does not propose the governance/versioning architecture Paper 3 describes.

---

### 10. Zhou et al. — "A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications"

**Citation:**  
Yingli Zhou, Wang Shu, Yaodong Su, et al. (2026). arXiv:2605.07358 [cs.IR]. Submitted 8 May 2026.  
URL: https://arxiv.org/abs/2605.07358

**Abstract / TL;DR:**  
Focused survey on agent skills as "reusable procedural artifacts." Organizes around four lifecycle stages: representation, acquisition, retrieval, evolution. Reviews open challenges in quality control, interoperability, safe updating, and long-term capability management.

**What it covers:**  
- Skill lifecycle: representation → acquisition → retrieval → evolution
- Skill as "reusable procedural artifacts that coordinate tools, memory, and runtime context"
- Ecosystem resources, application settings
- Open challenges: quality control, interoperability, safe updating, long-term capability management

**What it does NOT cover that Paper 3 would:**  
- Scope is the *skill library substrate only*
- No versioning or promotion of skills across projects (cross-project governance absent)
- No cross-session persistence framing
- No two-loop design space
- No governance/promotion architecture
- No industry vertical bundling
- No error-residual bridge
- No two-tier frontier+localhost framing
- "Long-term capability management" is identified as an open challenge — precisely what Paper 3's governance substrate proposes to answer

**Direct quote on scope:**  
> "We organize the literature around four stages of the agent skill lifecycle — representation, acquisition, retrieval, and evolution — and review representative methods, ecosystem resources, and application settings across each stage. We conclude by discussing open challenges in quality control, interoperability, safe updating, and long-term capability management."

**Verdict: ADJACENT.** Covers the skill substrate of Paper 3 in considerable depth. Its open challenges section ("safe updating" and "long-term capability management") explicitly acknowledges the gap Paper 3's governance substrate fills. A Paper 3 reviewer will ask why Paper 3's skill governance section goes beyond this — Paper 3's answer is the promotion-to-shared-repo mechanism with version history and human gates.

---

### 11. "Agentic Context Engineering" (ACE) — arXiv:2510.04618

**Citation:**  
(Authors per arXiv page, 2025). arXiv:2510.04618. Submitted Oct 2025.  
URL: https://arxiv.org/abs/2510.04618

**Abstract / TL;DR:**  
Introduces ACE, a framework treating contexts as "evolving playbooks" that accumulate, refine, and organize strategies through generation, reflection, and curation. Optimizes both offline (system prompts) and online (agent memory). Shows +10.6% on agents, +8.6% on finance.

**What it covers:**  
- System-prompt optimization as an evolving artifact (offline ACE)
- Agent memory as an evolving artifact (online ACE)
- Self-improvement without labeled supervision (execution feedback)
- Finance domain vertical

**What it does NOT cover that Paper 3 would:**  
- Treats context as a single unified artifact; Paper 3 separates six distinct substrates with different error-residual classes
- No versioning or promotion mechanism
- No governance layer
- No two-loop framing
- No cross-project promotion
- No industry vertical bundling thesis
- No error-residual bridge
- No frontier+localhost two-tier architecture

**Direct quote on scope:**  
> "We introduce ACE (Agentic Context Engineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation."

**Verdict: TANGENTIAL.** ACE is a system paper with partial overlap on the persistent-instructions and memory substrates. Its framing (context = single artifact) is fundamentally simpler than Paper 3's six-substrate model. Paper 3 should cite ACE as evidence that context evolution is already being studied, but Paper 3's contribution is the unified cross-substrate governance architecture.

---

### 12. AgentSquare — "Automatic LLM Agent Search in Modular Design Space" (ICLR 2025)

**Citation:**  
Yu Shang, Yu Li, Keyu Zhao, et al. (2025). ICLR 2025 Poster. OpenReview: mPdmDYIQ7f.  
URL: https://openreview.net/forum?id=mPdmDYIQ7f

**Abstract / TL;DR:**  
Proposes a modular design space for LLM agents with four modules (Planning, Reasoning, Tool Use, Memory) and an automatic agent search framework (AgentSquare) using module evolution and recombination. Achieves +17.2% over best human designs on six benchmarks.

**What it covers:**  
- Modular design space: Planning, Reasoning, Tool Use, Memory
- Automatic search for optimized module combinations
- Module evolution and recombination mechanisms
- Evaluation across web, embodied, tool-use, game applications

**What it does NOT cover that Paper 3 would:**  
- No versioning or governance of modules across deployments
- No cross-session persistence as design axis
- No outer feedback loop updating persisted artifacts
- No promotion mechanism
- No industry vertical bundling
- No error-residual bridge
- Four modules ≠ Paper 3's six substrates (AgentSquare omits persistent instructions and governance substrates entirely)
- Auto-search optimizes *module selection*, not *artifact lifecycle management*

**Direct quote on scope:**  
> "We propose a modular design space that abstracts existing LLM agent designs into four fundamental modules with uniform IO interface: Planning, Reasoning, Tool Use, and Memory."

**Verdict: TANGENTIAL.** AgentSquare and Paper 3 both modularize agent architectures, but AgentSquare is about search over module combinations for task performance, while Paper 3 is about how individual module instances *reliably evolve* over deployment time. Different problem statements.

---

### 13. Arunkumar et al. — "Agentic AI: Architectures, Taxonomies, and Evaluation" (arXiv:2601.12560)

**Citation:**  
Arunkumar V, Gangadharan G.R., Rajkumar Buyya (2026). arXiv:2601.12560 [cs.AI]. Submitted 18 Jan 2026.  
URL: https://arxiv.org/abs/2601.12560

**Abstract / TL;DR:**  
Proposes a unified taxonomy of agentic AI with six dimensions: Perception, Brain, Planning, Action, Tool Use, Collaboration. Reviews evolution from linear to hierarchical multi-agent systems, transition from fixed APIs to MCP. Highlights open challenges: hallucination in action, infinite loops, prompt injection.

**What it covers:**  
- Taxonomy: Perception, Brain, Planning, Action, Tool Use, Collaboration
- Multi-agent coordination topologies
- MCP and Computer Use as interface standards
- Software engineering, scientific discovery, web navigation environments
- Safety: hallucination in action, infinite loops, prompt injection

**What it does NOT cover that Paper 3 would:**  
- No versioning, promotion, or governance of artifacts
- No cross-session persistence as design axis
- No feedback-driven scaffold updates
- No industry vertical bundling thesis
- No error-residual bridge
- No two-loop framing
- Six taxonomy dimensions ≠ Paper 3's six substrates (different cut of the space)

**Verdict: DIFFERENT.** Broad taxonomy paper covering similar territory to Wang/Xi/Masterman in 2026 update form. No intersection with Paper 3's core thesis on scaffold lifecycle governance.

---

### 14. Yehudai et al. — "A Survey on Evaluation of LLM-based Agents" (arXiv:2503.16416)

**Citation:**  
Asaf Yehudai, Lilach Eden, Alan Li, et al. (2025/2026). arXiv:2503.16416 [cs.AI]. ACL Findings. Revised Apr 2026.  
URL: https://arxiv.org/abs/2503.16416

**What it covers:**  
- Agent evaluation: planning, tool use, self-reflection, memory
- Application-specific benchmarks: web, SWE, scientific, conversational
- Generalist agent evaluation and leaderboards
- Harness/scaffold distinction (notes that backbone LLM vs. agent harness should be evaluated separately)

**What it does NOT cover that Paper 3 would:**  
- Evaluation focus; does not propose an architecture
- No versioning, governance, promotion
- No cross-session persistence design
- No two-loop framing
- No industry vertical bundling

**Notable:** Explicitly coins "agent harness" as distinct from LLM backbone — structurally similar to Paper 3's "localhost scaffold" concept — but does not develop it architecturally.

**Verdict: DIFFERENT.** Evaluation survey; does not occupy the same slot.

---

### 15. LangChain — "State of Agent Engineering" (2025 report)

**Citation:**  
LangChain (2025). Survey of 1,300+ professionals. Dec 2025.  
URL: https://www.langchain.com/state-of-agent-engineering

**What it covers:**  
- Deployment status, evaluation practices, use-case maturity
- Mix of human and automated evaluation (LLM-as-judge: 53.3%)
- Industry adoption by sector

**What it does NOT cover that Paper 3 would:**  
- Practitioner survey; no architectural framework
- No substrate taxonomy, no versioning/governance, no two-loop

**Verdict: DIFFERENT.** Industry survey, not an architectural framework paper.

---

## The Strongest Competitors

### Competitor 1 (Closest): Du 2026 — "Memory for Autonomous LLM Agents" (arXiv:2603.07670)

**Why it is the strongest threat:** Du 2026 independently develops, within the memory substrate, the exact conceptual apparatus of Paper 3's memory layer: temporal versioning, promotion (episodic → semantic graduation), dual-buffer consolidation with quality gates, cross-session persistence, and even schema versioning for tool-use records. A reviewer familiar with Du 2026 will ask: "Hasn't the versioning/promotion idea already been published?"

**How Paper 3 is distinct:**
1. Du's versioning and promotion are *memory-internal* (within the memory management system). Paper 3's governance substrate operates *across* all six substrates — it is a version control system for the entire scaffold stack, not just memory.
2. Du does not propose the two-loop (within-session / cross-project-promotion) design space.
3. Du does not propose the frontier+localhost two-tier architecture.
4. Du does not bridge to error-residual math.
5. Du does not unify the six substrates into a coherent reliability framework.
6. Du does not argue the industry vertical bundle thesis.

**Recommendation:** Paper 3 should cite Du 2026 in the memory substrate section and explicitly note that Du's "promotion" concept is a per-substrate instance of the more general governance mechanism Paper 3 proposes. This citation makes Paper 3 stronger by grounding its cross-substrate claims in a well-developed single-substrate precedent.

---

### Competitor 2: Gao et al. 2026 — "A Survey of Self-Evolving Agents" (arXiv:2507.21046, TMLR)

**Why it is a significant threat:** The intra-test-time / inter-test-time distinction in Gao et al. structurally maps onto Paper 3's Loop 1 / Loop 2. TMLR 2026 publication gives it high visibility.

**How Paper 3 is distinct:**
1. "Inter-test-time" in Gao et al. means *any* update between episodes (weight fine-tuning, prompt rewriting, memory update). Paper 3's Loop 2 specifically requires a *promotion event* — a versioned, governed artifact crossing from local context to shared repository with optional human gate. Governance is entirely absent from Gao et al.
2. Gao et al. focuses on *how agents learn*; Paper 3 focuses on *how the scaffold reliably deploys*.
3. The six-substrate unified framing, 2×2 design matrix, and NanoResearch/OpenCore templates are absent.
4. The frontier+localhost two-tier architecture and error-residual bridge are absent.
5. Gao et al.'s "agent components" (models, memory, tools, architecture) are not organized around error-residual classes.

**Recommendation:** Paper 3 should cite Gao et al. as the leading self-evolution survey and explicitly state that patch-plasticity is a deployment-architecture concept orthogonal to self-evolution's training-architecture focus. The loop framing should be differentiated clearly in Paper 3's Loop 2 definition section.

---

### Competitor 3: Jiang et al. 2025 — "Adaptation of Agentic AI" (arXiv:2512.16301)

**Why it is a significant threat:** Jiang et al. covers three of Paper 3's six substrates (memory, skills, tools) under a unified "adaptation" frame, and applies the framework to multiple application domains.

**How Paper 3 is distinct:**
1. "Adaptation" in Jiang et al. means *learning* (fine-tuning, RL); Paper 3's patch-plasticity means *scaffold artifact management* (persist, version, promote) without weight changes.
2. Governance, versioning, and promotion are entirely absent.
3. The persistent-instructions substrate and the governance/versioning substrate are not covered.
4. The two-loop design space and 2×2 automation matrix are absent.
5. The frontier+localhost two-tier framing and error-residual bridge are absent.

**Recommendation:** Paper 3 should cite Jiang et al. in the background section and explicitly position patch-plasticity as complementary to (not competing with) adaptation: adaptation changes what the model *knows*; patch-plasticity changes what the *scaffold* maintains across deployments of an unchanged model.

---

## Honest Synthesis

### What is genuinely novel about Paper 3 after this check?

1. **The "patch-plastic" term and concept itself.** No paper uses this framing. The analogy to synaptic plasticity applied to software scaffold artifacts — where the "weights" are external versioned artifacts rather than neural parameters — is original. Zero prior-art hits on "patch-plastic."

2. **The six-substrate taxonomy as a unified reliability architecture.** While individual substrates are covered by Du (memory), Zhou et al. (skills), ACE (instructions+memory), and Jiang et al. (memory+skills+tools), no paper organizes all six (persistent instructions, skill libraries, memory, tool/context attachment, orchestration/swarms, governance/versioning) as a *joint* reliability architecture where each substrate compensates for a distinct residual-error class.

3. **The 2×2 design-space matrix on automated vs. human gate per loop.** This is entirely absent from the prior art. The NanoResearch (auto/auto) and OpenCore (human/human) composite templates as named design archetypes also appear to be original.

4. **The bridge to arXiv:2505.24187's three-layer error math.** No surveyed paper explicitly derives scaffold architecture from a formal reliability model. This positions Paper 3 as the applied architecture partner to Paper 1's mathematical foundations — a structurally novel contribution within the trilogy framing.

5. **The industry vertical-bundle thesis (Harvey, Hippocratic AI, Sierra) as commercial evidence.** The Sequoia AI 50 report (2025) mentions Harvey as an example of full-workflow agents but makes no architectural argument. No academic paper organizes these companies' products as evidence for a specific architectural pattern.

6. **Cross-project promotion with governance as first-class concept.** Du 2026 develops promotion within memory; no paper develops it at the scaffold-system level with versioning and human gates.

### What sections of Paper 3 are LESS novel than the trilogy framing suggested?

1. **Memory substrate section.** Du 2026 (arXiv:2603.07670) is a dense, rigorous survey of memory mechanisms including temporal versioning, promotion, and cross-session persistence. Paper 3's memory substrate section must make a clear contribution beyond Du's coverage or explicitly defer to Du and focus its energy on the *governance integration* of the memory substrate with the other five.

2. **Skill library substrate section.** Zhou et al. 2026 (arXiv:2605.07358) covers skill representation, acquisition, retrieval, and evolution with considerable depth. Paper 3's skill substrate section adds primarily the governance/promotion architecture, not new mechanism taxonomy.

3. **Self-evolving agent framing.** The observation that agents should evolve their scaffolds based on feedback is thoroughly covered by the self-evolution surveys (Gao 2026, Fang 2025). Paper 3's novelty is the *architecture* of how this evolution is governed, not the observation that it occurs.

4. **The existence of feedback loops.** ACE (arXiv:2510.04618) already demonstrates empirically that evolving system prompts and memory based on execution feedback improves performance. The idea is not new; Paper 3's contribution is the *structured substrate-by-substrate governance framework* around it.

### What angle does Paper 3 own that no surveyed work covers?

The angle Paper 3 owns uniquely is the **governance layer as a first-class architectural substrate**: the claim that the sixth substrate (governance/versioning/promotion) is not scaffolding overhead but the *reliability mechanism* that makes the other five substrates coherent across projects and time. No surveyed paper makes this claim or develops the promotion-to-shared-repo mechanism with version history and human gates as a design primitive. This is Paper 3's white space.

Combined with the **two-tier framing** (frontier model as slow-changing deep weights; localhost scaffold as fast-changing versioned artifact stack), Paper 3 frames reliability as a property of the *model-scaffold composite*, not of the model alone. This composite unit-of-reliability framing is absent from all surveyed work, which either analyzes the model or the agent scaffold but not their joint reliability as a versioned two-tier system.

### Should Paper 3 be repositioned?

**Yes, with a specific recommendation:** Paper 3 should position itself as a direct successor to CoALA (Sumers et al. 2023), updating CoALA's static cognitive-architecture snapshot into a *dynamic deployment architecture with governance*. This positioning is strong because:

1. CoALA is widely cited (TMLR, well-known authors) and provides a legitimate launching point.
2. CoALA explicitly calls for "actionable directions towards more capable agents" — Paper 3 answers this call for the deployment governance direction.
3. This positioning distances Paper 3 from the self-evolution surveys (Gao, Fang, Tao) whose framing it superficially resembles but conceptually differs from.
4. A clear "CoALA → Patch-Plastic" lineage helps readers understand the contribution without requiring them to first dismiss the self-evolution framing.

**Secondary positioning:** Paper 3 should also explicitly cite Du 2026 and Zhou et al. 2026 as peer substrate-specific surveys and claim the synthesis role: "We integrate and generalize the per-substrate analyses of [Du 2026, Zhou 2026, ACE 2025] into a six-substrate unified governance architecture."

---

## Source Index

| ID | Authors | Title | Year | URL |
|---|---|---|---|---|
| Wang-2023 | Lei Wang et al. | A Survey on Large Language Model based Autonomous Agents | 2023 | https://link.springer.com/10.1007/s11704-024-40231-1 |
| Xi-2023 | Zhiheng Xi et al. | The Rise and Potential of Large Language Model Based Agents | 2023 | https://arxiv.org/abs/2309.07864 |
| CoALA-2023 | Sumers, Yao, Narasimhan, Griffiths | Cognitive Architectures for Language Agents | 2023 | https://arxiv.org/abs/2309.02427 |
| Masterman-2024 | Masterman, Besen, Sawtell, Chao | The Landscape of Emerging AI Agent Architectures | 2024 | https://arxiv.org/abs/2404.11584 |
| Tao-2024 | Zhengwei Tao et al. | A Survey on Self-Evolution of Large Language Models | 2024 | https://arxiv.org/abs/2404.14387 |
| AgentSquare-2025 | Yu Shang et al. | Automatic LLM Agent Search in Modular Design Space | 2025 | https://openreview.net/forum?id=mPdmDYIQ7f |
| ACE-2025 | (per arXiv) | Agentic Context Engineering (ACE) | 2025 | https://arxiv.org/abs/2510.04618 |
| Adaptation-2025 | Pengcheng Jiang et al. | Adaptation of Agentic AI: Post-Training, Memory, and Skills | 2025 | https://arxiv.org/abs/2512.16301 |
| SelfEvolving-TMLR-2026 | Huan-ang Gao et al. | A Survey of Self-Evolving Agents: What, When, How | 2025/2026 | https://arxiv.org/abs/2507.21046 |
| SelfEvolvingComp-2025 | Jinyuan Fang et al. | A Comprehensive Survey of Self-Evolving AI Agents | 2025 | https://arxiv.org/abs/2508.07407 |
| ArchTax-2026 | Arunkumar V et al. | Agentic AI: Architectures, Taxonomies, Evaluation | 2026 | https://arxiv.org/abs/2601.12560 |
| MemorySurvey-2026 | Pengfei Du | Memory for Autonomous LLM Agents | 2026 | https://arxiv.org/abs/2603.07670 |
| SkillsSurvey-2026 | Yingli Zhou et al. | Comprehensive Survey on Agent Skills | 2026 | https://arxiv.org/abs/2605.07358 |
| EvalSurvey-2026 | Asaf Yehudai et al. | Survey on Evaluation of LLM-based Agents | 2025/2026 | https://arxiv.org/abs/2503.16416 |
| LangChain-2025 | LangChain | State of Agent Engineering | 2025 | https://www.langchain.com/state-of-agent-engineering |
| ToolLearning-2024 | Qiancheng Xu et al. | Tool Learning with Large Language Models: A Survey | 2024 | https://arxiv.org/abs/2405.17935 |
| ParentPaper | Arbuzov, Shvets, Beir | Beyond Exponential Decay: Rethinking Error Accumulation in LLMs | 2025 | https://arxiv.org/abs/2505.24187 |
| EfficientAgents | (per efficient-agents.github.io) | Toward Efficient Agents: Memory, Tool Learning, Planning Survey | 2024+ | https://efficient-agents.github.io |
