# Substrate 6: Governance, Versioning, and Promotion Loops
## Evidence Harvest for Paper 3 — Patch-Plastic Architecture Trilogy

**Harvest date:** 2026-05  
**Scope:** Systems with explicit scaffold governance — versioned rules/skills/memories, promotion mechanisms from local to shared scope, eval-gated promotion, and auditable change logs.  
**Rubric:** 0 = none; 1 = ad-hoc/single-user; 2 = versioned but no promotion gate; 3 = versioned + explicit scope hierarchy; 4 = versioned + eval-or-manual gate + rollback; 5 = full two-loop (eval → promotion → org-wide rollout, auditable, rollback).

---

## Scored Summary Table

| System | Versioning | Promotion Gate | Audit Trail | Local→Shared | Rollback | **Score** |
|--------|-----------|----------------|-------------|--------------|----------|-----------|
| **Braintrust** | Content-addressed IDs, immutable, full diff | CI/CD GitHub Action + eval threshold gate | Complete: author, timestamp, eval results, traces | dev → staging → prod (3 environments) | Instant, no redeploy | **5** |
| **Vellum** | Semantic-versioned release tags, env-scoped | Protected Release Tags require reviewer approval + zero outstanding change requests | Deployment descriptions, release history per env | sandbox → staging → prod | Tag reassignment | **5** |
| **LangSmith Hub** | Immutable commit hashes, tag pointers | Prompt Owners RBAC, webhook-triggered CI/CD, manual Staging→Production promotion UI | Commit hash, author, timestamp, model config | personal → org workspace → staging → prod | Point tag to prior commit hash | **5** |
| **AGENTS.md / Agentic AI Foundation** | Git-tracked `.md` files, PR-reviewed, same rigor as code | PR review (code review parity); Linux Foundation AAIF governance since Dec 2025 | Full git history, PR discussion threads | local `.cursor/rules` → repo AGENTS.md → org standard → AAIF governed spec | Git revert | **5** |
| **Anthropic `skills` repo** | Git with 956+ PRs, Apache 2.0 open-source skills | PR review by maintainers (120k stars, 14 contributors); no automated eval gate | Full git commit history, PR threads | personal SKILL.md → PR → shared `anthropics/skills` → Claude Code marketplace | Git revert/rollback | **4** |
| **GitHub Copilot enterprise** | Git-tracked `.github/copilot-instructions.md`; org-level UI setting (GA April 2026) | PR review for repo instructions; admin-only org settings UI for org-wide instructions | Git history for file; no dedicated audit log for org UI setting | personal → repo-scoped → path-scoped → org-wide | Git revert / admin UI edit | **4** |
| **Cursor Rules** | `.cursor/rules/*.mdc` files in git repo; team-shared via git commit | PR review (convention); no automated eval gate | Git history | user-global → project-repo → team-shared-in-git | Git revert | **3** |
| **DSPy compile** | JSON/pickle saved programs; manual versioning via file path naming (e.g. `v1.json`) | None built-in; relies on external CI; eval metrics drive optimization within compile loop | No native audit log; JSON files inspectable | compile-time local → manually shared file/repo | Reload prior JSON | **3** |
| **TextGrad** | In-memory variable optimization; no persistent versioning built-in | Eval loop (loss function) drives updates, but no deployment gate | None — transient computation graph | No promotion mechanism (all local) | Re-run from original value | **2** |
| **OPRO** | Text file output of optimized instructions; no native versioning | Eval accuracy gates next optimization step (in-loop only) | None beyond run logs | No promotion mechanism | Re-run | **2** |
| **NanoResearch (2605.10813)** | Append-and-merge skill bank: `S^(t+1) = S^(t) ∪ Distill(τ)` — no version IDs or diffs | Automated semantic merging by Orchestrator; no external review or eval threshold | No audit log; growth tracked as count only (Table 4) | Skills reusable across projects (same user); no org-shared pool described | No rollback — additive only | **2** |
| **LangFuse** | Numeric version IDs + labels (staging, production); protected labels for RBAC | Label assignment by admins (RBAC); no eval gate built in | Version diff view; label change history | self-hosted or cloud org scope; per-project | Set `production` label to prior version ID | **3** |
| **Agenta** | Git-like branching + commit history per variant; multi-environment (dev/staging/prod) | Manual deployment through environment promotion UI; no eval threshold gate | Full version history, environment deployment log | project → team → org workspace | Deploy prior version to env | **3** |
| **W&B Weave (Prompts)** | Auto-versioned on every `weave.publish()`; content-hashed; complete history | No gate — publish-on-change; eval integration via Weave Evals but not blocking | Version history with comparison; linked to traces | per-project within org | Load prior version object | **3** |
| **OpenAI AgentKit Evals** | Agent Builder with visual versioning of multi-agent workflow nodes (beta Oct 2025) | Trace grading + automated prompt optimization + human annotation as pre-deploy gate | Eval dataset traces, grader outputs, version history | individual dev → deployed agent endpoint | Revert to prior workflow version | **3** |
| **Constitutional AI (Anthropic)** | Constitution document version-controlled at Anthropic (not public git) | Multi-stage: SL critique-revise → RL from AI Feedback → human eval; internally gated | Internal governance only; constitution published publicly | Internal: Anthropic research process | Retrain with revised constitution | **2** |
| **Inspect AI (UK AISI)** | Python eval scripts in git (`inspect_evals` GitHub repo); CHANGELOG.md | CI-like: reproducible evals run on any model; pass/fail gates; used by Anthropic, DeepMind, Grok | Per-step traces, cost logs, scorer heatmaps; tamper-proof logs for SOC2 | AISI internal → open-source community contributions via PR | Git revert; reload prior eval | **3** |
| **Self-Refine (Madaan et al. 2023)** | No versioning — in-context iteration only | No gate; iterates until stopping criterion | No audit trail | No promotion mechanism | N/A — test-time only | **1** |
| **Cleric.ai** | Dynamic operational memory graph built from incident trajectories; no explicit versioning | Continuous learning from high-frequency operational data (implicit quality gate via outcome) | "Every investigation compounds Cleric's understanding" — operational memory | Per-customer environment; not cross-customer | No described rollback | **2** |
| **Sierra AI (Ghostwriter)** | Agent harness ("scaffolding") editable via Ghostwriter agent in sandboxed environment; changes validated before deployment | Sandbox validation + supervisor model checks before production promotion | "Test and safely validate changes in a sandboxed environment" | Per-deployment; no cross-customer scope described | Sandbox validates before overwriting | **2** |
| **Decagon** | Agent Operating Procedures (AOPs) as versioned templates (Feb 2026 launch) | Layered guardrail models gate responses at runtime; AOP template reviews | Guardrail model audit at every stage; AOP template history | AOP templates shared across Decagon platform | Prior AOP version | **2** |

