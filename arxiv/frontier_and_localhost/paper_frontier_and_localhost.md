---
title: "Frontier and Localhost: How Production AI Learns Outside the Weights"
author:
  - Mikhail L. Arbuzov
  - Alexey A. Shvets
  - Sisong Bei
date: ""
header-includes:
  - \usepackage{xurl}
---

**Abstract**

Reliability has moved from the weights to the scaffold. Surveying production and research LLM systems from 2023–2026, we show that practitioners repeatedly wrap frozen frontier models in local, persistent, feedback-updated artifacts: instructions, skills, memories, tools, orchestration graphs, and governance pipelines. We argue that these artifacts form a deployment-time learning layer — a *localhost scaffold* — that adapts a general model to the recurring failure topology of a specific patch. We formalise this as **artifact-layer descent**: failures provide noisy loss signals, candidate scaffold deltas are generated, gates accept or reject them, accepted deltas persist and may be promoted across contexts. The resulting two-loop architecture explains the convergence of modern agent systems across IDE plugins, vertical-bundle vendors, and self-evolving research agents, and it reveals an unfilled design corner: automated local scaffold evolution combined with governed, auditable, cross-organisation promotion — a *DP-FedAvg-style aggregator with an automated eval gate at the scaffold layer*. The contribution is conceptual and survey-based. A practitioner-facing companion paper will handle reference architectures, maturity ladders, design principles, and the full failure taxonomy.

---

## 1. The gradient moved outside the model

The standard mental model of an LLM system is the model. Pre-training fixes the weights; fine-tuning or RLHF nudges them; deployment wraps a thin prompt-plus-tool layer around the result and ships. Errors are weight errors; reliability is a weight-training problem.

Production has stopped behaving this way. In 2025–2026, frontier models update on cycles measured in months, but the systems built on top of them update continuously — in markdown files, persistent memories, retrieved skills, registered tools, evaluation suites, agent topologies, version-controlled prompt repositories, and PR-gated governance. The fast learning is no longer in the weights. It is in a fast-changing *localhost* scaffold wrapped around a slow-changing frontier.

This paper argues that *the localhost is doing learning*. Not merely metaphorically: scaffold artifacts are updated from failure signal, the updated artifacts reduce future failure probability on a local patch, and the update process — observe failure, generate candidate delta, gate it, persist it, optionally promote it — has the structure of stochastic descent. The substrate happens to be discrete, symbolic, and human-readable rather than continuous and differentiable, but the function is the same.

Once you accept the framing, the field snaps into place. A Claude Skill is not "just a markdown file." It is a learned procedural weight kept outside the model. A Cursor Rule is not "just an instruction." It is a local parameter for one project's distribution shift. A RAG connector is not "just retrieval." It is patch-specific memory access. A tool registry is not "just integration." It is capability provisioning along an axis the base model cannot reach. A PR review against a shared rule repository is not "just governance." It is a promotion gate on a federated update. An eval suite that blocks merge is not "just testing." It is a validation-loss check before promotion. A cross-tenant artifact repository is not "just sharing." It is federated learning across distributed shards. The mechanisms were already there; only the name was missing.

We survey 142 systems across six substrates (instructions, skills, memory, tools, orchestration, governance), score each on a 0–5 patch-plasticity rubric, and analyse the fourteen that satisfy a strict *composite two-loop* criterion: an inner loop that updates a persisted artifact from session feedback, an outer loop that promotes the artifact across scopes under explicit versioning. The two-loop design space is a 3×3 matrix on gate type — *Auto-gated* when the commit-or-promote decision is operationalised by an algorithmic criterion, *Human-gated* when it is reviewer judgment. The matrix has four cells of interest, three populated by working systems and one empty by engineering logic. The fourth diagonal — fully automated, governed, cross-tenant — has no surveyed occupant. That empty corner is the paper's open-question headline and a concrete Paper-4 target.

The architectural review of how to actually build such systems — five reference patterns, a five-level maturity model, a substrate-selection rubric, three migration paths, the full nine-category failure taxonomy, and eight design principles — is deferred to follow-on practitioner work. This paper is the survey and the framework.

## 2. Why patch errors must live outside the weights

The scaffold is not merely where production systems happen to store patches. It is the *only reasonable substrate* for patch-specific adaptation, because the weight substrate is structurally wrong for it. Frontier training and production reliability optimise for objectives that are in tension, and that tension forces adaptation outside the model.

**Frontier training optimises for breadth.** The weights are tuned for cross-patch generalisation: they smooth over local conventions, contradictory tenant preferences, and rare workflow-specific failures in order to preserve broad competence across millions of unseen deployments. The smoothing is not incidental. It is the training objective. A model that overfits to one tenant's naming conventions or one team's preferred error-handling style loses transfer to the next tenant; a model that encodes every patch's idiosyncratic eval expectation loses the general-purpose competence that made it worth deploying in the first place.

**Production reliability is achieved in depth.** Inside a single deployment patch, reliability is determined by exactly the stuff global training had to smooth away: local naming conventions, team-specific workflows, domain-specific failure patterns, project-specific schemas, idiosyncratic tool chains, customer-specific risk tolerances, recurring local mistakes, institutional preferences, hidden evaluator expectations. The per-patch quantities from our previous work — failure-mode catalogue size $|C_D|$, hard-fraction $\beta_D$, mode-discovery rate $\sigma_D$ — are local by construction, and a library calibrated to one patch under-covers the next.

**Encoding every patch in the weights is structurally infeasible.** Three constraints rule out the obvious approach. *Economic:* millions of patches multiplied by billions of parameters times the cost of per-patch fine-tuning is not a viable training-compute budget. *Release-cycle:* the patch wants daily updates; weight releases ship quarterly at best. *Cross-patch interference:* overfitting the weights to one tenant's preferences degrades behaviour for adjacent tenants whose preferences contradict. The weights are tuned for cross-patch invariants by construction; that is what they are *for*.

The localhost scaffold solves the conflict. It is the only substrate that can:

- overfit aggressively to one tenant without damaging another;
- encode local conventions without polluting global behaviour;
- update daily instead of waiting for release cycles;
- be inspected, versioned, audited, and rolled back;
- attach tools, memories, rules, workflows, and evals that are meaningless outside the patch;
- specialise inside the patch while the model remains broadly competent.

