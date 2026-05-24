# Substrate 5: Orchestration & Agent Swarms
## Evidence Harvest for Paper 3 — LLM Reliability Trilogy

**Compiled:** July 2025  
**Scope:** 17 systems surveyed; peer-reviewed papers, official product docs, and major open-source repos

---

## Quick Reference: Scored Summary Table

| System | Orchestration Pattern | Specialization | Feedback/Adaptation | Eval Integration | Maturity | Patch-Plasticity Score |
|---|---|---|---|---|---|---|
| AutoGen / MagenticOne | Dual-loop hierarchical + group-chat | Per-agent prompt + tools | Progress Ledger re-planning | AutoGenBench | Research → GA | **3/5** |
| CrewAI | Flow-first sequential + conditional branching | Role/goal/tools per agent | Task Guardrails (output validation) | Tracing + Enterprise | Production GA | **3/5** |
| LangGraph | Graph state machine + supervisor node | Per-node tools + prompt | State-driven looping | LangSmith traces | Production GA | **3/5** |
| LlamaIndex Workflows | Event-driven async pipeline | Per-step agents | Reflection loop + HITL pause/resume | Tracing (Arize) | Production GA | **2/5** |
| MetaGPT | Assembly-line SOP | Role-defined agents (CEO → Tester) | Intermediate result verification | HumanEval/SWE-bench | Research → toolkit | **2/5** |
| OpenAI Swarm | Handoff/triage | Per-agent instructions + tools | Error recovery only | Bring-your-own evals | Educational/deprecated | **1/5** |
| OpenAI AgentKit | Visual canvas + multi-agent workflow | Role-typed agents | RFT + automated prompt optimization | Built-in Evals + trace grading | Beta → GA | **4/5** |
| Microsoft Semantic Kernel | Five patterns (sequential, concurrent, handoff, group-chat, Magentic) | Per-agent skills | Not yet (prerelease) | External integration | Prerelease | **2/5** |
| AWS Bedrock Multi-Agent | Hierarchical supervisor | Domain-specialist sub-agents | None documented | GuardRails | Production GA | **2/5** |
| Vertex AI Agent Builder (ADK + A2A) | A2A protocol + ADK deterministic controls | Specialized sub-agents + grounding tools | Fine-tuning on real usage + simulation env | Built-in eval tools + Example Store | Production GA | **4/5** |
| ChatDev | Chat-chain (waterfall → cyclic) | Software company roles | Communicative dehallucination | ProgramDev / HumanEval | Research | **2/5** |
| CAMEL | Inception-prompted role-play | Role-assigned pairs | None explicitly | NeurIPS eval suite | Research | **1/5** |
| AgentVerse | Dynamic composition recruitment | Group-dynamic role assignment | Social behavior mitigation strategies | Custom experiments | Research | **2/5** |
| OpenHands / CodeAct | Event-stream delegation | Generalist + specialist micro-agents | Self-debugging + HITL interruption | 15 benchmarks (SWE-Bench etc.) | Research → open-source prod | **3/5** |
| Pydantic AI | 5-level delegation + graph state machine | Typed deps + per-agent tools | Logfire tracing (manual) | OpenTelemetry | GA (Python/TS) | **2/5** |
| Letta | Stateful memory + dream-agent background | Identity + skill per agent | Continual learning in token space | Context-Bench | Early prod | **3/5** |
| Inspect AI (UK AISI) | Solver pipeline + handoff + subagent delegation | ReAct / Deep / SWE / custom | Eval scores drive external iteration | Native evaluation framework | Research + evals prod | **2/5** |
| Multi-Agent Evolve (MAE) | Triplet co-evolution (Proposer-Solver-Judge) | Role specialization via RL | RL policy update per round | Automated Judge + RL signal | Research | **5/5** |
| Memento-Skills | Router + skill rewrite orchestration | Skill-library specialization | Read-Write Reflective Learning + unit-test gate | Automated unit tests + GAIA/HLE | Research (2026) | **5/5** |

*Score rubric: 0 = static pipeline, 1 = modular only, 2 = human-in-loop adaptation, 3 = automated retry/rerouting, 4 = eval-driven routing update, 5 = orchestrator updates agent population or routing policy from residual errors.*

---

## Per-System Entries

