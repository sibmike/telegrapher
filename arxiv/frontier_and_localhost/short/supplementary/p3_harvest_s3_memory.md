# Paper 3 — Substrate 3: Memory Systems
## Evidence Harvest for LLM Reliability Trilogy

*Compiled 14 May 2026 | 17 systems evaluated | Patch-Plasticity Rubric 0–5*

---

## 0. Patch-Plasticity Rubric (0–5)

| Score | Criterion |
|-------|-----------|
| **0** | No persistent memory; stateless at session boundaries |
| **1** | Within-session memory only (context window); no cross-session store |
| **2** | Cross-session persistence but dump-all (no relevance retrieval); or retrieval but no experience distinction from raw docs |
| **3** | Cross-session + relevance retrieval + experience origin clearly distinguished from raw corpora |
| **4** | All of score 3 + captures failure/error patterns explicitly OR has consolidation/forgetting mechanism |
| **5** | All of score 4 + versioned/governed memory (provenance, auditability, correction pathways, institutional selection) |

---

## 1. Scored Summary Table

| # | System | Cross-Session | Relevance Retrieval | Experience ≠ RAG | Failure/Error Memory | Versioned/Governed | **Patch-Plasticity** |
|---|--------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Reflexion (Shinn et al. 2023) | ✓ (within-run) | Partial | ✓ | ✓✓ | ✗ | **4** |
| 2 | MemGPT / Letta (Packer et al. 2023) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 3 | Generative Agents (Park et al. 2023) | ✓ | ✓✓ | ✓ | ✗ | ✗ | **3** |
| 4 | A-MEM (Xu et al. 2025) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 5 | Mem0 (Chhikara et al. 2025) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 6 | Zep / Graphiti (Rasmussen et al. 2025) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 7 | LangGraph Long-Term Memory | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 8 | LangChain Primitives (legacy) | ✗ | ✗ | ✗ | ✗ | ✗ | **1** |
| 9 | Voyager Skill Library (Wang et al. 2023) | ✓ | ✓ | ✓ | ✓ (procedural) | ✗ | **4** |
| 10 | ChatGPT Memory (OpenAI 2024+) | ✓ | ✓ | ✓ | ✗ | Partial | **3** |
| 11 | Claude Memory (Anthropic 2025) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 12 | Gemini Code Assist Memory (Google 2025) | ✓ | ✓ | ✓ | ✓ (PR rejections) | ✗ | **4** |
| 13 | Cognee (open-source, 2024+) | ✓ | ✓✓ | ✓ | ✗ | ✗ | **3** |
| 14 | HippoRAG (Gutiérrez et al. 2024) | ✗ (one-pass) | ✓✓ | Partial | ✗ | ✗ | **2** |
| 15 | MIRIX (Wang & Chen 2025) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 16 | SOAR Cognitive Architecture | ✓ | ✓✓ | ✓ | ✓ (chunking) | ✗ | **4** |
| 17 | Governed Collaborative Memory / SSGM | ✓ | ✓ | ✓ | ✓ | ✓✓ | **5** |
| 18 | NanoResearch Memory Module (2026) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |
| 19 | MemoryBank (Zhong et al. 2023) | ✓ | ✓ | ✓ | ✗ | ✗ | **3** |

---

## 2. Per-System Entries

---

### 2.1 Reflexion (Shinn et al., NeurIPS 2023)
**Source:** arXiv:2303.11366 | [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366)

#### Memory Taxonomy
- **Episodic (explicit):** Reflective verbal summaries of prior task attempts are stored in an *episodic memory buffer*. The agent literally maintains a "filing cabinet" of its own post-failure analyses in natural language.
- **Working memory:** The current trajectory/context window serves as short-term memory.
- No semantic or procedural memory types distinguished.

#### Storage Backend
- Flat list / string buffer (in-context injection). Capped at the last 3 self-reflections to avoid context overflow. No vector DB — concatenation into the LLM prompt.

#### Retrieval Mechanism
- All-or-recent: memories are injected sequentially (most recent first). No similarity-based retrieval; the top-*k* most recent reflections are prepended. Not relevance-weighted.

#### Write Policy
- **After each failed episode:** The Self-Reflection LM observes (a) the trajectory, (b) the reward/feedback signal, and (c) prior `mem`, then generates a verbal critique stored as a new memory entry. Write is triggered unconditionally on task failure.
- Per the source text: *"Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials."*

#### Forgetting / Consolidation
- Hard cap: only the last 3 reflections are kept. No principled forgetting — purely FIFO eviction. No consolidation across episodes.

#### Empirical Metrics
| Benchmark | Baseline | Reflexion | Δ |
|-----------|----------|-----------|---|
| HumanEval pass@1 | 80% (GPT-4) | **91%** | +11pp |
| HotPotQA (ReAct) | baseline | +8% absolute | over EPM-only |
| AlfWorld (sequential decisions) | baseline | significant | vs CoT+ReAct |

Ablation (Fig. 4): Self-reflection provides **+8% absolute** over episodic memory alone (EPM), confirming the value of verbal failure synthesis beyond mere trajectory replay.