Each scaffold substrate targets a different patch-residual class. Instructions and tools address *capability* residuals — the model could not do this on its own (PAL for arithmetic, RAG for retrieval, constrained decoders for format). Skills and memory address *catalogue* residuals — the same patch-specific failure mode keeps recurring and now has a patch. Orchestration addresses *hard-fraction* residuals — the per-step decision was too hard, so specialised sub-agents bring it back into capability range. Governance addresses *propagation* residuals — a correction proven in one deployment is wasted unless it can be promoted to others under audit.

Our previous work (Arbuzov, Shvets & Bei, 2025; *Architecture of Errors*, 2026) argued that LLM errors concentrate sparsely at key tokens and cluster into a finite catalogue of recurring modes whose size grows polylogarithmically in observed failures. The framework left a *placement* question — where do the interventions live? The answer follows from the tension above. The interventions live in scaffold artifacts because they cannot live anywhere else. The frontier model generalises; the localhost scaffold specialises; reliability comes from governing that specialisation.

## 3. Artifact-layer descent

The remaining question is whether "scaffold evolution" is learning in any technical sense or just engineering practice. The answer depends on what one means by learning.

Let $D$ be a deployment patch — a specific application, user, or task distribution. Let $M$ be the frozen frontier model, accessed via inference but not updated. Let $S_t$ be the scaffold at time $t$: the layered collection $\{S_t^{(1)}, \ldots, S_t^{(6)}\}$ of instruction set, skill library, memory store, tool registry, orchestration graph, and governance configuration. Let $\pi(M, S_t, x)$ denote the system's behaviour on input $x$ — the model running on the model-plus-scaffold composite. Let $L_D(S_t) = \mathbb{E}_{x \sim D}[\ell(\pi(M, S_t, x))]$ be the expected residual failure rate on the patch.

A failure observation produces a candidate delta $\Delta S$: an instruction edit, a new skill, a memory correction, a tool re-registration, a topology change, or a governance-rule update. A gate $G$ accepts $\Delta S$ if estimated patch loss decreases or if risk stays within tolerance:

$$
S_{t+1} = S_t + G(\Delta S)
$$

Different surveyed systems instantiate $G$ differently. NanoResearch's gate is a semantic-merge by the orchestrator (algorithmic). SkillRL's gate is an RL threshold at task-category accuracy below 0.4 (algorithmic). AlphaEvolve's gate is a cascade evaluator with MAP-Elites archive selection (algorithmic). SkillForge's gate is an LLM-judge with >90% human agreement *plus* a human support engineer (hybrid algorithmic + reviewer). OpenCore's gate is a reviewer-judgment check against `core-update-gate.md`, with no algorithmic threshold — only a checklist (purely reviewer-judgment). DSPy's gate is gradient-like over prompt-template space without persistent commitment. Reflexion's gate is essentially absent: any reflection becomes a memory entry.

Different estimators of the same quantity. Each surveyed system is asking, by some method, whether $\Delta S$ moves $S_t$ toward lower $L_D$. The substrate is discrete: scaffold edits are typically textual, procedural, or symbolic, not differentiable in the backpropagation sense. The gate is mediated: humans, evals, LLM-judges, or surrogate verifiers stand in for the gradient. The update is governed: not every candidate $\Delta S$ propagates; some are rejected, some are quarantined to a single user's fork, some climb a layered hierarchy from local to shared scope before they take.

We call this *artifact-layer descent*. In the limit where scaffold edits are represented as coordinates in an artifact basis and the gate is a differentiable validation-loss estimator, the process is gradient descent. In ordinary deployments, where edits are discrete and gates are eval-, judge-, or reviewer-mediated, it is a stochastic approximation to descent. The two are continuous with one another; the difference is one of substrate and signal-to-noise, not of mechanism.

Two loops follow naturally. **Loop 1** is within-context: a session feedback signal triggers an update to a persisted local artifact. **Loop 2** is cross-context: a local artifact is promoted to a shared scope (cross-project, cross-user, cross-organisation) under explicit versioning. Loop 1 is the local SGD step; Loop 2 is federated averaging across distributed shards. Each loop has a gate; gates are **Auto-gated** when the decision is an operationalised algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement, surrogate verifier, benchmark cascade), **Human-gated** when the decision is reviewer judgment (automation often precedes the gate but the gate itself is reviewer discretion), and **None** when the loop is absent.

These five terms — Loop 1, Loop 2, Auto-gated, Human-gated, None — anchor the rest of the paper.

The framing positions the work against several adjacent literatures. CoALA (Sumers et al., 2023) proposes a static cognitive architecture of modular memory and structured action; we update CoALA's snapshot into a dynamic deployment architecture with governance. The self-evolution surveys (Tao 2024; Gao et al. 2026; Fang et al. 2025) treat agents as learners that update weights, representations, or optimiser-selected artifacts — they locate the gradient inside the model. The memory-survey of Du (2026) and the skills-survey of Zhou et al. (2026) cover individual substrates with version-and-promotion machinery that mirrors S3 and S2 here but stops at the substrate boundary. ACE (2025) treats context as a single evolving playbook. Each adjacent work touches a piece of the picture; none develops the cross-substrate artifact-layer descent framing or the design space it implies.

### 3.1 The mechanism stack

The abstract update rule $S_{t+1} = S_t + G(\Delta S)$ expands into six operations that every patch-plastic system must perform — whether explicitly engineered or accidentally emergent.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, eval regressions, tool-call failures. The Loop-1 signal source. Without it, $\Delta S$ has no provenance.
2. **Mode discovery.** Cluster repeated failures into patch-specific error modes. The Paper-2 catalogue, instantiated locally per patch.
3. **Delta synthesis.** Convert a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, an eval case. This is the production of $\Delta S$.
4. **Delta validation.** Estimate whether the edit reduces $L_D$ without collateral damage on adjacent inputs. This is the gate $G$ — Auto-gated when the check is an algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement), Human-gated when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted $\Delta S$ stays in the local fork or climbs the scope hierarchy — project, stack, organisation, cross-tenant. This is Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, detect over-fitting to one patch. Without this layer, accumulated $\Delta S$ produces the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline that does not yet exist in coordinated form. Surveyed systems implement the operations partially and unevenly: research full-auto systems excel at (3) and (4), production governance leaders at (5), industry hybrids at most of (1)–(5) but rarely (6). Implementation patterns for each of the six are deferred to follow-on work; this paper's purpose is to make the discipline visible.

## 4. Six scaffold substrates

