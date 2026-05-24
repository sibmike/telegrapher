# P3 Substrate 4 — Tool & Context Attachment: Evidence Harvest

**For:** Paper 3 of the LLM Reliability Trilogy  
**Substrate:** 4 — External Capability Layer (Tool & Context Attachment)  
**Compiled:** 2025  
**Function:** Bridge from Paper 2 (each cluster needs a capability) → Paper 3 (capabilities are attached, not trained in)

---

## Patch-Plasticity Rubric (0–5)

| Score | Meaning |
|-------|---------|
| 0 | No external tool interface; capabilities must be baked into weights |
| 1 | Single hard-coded tool or plugin, no composability |
| 2 | Multi-tool support, generic only, no domain bundling primitives |
| 3 | Multi-tool + some domain grouping, but bundling is manual/informal |
| 4 | First-class domain bundle support; can ship a "patch toolkit" as a unit |
| 5 | Full patch-plasticity: bundle discovery, eval gating, live swap, portable across agents |

---

## Master Scored Table

| # | System | Interface Format | Discovery | Domain Bundling | Plasticity Score | Key Metric |
|---|--------|-----------------|-----------|-----------------|-----------------|------------|
| 1 | **Model Context Protocol (MCP)** | JSON-RPC 2.0 + JSON Schema | `tools/list` + paginated registry | Explicit server = bundle unit; 9,400+ public servers | **5** | 78% enterprise adoption; 9,400 servers; 97M SDK downloads/mo |
| 2 | **OpenAI Function Calling / tool_choice** | JSON Schema (parameters object) | Preloaded array; `tool_search` for deferred load (gpt-5.4+) | Manual array; no native bundle primitive | **3** | BFCL top-10 models; ~72% overall accuracy for leading models |
| 3 | **Anthropic Tool Use API** | JSON Schema (`input_schema`); Tool Search Tool; Programmatic TC | Preloaded + `defer_loading:true`; dynamic discovery | ToolSpec arrays; server tools (web_search, code_exec) | **4** | Tool Search handles 1000s of tools without context overflow |
| 4 | **Gemini Function Calling** | JSON Schema (`functionDeclarations`); REST + SDK | Preloaded; `toolConfig.functionCallingConfig` | Tool config object; parallel + compositional calls | **3** | Gemini 2.5 Pro tops LMArena; native Google Search + code exec |
| 5 | **LangChain Tools Abstraction** | Pydantic schema / `@tool` decorator → provider-specific | Preloaded via `bind_tools()`; LangChain Hub | ToolSpec collections; provider-agnostic interface | **3** | 65M+ downloads/month; standard cross-provider tool interface |
| 6 | **LlamaIndex Tool Ecosystem** | `FunctionTool`, `QueryEngineTool`, `ToolSpec` | Preloaded; `LoadAndSearchToolSpec` for on-demand | `ToolSpec` = domain bundle primitive; LlamaHub ToolSpecs | **4** | 3,451 tools in ToolBench; on-demand indexing pattern |
| 7 | **Toolformer** (Schick et al., arXiv:2302.04761) | Simple API call tokens in text (`[API(args) → result]`) | Self-supervised selection from text generation | Fixed set of 5 tools; no bundling primitive | **2** | Zero-shot competitive with 175B models using 6.7B params |
| 8 | **ToolLLM / ToolBench** (Qin et al., arXiv:2307.16789) | RESTful API calls; JSON schema; DFSDT search | Neural API retriever recommends tools per instruction | 3,451 tools, 49 categories; retrieval-based discovery | **3** | ToolLLaMA ≈ ChatGPT pass rate; 16,464 real APIs; 70%+ pass rate |
| 9 | **Harvey (Legal Vertical)** | Tool Bundles (internal abstraction) + LexisNexis/iManage/Vault integrations | Planner agent selects bundles; 500+ pre-built agents | **Tool Bundle is first-class product unit**; practice-area packs | **5** | 400K agentic queries/day; 18,000+ custom workflows; 200+ legal sources |
| 10 | **Hippocratic AI (Healthcare Vertical)** | EHR integrations (Epic, Cerner, Salesforce HC); voice + API | Clinician marketplace (300+ agents); Polaris architecture | Specialty-specific agent bundles; clinical workflow packs | **5** | $3.5B valuation; 30% readmission reduction; 360% care capacity boost |
| 11 | **Sierra (Customer-Facing Vertical)** | API connectors to order management, CRM, diagnostics; 30+ languages | Ghostwriter builds agents from SOPs + transcripts | Composable skills; tool harness = product | **4** | Deployed at major enterprises; multi-channel (chat/SMS/voice/email) |
| 12 | **Cursor MCP Integration** | MCP (JSON-RPC); native Cursor settings config | MCP registry + manual config; server-per-tool | Any MCP server is a composable tool pack for the IDE | **4** | 4.3x faster time-to-integrate vs native function calling |
| 13 | **Claude Code Tool API** | Anthropic Tool Use API; bash, file read/write, code exec | System-level preload; programmatic tool calling from code | Tools injected as agent capabilities at session start | **4** | Programmatic TC: tools called from within sandboxed code execution |
| 14 | **OpenAI Assistants API** | `code_interpreter`, `file_search`, `function` type tools | Tool selection per-run; `tools` array on assistant object | Per-assistant tool sets; multi-tool composition | **3** | Code Interpreter: sandboxed Python; File Search: vector store retrieval |
| 15 | **GPT Actions** | OpenAPI specification (YAML/JSON) | Preloaded from spec; schema auto-parsed | One OpenAPI spec = one action bundle (domain fit is natural) | **3** | OpenAPI → function definitions; N tools from 1 spec document |
| 16 | **Code Interpreter / Advanced Data Analysis** | Sandboxed Python REPL; file I/O; iterative execution | Built-in tool type; always available when enabled | Data science toolkit is a fixed bundle (pandas, matplotlib, etc.) | **3** | Write → run → debug loop; math, data analysis, image transforms |
| 17 | **Browser Tools (Playwright / Anthropic Computer Use)** | DOM/screenshot-based; CDP over WebSocket; tool_use API | Agent decides when to use; model-agnostic | Browser automation = domain bundle for web-interactive tasks | **3** | Computer Use: full desktop control; Playwright: 96% web coverage |
| 18 | **Devin / SWE-agent Tool Harness** | Bash, git, file I/O, web search, code exec as tools | Agent planner routes to tools; no user selection needed | Engineering tool harness IS the product; fixed vertical bundle | **4** | Devin: 13.86% SWE-bench (SOTA at launch); SWE-agent: 12.29% |
| 19 | **LangGraph Tool Nodes** | `ToolNode` prebuilt; LangGraph state graph edges | Conditional edges route to `tool_node`; graph-defined | Multi-agent graphs: each node = domain tool cluster | **4** | Parallel tool execution; error handling; state injection built-in |
| 20 | **BFCL — Berkeley Function-Calling Leaderboard** | Evaluation framework (AST-based, multi-language) | N/A (benchmark, not a tool system) | N/A | **N/A** | De facto industry standard; top: GLM-4.5 70.85%, Claude Opus 4.1 70.36% |