---

## Per-System Evidence Entries

---

### 1. Braintrust — Score: **5/5**

**Classification:** Full two-loop patch-plastic system.

**Versioning mechanism:**  
Every prompt change is assigned a **content-addressable version ID** derived from the prompt's content. Identical prompts produce the same ID. Versions are **immutable** — modification creates a new version, never overwrites. Complete history with visual diffs is maintained. Teams manage prompts via UI or programmatically with `braintrust push` / `braintrust pull` SDK commands.

**Promotion gate:**  
Three-stage environment pipeline: **Development → Staging → Production**. Promotion requires passing defined evaluation thresholds (e.g., ≥90% on a golden dataset). A **dedicated GitHub Action** runs evaluation suites on every pull request modifying a prompt; merges are blocked when quality drops below thresholds. Gates are layered: deterministic checks (structure/JSON schema) → semantic checks (embedding similarity, key fact coverage) → LLM-as-judge → non-functional (latency/cost). Human annotation queues for high-stakes cases.

**Audit trail:**  
Metadata per version: author, timestamp, rationale, linked model/parameter settings, evaluation results. Every production output is traceable to its exact prompt version, model, and parameters via production traces.

**Local vs. shared scope:**  
Development environment is individual/team; staging mirrors production conditions; production is org-wide. RBAC controls who can promote.

**Rollback:**  
Instant: traffic redirected to last known-good version. No redeployment needed. Failing versions become test cases to prevent recurrence.

**Key quote:**  
> "Prompt versions that fail evaluation in staging cannot be automatically promoted to production." — Braintrust docs, 2026

> "A dedicated GitHub Action runs evaluation suites on every pull request and blocks merges when quality drops below thresholds." — Braintrust prompt versioning guide, Feb 2026