A patch-plastic scaffold composes six substrates. They are the coordinates of $S_t$.

| Substrate | What persists | Score-5 mark |
|---|---|---|
| **S1 — Instructions** | Project/team/org rules attached to a workspace | Versioned, two-loop, Auto-gated promotion |
| **S2 — Skills** | Procedural artifacts (code/text) loaded on demand | Skill bank self-modifies on failure, unit-test gated, versioned, promoted |
| **S3 — Memory** | Cross-session experience (episodic / semantic / procedural) | Provenance + versioning + correction pathways |
| **S4 — Tools** | Vetted action surface + context schemas | Domain-curated bundle is the product; eval-gated tool versions |
| **S5 — Orchestration** | Multi-role graph + routing | Population/policy updates from outer-loop signal |
| **S6 — Governance** | Versioning, promotion, audit, rollback | dev→staging→prod with eval thresholds + audit log + rollback |

The 0–5 rubric is uniform across substrates: **0** ephemeral; **1** persistent local; **2** persistent + tool attachment, no feedback; **3** multi-scope or feedback but no automated promotion; **4** automated feedback updates the scaffold (one loop closed); **5** two-loop versioned promotion plus governance (both loops closed).

Each substrate maps to a different Paper-2 residual class. S1 and S4 carry capability provisioning. S2 and S3 accumulate the patch-specific failure-mode catalogue. S5 lowers per-step hard-fraction by specialisation. S6 is the gate substrate — without it, none of the other five can be updated safely across deployments. *The substrates are not a taxonomy of nice-to-haves. They are the layers of the scaffold parameter vector, separately addressable by Loop 1 and Loop 2.* Score distributions and per-substrate exemplars are summarised in §6.1; the maturity-rubric details for practitioner adoption are deferred to follow-on work.

## 5. Survey method and evidence tiers

The survey covers 142 LLM systems published or productionised between January 2023 and May 2026, split into two sets. The **core corpus** of 104 candidate scaffold-learning systems satisfies the patch-plastic discriminator (score ≥ 3 on at least one substrate, indicating skills, memory, or multi-scope persistence beyond ephemeral prompts). The **contrast corpus** of 38 systems is commonly described in the public discourse as agentic or self-improving but fails at least one discriminator — typically Loop 2 absent, no persistent artifact distinct from optimiser state, or in-context-only adaptation. Headline statistics quote the core corpus; the contrast set is preserved as asterisked entries in the matrices for definitional clarity.

**Inclusion.** Any system that (a) wraps a foundation model with at least one persistent artifact updated from deployment signal, or (b) is named in the public discourse as a "self-improving," "scaffolded," or "agentic" system. The contrast set (Self-Refine, ReAct, plain Mem0, DSPy/TextGrad, etc.) is included precisely so the discriminator has something to mark against.

**Exclusion.** Systems whose only update mechanism is weight-level fine-tuning or RLHF — these are model-side, not scaffold-side, and belong to the self-evolution literature this paper differentiates from. Systems with no public evidence of deployment (white papers without code, demos, or production claim).

**Evidence tiers.** Each system carries one or more of: (T1) peer-reviewed publication, (T2) arXiv preprint, (T3) production claim with metrics, (T4) open-source artifact (GitHub, registry), (T5) industry-blog or interview-level documentation. Systems with T1 or T4 evidence carry highest weight in the cluster analysis (§7); T3 systems are admissible where the claim is concrete (specific benchmark, named integration target); T5 systems are admissible only when corroborated by T1–T4 elsewhere.

**Scoring.** Each system received a substrate-by-substrate 0–5 score against the rubric of §4 and an integrated patch-plasticity (PP) score in {0,1,2,3,3.5,4,4.5,5}. Half-scores were used sparingly for systems where one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). Each scoring decision is recorded in the master CSV.

**Composite two-loop criterion.** A separate, stricter audit applied to 22 candidate systems. A system qualifies as composite two-loop if and only if it satisfies both: Loop 1 modifies a persisted artifact from a session signal *and* Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage. Fourteen systems passed the audit; eight failed (MAE, MetaGen, MetaReflection, CLIN — Loop-2 absent; DSPy, TextGrad — no persistent artifact distinct from optimiser state; Mem0, Zep, ChatGPT Memory — no Loop-2 promotion path).

**Audit trail.** The full per-system spreadsheet (`p3_master_scores.csv`), per-substrate evidence harvests, and the composite-two-loop audit (`p3_harvest_composite_two_loop.md`) are in the paper's repository. Reviewers can re-run the analysis from primary sources.

## 6. Survey findings: the scaffold is unevenly mature

The 104-system core corpus does not mature uniformly. Tools and integrated systems are the most mature substrates; skills and orchestration lag; instructions are ubiquitous but shallow; memory is the most paradoxical of the six. This section presents the headline distributions before the cluster interpretation of §7. The full per-system spreadsheet is in `p3_master_scores.csv`; Appendix A lists representative rows.

### 6.1 Substrate maturity is uneven