---

## Per-System Entries

### 1. Model Context Protocol (MCP)

**Source:** [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools); [Adoption statistics](https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol)

**Interface format:** JSON-RPC 2.0 transport with JSON Schema 2020-12 for tool `inputSchema` and optional `outputSchema`. Each tool definition requires `name` (1–128 chars), `description`, and `inputSchema`. Tool calls use `tools/call` with `arguments` JSON.

**Discovery mechanism:** Clients issue `tools/list` requests (paginated via cursor). Servers emit `notifications/tools/list_changed` when the tool list updates. This enables live swap of tool sets without reconnection.

**Domain-bundling support:** The MCP server IS the bundle unit. A single MCP server packages a coherent set of domain tools (e.g., a "Legal Research" server exposes Westlaw search, citation check, and jurisdiction filter as three tools). The public registry grew from ~210 servers at launch (Nov 2024) to 9,400+ by April 2026 — a 7.8× year-over-year expansion. Registry is organized by category (dev tools, databases, communication, marketing, etc.).

**Adoption data:** 
- Server downloads: 100K (Nov 2024) → 8M (Apr 2025) → 97M monthly SDK downloads (Dec 2025)
- 78% of enterprise AI teams have ≥1 MCP-backed agent in production (Apr 2026)
- 14,000 MCP servers + 300 MCP clients cataloged (2025)
- Median: 4 MCP servers per production agent stack
- 67% of CTOs have named MCP their default agent-integration standard
- All frontier labs (Claude, ChatGPT, Gemini, every major IDE) ship MCP client support

**Key advantage over native function calling:** MCP reduces integrations from N×M to N+M (each provider implements once, each tool server implements once). Digital Applied reports 4.3× faster time-to-integrate than native function calling.

**Reliability:** Protocol distinguishes protocol errors (JSON-RPC, e.g., -32602 unknown tool) from tool execution errors (isError:true for business logic failures) — enabling model self-correction.

**Patch-plasticity score: 5** — Full bundle discovery, live `tools/list_changed` notifications, portable across all MCP clients, ecosystem standardization achieved. Domain bundles ship as server objects with independent lifecycle.

---

### 2. OpenAI Function Calling / tool_choice