**Reference:**  
[Braintrust prompt versioning guide](https://www.braintrust.dev/articles/what-is-prompt-versioning) (Feb 2026); [Braintrust prompt management](https://www.braintrust.dev/articles/what-is-prompt-management) (Feb 2026).

---

### 2. Vellum — Score: **5/5**

**Classification:** Full two-loop with mandatory human review gate.

**Versioning mechanism:**  
Semantic-versioned **Release Tags** per environment. Static Release Tags create unique version identifiers tied to each deployment. Environment-scoped: each environment (dev, staging, production) maintains its own separate release history. Org-level default release tags configurable (June 2025 update).

**Promotion gate:**  
**Protected Release Tags** (April 2025 launch): releases marked "protected" require at minimum one reviewer approval AND zero outstanding change requests before they can be assigned to a Prompt/Deployment. Inspired by GitHub PR reviews. Manual approval gate at production boundary.

**Audit trail:**  
Deployment descriptions per release; per-environment release history with timestamps; reviewer approval records (March 2025 "Deployment Release Reviews" feature).

**Local vs. shared scope:**  
Sandbox (development) → Staging → Production. API keys are environment-scoped; release tag resolution is environment-aware.

**Rollback:**  
Reassign release tag to prior version; or pin to a static release tag in code. No redeployment required.

**Key quote:**  
> "Protected Release Tags — a feature which will enforce Releases marked as 'protected' to have at least one approval from a Reviewer and have zero outstanding change requests before it can be assigned to a Prompt/Deployment." — Vellum product update, April 2025

**Reference:**  
[Vellum Release Tags docs](https://docs.vellum.ai/product/deployments/release-tags); [Vellum April 2025 product update](https://www.vellum.ai/blog/vellum-product-update-april-2025).

---

### 3. LangSmith Hub — Score: **5/5**

**Classification:** Full two-loop with git-parity commit model.

**Versioning mechanism:**  
Every `push_prompt` call creates an **immutable commit with a unique hash** capturing the exact prompt, variables, and model configuration. `staging` and `production` are **tag pointers** that move between commits — they do not overwrite values. Webhook triggers fire on every commit (for CI/CD pipeline automation).

**Promotion gate:**  
**Prompt Owners** feature (RBAC): fine-grained control over who can tag commits and delete prompts — limiting production promotion to authorized team members. Webhook-triggered CI/CD pipeline integration. Staging→Production promotion UI with confirmation modal showing what will be replaced.

**Audit trail:**  
Commit hash, author, timestamp, associated model config. Every production trace shows exactly which prompt version was used.

**Local vs. shared scope:**  
Personal (private) → Org workspace (shared). Public prompt hub for community-created prompts. Rollback is sub-5-minute, no redeployment.

**Rollback:**  
One SDK call: point tag to a prior commit hash. No deployment, no merge, no pipeline.

**Key quote:**  
> "LangSmith Hub treats prompts like code: Every `push_prompt` call = immutable commit with a hash. `staging` and `prod` are tag pointers that move between commits, not values that get overwritten. Rollback is one SDK call." — LangChain community spotlight, March 2026

> "Environments represent named deployment targets, Staging and Production, that you can assign to specific commits." — LangSmith docs, May 2026

**Reference:**  
[LangSmith manage prompts docs](https://docs.langchain.com/langsmith/manage-prompts) (May 2026); [LangChain community spotlight](https://www.linkedin.com/posts/langchain-oss_langchain-community-spotlight-production-activity-7443703468844036097-InfI) (March 2026).

---

### 4. AGENTS.md / Agentic AI Foundation — Score: **5/5**

**Classification:** Governed open standard with institutional promotion loop. Unique: scaffold governance for agent configuration files at ecosystem scale.

**Versioning mechanism:**  
AGENTS.md files are **git-tracked Markdown files** stored in repository roots (or subdirectories for scoped rules). Treated with same review rigor as code. Changes go through pull requests. OpenAI maintains ~88 nested AGENTS.md files across their repositories. The file is hierarchical: subdirectory AGENTS.md overrides parent, enabling scoped rules.

**Promotion gate:**  
PR-based review by repository owners. The **Agentic AI Foundation (AAIF)** under the Linux Foundation (founded December 9, 2025 by OpenAI, Anthropic, Block) now governs the AGENTS.md specification — providing institutional oversight, versioning of the standard itself, and cross-vendor promotion governance.

**Audit trail:**  
Full git history with PR discussion threads. Harness.io: "Instruction drift is as dangerous as code drift. Version-controlled agent guidance becomes part of your engineering contract."

**Local vs. shared scope:**  
`~/.cursor/rules` (user-global) → `.cursor/rules/*.mdc` (project-local) → `.github/copilot-instructions.md` (repo-wide) → AGENTS.md (open standard, 60,000+ projects) → AAIF governed spec (ecosystem-wide). The "closest file in the directory tree takes precedence."

**Rollback:**  
Git revert on any AGENTS.md file.

**Adoption scale:**  
60,000+ open-source projects; supported by Codex, Cursor, Devin, Factory, Gemini CLI, GitHub Copilot, Jules, VS Code, and others.

**Key quote:**  
> "Changes to these files should follow the same review rigor as code changes. Instruction drift is as dangerous as code drift. Version-controlled agent guidance becomes part of your engineering contract." — Harness.io, March 2026

> "AGENTS.md transforms prompt engineering from a personal habit into a shared, reviewable, versioned discipline." — Harness.io, March 2026

**Reference:**  
[Linux Foundation AAIF announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (Dec 9, 2025); [agents.md spec](https://agents.md); [GitHub agentsmd/agents.md](https://github.com/agentsmd/agents.md); [Harness.io analysis](https://www.harness.io/blog/the-agent-native-repo-why-agents-md-is-the-new-standard) (March 2026).

---

### 5. Anthropic `anthropics/skills` GitHub Repository — Score: **4/5**

**Classification:** PR-based promotion mechanism from personal SKILL.md to shared org pool.

**Versioning mechanism:**  
Git repository with 956+ merged PRs as of April 2026. Skills are self-contained folders with `SKILL.md` files (YAML frontmatter: `name`, `description`; Markdown content with instructions and examples). Apache 2.0 open-source for most skills; source-available for document skills. 120k stars, 14 contributors, 13.8k forks.

**Promotion gate:**  
**PR-based review by Anthropic maintainers**. Contributors must submit a PR; maintainers review and merge. No automated eval gate is documented — quality assurance relies on human review. The `spec/` directory contains the Agent Skills specification; `template/` provides the canonical skill template.

**Scope levels:**
- Local: personal SKILL.md file in any directory
- Shared: published to `anthropics/skills` GitHub repo
- Production: available in Claude Code marketplace via `/plugin marketplace add anthropics/skills`; also installable in Claude.ai (paid plans) and via Claude API

**Audit trail:**  
Full git commit history with PR numbers and commit messages. 14 branches. No semantic versioning tags (0 tags, 0 releases).

**Rollback:**  
Git revert on any commit; prior versions accessible via commit hash.

**Gap:**  
No automated eval gate; no canary deployment; no formal version scheme for individual skills. The promotion is manual review only.

**Key quote:**  
From repo fetch: "No automated evaluation gates, validation tests, or CI/CD gates are mentioned; the page only states users should 'test skills thoroughly in your own environment.'"

**Reference:**  
[anthropics/skills GitHub](https://github.com/anthropics/skills) (fetched April 2026).

---

### 6. GitHub Copilot Enterprise Instructions — Score: **4/5**

**Classification:** Three-tier scope hierarchy with org-wide rollout; no eval gate.

**Versioning mechanism:**  
- Repository instructions: `.github/copilot-instructions.md` — **git-tracked**, versioned with the codebase
- Path-specific instructions: `.github/instructions/*.instructions.md` with `applyTo` glob frontmatter
- Org-wide instructions: set via GitHub Organization Settings UI (not git-tracked for org-level setting)
- The file-based instructions can be auto-generated by Copilot coding agent via PR

**Promotion gate:**  
- Repo instructions: standard PR review workflow
- Org instructions: admin-only settings (Organization owners only; Copilot Business/Enterprise required)
- Org-level instructions went **Generally Available April 2, 2026** after first introduced April 2025
- No eval gate or automated quality check for instructions

**Scope:**  
Personal (global settings) → Workspace (single IDE workspace) → Repository-wide (all requests in repo context) → Path-specific (matching files) → **Organization-wide** (all repos in org, applied to Copilot Chat on GitHub.com, code review, cloud agent).

**Audit trail:**  
Git history for file-based instructions. Org UI setting has no independent audit log.

**Rollback:**  
Git revert for file-based instructions; admin UI edit for org settings.

**Key quote:**  
> "With organization custom instructions, Copilot Business and Copilot Enterprise organization administrators can set default instructions that guide Copilot's behavior across all repositories in their organization." — GitHub Changelog, April 2, 2026

**Reference:**  
[GitHub Copilot org instructions docs](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-organization-instructions); [GitHub Changelog April 2026](https://github.blog/changelog/2026-04-02-copilot-organization-custom-instructions-are-generally-available/).

---

### 7. Cursor Rules — Score: **3/5**

**Classification:** Git-versioned scaffold with team sharing but no promotion gate.

**Versioning mechanism:**  
`.cursor/rules/*.mdc` files (Markdown with YAML frontmatter) stored in the project repository. Teams commit these files to git like any configuration file. Rule types: `always` (always included), `auto-attached` (glob-triggered), `agent-requested` (on-demand), `manual` (explicit invocation).

**Promotion gate:**  
PR review by convention only. No automated eval gate, no environment staging, no admin-enforced promotion.

**Scope:**  
User-global (`~/.cursor/rules/`) → Project-local (`.cursor/rules/` in repo, shared via git commit) → Team-shared (same file, committed to team repo). No separate org-level scope distinct from repo.

**Audit trail:**  
Full git history. No Cursor-native audit UI.

**Rollback:**  
Git revert.

**Key finding:**  
Cursor rules demonstrate the "prompts as code" paradigm but stop short of eval-gated promotion. The team-sharing mechanism is entirely dependent on git discipline rather than a built-in governance layer. `cursorrules.org` notes: "Treat [rules] like any other config file" and "Cursor's cloud sync can help distribute it."

**Reference:**  
[Cursor docs](https://docs.cursor.com/context/rules); [cursorrules.org guide](https://cursorrules.org/blog/mastering-cursor-rules-developer-blueprint-context-aware-ai); [Reddit Cursor forum](https://www.reddit.com/r/cursor/comments/1icmmb0/cursorrules_rules_for_ai_or_project_rules/) (Jan 2025).

---

### 8. DSPy — Score: **3/5**

**Classification:** Eval-driven compilation with manual versioning; no native promotion infrastructure.

**Versioning mechanism:**  
Compiled programs saved as **JSON files** (`program.save("./v1.json")`) or as a directory (whole-program save including architecture). Human-assigned file names serve as the versioning system (e.g., `mipro_optimized_v1.json`). Explicitly recommended to use same DSPy version for save/load.

**Promotion gate:**  
**Within compilation**: optimizer (MIPROv2, BootstrapFewShot, GEPA, BootstrapFinetune) iterates against a metric function, keeping candidates that improve the score. This is an internal eval loop, not a deployment gate. **After compilation**: no built-in mechanism to gate deployment to staging/production.

**Roadmap gap:**  
DSPy roadmap explicitly lists "Building end-to-end tutorials from DSPy's ML workflow to deployment" and "Shifting towards more interactive optimization & tracking" as future work — acknowledging that the promotion loop is incomplete.

**Audit trail:**  
JSON files are human-readable and inspectable ("you can open and inspect it with any text editor"). No native diff, history, or metadata.

**Local vs. shared:**  
Files can be shared via git or file system manually; no native team workspace or promotion workflow. The compile step itself stays local.

**Rollback:**  
Load any previously saved `.json` file.

**Key quote:**  
> "Saving allows us to reload the optimized system during a different session... It enables sharing optimized programs with teammates or deploying them to production environments." — DSPy saving tutorial

> "the framework for programming—rather than prompting—language models." — dspy.ai (analogy to compiler: source code → optimized binary)

**Reference:**  
[DSPy saving tutorial](https://dspy.ai/tutorials/saving/); [DSPy site](https://dspy.ai); [DSPy roadmap](https://dspy.ai/roadmap/).

---

### 9. TextGrad — Score: **2/5**

**Classification:** Automated in-loop gradient-descent on text scaffolds; no persistence or promotion.

**Versioning mechanism:**  
None built-in. TextGrad operates on in-memory `tg.Variable` objects. The "gradient" is textual feedback from an LLM; the optimizer (`TGD`) applies it to update the variable. Final optimized values exist only in Python memory unless the user manually serializes them.

**Promotion gate:**  
The eval loop itself functions as an implicit gate (optimization stops when loss plateaus), but there is no deployment gate, staging environment, or human review. The framework is research-oriented, not production-deployment oriented.

**Technical mechanism:**  
```
Prediction = LLM(Prompt + Question)
Evaluation = LLM(Evaluation_Instruction + Prediction)
Prompt_new = TGD.step(Prompt, ∂Evaluation/∂Prompt)
```

**Audit trail:**  
None — transient computation graph. No logging, history, or diff.

**Local vs. shared:**  
All local (in-process). No promotion to shared/org scope.

**Rollback:**  
Restart from original `tg.Variable` value.

**Paper scope:**  
TextGrad is the clearest academic demonstration of **automated scaffold optimization** — but purely as a research primitive. It has the inner loop of Substrate 6 (eval-driven update) without any of the outer loop (governance, promotion, audit).

**Key quote:**  
> "TextGrad backpropagates textual feedback provided by LLMs to improve individual components of a compound AI system... improves zero-shot accuracy of GPT-4o in Google-Proof Question Answering from 51% to 55%." — TextGrad paper (arXiv:2406.07496, June 2024)

**Reference:**  
[TextGrad paper](https://arxiv.org/abs/2406.07496) (arXiv:2406.07496, June 2024); [TextGrad GitHub](https://github.com/zou-group/textgrad); [Stanford HAI analysis](https://hai.stanford.edu/news/textgrad-autograd-text).

---

### 10. OPRO (Large Language Models as Optimizers) — Score: **2/5**

**Classification:** Eval-driven automated prompt optimization; no versioning or promotion.

**Versioning mechanism:**  
Output is text instructions appended to a file. No version IDs, history, or diffs.

**Promotion gate:**  
Implicit within the optimization loop: LLM generates new instructions from a prompt containing previously generated solutions with their scores; instructions are evaluated and those with higher accuracy scores replace or augment prior candidates. This is an **inner loop only** — no deployment gate.

**Technical mechanism:**  
At each step: LLM generates new solutions from a prompt containing prior solutions + values → evaluated on task → best solutions kept → fed back to next step. Best prompts outperform human-designed ones by up to 8% on GSM8K and 50% on Big-Bench Hard tasks.

**Audit trail:**  
Run logs only. No persistent versioning.

**Limitations:**  
Review (ACL 2024, "Revisiting OPRO") shows limited effectiveness on small-scale LLMs with limited inference capabilities. Scope is research benchmark optimization, not production scaffold governance.

**Reference:**  
[OPRO paper](https://arxiv.org/abs/2309.03409) (arXiv:2309.03409, Sept 2023); [OPRO GitHub](https://github.com/google-deepmind/opro); [Revisiting OPRO, ACL 2024](https://aclanthology.org/2024.findings-acl.100/).

---

### 11. NanoResearch (arXiv:2605.10813) — Score: **2/5**

**Classification:** Automated co-evolution of skill bank + memory + policy; no versioning or external governance.

**Versioning mechanism:**  
**None.** The skill bank update is strictly additive and merge-based:
```
S^(t+1) = S^(t) ∪ Distill_skill(τ)
M^(t+1) = M^(t) ∪ Summarize_mem(τ)
```
No version IDs, diffs, or snapshots. Growth is tracked only as entry count (Table 4: skill bank grows from 0.80 to 2.30 entries per topic across R1–R3).

**Promotion gate:**  
**Automated by Orchestrator only**: upon completing a stage, the Orchestrator reflects over the trajectory (actions, critiques, outcomes) and distills generalizable rules into the Skill Bank and project-specific experiences into Memory. Semantic overlap merging prevents unbounded growth. No human review, no eval threshold gate, no external promotion.

**Scope:**  
Skill Bank is **user-scoped and project-reusable** ("reusable across projects" but per-user). Memory is **user-bound and project-bound**. No cross-user shared skill pool described.

**Audit trail:**  
None. No mechanism to inspect what changed between rounds or why.

**Rollback:**  
None — additive-only design. Cannot revert a skill distillation.

**Policy co-evolution:**  
Label-free SDPO (Supervised Direct Preference Optimization) converts free-form user feedback into persistent planner parameter updates — the most sophisticated of the three layers, but still entirely internal.

**Paper significance:**  
Tri-level co-evolution (skill + memory + policy) across three research rounds is the most architecturally complete academic example of Substrates 1–5 co-evolving. It achieves the inner loop (continuous self-improvement) but has **no outer loop** (no governance, no audit, no promotion to shared scope). Skills are also 2026-era: paper published May 11, 2026.

**Key quote:**  
> "A skill bank distills recurring operations into compact procedural rules reusable across projects... the Orchestrator merges semantically overlapping entries to keep both stores compact for future cycles." — arXiv:2605.10813

**Reference:**  
[NanoResearch arXiv](https://arxiv.org/abs/2605.10813) (May 11, 2026); [HuggingFace paper page](https://huggingface.co/papers/2605.10813).

---

### 12. LangFuse — Score: **3/5**

**Classification:** Versioned prompt management with label-based promotion and RBAC; no eval gate.

**Versioning mechanism:**  
Every prompt version is auto-assigned a numeric `version ID`. Labels (e.g., `staging`, `production`, `latest`, custom tenant/experiment labels) are movable pointers to specific versions. Diff view shows changes between versions.

**Promotion gate:**  
**Protected labels** (RBAC): project admins/owners can prevent labels from being modified or deleted — ensuring only authorized users can promote to production. No automated eval threshold gate.

**Audit trail:**  
Version history with diff view; label change history.

**Local vs. shared:**  
Per-project within a Langfuse org (self-hosted or cloud). Production label serves as the promotion target.

**Rollback:**  
Set `production` label to a prior version ID in the UI.

**Key quote:**  
> "To 'deploy' a prompt version, you have to assign the label `production` or any environment label you created to that prompt version." — Langfuse docs

> "Currently, Langfuse lacks a definitive approval process before changes are deployed to production." — Reddit, March 2026 (community acknowledgment of governance gap)

**Reference:**  
[Langfuse prompt version control docs](https://langfuse.com/docs/prompt-management/features/prompt-version-control).

---

### 13. Agenta — Score: **3/5**

**Classification:** Git-like open-source LLMOps with branching, environments, and collaboration.

**Versioning mechanism:**  
Git-like branching + commit history per variant. Multiple variants (branches) of a prompt, each with own commit history. OpenTelemetry-based tracing links every output to its exact prompt version.

**Promotion gate:**  
Manual deployment through environment promotion UI. No eval threshold gate for automated blocking, though evals can inform the decision.

**Scope:**  
Dev → Staging → Production. Team collaboration via UI (non-engineers can edit without code changes).

**Rollback:**  
Deploy a prior version to the environment.

**Reference:**  
[Agenta prompt versioning guide](https://agenta.ai/blog/prompt-versioning-guide) (Feb 2026); [Agenta open-source platforms comparison](https://agenta.ai/blog/top-open-source-prompt-management-platforms) (Dec 2025).

---

### 14. W&B Weave (Prompts) — Score: **3/5**

**Classification:** Auto-versioned prompt objects with org-scope sharing; no eval gate.

**Versioning mechanism:**  
`weave.publish(prompt, name="calculator_prompt")` — every publish with the same name but different content creates a new version while preserving all previous versions. Content-hashed versioning.

**Promotion gate:**  
None built-in. Eval integration exists (Weave Evals) but does not block deployment.

**Scope:**  
Per-project within W&B org. Dataset and model versioning via W&B Artifacts at the pipeline level.

**Rollback:**  
Load any prior version object.

**Reference:**  
[W&B Weave Prompts docs](https://docs.wandb.ai/weave/guides/core-types/prompts).

---

### 15. OpenAI AgentKit Evals — Score: **3/5**

**Classification:** Eval-informed agent workflow versioning; no hard gate but structured optimization loop.

**Versioning mechanism:**  
**Agent Builder** provides a visual canvas for creating and **versioning multi-agent workflows** (node graphs). GA with standard API pricing as of October 6, 2025.

**Promotion gate:**  
New eval capabilities: datasets, **trace grading** (end-to-end workflow assessment), **automated prompt optimization** (generate improved prompts from human annotations + grader outputs), third-party model evaluation. These inform but do not block promotion — "continuous measurement to raise task accuracy."

**Scope:**  
Individual developer → Connector Registry (admin-managed, org-wide integration governance, requires Global Admin Console).

**Audit trail:**  
Eval dataset traces, grader outputs, human annotation records.

**Rollback:**  
Prior workflow version in Agent Builder.

**Key quote:**  
> "New capabilities include datasets, trace grading for end-to-end workflow assessment, automated prompt optimization, and third-party model evaluation. OpenAI emphasizes continuous measurement to raise task accuracy." — MarktechPost analysis, Oct 2025

**Reference:**  
[OpenAI AgentKit announcement](https://openai.com/index/introducing-agentkit/) (Oct 6, 2025).

---

### 16. Constitutional AI (Anthropic) — Score: **2/5**

**Classification:** Internally governed scaffold update process; not externally observable as versioned artifacts.

**Versioning mechanism:**  
The "constitution" (set of ~10 human-authored principles) is version-controlled internally at Anthropic. Anthropic has published the constitution publicly, but the update process is not a public git workflow.

**Promotion gate:**  
Multi-stage: (1) Supervised Learning phase: sample → self-critique → revision → finetune on revised responses. (2) RL phase: sample → AI evaluates pairs → preference model → RLAIF. Human evaluation at each stage provides quality gates.

**Scope:**  
Internal Anthropic research pipeline → trained Claude model weights (global). No local-to-shared promotion in the scaffold governance sense.

**Audit trail:**  
Internal. Constitution published publicly as a governance transparency mechanism.

**Significance for paper:**  
CAI is the clearest example of **the constitution as a versioned scaffold artifact** governing LLM behavior. The critique-revise loop is an automated inner loop; the human oversight at each training phase is the outer loop. But because it operates at the model-weight level rather than the scaffold/prompt layer, and governance is internal, it does not demonstrate the external two-loop architecture.

**Reference:**  
[Constitutional AI paper](https://arxiv.org/abs/2212.08073) (arXiv:2212.08073, Dec 2022); [Anthropic research page](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback).

---

### 17. Inspect AI (UK AISI / Meridian Labs) — Score: **3/5**

**Classification:** Reproducible eval framework used as a governance layer for scaffold promotion; not a scaffold manager itself.

**Versioning mechanism:**  
Eval scripts in git (`UKGovernmentBEIS/inspect_evals` GitHub repo). CHANGELOG.md tracks version history. Used for nearly all UK AI Security Institute automated evaluations; adopted by Anthropic, DeepMind, Grok.

**Promotion gate:**  
Provides the infrastructure for eval-gated promotion — pass/fail gates with bootstrap confidence intervals, LLM-as-judge scoring, cost/token tracking. Used by production teams as the gate layer in deployment pipelines. SOC2-compatible tamper-proof logs.

**Scope:**  
Open-source community contributions via PR (200+ pre-built evaluations). Used as org-internal and cross-org eval infrastructure.

**Audit trail:**  
Per-step traces, cost logs, scorer heatmaps via Inspect View; VS Code extension for authoring. Regulatory/SOC2 tamper-proof logs.

**Significance:**  
Inspect AI is the most credible **eval framework** that can be used as a promotion gate for scaffold updates. It fills the "eval layer" of a full two-loop system when combined with a prompt versioning platform like Braintrust or LangSmith.

**Reference:**  
[Inspect AI](https://inspect.aisi.org.uk); [inspect_evals GitHub](https://github.com/UKGovernmentBEIS/inspect_evals); [Inspect AI review](https://neurlcreators.substack.com/p/inspect-ai-evaluation-framework-review) (Sept 2025).

---

### 18. Self-Refine (Madaan et al., 2023) — Score: **1/5**

**Classification:** In-context iterative refinement; no versioning, no promotion, no persistence.

**Mechanism:**  
Generate output → LLM generates feedback on its own output → LLM uses feedback to refine → repeat. Same model is generator, refiner, and feedback provider. No supervised training, no weight updates.

**Governance:**  
None. Test-time only. Outputs are ephemeral — the refined artifact is not persisted, versioned, or promoted.

**Significance for paper:**  
Self-Refine is a clean example of the **inner loop without any outer loop**. It achieves ~20% absolute improvement on task performance, demonstrating that iterative refinement works — but produces nothing that can be governed, audited, or promoted.

**Reference:**  
[Self-Refine paper](https://arxiv.org/abs/2303.17651) (arXiv:2303.17651, March 2023); [GitHub](https://github.com/madaan/self-refine).

---

### 19. Cleric.ai (AI SRE) — Score: **2/5**

**Classification:** Continuously learning operational memory; no formal versioning or promotion.

**Versioning mechanism:**  
"Dynamic operational memory" built from incident trajectories — a knowledge graph updated per investigation. No explicit version IDs or snapshots.

**Promotion gate:**  
Implicit: each investigation compounds the model's understanding of the customer's specific environment. High-frequency operational data (every alert, investigation, ticket) is the learning signal. No explicit promotion gate between "local session learning" and "promoted to all sessions."

**Scope:**  
Per-customer environment (not cross-customer). "Cleric learns from their specific environment — their dependencies, failure modes, and architecture."

**Key quote:**  
> "Every investigation compounds Cleric's understanding of your specific environment. It moves beyond static playbooks or simple pattern matching. Instead, it constructs a dynamic operational memory." — Cleric.ai blog, Dec 2025

**Reference:**  
[Cleric self-improving AI SRE](https://cleric.ai/blog/the-self-improving-ai-sre) (Dec 2025).

---

### 20. Sierra AI (Ghostwriter agent builder) — Score: **2/5**

**Classification:** Sandboxed agent-modifies-agent scaffold with validation gate; no external versioning.

**Versioning mechanism:**  
Sierra's **Ghostwriter** agent (announced March 2026) builds and improves agent configurations ("scaffolding — tools, memory, a coherent action space") by accessing the platform's full workspace in a sandboxed environment. Changes are validated before deployment.

**Promotion gate:**  
Sandbox validation before overwriting production agent configuration. "Ghostwriter has access to the platform's full workspace, as well as a clear way to test and safely validate changes in a sandboxed environment."

**Scope:**  
Per-deployment (per-customer). No cross-customer promotion.

**Significance:**  
Sierra's Ghostwriter is a notable example of an **agent that modifies its own scaffold** — agentic self-modification with a sandbox validation gate. This is rare in production systems. However, there is no external versioning, audit trail, or rollback described.

**Key quote:**  
> "Ghostwriter has access to the platform's full workspace, as well as a clear way to test and safely validate changes in a sandboxed environment. All this enables Ghostwriter to build and improve the most sophisticated agents reliably and autonomously." — Sierra blog, March 2026

**Reference:**  
[Sierra Agents as a Service](https://sierra.ai/blog/agents-as-a-service) (March 2026).

---

### 21. Decagon — Score: **2/5**

**Classification:** Templated Agent Operating Procedures (AOPs) with runtime governance; no scaffold versioning.

**Versioning mechanism:**  
**Agent Operating Procedures (AOPs)** as versioned templates (Feb 2026 launch). Teams can reuse templates across deployments.

**Promotion gate:**  
Runtime guardrail models gate responses at every stage (before, during, after conversation): bad actor detection, hallucination supervisor, brand guidelines enforcement, escalation rules. These are runtime quality gates, not promotion gates for scaffold changes.

**Scope:**  
Shared AOP templates across the Decagon platform.

**Key quote:**  
> "We've built our platform with rigorous guardrails at every stage of the customer interaction—before, during, and after the conversation." — Decagon blog

**Reference:**  
[Decagon guardrails blog](https://decagon.ai/blog/designing-layered-guardrails-for-reliable-ai-agents) (July 2025); [LinkedIn: Decagon AOP templates](https://www.linkedin.com/posts/sreenivasashwin_today-were-launching-templates-for-the-core-activity-7424496288731410432-2FWv) (Feb 2026).

---

## Cross-Cutting Findings for the Paper

### 1. How Rare Full Two-Loop Systems Are (2025–2026)

Of 21 systems examined, **only three** (Braintrust, Vellum, LangSmith) achieve a full Score 5 — meaning eval-gated promotion across explicit scope levels with audit trail and rollback. AGENTS.md/AAIF achieves Score 5 via institutional governance rather than eval gating, making it a distinct variant.

The distribution tells the story of where the field actually is:

| Score | Count | Systems |
|-------|-------|---------|
| 5 | 4 | Braintrust, Vellum, LangSmith, AGENTS.md/AAIF |
| 4 | 2 | Anthropic skills repo, GitHub Copilot enterprise |
| 3 | 7 | Cursor, DSPy, LangFuse, Agenta, W&B Weave, OpenAI AgentKit, Inspect AI |
| 2 | 7 | TextGrad, OPRO, NanoResearch, CAI, Cleric, Sierra, Decagon |
| 1 | 1 | Self-Refine |
| 0 | 0 | (none examined — by selection bias) |

**The central gap:** Academic systems (TextGrad, OPRO, NanoResearch, Self-Refine) have sophisticated inner loops (eval-driven updates) but almost no outer loop (governance, audit, promotion). Production commercial systems (Braintrust, Vellum, LangSmith) have strong outer loops but relatively simple inner loops (human engineers iterating prompts, not automated self-optimization). **No system in this survey has both a strong automated inner loop and a full outer-loop governance architecture.** This gap is the paper's core claim.

### 2. "Prompts as Code" — Evidence for the Thesis

Multiple independent sources confirm that leading production teams now treat prompts/rules/scaffolds as code with engineering discipline:

- **LangChain community (March 2026):** "Every `push_prompt` call = immutable commit with a hash. `staging` and `prod` are tag pointers... not values that get overwritten. Rollback is one SDK call — no deployment, no merge, no pipeline."
- **Harness.io (March 2026):** "Changes to AGENTS.md files should follow the same review rigor as code changes. Instruction drift is as dangerous as code drift."
- **Braintrust (Feb 2026):** "Automated evaluations should run on every pull request that modifies a prompt. If scores fall below defined thresholds, the pull request is blocked from merging."
- **Restate.dev (March 2026):** "Every deployment is a complete, versioned snapshot of the agent: code, prompts, tool definitions, schemas, guardrails, and model configuration. Once deployed, it never changes."
- **LaunchDarkly:** "Prompts need to be treated with the same care normally applied to application code. You wouldn't push code straight to production without version control, testing, and proper deployment processes."
- **Vercel evaluation data:** "Repository-level AGENTS.md context outperformed tool-specific skills in agent benchmarks" — empirical evidence that formalized scaffold governance improves outcome.
- **GitHub analysis of 2,500+ repos:** AGENTS.md raises agent task success from 40–60% (no file) to 85–90% (comprehensive file).

### 3. Survey/Industry Paper on Agent Lifecycle Management

- **"The 2025 AI Agent Index"** (arXiv:2602.17753, Feb 2026) — documents technical and governance developments in AI agents.
- **"Eval-driven development: Build and evaluate reliable AI agents"** (Red Hat, March 2026) — describes eval-driven development as a formalized practice.
- **"AI Governance Is Not Policy. It Is Infrastructure"** (JD Supra, March 2026) — argues governance must be architectural, not just policy.
- **"The Year Agentic Operations Got Real"** (XMPro, Feb 2026) — "true multi-agent systems are approximately ninety percent business process intelligence and ten percent language model capability... Governance structures that enforce boundaries and capture approvals; Decision trace infrastructure that preserves reasoning for audit."
- **"AGENTFLOW: In-the-Flow Agentic System Optimization"** (arXiv:2510.05592) — on-policy optimization inside the live multi-turn loop.
- **"COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents"** (arXiv:2604.20987, April 2026) — co-evolution framework where skill bank is continuously extracted and refined from unlabeled rollouts; 25.1% reward improvement.

### 4. The OpenCore Gap

No public artifact, blog post, or paper was found for an "OpenCore" reference architecture described as a patch-plastic scaffold system. The name "OpenCore" primarily resolves to the OpenCore Legacy Patcher (a macOS boot loader project) in public search results. This system appears to be either internal/unpublished, or the name is used in private documentation not indexed publicly.

### 5. DSPy as the Strongest Academic Bridge

DSPy is the most production-relevant academic system in the survey — used in deployed systems, with tutorials on saving/loading compiled programs, and with an explicit roadmap toward "interactive optimization & tracking" and "deployment tutorials." The `program.save(path)` / `program.load(path)` API provides the serialization primitive needed for a promotion loop, but the governance scaffold (who reviews the compiled program before production deployment? what eval threshold must it meet? where is the audit log?) must be added externally (e.g., via LangSmith or Braintrust).

The combination **DSPy (compile) + Braintrust (govern)** is the current closest to a full two-loop system available as open components.

---

## Rubric Anchor Points (for Paper 3)

| Score | Canonical Example | Definition |
|-------|------------------|------------|
| **5** | Braintrust / Vellum / LangSmith | Eval-gated promotion through explicit scope levels (dev→staging→prod), content-addressed immutable versioning, full audit trail with author/timestamp/eval results, instant rollback, org-wide deployment with RBAC |
| **4** | Anthropic skills repo / GitHub Copilot enterprise | PR-based human review gate, explicit scope hierarchy (personal→shared→org), git-tracked versioning, rollback via git, but no automated eval threshold gate |
| **3** | Cursor rules / DSPy / LangFuse | Versioned artifacts in git or DB, explicit local vs. shared scope, some promotion mechanism (manual UI or PR), rollback, but no eval gate and/or incomplete audit trail |
| **2** | TextGrad / NanoResearch / Cleric | Internal optimization loop (eval-driven updates within the system), no external versioning, no scope distinction, no audit trail, no rollback |
| **1** | Self-Refine | Ad-hoc in-context refinement, no persistence, no versioning, no promotion |
| **0** | Hardcoded system prompts | Static scaffold artifacts; no governance of any kind |

---

## Sources Index

| Source | URL | Date |
|--------|-----|------|
| Braintrust prompt versioning | https://www.braintrust.dev/articles/what-is-prompt-versioning | Feb 2026 |
| Braintrust prompt management | https://www.braintrust.dev/articles/what-is-prompt-management | Feb 2026 |
| Vellum release tags docs | https://docs.vellum.ai/product/deployments/release-tags | March 2026 |
| Vellum April 2025 update | https://www.vellum.ai/blog/vellum-product-update-april-2025 | May 2025 |
| LangSmith manage prompts | https://docs.langchain.com/langsmith/manage-prompts | May 2026 |
| LangFuse version control | https://langfuse.com/docs/prompt-management/features/prompt-version-control | — |
| Anthropic skills repo | https://github.com/anthropics/skills | April 2026 |
| AGENTS.md spec | https://agents.md | — |
| agentsmd GitHub | https://github.com/agentsmd/agents.md | Aug 2025 |
| Linux Foundation AAIF | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | Dec 9, 2025 |
| OpenAI AAIF | https://openai.com/index/agentic-ai-foundation/ | Dec 9, 2025 |
| GitHub Copilot org instructions GA | https://github.blog/changelog/2026-04-02-copilot-organization-custom-instructions-are-generally-available/ | April 2, 2026 |
| GitHub Copilot org instructions docs | https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-organization-instructions | — |
| Harness.io AGENTS.md analysis | https://www.harness.io/blog/the-agent-native-repo-why-agents-md-is-the-new-standard | March 2026 |
| BigHat AGENTS.md enterprise guide | https://www.bighatgroup.com/blog/agents-md-guide-enterprise-ai-coding/ | March 2026 |
| NanoResearch paper | https://arxiv.org/abs/2605.10813 | May 11, 2026 |
| NanoResearch HuggingFace | https://huggingface.co/papers/2605.10813 | May 2026 |
| DSPy saving tutorial | https://dspy.ai/tutorials/saving/ | — |
| DSPy site | https://dspy.ai | — |
| DSPy roadmap | https://dspy.ai/roadmap/ | — |
| TextGrad paper | https://arxiv.org/abs/2406.07496 | June 2024 |
| TextGrad GitHub | https://github.com/zou-group/textgrad | June 2024 |
| Stanford HAI TextGrad | https://hai.stanford.edu/news/textgrad-autograd-text | June 2024 |
| OPRO paper | https://arxiv.org/abs/2309.03409 | Sept 2023 |
| OPRO GitHub | https://github.com/google-deepmind/opro | — |
| Revisiting OPRO (ACL 2024) | https://aclanthology.org/2024.findings-acl.100/ | Aug 2024 |
| Self-Refine paper | https://arxiv.org/abs/2303.17651 | March 2023 |
| Constitutional AI paper | https://arxiv.org/abs/2212.08073 | Dec 2022 |
| Anthropic CAI research | https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback | — |
| Inspect AI | https://inspect.aisi.org.uk | — |
| inspect_evals GitHub | https://github.com/UKGovernmentBEIS/inspect_evals | — |
| Inspect AI review | https://neurlcreators.substack.com/p/inspect-ai-evaluation-framework-review | Sept 2025 |
| OpenAI AgentKit | https://openai.com/index/introducing-agentkit/ | Oct 6, 2025 |
| Cleric self-improving | https://cleric.ai/blog/the-self-improving-ai-sre | Dec 2025 |
| Sierra Ghostwriter | https://sierra.ai/blog/agents-as-a-service | March 2026 |
| Decagon guardrails | https://decagon.ai/blog/designing-layered-guardrails-for-reliable-ai-agents | July 2025 |
| Decagon AOP templates | https://www.linkedin.com/posts/sreenivasashwin_today-were-launching-templates-for-the-core-activity-7424496288731410432-2FWv | Feb 2026 |
| Restate.dev agent versioning | https://www.restate.dev/blog/dealing-with-versioning-in-long-running-agents | March 2026 |
| COSPLAY paper | https://arxiv.org/abs/2604.20987 | April 2026 |
| XMPro agentic ops | https://xmpro.com/the-year-agentic-operations-got-real-2025-reflections-and-what-2026-demands/ | Feb 2026 |
| Reddit prompt management | https://www.reddit.com/r/AI_Agents/comments/1rsji8z/prompt_management_in_production_langfuse_vs_git/ | March 2026 |
| W&B Weave prompts | https://docs.wandb.ai/weave/guides/core-types/prompts | — |
| Agenta prompt versioning | https://agenta.ai/blog/prompt-versioning-guide | Feb 2026 |
| LangChain community spotlight | https://www.linkedin.com/posts/langchain-oss_langchain-community-spotlight-production-activity-7443703468844036097-InfI | March 2026 |