Aggregating the survey by substrate gives this distribution:

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|--------------|---:|----:|----------------------|-------------------------------------------------------|
| **S1 — Instructions** | 12 | 2.83 | *(none)* | Rules persist across IDEs and agents (Claude Code's CLAUDE.md, Cursor Rules, AGENTS.md, Windsurf, Continue.dev) but no surveyed instruction system closes both an automated inner loop and a governed two-loop promotion. Ceiling held at 4 by Claude Code and Replit |
| **S2 — Skills** | 16 | 2.62 | SAGE, COSPLAY | Research frontier is active (failure-triggered skill update); production governance is weaker. Anthropic's skills repository is one-pool with PR review but no automated eval gate |
| **S3 — Memory** | 19 | 3.16 | SSGM | Cross-session memory is widespread; *correctable, versioned* memory is rare. Production memory systems (ChatGPT Memory, Claude Memory, Mem0, Zep, MemGPT) treat memory as append-only |
| **S4 — Tools** | 19 | 3.63 | MCP, Harvey, Hippocratic AI | Most mature production substrate. Tool bundles are the commercial unit; MCP is the cross-vendor standard with 9,400+ public servers and 78% enterprise adoption |
| **S5 — Orchestration** | 19 | 2.68 | MAE, Memento-Skills | Multi-agent topologies exist (LangGraph, AutoGen, CrewAI) but topology *evolution* is rare; production rarely exposes governed promotion paths for emerging agent graphs |
| **S6 — Governance** | 21 | 3.05 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | High production maturity for prompts-as-code — immutable commits, eval-gated PR merge, sub-five-minute rollback — typically without inner-loop adaptation |
| **INTEGRATED** | 34 | 3.74 | NanoResearch, AutoAgent, SkillRL | The high-water mark when present, but the cluster is dominated by research systems lacking enterprise governance |

The unevenness is the survey's central empirical pattern. The field has independently converged on the six substrates, but no system matures all six at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation; vertical-bundle vendors solve patch specificity but rarely expose cross-tenant promotion. The missing architecture is not "agents with tools" or "memory with evals." It is *governed scaffold adaptation* — fast local learning paired with safe cross-context promotion.

### 6.2 Representative systems by cluster

Five clusters recur across the corpus. The four-cluster grouping below maps each system to its gate types and to the structural lesson it carries. The matrix in §8 places the same systems on the 3×3 design space.

| Cluster | Representative systems (year, PP score) | Loop 1 / Loop 2 | What the cluster proves |
|--------------|------------------------------|--------------|------------------------------------------|
| Research full-auto | NanoResearch (2026, 5), SkillRL (2026, 5), AlphaEvolve (2025, 4), DGM (2025, 4), ADAS (2024, 4), Voyager (2023, 4) | Auto / Auto | Both loops can be fully automated under algorithmic gates; benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge (2026, 4), CASCADE (2025, 4.5), Sierra OS 2.0 (2025, 3), Cognition Devin (2024, 3) | Auto / Human | Algorithmic Loop-1 gate plus reviewer-judgment Loop-2 gate is the production-viable cell; SkillForge is the architectural exemplar |
| Reviewer-judgment | OpenCore (2025, 4) | Human / Human | Automated extraction machinery with reviewer-judgment gates on both loops; the only published $n>1$ mini-batch rule in the corpus (5-dream threshold); cross-organisation federation via fork-and-contribute-back |
| Governance-first | Braintrust, Vellum, LangSmith Hub (all 2024, S6 = 5) | None / Auto | Eval-gated promotion exists; candidate generation is manual (engineers iterate prompts); no patch-plastic inner loop |
| Open standards | AGENTS.md (2025), MCP (2024), Claude Skills (2025), Cursor Rules (2024) | Mixed / Mixed | Vendor-cross convergence on artifact format and tool attachment; 60k+ AGENTS.md repos; 9,400+ MCP servers; 78% enterprise MCP adoption |

### 6.3 Surprising absences

What is missing from the survey is as instructive as what is present. Five absences stand out across the 104-system core corpus:

1. **Failure-triggered memory is rare in production.** Deployed memory systems prefer recording preferences and successful facts; only Reflexion, the Voyager skill library, Gemini Code Assist's PR-rejection memory, and the classical SOAR chunking pattern explicitly record residuals. The most obvious Loop-1 signal is the one production memory systems mostly ignore.
2. **Cross-customer skill promotion is absent.** AGENTS.md is cross-vendor; Anthropic's skills repository is one-pool. No surveyed system has a vetted cross-organisational marketplace with eval-gated promotion.
3. **Memory versioning is mostly unsolved.** Only SSGM provides explicit provenance, versioning, and correction pathways. Production default is append-only with implicit retrieval-based forgetting — at odds with the patch-plastic discriminator's correction requirement.
4. **Scaffold-level curriculum is absent.** No surveyed system selects *which* sessions inform the gradient. Every session contributes equally; weighting by recency, severity, or representativeness has not been published.
5. **Overfitting detection at Loop-2 promotion is absent.** No surveyed system runs a held-out eval set per project to catch scaffolds that over-fit one deployment before they propagate to another.

Each absence is a Paper-4 target. The conclusion echoes them; the survey makes them visible.

## 7. Convergent patterns

The 142-system corpus, scored against the rubric of §4, produces four archetypal clusters that recur across both research and industry. We present the clusters here rather than walking every system; the full table is in the repository.

**Research full-auto.** Systems where both loops fire from algorithmic criteria and no human gates the routine update. **NanoResearch** (Xu et al., 2026) co-evolves Skills, Memory, and Policy with a semantic-merge orchestrator; Innovation 4.96 → 5.65 and Compliance 6.66 → 8.96 across three rounds. **SkillRL** (arXiv:2602.08234) uses RL reward distillation with a hard threshold at task-category accuracy below 0.4 and reports +15.3% over strong baselines. **AlphaEvolve** (DeepMind, 2025) runs a Gemini-driven ensemble with a cascade evaluator and a MAP-Elites archive, deployed at Google to gain +0.7% Borg compute worldwide, +23% on the Gemini training kernel, +32.5% on FlashAttention, and a first improvement over Strassen's 1969 bound on 4×4 complex matrix multiplication (48 scalar multiplications). **DGM** (Zhang et al., 2025) modifies its own source code with archive-based parent selection; SWE-bench 20% → 50%. The cluster maximises velocity. Enterprise governance is uniformly absent.

**Production hybrid.** Systems where Loop 1 is Auto-gated (an algorithmic criterion) and Loop 2 is Human-gated (reviewer approval before propagation). **SkillForge** (Alibaba Cloud, arXiv:2604.08618) drives auto-generated skill diffs through an LLM-judge with >90% human agreement (the Loop-1 gate); human support engineers then review what the LLM-judge passes (the Loop-2 gate). VFS version commits provide full lineage. **CASCADE** (Huang et al., 2025) reports the corpus's largest ablation gain — 93.3% vs. 35.4% on SciSkillBench — driven by memory consolidation gated by human-agent collaboration. **Sierra Agent OS 2.0** routes AI-driven Insights through human-authored Expert Answers in GitHub-style Workspaces. **Cognition Devin** ships dynamic in-session tool creation with a 67% PR-merge rate (the merged PRs are the Loop-2 promotion). This is the production-viable cell.

**Governance-first.** Systems where Loop 2 is Auto-gated by an eval criterion but Loop 1 is essentially absent — there is no automatic candidate-generation pipeline. **Braintrust**, **Vellum**, **LangSmith Hub**, **W&B Weave**, **Agenta**, **LangFuse**. The pattern is *prompts-as-code*: immutable commits, semantic-version tag pointers, PR-blocked merges on eval regression, sub-five-minute rollback. Engineers iterate the artifacts manually; the eval pipeline gates the promotion. We frame this as **MLOps for scaffolds**, distinct from MLOps for weights.

**Open standards.** Systems where the artifact format and the layering convention are open standards across vendors. **AGENTS.md** (Linux Foundation, December 2025) is now in over 60,000 GitHub repositories; Lulla et al. (2026) report −28.64% wall-clock and −16.58% tokens with no quality loss after adding an AGENTS.md scaffold. **MCP** (Anthropic, 2024) has 9,400+ public servers, 78% enterprise adoption, ~97M SDK downloads/month. **Claude Agent Skills**, **Cursor Rules**, **GitHub Copilot custom instructions**, **Windsurf rules**, **Continue.dev rules**, **Zed AI rules**, **Replit `replit.md`** all converge on the same pattern: a git-tracked markdown artifact attached to a workspace, with an MCP-style tool layer for actions. Convergence across vendors is the strongest evidence the architecture is real rather than a single vendor's local optimum.

The four clusters do not partition the corpus — many systems sit between two clusters — but they capture the architectural variation. Vertical-bundle vendors (Harvey for legal, Hippocratic AI for healthcare, Sierra for customer experience) sit between *open standards* and *production hybrid*: the bundle is the commercial unit; the underlying model is mostly the same one a competitor would use.

## 8. The two-loop design space

The fourteen composite-two-loop systems sit in a 3×3 matrix indexed by gate type on each loop.

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillRL, AlphaEvolve, ADAS, DGM (primary), Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, DGM (sandbox), Sierra OS 2.0, Cognition Devin | MAE\*, MetaGen\*, MetaReflection\*, CLIN\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | OpenCore | *(none)* |
| **Loop-1 None** | ExpeL (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repo\*, DSPy\*, TextGrad\* | Self-Refine\*, ReAct\*, Mem0\* |

*Asterisks fail at least one composite-two-loop criterion; included for contrast.*

The matrix has four cells of interest. **[Auto × Auto]** is most populated (eleven systems). Every member has a machine-evaluated decision criterion on both loops. **[Auto × Human]** is the production-viable cell — Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. **[Human × Human]** contains only OpenCore: the dream → delta → PR machinery is automated throughout, but both gates — `core-update-gate.md` for Loop 1 PR review and the upstream-CORE PR for Loop 2 — are reviewer-judgment checklists rather than algorithmic criteria. **[Human × Auto]** is empty by engineering logic; if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping), but no published example exists.

The **[None × Auto-gated]** cell holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 — eval-gated CI blocks promotion on regression — but no Loop 1 in the patch-plastic sense, because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative precisely because it shows what survives when only the outer loop is automated.

OpenCore deserves one paragraph here because its ML-mapping is unusually clean and the four-layer architecture is unique in the corpus. The dream → 5-dream rule is the only published $n > 1$ minibatch in the survey: each "dream" is a candidate gradient sample at $n = 1$, and the 5-dream threshold defers the fork update until five independent dreams converge — directly mirroring mini-batch gradient descent at batch size 5. The four-layer fork (USER → PROJECT → STACK → CORE) is the only explicit deep-vs-surface hierarchy in the corpus, with CORE as the slow-moving universal layer and USER as the fast-adapting per-instance layer. Cross-project drift upstream-promoted to CORE is federated averaging across user/project shards, gated by human PR review. The key observation here is that OpenCore demonstrates *cross-organisation* federated aggregation — the only surveyed system to do so explicitly — and that the gates are reviewer-judgment because the design is targeted at solo and small-team workflows where the marginal cost of a bad auto-merge exceeds the marginal cost of human latency.

Two cross-cutting findings sharpen the picture. **Noise reduction via batching shows up only under human gates** in the surveyed corpus: OpenCore's 5-dream rule is the only published $n > 1$ minibatch, and it sits in [Human × Human]. The auto-gated systems all fire at $n = 1$ per generation step, absorbing noise statistically via the algorithmic gate. Whether the implicit minibatch in OpenCore reduces residual error against an $n = 1$ baseline is untested; we predict it does. **Multi-layer hierarchies are under-explored**: only OpenCore and AlphaEvolve demonstrate explicit depth. The other twelve composite-two-loop systems treat their artifact pool as flat. Adding a STACK-style intermediate layer to NanoResearch or a multi-archetype scope to Anthropic's skills repository is a tractable engineering direction.

## 9. The empty corner

Four properties define what we call **enterprise full-auto**:

- (a) **Auto-gated Loop 1** — the commit criterion is an algorithmic threshold.
- (b) **Multi-tenant cross-org promotion** — Loop 2 routes artifacts between organisations, not just within one.
- (c) **Versioned lineage with RBAC** — promoted artifacts carry semantic versions, audit trails, and access-control policies.
- (d) **Rollback** — a bad promotion can be reverted without redeploy.

No surveyed system has all four. Closest approaches partition the requirements: **AlphaEvolve** has (a) and partial (b) within a single organisation; **NanoResearch** has (a) at the research level; **SkillForge** has (a) and (b) within one enterprise, partial (c) via VFS commits, undocumented (d); **OpenCore** has (b), (c), and (d) under reviewer-judgment gates but not (a); **Sierra Agent OS 2.0** has (b) and partial (a); **Vellum / Braintrust / LangSmith Hub** have (c) and (d) explicitly but no (a) or (b) in the strict sense.

The empty corner is concrete in ML terms: a *DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer*. Differential-privacy federated averaging (DP-FedAvg) is the closest analogue in the federated-learning literature — gradient updates aggregated across distributed shards with privacy-preserving noise and an aggregation gate. At the scaffold layer this would mean: per-tenant artifact pools with tenant-tagged provenance, aggregation across tenants with operator-tunable privacy bounds, an automated eval gate (held-out task suite per tenant) blocking promotion when patch loss does not decrease, versioned lineage with RBAC carrying tenant access policies forward through the promotion, and a rollback envelope on every promoted artifact. Naming the corner converts a vague gap into a specific four-property audit criterion; the implementor's safety requirements are deferred to follow-on practitioner work. It is no longer "no system closes both loops" — too coarse — but a specific four-property combination that the survey can audit any future system against.

Whether this corner *should* be filled is deployment-dependent. In safety-critical domains — medical decision support, legal advice, financial advice — reviewer-judgment gates may be a design feature rather than a defect, and the human latency is the point. The narrower survey claim is what matters: no public system currently combines automated local scaffold evolution with governed cross-organisation promotion, versioned lineage with RBAC, and rollback. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. The shortest demonstrable path appears to build on AlphaEvolve's cascade evaluator + MAP-Elites archive, extending federation from within-DeepMind multi-target to cross-customer multi-tenant — but the architectural surface, not the timeline, is what this paper claims.

### 9.1 Patch-complete systems

The two-tier architecture also changes the practical meaning of "general" capability. A frontier model need not be globally general for the deployed system to become effectively general inside a bounded patch. Once a localhost scaffold contains the patch's rules, tools, memories, workflows, evals, and promotion gates, the model–scaffold composite can cover the economically relevant task distribution of that patch with broad competence. We call this condition **patch-completeness**: the system is not generally intelligent over the world, but it is operationally general over the bounded world it inhabits.

This is why many production systems already feel further along than model-only benchmarks imply. A coding agent inside one repository — with project rules, tests, CI, documentation, tool access, issue history, and PR review — may be patch-complete for that repository. A legal agent inside a firm's due-diligence workflow, with vetted document stores, clause libraries, playbooks, and review gates, may be patch-complete for that workflow. The competence is not located in the model alone. It is distributed across the frontier prior and the localhost scaffold.

Patch-completeness is not global generality. It is local generality under boundary conditions. The distinction matters because the failure mode changes: a patch-complete system can appear broadly competent while silently depending on local conventions, hidden evaluator expectations, and scaffold assumptions that do not transfer. Moving it to a neighbouring patch without re-measuring the residual catalogue is therefore a patch-shift event, not ordinary deployment. The governance problem is not merely how to make scaffolds learn but *how to know where their local generality ends*. If patch-complete systems exist — and many deployed systems likely already are — then scaffold governance matters because local competence can become powerful before global robustness exists. §10 catalogues the failure surface that newly powerful local systems exhibit.

## 10. A new failure surface

Patch-plasticity introduces failure modes weight-only systems do not have. We name them here; the full taxonomy (nine categories A–I with severity ratings and counter-principles P1–P8) is deferred to follow-on practitioner work.

**Scaffold bloat** is the dominant near-term risk. IFScale (Jaroslawicz et al., 2025) reports a 35× cost increase as instruction count scales from 10 to 250, with frontier-model accuracy collapsing to 68% at 500 instructions. Lost-in-the-middle (Liu et al., 2024) supplies the mechanism. **Poisoned memory** is the dominant security risk: PoisonedRAG (Zou et al., 2024) reports 90%+ attack success rate against standard RAG; Memory Control Flow Attacks (Xu et al., 2026) report 100% persistence after injection. **Prompt injection via tools and MCP** is the dominant cross-vendor attack surface, with CVE-2025-54136 ("MCPoison") demonstrating a public MCP-server compromise pathway. **Eval fragility** is the dominant ecosystem risk: the Leaderboard Illusion (Lin et al., 2025) documents up to 112% inflation on common benchmarks under optimisation-on-test-set effects; eval suites are themselves patch-plastic artifacts and must survive Goodhart's Law. **Coordination failures** in multi-agent systems are documented in MAST (Cemri et al., 2025) — 14 distinct failure modes with $\kappa = 0.88$ agreement, dominantly role-confusion / context-loss / coordination rather than prompt quality. **Overfitting to patch** is structural: scaffolds tuned to a deployment over-fit it, and the framework predicts but does not measure how badly. **Plasticity loss at the scaffold level** is the slow-moving risk: context rot, instruction conflict, memory pollution, and tool-version drift produce a scaffold-level analogue of weight-level plasticity loss (Dohare et al. 2024, Lyle et al. 2023). Scaffolds age; a six-month-old `CLAUDE.md` is often worse than a clean rebuild, and no surveyed system treats pruning or expiration as a first-class operation.

Taken together: the patch-plastic surface is real, quantified by 2024–2026 work, and largely unmitigated in production. Follow-on practitioner work walks the mitigation principles in detail.

## 11. Conclusion

The field did not wait for frontier weights to become perfectly reliable. It built a second learning system around them. That second system is made of markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, and rollback buttons. It looks like engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights.

The mechanisms were already there. A Claude Skill has been a procedural weight since Anthropic shipped progressive disclosure. A Cursor Rule has been a local parameter since `.cursor/rules/` became a directory. A PR against `agents.md` has been a promotion gate since the Linux Foundation took stewardship. What changed in 2025–2026 is that the *combination* — these substrates wrapping a frozen frontier model and updating from deployment signal — became dense enough across vendors that the convergence reads as architecture rather than coincidence. Once you name it, the empty corners of the design space become concrete engineering targets. The most consequential one is enterprise full-auto: Auto-gated Loop 1 plus governed multi-tenant cross-org Loop 2, with versioned lineage, RBAC, and rollback. In ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer. Whether it should be filled is deployment-dependent; that it has not been is the survey's headline finding.

The five surveyed absences of §6.3 — failure-triggered memory rare in production, cross-customer skill promotion absent, memory versioning unsolved, scaffold-level curriculum unspecified, Loop-2 overfitting detection missing — are each a Paper-4 target. None of these is novel as a complaint; each is novel as a *gap the architecture makes visible*. The patch-completeness observation of §9.1 sharpens the urgency: local competence is becoming powerful enough to require governance attention before global robustness has been demonstrated.

The deepest connection — back to Paper 2 — is structural. Patch-plasticity is plastic because residual errors are clustered; if mode discovery were not slow (Postulate 1 in *Architecture of Errors*), patches would not generalise across deployments and the architecture would collapse. The survey is consistent with the postulate at the system level: deployments do generalise enough of the patch to make scaffold investment pay off. Whether this remains true at agentic, scientific, and long-horizon scales is the empirical test the next paper should design.

The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation. The mechanisms were already there — markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, rollback buttons — but they read as engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights, because that is the only place patch-specific adaptation can safely happen.

---

## Appendix A. Representative survey rows

The full per-system spreadsheet is `p3_master_scores.csv` in the repository. The 30 rows below are a representative spot-check covering all six substrates, both research and production, and all five clusters of §6.2. *Loop 1* and *Loop 2* columns apply to systems satisfying the composite-two-loop criterion; *n/a* means the loop is absent for that system. The *PP* column is the integrated patch-plasticity score (0–5) used in the survey; the *Evidence* column abbreviates the strongest available source tier (T1 peer-reviewed; T2 arXiv preprint; T3 production claim; T4 open-source artifact; T5 industry blog).

```{=latex}
\begingroup\small
```

| System | Year | Substrate | Loop 1 | Loop 2 | PP | Evidence | Why included |
|------------|---:|-----------|-------|-------|---:|------------------|------------------------------------|
| NanoResearch | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2605.10813) | Tri-level Skills/Memory/Policy co-evolution; cleanest full-auto exemplar |
| AutoAgent | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2603.09716) | Dual-cycle Execution+Evolution + elastic memory orchestration |
| SkillRL | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2602.08234) | Recursive skill-augmented RL with $\text{SR}<0.4$ threshold gate |
| AlphaEvolve | 2025 | Integrated | Auto | Auto | 4 | T2/T3 (arXiv:2506.13131) | Production proof-point: Borg +0.7%, Gemini kernel +23%, FlashAttention +32.5% |
| DGM (primary) | 2025 | Integrated | Auto | Auto | 4 | T2 (arXiv:2505.22954) | Recursive self-modifying code; SWE-bench 20%→50% |
| ADAS | 2024 | Integrated | Auto | Auto | 4 | T2 (arXiv:2408.08435) | Meta-agent search; Turing-complete agent representation |
| SkillForge | 2026 | Integrated | Auto | Human | 4 | T2 (arXiv:2604.08618) | Production hybrid exemplar; LLM-judge >90% + VFS versioning |
| CASCADE | 2025 | Integrated | Auto | Human | 4.5 | T2 (arXiv:2512.23880) | Largest published ablation gain in corpus: +57.9 pp on SciSkillBench |
| OpenCore | 2025 | Integrated | Human | Human | 4 | T4 (\url{github.com/sibmike/opencore}) | Only [Human × Human] system with explicit cross-organisation federation |
| Voyager | 2023 | Integrated | Auto | Auto | 4 | T2 (arXiv:2305.16291) | Foundational skill-library result; 3.3× items, 15.3× tech-tree milestones |
| AGENTS.md | 2025 | S1 Instructions | n/a | n/a | 2 | T3/T4 (agents.md) | Cross-vendor standard; 60k+ repos; Lulla 2026 measures −28.6% runtime |
| Claude Code CLAUDE.md | 2025 | S1 Instructions | n/a | n/a | 4 | T3/T4 (docs.anthropic.com) | Four scoping levels including org-IT policy + auto-memory layer; ceiling for S1 |
| Cursor Rules | 2024 | S1 Instructions | n/a | n/a | 3 | T3/T4 (\url{docs.cursor.com/rules}) | `.cursor/rules/*.mdc` multi-scope + MCP attach; git-tracked |
| Anthropic Agent Skills | 2025 | S2 Skills | n/a | Human | 3 | T3 (\url{anthropic.com/engineering}) | Progressive disclosure spec; LangChain replication 29%→95% pass-rate |
| SAGE | 2025 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2512.17102) | +8.9% SGC, 26% fewer steps, 59% fewer tokens on AppWorld |
| COSPLAY | 2026 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2604.20987) | Boundary proposal + segmentation; only S2 = 5 with contracts |
| Reflexion | 2023 | S3 Memory | Auto | n/a | 4 | T1 (NeurIPS 2023; arXiv:2303.11366) | Canonical failure-triggered episodic memory; +8% HotpotQA |
| Generative Agents | 2023 | S3 Memory | Auto | n/a | 4 | T1 (UIST 2023; arXiv:2304.03442) | Reflection + importance memory primitive |
| Governed Collaborative Memory (SSGM) | 2026 | S3 Memory | Auto | Auto | 5 | T2 (arXiv:2605.04264) | Only memory system with full provenance + versioning + correction |
| MCP | 2024 | S4 Tools | n/a | n/a | 5 | T3 (modelcontextprotocol.io) | Cross-vendor; 9,400+ servers; 78% enterprise; ~97M SDK downloads/month |
| Harvey | 2026 | S4 Tools | n/a | n/a | 5 | T3 (harvey.ai) | 400K queries/day; 18,000+ workflows; 200+ legal data sources |
| Hippocratic AI | 2026 | S4 Tools | n/a | n/a | 5 | T3 (hippocraticai.com) | \$3.5B valuation; 30% readmission reduction; 360% care-capacity boost |
| Multi-Agent Evolve (MAE) | 2025 | S5 Orchestration | Auto | n/a | 5 | T2 (arXiv:2510.23595) | RL co-evolution of Proposer/Solver/Judge population |
| Memento-Skills | 2026 | S5 Orchestration | Auto | Auto | 5 | T2 (arXiv:2604.02460) | Unit-test-gated skill promotion within multi-agent topology |
| Cemri et al. (AG2) | 2025 | S5 Orchestration | n/a | n/a | 3 | T2 (arXiv:2503.13657) | Specialisation +4.5 pp on GSM-Plus ($p = 0.03$); MAST 14 failure modes |
| Braintrust | 2024 | S6 Governance | n/a | Auto | 5 | T3 (braintrust.dev) | Prompts-as-code: immutable commits, eval-gated PR merge, sub-5 min rollback |
| Vellum | 2024 | S6 Governance | n/a | Auto | 5 | T3 (vellum.ai) | Same governance pattern; production deployment with eval thresholds |
| LangSmith Hub | 2024 | S6 Governance | n/a | Auto | 5 | T3 (\url{smith.langchain.com}) | Prompt repository with environment promotion and eval blocking |
| Self-Refine\* | 2023 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2303.17651) | Fails the patch-plastic discriminator: in-context iteration only |
| Mem0\* | 2024 | (contrast) | n/a | n/a | 2 | T3/T4 (mem0.ai) | Fails Loop 2: per-user memory with no cross-context promotion path |

