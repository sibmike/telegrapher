# Substrate 1: Persistent Instruction Scaffolds — Evidence Harvest
## Paper 3 of the LLM Reliability Trilogy

**Thesis:** Production LLM systems already adapt to local domains via versioned externalized scaffolds, not weight updates. Substrate 1 is the simplest layer: persistent project/team/user instructions loaded at session start.

**Harvest date:** 2025–2026 evidence window  
**Rubric (patch-plasticity 0–5):**
- 0 = ephemeral prompt only, no persistence
- 1 = persistent local instructions, manual load
- 2 = persistent instructions + tool/MCP attachment
- 3 = skills or memory layer present
- 4 = automated feedback updates the scaffold
- 5 = two-loop versioned promotion/governance

---

## Summary Table

| System | Domain | Persists | Versioned (Git) | Tool/MCP Attach | Score | Best Citation |
|---|---|---|---|---|---|---|
| **Cursor Rules** | IDE (code) | `.cursor/rules/*.mdc`, `~/.cursor/rules` | ✅ explicit | ✅ MCP supported | **3** | [docs.cursor.com/rules](https://docs.cursor.com/en/context/rules) |
| **AGENTS.md** | Cross-tool standard | Repo root / nested dirs | ✅ git-tracked | ✅ 20+ agents | **2** | [arxiv.org/abs/2601.20404](https://arxiv.org/abs/2601.20404) |
| **Claude Code CLAUDE.md** | IDE/CLI (code) | Multi-scope MD files | ✅ project file | ✅ MCP, tools | **4** | [docs.anthropic.com/en/docs/claude-code/memory](https://docs.anthropic.com/en/docs/claude-code/memory) |
| **GitHub Copilot Custom Instructions** | IDE/cloud (code) | `.github/copilot-instructions.md` | ✅ base-branch | ✅ AGENTS.md, tools | **3** | [docs.github.com/en/copilot/…](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) |
| **Windsurf Cascade Rules** | IDE (code) | `.windsurf/rules/*.md`, `global_rules.md` | ✅ workspace dir | ✅ MCP supported | **3** | [docs.windsurf.com/windsurf/cascade/memories](https://docs.windsurf.com/windsurf/cascade/memories) |
| **Continue.dev Rules** | IDE (code) | `.continue/rules/*.md`, `~/.continue/rules` | ✅ git-tracked | ✅ MCP servers | **3** | [docs.continue.dev/customize/deep-dives/rules](https://docs.continue.dev/customize/deep-dives/rules) |
| **Aider Conventions** | CLI (code) | `CONVENTIONS.md` + `.aider.conf.yml` | ✅ git-tracked | ✅ via config | **2** | [aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html) |
| **Lovable Knowledge** | Web (low-code) | Workspace + project text fields (10k chars) | ❌ DB-stored, not git | ❌ no MCP | **2** | [docs.lovable.dev/features/knowledge](https://docs.lovable.dev/features/knowledge) |
| **Replit replit.md** | Web IDE (code) | Project root markdown file | ⚠️ possible (git-backed repls) | ❌ not documented | **4** | [docs.replit.com/core-concepts/agent/replit-dot-md](https://docs.replit.com/core-concepts/agent/replit-dot-md) |
| **Zed AI Rules** | IDE (code) | `.rules` / `.cursorrules` / `CLAUDE.md` etc. | ✅ git-tracked | ✅ MCP via custom server | **3** | [zed.dev/docs/ai/rules](https://zed.dev/docs/ai/rules) |
| **VS Code Copilot Instructions** | IDE (code) | `.github/instructions/*.instructions.md` | ✅ workspace git | ✅ MCP, tools | **3** | [code.visualstudio.com/docs/copilot/customization/custom-instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) |
| **Cody / Sourcegraph** | IDE (code) | `.vscode/cody.json` custom commands | ⚠️ git-tracked | ❌ limited | **2** | [sourcegraph.com/docs/cody](https://sourcegraph.com/docs/cody) |

---

## Per-System Evidence Entries

---

### 1. Cursor Rules

**Official docs:** [https://docs.cursor.com/en/context/rules](https://docs.cursor.com/en/context/rules)

#### What persists
> "Project rules live in `.cursor/rules`. Each rule is a file and version-controlled. They can be scoped using path patterns, invoked manually, or included based on relevance. Subdirectories can include their own `.cursor/rules` directory scoped to that folder."

#### Scoping
| Scope | Storage | Applies to |
|---|---|---|
| User (global) | `Cursor Settings → Rules` (plain text) | All projects |
| Project | `.cursor/rules/*.mdc` | Codebase-specific |
| Nested project | Subdirectory `.cursor/rules/` | Folder-specific |
| Legacy | `.cursorrules` (deprecated) | Project root |

#### Loading mechanism
> "When applied, rule contents are included at the start of the model context."

Four rule types control when a rule fires:

| Rule Type | Trigger | `alwaysApply` | `globs` |
|---|---|---|---|
| `Always` | Every context window | `true` | — |
| `Auto Attached` | Files matching glob pattern | `false` | `*.ts`, `src/**` etc. |
| `Agent Requested` | AI decides based on description | `false` | — |
| `Manual` | Explicit `@ruleName` mention | `false` | — |

Format: **MDC** (`.mdc`), a Markdown variant supporting YAML frontmatter metadata.

#### Versioning
Explicitly versioned: `.cursor/rules` directory is committed to Git. The docs state: "Teams can collaborate using shared rules, ensuring consistency as everyone pulls the same rules." ([forum.cursor.com deep dive, 2025](https://forum.cursor.com/t/a-deep-dive-into-cursor-rules-0-45/60721))

#### Interop
Cursor also reads AGENTS.md (the cross-tool open standard) and lists its supported agent file formats via AGENTS.md ecosystem.

#### Adoption/metrics
Cursor is one of the most widely-used AI IDEs (~4M users as of 2025 reports). No published per-rules adoption number, but `.cursor/rules` directories are present in tens of thousands of public GitHub repos. The legacy `.cursorrules` ecosystem has over 10,000 community-shared rule files catalogued.

#### Honest gaps
- No official published metric on rule-usage impact on code quality from Cursor itself
- Two-stage activation (injection vs. activation via description field) means `alwaysApply: true` does not guarantee execution when context is congested

#### **Patch-plasticity score: 3**
**Justification:** Persistent file-based rules ✅, auto-loaded at session start ✅, git-versioned and team-shared ✅, MCP attachment supported ✅, skills layer via nested rules ✅. Does not yet have automated feedback writing rules (would be score 4) or PR-promotion governance (score 5).

---

### 2. AGENTS.md (Open Ecosystem Standard)

**Official spec:** [https://agents.md](https://agents.md)  
**Linux Foundation announcement:** [https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

#### What persists
> "AGENTS.md is a simple, open format for guiding coding agents. Think of it as a README for agents."

Content types: build steps, tests, project conventions, coding style, security considerations, commit message guidelines, PR instructions, deployment steps, CI plan locations, programmatic checks.

#### Loading mechanism
> "Agents automatically read the nearest file in the directory tree; the closest file to the edited file takes precedence."
> "Monorepos: Supports nested AGENTS.md files inside specific packages or subprojects."
> "Explicit user chat prompts override instructions in the AGENTS.md file."

Configuration examples:
- **Aider:** `.aider.conf.yml` using `read: AGENTS.md`
- **Gemini CLI:** `.gemini/settings.json` using `{ "context": { "fileName": "AGENTS.md" } }`

#### Versioning
Standard Markdown (`.md`) committed to git. "Living documentation" stewarded by the **Agentic AI Foundation** under the Linux Foundation.

#### Adoption (confirmed numbers)
| Metric | Value |
|---|---|
| Total GitHub examples | **60,000+** |
| OpenAI main repo files | 88 |
| apache/airflow adoption | +4,370 |
| openai/codex adoption | +445 |
| Supported tools | 20+ (Cursor, Copilot, Codex, Jules, Devin, Zed, VS Code, Windsurf, Aider, Factory, etc.) |

From [Linux Foundation (2025-12-09)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation): "AGENTS.md has already been adopted by more than 60,000 open source projects."

#### Quality/reliability impact (empirical)
Key paper: **Lulla et al. (2026), arXiv:2601.20404** — "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents"
- **28.64% reduction in median runtime** for AI coding agents
- **16.58% reduction in output token consumption**
- Comparable task completion rate (no quality degradation)
- N=10 repos, N=124 pull requests, agents: Codex and Claude Code

> "The presence of AGENTS.md is associated with a lower median runtime (Δ28.64%) and reduced output token consumption (Δ16.58%), while maintaining a comparable task completion behavior."

#### Interop
- Windsurf: Root-level AGENTS.md is always-on; subdirectory = auto-glob for that directory
- GitHub Copilot (Aug 2025): officially added AGENTS.md support
- Zed: Reads AGENTS.md in fallback priority list (priority #6-7)
- Claude Code: Supports symlinks from AGENTS.md → CLAUDE.md

#### Honest gaps
- No explicit versioning protocol or schema versioning in the spec itself
- One noted holdout: Claude Code has not *officially* adopted AGENTS.md (community workaround is symlink)
- Spec has no formal conditional inclusion mechanism (no glob frontmatter in base spec; tools add their own on top)

#### **Patch-plasticity score: 2**
**Justification:** The base AGENTS.md *format* is score 2 (persistent + auto-loaded + git-tracked + multi-tool attachment). Specific *implementations* within tools (Windsurf, Cursor) layer on top to reach score 3. The format itself doesn't define memory, skills, or automated feedback update loops.

---

### 3. Claude Code CLAUDE.md / Project Memory

**Official docs:** [https://docs.anthropic.com/en/docs/claude-code/memory](https://docs.anthropic.com/en/docs/claude-code/memory)

#### Scoping (four levels)
| Scope | Location | Shared via |
|---|---|---|
| Managed policy (org) | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux) | IT/DevOps deployment |
| User | `~/.claude/CLAUDE.md` | Personal (all projects) |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team via source control |
| Local | `./CLAUDE.local.md` | Personal project (gitignored) |

#### What persists
> "CLAUDE.md persistence: Instructions persist as markdown files."

Content types: build/test commands, coding standards, naming conventions, architectural decisions, common workflows, debugging insights.

#### Loading mechanism
> "Resolution Order: Claude walks up the directory tree from the current working directory to the filesystem root."
> "Files are ordered from the filesystem root down to the working directory. Broadest scopes (Managed/User) load before specific scopes (Project/Local)."
> "CLAUDE.md: Loaded in full at launch."

Special features:
- **Imports:** `@path/to/import` syntax, max 5 hops recursion
- **Path-scoped rules:** `.claude/rules/` with YAML frontmatter `paths:` field
- **On-demand loading:** Nested CLAUDE.md files (sub-directories) load when Claude reads files in those directories
- **Compaction:** Project-root CLAUDE.md re-injected after `/compact`

#### Versioning
> "Project CLAUDE.md: Intended to be committed to version control and shared with the team."
> "CLAUDE.local.md: Intended to be added to .gitignore."
> "Symlinks: Supported for sharing rules across projects or linking AGENTS.md to CLAUDE.md."

Org-level managed policy: cannot be excluded by users (`claudeMdExcludes` only works for non-managed files).

#### Auto-memory layer (score-4 feature)
> "Auto memory persistence: Knowledge accumulates across sessions without manual input."
> "Who writes it: Claude (auto-memory) vs. You (CLAUDE.md)"

Auto memory (v2.1.59+) stores `~/.claude/projects/<project>/memory/MEMORY.md`. First 200 lines or 25KB loaded at session start. Claude writes this file autonomously from corrections and preferences.

#### Interop
- AGENTS.md: Symlink supported (`ln -s AGENTS.md CLAUDE.md`)
- GitHub Copilot: CLAUDE.md listed as accepted agent instruction file
- Zed: Reads CLAUDE.md (priority #8)

#### **Patch-plasticity score: 4**
**Justification:** Persistent multi-scope files ✅, git-versioned ✅, org-managed policy layer ✅, tool attachment via MCP ✅, **auto-memory writes the scaffold from agent feedback** ✅. Lacks automated PR-promotion governance loop (would be score 5). The managed policy layer + auto-memory makes this the most mature scaffold among the systems reviewed.

---

### 4. GitHub Copilot Custom Instructions

**Official docs:** [https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

#### File formats supported
| Instruction Type | File | Location |
|---|---|---|
| Repository-wide | `copilot-instructions.md` | `.github/` |
| Path-specific | `NAME.instructions.md` | `.github/instructions/` |
| Agent (AGENTS.md) | `AGENTS.md` | Anywhere in repo |
| Agent (Claude format) | `CLAUDE.md` | Repo root |
| Agent (Gemini format) | `GEMINI.md` | Repo root |

#### Loading mechanism
> "Instructions are automatically added to requests submitted to Copilot."
> "Copilot uses the instructions located in the base branch of the pull request" (for code review)

Priority order:
1. Personal (highest) — user-specific
2. Repository — `.github/copilot-instructions.md` + path-specific
3. Organization (lowest)

Conditional inclusion via YAML frontmatter:
```yaml
applyTo: "**/*.ts,**/*.tsx"
excludeAgent: "code-review"
```

#### Versioning
Instructions stored in repo base branch; code reviews use base-branch version, ensuring stability during PRs. Git-tracked by default.

#### VS Code integration (separate docs)
From [VS Code custom instructions docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions):
> "VS Code automatically detects a `.github/copilot-instructions.md` Markdown file in the root of your workspace and applies the instructions in this file to all chat requests within this workspace."

Scopes supported in VS Code:
| Scope | Location |
|---|---|
| Workspace | `.github/instructions` folder |
| Workspace (Claude format) | `.claude/rules` folder |
| User profile | `~/.copilot/instructions`, `~/.claude/rules` |

#### AGENTS.md support (added August 2025)
From [GitHub blog (2025-08-28)](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/): "Copilot coding agent now supports AGENTS.md custom instructions... You can create a single AGENTS.md file in the root of your repository. You can also create nested AGENTS.md files which apply to specific parts of your project."

#### Custom agent profiles
GitHub Copilot supports `.github/agents/*.agent.md` files (YAML frontmatter + Markdown) defining custom agents with tool lists, MCP server configurations, and behavioral prompts. These are per-repo and committed to the branch.

#### **Patch-plasticity score: 3**
**Justification:** Persistent repo-committed files ✅, git-versioned ✅, multi-scope (user/repo/org) ✅, conditional inclusion via glob ✅, multiple file format standards supported (AGENTS.md, CLAUDE.md, GEMINI.md, copilot-instructions.md) ✅, MCP via custom agent profiles ✅. No automated feedback-writing loop (score 4 would require auto-update from CI outcomes).

---

### 5. Windsurf Cascade Rules

**Official docs:** [https://docs.windsurf.com/windsurf/cascade/memories](https://docs.windsurf.com/windsurf/cascade/memories)

#### What persists — rules
| Scope | Storage | Notes |
|---|---|---|
| Global | `~/.codeium/windsurf/memories/global_rules.md` | Max 6,000 chars, always-on |
| Workspace | `.windsurf/rules/*.md` | Per-rule files, max 12,000 chars each |
| AGENTS.md | Any directory in workspace | Root = always-on; subdirectory = auto-glob |
| System (Enterprise) | macOS: `/Library/Application Support/Windsurf/rules/*.md`; Linux: `/etc/windsurf/rules/*.md` | Deployed by IT, read-only |

#### Activation modes (conditional inclusion)
From the rules frontmatter `trigger:` field:
| Mode | Value | Context cost |
|---|---|---|
| Always On | `always_on` | Full content in system prompt every message |
| Model Decision | `model_decision` | Description shown; full content on demand |
| Glob | `glob` | Applied when Cascade reads/edits matching file |
| Manual | `manual` | Only when @mentioned |

Format example:
```markdown
---
trigger: glob
globs: **/*.test.ts
---
```

> "global_rules.md and root-level AGENTS.md do not use frontmatter and are always on."

#### Loading mechanism
> "Workspace Search: All `.windsurf/rules` directories within the current workspace and its sub-directories."
> "Git Integration: Searches up to the git root directory in parent directories."

#### Versioning
Workspace rules (`.windsurf/rules/*.md`) are in the git-tracked workspace directory, enabling team sharing via source control. Global rules (`~/.codeium/windsurf/`) are local-only.

#### Memories (separate feature)
Auto-generated from conversations. Storage: `~/.codeium/windsurf/memories/`. Not shared across workspaces; not committed.

> "Rules tell Cascade how to behave (e.g. 'use bun, not npm'). Memories let Cascade auto-generate context from conversations."

#### Workflows layer (score-3+ feature)
`.windsurf/workflows/*.md` — markdown prompt templates invoked via `/workflow-name`. Committed to repo; enterprise system-level workflows via OS-specific directories. These are a distinct layer above rules.

#### AGENTS.md interop
From the Windsurf rules docs: AGENTS.md is listed alongside workspace rules as an always-on configuration source. Windsurf also appears in AGENTS.md's supported tools list on agents.md.

#### Honest gaps
- The legacy `.windsurfrules` filename (referenced in community posts pre-2025) appears superseded by `.windsurf/rules/` directory structure in official docs; older file may still work but is undocumented
- No explicitly documented versioning protocol; relies on standard git

#### **Patch-plasticity score: 3**
**Justification:** Persistent file-based rules ✅, git-traceable workspace location ✅, multiple scope levels ✅, enterprise managed rules via system directories ✅, conditional inclusion via trigger frontmatter ✅, MCP supported ✅, memories/skills layers ✅. No automated feedback writing rules.

---

### 6. Continue.dev Rules

**Official docs:** [https://docs.continue.dev/customize/deep-dives/rules](https://docs.continue.dev/customize/deep-dives/rules)

#### What persists
> "Rules are used to provide system message instructions to the model for Agent mode, Chat mode, and Edit mode requests."

| Scope | Location | Persistence |
|---|---|---|
| Local workspace | `.continue/rules/` (top level of workspace) | Actual `.md` files, git-tracked |
| Global (user) | `~/.continue/rules/` | Local `.md` files |
| Hub | Continue Mission Control (cloud) | No local files; managed via Hub interface |

#### Loading mechanism
Rules concatenated into the system message in this order:
1. Hub assistant rules (if Hub-based assistant)
2. Referenced Hub rules (via `uses:` in `config.yaml`)
3. Local workspace rules (`.continue/rules/`)
4. Global rules (`~/.continue/rules/`)

> "Rules are joined with new lines to form the system message."

Loading is controlled by file properties:
| Property | Effect |
|---|---|
| `alwaysApply: true` | Always included |
| `globs: "**/*.ts"` | Included when matching files are in context |
| `regex: "^import .*"` | Included when file content matches |
| `alwaysApply: false` + no globs | Agent decides based on `description` |

File format: Markdown (`.md`) with YAML frontmatter recommended. YAML-only also supported.

Example:
```markdown
---
name: Documentation Standards
globs: docs/**/*.{md,mdx}
alwaysApply: false
description: Standards for writing and maintaining Continue Docs
---
# Continue Docs Standards
- Follow Mintlify documentation standards
```

#### Versioning
Local workspace rules: `.continue/rules/` is committed alongside code. From the docs: "Version controlled alongside your code." Files loaded in **lexicographical order** (controllable with numeric prefixes: `01-general.md`, `02-frontend.md`).

#### `config.yaml` top-level rules declaration
```yaml
rules:
- uses: sanity/sanity-opinionated  # Hub rule
- uses: file://user/Desktop/rules.md  # Local file
```

#### Hub layer (cross-team sharing)
Hub rules stored on Continue Mission Control, referenced in `config.yaml`. Enables org-wide rule sharing. Creating rules via agent: if `create_rule_block` tool enabled, the AI can generate `.md` files in `.continue/rules/`.

#### Known issues
Community reports (GitHub issue #6076, 2025) indicate rules in `.continue/rules/` are "completely ignored" by some extension versions — the toolbar shows them as enabled but the system prompt does not include them. Workaround: manually add rule content to global `config.yaml`. This is a documented stability gap.

#### **Patch-plasticity score: 3**
**Justification:** Persistent files in git-tracked location ✅, workspace + global + hub scoping ✅, conditional loading via glob/regex ✅, MCP servers in `config.yaml` ✅, Hub enables cross-team sharing ✅. Score 4 would require automated rule generation from feedback. Gap: known reliability issues with extension parsing.

---

### 7. Aider Conventions

**Official docs:** [https://aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html)

#### What persists
Aider uses a `CONVENTIONS.md` file (or any named file) as a persistent read-only instruction file.

> "You can tell aider to always consider CONVENTIONS.md as a read only file by adding it to the .aider.conf.yml file."

Configuration approaches:
| Method | Syntax |
|---|---|
| In-chat (per-session) | `/read CONVENTIONS.md` |
| CLI flag | `aider --read CONVENTIONS.md` |
| Persistent config | `read: CONVENTIONS.md` in `.aider.conf.yml` |
| Multiple files | `read: [CONVENTIONS.md, anotherfile.txt]` |

#### Operational characteristics
> "Files loaded via the `read` command or flag are marked as read-only."
> "Files are cached if prompt caching is enabled."
> "Effect on Output: Influences GPT to follow specific guidelines, such as library preferences (e.g., `httpx` vs `requests`) and coding styles."

The `.aider.conf.yml` config file is searched in:
1. Git root
2. Current working directory
3. Home directory

#### AGENTS.md integration
Aider is listed in AGENTS.md's supported tools, and the AGENTS.md spec notes: "Aider Configuration: Loaded via `.aider.conf.yml` using `read: AGENTS.md`."

#### `.aiderignore` for exclusions
Analogous to `.gitignore`, placed at git root.

#### Versioning
`CONVENTIONS.md` and `.aider.conf.yml` are plain files, typically committed to git alongside the codebase.

#### Honest gaps
- No project/user/team scoping hierarchy (flat: you choose what to read)
- No glob-based conditional inclusion
- No memory or automated feedback loop
- The system relies entirely on manual curation of the conventions file

#### **Patch-plasticity score: 2**
**Justification:** Persistent file-based instructions ✅, git-trackable ✅, auto-loaded via `.aider.conf.yml` ✅. No scoping hierarchy, no conditional inclusion, no memory layer, no MCP attachment. Score 2 is correct: this is intentionally minimal and composable.

---

### 8. Lovable Knowledge

**Official docs:** [https://docs.lovable.dev/features/knowledge](https://docs.lovable.dev/features/knowledge)

#### What persists
> "Knowledge lets you provide persistent instructions and context to the Lovable agent. Instead of repeating the same explanations in every conversation, you can define them once and Lovable will consider them when generating edits."

Two levels:
| Level | Storage | Max size | Managed by |
|---|---|---|---|
| Workspace knowledge | Database field (Settings → Knowledge) | 10,000 chars | Workspace owners/admins only |
| Project knowledge | Database field (Project settings → Knowledge) | 10,000 chars | Anyone with edit permission |

> "Workspace knowledge is a text field that lets you define shared rules once and apply them across all projects in your workspace."
> "Project knowledge is a text field that stores persistent instructions and context for a single project."

#### Loading mechanism
> "When you send a message, Lovable reads your project knowledge, workspace knowledge, and project code to understand how your project works before generating edits."

> "root-level CLAUDE.md, AGENTS.md files are always read by the Lovable agent regardless of session length."

Priority rule:
> "If the instructions conflict, Lovable is encouraged to prioritize the instructions defined in project knowledge, since they apply specifically to the current project."

#### Context length note
> "In very long conversations with a lot of context, instructions may not always be followed consistently."

#### Versioning
**No git-based versioning** for workspace/project knowledge — these are database text fields edited in the UI. However, Lovable docs note that repo-level files (CLAUDE.md, AGENTS.md) are also read, which would be git-tracked.

#### Team scoping
Workspace knowledge is an admin-only setting for cross-team guardrails — effective enterprise governance primitive. Multiple admins can edit; changes apply immediately.

> "Workspace admins can define guardrails such as coding standards, testing requirements, or architectural rules so every project follows the same conventions automatically."

#### Honest gaps
- Not git-tracked (the primary knowledge store is a database field)
- No conditional inclusion / glob support
- No MCP attachment
- No memory/skills layer
- No automated feedback writing

#### **Patch-plasticity score: 2**
**Justification:** Persistent database-backed instructions ✅, auto-loaded every session ✅, workspace + project scoping ✅. No versioning ❌, no git tracking ❌, no MCP, no memory, no automated feedback loop. The workspace admin scoping provides governance primitives but the lack of git history limits verifiability.

---

### 9. Replit replit.md

**Official docs:** [https://docs.replit.com/core-concepts/agent/replit-dot-md](https://docs.replit.com/core-concepts/agent/replit-dot-md)

#### What persists
> "Agent automatically creates this file in your project's root directory using proven best practices."
> "When Agent processes your requests, it automatically reads your replit.md file and uses its contents to: Understand your project's architecture and conventions; Follow your preferred coding patterns and style; Use your specified package managers and dependencies."

Key features:
| Feature | Details |
|---|---|
| File name | `replit.md` |
| Location | Project's root directory (required) |
| Auto-detection | Automatic once present |
| Auto-update | Agent can update file as it learns about project |
| Scope | Agent conversations only; does not apply to other AI tools |

#### Loading mechanism
> "Agent includes its contents in the context to help it understand your preferences, project structure, and coding style."
> "Agent will automatically detect and use this file in future conversations."

#### Auto-generation (score-4 feature)
A unique behavior: the agent itself creates and updates this file.
> "Agent first creates a `replit.md` file in your project's root directory using proven best practices."
> "Agent can also update your `replit.md` file as it learns more about your project."

From the [2025 Replit in Review blog post](https://blog.replit.com/2025-replit-in-review): "**Custom Agent Instructions via replit.md** let you personalize Agent behavior with coding style preferences, project context, and workflow settings."

#### Versioning
Repls can be git-backed (Replit supports GitHub integration). The file itself is a markdown file in the project root, readable and editable. Enterprise note: "Pre-configure `replit.md` in custom templates to give every builder in your organization a consistent starting context."

#### Honest gaps
- Not reliably always loaded — community reports indicate agent sometimes "forgets" the file between prompts
- No conditional/glob inclusion
- No MCP attachment documented
- The auto-update feature creates governance risk (agent can overwrite human instructions)

#### **Patch-plasticity score: 4**
**Justification:** Persistent root markdown file ✅, auto-loaded each session ✅, human-editable ✅, **agent autonomously writes and updates the file from project learning** ✅. This is the defining score-4 feature — automated feedback updates the scaffold. Score 5 would require a promotion/governance loop (e.g., human approval of agent-proposed updates). Known reliability gaps with loading consistency.

---

### 10. Zed AI Rules

**Official docs:** [https://zed.dev/docs/ai/rules](https://zed.dev/docs/ai/rules)

#### Supported file names (priority order)
| Priority | File |
|---|---|
| 1 | `.rules` |
| 2 | `.cursorrules` |
| 3 | `.windsurfrules` |
| 4 | `.clinerules` |
| 5 | `.github/copilot-instructions.md` |
| 6 | `AGENT.md` |
| 7 | `AGENTS.md` |
| 8 | `CLAUDE.md` |
| 9 | `GEMINI.md` |

> "Zed supports including `.rules` files at the root of a project's file tree, and they act as project-level instructions that are auto-included in all of your interactions with the Agent Panel."
> "Other names for this file are also supported for compatibility with other agents, but note that the first file which matches in this list will be used."

#### Loading mechanism
> "Project Rules: Automatically inserted at the beginning of each Agent Panel interaction if a supported file is found in the project root."

#### Rules Library (global rules)
> "Default Rules: Any rule in the Rules Library can be set as a 'default rule' by clicking the paper clip icon. Default rules are automatically inserted into context for every new Agent Panel interaction."
> "User/Global Scoping: Rules created in the Rules Library are stored locally and can be accessed at any time."

#### Versioning
Project `.rules` file (and any of the supported aliases) are in the project root, committed to git. Rules Library rules are local-machine storage only.

#### On-demand usage
> "Every rule in the Rules Library can be @-mentioned in the Agent Panel to insert the prompt manually."

#### Interop
Zed's multi-format support makes it the most interoperable rules consumer in the ecosystem: it reads `.cursorrules`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`.

#### MCP support
Zed supports custom MCP servers via agent panel configuration (`Add custom server`). Persistent memory via MCP is a community pattern (e.g., CORE Memory MCP documented by users).

#### Honest gaps
- No conditional inclusion / glob triggers within `.rules` file itself (only one file per project loaded)
- No auto-memory or feedback writing
- Rules Library lacks sync across machines

#### **Patch-plasticity score: 3**
**Justification:** Persistent git-tracked file ✅, auto-loaded at session start ✅, human-editable ✅, supports 9 different file format standards (maximum interop) ✅, MCP attachment supported ✅, Rules Library for user-level global defaults ✅. No conditional inclusion in base `.rules` format, no memory/skills auto-update loop.

---

### 11. VS Code Copilot / GitHub Copilot Instructions (VS Code)

**Official docs:** [https://code.visualstudio.com/docs/copilot/customization/custom-instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

#### What persists
> "Custom instructions enable you to define common guidelines and rules that automatically influence how AI generates code and handles other development tasks."

File formats:
| File | Scope | Auto-applied |
|---|---|---|
| `.github/copilot-instructions.md` | Workspace | Always (all chat requests) |
| `AGENTS.md` | Workspace / subfolder | Always (or subfolder-scoped) |
| `*.instructions.md` in `.github/instructions/` | Workspace | Conditional on `applyTo` glob |
| `~/.copilot/instructions` or `~/.claude/rules` | User profile | Across workspaces |

```json
"chat.instructionsFilesLocations": {
  ".github/instructions": true,
  ".claude/rules": true,
  "~/.copilot/instructions": false,
  "~/.claude/rules": false
}
```

> "VS Code automatically detects a `.github/copilot-instructions.md` Markdown file in the root of your workspace and applies the instructions in this file to all chat requests within this workspace."

#### AI-generated instructions (`/init` command)
> "VS Code can analyze your workspace and generate always-on custom instructions that match your coding practices and project structure."

Steps:
1. Discovers existing AI conventions (copilot-instructions.md, AGENTS.md)
2. Analyzes project structure and coding patterns
3. Generates comprehensive workspace instructions

Also `/create-instruction` for targeted rule generation and "extract an instruction from this" for extracting corrections from chat.

#### Priority
1. Personal instructions (user-level, highest priority)
2. Repository instructions (`.github/copilot-instructions.md` or `AGENTS.md`)
3. Organization instructions (lowest priority)

#### Versioning
`.github/copilot-instructions.md` and `.github/instructions/` are git-tracked workspace files. User profile instructions are local-machine.

#### **Patch-plasticity score: 3**
**Justification:** Persistent git-tracked files ✅, auto-loaded at session start ✅, user/repo/org scoping ✅, conditional inclusion via `applyTo` glob ✅, AI-generated instruction creation ✅, MCP via custom agent profiles ✅. The `/init` command auto-generates instructions from project analysis — approaching score 4 but does not autonomously write feedback-driven updates.

---

### 12. Cody / Sourcegraph

**Official docs:** [https://sourcegraph.com/docs/cody](https://sourcegraph.com/docs/cody)  
**Community reference:** [awesome-cody-commands](https://github.com/deepak2431/awesome-cody-commands)

#### What persists
Cody's primary persistent instruction mechanism is **custom commands** stored in `.vscode/cody.json` (VS Code) or the Prompt Library. Format: JSON file defining prompt + context.

> "Prompts: Automate key tasks in your workflow with premade and customizable prompts. Any common query or task can be built into a prompt to save and share with your team."

Separate `.cody/ignore` file (analogous to `.gitignore`) controls what context Cody can access.

#### Loading mechanism
Cody pulls context from the open file and repository by default, using Sourcegraph's search API for cross-codebase retrieval. Custom commands are user-invoked (not auto-loaded at session start in the same way as CLAUDE.md or `.cursor/rules`).

#### Versioning
`.vscode/cody.json` is committed to the workspace. The Prompt Library (cloud-stored) is not git-tracked.

#### Honest gaps
- **No auto-loading at session start** analogous to CLAUDE.md: Cody's commands are invoked, not injected into every session context
- No project-level always-on instruction file equivalent to `.cursorrules` documented in official sources (as of 2025)
- Team sharing is via the Sourcegraph Prompt Library, not git files
- Enterprise Starter plans discontinued July 2025, limiting enterprise availability

#### **Patch-plasticity score: 2**
**Justification:** Persistent `.vscode/cody.json` for custom commands ✅, git-tracked ✅. However, instructions are **not auto-loaded at session start** (manual invocation required) ❌. This limits the score: the persistence criterion is met but the "automatically loaded into model's context at session start" criterion is only partially met for commands (not for global instructions). Honest inclusion gap.

---

## Academic Citations: Persistent Context as Soft Adaptation

### Citation 1 (Empirical Impact — Strongest Evidence)

**Lulla, J.L., Mohsenimofidi, S., Galster, M., Zhang, J.M., Baltes, S., & Treude, C. (2026). "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents." arXiv:2601.20404.**

- **URL:** [https://arxiv.org/abs/2601.20404](https://arxiv.org/abs/2601.20404)
- **Published:** January 28, 2026 (v2: March 30, 2026)
- **Key finding:** AGENTS.md presence → **28.64% lower median runtime**, **16.58% lower output token consumption**, comparable task completion. N=10 repos, 124 PRs.
- **Why cite:** First empirical paper to quantify the operational effect of persistent repository-level instruction scaffolds on AI agent behavior. Directly supports the thesis that externalized scaffolds improve reliability and efficiency without weight updates.
- **Core quote:** "The presence of AGENTS.md is associated with a lower median runtime (Δ28.64%) and reduced output token consumption (Δ16.58%), while maintaining a comparable task completion behavior... These findings position AGENTS.md as a practical repository-level mechanism for shaping agent behavior."

### Citation 2 (Theoretical Framework — Context Adaptation vs. Fine-Tuning)

**Zhang, Q. et al. (2025). "Evolving Contexts for Self-Improving Language Models." arXiv:2510.04618.**

- **URL:** [https://arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618) (v3: March 2026)
- **Key finding:** ACE (Agentic Context Engineering) — context adaptation achieves +10.6% gains on agent benchmarks, +8.6% on finance benchmarks, without fine-tuning or labeled supervision.
- **Why cite:** Provides the theoretical framing of *context adaptation* as the formal alternative to weight updates:
  > "Modern AI applications based on large language models increasingly depend on *context adaptation*: modifying inputs with instructions, strategies, or evidence, rather than weight updates."  
  > "Adapting through contexts rather than weights offers several key advantages. Contexts are interpretable and explainable for users and developers, allow rapid integration of new knowledge at runtime, and can be shared across models or modules in a compound system."
- **Core contribution:** Frames system prompts and externalized scaffolds as first-class adaptation mechanisms — "evolving playbooks" — not workarounds for fine-tuning.

### Supporting citation (security evidence for system prompt primacy)

**Bai, Y. et al. (2025). "System Prompt Poisoning: Persistent Attacks on Large Language Models." arXiv:2505.06493.**

- **URL:** [https://arxiv.org/abs/2505.06493](https://arxiv.org/abs/2505.06493)
- **Key finding:** System prompts dominate user prompts in the instruction hierarchy. "Models prioritize instructions from the system prompt over redundant, benign instructions repeated in the user prompt."
- **Why cite (for Paper 3):** While a security paper, the findings confirm that system-level persistent instructions exercise strong behavioral control over LLMs — precisely the mechanism exploited in production scaffolds. The "clear hierarchy of instruction-following where the system-level context dominates" validates why externalized scaffolds function as reliable domain adaptation primitives.

---

## Comparison: File Format Interoperability Matrix

| File Format | Cursor | Copilot | Windsurf | Zed | Claude Code | Continue | Aider | VS Code |
|---|---|---|---|---|---|---|---|---|
| `AGENTS.md` | ✅ | ✅ | ✅ | ✅ (priority 7) | ✅ (symlink) | ❌ | ✅ | ✅ |
| `CLAUDE.md` | ❌ | ✅ | ❌ | ✅ (priority 8) | ✅ native | ❌ | ❌ | ✅ |
| `.cursor/rules/*.mdc` | ✅ native | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| `.github/copilot-instructions.md` | ❌ | ✅ native | ❌ | ✅ (priority 5) | ❌ | ❌ | ❌ | ✅ |
| `.windsurf/rules/*.md` | ❌ | ❌ | ✅ native | ❌ | ❌ | ❌ | ❌ | ❌ |
| `.continue/rules/*.md` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ native | ❌ | ❌ |
| `.rules` | ❌ | ❌ | ❌ | ✅ (priority 1) | ❌ | ❌ | ❌ | ❌ |
| `CONVENTIONS.md` (read:) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ native | ❌ |

**Key observation:** AGENTS.md is the only format with near-universal adoption across 5+ major tools. CLAUDE.md is second (4 tools). All other formats are proprietary to a single tool.

---

## Adoption Numbers Summary

| System | Adoption Anchor |
|---|---|
| AGENTS.md | 60,000+ GitHub repos (Linux Foundation, Dec 2025) |
| GitHub Copilot | >4M users (GitHub Universe 2024) |
| Cursor | ~4M users (TechCrunch 2025) |
| Continue.dev | >1M VS Code installs |
| Claude Code | Millions of CLAUDE.md files in public repos (inferred from Anthropic blog posts) |

---

## Honest Gaps and Underdocumented Systems

### Cody/Sourcegraph
- **Gap:** No documented always-on session-start instruction file equivalent; custom commands are invoked, not injected. Enterprise Starter discontinued July 2025.
- **Status:** Partial credit (score 2); inclusion criterion #2 (auto-loaded at session start) is only weakly met.

### Continue.dev
- **Gap:** Known parsing bugs where `.continue/rules/` files are visible in UI but ignored in actual system prompts (GitHub issue #6076, confirmed 2025). Production reliability unclear.
- **Status:** Documented feature, reliability caveat noted.

### Aider
- **Gap:** No scoping hierarchy, no conditional inclusion, no glob patterns. Convention files are manually listed in `.aider.conf.yml`. Intentional minimalism.
- **Status:** Score 2 is accurate; not a limitation but a design choice.

### Lovable Knowledge
- **Gap:** DB-stored text fields; not git-tracked; no YAML/glob conditional inclusion; no MCP. Character limit (10k) is restrictive for complex projects.
- **Status:** Score 2. Enterprise use limited by lack of version control.

### Replit replit.md
- **Gap:** Reliability issues documented in community forums — agent sometimes skips the file mid-session. Auto-update can overwrite human instructions unexpectedly.
- **Status:** Score 4 for the architectural design; real-world reliability is score 2-3.

---

## Scoring Summary with Justifications

| System | Score | Key Reason |
|---|---|---|
| Claude Code CLAUDE.md | **4** | Multi-scope (managed/user/project/local), org IT-deployable, auto-memory writes scaffold from feedback |
| Replit replit.md | **4** | Agent auto-generates and updates the file — but reliability gaps |
| Cursor Rules | **3** | .mdc format, 4 trigger types, git-versioned, nested rules, MCP supported |
| GitHub Copilot Custom Instructions | **3** | Multi-format (AGENTS.md + CLAUDE.md + GEMINI.md + copilot-instructions.md), repo/user/org scoping, AI-generated |
| Windsurf Cascade Rules | **3** | Enterprise system-level rules, 4 trigger modes, memories layer, git-tracked workspace |
| Continue.dev Rules | **3** | 3-tier hierarchy (hub/workspace/global), glob+regex conditions, MCP servers, Hub sharing |
| Zed AI Rules | **3** | 9-format interop (widest), auto-load, Rules Library, MCP supported |
| VS Code Copilot Instructions | **3** | All formats + AI-generated init, user/repo/org, conditional glob, custom agents |
| AGENTS.md (base format) | **2** | Cross-tool open standard, 60k+ adoption, git-tracked, but format itself has no scoping/conditions |
| Aider Conventions | **2** | Persistent + git-tracked + auto-loaded via config, but flat/manual, no scoping |
| Lovable Knowledge | **2** | Workspace+project scoping, instant apply, but DB-stored (no git), no conditions |
| Cody/Sourcegraph | **2** | Git-tracked commands but not auto-loaded at session start |