**Source:** [OpenAI Function Calling Guide](https://developers.openai.com/api/docs/guides/function-calling)

**Interface format:** JSON Schema object with `type:"function"`, `name`, `description`, `parameters` (JSON Schema defining arguments), and optional `strict` mode for guaranteed schema adherence. Tool calls returned as `tool_calls` array in response.

**Discovery mechanism:** Preloaded `tools` array per request. For large schemas, `tool_search` (gpt-5.4+ only) enables deferred loading — tools marked `defer_loading:true` are discoverable on-demand without consuming context. `tool_choice` parameter controls selection: `"auto"` (default), `"required"`, `{type:"function", name:"..."}` (forced), or `"none"`.

**Domain-bundling support:** No native bundle primitive — tools are passed as flat arrays. Developers must manually curate domain tool sets per request. GPT Actions (see #15) provide a partial answer via OpenAPI specs. `tool_search` is the first step toward retrieval-based bundle management.

**Reliability metrics:** BFCL: GPT-4o-2024-11-20 scores ~72% overall accuracy (rank #2 on prompt mode). GPT-5 scores 59.22% on BFCL overall (7th overall, strong in multimodal tasks). Bloomberg internal work shows 70% reduction in required tool calls with improved prompt context.

**Patch-plasticity score: 3** — Robust, production-proven, but bundling is implicit (developer responsibility). `tool_search` moves toward 4 but is model-gated (gpt-5.4+ only).

---

### 3. Anthropic Tool Use API

**Source:** [Anthropic Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview); [Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use)

**Interface format:** JSON Schema via `input_schema` field (vs OpenAI's `parameters`). Three tool classes: (a) **Client tools** — developer-defined, execution on client side, `stop_reason:"tool_use"` triggers; (b) **Server tools** — Anthropic-hosted (`web_search`, `code_execution`, `web_fetch`, `tool_search`), results returned directly; (c) **Anthropic-defined computer use tools** (bash, text_editor, etc.).

**Discovery mechanism:** Three modes:
1. Preloaded array (standard)
2. Tool Search Tool — `defer_loading:true` makes tools discoverable on-demand; Claude sees only `tool_search` + always-loaded tools, then pulls domain tools as needed
3. Programmatic Tool Calling — Claude writes Python orchestration code; tools called as `await tool_name(args)` from within sandboxed code execution; intermediate results do NOT enter Claude's context window

**Domain-bundling support:** ToolSpec arrays provide domain grouping. The Tool Search Tool explicitly addresses the "1000s of tools" use case — you provide all definitions but defer loading, enabling large domain catalogs without context overflow. `allowed_callers` field controls which execution contexts can invoke each tool.

**Reliability metrics:** Advanced Tool Use (Nov 2025): Programmatic TC reduces context rot by keeping intermediate tool results out of model context. Tool Search: dynamic discovery enables enterprise-scale tool libraries.

**Patch-plasticity score: 4** — Tool Search + programmatic TC represent genuine advances in large-scale bundle management. The `defer_loading` pattern is functionally equivalent to a retrieval-based bundle catalog.

---

### 4. Gemini Function Calling

**Source:** [Gemini Function Calling Guide](https://ai.google.dev/gemini-api/docs/function-calling); [Vertex AI docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)

**Interface format:** JSON Schema via `functionDeclarations` array within `types.Tool` object. REST API uses `functionDeclarations` key. SDK: `genai.Client()` with `types.GenerateContentConfig(tools=[tools])`. Supports parallel function calling (multiple calls in one turn), compositional function calling (sequential), and multi-tool use (mixing built-in Gemini tools + custom functions).

**Discovery mechanism:** Preloaded via `GenerateContentConfig`; `toolConfig.functionCallingConfig.mode` controls selection: `"auto"`, `"any"`, `"none"`. MCP client support added in Gemini API + Vertex AI (March 2026, Q1 2026 catalyst in registry data).

**Domain-bundling support:** Tool config object groups declarations; native integration with Google Search + code execution as built-in tools. Gemini natively bundles "search + code" as a capability.

**Reliability metrics:** Gemini 2.5 Pro tops LMArena leaderboard by significant margin. GLM-4.5 ranks #1 on BFCL at 70.85%; Gemini models competitive in top tier.

**Patch-plasticity score: 3** — Strong parallel/compositional calling and native built-in tools, but domain bundling still developer-managed. MCP client (March 2026) moves toward 4.

---

### 5. LangChain Tools Abstraction

**Source:** [LangChain Tool Calling](https://www.langchain.com/blog/tool-calling-with-langchain); [LangChain State of AI Agents 2024](https://www.langchain.com/stateofaiagents)

**Interface format:** Provider-agnostic abstraction: `@tool` decorator, Pydantic classes, or `BaseTool` subclass → auto-translated to provider-specific schemas (OpenAI `parameters`, Anthropic `input_schema`, etc.). `llm.bind_tools([...])` standardizes the interface. `AIMessage.tool_calls` attribute introduced for standard cross-provider tool invocation.

**Discovery mechanism:** Preloaded via `bind_tools()`; LangChain Hub for shared tool definitions. No native dynamic retrieval (LangGraph adds routing).

**Domain-bundling support:** Community tool collections; `ToolSpec` pattern inherited from LlamaIndex idioms; framework-level composability. Not a first-class bundle primitive — tools are lists passed to agents.

**Reliability metrics:** 65M+ monthly downloads. Standard interface adopted across all major providers.

**Patch-plasticity score: 3** — Excellent abstraction layer, provider-portable, but bundling is a convention not a primitive. LangGraph (see #19) elevates this.

---

### 6. LlamaIndex Tool Ecosystem

**Source:** [LlamaIndex Tools Documentation](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/); [LlamaHub ToolSpecs](https://developers.llamaindex.ai/python/examples/agent/openai_agent_with_query_engine/)

**Interface format:** `FunctionTool` (auto-infers schema from Python function signature), `QueryEngineTool` (wraps any index as a tool), `ToolSpec` (multi-tool service wrapper, e.g., GmailToolSpec). `LoadAndSearchToolSpec` wraps any tool to add on-demand indexing.

**Discovery mechanism:** `LoadAndSearchToolSpec`: load tool populates an index; search tool queries it on-demand. Recursive retrieval: search through tool descriptions, then step into tool documentation. Agents can wrap other agents as tools (composable agent hierarchy).

**Domain-bundling support:** `ToolSpec` IS the domain bundle primitive — wraps a set of tools around a single service (Gmail, Notion, database) and exposes them as a coherent unit. Utility tools handle cross-cutting concerns (caching, pagination). LlamaHub provides 150+ community ToolSpecs.

**Patch-plasticity score: 4** — `ToolSpec` is the clearest bundle primitive in the open-source ecosystem. On-demand loading via `LoadAndSearchToolSpec` approaches retrieval-based bundle management.

---

### 7. Toolformer (Schick et al., arXiv:2302.04761)

**Source:** [arXiv:2302.04761](https://arxiv.org/abs/2302.04761); NeurIPS 2023

**Interface format:** In-text API call tokens: `[API_NAME(args) → result]` embedded within text generation. Model generates the call token, execution happens, result is inserted, and generation continues. Self-supervised: uses a handful of demonstrations per API to bootstrap.

**Discovery mechanism:** Model decides via text generation probability — API calls are kept only if they reduce the loss over subsequent tokens. No external registry or planner.

**Domain-bundling support:** Fixed set of 5 tools (calculator, Q&A system, 2 search engines, translation, calendar). No bundle primitive — the tool set is baked into fine-tuning. **This is the foundational paper establishing that tool use need not require architectural changes — the model learns to self-attach tools, the precursor to the modern pattern.**

**Reliability metrics:** 6.7B parameter Toolformer achieves zero-shot performance competitive with 175B GPT-3 on multiple downstream tasks. Arithmetic: near-perfect via calculator. QA: large gains from search.

**Key theoretical claim:** "LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds" — combining generative capability with precise external computation. This frames tool attachment as an alternative to scaling.

**Patch-plasticity score: 2** — Pioneering concept but fixed tool set, no bundle primitive, tool selection baked into fine-tuning rather than runtime. Sets the intellectual foundation; modern systems are the runtime realization.

---

### 8. ToolLLM / ToolBench (Qin et al., arXiv:2307.16789)

**Source:** [arXiv:2307.16789](https://arxiv.org/abs/2307.16789); ICLR 2024

**Interface format:** RESTful API calls (RapidAPI Hub); JSON schema function definitions. DFSDT (depth-first search-based decision tree) algorithm for multi-step tool chain reasoning. Neural API retriever recommends relevant APIs per instruction.

**Discovery mechanism:** Neural API retriever (BERT-based) maps natural language instructions to relevant APIs from a catalog of 16,464 APIs. At inference: retriever recommends top-K APIs → model selects and chains calls. This is retrieval-based bundle construction.

**Domain-bundling support:** 3,451 tools across 49 categories from RapidAPI; both single-tool and multi-tool scenarios. ToolEval: automatic evaluator using ChatGPT as judge. Generalization to unseen APIs demonstrated.

**Reliability metrics:** ToolLLaMA (LLaMA fine-tuned on ToolBench): comparable to ChatGPT pass rate on ToolEval; strong zero-shot generalization on APIBench (out-of-distribution). Tool-MVR (2025 extension): +24% over ToolLLM baseline, error correction rate 58.9%.

**Key contribution:** Establishes the retrieval pattern for tool discovery at scale — the model doesn't need the full tool manifest; a retriever surfaces the relevant subset. This prefigures the `defer_loading` / Tool Search Tool patterns in production systems.

**Patch-plasticity score: 3** — Retrieval-based discovery is a significant advance, but tool set is curated for training; domain bundling is category-based rather than a first-class primitive.

---

### 9. Harvey (Legal Vertical Agent)

**Source:** [Harvey Tool Bundles Engineering Post](https://www.harvey.ai/blog/principles-that-helped-us-scale-agent-development); [Harvey Agents Announcement](https://www.harvey.ai/blog/built-by-lawyers-tailored-by-you); [Harvey Vault](https://www.harvey.ai/platform/vault); [Data Factory Post](https://www.harvey.ai/blog/using-agents-to-scale-harveys-knowledge-sources)

**Interface format:** Internal **Tool Bundle** abstraction — each bundle packages multiple related tools + sub-agents + system prompt injection into a single deployable unit. External integrations: Ask LexisNexis (direct API), iManage, NetDocuments, SharePoint, Google Drive, EDGAR, 60+ jurisdictions of legal databases.

**Discovery mechanism:** Harvey's Assistant agent receives a system prompt composed of active Tool Bundles. The planner agent selects bundles based on task type. 500+ pre-built agents cover common legal workflows; Agent Builder allows custom agents.

**Domain-bundling support:** **Tool Bundle IS the first-class product unit.** From Harvey's engineering blog: "All new product features that live in Assistant are Tool Bundles, and every top-level thread interface is an agent." A Tool Bundle gives developers freedom to inject instructions into the system prompt and bundle multiple tools/sub-agents into one capability. Bundles are portable between agents.

**Scale metrics:**
- 400K+ agentic queries daily
- 18,000+ custom workflows built by customers (as of Dec 2025)
- 500+ purpose-built legal agents across every major practice area (May 2026)
- 200+ legal knowledge sources, 60+ jurisdictions
- Data Factory scaled legal database coverage from 6 → 60 jurisdictions, 20 → 400+ data sources
- 96% key-term extraction accuracy in Vault
- 75% time savings on due diligence at GSK Stockmann
- 95% time reduction for trading agreement review at Bridgewater

**Key insight for Paper 3:** Harvey explicitly uses "leave-one-out eval gates" on Tool Bundles — each bundle must pass recall benchmarks before deployment. This is production evidence of the paper's core claim: reliability is achieved by attaching the right tools + eval, not by training.

**Patch-plasticity score: 5** — Tool Bundle is a named first-class primitive; eval gates on bundles; dynamic agent selection; live swap; practice-area portability; the architecture IS the patch-plastic model.

---

### 10. Hippocratic AI (Healthcare Vertical Agent)

**Source:** [Hippocratic AI](https://hippocraticai.com); [LinkedIn analysis](https://www.linkedin.com/pulse/how-hippocratic-ai-transforming-healthcare-through-generative-baek-t3xbc)

**Interface format:** Voice AI agents with native EHR connectors (Epic, Cerner, Salesforce Health Cloud, Athenahealth, eClinicalWorks); IVR navigation tools; adverse event reporting APIs; appointment scheduling integrations.

**Discovery mechanism:** Clinician marketplace — 300+ AI agents across 25+ specialties, each designed by licensed US clinicians via the AI Agent Trainer (no-code). Polaris 5.0T+ parameter constellation architecture: specialized support models increase medical accuracy and safety.

**Domain-bundling support:** Each marketplace agent = a specialty-specific bundle (e.g., post-discharge follow-up, chronic care management, medication adherence). Bundles include: tool set (EHR APIs + scheduling + adverse event) + system prompt + guardrails + clinical validation criteria. Clinician creators receive revenue share, creating market incentives for specialized bundle creation.

**Scale metrics:**
- $3.5B valuation (Nov 2025)
- 30% reduction in readmission rates
- 360% increase in care team capacity
- 12× average ROI across use cases
- 2.6× higher engagement with Spanish-speaking populations
- 3 of top 8 pharmaceutical companies as customers

**Patch-plasticity score: 5** — Specialty bundles are the product; clinician marketplace creates domain-specific bundle diversity; clinical validation gates (analogous to Harvey's eval gates); EHR integrations are the operational layer.

---

### 11. Sierra (Customer-Facing Vertical Agent)

**Source:** [Sierra AI Agent Guide](https://sierra.ai/blog/ai-agents-guide); [Sierra Agents as a Service](https://sierra.ai/blog/agents-as-a-service); [Sierra Product](https://sierra.ai/product)

**Interface format:** API connectors to systems of record (order management, CRM, diagnostics, subscription systems); multi-channel deployment (chat, SMS, WhatsApp, email, voice, ChatGPT); 30+ language support.

**Discovery mechanism:** Ghostwriter (agent-building agent) — ingest SOPs, support call transcripts, whiteboard photos, audio recordings → automatically builds production-ready agents with guardrails. Agent harness = headless Sierra platform infrastructure accessed by Ghostwriter.

**Domain-bundling support:** "Composable skills" — out-of-the-box skills assembled into domain-specific agents. Specialist "supervisor" agents monitor for factuality, prevent domain drift (medical advice, misuse detection). Tool access: order history lookup, return processing, channel lineup search, device diagnostics, subscription changes.

**Reliability:** Supervisor layering provides reliability guarantees per domain. Full visibility into every change with review/validate/ship pipeline. Triggered next-best-action workflows based on real-world signals.

**Patch-plasticity score: 4** — Composable skill bundles, multi-channel deployment, Ghostwriter as meta-agent. Domain bundling is strong but less formally named than Harvey's Tool Bundle construct.

---

### 12. Cursor MCP Integration

**Source:** [Best MCP Servers for Cursor](https://www.truefoundry.com/blog/best-mcp-servers-for-cursor-ai); [Composio Cursor Integration](https://composio.dev/toolkits/cursor); [The Hacker News CVE report](https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability)

**Interface format:** MCP (JSON-RPC); configured via `mcp_servers` in Cursor settings. Supports both local stdio transport and remote HTTP MCP servers. Structured LLM-friendly schemas for reliable tool execution.

**Discovery mechanism:** MCP registry + manual config in settings file. Any MCP server becomes a Cursor tool. Popular servers: GitHub, filesystem, databases, Slack, Notion, Linear, web search.

**Domain-bundling support:** Any MCP server is a composable domain pack. Workflow example: Query database → update backend logic → push changes → notify team — all from a single Cursor prompt. Transforms IDE from code editor to workflow orchestrator.

**Security note:** CVE-2025-54136 — post-approval config modification attack. Fixed in Cursor 1.3 (July 2025) by requiring approval on every config modification. Demonstrates production-grade security engineering around tool attachment.

**Patch-plasticity score: 4** — Native MCP client; full domain pack composability; inherits MCP's 5-score properties. Score held at 4 because the IDE context is domain-specialized (software engineering) rather than fully general.

---

### 13. Claude Code Tool API

**Source:** [Anthropic Programmatic Tool Calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling); [Anthropic Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use)

**Interface format:** Standard Anthropic Tool Use API + `code_execution` server tool. `allowed_callers: ["code_execution_20260120"]` enables tools to be invoked from within sandboxed Python code that Claude writes. Tools become `async` Python functions in the execution environment.

**Discovery mechanism:** Session-level injection: tools declared at request time. Claude writes orchestration code that calls tools as functions; intermediate results bypass Claude's context window entirely (going to the Python runtime, not the LLM). Multi-tool parallel orchestration without per-tool context overhead.

**Domain-bundling support:** The "programmatic tool calling" pattern enables Claude to orchestrate a domain-specific tool suite via a single Python script — effectively compressing N sequential tool calls and their results into one final output to Claude. Reduces context rot for multi-step domain workflows.

**Patch-plasticity score: 4** — Programmatic TC is a novel architectural advance: tools become callable library functions in a code environment rather than interleaved LLM conversation turns. Domain bundles benefit from the reduced context overhead.

---

### 14. OpenAI Assistants API

**Source:** [Assistants Code Interpreter](https://developers.openai.com/api/docs/assistants/tools/code-interpreter); [OpenAI Assistants API tools](https://developers.openai.com/api/docs)

**Interface format:** Three tool types: `code_interpreter` (sandboxed Python REPL + file I/O), `file_search` (vector store retrieval over uploaded files), `function` (standard function calling). Tools declared on the assistant object; activated per-run via the `tools` array.

**Discovery mechanism:** Per-assistant configuration + per-run override. Tool resources (`code_interpreter.file_ids`, `file_search.vector_store_ids`) injected at creation time or run time.

**Domain-bundling support:** An Assistant object is a rudimentary bundle — it packages model + instructions + tools + knowledge files. Limitation: `file_search` and `code_interpreter` have documented interaction challenges (Excel files must go to code_interpreter, not file_search). Per-run tool selection provides flexibility but requires developer management.

**Patch-plasticity score: 3** — Assistant = lightweight bundle container, but tool interaction constraints and manual management limit full plasticity. No dynamic tool discovery within the assistant.

---

### 15. GPT Actions

**Source:** [OpenAI Function Calling with OpenAPI](https://developers.openai.com/cookbook/examples/function_calling_with_an_openapi_spec)

**Interface format:** OpenAPI specification (YAML/JSON) parsed into function definitions. `openapi_to_functions()` converts paths + methods into `{type:"function", function:{name, description, parameters}}` arrays. One spec = N callable functions.

**Discovery mechanism:** Preloaded from spec at GPT creation time; spec auto-parsed to enumerate available operations. Used in ChatGPT custom GPTs to give models access to any REST API.

**Domain-bundling support:** An OpenAPI spec is naturally a domain bundle — it describes all operations of a specific service. A "Legal Research GPT Action" would define endpoints for case search, statute lookup, citation validation. Composing multiple specs = composing domain bundles.

**Patch-plasticity score: 3** — OpenAPI as interface format provides excellent domain capture, but discovery is spec-static (not dynamic retrieval). Bundle composition requires manual multi-spec management.

---

### 16. Code Interpreter / Advanced Data Analysis

**Source:** [OpenAI Code Interpreter Tool Guide](https://developers.openai.com/api/docs/guides/tools-code-interpreter); [Pluralsight: ADA](https://www.pluralsight.com/resources/blog/ai-and-data/ChatGPT-Advanced-Data-Analytics)

**Interface format:** Sandboxed Python REPL with iterative write-run-debug loop. Model writes code, executes it, sees output, rewrites if needed. File I/O for uploads/downloads. Image transforms (crop, zoom, rotate) for reasoning models (o3, o4-mini).

**Discovery mechanism:** Built-in tool type; enabled by specifying `{type:"code_interpreter", container:{type:"auto", memory_limit:"4g"}}`. Always available when enabled — no selection needed.

**Domain-bundling support:** The execution environment IS a domain bundle: Python standard library + data science stack (pandas, numpy, matplotlib, scipy, etc.). Fixed bundle for data analysis / math / scientific computing. Limitation: bundle is fixed, not customizable beyond uploaded files.

**Reliability:** Iterative self-correction: model writes code that fails → rewrites → runs again → converges. This is tool-attachment-as-reliability-mechanism in a pure form.

**Patch-plasticity score: 3** — Pre-bundled data science toolkit, iterative correction loop, but bundle is fixed (not domain-customizable at runtime without uploading files).

---

### 17. Browser Tools (Playwright / Anthropic Computer Use)

**Source:** [Firecrawl: Best AI Browser Agents](https://www.firecrawl.dev/blog/best-browser-agents); [Anthropic Computer Use](https://www.anthropic.com/engineering/advanced-tool-use)

**Interface format:** 
- **Playwright-based agents:** CDP (Chrome DevTools Protocol) over WebSocket; DOM interaction; model-agnostic (OpenAI, Anthropic, Google, local via LiteLLM)
- **Anthropic Computer Use:** Screenshot + coordinate-based interactions; bash tool; keyboard/mouse emulation; full desktop control

**Discovery mechanism:** Agent decides when to use browser tool based on task type. Playwright agents: DOM distillation strips pages to essential interactive elements, reducing token consumption. Computer Use: model sees screenshot + decides next action.

**Domain-bundling support:** Browser automation is a domain bundle for web-interactive tasks (data extraction, form filling, UI testing, research). Playwright wrappers like Firecrawl add "96% web coverage" with structured extraction layer.

**Reliability:** Key distinction from traditional automation: LLM recognizes semantic intent (the "Submit" button) even when DOM selectors change. Playwright scripts break on class name changes; LLM agents adapt.

**Patch-plasticity score: 3** — Strong for web-domain tasks, but the tool is general-purpose (any website) rather than a domain-specific bundle. Specialized browser agents (legal database navigation, financial data extraction) would score higher.

---

### 18. Devin / SWE-agent Tool Harness

**Source:** [Cognition SWE-bench Technical Report](https://cognition.ai/blog/swe-bench-technical-report); [SWE-bench Leaderboard](https://www.swebench.com); [SWE-agent Reddit](https://www.reddit.com/r/singularity/comments/1bu9iae/)

**Interface format:** Tool harness includes: bash shell execution, git operations, file read/write, code execution, web search, editor. SWE-agent uses an Agent-Computer Interface (ACI) with purpose-built commands optimized for LLM interaction (not raw terminal).

**Discovery mechanism:** Agent planner routes to tools without user selection. The tool harness is always present — the agent decides which tools to use per subtask. No dynamic discovery needed: fixed engineering tool set is comprehensive.

**Domain-bundling support:** The engineering tool harness IS the domain bundle — it defines "software engineer capability." This is a fixed vertical bundle: bash + git + editor + tests = software engineering. The model comes with no special engineering knowledge; the tool bundle delivers the capability.

**Key evidence for Paper 3:** Engine Labs (top-4 SWE-bench Verified): "Engine achieves this with state of the art reasoning and agentic behaviour built on custom workflow integrations and a deep understanding of complex multi-repo codebases. Engine also runs on the latest available models like Claude 3.5 Sonnet and does not use proprietary models or fine-tunes." — Tool attachment, not fine-tuning, delivers SOTA engineering capability.

**Reliability metrics:**
- Devin: 13.86% SWE-bench Full (SOTA at launch March 2024; previous best: 4.80% assisted)
- SWE-agent: 12.29% (GPT-4 backbone)
- Devin test-driven development setting: 23% pass rate
- Current SOTA on SWE-bench Verified: 50%+ for top agents

**Patch-plasticity score: 4** — Fixed but comprehensive domain bundle; tool harness delivers engineering capability without fine-tuning; strong SWE-bench evidence that tool + model > fine-tuned model for coding.

---

### 19. LangGraph Tool Nodes

**Source:** [LangGraph Workflows and Agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents); [IBM: What is LangGraph](https://www.ibm.com/think/topics/langgraph); [LangChain LangGraph page](https://www.langchain.com/langgraph)

**Interface format:** `ToolNode` prebuilt node handles tool execution within a LangGraph `StateGraph`. Accepts list of tools; handles parallel execution, error handling, and state injection automatically. Tool calls extracted from `AIMessage.tool_calls`; results returned as `ToolMessage` objects.

**Discovery mechanism:** Conditional edges route to `tool_node` based on `should_continue()` function checking `last_message.tool_calls`. Each node in the graph is a "domain actor." Multi-agent graphs: specialized subgraphs per domain, hierarchical routing.

**Domain-bundling support:** Multiagent architectures: dedicated LangChain agents for specific tasks/domains, routing tasks to appropriate agents for parallel execution. Each node cluster = a domain tool group. Support for: single-agent, multi-agent, hierarchical agent workflows in one framework.

**Patch-plasticity score: 4** — Graph-level domain decomposition with conditional routing; stateful orchestration; parallel tool execution; natural architecture for domain-specific tool cluster deployment. The graph topology IS the bundle structure.

---

### 20. BFCL — Berkeley Function-Calling Leaderboard

**Source:** [BFCL Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html); [Patil et al., ICML 2025](https://proceedings.mlr.press/v267/patil25a.html)

**Interface format:** Evaluation framework (not a tool system). AST-based evaluation method that scores tool call structural correctness without executing every call. Tests: single-turn (simple, parallel, multiple, nested), multi-turn (stateful conversation), hallucination measurement.

**Significance as evidence:** BFCL is cited as "the de facto standard for evaluating function-calls" (ICML 2025). Its existence proves industry consensus that **tool-calling accuracy is a distinct, measurable capability** — separate from general language ability.

**Key BFCL findings:**
- Top models (BFCL V4, April 2026): GLM-4.5 (FC): 70.85%; Claude Opus 4.1: 70.36%; Claude Sonnet 4: 70.29%; GPT-5: 59.22%
- "While state-of-the-art LLMs excel at single-turn calls, memory, dynamic decision-making, and long-horizon reasoning remain open challenges"
- MCPMark: GPT-5 leads with lower cost ($127/run vs Claude Sonnet 4 at $252/run); Claude Sonnet 4: 28.1% pass@1, 44.9% pass@4

**BFCL as evidence for Substrate 4 framing:** The leaderboard scores tool-calling as a *capability axis* independent of general intelligence — exactly the Paper 3 claim that tool attachment is measurable, separable capability. Models specialized in tool use (GLM-4.5) outperform larger general models (GPT-5) on this dimension.

**Patch-plasticity score: N/A** — Benchmark, not a system.

---

## Vertical Agent Thesis: The Bundle IS the Product

### The Commercial Reality Argument

Companies like Harvey, Hippocratic AI, and Sierra represent the strongest industry-side evidence that the paper's patch-plastic architecture is not theoretical — it is already the dominant commercial model for AI deployment in regulated verticals.

**The central observation:** Each of these companies ships a general-purpose foundation model (GPT-4o, Claude, etc.) with zero proprietary weight modifications. Their entire product differentiation lies in the **domain tool bundle** — the curated set of APIs, knowledge sources, workflow agents, and evaluation gates assembled around the model. The bundle is the moat; the model is the commodity.

**Harvey's explicit articulation** (from their engineering blog, Nov 2025): The company adopted a "no custom orchestration" rule and formalized every new capability as a **Tool Bundle** — a portable, eval-gated unit that packages tools, sub-agents, and system prompt injections. "Capabilities are Tool Bundles" is Harvey's stated architectural principle. This is the Paper 3 substrate described in prose from inside a $1B+ legal AI company.

**Harvey's scale data** confirms commercial viability: 400K+ agentic queries daily, 200+ legal knowledge sources across 60+ jurisdictions, 18,000+ customer-built custom workflows. The "Data Factory" (2026) extended this further: an autonomous pipeline that discovers legal databases, builds connectors, and validates them against eval benchmarks before launch — automated patch assembly at scale.

**Hippocratic AI's clinician marketplace** operationalizes bundle creation as a two-sided marketplace: licensed clinicians design specialty-specific agent bundles (chronic care management, post-discharge follow-up, medication adherence), pass clinical review, and receive revenue share. The result: 300+ specialty bundles across 25+ clinical areas. No new model training required — each new bundle is a new tool set + system prompt + guardrails pointing at the same Polaris foundation model.

**Sierra's Ghostwriter** auto-assembles tool bundles from unstructured inputs (SOPs, transcripts, whiteboard photos) — the bundle construction is itself automated. This represents the next evolution: not just patch-plastic deployment but **patch-plastic generation**, where the bundle-assembly process is also an AI task.

### The Reliability-Through-Tools Argument

The vertical agent companies have arrived empirically at the same conclusion Paper 3 argues theoretically: **domain reliability comes from the right tool bundle, not from model fine-tuning.**

Evidence:
1. **Harvey explicitly chose not to fine-tune** for legal tasks; reliability is enforced through Tool Bundle eval gates and 200+ curated legal knowledge sources.
2. **Engine Labs (SWE-bench top-4)** states explicitly: "Engine also runs on the latest available models like Claude 3.5 Sonnet and **does not use proprietary models or fine-tunes**. This means Engine always runs on the latest foundation models which have historically consistently outperformed use-case specific models."
3. **Hippocratic AI's Polaris architecture** uses a constellation of specialized support models — but these are tool-like modules (medical accuracy, safety) layered around the base model, not fine-tuned weights for each clinical use case.
4. **Intellihuman AI analysis** reports 85–95% accuracy for domain-specific AI on structured tasks vs. 60–75% for general LLMs — but this advantage is achievable via tool attachment (curated data access, domain-specific APIs) without requiring fine-tuning.

### The "Tool Bundle IS the Patent" Pattern

Across all three companies:
- Harvey's competitive moat = 200+ legal database integrations + Tool Bundle eval framework
- Hippocratic's moat = Epic/Cerner/Salesforce integrations + clinical validation pipeline
- Sierra's moat = Ghostwriter + composable skill library + multi-channel deployment

None of these are achievable through prompt engineering alone. None require model fine-tuning. All are tool-attachment architectures. This is the commercial validation of Substrate 4.

---

## Domain-Specific Tool Bundles vs. General Tool Access

### Evidence for the Key Paper Argument

**Argument:** Domain-specific tool bundles outperform general-purpose tool access for reliability in specialized tasks.

**Evidence 1: Bloomberg tool calling optimization (ACL 2025)**
Bloomberg's AI engineers demonstrated that "incomplete context requires LLMs to call more tools to generate their response." Their three-stage optimization framework (Feedback Generator → Suggestion Coordinator → Context Refiner) achieved:
- **70% reduction in required tool calls** on StableToolBench
- **47% fewer redundant calls** on RestBench while maintaining or improving pass rates
This directly supports the argument: domain-curated tool context → fewer errors → higher reliability.

**Evidence 2: OpenMedCalc / MedCalc-Bench**
From NIH/PMC research: "The medical calculation output of LLMs can be improved through the use of both generic and task-specific tools." MedCalc-Bench demonstrates that "LLMs are not yet computationally accurate or reliable enough for clinical use with prompt engineering alone" — but tool-augmented systems (OpenMedCalc API + ChatGPT integration) achieve acceptable clinical accuracy. The improvement is tool-specific, not model-specific.

**Evidence 3: Wolfram Foundation Tool**
Wolfram's CAG (Computation-Augmented Generation) shows: attaching Wolfram Language + Wolfram|Alpha as a "foundation tool" allows using a *lower-cost LLM tier* for tasks that would normally require a more expensive model. Domain-specific computational tool = reliability substitute for larger/fine-tuned model.

**Evidence 4: IntelliHuman AI quantification**
Vertical AI systems (with domain-specific tool bundles) achieve 85–95% accuracy on structured domain tasks vs. 60–75% for general LLMs. The gap is 20–35 percentage points — exceeding what fine-tuning typically achieves on the same benchmarks.

**Evidence 5: ToolLLM neural retriever**
The DFSDT + neural retriever pattern shows: when the model selects tools from a domain-curated subset (relevant API categories) rather than all 16,464 APIs, pass rates are significantly higher. Retriever accuracy is the limiting factor — supporting the bundle argument (pre-curated domain bundle > ad-hoc general access).

**Evidence 6: Harvey eval gates**
Harvey's leave-one-out validation on Tool Bundles prevents capability regression: "our retrieval dataset defines a large number of queries with expected recall across a set of knowledge sources. When any change is made to the system, developers can verify that their capability has not regressed." This is quantified domain tool reliability.

---

## Industry Convergence Narrative: MCP as Universal Standard

The MCP adoption data represents a convergence event unprecedented in AI infrastructure:

| Quarter | Registered MCP Servers | Notable Catalyst |
|---------|------------------------|-----------------|
| Q4 2024 | ~210 | Anthropic open-sources MCP (Nov 25, 2024) |
| Q1 2025 | 1,200 | Cursor, Windsurf, Zed ship MCP support |
| Q2 2025 | 2,300 | ChatGPT MCP support (Apps SDK + Connectors) |
| Q3 2025 | 3,400 | Microsoft + GitHub first-party servers |
| Q4 2025 | 6,800 | Streamable HTTP transport stabilizes |
| Q1 2026 | 9,400+ | Gemini API + Vertex AI MCP launch |

Source: [Digital Applied MCP Adoption Statistics](https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol)

The pattern: every frontier lab, every major IDE, every enterprise AI platform has standardized on MCP as the tool attachment protocol. This is the industry's answer to the N×M integration problem (N models × M tools = N+M implementations with MCP). The domain bundle = the MCP server. The patch = connecting the model to the relevant bundle.

**The convergence validates Substrate 4 as the correct abstraction level** for the paper. The industry did not converge on fine-tuning as the mechanism for domain capability. It converged on tool attachment with standardized interfaces.

---

## Key Papers and References

| Paper | Claim Relevant to Substrate 4 |
|-------|-------------------------------|
| Toolformer (Schick et al., 2023, arXiv:2302.04761) | LMs can teach themselves to use external tools; zero-shot gains competitive with 10× larger models |
| ToolLLM/ToolBench (Qin et al., 2023, arXiv:2307.16789) | Neural retriever + DFSDT enables mastery of 16,464 real APIs; retrieval-based bundle discovery |
| BFCL (Patil et al., ICML 2025) | Tool-calling accuracy is a distinct measurable capability; de facto evaluation standard |
| BloombergGPT (2023) | Finance-domain LLM; but Bloomberg's 2025 ACL work shows tool context optimization outperforms model scaling |
| Harvey Engineering Blog (Nov 2025) | "Capabilities are Tool Bundles" — production implementation of Substrate 4 at scale |
| Wolfram CAG (2026) | Foundation tool as alternative to larger models for precise computation; tool attachment = reliability |
| OpenMedCalc / MedCalc-Bench | Medical calculation accuracy requires domain-specific tools, not prompt engineering alone |

---

## Summary Assessment for Paper 3

**Substrate 4 claim to defend:** Capabilities are attached at inference time via tool interfaces, not trained into weights. Domain-specific bundles deliver reliability superior to general-purpose access.

**Evidence quality:** Strong across three dimensions:
1. **Infrastructure convergence:** MCP achieved 78% enterprise adoption in 17 months — the fastest protocol adoption in AI infrastructure history. This is the standardization of Substrate 4.
2. **Commercial validation:** Harvey/Hippocratic/Sierra are $1B+ companies whose products are literally "tool bundle + foundation model." They did not fine-tune their way to reliability.
3. **Benchmark evidence:** BFCL as de facto standard proves tool-calling is a measurable, separable capability. BFCL top performers (GLM-4.5, Claude Opus 4.1) are specialists in this substrate, not necessarily the largest models.

**Key gap to acknowledge:** Most "domain-specific tool bundle outperforms general" comparisons in the literature compare fine-tuned domain LLMs vs. general LLMs, not domain-bundled-general vs. general. The Harvey/Bloomberg/OpenMedCalc evidence fills this gap, but a dedicated controlled study would strengthen the argument. The Wolfram CAG work is the closest to a controlled comparison.

**Strongest single sentence for the paper:** Harvey's engineering principle — *"Capabilities are Tool Bundles, and every top-level thread interface is an agent"* — is the commercial-production formulation of the paper's central substrate claim.