```{=latex}
\endgroup
```

*Asterisks mark contrast systems included for definitional clarity.*

---

## References

ACE authors. (2025). Agentic Context Engineering: Evolving playbooks via generation, reflection, and curation. *arXiv preprint arXiv:2510.04618*.

AGENTS.md. (2025). AGENTS.md: A cross-vendor open standard for agent instructions. Linux Foundation. <https://agents.md>

Anthropic. (2024). Model Context Protocol specification. <https://modelcontextprotocol.io>

Arbuzov, M. L., Shvets, A. A., & Bei, S. (2025). Beyond exponential decay: Rethinking error accumulation in large language models. *arXiv preprint arXiv:2505.24187*.

Arbuzov, M. L., Shvets, A. A., & Bei, S. (2026). The architecture of errors: Logarithmic mode discovery and polylogarithmic intervention budgets for long-context LLM reliability. *arXiv preprint* (forthcoming).

Bao, M., et al. (2024). AutoManual: Constructing instruction manuals by LLM agents via interactive environmental learning. *NeurIPS 2024*. arXiv:2405.16247.

Cao, Y., et al. (2025). Mobile-Agent-E: Self-evolving mobile assistant for complex tasks. *arXiv preprint arXiv:2501.11733*.

Cemri, M., et al. (2025). MAST: A taxonomy of failure modes in multi-agent LLM systems. *arXiv preprint arXiv:2503.13657*.