### 1. AutoGen / MagenticOne
**Citation:** Wu et al., arXiv:2308.08155 ([AutoGen paper](https://arxiv.org/abs/2308.08155)); MagenticOne: [Microsoft Research](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/)

**Orchestration pattern:** Dual-loop hierarchical. MagenticOne extends AutoGen with an Orchestrator agent that runs an *outer loop* (Task Ledger: fact-gathering, plan creation) and an *inner loop* (Progress Ledger: subtask assignment, self-reflection, and corrective re-planning if progress stalls). AutoGen itself supports arbitrary conversation topologies: two-agent, group chat, nested chat, and custom "ConversableAgent" graphs.

**Specialization mechanism:** Per-agent system prompt + toolset. MagenticOne's five agents are: Orchestrator (planner), WebSurfer (browser + accessibility-tree prompting), FileSurfer (file reader), Coder (code generation), and ComputerTerminal (shell executor). Each carries a different instruction set and tool registry.

**Feedback / adaptation:** The Progress Ledger loop is the key feedback mechanism — if no progress after N steps, the Orchestrator returns to the outer Task Ledger loop, revises the plan, and re-routes work. This is *reactive rerouting* but does not update agent prompts or population; the agent definitions are static across a run.

**Eval integration:** AutoGenBench (standalone open-source benchmarking tool released with MagenticOne). Tested on GAIA, AssistantBench, WebArena — achieves statistically comparable performance to SOTA on GAIA and AssistantBench ([source](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/)).

**Production maturity:** AutoGen has 20k+ GitHub stars and active enterprise deployments. AutoGen Studio (low-code UI) is generally available. Microsoft Research ships MagenticOne as a reference implementation.

**Patch-plasticity score: 3/5** — Automated rerouting via ledger loops; no update to agent definitions from outcome signals.

---

### 2. CrewAI
**Citation:** Official docs: [docs.crewai.com/en/concepts/production-architecture](https://docs.crewai.com/en/concepts/production-architecture)

**Orchestration pattern:** *Flow-first* production architecture. A `Flow` class defines entry points (`@start()`), listens to method completions (`@listen()`), and chains Crews (sets of agents) as units of work. Supports loops, conditionals, branching, async execution (`kickoff_async`), and state persistence (`@persist`).

**Specialization mechanism:** Each Agent in a Crew is defined with a `role`, `goal`, `backstory`, and a list of `tools`. Agents are goal-oriented and task-focused (e.g., "Research a topic," "Write a blog post"). Memory and Knowledge modules provide retrieval context per agent.

**Feedback / adaptation:** Task Guardrails validate task outputs before acceptance — if output fails a condition (e.g., `len(result.raw) < 100`), a corrective instruction is sent back to trigger revision. `LLM Hooks` (`@before_llm_call`) allow inspection and modification of messages. Flow state is updated by mapping Crew outputs into typed Pydantic state fields. No automated update to agent definitions from aggregate error signals.

**Eval integration:** CrewAI Tracing provides observability (login via `crewai login`). CrewAI Enterprise manages deployment, authentication, and monitoring. No native eval-score-to-routing-update loop.

**Production maturity:** Production GA. CrewAI Enterprise deploys via `crewai deploy create`. Stacks with async execution, state persistence, and flow forking are documented for production use.

**Patch-plasticity score: 3/5** — Automated output validation loops; no population-level adaptation from task outcomes.

---

### 3. LangGraph
**Citation:** [LangChain LangGraph docs](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/); [LangGraph 1.0 blog](https://www.langchain.com/blog/langchain-langgraph-1dot0)

**Orchestration pattern:** *Graph-based state machine* with supervisor node. The supervisor is an LLM-based router (`llm.with_structured_output(Router)`) that returns the next worker to invoke or "FINISH." Hierarchical teams are built as nested subgraphs where mid-level supervisors manage their own worker teams, all reporting back to a top-level supervisor.

**Specialization mechanism:** Each graph node is a distinct agent with its own LLM prompt and tool list. Example specializations include: search_node (TavilySearch), web_scraper_node (WebBaseLoader), doc_writing_node (write/edit/read document tools), chart_generating_node (PythonREPL).

**Feedback / adaptation:** Worker nodes return `Command(goto="supervisor")` on completion, feeding results back to the supervisor for next-step routing. The supervisor can re-route to the same agent or loop. State accumulates across the graph run via `MessagesState`. No automatic update to supervisor routing policy from cumulative error signals.

**Eval integration:** LangSmith tracing; LangGraph integrates with LangSmith for full trace observability. [LangChain State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) (Dec 2025, n=1,340): 57% of organizations have agents in production; 62% use detailed multi-step tracing; LangChain/LangGraph is the most-used third-party framework at 25% ([MAP study](https://arxiv.org/html/2512.04123v1)).

**Production maturity:** Production GA since LangGraph 1.0. Deployed widely: customer service, internal workflow automation, research/data analysis are top use cases.

**Patch-plasticity score: 3/5** — Automated rerouting via supervisor node; no routing-policy update from accumulated failures.

---

### 4. LlamaIndex Workflows
**Citation:** [llamaindex.ai/workflows](https://www.llamaindex.ai/workflows); [developers.llamaindex.ai — multi-agent](https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/)

**Orchestration pattern:** *Event-driven async pipeline.* Workflows 1.0 (released June 30, 2025) provide multi-step orchestration with event triggers, parallel paths, loops, and stateful pause/resume. Combines multiple agents within a single workflow.

**Specialization mechanism:** Per-step agents with distinct roles (Text-to-SQL agent, RAG pipeline agent, structured extraction agent). LlamaIndex provides state and memory primitives; Workflows provide orchestration to chain them.

**Feedback / adaptation:** *Reflection Workflow* for structured outputs provides iterative refinement. Human-in-the-loop (HITL) patterns allow workflow pause for human review then resume. No automated routing update from failure signals.

**Eval integration:** Integrates with Arize Phoenix for tracing. Salesforce Agentforce partnership. No built-in eval-to-routing loop.

**Production maturity:** Production GA. 25M+ package downloads/month, 1.5k+ contributors, 20k+ community members.

**Patch-plasticity score: 2/5** — Reflection loop is manual/HITL; no automated failure-driven routing adaptation.

---

### 5. MetaGPT
**Citation:** Hong et al., arXiv:2308.00352 ([MetaGPT paper](https://arxiv.org/abs/2308.00352)); ICLR 2024 oral.

**Orchestration pattern:** *Assembly-line paradigm* modeled as a software company. Standardized Operating Procedures (SOPs) are encoded into prompt sequences that define the ordered handoff chain: Product Manager → Architect → Project Manager → Engineer → QA Engineer.

**Specialization mechanism:** Role-defined agents with human-like domain expertise. Each role maps to a distinct system prompt encoding its responsibilities. Agents verify intermediate artifacts before passing to the next role (design documents, code modules, test cases).

**Feedback / adaptation:** Intermediate result verification reduces cascading hallucinations — each role checks the prior role's output and can flag inconsistencies. However, the SOP chain is fixed; no dynamic rerouting or role population update occurs based on runtime errors. MetaGPT 2.0 (FoundationAgents) extends with meta-programming capabilities for more flexible role instantiation.

**Eval integration:** Evaluated on HumanEval and SWE-bench; cited in [Cemri et al. (2025)](https://arxiv.org/html/2503.13657v1) as a baseline. ChatDev's specialized topology (cyclic graph + refined role prompts) showed +15.6% improvement over baseline on ProgramDev benchmark.

**Production maturity:** Research toolkit with GitHub repo; not a commercial product. Used extensively as academic baseline.

**Patch-plasticity score: 2/5** — Intermediate verification provides within-run feedback but no population-level update.

---

### 6. OpenAI Swarm (deprecated → Agents SDK)
**Citation:** [GitHub openai/swarm](https://github.com/openai/swarm)

**Orchestration pattern:** *Handoff / triage pattern.* A triage agent receives a request, determines the appropriate specialized agent, and hands off via a Python function that returns an `Agent` object. The `client.run` loop: get completion → execute tool calls → switch agent if handoff triggered → update context variables → terminate if no new tool calls.

**Specialization mechanism:** Per-agent `instructions` (string or callable) + per-agent `functions` list. Example specializations: Triage Agent, Sales Agent, Refunds Agent (airline demo), Weather Agent, Support Bot.

**Feedback / adaptation:** Error recovery: if a tool call fails, an error response is appended to context for the agent to recover. No automated routing update. Swarm is *stateless between calls*.

**Eval integration:** "Bring your own eval suite" — reference evals in `airline/`, `weather_agent/`, `triage_agent/` directories. No built-in eval infrastructure.

**Production maturity:** Explicitly deprecated. Replaced by the [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents) for production use. Still has 20.6k GitHub stars as an educational reference.

**Patch-plasticity score: 1/5** — Modular handoffs; no adaptation mechanism of any kind.

---

### 7. OpenAI AgentKit (Agent Builder + ChatKit + Connector Registry)
**Citation:** [openai.com/index/introducing-agentkit](https://openai.com/index/introducing-agentkit/) (released Oct 2025)

**Orchestration pattern:** *Visual canvas multi-agent workflow.* Agent Builder provides drag-and-drop node composition, templates, versioning, and inline eval configuration. Supports complex multi-agent workflows with custom guardrails.

**Specialization mechanism:** Role-typed agents (support, sales, buyer, research, deep-research, knowledge assistant, onboarding guide). Connector Registry manages shared tool/data connections. Reinforcement Fine-Tuning (RFT) trains agents to call specific tools at optimal times.

**Feedback / adaptation:** This is the most evolved closed-platform feedback loop documented:  
  1. **Trace grading** — end-to-end assessment of agentic workflows with automated grading to identify shortcomings  
  2. **Automated prompt optimization** — generates improved prompts based on grader outputs and human annotations  
  3. **RFT (Reinforcement Fine-Tuning)** — available for o4-mini (GA) and GPT-5 (private beta), using custom tool-call training and custom graders  
  This constitutes a near-full feedback loop from agent outcomes to agent definition updates.

**Eval integration:** Built-in Evals platform; datasets from scratch + automated graders + human annotations; third-party model evaluation support. Ramp: "slashing iteration cycles by 70%"; Carlyle: "agent accuracy increased by 30%" ([source](https://openai.com/index/introducing-agentkit/)).

**Production maturity:** ChatKit GA; new Evals GA; Agent Builder beta; Connector Registry beta rollout. Klarna: handles 2/3 of all support tickets. Clay: 10x growth with sales agent.

**Patch-plasticity score: 4/5** — RFT closes the loop from task outcomes to agent weights; automated prompt optimization updates routing policy. Missing the 5/5 criterion of fully automated agent *population* update (adding/retiring agents based on residual error clusters).

---

### 8. Microsoft Semantic Kernel Multi-Agent
**Citation:** [learn.microsoft.com — Semantic Kernel Agent Orchestration](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/) (updated July 2025)

**Orchestration pattern:** Five named patterns:  
  1. **Sequential** — ordered pipeline  
  2. **Concurrent** — broadcast to all agents, independent results  
  3. **Handoff** — dynamic control transfer based on context/rules  
  4. **Group Chat** — all agents in conversation with group manager  
  5. **Magentic** — MagenticOne-inspired generalist multi-agent collaboration

**Specialization mechanism:** Agents with specialized skills or roles; generalists in Magentic pattern. Unified interface (`InvokeAsync`) abstracts pattern differences.

**Feedback / adaptation:** No explicit feedback loops documented in current release. The Magentic pattern inherits MagenticOne's ledger-based re-planning.

**Eval integration:** External; no built-in eval infrastructure documented.

**Production maturity:** Prerelease (NuGet packages marked `--prerelease`). C# and Python supported; Java not yet available. Last updated July 2025.

**Patch-plasticity score: 2/5** — Multiple patterns available; adaptation is human-driven or inherited from MagenticOne.

---

### 9. AWS Bedrock Agents — Multi-Agent Collaboration
**Citation:** [AWS Bedrock multi-agent docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html); [AWS blog](https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/)

**Orchestration pattern:** *Hierarchical supervisor.* A designated Bedrock Agent (supervisor) automatically creates and executes plans across collaborator (sub-)agents. The supervisor routes requests based on natural-language domain instructions — example: mortgage routing to Existing Mortgage Agent, New Mortgage Agent, or General Agent.

**Specialization mechanism:** Domain-specialist sub-agents, each optimized for a specific use case. Every agent has access to full Bedrock features: tools, action groups, knowledge bases, guardrails.

**Feedback / adaptation:** No feedback mechanisms documented. The routing logic is static (defined at configuration time via natural-language instructions). Scalability: additional collaborators can be added as the system matures.

**Eval integration:** AWS Bedrock Guardrails for safety; no built-in eval-to-routing-update loop.

**Production maturity:** Production GA. Fully managed; scales natively within AWS infrastructure.

**Patch-plasticity score: 2/5** — Hierarchical routing; domain specialists; no adaptation from outcomes.

---

### 10. Vertex AI Agent Builder (ADK + A2A + Agent Engine)
**Citation:** [cloud.google.com — Build and manage multi-system agents](https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai) (April 2025)

**Orchestration pattern:** *A2A Protocol + ADK deterministic controls.* Agent2Agent (A2A) is an open protocol enabling agents built on different frameworks (ADK, LangGraph, CrewAI) or vendors to communicate, publish capabilities, and negotiate interactions (text, forms, bidirectional audio/video). Agent Engine provides the managed runtime.

**Specialization mechanism:** Specialized sub-agents with grounding tools (Google Search, Google Maps with 100M daily updates, enterprise data providers: D&B, S&P Global, Cotality). Real production examples: video analysis agents (Nippon TV), infrastructure planning agents for EV charger siting (Renault), pricing AI agents (Revionics).

**Feedback / adaptation:** Built-in comprehensive evaluation tools; Example Store to improve agent performance; model fine-tuning on real-world usage data; upcoming simulation environment with diverse user personas. A2A allows dynamic capability negotiation between agents — closest to a *runtime* feedback loop at the orchestration layer.

**Eval integration:** Full evaluation stack: tracing (agent reasoning, tool selection, execution paths), example store, fine-tuning, simulation environment. Nippon TV: saved one month of development time using Agent Engine.

**Production maturity:** Production GA. 200+ models via Model Garden; 100+ pre-built connectors; 800K+ APIs via Apigee; 50+ industry partners on A2A protocol.

**Patch-plasticity score: 4/5** — Eval-driven fine-tuning closes the loop from agent outcomes to model updates; A2A capability negotiation enables runtime routing adaptation. Full 5/5 would require automated agent-population restructuring from residual error signals.

---

### 11. ChatDev
**Citation:** Qian et al., arXiv:2307.07924 ([ChatDev paper](https://arxiv.org/abs/2307.07924)); ACL 2024.

**Orchestration pattern:** *Chat-chain* — a directed communication graph across software development phases. Originally a DAG (waterfall); modified in Cemri et al. (2025) interventions to a *cyclic graph* enabling iterative refinement until the CTO confirms requirements are met.

**Specialization mechanism:** Software company roles: CEO (requirements), CTO (architecture), Programmer (implementation), Reviewer (code review), Software Test Engineer (testing). Each role has a distinct system prompt enforcing its responsibilities.

**Feedback / adaptation:** *Communicative dehallucination* — agents challenge each other's outputs during multi-turn dialogues. In the cyclic-graph topology, the loop continues until quality criteria pass. Evidence from [Cemri et al. 2025](https://arxiv.org/html/2503.13657v1): cyclic topology + improved prompts achieved +15.6% on ProgramDev (25.0% → 40.6%) and +1.9% on HumanEval (89.6% → 91.5%).

**Eval integration:** ProgramDev benchmark; HumanEval; evaluated in the "Why Do Multi-Agent LLM Systems Fail?" systematic study (arXiv:2503.13657).

**Production maturity:** Research prototype. Open-source (GitHub: OpenBMB/ChatDev).

**Patch-plasticity score: 2/5** — Cyclic feedback loop within a run; no cross-run adaptation of role definitions.

---

### 12. CAMEL (Communicative Agents for Mind Exploration)
**Citation:** Li et al., arXiv:2303.17760 ([CAMEL paper](https://arxiv.org/abs/2303.17760)); NeurIPS 2023.

**Orchestration pattern:** *Role-playing dyad.* An AI User agent instructs an AI Assistant agent toward task completion, guided by *inception prompting* that assigns roles and maintains consistency with human intentions throughout a multi-turn conversation.

**Specialization mechanism:** Role assignment via inception prompt (e.g., "Python programmer" + "stock trader"); the roles condition all subsequent turns. The CAMEL framework has since expanded to support multi-role societies.

**Feedback / adaptation:** No explicit feedback mechanism described in the founding paper. Role assignments are fixed at task initialization. The `camel-ai` library (now an active framework) adds tool integration, knowledge graphs, and multi-agent societies, but the core architecture remains role-play without automated adaptation.

**Eval integration:** AI Society dataset (conversational data from role-playing pairs); used as a research resource rather than a live evaluation loop.

**Production maturity:** Research origin; camel-ai.org now maintains an active open-source framework with societies, tools, and memory modules.

**Patch-plasticity score: 1/5** — Fixed role assignment; no adaptation.

---

### 13. AgentVerse
**Citation:** Chen et al., arXiv:2308.10848 ([AgentVerse paper](https://arxiv.org/abs/2308.10848))

**Orchestration pattern:** *Dynamic group composition.* AgentVerse dynamically adjusts the composition of the agent group during collaborative task accomplishment, inspired by human group dynamics.

**Specialization mechanism:** Agents are recruited and assigned roles based on task requirements. The framework explores *emergent social behaviors* (positive and negative) and proposes strategies to leverage or mitigate them.

**Feedback / adaptation:** Dynamic composition is the closest thing to adaptation — the agent population can be restructured during task execution. The paper discusses strategies to promote positive emergent behaviors and mitigate negative ones (e.g., conformity, free-riding), suggesting a feedback-sensitive population adjustment mechanism. Multi-agent groups outperform single agents in experiments.

**Eval integration:** Custom experiments demonstrating multi-agent outperformance vs. single agent across a broad spectrum of tasks.

**Production maturity:** Research (GitHub: OpenBMB/AgentVerse).

**Patch-plasticity score: 2/5** — Dynamic composition is partially adaptive, but lacks a systematic error-signal-driven population update.

---

### 14. OpenHands / CodeAct
**Citation:** Wang et al., arXiv:2407.16741 ([OpenHands paper](https://arxiv.org/abs/2407.16741)); [openhands.dev](https://openhands.dev)

**Orchestration pattern:** *Event-stream delegation.* An event stream records all actions and observations chronologically. The primary agent (CodeActAgent) uses `AgentDelegateAction` to hand off subtasks to specialist agents. Patterns: generalist-to-specialist delegation, graph-based collaboration (GPTSwarm), and subtask hand-off.

**Specialization mechanism:** AgentHub hosts multiple agent types: CodeActAgent (default, code-execution generalist), BrowsingAgent (web specialist with BrowserGym DSL), CodeActSWEAgent (SWE-bench specialist with in-context demonstrations), Micro Agents (task-specific variants using specialized prompts).

**Feedback / adaptation:** Multi-layer: (1) *Self-debugging* — agents execute code and receive execution feedback (logs, errors) to iteratively correct; (2) *HITL interruption* — users interrupt via GUI for real-time course correction; (3) *Integration testing* framework for prompt regression testing. GPTSwarm agents have *optimizable graph edges* (collaboration pathway optimization).

**Eval integration:** 15 evaluation benchmarks including SWE-Bench Lite, HumanEvalFix, BIRD (SQL), BioCoder, ML-Bench. Most comprehensive benchmark suite of any system reviewed.

**Production maturity:** Open-source production; active community; benchmarked against SWE-bench leaderboard.

**Patch-plasticity score: 3/5** — Self-debugging feedback loops; GPTSwarm graph optimization is a partial path to 4/5.

---

### 15. Pydantic AI Multi-Agent
**Citation:** [pydantic.dev/docs/ai/guides/multi-agent-applications](https://pydantic.dev/docs/ai/guides/multi-agent-applications/)

**Orchestration pattern:** Five-level complexity ladder: (1) single agent, (2) agent delegation via tools, (3) programmatic hand-off, (4) graph-based state machine, (5) Deep Agents (autonomous planning + file ops + delegation + sandboxed code).

**Specialization mechanism:** Per-agent typed dependency injection (`deps_type` dataclass with clients/keys) + per-agent tool registry. Dependency sharing requirements between parent and delegate agents are enforced by the type system.

**Feedback / adaptation:** *Logfire* tracing (built on OpenTelemetry) provides observability: delegation decisions, end-to-end latency per agent, token costs. Human-in-the-loop approval workflows for dangerous operations. No automated routing update from outcome signals.

**Eval integration:** External (via Logfire / OTel backends). No built-in eval framework.

**Production maturity:** GA (Python + TypeScript/JavaScript). Used in production by teams building typed, structured agent workflows.

**Patch-plasticity score: 2/5** — Typed delegation with observability; adaptation is human-mediated.

---

### 16. Letta (formerly MemGPT)
**Citation:** [letta.com](https://www.letta.com); originating research: MemGPT, UC Berkeley Sky Computing Lab

**Orchestration pattern:** *Stateful memory-first* architecture. Primary agents are augmented by *background memory agents* ("dream agents") that run during idle time to transform the primary agent's context, prompts, and skills. Sleep-time compute shifts reasoning to between-session periods.

**Specialization mechanism:** Per-agent identity and expertise; agents maintain persistent memory across sessions. Git-based memory for coding agents provides versioned context. Memory is portable across LLM providers.

**Feedback / adaptation:** *Continual learning in token space* — agents learn from experience over time, not just within a session. Dream agents actively mutate the primary agent's skill representation. Context-Bench evaluates long-horizon memory chaining. This is the closest among production-adjacent systems to a genuine *agent self-improvement* loop outside of pure research.

**Eval integration:** Context-Bench (internal benchmark for long-horizon information management).

**Production maturity:** Early production. Letta Code environment for coding agents; SDK + CLI + agent teleportation across machines.

**Patch-plasticity score: 3/5** — Continual learning via dream agents constitutes cross-session adaptation; limited evidence of systematic error-cluster-driven population restructuring.

---

### 17. Inspect AI (UK AISI)
**Citation:** [inspect.aisi.org.uk](https://inspect.aisi.org.uk); [inspect.aisi.org.uk/agents.html](https://inspect.aisi.org.uk/agents.html)

**Orchestration pattern:** *Evaluation-driven solver pipeline.* Agents are solvers in Inspect's evaluation framework. Supported roles: top-level solver, standalone step in workflow, delegation target (subagent), or standard tool (via `as_tool()`). Routing via `handoff()` (full history transfer) or `as_tool()` (string-in/string-out).

**Specialization mechanism:** Built-in agent types: ReAct (general), Deep Agent (long-horizon with subagent delegation, memory, planning), SWE agents (Claude Code, Codex CLI integration), Custom agents (user-defined), Agent Bridge (integration of LangChain, OpenAI Agents SDK, Pydantic AI). Human Agent for baseline comparison.

**Feedback / adaptation:** The `generate_loop()` function runs the model until tool calls stop — this is an automated retry loop. However, the *evaluation results* do not automatically update the agent routing policy; they are consumed by researchers externally. The eval framework is used to benchmark, not to close a feedback loop within deployment.

**Eval integration:** Native evaluation is the *primary purpose* of Inspect AI, not a secondary feature. Token, message, and time limits enforced per agent. Maintained by UK AISI for safety-critical LLM evaluation.

**Production maturity:** Production for evaluation use cases; used by UK government for AI safety assessments. Open-source (GitHub: UKGovernmentBEIS/inspect_ai).

**Patch-plasticity score: 2/5** — Best eval infrastructure of any system reviewed, but eval results feed into human decision-making rather than automated agent population updates.

---

### 18. Multi-Agent Evolve (MAE) — Automated 5/5 Case
**Citation:** Chen et al., arXiv:2510.23595 ([MAE paper](https://arxiv.org/abs/2510.23595)); submitted October 2025

**Orchestration pattern:** *Triplet co-evolution.* Three agents instantiated from a single LLM: (1) Proposer (generates questions), (2) Solver (attempts solutions), (3) Judge (evaluates both Proposer and Solver). All three are simultaneously optimized via Self-Play Reinforcement Learning.

**Specialization mechanism:** Role specialization emerges from RL optimization rather than fixed system prompts. The Judge's evaluations drive the training signal for both other roles.

**Feedback / adaptation:** This is the *automated 5/5 case*: RL policy updates modify all three agent behaviors based on each round's outcomes. The agent "population" (roles and their behavioral policies) updates from residual error signals. Works without human-annotated data or grounded environments. Average 4.54% improvement on multiple benchmarks with Qwen2.5-3B-Instruct.

**Eval integration:** The Judge agent is the built-in evaluator; RL signal = evaluation signal. Tested on math, reasoning, and general knowledge Q&A benchmarks.

**Production maturity:** Research (Oct 2025 submission). No production deployment documented.

**Patch-plasticity score: 5/5** — The orchestration *is* the feedback loop; agent population and routing policies update from residual errors via RL.

---

### 19. Memento-Skills — Automated Skill Promotion (5/5 Case)
**Citation:** Dickson, VentureBeat, April 2026 ([article](https://venturebeat.com/orchestration/new-framework-lets-ai-agents-rewrite-their-own-skills-without-retraining-the))

**Orchestration pattern:** *Skill-router + rewrite orchestrator.* A specialized skill router selects the most behaviorally relevant skill based on execution utility (not just semantic similarity). An orchestrator evaluates execution traces and directs skill mutation.

**Specialization mechanism:** Skills stored as structured markdown files (declarative spec + specialized prompts + executable code). Skill library grows from 5 seed skills to 41 (GAIA) or 235 (HLE) distinct skills autonomously.

**Feedback / adaptation:** *Read-Write Reflective Learning* — if execution fails, the system actively mutates its memory: updating code artifacts, rewriting prompts to patch specific failure modes, or creating entirely new skills. The skill router is updated via one-step offline RL from execution feedback. An automatic unit-test gate prevents regression: synthetic test generation → execution → library update only if test passes.

**Eval integration:** Automated unit tests as promotion gate. GAIA: 66.0% vs. 52.3% baseline (+13.7pp). HLE: 38.7% vs. 17.9% (+20.8pp). Retrieval: 80% task success (specialized router) vs. 50% (BM25) ([source](https://venturebeat.com/orchestration/new-framework-lets-ai-agents-rewrite-their-own-skills-without-retraining-the)).

**Production maturity:** Research (April 2026). Code released on GitHub; not yet production-deployed.

**Patch-plasticity score: 5/5** — The orchestration layer rewrites agent skill definitions from residual errors and promotes new skills through automated testing.

---

## Special Evidence: Specialized Agents vs. Monolithic Systems

### Direct Evidence (Paper-2 → Paper-3 Bridge)

The systematic study "Why Do Multi-Agent LLM Systems Fail?" ([Cemri et al., arXiv:2503.13657](https://arxiv.org/html/2503.13657v1)) provides the clearest empirical bridge:

**AG2 (AutoGen) — MathChat:**  
Baseline (Student + Assistant dyad) → Specialized topology (Problem Solver + Coder + Verifier):
- GPT-4o: 84.25% → 88.83% on GSM-Plus (p=0.03, statistically significant)
- The text explicitly states: "a modular approach using simple, well-defined agents, rather than complex, multitasked ones, **enhances performance and simplifies debugging**"

**ChatDev — ProgramDev:**  
Baseline (DAG topology) → Cyclic topology + improved role prompts:
- 25.0% → 40.6% (+15.6% absolute, +62.4% relative)
- The cyclic graph enables iterative refinement until the CTO confirms requirements; the DAG cuts the feedback loop prematurely.

**AppWorld:**  
Monolithic supervisor vs. service-specific specialist agents (Spotify Agent, Phone Agent, Gmail Agent):  
- Domain specialization is the key architectural choice distinguishing AppWorld's approach.

**Parallel-Roles Architecture** (Tran & Kiela, arXiv:2604.02460):  
At 100-token budget on FRAMES, Parallel-Roles (Solver + Second Solver + Fact Extractor + Skeptic) outperforms single-agent:
- DeepSeek-R1-70B: 0.427 vs. 0.365 (+16.7%)
- Gemini-2.5-Pro: 0.654 vs. 0.368 (+77.7% at 100-token budget)

**Key nuance:** Under *unconstrained token budgets*, single agents often match multi-agent systems (Tran & Kiela, 2025). The specialization advantage is most pronounced at *tight compute budgets* and in *context degradation regimes* — precisely the conditions where a monolithic agent's attention spreads too thin across a complex domain.

**Failure-cluster → specialist mapping:** The AppWorld and HyperAgent examples show that creating agents aligned to *failure domains* (Spotify API failures, navigation failures, code execution failures) is more tractable than engineering a single agent robust to all failure modes. This is the Paper-2 → Paper-3 bridge: failure clusters identified in Paper 2 (reliability analysis of monolithic agents) motivate the specialist routing topology of Substrate 5.

---

## Special Evidence: Automated Skill/Agent Promotion (5/5 Cases)

Only three systems reviewed achieve the 5/5 patch-plasticity criterion of automated agent/skill promotion:

| System | Promotion Mechanism | Gate | Evidence |
|---|---|---|---|
| **Memento-Skills** (2026) | Read-Write Reflective Learning; skill rewrite + new skill creation from failed executions | Automated unit-test gate before library update | GAIA +13.7pp; HLE +20.8pp; 5→235 skills autonomously |
| **Multi-Agent Evolve / MAE** (2025) | RL policy update for Proposer, Solver, and Judge roles from co-evolutionary feedback | RL reward signal from Judge agent | +4.54% avg across benchmarks |
| **OpenAI AgentKit (partial)** (2025) | Reinforcement Fine-Tuning (RFT) + automated prompt optimization from trace grading | Custom graders + human annotation | Carlyle +30% agent accuracy; Ramp -70% iteration cycles |

AgentKit scores 4/5 rather than 5/5 because the RFT process requires human-designed graders and does not autonomously restructure the *population* of agents (add/retire specialists) — it updates model weights and prompts within a fixed agent topology.

---

## Industry Adoption Data (2025–2026)

| Metric | Value | Source |
|---|---|---|
| Organizations with AI agents in production | 57.3% | [LangChain State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering), Dec 2025, n=1,340 |
| Large enterprises (10k+ employees) with agents in production | 67% | Ibid. |
| Companies using AI agents (any form) | 79% | [PwC AI Agent Survey](https://prefactor.tech/learn/ai-agent-adoption-statistics), Jun 2025 |
| Organizations scaling AI agents in ≥1 function | 23% | McKinsey State of AI, Nov 2025 |
| Enterprise apps embedding task-specific agents by 2026 | 40% (from <5% in 2025) | Gartner, Aug 2025 |
| Agentic AI project cancellations projected by 2027 | >40% | Gartner, Jun 2025 |
| Production teams using LangChain/LangGraph | 25% of framework users | MAP Study ([arXiv:2512.04123](https://arxiv.org/html/2512.04123v1)), n=306 practitioners |
| Production teams using CrewAI | 10.7% of framework users | Ibid. |
| Production teams building in-house (no third-party framework) | 85% of case study orgs | Ibid. |
| Enterprises rebuilding agent stack every 3 months | 70% (regulated), 41% (unregulated) | [Cleanlab AI Agents in Production 2025](https://cleanlab.ai/ai-agents-in-production-2025/), Aug 2025, n=95 |
| Teams satisfied with observability/guardrails | <33% | Ibid. |
| Enterprises planning to add oversight features | 42% (regulated) | Ibid. |
| Devin enterprise usage growth | ~8x in 6 months | [Cognition blog](https://cognition.ai/blog/multi-agents-working), Apr 2026 |

---

## Are Agent Swarms Patch-Plastic or Just Modular?

The evidence above reveals a sharp distinction that most orchestration marketing obscures. **Modularity** — dividing a task among specialized agents with fixed responsibilities — is the baseline property of every system reviewed. All seventeen frameworks achieve modularity. A modular system routes work to the right specialist, but that routing policy is determined at design time and does not change when the system encounters novel failure modes. In the reliability framing of this trilogy, a modular swarm is a *static patch*: it covers known failure domains more efficiently than a monolithic agent, but its coverage is bounded by the designer's foresight.

**Patch-plasticity** is the orthogonal property: does the orchestration layer observe residual errors — failures that fall between or exceed the current specialists — and *update the agent population or routing policy* in response? The evidence shows this is rare. Of the nineteen systems reviewed, only two (Multi-Agent Evolve and Memento-Skills) fully automate the loop from residual error signals to agent definition updates, and both are 2025–2026 research prototypes. OpenAI AgentKit approaches this with Reinforcement Fine-Tuning from trace grading (4/5), and Letta's dream agents provide cross-session skill mutation (3/5). Every other production system — LangGraph, CrewAI, AWS Bedrock, Vertex AI Agent Builder, Semantic Kernel — operates as a sophisticated static router: well-engineered and scalable, but structurally unable to cover failure clusters that emerge in deployment without human re-engineering.

The policy implication for Paper 3 is direct: multi-agent orchestration is a necessary but not sufficient condition for reliability improvement. A three-tier reliability architecture would combine (a) modular specialization for known failure clusters (the 3/5 systems), (b) eval-driven routing updates that adjust traffic between existing specialists based on performance signals (the 4/5 systems), and (c) automated skill promotion that creates new specialists when residual error rates exceed a threshold (the 5/5 systems, currently research-only). The gap between tiers (b) and (c) is the frontier of the field in 2025: organizations can measure residual errors at tier (b), but the automated loop that converts those measurements into new agent definitions — without human engineering intervention — remains the domain of research prototypes, not production deployments.

---

## Source Index

1. Wu et al. (2023). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. arXiv:2308.08155. https://arxiv.org/abs/2308.08155
2. Hong et al. (2023). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. arXiv:2308.00352. https://arxiv.org/abs/2308.00352
3. Qian et al. (2023). ChatDev: Communicative Agents for Software Development. arXiv:2307.07924. https://arxiv.org/abs/2307.07924
4. Li et al. (2023). CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society. arXiv:2303.17760. https://arxiv.org/abs/2303.17760
5. Chen et al. (2023). AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors. arXiv:2308.10848. https://arxiv.org/abs/2308.10848
6. Wang et al. (2024). OpenHands: An Open Platform for AI Software Developers as Generalist Agents. arXiv:2407.16741. https://arxiv.org/abs/2407.16741
7. Fourney et al. (2024). MagenticOne: A Generalist Multi-Agent System. Microsoft Research. https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/
8. Cemri et al. (2025). Why Do Multi-Agent LLM Systems Fail? arXiv:2503.13657. https://arxiv.org/html/2503.13657v1
9. Tran & Kiela (2025). Single-Agent LLMs Outperform Multi-Agent Systems on Complex Reasoning Tasks. arXiv:2604.02460. https://arxiv.org/html/2604.02460v1
10. Chen et al. (2025). Multi-Agent Evolve: LLM Self-Improve through Co-evolution. arXiv:2510.23595. https://arxiv.org/abs/2510.23595
11. Pan et al. (2025). Measuring Agents in Production. arXiv:2512.04123. https://arxiv.org/html/2512.04123v1
12. Dickson, B. (2026). New framework lets AI agents rewrite their own skills. VentureBeat. https://venturebeat.com/orchestration/new-framework-lets-ai-agents-rewrite-their-own-skills-without-retraining-the
13. CrewAI Production Architecture. https://docs.crewai.com/en/concepts/production-architecture
14. LangGraph Hierarchical Agent Teams. https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/
15. AWS Bedrock Multi-Agent Collaboration. https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
16. Semantic Kernel Agent Orchestration. https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/
17. Vertex AI Agent Builder. https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai
18. OpenAI AgentKit. https://openai.com/index/introducing-agentkit/
19. OpenAI Swarm. https://github.com/openai/swarm
20. LlamaIndex Workflows. https://www.llamaindex.ai/workflows
21. Pydantic AI Multi-Agent. https://pydantic.dev/docs/ai/guides/multi-agent-applications/
22. Letta. https://www.letta.com
23. Inspect AI. https://inspect.aisi.org.uk/agents.html
24. LangChain State of Agent Engineering (Dec 2025). https://www.langchain.com/state-of-agent-engineering
25. Cleanlab AI Agents in Production 2025 (Aug 2025). https://cleanlab.ai/ai-agents-in-production-2025/
26. AI Agent Adoption Statistics 2026. Prefactor. https://prefactor.tech/learn/ai-agent-adoption-statistics
