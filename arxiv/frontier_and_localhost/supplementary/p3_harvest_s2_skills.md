# P3 Harvest — Substrate 2: Skill Libraries
*Paper 3 of a trilogy on LLM reliability. Compiled: 2025.*

---

## Patch-Plasticity Rubric (0–5)

| Score | Meaning |
|-------|---------|
| **0** | Static prompt — no procedural library, skills baked into system prompt at authoring time |
| **1** | Structured assets stored externally, but always loaded eagerly (no selective loading) |
| **2** | Dynamic discovery: skills loaded on demand from metadata/description matching; no agent-initiated modification |
| **3** | Dynamic loading + agent can trigger skill updates or additions (human-in-loop or explicit instruction) |
| **4** | Agent autonomously generates new skills from experience and verifies/saves them to library |
| **5** | Two-loop versioned promotion: agent generates → verifies → promotes to versioned library; RL or feedback signal drives skill refinement across episodes |

---

## Scored Summary Table

| # | System | Score | Skill Format | Loading Mechanism | Self-Modifying | Verifiers/Tests | Benchmark Gain |
|---|--------|-------|-------------|-------------------|----------------|-----------------|---------------|
| 1 | **Anthropic Claude Agent Skills** (claude.ai, Claude API) | **3** | SKILL.md (YAML frontmatter + markdown + scripts/) | Progressive disclosure (3 levels) | User-directed; future autonomous planned | scripts/validate.*, examples/ | None published |
| 2 | **Claude Code Skills** | **3** | SKILL.md + scripts/ + examples/ + references/ | Progressive disclosure; file-system watch; live reload | User-directed; file edits detected live | scripts/ (validate.sh, helper.py) | LangChain Skills: 29%→95% pass rate |
| 3 | **Anthropic/skills GitHub repo** | **2** | SKILL.md + Python/HTML/Shell scripts; plugin manifest | Installed as plugin packages (eager per session) | Static repo; PR-based modification | spec/ folder; implicit via scripts | None published |
| 4 | **Voyager** (Wang et al., NeurIPS 2023) | **4** | Executable JavaScript; embedding-indexed library | RAG-style: top-5 skills retrieved by embedding similarity | Agent generates, verifies, saves autonomously | Environment execution + self-verification loop | 3.3× items, 15.3× tech tree speed, 63 unique items |
| 5 | **NanoResearch Skill Bank** (arXiv:2605.10813) | **4** | Compact procedural rules (natural language) | Heuristic scoring (keyword match + tag alignment + recency) | Orchestrator distills recurring ops into bank after each stage | Implicit: skills only promoted on successful execution | Innovation score 4.96→5.65, Compliance 6.66→8.96 |
| 6 | **SAGE** (arXiv:2512.17102) | **5** | Python functions (executable code) | Embedding-based retrieval (all-MiniLM-L6-v2 / Qwen3-Embedding) | RL-driven: skill generation + update on error + RL reward signal | Execution verification; -1.0 penalty for no-code responses | +8.9% SGC, 26% fewer steps, 59% fewer tokens on AppWorld |
| 7 | **Microsoft Semantic Kernel Plugins** (formerly "Skills") | **2** | Native code (C#/Python/Java) + OpenAPI spec + MCP server | Eager registration via kernel.add_plugin(); LLM selects via function calling | No self-modification; code changes require developer | OpenAI: ≤10 tools recommended (perf degrades >10) | None specific to SK; OpenAI: accuracy drop 10–20 tools |
| 8 | **CrewAI Skills** | **2** | SKILL.md (YAML frontmatter + markdown body) | discover_skills() + activate_skill(); two-stage discovery/activation | Static files; no agent self-modification | None explicit; 50k char soft cap | None published |
| 9 | **LangChain Skills** | **2** | Markdown + scripts (SKILL.md-compatible) | Progressive disclosure (identical to ACS spec) | Static; managed via npx skills CLI | None explicit | 29% → 95% pass rate on internal LangSmith eval (Claude Code + Sonnet 4.6) |
| 10 | **HuggingFace Agent Skills** | **2** | SKILL.md + helper scripts | Manual install via /plugin marketplace add; mention-triggered load | Static; contrib via GitHub PR | None explicit | None published |
| 11 | **OpenAI Custom GPTs / Actions** | **2** | OpenAPI spec (JSON/YAML) + ai-plugin.json manifest + system instructions | Eager load per GPT instance; no dynamic selection at runtime | No; developer must update via GPT Builder UI | None | None published |
| 12 | **ChatGPT Plugins** (legacy, 2023) | **1** | ai-plugin.json manifest + openapi.yaml (hosted at /.well-known/) | All enabled plugins loaded at session start (no selective loading) | No | No | None (deprecated 2024) |
| 13 | **MetaGPT** (arXiv:2308.00352) | **3** | Role-based SOPs encoded as structured prompts + executable feedback | Eager per role; Engineer iterates with executable feedback (≤3 retries) | Agent reruns tests, debugs autonomously within a session | Unit tests written and executed by QA Engineer agent | +4.2% HumanEval Pass@1, +5.4% MBPP Pass@1 |
| 14 | **SuperAGI Toolkits** | **1** | Python tool classes in GitHub repos; manifest via config.yaml | Toolkit installed at agent config time; all tools eager-loaded | No; requires developer to push code | No | None published |
| 15 | **AgentVerse** (arXiv:2308.10848) | **1** | Agent roles with fixed capabilities; no separate skill files | Fixed at team composition time; dynamic team resizing but not skill loading | No skill library; team composition changes | No | None for skills specifically |
| 16 | **COSPLAY** (arXiv:2604.20987) | **5** | Skills with contracts extracted from unlabeled rollouts | LLM-based decision agent retrieves skills from learnable bank | Skill bank agent continually extracts, refines, updates; boundary proposal + segmentation | Contract learning validates skill utility | Reported gains on long-horizon game environments |

---

## Per-System Entries

---

### 1. Anthropic Claude Agent Skills

**Sources:** [Anthropic Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) · [Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [agentskills.io spec](https://agentskills.io/home)

**Overview.** Announced December 2025. Agent Skills is Anthropic's formal name for the SKILL.md-based format it designed. The spec is now open (agentskills.io) and adopted by CrewAI, LangChain, HuggingFace, and others.

**Skill Format / File Structure:**
```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + markdown body
├── scripts/          # Optional: Python, Bash, JS executables
├── references/       # Optional: long supporting docs (loaded lazily)
└── assets/           # Optional: templates, schemas, data files
```
SKILL.md YAML frontmatter:
```yaml
---
name: pdf-processing           # required; 1–64 chars
description: >-                # required; 1–1536 chars (Claude Code)
  Extract text and tables from PDF files. Use when the user
  provides a PDF or asks to process document content.
allowed-tools: bash python     # optional; experimental
---
# PDF Processing
Instructions here in markdown...
```

**Loading Mechanism — Three-Level Progressive Disclosure:**
| Level | Content | Token Cost | When |
|-------|---------|-----------|------|
| 1: Metadata | name + description only | ~100 tokens/skill | Startup (always) |
| 2: Instructions | Full SKILL.md body | ≤5k tokens | When task matches skill |
| 3+: Resources/Code | scripts/, references/ files | Effectively unlimited (bash, no context cost) | When SKILL.md references them |

Claude uses `bash` tool calls to read SKILL.md from the filesystem — the progressive disclosure mechanism is literally Claude deciding whether to execute `cat skill-name/SKILL.md`. Scripts are run via bash without ever loading their source into context, which is a key efficiency.

**Dynamic Discovery:** At startup, only `name` + `description` from frontmatter enter the system prompt (~30–50 tokens per skill). For 50 installed skills, startup overhead is ~1,500–2,500 tokens. Skill files are watched for live changes (Claude Code); changes take effect within the current session without restart.

**Self-Modification:** Currently user-directed: a user can ask Claude to "capture successful approaches and common mistakes into the skill." Anthropic has stated the future goal is for agents to "create, edit, and evaluate Skills on their own."

**Verifiers/Tests:** The `scripts/` directory explicitly supports validation scripts (e.g., `scripts/validate.sh`). An `examples/` directory provides expected output formats. No formal test harness mandated by the spec.

**Platforms:** claude.ai, Claude Code, Claude Agent SDK, Developer Platform.

**Patch-Plasticity Score: 3/5.** Structured reusable format ✓. On-demand loading ✓. Distinguishes skills from raw instructions ✓. Agent-initiated modification: user-directed only (not autonomous). No RL signal. No versioning mechanism.

---

### 2. Claude Code Skills

**Sources:** [Claude Code Docs](https://code.claude.com/docs/en/skills) · [Firecrawl explainer](https://www.firecrawl.dev/blog/agent-skills) · [Vercel FAQ](https://vercel.com/blog/agent-skills-explained-an-faq)

**Overview.** Claude Code's implementation of Agent Skills has the most fully-specified format in the ecosystem, with additional frontmatter fields for subagent control, model override, effort level, hooks, path filters, and shell selection.

**Extended Frontmatter Fields (beyond base spec):**
| Field | Purpose |
|-------|---------|
| `when_to_use` | Additional trigger phrases (appended to description) |
| `argument-hint` | Autocomplete hint (e.g., `[filename]`) |
| `arguments` | Named positional arguments for `$name` substitution |
| `disable-model-invocation` | Prevent automatic triggering; manual `/skill-name` only |
| `allowed-tools` | Tools permitted without asking permission during skill |
| `model` | Model override for skill's duration |
| `effort` | Effort level override (low/medium/high/xhigh/max) |
| `context: fork` | Run skill in forked subagent context |
| `hooks` | Lifecycle hooks scoped to skill |
| `paths` | Glob patterns for auto-activation |
| `shell` | bash or powershell |

**Dynamic Context Injection:**
- Inline: `` !`command` `` — shell command output injected before Claude sees the skill
- Block: ` ```!` `` — multi-line command output
- Variable substitution: `$ARGUMENTS`, `$ARGUMENTS[N]`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_SKILL_DIR}`

**Discovery Hierarchy:** Enterprise > Personal (`~/.claude/skills/`) > Project (`.claude/skills/`) > Plugin. Nested `.claude/skills/` in subdirectories discovered on demand.

**Loading with Auto-compaction:** After context summarization, Claude re-attaches up to 5,000 tokens per skill and 25,000 tokens total for all active skills.

**Self-Modification:** File changes detected live; user can edit SKILL.md during a session and changes apply. Claude Code does not autonomously write to SKILL.md files.

**Benchmark Evidence:** LangChain's Skills (using Claude Code) showed pass rate improvement from **29% → 95%** on LangSmith evaluations. This is the strongest productivity benchmark published for the SKILL.md format.

**Patch-Plasticity Score: 3/5.** Identical to Claude Agent Skills in capability score. Richer frontmatter spec and live reload add operational plasticity but not autonomous self-modification.

---

### 3. Anthropic/skills GitHub Repository

**Sources:** [github.com/anthropics/skills](https://github.com/anthropics/skills) (public repo, September 2025)

**Overview.** Official repository of pre-built skills covering document processing, creative/design, development, enterprise, and personal automation domains.

**Repository Structure:**
```
skills/
├── docx/            # Word document creation/editing
├── pdf/             # PDF processing
├── pptx/            # PowerPoint creation
├── xlsx/            # Excel manipulation
├── claude-api/      # Claude API patterns
├── template/        # Starter template for skill authors
└── spec/            # Agent Skills Specification (agentskills.io source)

.claude-plugin/      # Plugin metadata for plugin collections
```

**Plugin Collections:** Skills are grouped into installable plugin bundles: `anthropic-agent-skills`, `document-skills`, `example-skills`. This is the distribution mechanism for curated skill sets.

**Script Languages:** Python (84.4%), HTML (12.4%), Shell (1.9%), JavaScript (1.3%). Document skills (xlsx, pptx, pdf) are the most script-heavy — they bundle openpyxl, python-pptx, and PDF processing libraries as executable tooling.

**Format Compliance:** SKILL.md with YAML frontmatter (name, description required). The `spec/` folder defines the canonical Agent Skills Specification.

**Self-Modification:** No. PR-based external contribution model.

**Patch-Plasticity Score: 2/5.** Well-structured, versioned via Git, distributed as installable plugins. Skills are static authored artifacts — no dynamic discovery beyond what the consuming platform provides, no agent-driven modification.

---

### 4. Voyager (Wang et al., 2023)

**Sources:** [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) · [voyager.minedojo.org](https://voyager.minedojo.org) · [github.com/MineDojo/Voyager](https://github.com/MineDojo/Voyager)

**Overview.** *The* foundational academic case study for autonomous skill library accumulation. Voyager is an LLM-powered Minecraft agent that grows a library of executable JavaScript skills without any parameter fine-tuning. Published NeurIPS 2023.

**Skill Format:**
- **Language:** JavaScript (Mineflayer API)
- **Characteristics:** Temporally extended, interpretable, compositional
- **Storage:** Indexed by text embedding of skill description; library directory on filesystem (e.g., `./skill_library/trial1/`)
- **Retrieval:** Top-5 skills retrieved by embedding similarity to current task query

**Three Core Components:**
1. **Automatic Curriculum** — GPT-4 proposes exploration tasks appropriate to current capability level
2. **Skill Library** — ever-growing store of executable JavaScript programs; compositional (new skills build on existing ones)
3. **Iterative Prompting Mechanism** — generates skill code → executes in Minecraft → receives (a) environment feedback, (b) execution errors, (c) self-verification result → revises until passing or max retries

**Self-Verification Loop (the key mechanism):**
```
GPT-4 generates JavaScript skill → Execute in Minecraft → 
  If pass: save to skill library (embedding indexed)
  If fail: include error + env feedback → GPT-4 revises → repeat
```
This is fully autonomous: no human in the loop for skill generation or validation.

**Benchmark Results:**

| Metric | Voyager | Prior SOTA | Multiplier |
|--------|---------|-----------|-----------|
| Unique items obtained (160 iterations) | 63 | ~19 | **3.3×** |
| Distance traveled | — | baseline | **2.3×** |
| Wooden tool milestone | — | — | **15.3× faster** |
| Stone tool milestone | — | — | **8.5× faster** |
| Iron tool milestone | — | — | **6.4× faster** |
| Diamond tool milestone | ✓ (only Voyager) | ✗ (no baseline reached) | **∞** |

**Zero-Shot Generalization (New World Seeds):**
- Setup: inventory cleared, fresh world, novel tasks
- Voyager: **solved all tasks** using the transferred skill library
- AutoGPT, ReAct, Reflexion: **could not solve any tasks** within 50 prompting iterations
- Cross-framework test: Voyager's skill library, used as plug-and-play by AutoGPT, improved AutoGPT's performance — demonstrating library portability

**Ablation:** GPT-4 significantly outperforms GPT-3.5 for skill code generation; all three components (curriculum, library, iterative prompting) are individually necessary.

**Skill Library Growth:** Skills accumulate compositionally — navigating to a biome becomes a reusable primitive for crafting tasks; crafting becomes a primitive for combat tasks. This compounding is what drives the superlinear gains.

**Why This Matters for Paper 3:** Voyager bypasses fine-tuning entirely — all behavioral plasticity is captured in the skill library. It is the strongest empirical argument that a skill library is a viable alternative to weight updates for long-horizon capability accumulation.

**Patch-Plasticity Score: 4/5.** Autonomous generation ✓. Execution verification ✓. Embedding-based retrieval ✓. Compositional growth ✓. Missing: versioning (skills are saved but not versioned/promoted with explicit version control), no explicit RL reward signal back-propagated to skill generation (the iterative refinement is local to each skill, not across-episode RL). Loses one point vs. SAGE/COSPLAY on this axis.

---

### 5. NanoResearch Skill Bank (Xu et al., 2026)

**Sources:** [arXiv:2605.10813](https://arxiv.org/abs/2605.10813) · [arXiv HTML](https://arxiv.org/html/2605.10813v1)

**Overview.** A multi-agent research automation framework. The skill bank is one of three co-evolving components (alongside a memory module and a policy learning layer). Published May 2026.

**Skill Format:** Compact procedural rules — condensed natural language descriptions of recurring operations. Examples: debugging strategies, formatting patterns, experiment workflow steps. Not executable code.

**Skill Bank Growth Across Rounds:**
| Round | Skill Bank Size / Topic | Memory Size / Topic | New Skills / Topic |
|-------|------------------------|---------------------|--------------------|
| R1 | 0.80 | 6.40 | 0.80 |
| R2 | 1.00 | 8.15 | 0.20 |
| R3 | 2.30 | 12.00 | 1.30 |

**Retrieval Mechanism:** Heuristic scoring function combining:
- Keyword matching
- Tag alignment
- Recency weighting
- Usage frequency and confidence (for skills — surfaces robust strategies)
- Strict condition matching (for memories — project-specific)

Top-k skills retrieved before each task stage; both stores updated after each stage via trajectory reflection.

**Co-Evolution Loop:**
```
Skills → produce richer memory
Memory → informs better planning
Policy (SDPO) → internalizes user preferences → realigns the loop
```
The Orchestrator O drives continuous evolution: retrieves `S_C` (relevant skills) and `M_C` (relevant memories) before each task, then after task completion, reflects over trajectory τ and distills generalizable rules into `S` and project-specific experiences into `M`.

**Benchmark Results:**
| Metric | NanoResearch (R3) | Baseline (R1) | Gain |
|--------|-------------------|---------------|------|
| Innovation score | 5.645 | 4.960 | +13.8% |
| Expression score | 6.172 | 5.428 | +13.7% |
| Compliance score | 8.963 | 6.656 | +34.7% |
| Cost | lower per cycle | baseline | decreasing |

Full system outperforms all partial variants; Skill Bank and Memory Module are complementary and individually necessary.

**Patch-Plasticity Score: 4/5.** Autonomous skill distillation ✓. Cross-project reuse ✓. Multi-round growth ✓. Skills are natural language rules (not executable code — lowers reliability of execution). No formal versioning or explicit promotion protocol. The RL-like feedback (SDPO) operates on the policy, not the skill bank directly.

---

### 6. SAGE — Skill Augmented GRPO for self-Evolution (2025)

**Sources:** [arXiv:2512.17102](https://arxiv.org/abs/2512.17102) · [arXiv HTML v2](https://arxiv.org/html/2512.17102v2)

**Overview.** SAGE is an RL framework that explicitly integrates a skill library into the GRPO (Group Relative Policy Optimization) training loop. It is the strongest existing system on the patch-plasticity rubric because skill generation, verification, and use are all part of the RL reward signal.

**Skill Format:** Python functions. Each skill wraps multiple API calls with programming constructs (for loops, conditionals). The agent generates a skill function and immediately calls it — a unified generate-then-execute pattern.

**Skill Lifecycle (Four Actions):**
1. **Skill Usage** — retrieve `a_i` from library, use directly
2. **Skill Generation** — define new `â` composed of multiple actions, call immediately
3. **Skill Update** — if `a` fails to execute, revise and re-call
4. **Skill Save** — if `â` executes without error, persist to library `M`

**Retrieval Methods Evaluated:**
| Method | Mechanism | Threshold |
|--------|-----------|-----------|
| Same Scenario | Scenario labels (oracle) | — |
| Query N-gram | 2-gram Jaccard similarity | 0.5 |
| Query Embedding | all-MiniLM-L6-v2 cosine | 0.65 |
| Skill Embedding | Qwen3-Embedding-0.6B top-5 | — |

**Sequential Rollout (Key Innovation):** Agent is trained across chains of 2 similar tasks. Skills generated in task 1 are available in task 2. The RL reward from successful skill reuse in task 2 is back-propagated to the skill generation decisions in task 1. This closes the cross-episode feedback loop.

**AppWorld Benchmark Results:**
| Method | Test Normal SGC (%) | Test Normal TGC (%) | Avg Steps | Avg Tokens |
|--------|--------------------|--------------------|-----------|-----------|
| **SAGE (Qwen2.5-32B)** | **60.7 ± 1.5** | **72.0 ± 1.5** | **12.1** | **1,475** |
| GRPO (baseline) | 51.8 ± 5.8 | 69.2 ± 2.7 | 16.4 | 3,613 |
| LOOP | 53.6 ± 2.2 | 71.3 ± 1.3 | — | — |
| Claude Sonnet 3.5 V2 | 41.1 | 57.1 | 15.7 | 1,542 |
| OpenAI o1 | 41.1 | 61.9 | — | — |
| GPT-4o | 32.1 | 48.8 | — | — |
| SFT (prior to SAGE) | 41.7 ± 1.7 | 55.2 ± 1.5 | 11.4 | 1,340 |

**Key Gains over GRPO baseline:** +8.9% SGC, 26% fewer interaction steps, 59% fewer tokens. Skill utilization: >2× success rate when using learned skills.

**Patch-Plasticity Score: 5/5.** Autonomous skill generation ✓. Execution verification (error-triggered update) ✓. RL reward signal back-propagated through skill generation ✓. Cross-episode accumulation ✓. Multiple retrieval strategies evaluated ✓. Missing only a formal versioning system with named versions — but the RL-driven refinement loop is functionally equivalent.

---

### 7. Microsoft Semantic Kernel Plugins (formerly "Skills")

**Sources:** [MS Docs: Plugins](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/) · [Devblog: Skills → Plugins](https://devblogs.microsoft.com/agent-framework/skills-to-plugins-fully-embracing-the-openai-plugin-spec-in-semantic-kernel/)

**Overview.** Semantic Kernel (SK) is Microsoft's open-source SDK for LLM-based applications. It coined "Skills" in 2023 to describe units of agent capability; these were renamed "Plugins" in late 2023/early 2024 to align with the OpenAI plugin spec.

**Historical Context:** The original "Skills" in SK were native code functions decorated with `[KernelFunction]` annotations. They were functionally similar to what OpenAI called "plugins" — the name change was prompted by OpenAI's ChatGPT plugin ecosystem establishing "plugin" as the dominant term.

**Current Plugin Format (three authoring modes):**
1. **Native Code** — C#/Python/Java class with `[KernelFunction("name")]` + `[Description("...")]` annotations
2. **OpenAPI Specification** — standard OpenAPI YAML/JSON; cross-language portable
3. **MCP Server** — Model Context Protocol server import

**C# Example:**
```csharp
[KernelFunction("get_weather")]
[Description("Gets current weather for a city")]
public async Task<string> GetWeatherAsync(
    [Description("The city name")] string city)
{ ... }
```
Added to kernel: `kernel.Plugins.AddFromType<WeatherPlugin>("Weather")`

**Loading Mechanism:** Eager registration at `kernel.Plugins.AddFromType<T>()`. The LLM selects which plugin functions to call via `FunctionChoiceBehavior.Auto()`. There is no progressive disclosure — all registered plugins are available to the LLM at every turn.

**Performance Note:** OpenAI recommends ≤10 tools per API call; accuracy degrades between 10–20 tools. SK does not implement automatic context-aware filtering.

**Self-Modification:** None. Plugins are authored by developers; runtime behavior is fixed.

**Relationship to Substrate 2:** SK Plugins are the canonical enterprise example of skills-as-code. They predate the SKILL.md format and represent a different design philosophy: tight code coupling vs. the file-system-native, markdown-first approach of SKILL.md.

**Patch-Plasticity Score: 2/5.** Structured reusable code format ✓. Distinguishes from raw prompts ✓. Loading is eager (not on-demand) ✗. No self-modification ✗. No examples/verifiers in the skill format ✗.

---

### 8. CrewAI Skills

**Sources:** [docs.crewai.com/concepts/skills](https://docs.crewai.com/en/concepts/skills) · [docs.crewai.com/skills](https://docs.crewai.com/en/skills)

**Overview.** CrewAI adopted the SKILL.md format (Agent Skills Spec) and explicitly distinguishes skills from tools in its documentation: **Skills inject instructions into the agent prompt; Tools give agents callable functions.** This is an important taxonomy contribution.

**Skill Format (SKILL.md spec-compliant):**
```
skill-name/
├── SKILL.md          # YAML frontmatter + markdown instructions
├── scripts/          # Optional executable scripts
├── references/       # Optional reference documents
└── assets/           # Optional static files
```
Frontmatter fields: `name` (required), `description` (required), `license`, `compatibility`, `metadata`, `allowed-tools`.

**Loading API:**
```python
from crewai.skills import discover_skills, activate_skill
skills = discover_skills(Path("./skills"))  # loads metadata only
activated = [activate_skill(s) for s in skills]  # loads full body
agent = Agent(role="Researcher", skills=activated, ...)
```
Two-stage: `discover_skills()` → loads name/description; `activate_skill()` → loads full SKILL.md body.

**Crew-wide vs. Agent-level:**
```python
crew = Crew(agents=[...], tasks=[...], skills=["./skills"])  # all agents
```

**Skills vs. Knowledge (CrewAI's taxonomy):**
| Aspect | Skills | Knowledge |
|--------|--------|-----------|
| Provides | Instructions, procedures, guidelines | Facts, data, information |
| Stored as | SKILL.md files | Vector store (ChromaDB) |
| Retrieved by | Full body injection | Semantic search chunks |
| Best for | Methodology, checklists, style guides | Company docs, reference data |

**Self-Modification:** None. Skills are static authored files.

**Patch-Plasticity Score: 2/5.** Implements SKILL.md spec with two-stage discovery/activation. Explicit taxonomy distinction (skills ≠ tools ≠ knowledge) is valuable. No autonomous generation or RL feedback.

---

### 9. LangChain Skills

**Sources:** [langchain.com/blog/langchain-skills](https://www.langchain.com/blog/langchain-skills) · [docs.langchain.com/oss/python/langchain/multi-agent/skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills)

**Overview.** Released April 2026. LangChain's 11 skills cover LangChain, LangGraph, and Deep Agents primitives — essentially a curated expert knowledge base for LangChain's own APIs. The skills are distributed via npm (`npx skills add langchain-ai/langchain-skills`).

**Format:** SKILL.md-compatible (markdown + scripts). LangChain's primary innovation is the performance benchmark data showing progressive disclosure matters:

> "Historically, giving too many tools to an agent would cause its performance to degrade. Skills mitigate this through the progressive disclosure mechanism."

**Benchmark (most explicit published data for the SKILL.md format):**
| Condition | Model | Pass Rate |
|-----------|-------|-----------|
| Without Skills | Claude Sonnet 4.6 (Claude Code) | 25–29% |
| With LangChain Skills | Claude Sonnet 4.6 (Claude Code) | **95%** |

Evaluated via LangSmith on internal LangChain/LangGraph coding tasks.

**Dynamic Tool Registration Pattern** (LangChain agents):
```python
@tool
def load_skill(skill_name: str) -> str:
    """Load a specialized skill prompt. Available: write_sql, review_legal_doc"""
    # Returns skill content + registers skill-specific tools
    ...
```
LangChain's middleware architecture also supports runtime tool addition, though with constraints (tools must be pre-registered or handled in `wrap_tool_call`).

**Patch-Plasticity Score: 2/5.** Best published benchmark for SKILL.md format. Same static-file limitation as other SKILL.md consumers.

---

### 10. HuggingFace Agent Skills

**Sources:** [huggingface.co/docs/hub/agents-skills](https://huggingface.co/docs/hub/agents-skills) · [github.com/huggingface/skills](https://github.com/huggingface/skills)

**Overview.** HuggingFace maintains a curated set of SKILL.md-based skills for ML/AI tasks: model training, dataset creation, evaluation, experiment tracking, paper publishing. Cross-agent-compatible: works with Claude Code, OpenAI Codex, Gemini CLI, Cursor.

**Available Skills:**
| Skill | Capability |
|-------|-----------|
| `hf-cli` | Hub ops: download, upload, manage repos, run jobs |
| `huggingface-llm-trainer` | Train/fine-tune LLMs with TRL (SFT, DPO, GRPO) |
| `huggingface-vision-trainer` | Object detection, image classification |
| `huggingface-community-evals` | Evaluations on HF Hub hardware |
| `huggingface-datasets` | Explore, paginate, search, filter datasets |
| `huggingface-trackio` | Track/visualize ML experiments |
| `huggingface-papers` | Read HF paper pages |
| `huggingface-paper-publisher` | Publish/manage research papers |
| `huggingface-tool-builder` | Build reusable HF API scripts |
| `gradio` | Build Gradio UIs/demos |
| `transformers-js` | ML models in JavaScript/WebGPU/WASM |

**Installation:** `/plugin marketplace add huggingface/skills` → `/plugin install <skill-name>@huggingface/skills`

**Note on Terminology:** HuggingFace explicitly acknowledges that "'Skills' is actually an Anthropic term" — HF adopted it because of its intuitive clarity for the SKILL.md format.

**Patch-Plasticity Score: 2/5.** Strong domain coverage for ML tasks. Static curated library. No agent self-modification. Note: HuggingFace's smolagents library (transformed agents) is a separate system with its own tool format.

---

### 11. OpenAI Custom GPTs / Actions

**Sources:** [developers.openai.com/api/docs/actions/introduction](https://developers.openai.com/api/docs/actions/introduction) · [developers.openai.com/api/docs/actions/actions-library](https://developers.openai.com/api/docs/actions/actions-library)

**Overview.** Custom GPTs (launched November 2023) allow users to combine: (1) custom system instructions, (2) uploaded knowledge files, and (3) GPT Actions (API connections via OpenAPI spec). GPT Actions are the skill-library analogue — they extend what the GPT can do by calling external REST APIs.

**Format:**
- **Instructions:** Free-text system prompt (no structured format)
- **Knowledge:** Uploaded files (RAG-style retrieval)
- **Actions (the skill layer):** OpenAPI spec (JSON or YAML, max 1MB, ≤30 operations) + authentication config

**GPT Action Manifest:**
```json
{
  "name_for_human": "Weather Tool",
  "name_for_model": "weather",
  "description_for_human": "Get current weather",
  "description_for_model": "Retrieve weather data for a location",
  "auth": {"type": "none"},
  "api": {"type": "openapi", "url": "https://api.example.com/openapi.yaml"},
  "logo_url": "https://example.com/logo.png"
}
```

**Loading Mechanism:** All configured Actions are available at every turn within a GPT session — no progressive disclosure, no dynamic selection beyond LLM function calling.

**Limitations vs. SKILL.md:**
- No file-system-native format; Actions live in the GPT Builder UI
- No scripts bundled with the skill
- No versioning beyond manual re-upload
- OpenAPI size cap: 1MB, 30 operations

**Self-Modification:** None. Changes require developer access to GPT Builder.

**Patch-Plasticity Score: 2/5.** GPT Actions represent the commercial deployment of the plugin concept. They package API capability (not procedural knowledge) into a structured manifest. The lack of executable scripts, progressive loading, and self-modification limits them relative to SKILL.md-based systems.

---

### 12. ChatGPT Plugins (Legacy, 2023)

**Sources:** [OpenAI Plugin Documentation (archived)] · [github.com/fuegovic/Libre-Chat](https://github.com/fuegovic/Libre-Chat/blob/main/docs/features/plugins/chatgpt_plugins_openapi.md)

**Overview.** Launched March 2023, deprecated 2024. The ancestor of both GPT Actions and the broader "plugin" terminology adopted by Semantic Kernel and others. Three components: API, OpenAPI spec, ai-plugin.json manifest.

**Manifest format (ai-plugin.json):**
```json
{
  "schema_version": "v1",
  "name_for_human": "Todo List",
  "name_for_model": "todo",
  "description_for_human": "Manage your TODO list.",
  "description_for_model": "Help the user manage a TODO list.",
  "auth": {"type": "none"},
  "api": {"type": "openapi", "url": "https://example.com/openapi.yaml"},
  "logo_url": "...", "contact_email": "...", "legal_info_url": "..."
}
```

**Loading:** All enabled plugins loaded at session start — no selective/progressive loading.

**Historical Significance:** ChatGPT Plugins established the `name_for_model` / `description_for_model` pattern (semantic self-description for LLM function selection) that later informed both the SKILL.md `description` field and Semantic Kernel's function annotations. It also established the `/.well-known/ai-plugin.json` discovery convention.

**Patch-Plasticity Score: 1/5.** Foundational precedent but eager-loading, no scripts, no self-modification. Deprecated.

---

### 13. MetaGPT (Hong et al., 2023/2024)

**Sources:** [arXiv:2308.00352](https://arxiv.org/abs/2308.00352) · [arxiv.org/html/2308.00352v6](https://arxiv.org/html/2308.00352v6)

**Overview.** MetaGPT encodes Standardized Operating Procedures (SOPs) into role-based agent configurations. Each role (Product Manager, Architect, Project Manager, Engineer, QA Engineer) has a skill profile. Engineers use an executable feedback loop: generate code → run unit tests → debug → repeat (≤3 retries).

**"Skill" Format:** Role-defined capability profiles encoded in structured prompts. Not a separate file format; skills are embedded in role configuration:
- `name`, `profile`, `goal`, `constraints` per role
- Skill examples: Product Manager uses web search; Engineer uses code execution

**Executable Feedback Mechanism:**
```
Engineer generates code → runs unit tests (QA Engineer) →
  If pass: move to next task
  If fail: debug + re-run (max 3 retries)
```

**Benchmarks:**
- **HumanEval Pass@1:** +4.2% improvement with executable feedback
- **MBPP Pass@1:** +5.4% improvement with executable feedback
- **Feasibility score:** 3.67 → 3.75 with feedback
- **Human revision cost:** 2.25 → 0.83 revisions required

MetaGPT outperforms AutoGPT, LangChain, AgentVerse, and ChatDev on PRD generation, technical design, API interface generation, and precompilation execution capabilities.

**Self-Modification:** Within-session only. Engineers iteratively fix code within a session; skills (roles) are not updated across sessions.

**Patch-Plasticity Score: 3/5.** Role-based skills with executable feedback ✓. Agent performs within-session skill execution + verification ✓. No persistent skill library that grows across projects ✗. No RL signal ✗.

---

### 14. SuperAGI Toolkits

**Sources:** [web.superagi.com/docs/Core%20Components/Agents/](https://web.superagi.com/docs/Core%20Components/Agents/) · [datacamp.com/blog/superagi](https://www.datacamp.com/blog/superagi)

**Overview.** SuperAGI (2023) is one of the earliest open-source autonomous agent frameworks. "Toolkits" are the skill-layer equivalent — Python classes that group related tools, distributed via GitHub repos and installed into the agent.

**Format:** Python classes with `BaseTool` interface; toolkit manifests via `config.yaml`. Separate tool marketplace for discovery.

**Loading:** Toolkits are installed at agent configuration time and all tools are eager-loaded. ReAct-style execution: LLM thinks → selects tool → executes.

**Self-Modification:** None. Toolkit development requires writing Python code.

**Patch-Plasticity Score: 1/5.** Structured toolkits as a precursor to modern skill libraries. Eager-loading, no SKILL.md equivalent, no progressive disclosure, no self-modification.

---

### 15. AgentVerse (Chen et al., 2023)

**Sources:** [arXiv:2308.10848](https://arxiv.org/abs/2308.10848)

**Overview.** AgentVerse is a multi-agent collaboration framework. Its skill model is role-based: agents have fixed capabilities determined by their role assignment. No separate skill-file format exists — capability is encoded in the agent's role description and the framework's communication protocols.

**"Skill" Model:** Dynamic team composition (the framework can add/remove agents from a team), but individual agent capabilities are fixed at role assignment.

**Self-Modification:** None for skills.

**Relationship to Substrate 2:** AgentVerse does not have a skill library in the Substrate 2 sense. It is included here as a boundary case — team composition changes are a form of capability reconfiguration, but not procedural skill loading.

**Patch-Plasticity Score: 1/5.** No skill-file format, no dynamic loading of procedures, no self-modification.

---

### 16. COSPLAY — Co-Evolving LLM Decision and Skill Bank (2026)

**Sources:** [arXiv:2604.20987](https://arxiv.org/abs/2604.20987) · [wuxiyang1996.github.io/COSPLAY_page/](https://wuxiyang1996.github.io/COSPLAY_page/)

**Overview.** COSPLAY closes the skill-creation loop most completely among academic systems. Two agents co-evolve: a decision agent that retrieves and uses skills, and a skill bank agent that discovers, refines, and maintains skills from the decision agent's unlabeled rollouts.

**Skill Bank Pipeline:**
1. **Boundary Proposal** — identify skill-worthy segments in rollout trajectories
2. **Segmentation** — carve trajectory into candidate skills
3. **Contract Learning** — learn preconditions and postconditions for each skill
4. **Bank Curation** — maintain quality, deduplicate, version

**Co-evolution:** The decision agent's trajectories feed the skill bank agent. Improved skills feed back to improve the decision agent. This is a true two-agent closed loop.

**Retrieval:** LLM-based decision agent retrieves skills from the learnable bank to guide action selection.

**Benchmark:** Long-horizon gameplay environments (specific numbers reported in paper; gains demonstrated over non-skill baselines).

**Patch-Plasticity Score: 5/5.** Full two-loop co-evolution ✓. Automatic skill discovery from unlabeled rollouts ✓. Contract learning (verifiers/postconditions) ✓. Bank curation with versioning-like maintenance ✓. Autonomous operation ✓.

---

## Special Analysis: Skills vs. Instructions vs. Tools — Where Is the Boundary?

This taxonomy question is critical for Paper 3's conceptual architecture. Three substrates look similar but operate differently:

### The Core Distinction

| Dimension | Instructions (Substrate 1) | Skills (Substrate 2) | Tools (Substrate 3 / adjacent) |
|-----------|---------------------------|---------------------|-------------------------------|
| **Primary unit** | Free-text directive in system prompt | Structured, named, addressable procedural unit | Callable function or API endpoint |
| **Storage** | In-context (always loaded) | External file/library (loaded on demand) | External service/code (invoked on demand) |
| **Execution model** | LLM follows verbally | LLM follows + may run scripts; progressive load | LLM invokes; environment executes deterministically |
| **Authoring** | Written by human in natural language | Structured by human, may include scripts | Implemented in code |
| **Self-modification** | Rare; requires prompt engineering | Possible (SKILL.md files writable) | Rare (API endpoints are external) |
| **Context cost** | Fixed; always present | Variable; only loaded when relevant | Zero until invoked; only output enters context |
| **Versioning** | None (prompt snapshots only) | Git / manifest-tracked | API versioning |
| **Composability** | Via chaining prompts | Via SKILL.md references + script composition | Via function composition |

### The Hard Boundary Cases

**Case 1: CrewAI Skills vs. CrewAI Tools**
CrewAI's documentation makes the sharpest official distinction: "Skills inject *instructions and context* into the agent's prompt. Tools give the agent *callable functions* to take action." A skill tells the agent *how to think*; a tool gives the agent *something to do*. Both can reference scripts — but a skill's scripts are helper utilities bundled alongside instructions, while a tool's code *is* the capability.

**Case 2: Semantic Kernel Plugins vs. SKILL.md Skills**
Semantic Kernel Plugins are pure code — they have no markdown body, no progressive disclosure, and no instruction text. They are, by the Substrate 2 definition, closer to tools than skills. The original SK "Skills" included *semantic functions* (prompt templates) alongside *native functions* (code) — the semantic functions were skills in the Substrate 2 sense; the native functions were tools. The rename to "Plugins" collapsed this distinction.

**Case 3: Voyager JavaScript Skills vs. Tool Calls**
Voyager skills are executable JavaScript that the agent generates and stores. Are they skills or tools? Key distinction: (a) they are *generated by the agent*, not authored by humans; (b) they encode *compositional procedures* (multiple steps), not single actions; (c) they are *accumulated* in a library, not called as fixed endpoints. They meet the Substrate 2 criteria: reusable, discoverable, executable, agent-generated.

**Case 4: NanoResearch Skills vs. Memory**
NanoResearch's own taxonomy (skills vs. memory) is instructive. Skills = generalizable procedural rules reusable across projects. Memory = project-specific factual records from past runs. Both are retrieved dynamically; both grow over time. The difference is *generalizability* and *procedural vs. declarative* nature. Skills tell the agent *how* to do something; memory records *what happened*.

### Proposed Definitional Criteria for Substrate 2

A system qualifies as a **skill library** (Substrate 2) if it satisfies all four of:

1. **Structured storage** — Skills are stored as discrete, named, addressable units (files, database records, code objects) external to the active context window
2. **Dynamic loading** — Not all skills are loaded at startup; the agent or system selects which skills to load based on task relevance
3. **Procedural content** — Skills encode *how to do something* (procedures, workflows, code), not just *what to know* (facts) or *what to call* (API endpoints)
4. **Reuse across invocations** — The same skill can be used on multiple tasks, possibly by multiple agents, possibly in future sessions

**Boundary conditions:**
- A system prompt with a list of instructions → **Substrate 1** (not dynamic, not external)
- An API endpoint with a description → **Tool** (not procedural, not agent-authored)
- A RAG knowledge base → **Memory** (declarative, not procedural)
- A fine-tuned model weight → **Substrate 0** (not external, not loadable)
- A SKILL.md file loaded on demand → **Substrate 2** ✓
- A Voyager JavaScript skill → **Substrate 2** ✓
- A MetaGPT role SOP → **Borderline** (procedural but not dynamic-loaded; included as partial)

### The Progressive Disclosure Innovation

The most important architectural innovation in Substrate 2 is **progressive disclosure**: the observation that giving an LLM all available skills simultaneously degrades performance (LangChain's data: 29% vs. 95%), so skills should be loaded *on demand*. This requires:
- A **metadata layer** (name + description, ~30–100 tokens/skill) always loaded
- A **content layer** loaded only on trigger match
- An optional **resource layer** loaded only when referenced

This three-level architecture is now standardized in the Agent Skills Spec (agentskills.io) and implemented by Anthropic, CrewAI, LangChain, and HuggingFace in near-identical form.

The deeper implication: **progressive disclosure is to skill libraries what key-value caching is to KV stores** — it solves the context-window bottleneck without sacrificing capability breadth. A system with 50 skills installed costs ~2,000 tokens at startup (all names/descriptions) but can in principle hold as many procedures as the filesystem allows.

### What Distinguishes Academic Research Systems

Academic skill library systems (Voyager, SAGE, COSPLAY, NanoResearch) differ from production systems (Anthropic, LangChain, CrewAI) on one axis: **who authors the skills**.

In production systems, skills are authored by humans and curated into a library. The agent is a consumer.

In academic systems, the agent is a *producer* — it generates new skills from experience, verifies them, and adds them to the library. This is the key to the higher patch-plasticity scores (4–5 vs. 2–3) and is also the key to the stronger benchmark results: Voyager's skill accumulation compounds across episodes; SAGE's RL signal shapes skill quality across the training run.

Paper 3 should distinguish these two modes explicitly:
- **Curated skill libraries** (Substrate 2a): human-authored, structurally loaded on demand, static quality
- **Generative skill libraries** (Substrate 2b): agent-generated, accumulated across episodes, quality improves over time via verification or RL

---

## Source Reference Index

| System | Primary Source | URL |
|--------|---------------|-----|
| Anthropic Claude Agent Skills | Engineering blog | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| Claude Agent Skills API | Platform docs | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| Claude Code Skills | Code docs | https://code.claude.com/docs/en/skills |
| Anthropic/skills repo | GitHub | https://github.com/anthropics/skills |
| Agent Skills Spec | agentskills.io | https://agentskills.io/home |
| Voyager | arXiv | https://arxiv.org/abs/2305.16291 |
| Voyager project page | Website | https://voyager.minedojo.org |
| Voyager code | GitHub | https://github.com/minedojo/voyager |
| NanoResearch | arXiv | https://arxiv.org/abs/2605.10813 |
| NanoResearch HTML | arXiv | https://arxiv.org/html/2605.10813v1 |
| SAGE | arXiv | https://arxiv.org/abs/2512.17102 |
| SAGE HTML | arXiv | https://arxiv.org/html/2512.17102v2 |
| COSPLAY | arXiv | https://arxiv.org/abs/2604.20987 |
| COSPLAY page | GitHub Pages | https://wuxiyang1996.github.io/COSPLAY_page/ |
| Semantic Kernel Plugins | MS Docs | https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/ |
| SK Skills→Plugins rename | Devblog | https://devblogs.microsoft.com/agent-framework/skills-to-plugins-fully-embracing-the-openai-plugin-spec-in-semantic-kernel/ |
| CrewAI Skills | Docs | https://docs.crewai.com/en/concepts/skills |
| LangChain Skills blog | Blog | https://www.langchain.com/blog/langchain-skills |
| LangChain Skills docs | Docs | https://docs.langchain.com/oss/python/langchain/multi-agent/skills |
| HuggingFace Agent Skills | HF Docs | https://huggingface.co/docs/hub/agents-skills |
| HuggingFace/skills repo | GitHub | https://github.com/huggingface/skills |
| OpenAI GPT Actions | Docs | https://developers.openai.com/api/docs/actions/introduction |
| MetaGPT | arXiv | https://arxiv.org/abs/2308.00352 |
| AgentVerse | arXiv | https://arxiv.org/abs/2308.10848 |
| Firecrawl SKILL.md explainer | Blog | https://www.firecrawl.dev/blog/agent-skills |
| Vercel Agent Skills FAQ | Blog | https://vercel.com/blog/agent-skills-explained-an-faq |