Chen, S., et al. (2024). Agent S: An open agentic framework that uses computers like a human. *arXiv preprint arXiv:2410.08164*.

Chen, S., et al. (2025). Agent S2: Compositional open agentic framework. *arXiv preprint arXiv:2504.00906*.

Chen, W., et al. (2026). Governed collaborative memory / SSGM. *arXiv preprint arXiv:2605.04264*.

Dohare, S., et al. (2024). Loss of plasticity in deep continual learning. *Nature*, 632(8026), 768–774.

Du, P. (2026). Memory for autonomous LLM agents: Mechanisms, evaluation, and emerging frontiers. *arXiv preprint arXiv:2603.07670*.

Fang, J., Peng, Y., Zhang, X., et al. (2025). A comprehensive survey of self-evolving AI agents. *arXiv preprint arXiv:2508.07407*.

Gao, H.-A., Geng, J., Hua, W., et al. (2026). A survey of self-evolving agents: What, when, how. *Transactions on Machine Learning Research*. arXiv:2507.21046.

Harada, T., et al. (2025). The curse of instructions: Compliance collapse under instruction-set growth. *ICLR 2025*.

Harvey. (2026). Harvey product overview. <https://www.harvey.ai>

Hippocratic AI. (2026). Polaris clinical outcome evidence. <https://www.hippocraticai.com>