#### Bridge to Paper 2 (Error Memory)
**Critical finding for the trilogy:** Reflexion is the canonical example of explicit failure-pattern memory. Its episodic buffer stores *verbal diagnoses of what went wrong* ("I failed because I called tool X before establishing context Y"). This is the cleanest production-scale demonstration that memory can capture **residual error patterns** rather than just preferences. The CogArc survey paper ([arXiv:2309.02427](https://arxiv.org/abs/2309.02427)) notes: *"Reflexion uses an LLM to reflect on failed episodes and stores the results (e.g., 'there is no dishwasher in kitchen') as semantic knowledge."*

**Caveat:** Reflexion memory does NOT persist across session restarts — the buffer is populated during a single task-solving run. The paper [arXiv:2604.27707](https://arxiv.org/abs/2604.27707) ("Contextual Agentic Memory Is a Memo, Not True Memory") argues: *"A Reflexion agent that accumulates thousands of verbal self-critiques is still running the same frozen model at every session; its filing cabinet grows while its capacity does not."*

#### Patch-Plasticity Score: **4/5**
Captures failure patterns explicitly (+1 over score 3) but no true cross-session persistence (same-run only) and no versioning/governance.

---

### 2.2 MemGPT / Letta (Packer et al., arXiv 2023)
**Source:** arXiv:2310.08560 | [https://arxiv.org/abs/2310.08560](https://arxiv.org/abs/2310.08560)

#### Memory Taxonomy
OS-inspired hierarchy; two primary types:
- **Main context (RAM analogue):** The live LLM context window — fast, limited capacity.
- **External context (disk analogue):** Persistent storage outside the context window, paged in/out on demand. Subdivided into:
  - *Recall storage* (conversation history, episodic)
  - *Archival storage* (semantic/document facts)
- Does not explicitly use episodic/semantic/procedural vocabulary from cognitive science.

#### Storage Backend
- External context uses a **vector database** (FAISS or equivalent) for semantic similarity retrieval. Main context is the LLM's active context. Letta (the production evolution of MemGPT) uses PostgreSQL + pgvector as the default persistent backend, with pluggable vector stores.

#### Retrieval Mechanism
- **Relevance-on-demand:** When the agent needs information outside current context, it calls `archival_memory_search(query)` — a vector similarity search that pages relevant chunks into working context. Triggered by agent-initiated function calls ("interrupts"), not passively.
- Write/read operations are first-class agent actions: `core_memory_append`, `recall_memory_search`, etc.

#### Write Policy
- Explicit agent tool calls: the agent decides when to persist something using `archival_memory_insert(content)` and `core_memory_replace(key, value)`.
- Autonomous eviction: when main context nears capacity, the agent moves items to external storage via `archival_memory_insert`.
- Multi-session chat persistence: the agent can `core_memory_replace` personal facts about the user, enabling genuine cross-session memory.

#### Forgetting / Consolidation
- Main context: FIFO eviction when full.
- Archival storage: no decay or forgetting by default; entries accumulate. External context is permanent until explicitly deleted.

#### Empirical Metrics
- Evaluated on **document analysis** (large docs exceeding context) and **multi-session chat** tasks.
- Multi-session chat: agents "remember, reflect, and evolve dynamically through long-term interactions."
- In DMR benchmark (Deep Memory Retrieval, later used to benchmark Zep): MemGPT achieves **93.4%** accuracy ([arXiv:2501.13956](https://arxiv.org/abs/2501.13956) uses this as the baseline that Zep beats at 94.8%).

#### Patch-Plasticity Score: **3/5**
True cross-session persistence + relevance retrieval + experience origin distinct from docs. No explicit failure/error memory capture; no versioning.

---

### 2.3 Generative Agents (Park et al., ACM CHI 2023)
**Source:** arXiv:2304.03442 | [https://arxiv.org/abs/2304.03442](https://arxiv.org/abs/2304.03442)

#### Memory Taxonomy
- **Memory Stream:** A complete append-only log of all agent observations in natural language — a flat episodic record of every event the agent witnessed.
- **Reflections:** Higher-level semantic abstractions synthesized from the memory stream — effectively semantic memory extracted from episodic experience.
- **Plans:** Forward-looking procedural structures that emerge from reflection.
- Working memory: the active context window populated by the retrieval function.

#### Storage Backend
- **Natural language text with embeddings.** Each memory object has: (a) creation timestamp, (b) last-access timestamp, (c) importance score (rated 1–10 by LLM at write time), (d) embedding vector. Backend is not explicitly named but the implementation uses a vector store for cosine similarity.

#### Retrieval Mechanism
**Composite scoring — the paper's most important methodological contribution:**

```
Score(m, q) = α₁·recency(m) + α₂·importance(m) + α₃·relevance(m, q)
```

- **Recency:** Exponential decay with factor 0.995 per hour since last access.
- **Importance:** LLM-assigned score at write time (1 = mundane, 9 = poignant). Triggered by asking the LLM: *"On a scale of 1–10, how important is this memory?"*
- **Relevance:** Cosine similarity between query embedding and memory embedding.
- Top-*k* memories by composite score are retrieved into the active context.

#### Write Policy
- **Every observation → immediate write** to memory stream (always-on recording).
- **Reflection trigger:** When the sum of importances of recent, un-reflected memories exceeds a threshold (~100 points), the agent runs a reflection pass to synthesize higher-level insights. Reflection outputs are also stored as memories.

#### Forgetting / Consolidation
- No explicit deletion. Recency decay effectively suppresses old memories in retrieval without deleting them. Reflections consolidate multiple episodic observations into a single higher-level memory (semantic compression).

#### Empirical Metrics
- Ablation study (Table in paper): removing **observation** causes agents to lack situational awareness; removing **planning** causes reactive-only behavior; removing **reflection** causes loss of higher-level reasoning and social coordination.
- Emergent social behavior: starting from one Valentine's party idea, 25 agents autonomously coordinated party logistics over 2 simulated days.
- Behavioral evaluation by 25 crowdworkers: generative agents rated "more believable" than human interview transcripts in two of five interview types.

#### Patch-Plasticity Score: **3/5**
Robust cross-session persistence (within simulation runtime, but designed for persistence), tri-component retrieval, experience-origin distinct from docs. Does not explicitly capture failure patterns; no versioning.

---

### 2.4 A-MEM: Agentic Memory (Xu et al., NeurIPS 2025)
**Source:** arXiv:2502.12110 | [https://arxiv.org/abs/2502.12110](https://arxiv.org/abs/2502.12110)  
OpenReview: [https://openreview.net/forum?id=FiM0M8gcct](https://openreview.net/forum?id=FiM0M8gcct)

#### Memory Taxonomy
- Zettelkasten-inspired interconnected knowledge network.
- Each memory is a **structured note** with: contextual description, keywords, tags, embedding, and explicit links to related memories.
- No strict episodic/semantic/procedural split — the network is homogeneous but supports both factual and experiential content.

#### Storage Backend
- Graph-like linked structure (in-memory or persistent JSON). Exact DB backend not specified in the abstract; GitHub implementation uses a file-based store with vector embeddings.

#### Retrieval Mechanism
- Agent-driven: the system queries the knowledge network using the current task context.
- Link traversal: beyond embedding similarity, the agent follows explicit inter-memory links to surface related notes — analogous to associative retrieval.
- Dynamic: as new memories are added, the system re-analyzes existing memories to establish new links.

#### Write Policy
- On every new memory add: (1) generate structured note, (2) compare against historical memories for link candidates, (3) establish links where meaningful similarity found, (4) optionally **update attributes of existing memories** triggered by the new arrival.
- Memory evolution: new memories can modify the textual attributes of older memories — a rare property that enables retroactive correction.

#### Forgetting / Consolidation
- No explicit forgetting mechanism described. Memory evolution (retroactive attribute updates) serves as consolidation.

#### Empirical Metrics
- Experiments on **6 foundation models** show "superior improvement against existing SOTA baselines."
- NeurIPS 2025 poster acceptance confirms peer review.
- Specific numerical benchmarks not disclosed in abstract; full paper results pending detailed access.

#### Patch-Plasticity Score: **3/5**
Cross-session persistence, relevance + link-based retrieval, experience distinct from RAG. No explicit failure/error capture; no versioning.

---

### 2.5 Mem0 (Chhikara et al., arXiv 2025)
**Source:** arXiv:2504.19413 | [https://arxiv.org/abs/2504.19413](https://arxiv.org/abs/2504.19413)  
Docs: [https://docs.mem0.ai](https://docs.mem0.ai) | Product: [https://mem0.ai](https://mem0.ai)

#### Memory Taxonomy
- Flat fact extraction: salient facts distilled from conversation turns.
- **Graph memory variant:** Entity-relationship graph capturing relational structures.
- V3 (open-source, 2026): replaced external graph store with built-in entity linking in the vector store, with entity collection `{collection}_entities` boosting retrieval scores.
- Categories: user preferences, domain facts, procedural notes (informally).

#### Storage Backend
- **Vector store** (HNSW approximate nearest-neighbor index, e.g., Qdrant, pgvector, Pinecone). Partitioned by user identity.
- **Graph store** (optional, v2): neo4j-compatible for relational memory.
- **Relational store** (v3 open-source): metadata and entity links.

#### Retrieval Mechanism
- Query → embedding → top-*r* by cosine similarity → inject as context.
- Entity linking boost (v3): entities extracted from query are matched against `{collection}_entities`, boosting relevant memories in the combined score.
- Single-pass retrieval: one retrieval call, no agentic loops at inference time.

#### Write Policy
**Three-stage pipeline:**
1. **Extraction:** For each message pair (m_{t-1}, m_t), LLM extracts up to k≈5–10 salient facts.
2. **Consolidation:** Each candidate fact embeds → retrieves semantically similar existing memories → LLM classifies action as one of: `ADD / UPDATE / DELETE / NOOP`. Executed on vector store.
3. **Persistence:** Facts are inserted with hash-based deduplication (MD5).
- Optional decay: LRU policy or `exp(-λΔt)` memory decay for stale facts.

#### Forgetting / Consolidation
- Explicit: LRU eviction + exponential time-decay with configurable λ.
- Consolidation: `UPDATE` and `DELETE` operations during the consolidation step eliminate redundancy and stale information.

#### Empirical Metrics
| Benchmark | Old Algo | New Algo | Δ | Avg tokens/query |
|-----------|----------|----------|---|-----------------|
| LongMemEval overall | 67.8 | **93.4** | +25.6 | 6,787 |
| LoCoMo | 71.4 | **91.6** | +20.2 | 6,956 |
| BEAM (1M tokens) | — | **64.1** | — | 6,719 |
| BEAM (10M tokens) | — | **48.6** | — | 6,914 |

- vs OpenAI Memory: **+26% relative** on LOCOMO LLM-as-a-Judge metric.
- Latency: **91% lower** p95 latency vs full-context baseline.
- Token cost: **>90% savings** vs full-context.

Source: [docs.mem0.ai/core-concepts/memory-evaluation](https://docs.mem0.ai/core-concepts/memory-evaluation)

#### Patch-Plasticity Score: **3/5**
Full cross-session persistence, ADD/UPDATE/DELETE consolidation, entity-linked retrieval, experience distinct from RAG. No explicit failure/error capture as a first-class concept; no versioning or governance layer.

---

### 2.6 Zep / Graphiti (Rasmussen et al., arXiv 2025)
**Source:** arXiv:2501.13956 | [https://arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956)  
Docs: [https://help.getzep.com/v2/sessions](https://help.getzep.com/v2/sessions)

#### Memory Taxonomy
- **Temporal knowledge graph** (Graphiti engine): edges carry temporal validity intervals, enabling time-aware fact reasoning.
- Memory is user-scoped: all sessions for a user merge into a unified knowledge graph, not session-isolated.
- Types: conversational facts, business data entities, cross-session relationships.

#### Storage Backend
- **Knowledge graph** with temporal edges (Graphiti). Internally uses a graph database.
- Sessions are keyed by `session_id` and `user_id`; the user-level graph integrates data from all sessions.
- `memory.get()` returns user-level memory most relevant to the current session's recent messages — not session-isolated.

#### Retrieval Mechanism
- Session-aware: most recent messages from active session form the retrieval query.
- Knowledge graph traversal + temporal reasoning: resolves "what was true at time T" queries using edge timestamps.
- DMR (Deep Memory Retrieval) benchmark as primary evaluation signal.

#### Write Policy
- Continuous: `memory.add(messages)` ingests into session history AND into the user knowledge graph simultaneously.
- Knowledge graph updates: Graphiti dynamically synthesizes conversational data and structured business data, maintaining historical relationships with timestamps.

#### Forgetting / Consolidation
- Temporal supersession: new facts with more recent timestamps override older facts in the graph; old facts are preserved as historical data with end-timestamps (not deleted).
- No information destruction — temporal archiving rather than forgetting.

#### Empirical Metrics
| Benchmark | Zep | Baseline / Comparator |
|-----------|-----|----------------------|
| Deep Memory Retrieval (DMR) | **94.8%** | MemGPT: 93.4% |
| LongMemEval accuracy improvement | **+18.5%** | baseline implementations |
| Response latency | **90% lower** | baseline |

Source: [arXiv:2501.13956](https://arxiv.org/abs/2501.13956)

#### Patch-Plasticity Score: **3/5**
True cross-session persistence (user-level graph unifies sessions), relevance + temporal retrieval, experience-origin distinct from docs. No explicit failure/error memory; no governance layer.

---

### 2.7 LangGraph Long-Term Memory
**Source:** Official docs: [https://docs.langchain.com/oss/python/concepts/memory](https://docs.langchain.com/oss/python/concepts/memory)  
Announcement: [https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph](https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph)

#### Memory Taxonomy
Three explicitly named types mapped from cognitive science:

| LangGraph Type | What is Stored | Human Analogue | Implementation |
|----------------|----------------|----------------|----------------|
| **Semantic** | Facts about users/orgs | Things learned in school | JSON Profile or Document Collection |
| **Episodic** | Past agent actions/sequences | Things I did | Few-shot example prompting |
| **Procedural** | Rules/instructions/system prompt | Motor skills | Reflection or meta-prompting |

#### Storage Backend
- **JSON documents** in a `BaseStore` (hierarchical namespace/key structure).
- Namespace: custom labels (e.g., `(user_id, "preferences")`) — enables multi-tenant isolation.
- Production: database-backed store (PostgreSQL + pgvector, Redis, etc.).
- Default dev: `InMemoryStore`.

#### Retrieval Mechanism
- **Semantic search:** vector similarity via embeddings, sorted by cosine distance.
- **Content filtering:** exact-match filters on JSON document fields (`filter={"my-key": "my-value"}`).
- **Direct retrieval:** `store.get(namespace, key)` for known keys.
- Cross-namespace search supported via content filters.

#### Write Policy
Two modes:
1. **Hot path (synchronous):** Agent calls a memory-write tool during task execution, before responding. Immediate availability; adds latency.
2. **Background (asynchronous):** Scheduled task, cron, or user-triggered. Decoupled from main interaction loop; ideal for batch consolidation.

#### Forgetting / Consolidation
- No built-in decay. Developers implement UPDATE/DELETE via the `store.put()` API.
- `Trustcall` package (third-party) provides structured UPDATE/DELETE for collection-based memories.

#### Patch-Plasticity Score: **3/5**
Cross-session namespaced persistence, vector + filter retrieval, all three memory types explicitly supported, agent experience clearly distinguished from document RAG. No built-in failure/error capture; no governance layer.

---

### 2.8 LangChain Memory Primitives (Legacy)
**Source:** [https://docs.langchain.com/oss/python/langchain/short-term-memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)  
Deprecation note: official docs deprecate all classic memory classes as of LangChain 0.3.1.

#### Summary
The classic LangChain memory classes (`ConversationBufferMemory`, `ConversationSummaryMemory`, `ConversationBufferWindowMemory`, `ConversationEntityMemory`) are **within-session only**. They operate on the active context window and do not persist across session boundaries. As of v0.3.1, these are deprecated in favor of the LangGraph `Store` API and checkpointers.

| Primitive | Mechanism | Cross-Session |
|-----------|-----------|:---:|
| ConversationBufferMemory | Raw history in context | ✗ |
| ConversationSummaryMemory | LLM summary of history | ✗ |
| ConversationBufferWindowMemory | Window of last k turns | ✗ |
| ConversationEntityMemory | Entity state tracking | ✗ |

#### Patch-Plasticity Score: **1/5**
Within-session only; no cross-session persistence; no relevance retrieval.

---

### 2.9 Voyager Iterative Skill Library (Wang et al., 2023)
**Source:** arXiv:2305.16291 | [https://arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291)

#### Memory Taxonomy
- **Procedural memory (primary):** The skill library stores executable JavaScript code functions, each representing a learned behavior. This is the closest LLM-native analogue of procedural memory in the cognitive science sense.
- **Episodic (implicit):** Execution traces and error feedback from prior skill attempts are fed back into the iterative prompting mechanism to refine the current skill.

#### Storage Backend
- **Executable code files** (JavaScript) in a persistent directory — effectively a code repository serving as procedural memory.
- Retrieval uses **embedding-based similarity** (GPT-4 embeddings) to find relevant skills given a task description.

#### Retrieval Mechanism
- Task description → embedding → cosine similarity search over skill descriptions → top-5 skills retrieved.
- Compositional: retrieved skills can be composed into new skills.

#### Write Policy
- Skill is committed to the library **only after passing self-verification**: the agent checks that (a) the code executes without error, (b) the task objective is achieved (via GPT-4 self-check).
- Failed skills are iterated upon (using error feedback in the prompt) for up to N iterations before being abandoned.
- This is a **quality-gated write policy** — failure alone does not write to memory.

#### Forgetting / Consolidation
- No forgetting: the library only grows. Alleviates catastrophic forgetting by storing skills externally rather than in weights.
- No explicit consolidation of overlapping skills.

#### Empirical Metrics
| Metric | Voyager vs. Prior SOTA |
|--------|----------------------|
| Unique items obtained | **3.3×** more |
| Distance traveled | **2.3×** longer |
| Tech tree milestones | **15.3×** faster |

Skill library ablation: removing the skill library significantly degrades performance and prevents generalization to new Minecraft worlds.

#### Bridge to Paper 2 (Error Memory)
The **iterative prompting mechanism** explicitly incorporates execution errors into skill refinement. When a skill fails, the error message is injected into the next prompt iteration. This is a within-task form of failure memory that improves the procedural knowledge committed to the library. Cross-session, the library retains only **successful** procedures — failures are filtered out before persistence. This represents a partial answer to the error-pattern question: errors shape what gets stored but are not themselves stored.

#### Patch-Plasticity Score: **4/5**
Cross-session procedural persistence, embedding-based retrieval, quality-gated write (error-informed). Partial failure memory (errors shape library but are not retained as errors). No versioning.

---

### 2.10 ChatGPT Memory (OpenAI, 2024+)
**Source:** [https://help.openai.com/en/articles/8590148-memory-faq](https://help.openai.com/en/articles/8590148-memory-faq)

#### Memory Taxonomy
Two distinct mechanisms:
- **Saved memories:** Explicit user-requested or ChatGPT auto-detected facts stored in a "notepad." Semantic in nature (preferences, facts, names).
- **Chat history reference:** Implicit context from past conversations used to personalize responses. Episodic in nature.

#### Storage Backend
- Saved memories stored separately from chat history — persist even if the originating chat is deleted.
- Storage limit exists for saved memories (capacity increase of 20% for Enterprise in Feb 2025).
- Backend: OpenAI proprietary; not publicly disclosed.

#### Retrieval Mechanism
- Saved memories injected into context like custom instructions.
- Chat history references used to rewrite search queries (e.g., adding "vegan" to a restaurant query if the user's preference is stored).
- Relevance-conditioned: not all memories injected — ChatGPT selects contextually relevant ones.

#### Write Policy
- User-triggered: "remember that I am vegetarian."
- Auto-triggered: ChatGPT identifies useful information during conversation and saves autonomously.
- Update/merge: ChatGPT may update, combine, or remove memories on its own.
- Deleted memories retained for 30 days in system logs for safety/debugging.

#### Forgetting / Consolidation
- User can delete individual memories or all memories via Settings > Personalization.
- "Reference chat history" data deleted from systems within 30 days of toggling off the feature.
- No automatic time-based decay.

#### Versioning / Governance
- Admin controls for Enterprise: workspace owners can enable/disable memory globally.
- Explicit user controls: toggle on/off, delete individual or all.
- No provenance tracking (who/when a memory was created is not user-visible).

#### Patch-Plasticity Score: **3/5**
Cross-session persistence, relevance-conditioned retrieval, agent-experience origin (not RAG). Limited user controls (partial governance). No failure/error capture.

---

### 2.11 Claude Memory (Anthropic, 2025)
**Source:** [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) | [https://www.reworked.co/...](https://www.reworked.co/digital-workplace/claude-ai-gains-persistent-memory-in-latest-anthropic-update/)

#### Memory Taxonomy
- **Auto memory (Claude Code):** Claude saves notes for itself — build commands, debugging insights, architecture notes, code style preferences, workflow habits.
- **Cross-conversation memory:** For Claude Pro/Max/Team users (rolled out Sept 2025 to Team/Enterprise; all users subsequently), Claude retains context from previous conversations.
- Nature: primarily **semantic** (facts about user projects and preferences) with some **procedural** (workflow habits, debugging patterns).

#### Storage Backend
- Claude Code: local workspace `.claude` directory or similar markdown/JSON files.
- Claude.ai consumer product: proprietary backend (likely vector + key-value store).

#### Retrieval Mechanism
- Claude.ai: search-and-recall based on query relevance to past chat summaries + keyword search.
- Claude Code auto memory: context-conditional injection — Claude decides what's worth injecting into a given conversation.

#### Write Policy
- Auto memory: Claude decides what is "worth remembering based on whether the information would be useful in a future conversation."
- Not every session triggers a write — selective by design.
- Users can provide explicit instructions about what to retain or modify.

#### Forgetting / Consolidation
- Incognito chat mode: memory-free sessions available to all users.
- User can manage/delete memories.
- No automatic decay described.

#### Bridge to Paper 2 (Error Memory)
Claude Code auto memory explicitly lists **"debugging insights"** as a category that gets saved. This is the closest consumer product example of error/failure memory: failed build commands and their diagnoses can be retained as memory entries.

#### Patch-Plasticity Score: **3/5**
Cross-session persistence (Team/Enterprise), selective relevance-based write, experience-origin distinct from docs. Limited governance. No explicit failure-pattern taxonomy.

---

### 2.12 Gemini Code Assist Persistent Memory (Google, Nov 2025)
**Source:** [https://cloud.google.com/blog/products/ai-machine-learning/memory-for-ai-code-reviews-using-gemini-code-assist](https://cloud.google.com/blog/products/ai-machine-learning/memory-for-ai-code-reviews-using-gemini-code-assist)

#### Memory Taxonomy
- **Procedural memory (dominant):** Natural language rules encoding coding standards and best practices.
- **Episodic (implicit):** Pull request interaction histories serve as the raw material for rule extraction.
- Rules are generalizable — not raw episode storage.

#### Storage Backend
- Google-managed project, user-installation-isolated. Natural language rules stored as structured text. Exact DB not disclosed.

#### Retrieval Mechanism
**Two-pass contextual retrieval:**
1. Before analysis: broad query to retrieve rules relevant to the repository's domain/language.
2. After draft generation: narrow query to retrieve "highly specific rules" related to the AI's own draft suggestions.
- Relevance-conditioned: rules retrieved only when relevant to the specific code being reviewed.

#### Write Policy
- **Triggered only on PR merge** (to ensure conversation is complete and code is a "source of truth").
- Rule extraction: Gemini analyzes comment threads, identifies disagreements (e.g., developer rejects AI suggestion), infers a generalized rule.
- **Conflict-driven extraction:** rules are generated specifically when the AI suggestion is rejected — encoding PR-level error patterns into persistent procedural memory.
- Manual override: `styleguide.md` files provide always-injected static guidelines.

#### Forgetting / Consolidation
- Not described. Rules accumulate; no decay mechanism documented.

#### Bridge to Paper 2 (Error Memory)
**This is the most production-scale example of failure/rejection capture.** When a developer rejects an AI-generated code review comment, the system extracts the rejection as a generalized rule: *"Don't suggest line-wrapping for Java import statements."* This is an explicit, automated mechanism for persisting **AI error patterns** into long-term memory, operationalized at enterprise scale. The write trigger is precisely the signal that the AI got something wrong.

#### Empirical Metrics
Qualitative only (no published A/B numbers in the blog post):
- Transforms the agent from a "stateless tool" into a "long-term project contributor."
- Stops repeating rejected suggestions across PRs.

#### Patch-Plasticity Score: **4/5**
Cross-session persistence, two-pass relevance retrieval, experience clearly from agent interactions (not pre-existing docs), **explicit rejection/failure memory** as a write trigger. No versioning or provenance tracking of rules.

---

### 2.13 Cognee (Open-Source Framework, 2024+)
**Source:** [https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory](https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory) | GitHub: cognee-ai/cognee

#### Memory Taxonomy
- **Session memory:** Short-term working memory — relevant embeddings and graph fragments loaded into runtime context.
- **Permanent memory:** Long-term knowledge artifacts (user data, interaction traces, external documents, derived relationships). Continuously cross-connected inside the graph.
- Formal types: semantic (entity-relationship graph), episodic (interaction traces), episodic (via retrieval traces).

#### Storage Backend
Three unified layers:

| Layer | Purpose | Default | Also Supports |
|-------|---------|---------|--------------|
| Graph store | Entities, relationships | **Kuzu** | Neo4j, FalkorDB, Neptune, Memgraph |
| Vector store | Embeddings, semantic similarity | **LanceDB** | Qdrant, pgvector, Redis, Pinecone, ChromaDB |
| Relational store | Chunks, provenance | **SQLite** | PostgreSQL |

#### Retrieval Mechanism
14 retrieval modes, including:
- `GRAPH_COMPLETION`: vector hints → graph traversal → LLM grounded answer
- `TEMPORAL`: time-aware graph search
- `CODING_RULES`: code-focused with rule associations
- `GRAPH_COMPLETION_COT`: chain-of-thought over multi-hop graph traversals
- `FEELING_LUCKY`: LLM auto-selects mode

#### Write Policy
- `cognify()`: 6-stage pipeline — classify → permissions check → chunk → entity/relationship extraction → summarize → embed + commit graph edges. Hash-based deduplication; only new/updated files reprocessed.
- Multi-tenant: dataset-level permissions (read/write/delete/share).

#### Forgetting / Consolidation
`memify()` operation:
- Prunes stale nodes
- Strengthens frequent connections
- Reweights edges based on usage signals
- Adds derived facts
This makes Cognee's memory self-improving: the graph evolves based on retrieval feedback, not just insertion history.

#### Empirical Metrics
| Metric | Base Cognee | With CoT |
|--------|-------------|---------|
| Human-like correctness | 0.93 | +25% |
| DeepEval correctness | 0.85 | +49% |
| DeepEval F1 | 0.84 | **+314%** |
| DeepEval EM | 0.69 | **+1618%** |
| Base RAG correctness | 0.40 | — |

Source: cognee.ai benchmarks

#### Patch-Plasticity Score: **3/5**
Full cross-session persistence, 14 retrieval modes, self-improving `memify` consolidation, experience distinct from docs. No explicit failure/error memory; no versioning layer (though multi-tenant isolation is strong).

---

### 2.14 HippoRAG (Gutiérrez et al., 2024)
**Source:** arXiv:2405.14831 | [https://arxiv.org/abs/2405.14831](https://arxiv.org/abs/2405.14831)

#### Memory Taxonomy
- Neurobiologically inspired: LLMs as **neocortex** (general knowledge), knowledge graph as **hippocampus** (indexing new experiences).
- **Semantic long-term memory** for knowledge integration — not episodic experience storage.
- Designed for integrating *new textual knowledge* (documents/passages), not agent action traces.

#### Storage Backend
- **Knowledge graph** (open-triple extraction from passages) + **vector store** (dense embeddings).
- Personalized PageRank over the knowledge graph for multi-hop traversal.

#### Retrieval Mechanism
- Query → named entity extraction → dense retrieval for seed nodes → **Personalized PageRank** spreading activation through graph → retrieve supporting passages.
- Single-step retrieval achieves performance comparable to iterative retrieval (IRCoT) at 10–30× lower cost.

#### Write Policy
- One-time document indexing: passages are parsed, triples extracted, graph built. Not designed for continuous agent experience ingestion.

#### Forgetting / Consolidation
- Designed to avoid catastrophic forgetting by maintaining explicit graph structure rather than relying on model weights.
- No forgetting/pruning mechanism described.

#### Empirical Metrics
| Task | HippoRAG vs. SOTA RAG | vs. IRCoT |
|------|----------------------|-----------|
| Multi-hop QA | **+20%** accuracy | Comparable or better |
| Retrieval cost | — | **10–30× cheaper** |
| Retrieval speed | — | **6–13× faster** |

#### Limitations for Substrate 3
HippoRAG is more a **RAG architecture** than an agent memory system. It fails inclusion criterion 3 (memory from agent experience, not pre-existing corpora) — it indexes documents, not agent action traces. Included here as an influential architectural precursor to graph-based agent memory.

#### Patch-Plasticity Score: **2/5**
No cross-session experience persistence (document index, not agent memory). Excellent relevance retrieval via Personalized PageRank. Source is documents/corpora, not agent experience → fails criterion 3. No failure/error capture.

---

### 2.15 MIRIX (Wang & Chen, arXiv 2025)
**Source:** arXiv:2507.07957 | [https://arxiv.org/abs/2507.07957](https://arxiv.org/abs/2507.07957)

#### Memory Taxonomy
Six distinct types — the most comprehensive taxonomy in the field:

| Type | Function |
|------|----------|
| **Core** | Stable user identity, persistent preferences, fundamental facts |
| **Episodic** | Time-stamped event records from past interactions |
| **Semantic** | World knowledge and domain facts |
| **Procedural** | Skills and action sequences for tasks |
| **Resource Memory** | References to files, URLs, tools used |
| **Knowledge Vault** | Long-term accumulation of verified facts |

#### Storage Backend
- Secure local storage (privacy-preserving design). Multi-agent framework coordinates updates across the six stores. Specific DB not named in paper.

#### Retrieval Mechanism
- Multi-agent framework: specialized sub-agents handle retrieval from their respective memory stores. Dynamic coordination: updates and retrievals are controlled and coordinated across stores.
- Multimodal: handles both text and high-resolution screenshots.

#### Write Policy
- Multi-agent coordination: the framework dynamically determines which memory store receives a given piece of information based on its type.
- Real-time screen monitoring mode: monitors screen content to build personalized memory base.

#### Forgetting / Consolidation
- Not described in abstract. Secure local storage implies user control.

#### Empirical Metrics
| Benchmark | Metric | MIRIX | Comparator |
|-----------|--------|-------|------------|
| ScreenshotVQA | Accuracy | **+35%** vs RAG baseline | — |
| ScreenshotVQA | Storage | **99.9% reduction** | vs RAG baseline |
| LoCoMo | Overall accuracy | **85.4%** (SOTA) | — |

Source: [arXiv:2507.07957](https://arxiv.org/abs/2507.07957)

#### Patch-Plasticity Score: **3/5**
Cross-session persistence, multi-agent coordinated retrieval, 6-type taxonomy clearly distinguishes experience from documents. No explicit failure/error memory type; no versioning.

---

### 2.16 SOAR Cognitive Architecture
**Source:** Wikipedia: [https://en.wikipedia.org/wiki/Soar_(cognitive_architecture)](https://en.wikipedia.org/wiki/Soar_(cognitive_architecture)) | arXiv:2205.03854 | [https://soar.eecs.umich.edu](https://soar.eecs.umich.edu)

#### Memory Taxonomy
Full cognitive science taxonomy, the gold standard precursor:

| Memory Type | SOAR Implementation | Learning Mechanism |
|-------------|---------------------|--------------------|
| **Working memory** | Symbolic graph, current situation | Immediate update |
| **Procedural** | If-then rules (matched against WM) | **Chunking** (automatic rule induction) |
| **Semantic (SMEM)** | Directed cyclic graphs, fact-like structures | Online rule-based storage/retrieval |
| **Episodic (EPMEM)** | Automatic snapshots of WM in temporal stream | Automatic recording |

#### Storage Backend
- Symbolic relational structures with statistical metadata (recency, frequency, expected future reward).
- SMEM: directed cyclic graphs with base-level activation (ACT-R model).
- EPMEM: temporal stream of WM snapshots, queryable.

#### Retrieval Mechanism
- **Base-level activation** for SMEM: structure with highest activation matching query is retrieved. Frequency + recency weighted.
- **Spreading activation** for SMEM: activation spreads from retrieved structures to neighbors with decay, allowing context to influence retrieval.
- **Sequential temporal retrieval** for EPMEM: can page through episodes from past (like playing a tape).

#### Write Policy
- EPMEM: **automatic** — snapshots WM every decision cycle. No agent decision needed.
- SMEM: **rule-triggered** — rules create commands in a reserved WM area; retrieved structures added to WM.
- Procedural: **chunking** — SOAR automatically induces new rules from successful problem-solving sub-goals. This is the most powerful write mechanism: **experience directly generates new procedural knowledge**.

#### Forgetting / Consolidation
- Activation decay: SMEM structures deactivate over time/disuse but are not deleted.
- Chunking induces rules that generalize across episodes (consolidation of episodic experience into procedural memory).

#### Bridge to Paper 2 (Error Memory)
SOAR's **chunking** mechanism is the classical AI answer to the question of learning from failure: when an agent fails to find a rule, it enters an impasse, solves the subgoal, and then **chunks** the solution into a new procedural rule. This is automatic learning from encountered problems. While SOAR is a classical (non-LLM) architecture, it demonstrates that failure-driven procedural learning has been engineered successfully for 40 years — and LLM-based systems are only beginning to match it.

LLM-SOAR integration papers (arXiv:2510.09355) describe combining natural language with SOAR's symbolic memories, enabling LLMs to generate rules that are stored in SOAR's procedural memory.

#### Patch-Plasticity Score: **4/5**
Full cross-session persistence, base-level activation + spreading activation retrieval, chunking = failure-driven procedural learning, experience clearly distinct from corpus knowledge. No versioning/provenance layer (not designed for governed deployment).

---

### 2.17 Governed Collaborative Memory / SSGM
**Sources:**  
- arXiv:2605.04264 (Governed Collaborative Memory) | [https://arxiv.org/abs/2605.04264](https://arxiv.org/abs/2605.04264)  
- arXiv:2603.11768 (SSGM) | [https://arxiv.org/abs/2603.11768](https://arxiv.org/abs/2603.11768)

#### Memory Taxonomy
**SSGM (Stability and Safety-Governed Memory):**
- Distinguishes between: long-term memory, dynamic agent memory, consolidated knowledge.
- Identifies risks: topology-induced knowledge leakage, semantic drift (via iterative summarization).

**Governed Collaborative Memory:**
Four layers:
| Layer | Description |
|-------|-------------|
| Agent-local | Private to individual agent |
| Shared institutional | Governed, ratified, accessible across agents |
| Archive memory | Historical; superseded memories retained |
| Project-continuity | Cross-version, cross-phase memory |

#### Storage Backend
- Conceptual framework (not a specific implementation). Emphasizes provenance tracking and version lineage as requirements.

#### Retrieval Mechanism
- Governed access: dynamic access control prior to memory retrieval.
- Retrieval is gated by consistency verification and temporal decay modeling.

#### Write Policy
Four governance regimes:
1. **Ungoverned persistence:** No oversight (flagged as dangerous).
2. **Constitutional/hybrid:** Predefined rules + human oversight.
3. **Automatic metric-based:** Algorithmic performance signals select memories.
4. **Human-ratified artificial selection:** Human validation required for institutional persistence.

Documented traces from a live multi-agent ecosystem demonstrate: unmanaged false-memory persistence, ratified institutional memory, rejection and revision, identity-preserving expansion, governance-as-learning.

#### Forgetting / Consolidation
- **SSGM:** Temporal decay modeling; consistency verification before consolidation.
- **Governed:** Supersession (new memories replace old, but old are archived with lineage).
- Correction pathways: explicit mechanisms to identify and correct false memories.

#### Bridge to Paper 2 (Error Memory)
**This is the field's only framework explicitly addressing memory governance.** Key design criteria include:
- **Provenance fidelity:** Tracking what was remembered, when, by whom.
- **Selection traceability:** Why a memory was promoted to institutional state.
- **Epistemic quality:** Not just retrieval accuracy, but factual/logical correctness.
- **Correction pathways:** Mechanisms to identify and undo false memory persistence.

This directly bridges Paper 2 (error patterns) to Paper 3 (memory governance): a complete memory system must not only capture errors but also provide mechanisms to detect that a **memory itself is an error** and correct it.

#### Patch-Plasticity Score: **5/5**
Cross-session persistence, governed retrieval with access control, experience-origin distinct from docs, explicit governance regimes, provenance/version lineage, correction pathways, archive layer for historical memory. Only framework meeting all criteria.

---

### 2.18 NanoResearch Memory Module (2026)
**Source:** arXiv:2605.10813 | [https://arxiv.org/abs/2605.10813](https://arxiv.org/abs/2605.10813)

#### Memory Taxonomy
Tri-level architecture:
- **Memory Module:** User- and project-specific experience records — episodic/semantic in character. Grounds planning in the user's actual research history.
- **Skill Bank:** Procedural rules distilled from recurring operations — procedural memory, explicitly separated.
- **Policy Learning Layer:** Label-free conversion of free-form feedback → persistent parameter updates of the planner (parametric memory).

#### Storage Backend
Not specified in the abstract; the tri-level separation implies separate stores for each layer.

#### Retrieval Mechanism
- Context-aware heuristic scoring: `score(skill/memory, context) = f(task, user, background)`.
- Top-k relevant skills and memories retrieved before each task.

#### Write Policy
- Memory module: updated with new user/project experience after each interaction.
- Skill bank: recurring operations are distilled into compact procedural rules after multiple successful executions.
- Policy learning: SDPO (Sequential Direct Preference Optimization) converts feedback into parameter updates — the only example in this survey where memory persists as **weight changes**, not just external store entries.

#### Forgetting / Consolidation
- Not described. The parametric layer is updated continuously.

#### Empirical Metrics
| Dimension | Round 1 → Round 3 | Best vs. Comparator |
|-----------|-------------------|---------------------|
| Compliance (user preferences) | Monotonic improvement | 8.963 vs. 6.656 |
| Innovation | 4.960 → 5.645 | — |
| Expression | 5.428 → 6.172 | — |

"Performance improves monotonically from Round 1 to Round 3 on all dimensions, showing that the Skill Bank and Memory Module help NanoResearch genuinely accumulate procedural and contextual knowledge across cycles."

#### Patch-Plasticity Score: **3/5**
Cross-session persistence, context-aware retrieval, experience distinct from docs. The parametric learning layer is unique but not counted as memory governance.

---

### 2.19 MemoryBank (Zhong et al., 2023)
**Source:** arXiv:2305.10250 | [https://arxiv.org/abs/2305.10250](https://arxiv.org/abs/2305.10250)

#### Memory Taxonomy
- Long-term conversational memory tailored for personal companion applications.
- User personality model synthesized from interaction history.
- Primarily **semantic** (user facts, personality traits) and **episodic** (past interactions).

#### Storage Backend
- Not explicitly stated; likely vector store for embedding-based retrieval. Applied to ChatGPT and ChatGLM.

#### Retrieval Mechanism
- Relevance-based: "summon relevant memories" using the current context as query.

#### Write Policy
- Continuous update after each interaction.
- Memory updates incorporate both time elapsed and significance of the memory.

#### Forgetting / Consolidation
- **Ebbinghaus Forgetting Curve:** The defining contribution. Memory retention decays exponentially with time since last access, modulated by importance. When recalled, memory is reinforced (spaced repetition analogue). When importance drops below threshold, memory is forgotten.
- Formula: `R(I_t, τ) = e^(-τ/S)` where S is memory strength modulated by importance.

#### Empirical Metrics
- Qualitative: SiliconFriend chatbot demonstrates strong long-term companionship.
- Quantitative: Simulated dialogs with ChatGPT-as-user show improved personality understanding and memory recall vs. no-memory baseline.

#### Patch-Plasticity Score: **3/5**
Cross-session persistence, relevance retrieval, Ebbinghaus-based consolidation/forgetting (unique contribution), experience distinct from corpus. No failure/error capture; no versioning.

---

## 3. Memory Benchmarks: Head-to-Head Evidence

### 3.1 LongMemEval (Wu et al., 2024)
**Source:** [https://github.com/xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval) | EmergentMind: [https://www.emergentmind.com/topics/longmemeval](https://www.emergentmind.com/topics/longmemeval)

500 questions across 5 categories: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention. Context scales: 115K tokens (S) and 1.5M tokens (M).

| System | LongMemEval Overall | Key Gap |
|--------|--------------------:|---------|
| Naive LLM (no memory) | ~40–60% | Severe |
| Oracle / Full Context | ~70–75% | — |
| Session decomposition + fact-augmented keys | +4% recall, +5% QA | marginal |
| Time-aware query expansion | +7–11% temporal | — |
| **Mem0 (new algorithm)** | **93.4%** | SOTA |
| **Oracle AI Agent Memory** | **93.8%** | SOTA tie |
| **Zep** | **+18.5% vs baseline** | — |

Key findings: accuracy drops 30–60% as history lengthens for naive systems. Temporal reasoning and knowledge updates are the hardest categories.

LongMemEval-V2 (2026) extends to 25M–115M tokens using web agent trajectories. New challenge: "experienced operator" standard — agents must recall prior task patterns, not just conversational facts. Source: [arXiv:2605.12493](https://arxiv.org/abs/2605.12493)

### 3.2 LoCoMo (Maharana et al., ACL 2024)
**Source:** [https://snap-research.github.io/locomo/](https://snap-research.github.io/locomo/) | arXiv:2402.17753

10 conversations × 300 turns × up to 35 sessions. Evaluates: QA (single-hop, multi-hop, temporal, adversarial), event summarization, multimodal dialog generation.

| System | LoCoMo QA |
|--------|----------:|
| Long-context LLMs + RAG | +22–66% vs. base | 
| Human ceiling | 100% (approx) |
| Gap from human | 56% on QA, 73% on temporal |
| **Mem0 (new algorithm)** | **91.6%** |
| **MIRIX** | **85.4%** (SOTA for public systems) |

Key finding: temporal reasoning remains hardest — all automated systems lag human by >50% on causal/temporal questions.

### 3.3 BEAM (2026)
Multi-session benchmark at 1M and 10M token scales. Mem0 new algorithm: **64.1%** at 1M, **48.6%** at 10M. Reflects genuine difficulty of disambiguation when similar content appears many times across millions of tokens.

### 3.4 MemoryAgentBench (arXiv:2507.05257)
Four competencies: accurate retrieval, test-time learning, long-range understanding, selective forgetting. Includes LongMemEval reformatted for incremental multi-turn evaluation. MIRIX shows +9.7% average gain vs RAG across tasks. Source: [arXiv:2507.05257](https://arxiv.org/abs/2507.05257)

---

## 4. Error/Failure Memory: The Paper 2 Bridge

### 4.1 Systems That Explicitly Capture Failure Patterns

| System | Failure Memory Mechanism | Storage | Cross-Session? |
|--------|--------------------------|---------|:---:|
| **Reflexion** | Verbal self-critiques of what went wrong in failed task episodes | Episodic buffer (in-context string) | ✗ (within-run) |
| **Voyager** | Execution errors injected into skill refinement prompts; error-informed skills | Procedural (code) | ✓ |
| **Gemini Code Assist** | PR rejection events → generalized procedural rules ("don't suggest X") | Rule store (cloud) | ✓ |
| **SOAR chunking** | Impasse resolution → new procedural rules; automatic rule induction from failures | Procedural (rules) | ✓ |
| **Structured Reflection** (Su et al., 2025) | Mini-trajectories of erroneous call + reflection + corrected call as training data | Weight updates via RL | ✓ (baked into weights) |
| **Governed Collaborative Memory** | Identifies false-memory persistence; correction pathways as first-class concept | Governed archive | ✓ |

### 4.2 Systems That Do NOT Capture Failure Patterns
Mem0, Zep, Generative Agents, MemGPT, A-MEM, MIRIX, LangGraph, ChatGPT Memory, Claude Memory, Cognee — these systems capture **user preferences, domain facts, and successful procedures** but have no write trigger specific to errors or failures. Error information is lost at session boundaries.

### 4.3 Synthesis: Does Memory in Production Systems Capture Residual Error Patterns?

**The honest answer is: mostly no, with three important exceptions.**

The dominant paradigm in production memory systems (Mem0, Zep, ChatGPT Memory, Claude Memory, LangGraph) treats memory as a **preference and fact accumulation layer** — recording what the user likes, what domain knowledge has been established, and what procedures have worked. These systems have no write trigger for *"the agent got this wrong"*; failure is invisible to the memory layer. The information asymmetry is stark: successful interactions get stored while failures are discarded.

The three exceptions reveal the frontier:

1. **Reflexion** (research) demonstrates that verbal failure analysis can be stored and reused within a task run, yielding substantial performance gains (+8–11% on coding benchmarks). But its memory is within-run and not persisted across sessions — the "filing cabinet grows while its capacity does not," as the "Contextual Agentic Memory Is a Memo" paper ([arXiv:2604.27707](https://arxiv.org/abs/2604.27707)) puts it.

2. **Gemini Code Assist Persistent Memory** (production) is the most compelling production example: it explicitly makes PR rejection events — instances where the AI was wrong — into the write trigger for procedural memory. The system literally learns from its mistakes at scale, storing the lesson as a natural language rule for future deployment. This is the clearest operational bridge from Paper 2 (error patterns) to Paper 3 (memory systems).

3. **SOAR's chunking mechanism** (classical AI, 40 years old) demonstrates that failure-driven procedural learning is not a new problem. When SOAR fails to find a rule (impasse), the resolution is automatically compiled into a new procedural memory entry. LLM-based systems are only beginning to replicate this, with Structured Reflection ([arXiv:2509.18847](https://arxiv.org/abs/2509.18847)) baking error patterns into model weights via RL rather than external memory.

**The deeper issue** (flagged by [arXiv:2604.27707](https://arxiv.org/abs/2604.27707)): all current external memory is *C-compression* (context engineering) rather than *θ-compression* (weight updates). A Reflexion agent accumulates verbal self-critiques but runs the same frozen model weights; MemGPT pages in prior experiences but the model cannot generalize across them. True residual-error learning — where the agent's *capacity* for a domain improves because it has seen its own failures — requires either fine-tuning on error trajectories or formal chunking-style rule induction. This is the gap that NanoResearch's SDPO layer begins to address.

**Implication for Paper 3:** A complete memory substrate for LLM reliability should implement at minimum: (a) a failure-triggered write policy that stores the error trace alongside the correction, (b) retrieval that surfaces prior failures when entering similar contexts, and (c) a governance layer that prevents false memories (themselves a form of residual error) from persisting uncorrected. Only the Governed Collaborative Memory framework ([arXiv:2605.04264](https://arxiv.org/abs/2605.04264)) currently articulates all three as design requirements.

---

## 5. Versioned / Governed Memory: Rare but Important

| System | Governance Feature | Type |
|--------|--------------------|------|
| **SSGM** (arXiv:2603.11768) | Consistency verification + temporal decay + dynamic access control | Conceptual framework |
| **Governed Collaborative Memory** (arXiv:2605.04264) | 4 governance regimes, provenance/version lineage, archive layer, correction pathways | Design agenda + empirical traces |
| **Oracle AI Agent Memory** | Multi-tenant isolation, audit, encryption, governance at store layer; LongMemEval 93.8% | Production enterprise product |
| **ChatGPT Memory** | Admin on/off, user delete, 30-day log retention | Consumer controls (limited) |
| **Cognee** | Dataset-level permissions (read/write/delete/share), multi-tenant isolation | Open-source framework |
| **Galileo / Redis analysis** | Identifies versioned memory stores as a defense against memory corruption attacks | Practitioner guidance |

**Key gap:** No major open-source research system (Reflexion, MemGPT, Generative Agents, A-MEM) implements versioning or provenance tracking. This is a production concern, not a research concern — and it maps directly to the patch-plasticity rubric's highest tier (score 5).

---

## 6. Sources Index

| # | Citation | URL |
|---|----------|-----|
| S1 | Shinn et al. (NeurIPS 2023) — Reflexion | https://arxiv.org/abs/2303.11366 |
| S2 | Packer et al. (2023) — MemGPT | https://arxiv.org/abs/2310.08560 |
| S3 | Park et al. (ACM CHI 2023) — Generative Agents | https://arxiv.org/abs/2304.03442 |
| S4 | Xu et al. (NeurIPS 2025) — A-MEM | https://arxiv.org/abs/2502.12110 |
| S5 | Chhikara et al. (2025) — Mem0 | https://arxiv.org/abs/2504.19413 |
| S6 | Mem0 Docs — Memory Evaluation | https://docs.mem0.ai/core-concepts/memory-evaluation |
| S7 | Rasmussen et al. (2025) — Zep/Graphiti | https://arxiv.org/abs/2501.13956 |
| S8 | Zep Docs — Sessions | https://help.getzep.com/v2/sessions |
| S9 | LangGraph Memory Docs | https://docs.langchain.com/oss/python/concepts/memory |
| S10 | LangChain Blog — Long-Term Memory Launch | https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph |
| S11 | Wang et al. (2023) — Voyager | https://arxiv.org/abs/2305.16291 |
| S12 | OpenAI — Memory FAQ | https://help.openai.com/en/articles/8590148-memory-faq |
| S13 | Anthropic — Claude Code Memory | https://code.claude.com/docs/en/memory |
| S14 | Google — Gemini Code Assist Memory | https://cloud.google.com/blog/products/ai-machine-learning/memory-for-ai-code-reviews-using-gemini-code-assist |
| S15 | Cognee — How Cognee Builds AI Memory | https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory |
| S16 | Gutiérrez et al. (2024) — HippoRAG | https://arxiv.org/abs/2405.14831 |
| S17 | Wang & Chen (2025) — MIRIX | https://arxiv.org/abs/2507.07957 |
| S18 | Soar Cognitive Architecture | https://en.wikipedia.org/wiki/Soar_(cognitive_architecture) |
| S19 | Cuadros et al. (2026) — Governed Collaborative Memory | https://arxiv.org/abs/2605.04264 |
| S20 | Lam et al. (2026) — SSGM | https://arxiv.org/abs/2603.11768 |
| S21 | Xu et al. (2026) — NanoResearch | https://arxiv.org/abs/2605.10813 |
| S22 | Zhong et al. (2023) — MemoryBank | https://arxiv.org/abs/2305.10250 |
| S23 | Wu et al. (2024) — LongMemEval | https://github.com/xiaowu0162/LongMemEval |
| S24 | LongMemEval-V2 (2026) | https://arxiv.org/abs/2605.12493 |
| S25 | Maharana et al. (ACL 2024) — LoCoMo | https://arxiv.org/abs/2402.17753 |
| S26 | MemoryAgentBench (arXiv 2026) | https://arxiv.org/abs/2507.05257 |
| S27 | Su et al. (2025) — Failure Makes the Agent Stronger | https://arxiv.org/abs/2509.18847 |
| S28 | Xu et al. (2026) — Contextual Agentic Memory Is a Memo | https://arxiv.org/abs/2604.27707 |
| S29 | CoALA — Cognitive Architectures for Language Agents | https://arxiv.org/abs/2309.02427 |
| S30 | Oracle AI Agent Memory Blog | https://blogs.oracle.com/developers/oracle-ai-agent-memory-a-governed-unified-memory-core-for-enterprise-ai-agents |
