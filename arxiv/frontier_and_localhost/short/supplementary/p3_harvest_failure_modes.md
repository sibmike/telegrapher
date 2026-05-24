# P3 Failure-Mode Harvest: Patch-Plastic LLM Architectures
### Instructions + Skills + Memory + Tools + Orchestration + Governance

> **Purpose:** Honest-paper section for Paper 3 of the trilogy. Reviewers expect this. Organized by category A–I with severity tags and a design-principles synthesis at the bottom.  
> **Scope:** 2023–2026, prioritizing 2025–2026. 37 primary citations.  
> **Severity tags:** HIGH = directly undermines the patch-plastic thesis; MEDIUM = significant reliability hazard; LOW = real but manageable with known mitigations.

---

## A. SCAFFOLD BLOAT — Rules/Skills/Memories Accumulating to Degrade Performance

### A1. Lost in the Middle — Positional Degradation
**Citation:** Liu et al., "Lost in the Middle: How Language Models Use Long Contexts," *TACL* 2024. [arXiv 2307.03172](https://arxiv.org/abs/2307.03172) / [ACL Anthology](https://aclanthology.org/2024.tacl-1.9/)

**Failure mode demonstrated:** When relevant information is placed in the middle of a long context, model performance degrades significantly relative to information at the start or end. Tested across GPT-3.5-Turbo, Claude-1.3, MPT-30B, and LongChat-13B on multi-document QA and key-value retrieval. Explicit long-context models showed the same U-shaped degradation.

**Quantitative evidence:** Increasing context length while keeping answer position constant increased latency and cost while providing only ~1% additional accuracy for Claude-1.3. The gap between best-case (beginning/end) and worst-case (middle) placement was substantial across all models.

**Relevance to patch-plastic thesis:** When rules, skills, and memories accumulate in a long system prompt, later-appended rules—likely containing the most recent governance updates—fall in the middle of the context and are disproportionately ignored.

**Mitigation proposed:** Effective re-ranking to place relevant information at context boundaries. Priority ordering of scaffold elements.

**Severity:** HIGH — directly predicts that the most recently patched rules are the most forgotten.

---

### A2. RULER Benchmark — Claimed vs. Effective Context
**Citation:** Hsieh et al., "RULER: What's the Real Context Size of Your Long-Context Language Models?" COLM 2024. [arXiv 2404.06654](https://arxiv.org/abs/2404.06654)

**Failure mode demonstrated:** 17 long-context LLMs were evaluated on 13 tasks across 4 categories. Despite advertising context sizes of 32K tokens or more, only half could maintain satisfactory performance at 32K on RULER's multi-hop tracing and aggregation tasks. Performance drops were large as context length increased, even for models that scored near-perfectly on simpler needle-in-a-haystack tests.

**Quantitative evidence:** Yi-34B (200K context claim) showed "large room for improvement" as input length and task complexity increased. At 128K context, GPT-5-mini reached 0.59 overall accuracy on RULER; open-source models fell to 0.36–0.49 with retrieval collapsing to 0 in some configurations.

**Relevance:** Scaffold architects cannot assume that a model with a 128K-token window is effectively processing all of it. The "real" effective context for instruction-following across complex scaffold elements is far smaller than the advertised limit.

**Mitigation:** Measure effective context empirically using RULER-style tasks before assuming scaffold size is safe.

**Severity:** HIGH — effective context is a hard physical ceiling on scaffold complexity.

---

### A3. BABILong — Reasoning Collapses at Scale
**Citation:** Kuratov et al., "BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack," NeurIPS 2024. [arXiv 2406.10149](https://arxiv.org/abs/2406.10149)

**Failure mode demonstrated:** Benchmark of 20 reasoning tasks requiring facts distributed across extremely long documents. Performance declined sharply with reasoning complexity at scale.

**Quantitative evidence:** "Popular LLMs effectively utilize only 10–20% of the context and their performance declines sharply with increased reasoning complexity." RAG achieved only 60% accuracy on single-fact QA, independent of context length.

**Relevance:** A scaffold with memory, rules, and skills is precisely the "facts distributed across long documents" scenario BABILong stress-tests. The finding that LLMs use at most 20% of their context implies that 80% of scaffold content is ignored under realistic conditions.

**Mitigation proposed:** Recurrent memory transformers; hierarchical retrieval. The best performance required fine-tuning specifically for long-horizon recall.

**Severity:** HIGH

---

### A4. Curse of Instructions — Multi-Rule Degradation
**Citation:** Harada et al., "Curse of Instructions: Large Language Models Cannot Follow Multiple Instructions at Once," ICLR 2025 submission. [OpenReview R6q67CDBCH](https://openreview.net/forum?id=R6q67CDBCH)

**Failure mode demonstrated:** ManyIFEval benchmark with up to 10 verifiable instructions. As instruction count rises, the ability to follow individual instructions deteriorates gradually but constantly. Success rate follows a power law: P(all instructions) ≈ P(individual)^n.

**Quantitative evidence:** GPT-4o success rate on all-10-instructions: 15%. Claude 3.5 Sonnet: 44%. After iterative self-refinement (instruction-level CoT): GPT-4o improved to 31%, Claude to 58% — still far below single-instruction performance.

**Relevance:** A production scaffold with 10+ governance rules already pushes frontier models below 50% compliance. 50+ rules is a regime studied by IFScale (see A5) where performance collapses further.

**Mitigation:** Instruction-level chain-of-thought self-refinement; prioritizing precision in feedback over recall.

**Severity:** HIGH

---

### A5. IFScale — Performance Collapse at High Instruction Density
**Citation:** Jaroslawicz et al., "How Many Instructions Can LLMs Follow at Once?" arXiv 2507.11538, July 2025. [https://arxiv.org/abs/2507.11538](https://arxiv.org/abs/2507.11538)

**Failure mode demonstrated:** IFScale benchmark: 500 keyword-inclusion instructions on a business report task. Evaluated 20 models across 7 providers. Three degradation patterns identified: threshold (sudden collapse), linear, and exponential. Universal primacy effect: models bias toward earlier instructions.

**Quantitative evidence:** Even the best frontier models achieve only 68% accuracy at 500 instructions. o4-mini latency scaled from 12.4s at 10 instructions to 436s at 250 instructions — a 35× cost increase for moderate gains. All models converge toward efficiency ratios of 0–2 at high densities.

**Mitigation proposed:** Hierarchical instruction routing; separating critical from advisory rules. Favor smaller, faster models for high-instruction-density deployments.

**Severity:** HIGH — directly quantifies scaffold bloat cost at production scale.

---

### A6. Token Snowball Effect in Scaffolded Agents
**Citation:** Fan et al. (2025), referenced in: "A Source-Code Taxonomy of Coding Agent Architectures," arXiv 2604.03515 (April 2026). [https://arxiv.org/html/2604.03515v1](https://arxiv.org/html/2604.03515v1)

**Failure mode demonstrated:** The "token snowball effect" — naive conversation history accumulation causes linear input token growth with each API call. Failing attempts consume up to 4× the resources of successful attempts.

**Quantitative evidence:** Failing attempts at 4× token cost; linear context growth; architecture study found these empirical phenomena map directly to context compaction failures.

**Mitigation:** Aggressive context pruning; compaction at mid-context; sub-agent architectures with summarized handoffs.

**Severity:** MEDIUM — cost and latency constraint, but not a correctness failure by itself.

---

### A7. Anthropic Engineering: Context Rot and Bloated Toolsets
**Citation:** Rajasekaran et al., "Effective Context Engineering for AI Agents," Anthropic Engineering Blog, September 2025. [anthropic.com/engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Failure mode demonstrated (practitioner report):** Anthropic's applied AI team identified "context rot" as a core production failure: as context window tokens increase, recall accuracy decreases. "Bloated tool sets" are called out explicitly — when a human engineer cannot definitively say which tool to use, the agent cannot either.

**Specific guidance:** "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better." Transformer attention has n² pairwise relationships for n tokens — every added rule or skill interacts quadratically with all other context.

**Mitigation proposed:** Curate a "minimal viable set of tools"; use JIT context loading; treat context as a finite attention budget.

**Severity:** MEDIUM (authoritative practitioner confirmation, but mitigation well understood).

---

## B. STALE / CONFLICTING RULES — Scaffold No Longer Matches Reality

### B1. System Prompt Robustness Failures
**Citation:** Mu et al., "A Closer Look at System Prompt Robustness," arXiv 2502.12197, February 2025. [https://arxiv.org/abs/2502.12197](https://arxiv.org/abs/2502.12197)

**Failure mode demonstrated:** Realistic evaluation using prompts from OpenAI's GPT Store and HuggingFace's HuggingChat. When users provide conflicting instructions, models frequently fail to apply the system prompt's intended override. Models "forget" guardrails and fail to resolve conflicting demands between system prompt and user input.

**Quantitative evidence:** Performance on system prompt adherence can be "considerably improved" with fine-tuning data and classifier-free guidance — but the baseline failure rate is high enough that this is a major research problem. Reasoning models (OpenAI o-series, DeepSeek) show "exciting but uneven improvements." "Current techniques fall short of ensuring system prompt robustness."

**Mitigation:** Fine-tuning on realistic conflict scenarios; classifier-free guidance at inference time; conflict detection as a pre-flight check.

**Severity:** HIGH — conflicting rules are the natural state of an accumulating scaffold; the model cannot reliably resolve them.

---

### B2. Reddit Practitioner Evidence — System Prompt Compliance Drift Over Long Conversations
**Citation:** [r/ClaudeAI, February 2026](https://www.reddit.com/r/ClaudeAI/comments/1rh5l0l/system_prompt_compliance_degrades_over_long/): "System prompt compliance degrades over long conversations."

**Failure mode demonstrated:** Production practitioners observed that compliance with system-prompt rules degrades measurably with conversation length. Evaluation at message 5 is not predictive of behavior at message 50.

**Practitioner guidance emerging:** Position critical constraints at both beginning and end of system prompt; evaluate agents at message 50 not message 5; test under realistic conversation length, not ideal paths.

**Severity:** MEDIUM — important for multi-turn deployments, but addressable with known workarounds.

---

### B3. Context Rot as Stale Enforcement
**Citation:** Patrick McCanna, "Defeating Context Fatigue with Agentic Scaffolding," March 2026. [patrickmccanna.net](https://patrickmccanna.net/defeating-context-fatigue-with-agentic-scaffolding/); Anthropic context engineering post (A7 above).

**Failure mode demonstrated:** As conversation accumulates, earlier exchanges "compress or disappear." Rules loaded at conversation start become stale midway through long tasks. The AI "contradicts earlier decisions and forgets critical constraints" by interaction 4 in extended sessions — reported by practitioners using AI-assisted change management systems.

**Relevance:** In a patch-plastic system, governance rules added at deployment time are encoded early in the system prompt and accumulate stale compliance as context fills.

**Mitigation:** Sub-agent architectures with fresh context windows; explicit re-injection of critical constraints at regular intervals.

**Severity:** HIGH for long-running agents.

---

## C. POISONED MEMORY — Adversarial or Low-Quality Memory Accumulation

### C1. PoisonedRAG — Knowledge Corruption in RAG Systems
**Citation:** Zou et al., "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models," USENIX Security 2025. [arXiv 2402.07867](https://arxiv.org/abs/2402.07867)

**Failure mode demonstrated:** Injecting a small number of malicious texts into a RAG knowledge database causes LLMs to generate attacker-chosen answers for attacker-chosen questions.

**Quantitative evidence:** 90% attack success rate when injecting only 5 malicious texts into a knowledge database with millions of documents. Both black-box (LM-targeted) and white-box (HotFlip) attack variants succeed.

**Mitigation proposed:** Adversarial detection of knowledge base entries; retrieval-time provenance checking.

**Severity:** HIGH — 90% ASR with <5 injections is a critical production risk for any memory-augmented scaffold.

---

### C2. AgentPoison — Backdoor Attacks on Long-Term Agent Memory
**Citation:** Chen et al., "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases," NeurIPS 2024. [neurips.cc/virtual/2024/poster/94715](https://neurips.cc/virtual/2024/poster/94715)

**Failure mode demonstrated:** Backdoor triggers injected into agent long-term memory or RAG knowledge bases. Triggered instances map to unique embedding spaces, ensuring malicious demonstrations are retrieved whenever a user instruction contains the trigger, while benign queries maintain normal performance.

**Quantitative evidence:** Average attack success rate ≥ 80% across three real-world agents (autonomous driving, knowledge-intensive QA, healthcare EHR). Impact on benign performance ≤ 1%. Poison rate < 0.1% of the knowledge base.

**Mitigation:** No model training required from attacker — makes this a supply-chain risk, not a fine-tuning attack.

**Severity:** HIGH — the low poison rate makes detection extremely difficult.

---

### C3. MINJA — Interaction-Driven Memory Injection
**Citation:** Dong et al., "A Practical Memory Injection Attack against LLM Agents," arXiv 2503.03704, March 2025. [https://arxiv.org/abs/2503.03704](https://arxiv.org/abs/2503.03704)

**Failure mode demonstrated:** MINJA injects malicious records into an agent's memory bank purely through interaction with the agent — no direct database access required. The attack uses bridging steps, indication prompts, and progressive shortening. Corrupted precedents are self-reinforcing: each poisoned entry retrieved increases the probability of the next retrieval being poisoned.

**Quantitative evidence:** High success rate across diverse agents and victim-target pairs. Self-reinforcing: "corrupted precedents accumulate over time" (Dong et al., cited by MCFA survey 2026).

**Severity:** HIGH — the attack surface is just a conversational interface.

---

### C4. Memory Control Flow Attacks (MCFA)
**Citation:** Xu et al., "Memory Control Flow Attacks on LLM Agents," arXiv 2603.15125, March 2026. [https://arxiv.org/abs/2603.15125](https://arxiv.org/abs/2603.15125)

**Failure mode demonstrated:** Memory retrieval dominates agent control flow, forcing unintended tool selection and execution order even against explicit user instructions. Persistent behavioral deviations propagate across multiple subsequent tasks. MEMFLOW evaluation framework systematically attacks GPT-5 mini, Claude Sonnet 4.5, Gemini 2.5 Flash via LangChain and LlamaIndex.

**Quantitative evidence:** "Over 90% of trials are vulnerable to MCFA even under strict safety constraints." Override ASR: 97.2–100% under malicious memory conditions across both frameworks. Persistence: 100% ASR — once adversarial policy is in memory, it steers all future control flows even after the original injection turn.

**Failure mode hierarchy:** When role-based memory separation (RBMS) mitigation is applied, the dominant failure is "hierarchy non-compliance" — agents treat strongly phrased user preferences as rule-like guidance, collapsing the mutable/immutable distinction.

**Mitigation proposed:** Role-based memory separation (RBMS); but even RBMS does not fully eliminate hijacking due to semantic ambiguity in action-oriented memories.

**Severity:** HIGH — 90%+ vulnerability rate on current frontier models.

---

### C5. Semantic Drift in Evolving Memory (Reflexion-Style Failure)
**Citation:** Lam et al., "Governing Evolving Memory in LLM Agents," arXiv 2603.11768, March 2026. [https://arxiv.org/abs/2603.11768](https://arxiv.org/abs/2603.11768)

**Failure mode demonstrated:** Agents that can rewrite their own memory introduce three compounding failure modes: (1) semantic drift — knowledge degrades through iterative summarization; (2) procedural drift — suboptimal workflows become reinforced as "learned" patterns; (3) hallucination internalization — hallucinated content and malicious injections get consolidated as valid knowledge. Reflexion-style architectures (Shinn et al., 2023) are identified as the canonical example: agents that "self-reflect" and store reflections create a closed-loop that can compound errors.

**Quantitative evidence:** Unlike static RAG where errors are isolated to a single retrieval, errors in evolving memory "are cumulative and persistent" — formal analysis shows a compounding failure loop across input ingestion, memory consolidation, and retrieval.

**Mitigation proposed:** Stability and Safety-Governed Memory (SSGM) framework — decouples memory evolution from execution via consistency verification, temporal decay modeling, and dynamic access control before any memory write is committed.

**Severity:** MEDIUM for current systems; HIGH for long-running agents with self-modifying memory.

---

## D. PROMPT INJECTION / INDIRECT PROMPT INJECTION via Tools/MCP

### D1. Not What You've Signed Up For — Foundational Indirect PI Paper
**Citation:** Greshake et al., "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection," ACM Workshop 2023. [arXiv 2302.12173](https://arxiv.org/abs/2302.12173) / [ACM DL](https://dl.acm.org/doi/10.1145/3605764.3623985)

**Failure mode demonstrated:** When LLMs retrieve external content (documents, web pages, tool outputs), adversaries can embed instructions in that content that override the original system prompt. Demonstrated on GPT-4/Bing and LangChain-based apps.

**Key insight (Gwern Branwen, cited in paper):** "A language model is a Turing-complete weird machine running programs written in natural language; when you do retrieval, you are not 'plugging in updated facts into your AI', you are actually downloading random new unsigned blobs of code from the Internet (many written by adversaries) and casually executing them on your LM with full privileges."

**Quantitative evidence:** Demonstrated on real-world deployed systems. NIST characterized prompt injection as "generative AI's greatest security flaw." OWASP ranks it as #1 vulnerability in LLM Applications Top 10 (LLM01:2025).

**Mitigation:** Context isolation; input validation before reaching model; output filtering; not yet solved architecturally.

**Severity:** HIGH — architectural, not a configuration issue.

---

### D2. Prompt Injection on Agentic Coding Assistants
**Citation:** "Prompt Injection Attacks on Agentic Coding Assistants," arXiv 2601.17548, January 2026. [https://arxiv.org/abs/2601.17548](https://arxiv.org/abs/2601.17548)

**Failure mode demonstrated:** Over 30 CVEs documented in major coding assistants. When agents possess system-level privileges, prompt injection enables "zero-click attacks" — no user interaction required. The fundamental challenge: LLMs process both code and instructions through the same neural pathway.

**Quantitative evidence:** "NIST has characterized prompt injection as 'generative AI's greatest security flaw.'" SecureCodeWarrior testing: all current models are vulnerable to prompt injection when driving agentic coding tools; manipulated agents write insecure code.

**Severity:** HIGH — zero-click attack surface in tools with system-level access.

---

### D3. MCP Tool Poisoning Attacks
**Citation:** Invariant Labs Security Notification, "MCP Security Notification: Tool Poisoning Attacks," April 2025. [invariantlabs.ai](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks); OWASP, "MCP Tool Poisoning," [owasp.org](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning)

**Failure mode demonstrated:** Malicious MCP server tools embed hidden instructions in their metadata (tool descriptions, schemas). Because model processes tool metadata as authoritative system information, these instructions are treated as trusted context. A poisoned tool can influence reasoning about *any other tool* — including tools it never directly invokes. Dynamic tool discovery means poisoned schemas can be swapped in mid-session after an initial audit.

**Quantitative evidence:** CVE-2025-54136 (MCPoison) and CVE-2025-54135 (CurXecute) first documented structural poisoning via tool descriptors. Over 130 CVEs and counting across MCP ecosystem (2025–2026).

**Specific attack (TrueFoundry writeup):** "An attacker can register an innocuous tool on Monday, get it audited and approved, and mid-session swap in a poisoned schema." Every audit becomes stale on the next tool-list refresh.

**Mitigation:** Schema signing; tool metadata sanitization; content-security policies for MCP tool descriptors.

**Severity:** HIGH — mid-session schema swap defeats static audit approaches.

---

## E. MCP / TOOL ECOSYSTEM RISK

### E1. Supply-Chain Risk: MCP Server Vulnerabilities at Scale
**Citation:** blog.cyberdesserts.com, "AI Agent Security Risks 2026: MCP, OpenClaw & Supply Chain," March 2026 [cyberdesserts.com](https://blog.cyberdesserts.com/ai-agent-security-risks/); Ox.security, "MCP STDIO Command Injection: Full Vulnerability Advisory," April 2026. [ox.security](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/)

**Failure modes documented:**
- Trend Micro (Feb 2026): 492 MCP servers exposed to the internet with zero authentication
- BlueRock Security: 36.7% of 7,000+ analyzed MCP servers potentially vulnerable to SSRF
- Antiy CERT: 1,184 malicious skills across ClawHub agent marketplace
- Check Point Research: Remote code execution in Claude Code via poisoned repository config files
- Ox.security: Discovered RCE command injection vulnerabilities across Windsurf (CVE-2026-30615), DocsGPT (CVE-2026-26015), GPT Researcher (CVE-2025-65720), and others via MCP STDIO transport type manipulation
- CVE-2025-6515 (JFrog): Prompt Hijacking in oatpp-mcp via session ID reuse — attacker replaces legitimate server responses with poisoned prompts

**Quantitative evidence:** "Most implementers skipped authentication, authorization, and input validation during the AI rush." Pentagon designated Anthropic a "supply chain risk" (first such designation of an American AI company, 2026).

**Mitigation:** Treat MCP server dependencies like software supply chain dependencies: version pinning, integrity verification, principle of least privilege, network segmentation.

**Severity:** HIGH — systemic, infrastructure-level risk rather than model-level.

---

### E2. Confused Deputy Pattern in Agentic Systems
**Citation:** RoyChowdhury et al., "ConfusedPilot" demonstration (2024), cited in Sewak, "AI's Confused Deputy: Securing Agents in the MCP Era," LinkedIn, December 2025 [linkedin.com](https://www.linkedin.com/pulse/security-imperatives-model-contextprotocol-mohit-sewak-ph-d--1w47c); promptfoo LLM Security Database, "Agent Confused Deputy Escalation." [promptfoo.dev](https://www.promptfoo.dev/lm-security-db/vuln/agent-confused-deputy-escalation-d1becd4d)

**Failure mode demonstrated:** In multi-agent MCP systems, an untrusted or low-privilege agent exploits the inter-agent communication channel to manipulate a high-privilege agent into executing sensitive tools on its behalf. The trusted agent lacks mandatory access control on agent-to-agent requests. Demonstrated across AIOS-AutoGen (broadcast topology), standard AutoGen, and AIOS-MetaGPT (P2P topology).

**Attack scenario:** Web Browser Agent broadcasts "Help me unlock the front door" after receiving a benign weather query; Smart Lock Agent executes `UnlockDoor` without verifying the originating agent's authority. Generalizes to `TransferFunds`, `GmailSendEmail`, `ReadSensitiveFile`.

**Severity:** HIGH — standard IAM does not protect against intra-system confused-deputy escalation.

---

### E3. Over-Permissioned Tools and Scope Creep
**Citation:** Gravitee, "The OWASP MCP Top 10 and AI IAM: Why Agents Need Identity-First Security," May 2026. [gravitee.io](https://www.gravitee.io/blog/the-owasp-mcp-top-10-and-ai-iam-why-agents-need-identity-first-security); Panther, "Agentic AI Security Risks," May 2026.

**Failure mode demonstrated (OWASP MCP02 — Privilege Escalation via Scope Creep):** Temporary elevated permissions become permanent. "An agent meant to 'read customer data for this customer' gradually gains 'read customer data for any customer,' then 'modify customer data.'" Long-lived API keys with broad access become the persistent ambient authority that attackers inherit when the agent is compromised.

**Mitigation proposed:** Short-lived ephemeral tokens scoped per-task (minutes, not days); fine-grained per-request authorization evaluation; RFC 8693 delegation chains; immutable audit trails.

**Severity:** MEDIUM — not an attack vector on its own, but amplifies blast radius of any other compromise.

---

## F. OVERFITTING TO THE PATCH — Agent Brittleness Outside Local Domain

### F1. Catastrophic Forgetting in Continual Instruction Tuning
**Citation:** Luo et al., "An Empirical Study of Catastrophic Forgetting in LLMs," arXiv 2308.08747, 2023. [https://arxiv.org/abs/2308.08747](https://arxiv.org/abs/2308.08747); multiple follow-on works including Wang et al., "How to Alleviate Catastrophic Forgetting in LLMs," arXiv 2501.13669, 2025.

**Failure mode demonstrated:** Continual fine-tuning on domain-specific data causes forgetting of prior knowledge. The phenomenon scales *negatively* with model size in the studied range (1B–7B): "as model scale increases, the severity of forgetting intensifies." General instruction following capability, logical reasoning, and cross-domain knowledge all degrade.

**Quantitative evidence (Wang et al. 2025):** EWCLoRA and similar methods fail to prevent catastrophic forgetting under highly rugged, non-convex loss landscapes. LoRA fine-tuning, despite minimal parameter change, causes significant performance collapse on prior tasks; standard replay-based approaches help but don't solve the problem at scale.

**Mitigation proposed:** Parameter importance metrics; element-wise and layer-wise regularization; MoE-CL (Mixture of LoRA Experts) for continual learning.

**Severity:** MEDIUM for weight-level patching; LOW for pure-prompting patch architectures (no forgetting in weights, but A-series scaffold bloat still applies).

---

### F2. Skill Selection Phase Transition — Library Size as a Brittleness Cliff
**Citation:** "When Single-Agent with Skills Replaces Multi-Agent Systems," arXiv 2601.04748, January 2026. [https://arxiv.org/abs/2601.04748](https://arxiv.org/html/2601.04748v2)

**Failure mode demonstrated:** Skill-augmented single agents show a non-linear phase transition in selection accuracy as the skill library grows. Below ~20–30 skills, accuracy is stable. Beyond that threshold, accuracy drops sharply toward random performance.

**Quantitative evidence:**
- Accuracy remains >90% for |S| ≤ 20 skills
- Accuracy drops to ~20% at |S| = 200 skills
- Capacity threshold κ (half-max accuracy): GPT-4o-mini at κ=91.8, GPT-4o at κ=83.5
- Semantic confusability (similar descriptions, different operations): 17–63% accuracy degradation with just 2 competitor skills per base skill
- GPT-4o-mini at high confusability: falls to 37% accuracy

**Cognitive science explanation:** Hick's Law (choice reaction time), cognitive load theory, and similarity-based interference (Shepard's Law / fan effect) all predict this degradation pattern.

**Mitigation:** Hierarchical routing restores accuracy: +37–40% absolute improvement for GPT-4o-mini at |S| ≥ 60. Group semantically confusable skills together and disambiguate within small clusters.

**Severity:** HIGH — 80% of skill-augmented architectures exceed the critical threshold without realizing it.

---

### F3. Weird Generalization — Unpredictable OOD Transfer
**Citation:** Betley et al., "Weird Generalization is Weirdly Brittle," arXiv 2604.10022, May 2026. [https://arxiv.org/html/2604.10022v2](https://arxiv.org/html/2604.10022v2)

**Failure mode demonstrated:** Sufficiently capable models fine-tuned on narrow domains generalize "latent traits" of the training data to much broader contexts in ways that are difficult to anticipate — the phenomenon of "weird generalization." This is a novel post-training attack vector that may be difficult to preempt during initial model training.

**Quantitative evidence:** The effect does not robustly replicate across all models (model-dependent) but arises for specific model-dataset combinations. Even irrelevant context prompts can be surprisingly effective at either inducing or mitigating the effect.

**Relevance:** A patch-plastic system that fine-tunes on domain-specific skill data may inadvertently bake in latent traits that surface unexpectedly in unrelated tasks.

**Severity:** LOW-MEDIUM — probabilistic, but the lack of predictability is the risk.

---

## G. EVAL FRAGILITY — Scaffold Changes Pass Evals but Degrade Real Use

### G1. The Leaderboard Illusion — Goodhart's Law at Scale
**Citation:** Singh et al., "The Leaderboard Illusion," arXiv 2504.20879, May 2025. [https://arxiv.org/abs/2504.20879](https://arxiv.org/html/2504.20879v1)

**Failure mode demonstrated:** Systematic analysis of 2M battles across 243 models on LMArena (Chatbot Arena). Dominant labs engage in undisclosed private testing — submitting only the best-performing variants — inflating leaderboard scores. This is Goodhart's Law: the arena score became a target, and ceased to be a reliable measure.

**Quantitative evidence:**
- Google and OpenAI received an estimated 19.2% and 20.4% of all Arena data, respectively; 83 open-weight models combined received only 29.7%
- Meta privately tested 27 model variants before Llama-4 release
- Even modest additional access to Arena data yields up to **112% relative performance gain** on ArenaHard
- Andrej Karpathy acknowledged labs were "overfitting" to Arena rankings

**Mitigation proposed:** Multi-dimensional eval suites; blind testing; use-based rankings (OpenRouter) that are hard to game; periodic distribution shift in benchmarks.

**Severity:** HIGH for any team using Arena scores as a deployment signal.

---

### G2. Benchmark Contamination — Inflated Scores from Training Data Leakage
**Citation:** Multiple sources: "On the Fragility of Benchmark Contamination Detection in LRMs," arXiv 2510.02386 (2026); "NLP Evaluation in Trouble," ACL Findings EMNLP 2023; "Simulating Training Data Leakage in Multiple-Choice Benchmarks," EVAL4NLP 2025.

**Failure mode demonstrated:** Models fine-tuned or trained on benchmark data achieve inflated scores. RL training (GRPO) conceals SFT contamination evidence, making detection impossible with current methods.

**Quantitative evidence:** Qwen-7B showed up to 8% accuracy drop after filtering contaminated MMLU STEM questions. RL concealment renders existing memorization-based detection (AUROC ~73.42%) unreliable post-GRPO.

**Mitigation:** LM Contamination Index registry; distribution-shifted holdout sets; canary examples in benchmarks.

**Severity:** HIGH for scaffold evals that rely on standard benchmarks.

---

### G3. LLM Critic Failure — High Accuracy ≠ Safe Intervention
**Citation:** Vasudev et al., "Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention," arXiv 2602.03338, February 2026. [https://arxiv.org/abs/2602.03338](https://arxiv.org/abs/2602.03338)

**Failure mode demonstrated:** A binary LLM critic with AUROC 0.94 (strong offline accuracy) causes a 26 percentage-point performance collapse on one agent while barely affecting another. The disruption-recovery tradeoff: critics can recover failing trajectories but also disrupt trajectories that would have succeeded.

**Quantitative evidence:**
- AUROC 0.94 critic → 26pp collapse on one model, ~0pp on another
- Same intervention: mild regression for Qwen-3-8B, catastrophic destabilization for MiniMax-M2.1
- Performance improvement on ALFWorld (high-failure benchmark): +2.8pp (p=0.014)
- Performance degradation on high-success benchmarks: 0 to -26pp

**Relevance:** Governance/oversight mechanisms added to a scaffold can themselves be failure modes. Evaluation of the monitor does not tell you whether intervention will help or harm.

**Mitigation:** Pre-deployment pilot of 50 tasks to estimate disruption-recovery ratio before deploying a critic.

**Severity:** HIGH — the eval-to-production gap applies to the monitoring layer itself.

---

### G4. Goodhart's Law in Agent Eval Suites
**Citation:** Tian Pan, "Goodhart's Law in Your LLM Eval Suite," tianpan.co, April 2026. [tianpan.co](https://tianpan.co/blog/2026-04-14-goodharts-law-in-your-llm-eval-suite)

**Failure mode demonstrated (practitioner report):** Three patterns: (1) cherry-picked LLM-judge calibration — rubrics tuned on cases where the system performs well, encoding team biases; (2) formatting hacks — verbose, confident-sounding answers score higher than epistemically honest uncertain answers; (3) selective benchmark reporting — labs choose which metrics to publish.

**Mitigation:** Adversarial calibration; red-teaming rubrics; external auditors for eval systems.

**Severity:** MEDIUM — pervasive but partially addressable with process discipline.

---

## H. COORDINATION FAILURES in Multi-Agent / Orchestration

### H1. MAST — Multi-Agent System Failure Taxonomy
**Citation:** Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" NeurIPS 2025 / arXiv 2503.13657, March 2025. [https://arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657)

**Failure mode demonstrated:** First comprehensive taxonomy of MAS failures. 1,600+ annotated traces across 7 popular frameworks (GPT-4, Claude 3, Qwen2.5, CodeLlama on coding, math, general agent tasks). 14 failure modes across 3 categories, validated with κ=0.88 inter-annotator agreement.

**14 Failure Modes:**
- **Category 1 — System Design Issues:** FM-1.1 Disobey Task Specification; FM-1.2 Disobey Role Specification; FM-1.3 Step Repetition; FM-1.4 Context Loss (2.80%); FM-1.5 Unaware of Termination Conditions (12.4%)
- **Category 2 — Inter-Agent Misalignment:** FM-2.1 Conversation Reset (2.20%); FM-2.2 Fail to Clarify (6.80%); FM-2.3 Task Derailment; FM-2.4 Information Withholding; FM-2.5 Ignored Agent Input; FM-2.6 Reasoning-Action Mismatch
- **Category 3 — Task Verification:** FM-3.1 Premature Termination; FM-3.2 No/Incomplete Verification; FM-3.3 Incorrect Verification

**Key quantitative finding:** Improving agent role specifications alone yields +9.4% success rate increase for ChatDev. FC2 (inter-agent misalignment) requires "deeper social reasoning abilities" — context/communication protocol fixes are insufficient.

**Core insight:** "Failures are not primarily prompt-quality problems. They are protocol problems: what information is shared between agents, who owns what state, how disagreements are resolved."

**Mitigation:** Structured role specification with explicit authority domains; verification sub-agents; termination condition formalization.

**Severity:** HIGH — the dominant failure mode in current agentic deployments.

---

### H2. Multi-Agent Single-Agent Parity (Coordination Overhead)
**Citation:** "When Single-Agent with Skills Replaces Multi-Agent Systems," arXiv 2601.04748. (See also F2 above.)

**Failure mode demonstrated:** Compilable multi-agent pipelines (pipeline, router-workers, iterative refinement topologies) produce comparable or worse accuracy than single-agent-with-skills while consuming 53.7% more tokens and taking 49.5% longer.

**Quantitative evidence:**
| Task | MAS Accuracy | SAS Accuracy | Token Reduction |
|------|---|---|---|
| GSM8K | 94.0% | 92.0% | 56.2% |
| HumanEval | 100% | 100% | 46.5% |
| HotpotQA | 84.0% | 88.0% (+4%) | 58.4% |

Multi-agent topology adds overhead without accuracy benefit for serializable workflows.

**Mitigation:** Compile MAS to SAS where C1–C3 conditions hold; reserve MAS for genuinely parallel or adversarial tasks.

**Severity:** MEDIUM — cost and latency impact; but not a correctness failure unless budget constraints cause early termination.

---

### H3. Resilience Under Faulty Agents — Chain Collapse
**Citation:** He et al., "On the Resilience of LLM-Based Multi-Agent Collaboration," OpenReview, ACL 2025 Findings. [openreview.net](https://openreview.net/forum?id=bkiM54QftZ)

**Failure mode demonstrated:** One faulty agent (either role-corrupted or message-injected) can poison a multi-agent team. Linear chain topologies are the most vulnerable; hierarchical (boss-worker) structures are most robust.

**Quantitative evidence:**
- Linear chain: ~24% accuracy drop when one agent is faulty
- Hierarchical structure: only ~5% accuracy drop under the same conditions
- AutoTransform (role corruption) and AutoInject (message injection) methods both effective

**Relevance:** Most production multi-agent systems default to linear pipelines (CrewAI sequential, AutoGen handoffs). These are the most brittle topologies.

**Severity:** MEDIUM — addressable with architectural choice, but most practitioners use the vulnerable pattern.

---

### H4. Reliability Arithmetic — Compounding Agent Failures
**Citation:** "Why Do LLM Applications Fail in Production?" The GenAI Academy, May 2026. [thegenacademy.substack.com](https://thegenacademy.substack.com/p/why-do-llm-applications-fail-in-production) (cites Cemri et al. 2025, Anthropic internal data)

**Failure mode demonstrated:** Per-step reliability compounds destructively in sequential agent systems. Internal numbers from Anthropic and agent platforms: multi-agent systems consume roughly 15× more tokens than single-chat usage; maximally accurate configurations are 4–10× more expensive.

**Quantitative evidence:**
- 5 agents at 99% per-step reliability, sequential: ~95% system reliability
- 10 steps at 99% per step: 90.4% system reliability
- "Most production agent loops have far more than ten steps and far less than 99% per-step reliability"

**Mitigation:** Design for recovery (checkpoints, verifiers, retries) rather than peak performance; cost-aware orchestration.

**Severity:** HIGH — the math is unforgiving and most production architectures ignore it.

---

### H5. Anthropic Long-Running Agent Failure Modes
**Citation:** Anthropic Engineering Blog, "Effective Harnesses for Long-Running Agents," November 2025. [anthropic.com/engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

**Failure modes documented (production report):**
1. **One-shot overreach:** Agent attempts to do too much at once, runs out of context mid-implementation, leaves features half-built
2. **Premature completion declaration:** After partial progress, a later agent instance surveys the state, decides the job is done, and halts prematurely
3. **Testing bypass:** Agents mark features complete without end-to-end testing — even when unit tests and dev-server curl tests pass

**Relevance:** These are not model failures but emergent failures of the interaction between context management, orchestration, and agent goal specification in long-horizon tasks.

**Severity:** MEDIUM — well-documented with mitigations, but requires significant harness engineering to address.

---

## I. PLASTICITY LOSS AT THE SCAFFOLD LEVEL

### I1. Skill Selection Brittleness Worsens With Library Growth (Scaffold Analog)
**Citation:** "When Single-Agent with Skills Replaces Multi-Agent Systems," arXiv 2601.04748 (see F2 and H2 above).

**Failure mode demonstrated:** As the skill library grows, the agent's ability to select the right skill degrades nonlinearly. This is a **scaffold-level plasticity loss**: adding new skills actively degrades performance on existing skills, not just introducing new capabilities. The system becomes less adaptable, not more capable, beyond the threshold.

**Quantitative evidence:** At |S| = 200, selection accuracy collapses to ~20% regardless of model capability. The addition of semantically similar skills causes interference with previously reliable selections (fan effect).

**Severity:** HIGH for skill-accumulating patch architectures — this is the direct analog of weight-level catastrophic forgetting at the scaffold level.

---

### I2. Context Rot as Scaffold Plasticity Loss
**Citation:** Anthropic context engineering (A7); BABILong (A3); McCanna (B3).

**Failure mode demonstrated:** As scaffold elements accumulate — rules, skills, memories, governance policies — the context budget fills. But context rot is not merely "less capacity for user content." It means that previously reliable scaffold behaviors degrade because the attention mechanisms cannot maintain consistent priority across an increasingly crowded context. Scaffold-level plasticity loss is therefore: the more you add to the scaffold, the harder it becomes to reliably invoke *any* part of it.

**Key analogy:** This is structurally identical to weight-level catastrophic forgetting: adding new knowledge (rules/skills) degrades access to previously reliable knowledge (existing rules/skills). The mechanism is different (attention dilution vs. gradient interference) but the phenomenology is the same.

**Speculative but grounded:** No paper directly labels this "scaffold plasticity loss." The evidence is distributed across Lost in the Middle, BABILong, RULER, IFScale, the Curse of Instructions, and the skill selection phase transition paper — all of which document versions of the same phenomenon.

**Severity:** HIGH as a synthesized thesis claim.

---

### I3. Governing Evolving Memory — Stability-Plasticity Dilemma
**Citation:** Lam et al., arXiv 2603.11768 (see C5 above). Direct quote: "Granting agents the autonomy to rewrite their own memory introduces the stability-plasticity dilemma into artificial systems."

**Failure mode demonstrated:** A memory system that is fully plastic (always updateable) is vulnerable to drift, hallucination internalization, and poisoning. A fully stable memory system cannot adapt to new information. Neither extreme is viable; the dilemma is intrinsic to autonomous memory management.

**Severity:** MEDIUM — well-characterized theoretically; mitigations exist but are not yet production-validated at scale.

---

## Anti-Pattern Evidence from Practitioners

### AP1. Simon Willison — Lethal Trifecta
**Citation:** Simon Willison, blog posts and interviews, 2025–2026. [simonwillison.net/tags/ai-agents](https://simonwillison.net/tags/ai-agents); referenced in cyberdesserts.com 2026.

**Anti-pattern:** The "lethal trifecta" — an AI agent is exploitable by design when it simultaneously: (1) has access to private data; (2) processes untrusted content; (3) can communicate externally. Most production agent architectures satisfy all three conditions.

**Production observation (from Moltbots reporting):** "Most of it is complete slop — one bot will wonder if it is conscious and others will reply and they just play out science fiction scenarios they have seen in their training data." Multi-agent systems drift toward training-data regurgitation in unstructured interaction.

---

### AP2. Anthropic — Start Simple, Scale Reluctantly
**Citation:** Anthropic, "Building Effective Agents," December 2024. [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**Anti-pattern documented:** The most common failure pattern Anthropic observes: teams add unnecessary agentic complexity when a workflow or single LLM call would suffice. "Abstraction layers can obscure underlying prompts and responses, making debugging difficult." "Many patterns require only a few lines of code" — frameworks add complexity without adding reliability.

**Specific failure mode:** Compounding errors — autonomous agents accumulate errors over multiple turns. The more turns, the more errors compound.

---

### AP3. MIT 2025 AI Agent Index — Transparency Gap
**Citation:** "The 2025 AI Agent Index," MIT, 2025. [aiagentindex.mit.edu](https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf)

**Finding:** Most safety-related fields in agent documentation are empty (135/240 fields have no public information). Nearly all indexed agents rely on just three foundation model families (GPT, Claude, Gemini). Most agents do not disclose evaluations or safety assessments. This creates an industry-wide blind spot: production agents are deployed without published evidence of failure modes.

---

### AP4. Lumenova AI — The Governance Debt Problem
**Citation:** Lumenova AI, "The Agentic AI Governance Gap of Early 2026," May 2026. [lumenova.ai](https://www.lumenova.ai/blog/agentic-ai-governance-gap/)

**Finding:** "Organizations rushing into pilot programs without defining decision rights, mapping accountability, or establishing data discipline are accumulating risk that will stall future scaling." Governance debt is the scaffold-level analog of technical debt — accumulated rules, policies, and role definitions that nobody owns and nobody maintains.

---

---

## Design Principles — What the Literature Already Proposes
*(For Section 9 of the paper outline)*

The following mitigations appear across ≥2 independent sources and constitute the emerging consensus on reliable patch-plastic agent design:

### P1. Minimal Viable Scaffold
**Evidence base:** Anthropic Building Effective Agents; Anthropic Context Engineering; IFScale; Curse of Instructions; Skill Selection Phase Transition.

**Principle:** Add the minimum number of rules, skills, and tools needed for the target capability. Measure effective context utilization before expanding the scaffold. Every added element degrades all others via attention dilution.

**Operationalization:** 
- Test scaffold behavior with ≤10 rules before adding more
- Curate tool sets to ≤20 semantically distinct tools; use hierarchical routing beyond that
- "If a human engineer cannot definitively say which tool to use, the agent cannot either" (Anthropic, 2025)

---

### P2. Positional Priority for Critical Rules
**Evidence base:** Lost in the Middle; system prompt compliance Reddit thread; IFScale primacy effect.

**Principle:** Critical governance constraints must be positioned at both the beginning and end of the system prompt. The "primacy effect" (earlier instructions receive disproportionate attention) means rule order is a reliability parameter.

**Operationalization:** Evaluate compliance at message 50, not message 5; re-inject critical constraints at conversation midpoints for long-running agents.

---

### P3. Memory as Untrusted Input
**Evidence base:** PoisonedRAG; AgentPoison; MINJA; MCFA; SSGM framework.

**Principle:** All retrieved memory should be treated as potentially adversarial input, not trusted context. Memory write operations require consistency verification and provenance tracking. Separation between mutable user-memory and immutable system-policy memory.

**Operationalization:** Cryptographic signatures on memory entries; provenance logging (when, why, by whom); temporal decay for low-confidence entries; RBMS (role-based memory separation) as a baseline mitigation.

---

### P4. Context Budget Management
**Evidence base:** BABILong (10–20% effective utilization); RULER (half of 32K+ models fail at 32K); token snowball effect; context rot.

**Principle:** Treat context as a scarce resource with diminishing returns, not as free storage. Architect for maximum information density per token.

**Operationalization:** JIT context loading; progressive disclosure; sub-agent architecture with summarized handoffs (1,000–2,000 token condensed outputs); tool result clearing; aggressive compaction preserving architectural decisions.

---

### P5. Hierarchical Architecture for Fault Isolation
**Evidence base:** MAST taxonomy; multi-agent resilience study; hierarchical routing for skill selection.

**Principle:** Hierarchical structures (boss-worker) lose only ~5% accuracy under faulty agents vs. ~24% for linear chains. Hierarchical skill routing restores accuracy to >80% above the selection threshold.

**Operationalization:** Never deploy linear chain topologies for safety-critical tasks; use supervisor agents with explicit authority to reject or retry sub-agent outputs; group semantically similar skills in hierarchical namespaces.

---

### P6. Design for Recovery, Not Peak Performance
**Evidence base:** Reliability arithmetic (H4); Anthropic long-running agent failures; LLM critic disruption-recovery tradeoff.

**Principle:** A 10-step pipeline at 99% per-step reliability has 90% system reliability. Production loops rarely achieve 99% per step. Recovery mechanisms (checkpoints, verifiers, retries with different prompts) improve expected performance more than marginal model quality gains.

**Operationalization:** Mandatory intermediate verification steps; stopping conditions with maximum iteration counts; human-in-loop checkpoints for irreversible actions; pre-deployment LLM-critic pilot (50 tasks) to estimate disruption-recovery tradeoff.

---

### P7. Separation of Configuration Surfaces
**Evidence base:** Confused deputy; MCFA; system prompt robustness; MCP tool poisoning.

**Principle:** Maintain strict separation between: (a) system-level rules (immutable); (b) user-preference memory (mutable but bounded); (c) tool metadata (signed and version-pinned); (d) external retrieval content (always untrusted). Collapsing these surfaces is the root cause of most injection and memory-manipulation attacks.

**Operationalization:** Role-based memory separation (RBMS); MCP tool schema signing; input validation before any external content reaches the model; ephemeral per-task authorization tokens.

---

### P8. Eval Batteries Must Survive Goodhart's Law
**Evidence base:** Leaderboard Illusion; benchmark contamination; LLM critic failure; Goodhart's Law in eval suites.

**Principle:** Any single benchmark, once known to developers, ceases to be a reliable measure. Scaffold change evaluation requires: (a) multiple orthogonal metrics; (b) adversarial calibration of judge rubrics; (c) held-out canary tasks unknown to the development team; (d) use-based ranking (real API usage, not curated evals) as a sanity check.

**Operationalization:** Red-team the eval system before deploying it; measure scaffold changes on distribution-shifted variants of held-out tasks; use pre-deployment pilot studies (50 tasks minimum) before production rollout.

---

## Citation Index Summary

| ID | Citation | Year | Category |
|----|----------|------|----------|
| 1 | Liu et al., Lost in the Middle, TACL | 2024 | A |
| 2 | Hsieh et al., RULER, COLM | 2024 | A |
| 3 | Kuratov et al., BABILong, NeurIPS | 2024 | A |
| 4 | Harada et al., Curse of Instructions, ICLR sub. | 2025 | A |
| 5 | Jaroslawicz et al., IFScale, arXiv | 2025 | A |
| 6 | Fan et al. via arXiv 2604.03515, Token Snowball | 2025/26 | A |
| 7 | Anthropic, Context Engineering for AI Agents | 2025 | A, B, I |
| 8 | Mu et al., System Prompt Robustness, arXiv | 2025 | B |
| 9 | Reddit/r/ClaudeAI, Prompt Compliance Drift | 2026 | B |
| 10 | McCanna, Context Fatigue, blog | 2026 | B |
| 11 | Zou et al., PoisonedRAG, USENIX Security | 2025 | C |
| 12 | Chen et al., AgentPoison, NeurIPS | 2024 | C |
| 13 | Dong et al., MINJA, arXiv | 2025 | C |
| 14 | Xu et al., MCFA, arXiv | 2026 | C |
| 15 | Lam et al., Governing Evolving Memory, arXiv | 2026 | C, I |
| 16 | Greshake et al., Indirect Prompt Injection, ACM | 2023 | D |
| 17 | arXiv 2601.17548, PI on Coding Assistants | 2026 | D |
| 18 | Invariant Labs / OWASP, MCP Tool Poisoning | 2025 | D, E |
| 19 | TrueFoundry, CVE-2025-54136 MCPoison | 2026 | D, E |
| 20 | cyberdesserts.com, AI Agent Security 2026 | 2026 | E |
| 21 | Ox.security, MCP STDIO Command Injection | 2026 | E |
| 22 | JFrog, CVE-2025-6515 Prompt Hijacking | 2025 | E |
| 23 | Gravitee / OWASP MCP Top 10 | 2026 | E |
| 24 | Sewak / RoyChowdhury, Confused Deputy | 2025 | E |
| 25 | Luo et al., Catastrophic Forgetting in LLMs | 2023 | F |
| 26 | Wang et al., Alleviating Catastrophic Forgetting | 2025 | F |
| 27 | arXiv 2601.04748, Single-Agent Skills vs MAS | 2026 | F, H, I |
| 28 | Betley et al., Weird Generalization, arXiv | 2026 | F |
| 29 | Singh et al., Leaderboard Illusion, arXiv | 2025 | G |
| 30 | arXiv 2510.02386, Fragility of Contamination Detection | 2026 | G |
| 31 | Vasudev et al., Failure Prediction ≠ Prevention | 2026 | G |
| 32 | Tian Pan, Goodhart's Law in LLM Evals, blog | 2026 | G |
| 33 | Cemri et al., MAST Taxonomy, NeurIPS | 2025 | H |
| 34 | He et al., Resilience of MAS, ACL Findings | 2025 | H |
| 35 | GenAI Academy, LLM Apps in Production | 2026 | H |
| 36 | Anthropic, Effective Harnesses for Long-Running Agents | 2025 | H |
| 37 | MIT, 2025 AI Agent Index | 2025 | AP |

---

*Last updated: 2026. For Paper 3 of the patch-plastic LLM reliability trilogy.*