Hu, S., Lu, C., & Clune, J. (2024). Automated design of agentic systems (ADAS). *arXiv preprint arXiv:2408.08435*.

Huang, T., et al. (2025). CASCADE: A collaborative and adaptive science agent with skill distillation and evolution. *arXiv preprint arXiv:2512.23880*.

Jaroslawicz, K., et al. (2025). IFScale: Instruction-following at scale. *arXiv preprint arXiv:2507.11538*.

Jiang, P., Lin, J., Shi, Z., et al. (2025). Adaptation of agentic AI: A survey of post-training, memory, and skills. *arXiv preprint arXiv:2512.16301*.

Lin, T., et al. (2025). The leaderboard illusion: Quantifying optimisation-on-test-set effects in LLM benchmarks. *arXiv preprint*.

Liu, N. F., et al. (2024). Lost in the middle: How language models use long contexts. *TACL*.

Liu, Z., et al. (2025). Multi-agent evolve: RL for joint Proposer/Solver/Judge optimisation. *arXiv preprint arXiv:2510.23595*.

Lulla, A., et al. (2026). Empirical evaluation of AGENTS.md as a scaffold standard. *arXiv preprint arXiv:2601.20404*.

Lyle, C., et al. (2023). Understanding plasticity in neural networks. *arXiv preprint arXiv:2303.07507*.

Newell, A., et al. (1990). *Unified theories of cognition*. Harvard University Press.

OpenCore. (2025). OpenCore: Open-source LLM-assisted coding practices. <https://github.com/sibmike/opencore>. MIT License.

Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *UIST 2023*. arXiv:2304.03442.

Press, O., et al. (2022). Measuring and narrowing the compositionality gap in language models. *arXiv preprint arXiv:2210.03350*.

Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*. arXiv:2303.11366.

Sierra. (2024). Sierra Agent OS. <https://sierra.ai>

Sierra. (2025). Agent OS 2.0: From answers to memory and action. <https://sierra.ai/blog/agent-os-2-0>

SkillForge authors. (2026). SkillForge: Forging domain-specific self-evolving agent skills in cloud technical support. *arXiv preprint arXiv:2604.08618*.

SkillRL authors. (2026). SkillRL: Evolving agents via recursive skill-augmented reinforcement learning. *arXiv preprint arXiv:2602.08234*.

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive architectures for language agents (CoALA). *Transactions on Machine Learning Research*. arXiv:2309.02427.

Tan, W., et al. (2024). Cradle: Empowering foundation agents towards general computer control. *arXiv preprint arXiv:2403.03186*.

Tran, S., & Kiela, D. (2026). Memento-Skills: Unit-test-gated skill promotion for multi-agent systems. *arXiv preprint arXiv:2604.02460*.

Wang, G., et al. (2023). Voyager: An open-ended embodied agent with large language models. *arXiv preprint arXiv:2305.16291*.

Wang, X., et al. (2026). AutoAgent: Evolving cognition and elastic memory orchestration for adaptive agents. *arXiv preprint arXiv:2603.09716*.

Wu, R., et al. (2025). EvolveR: Self-evolving LLM agents through an experience-driven lifecycle. *arXiv preprint arXiv:2510.16079*.

Wu, Z., et al. (2024). OS-Copilot: Towards generalist computer agents with self-improvement. *arXiv preprint arXiv:2402.07456*.

Xu, J., et al. (2026). NanoResearch: Co-evolving skills, memory, and policy for personalized research automation. *arXiv preprint arXiv:2605.10813*.

Xu, Z., et al. (2026). Memory control flow attacks against large language model agents. *arXiv preprint* (MCFA).

Zhang, H., et al. (2026). CoEvoSkills: Self-evolving agent skills via co-evolutionary verification. *arXiv preprint arXiv:2604.01687*.

Zhang, J., et al. (2025). Darwin Gödel machine: Open-ended evolution of self-improving agents. *arXiv preprint arXiv:2505.22954*.

Zhou, Y., Shu, W., Su, Y., et al. (2026). A comprehensive survey on agent skills: Taxonomy, techniques, and applications. *arXiv preprint arXiv:2605.07358*.

Zhou, Y., et al. (2025). SAGE: Skill-augmented GRPO for self-evolution. *arXiv preprint arXiv:2512.17102*.

Zou, W., et al. (2024). PoisonedRAG: Knowledge corruption attacks on retrieval-augmented generation. *arXiv preprint*.

(DeepMind AlphaEvolve authors). (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. *arXiv preprint arXiv:2506.13131*.
