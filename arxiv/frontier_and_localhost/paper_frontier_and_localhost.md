---
title: "Frontier and Localhost: How Production AI Learns Outside the Weights"
author:
  - |
    Mikhail L. Arbuzov  
    Independent Researcher  
    mike.arbuzov54@gmail.com
  - |
    Lee Mosbacker  
    Independent Researcher  
    lee.mosbacker@gmail.com
  - |
    Sisong Bei  
    Independent Researcher  
    qurining@gmail.com
  - |
    Ziwei Dong  
    Independent Researcher  
    ziwei.dong@alumni.emory.edu
  - |
    Dmitri Kalaev  
    Independent Researcher  
    kalaevdr@gmail.com
  - |
    Alexey A. Shvets  
    Palo Alto Networks  
    ashvets@paloaltonetworks.com
date: ""
nocite: "@*"
header-includes:
  - \usepackage{xurl}
---

**Abstract**

Production LLM systems increasingly adapt outside the model weights. After deployment failures, teams modify prompts, rules, memories, skills, tools, eval suites, routing graphs, and governance pipelines on a cadence that frontier weight updates cannot match. Yet this scaffold layer is still mostly maintained as *patchwork*: fixes are proposed by intuition, committed with weak credit assignment, accumulated without pruning, and promoted beyond the scope where they were validated. The field has built an external adaptation layer for LLMs without building the optimizer that should govern it. Surveying approximately 130 production and research systems from 2023–2026, we formalise the disciplined alternative as **artifact-layer descent**: a discrete, gated, deployment-time update process in which recurring residuals are assigned to scaffold coordinates, candidate artifact deltas are tested against patch loss, accepted deltas persist with rollback, and promotion across contexts is bounded by *evidence radius* — a local fix spreads only as far as the evidence supports. The resulting two-loop architecture (local update; cross-context promotion under a gate) is consistent with convergent patterns across IDE plugins, vertical-bundle vendors, and self-evolving research agents. Thirteen research systems plus two industry exemplars satisfy a strict composite-two-loop criterion; placing them on a 3×3 matrix of gate types leaves three populated cells and three empty cells. The consequential gap is governed cross-tenant scaffold optimization: automated local evolution combined with governed cross-organisation promotion, versioned lineage with RBAC, and rollback — in ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer, in the limit where artifacts are embedded as mergeable update representations. The contribution is not the claim that prompts are weights; it is to name the missing optimizer for an adaptation layer the field has already built, and to show that the path from today's patchwork to that discipline is a tractable engineering programme. This paper is the survey and framework, jointly authored by six researchers as Part 3 of a series; a practitioner-facing companion paper will handle reference architectures, maturity ladders, design principles, and the full failure taxonomy.

---

## 1. The gradient moved outside the model

The standard mental model of an LLM system is the model. Pre-training fixes the weights; fine-tuning or RLHF nudges them; deployment wraps a thin prompt-plus-tool layer around the result and ships. Errors are weight errors; reliability is a weight-training problem.

Production has stopped behaving this way. In 2025–2026, frontier models update on cycles measured in months, but the systems built on top of them update continuously — in markdown files, persistent memories, retrieved skills, registered tools, evaluation suites, agent topologies, version-controlled prompt repositories, and PR-gated governance. A growing share of deployment-time adaptation now occurs outside the weights, in a fast-changing *localhost* scaffold wrapped around a slow-changing frontier. The section title is a metaphor — the gradient inside the model still happens during training, and the scaffold layer is not a gradient in the calculus sense. The substantive claim is the milder one: production AI has accidentally created an external learning surface, and right now it is being operated as patchwork rather than as a disciplined optimization process. What this paper formalises is the disciplined limit case — a discrete, gated, deployment-time update process that adapts a frozen frontier to the recurring failure topology of a specific patch — and what the survey finds is that almost no deployed system has yet built the optimizer for that surface.

This paper argues that scaffold evolution can be modeled as learning in a precise sense: scaffold artifacts are updated from failure signal, the updated artifacts reduce future failure probability on a local patch, and the update process — observe failure, generate candidate delta, gate it, persist it, optionally promote it — has the structure of discrete, gated, stochastic local optimization. The substrate is symbolic and human-readable rather than continuous and differentiable, and the gate stands in for the gradient; the model is best read as *artifact-layer optimization*, with descent-like behavior under the assumptions catalogued in §3 and proved in Appendix E. Where those assumptions fail (no measurable patch loss, no credit-assignment process, no persistent artifact distinct from optimiser state) the framing should be read as modeling language rather than a theorem.

Read together, these artifacts form a single external adaptation surface that current production practice still treats as scattered engineering. Naming the surface makes the optimization discipline it needs — and visibly lacks — visible. A Claude Skill is not "just a markdown file." It is a learned procedural weight kept outside the model. A Cursor Rule is not "just an instruction." It is a local parameter for one project's distribution shift. A RAG connector is not "just retrieval." It is patch-specific memory access. A tool registry is not "just integration." It is capability provisioning along an axis the base model cannot reach. A PR review against a shared rule repository is not "just governance." It is a promotion gate on a federated update. An eval suite that blocks merge is not "just testing." It is a validation-loss check before promotion. A cross-tenant artifact repository is not "just sharing." It is *federated artifact promotion* across distributed shards — scope expansion under a gate, rather than arithmetic averaging of numeric updates (we sharpen the distinction in §3 and §9). The mechanisms were already in production; what is new is reading them as a single external adaptation surface rather than as scattered engineering choices, and asking what optimization discipline that surface needs.

We survey approximately 130 systems across six substrates (instructions, skills, memory, tools, orchestration, governance), score each on a 0–5 patch-plasticity rubric, and analyse the thirteen research systems (plus two industry exemplars) that satisfy a strict *composite two-loop* criterion: an inner loop that updates a persisted artifact from session feedback, an outer loop that promotes the artifact across scopes under explicit versioning. The two-loop design space is a 3×3 matrix on gate type — *Auto-gated* when the commit-or-promote decision is operationalised by an algorithmic criterion, *Human-gated* when it is reviewer judgment. The matrix has three populated cells; three are empty for distinct structural reasons. The fully automated, governed, cross-tenant cell has no surveyed occupant. That missing architecture — governed cross-tenant scaffold optimization — is the paper's open-question headline and a concrete Paper-4 target.

The architectural review of how to actually build such systems — five reference patterns, a five-level maturity model, a substrate-selection rubric, three migration paths, the full nine-category failure taxonomy, and eight design principles — is deferred to follow-on practitioner work. This paper is the survey and the framework. The single-line thesis is this: **the field has built an external adaptation layer for LLMs, but not the optimizer that should govern it.** The rest of the paper develops that observation into a survey of where production sits on a *patchwork → random-search → descent* gradient, a formalisation of the disciplined limit case under stated assumptions, and a named missing architecture where the optimizer most plainly does not yet exist.

## 2. Why patch errors must live outside the weights

The scaffold is not merely where production systems happen to store patches. For high-churn, tenant-specific, auditable adaptation, the scaffold is *often the practical substrate* — not because no alternative exists, but because under deployment-time constraints (release cadence, tenant isolation, inspectability, rollback) it is cheap, locally scoped, reversible, and updatable at human time-scales while the weights are not. Frontier training and production reliability optimise for objectives that are in tension, and that tension pushes most patch-specific adaptation outside the model. Per-tenant fine-tunes, LoRA adapters, distilled small models, and learned routing can in principle absorb some patch residuals; the survey finds production has consequently located the bulk of patch-residual adaptation in the scaffold, but whether this remains true under different deployment constraints is an empirical question rather than a structural necessity.

**Frontier training optimises for breadth.** The weights are tuned for cross-patch generalisation: they smooth over local conventions, contradictory tenant preferences, and rare workflow-specific failures in order to preserve broad competence across millions of unseen deployments. The smoothing is not incidental. It is the training objective. A model that overfits to one tenant's naming conventions or one team's preferred error-handling style loses transfer to the next tenant; a model that encodes every patch's idiosyncratic eval expectation loses the general-purpose competence that made it worth deploying in the first place. The smoothing dynamics have been measured directly: RLHF reduces output diversity and homogenises preferred styles across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data distributions favour patterns that generalise across the annotator pool rather than patterns specific to any one deployment. The frontier model is therefore *trained to be unable* to encode a single tenant's idiosyncrasies as preferred behaviour; absorbing that idiosyncrasy without weight retraining is exactly what the scaffold layer is for. @tiwari2026fastandslow supply an independent two-timescale optimisation motivation from the in-context / in-weights side: in-context adaptation is cheap and rapid but capacity-bounded, in-weights adaptation is expressive but induces catastrophic forgetting and plasticity loss; the scaffold layer is the substrate that absorbs what in-context adaptation can carry cheaply, leaving the weights free to generalise.

**Production reliability is achieved in depth.** Inside a single deployment patch, reliability is determined by exactly the stuff global training had to smooth away: local naming conventions, team-specific workflows, domain-specific failure patterns, project-specific schemas, idiosyncratic tool chains, customer-specific risk tolerances, recurring local mistakes, institutional preferences, hidden evaluator expectations. The per-patch quantities from our previous work — failure-mode catalogue size $|C_D|$, hard-fraction $\beta_D$, mode-discovery rate $\sigma_D$ — are local by construction, and a library calibrated to one patch under-covers the next.

**Encoding every patch in the weights is structurally infeasible.** Three constraints rule out the obvious approach. *Economic:* millions of patches multiplied by billions of parameters times the cost of per-patch fine-tuning is not a viable training-compute budget. *Release-cycle:* the patch wants daily updates; weight releases ship quarterly at best. *Cross-patch interference:* overfitting the weights to one tenant's preferences degrades behaviour for adjacent tenants whose preferences contradict. The weights are tuned for cross-patch invariants by construction; that is what they are *for*.

The localhost scaffold solves the conflict. It is the substrate that uniquely satisfies all of:

- overfit aggressively to one tenant without damaging another;
- encode local conventions without polluting global behaviour;
- update daily instead of waiting for release cycles;
- be inspected, versioned, audited, and rolled back;
- attach tools, memories, rules, workflows, and evals that are meaningless outside the patch;
- specialise inside the patch while the model remains broadly competent.

Each scaffold substrate targets a different patch-residual class. Instructions and tools address *capability* residuals — the model could not do this on its own (PAL for arithmetic, RAG for retrieval, constrained decoders for format). Skills and memory address *catalogue* residuals — the same patch-specific failure mode keeps recurring and now has a patch. Orchestration addresses *hard-fraction* residuals — the per-step decision was too hard, so specialised sub-agents bring it back into capability range. Governance addresses *propagation* residuals — a correction proven in one deployment is wasted unless it can be promoted to others under audit.

Our previous work [@arbuzov2025beyond; @arbuzov2026architecture] argued that LLM errors concentrate sparsely at key tokens and cluster into a finite catalogue of recurring modes whose size grows polylogarithmically in observed failures. The framework left a *placement* question — where do the interventions live? The answer follows from the tension above. Under deployment-time constraints (release cadence, tenant isolation, inspectability, rollback), the scaffold is the substrate that satisfies all four; the survey finds that production systems consequently locate the bulk of patch-residual interventions there. The frontier model generalises; the localhost scaffold specialises; reliability comes from governing that specialisation.

## 2.5 Patchwork, random artifact search, and artifact-layer descent

Three stages of scaffold maintenance practice recur across the corpus. They differ in how candidate updates are produced, in whether failure-mode discovery and credit assignment are explicit, and in whether promotion is bounded by evidence radius.

**Stage 1 — Patchwork.** Humans add prompts, rules, tools, memories, and routing logic after failures. Each fix is proposed by intuition, committed with weak evidence, and accumulated without pruning. The dominant failure mode is bloat: scaffolds grow until lost-in-the-middle (§10) erases the marginal benefit of new additions. Most production deployments observed in the survey sit here.

**Stage 2 — Random artifact search.** Many scaffold variants are tried — A/B'd rubrics, swapped memory schemas, regenerated tool bundles — but without stable credit assignment or principled promotion. Improvements happen locally; transfer is unreliable; overfitting to the in-distribution patch is the dominant failure mode. The governance-first cluster of §7 sits here when the eval pipeline is automated but the candidate-generation pipeline is not.

**Stage 3 — Artifact-layer descent.** Candidate deltas are tied to recurring failure modes, scored by an estimator of finite directional loss change, regularized by complexity/risk penalties, accepted only when they clear a gate, versioned, prunable, and promoted only within evidence radius. The composite-two-loop systems of §8 instantiate Stage 3 for *within-organisation* scope; the missing architecture of §9 is Stage 3 for *cross-tenant* scope. The math of §3 (proved in Appendix E) applies to Stage 3 and only suggestively to Stages 1–2.

| Stage | Update mechanism | Credit assignment | Promotion discipline | Dominant failure mode |
|---|---|---|---|---|
| **1. Patchwork** | Intuition-driven local edits | Implicit / ad hoc | None | Bloat |
| **2. Random artifact search** | Many variants tried under eval | Weak; eval is the only signal | Eval-gated CI but no failure-to-coordinate tracing | Overfitting to in-distribution patch |
| **3. Artifact-layer descent** | Residual → coordinate → delta | Explicit per failure mode | Evidence-radius-bounded; reversible | (the discipline this paper formalises) |

The paper's central claim is not that today's production systems already run this loop — most do not. It is that a patchwork loop *becomes* artifact-layer descent once five pieces are in place: a measurable patch loss, captured residuals, a failure traced back to the scaffold coordinate that caused it, a synthesised candidate edit, and a gate that checks whether the edit actually lowers loss before it is kept or promoted. The survey of §§5–8 asks which deployed systems have closed which of those five steps; the missing architecture of §9 names the closure that no public system has yet reached.

## 3. Artifact-layer descent

**The disciplined version of scaffold maintenance is a concrete pipeline.** Observe a failure. Diagnose its failure mode. Identify which scaffold coordinate caused it: a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, a misrouted agent edge. Propose a candidate artifact edit. Test the edit against patch loss. Accept or reject by a gate. Persist accepted edits; prune or roll back when they regress. Promote across contexts only as far as the evidence supports. We call that last constraint the edit's *evidence radius*: a local fix should only spread to other deployments to the extent it has been validated there. The rest of this section formalises this pipeline. §§4–9 ask which deployed systems have closed which of its steps.

**Most current production does not close this loop.** A failure happens, someone adds a prompt or rule or memory entry, the artifact pile grows, nobody knows what caused improvement, nobody knows when to prune, and fixes leak into broader contexts. This is patchwork (Stage 1 of §2.5), not stochastic descent. Even systems with eval-gated CI (Stage 2) usually lack failure-to-coordinate credit assignment, so improvements are real but unattributed and brittle to transfer. Scaffold updates *become* stochastic descent (Stage 3) only when five pieces are in place: a measurable patch loss; captured residuals; a failure traced back to the scaffold coordinate that caused it; a synthesised candidate edit; and a gate that checks whether the edit lowers loss before it is kept or promoted. The descent picture below is mechanism when those five conditions hold, and modeling language otherwise.

**Two loops, in plain English first.** *Loop 1* is the local fix: a failure produces a candidate edit, the edit is tested, the accepted edit changes one deployment's scaffold. *Loop 2* is the decision whether that local fix should be shared with other deployments. It promotes from one repository to a team-wide template, from one tenant's playbook to a cross-tenant skill library, and so on. Loop 1 changes one $L_D$. Loop 2 changes *which* $L_D$ is being descended on.

**Assumptions and scope of the formalization.** The descent argument below holds when: (i) the frontier model parameters $\theta_M$ are fixed during the adaptation window; (ii) scaffold edits are persistent, inspectable artifacts distinct from transient context; (iii) the patch admits a measurable operational loss; (iv) the proposal process can attribute failures to scaffold coordinates with non-zero probability; (v) gates are imperfect estimators of finite directional loss change rather than oracle access to the true loss change; (vi) Loop-2 promotion is scope expansion under a gate, not arithmetic averaging of comparable updates. Survey claims of the form "no surveyed system has X" are bounded by the audited public corpus and the survey cutoff of May 2026.

**Patch scope hierarchy.** *Patch* is used throughout this paper with a defined scope hierarchy: USER ⊂ PROJECT ⊂ STACK ⊂ TENANT ⊂ CORE. A USER patch is one human's account or fork. A PROJECT is one repository, workflow, or product workspace. A STACK is a curated bundle of projects under one team. A TENANT is an organisation or customer. CORE is the cross-tenant universal scope. Each level induces its own loss as an average over the patches it contains. When the text says "cross-tenant promotion" it specifically means moving artifacts up to the TENANT or CORE level. "Patch-specific adaptation" without qualifier means descent on a USER or PROJECT-level loss.

The patch loss is the expected residual failure rate of the model-scaffold composite on patch $D$:

$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$

where $\theta_s$ is a structured scaffold parameter object over six substrate coordinates and $\ell$ is an operational loss (failure indicator, user-correction rate, eval error, schema violation, reviewer disagreement). The important distinction is substrate. $\theta_M$ is fixed during deployment. $\theta_s$ is the object being fit.

A failure does not yield an analytic gradient. It yields a candidate edit. The gate $G_t$ accepts the edit if its noisy estimate of the directional loss change clears a margin. The accepted edit applies to the current scaffold; rejected edits leave the scaffold unchanged:

$$\theta_s^{t+1} = \begin{cases} \theta_s^t \oplus z_t, & G_t(z_t)=1, \\ \theta_s^t, & G_t(z_t)=0, \end{cases}$$

with the gate accept condition

$$G_t(z_t)=1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \leq -\tau_t,$$

where $\widehat{\Delta}$ is the gate's estimator of the loss change, $\Omega \geq 0$ is a complexity penalty on the edit (instruction length, tool-permission breadth, promotion scope), $\lambda \geq 0$ regularises that penalty, and $\tau_t \geq 0$ is the required improvement margin. Production systems implement this without writing the equation: an eval blocks a merge on regression, a reviewer rejects a vague rule, a governance system prevents a local artifact from being shared until evidence accumulates. Different surveyed gate families instantiate the abstraction differently. Eval-cascade, RL-threshold, LLM-judge, surrogate verifier, and reviewer-judgment families directly populate the per-edit gate. Semantic-merge and MAP-Elites archive selection act as proposal-pruning steps that *precede* the per-edit gate. The per-system mapping is in Appendix C.

**Two loops, two distinct knobs.** Consider a concrete case. An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repo's instruction file. The edit is small. Its scope is one project. The same engineer could promote the rule to a team-wide template, or to the company's CORE instructions, or to a cross-tenant skill registry. The *edit* did not change. The *scope* did. And the gate that should let it through gets stricter at each step, because the loss it is being tested against is now an average over more patches, and a fix that helps one repo can hurt another.

That observation maps cleanly onto two distinct quantities in the optimisation analogy. *Edit magnitude* (how much a single accepted edit changes the local scaffold) plays the role of learning rate. *Promotion radius* (how many downstream patches the accepted edit affects) controls *which loss* is being descended on. USER-level acceptance descends on one patch's $L_D$. PROJECT promotion descends on an average over a project's patches. TENANT or CORE promotion descends on a federated average over many tenants' losses. The two knobs are independently controllable, and the gate must be calibrated against both. This is why governance is not administrative overhead. It is the regularization system that prevents a small fix from being descended on the wrong loss.

A note on Loop 2 and FedAvg. Loop 2 is *federated artifact promotion*: selection, merge, curation, review, distribution. It is not arithmetic averaging of numeric updates. FedAvg is a useful analogy only in the limit where artifacts have been embedded as mergeable update representations and the aggregation is parameter-space averaging. No surveyed system meets that limit.

Each loop has a gate. Gates are **Auto-gated** when the decision is an operationalised algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement, surrogate verifier, benchmark cascade). They are **Human-gated** when the decision is reviewer judgment. They are **None** when the loop is absent. These five terms (Loop 1, Loop 2, Auto-gated, Human-gated, None) anchor §§5–9.

The descent argument is *mechanism* when five conditions hold: a measurable patch loss; captured residuals; a failure traced back to the scaffold coordinate that caused it; a synthesised candidate edit; and a gate that checks whether the edit lowers loss before it is kept or promoted. It is *metaphor* when those conditions are absent. Appendix E formalises the assumptions A1–A5 needed for a one-step descent inequality and a convergence proposition of the loss to a $G$-stable scaffold, expands the six-operation mechanism stack, gives the full optimisation-analogy correspondence, and works through the RAG, pitch-review, tool-use, and memory cases that make the mechanism visible.

The framing positions the work against several adjacent literatures. CoALA [@sumers2023coala] proposes a static cognitive architecture of modular memory and structured action; we update CoALA's snapshot into a dynamic deployment architecture with governance. The self-evolution surveys [@gao2026survey; @fang2025comprehensive] treat agents as learners that update weights, representations, or optimiser-selected artifacts — they locate the gradient inside the model. The memory-survey of @du2026memory and the skills-survey of @zhou2026survey cover individual substrates with version-and-promotion machinery that mirrors S3 and S2 here but stops at the substrate boundary. ACE [@ace2025agentic] treats context as a single evolving playbook. Each adjacent work touches a piece of the picture; none develops the cross-substrate artifact-layer descent framing or the design space it implies.

### 3.5 SkillOpt and the convergence on artifact-layer descent

The §3 picture is mechanism when the five conditions hold and metaphor otherwise; recent work has begun to operationalise all five for skill-document adaptation. SkillOpt [@yang2026skillopt] treats a single markdown skill document as the trainable external state of a frozen agent and edits it with seven explicit deep-learning-style controls: rollout batches; reflection minibatches; add/delete/replace edits; a textual learning-rate budget with cosine decay; a held-out selection-split accept gate; a rejected-edit buffer that keeps failed proposals as negative feedback; and an epoch-wise slow/meta update for longer-horizon consolidation. SkillOpt's introduction and method make the same operational analogy explicit (parameter → skill document; gradient → trajectory-derived edit direction; learning rate → edit budget; validation check → held-out selection gate; stable training setting → batch / minibatch / schedule / gate), and the framing — *skill optimization as deep-learning-style optimization over an external natural-language state* — is the same disciplined gradient-like update mechanism for the scaffold layer that this paper argues is missing in current production.

SkillOpt is, however, one instance in a rapidly crystallising research space rather than an isolated proof of concept. The same convergence pressure this paper identifies — that the scaffold needs a disciplined optimizer, not patchwork — is arriving from at least 14 independent directions in 2025 and 2026, each instantiating a different subset of §3's five conditions, each targeting a different substrate (skill document, harness code, system prompt, shared memory), and each exposing a different gap. Read together, the family confirms the architecture is real rather than any one group's local optimum. Read against §9's four-property criterion, the family confirms that no member yet closes the cross-tenant governed-optimization corner. The remainder of this section gives the SkillOpt walkthrough as the canonical worked instance and then names the convergent landscape; Appendix G walks each cluster in detail.

Mapped onto §3, SkillOpt instantiates each abstract quantity with a concrete mechanism. The compact correspondence below tracks the eight load-bearing pieces of the §3 formalism; Appendix G expands every row with the exact algorithm-level mechanism, including pointers to SkillOpt's Algorithm 1 line numbers.

| §3 quantity | SkillOpt instantiation | Mechanism | Numerical signature |
|---|---|---|---|
| $\theta_s$ (scaffold) | `best_skill.md` | persistent text artifact, exported as the deployment object | 379–1,995 tokens; ×2.5–53 growth |
| $L_D$ (patch loss) | held-out hard / exact-match score | per-benchmark evaluator | 6 benchmarks |
| $Q_t$ (proposal) | optimizer-model reflection over failure and success minibatches | LLM-judge over rollout batch | $B_m{=}8$, parallel reflectors |
| $z_t$ (edit) | add/delete/replace patch on the skill | structured JSON edit | 1–4 accepted edits per skill |
| $L_t$ (textual learning rate) | bounded edit budget per step | constant/linear/cosine/autonomous schedule | $L_t \in \{1,2,4,8,16\}$ |
| $G_t$ (gate) | held-out selection-split accept gate | strictly-greater validation | ties rejected |
| rejected-edit buffer | epoch-local store of failed proposals | training-time negative feedback only | zero inference cost |
| slow/meta update | epoch-wise longitudinal guidance written to a protected slow-update field | second-order consolidation | $-22.5$ pts on SpreadsheetBench when removed |

The headline empirics make the descent picture testable rather than aspirational. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied-best on all 52 evaluated (model, benchmark, harness) cells, lifting GPT–5.5 by +23.5 / +24.8 / +19.1 points over no-skill under direct chat / Codex / Claude Code, and beating the strongest per-cell baseline drawn from TextGrad, GEPA, Trace2Skill, EvoSkill, human-skill, and one-shot-LLM by +5.4 points on average. Transfer is also measured: a SpreadsheetBench skill trained inside the Codex loop transfers to Claude Code at +59.7 over that harness's no-skill baseline, and an OlympiadBench skill yields positive gains on Omni-MATH at every model scale tested. In §3 vocabulary: SkillOpt closes Loop 1 under an algorithmic gate, runs an epoch-wise auto-gated stabiliser as a second algorithmic loop, and reports cross-model / cross-harness / cross-benchmark transfers that read as *empirical evidence-radius measurements* — Loop-2 scope expansion that is sound for the demonstrated radii while no cross-organisational governance is shipped. We carry that distinction into §§7–9.

**The convergent landscape.** Five clusters of concurrent work instantiate complementary subsets of §3's mechanism stack, each targeting a different substrate or exposing a different constraint. The *reflective-evolution* family [GEPA; @agrawal2025gepa] instantiates $Q_t$ via reflection-as-gradient over trajectory feedback and a Pareto-frontier proposal-pruning step, leaving the SkillOpt-style persistent skill artifact $\theta_s$ and strictly-greater held-out gate open; @tiwari2026fastandslow supply the matching two-timescale motivation cited in §2. *Reflective Context Learning* [@vassilyev2026rcl] is the most direct independent formalisation: it observes that "the fundamental problems of learning, including credit assignment, overfitting, forgetting, local optima, and high-variance learning signals, persist whether the learned object lies in parameter space or context space" and introduces a generalisation penalty that maps onto §3's $\Omega(z)$. A *harness-optimisation* cluster [Meta-Harness, @lee2026metaharness; AHE, @lin2026ahe; MOSS, @cai2026moss; CANTANTE, @zehle2026cantante; @ong2026harnesseval] targets the orchestration substrate (§4, S5) rather than the skill substrate, names credit assignment as the central engineering bottleneck of scaffold evolution, and — in MOSS's case — extends evolution to source-level code that is "physically unreachable from the text layer." A *multi-objective + lifecycle* pair [MOCHA, @tanjim2026mocha; Ratchet, @zhang2026ratchet] sharpens two assumptions of the §3 picture: MOCHA shows that the complexity penalty $\Omega(z)$ is a Pareto frontier rather than a scalar, and Ratchet shows that lifecycle hygiene (outcome-driven retirement, bounded active-cap, pattern canonicalisation) is a precondition for residual capture and mode discovery — the gap between LLM-authored skills ($+0.0$ pp over no-skill) and human-curated skills ($+16.2$ pp) is Ratchet's evidence that the bottleneck is lifecycle management, not authoring alone. A *cross-task transfer / evidence-radius* cluster [ICT, @shalev2026ict; Combee, @li2026combee; CORAL, @qu2026coral; PACE, @ling2026pace] instruments Loop 2 empirically: ICT measures the lower bound of evidence radius (one task), Combee scales the evidence pool through parallelism, CORAL provides the only asynchronous multi-agent Loop-2 mechanism in the current corpus through shared persistent memory and a heartbeat gate, and PACE demonstrates the two-timescale Loop-1 / Loop-2 architecture under small-frozen-model production constraints.

| Cluster | Representative systems | §3 mechanism instantiated | What is left open |
|---|---|---|---|
| Reflective-evolution | GEPA; Tiwari et al. | $Q_t$ over trajectory evidence; two-timescale motivation | persistent $\theta_s$; $L_t$ budget; held-out $G_t$ |
| Reflective context | RCL (Vassilyev et al.) | $\theta_s$ over context space; $\Omega(z)$ as generalisation penalty | cross-deployment Loop 2 |
| Harness optimisation | Meta-Harness; AHE; MOSS; CANTANTE; Ong et al. | credit assignment over S5; source-level extension | governed Loop 2 across orgs |
| Multi-objective + lifecycle | MOCHA; Ratchet | constraint Pareto frontier; hygiene-as-precondition | gradient-analogue closure |
| Cross-task transfer | ICT; Combee; CORAL; PACE | empirical evidence-radius; async multi-agent Loop 2 within one org | cross-organisational gate, lineage, rollback |

**What the convergence establishes.** Read against the §3 mechanism stack and the §9 four-property criterion, four claims are now well-supported. *(i)* The scaffold-versus-weights decomposition is independently confirmed: GEPA, Meta-Harness, MOSS, RCL, and PACE all begin from the observation that model weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope properties. *(ii)* Credit assignment — attributing a system-level failure to a specific scaffold coordinate (§3 operation 3, Appendix E.1) — is the central engineering bottleneck, named explicitly by AHE, CANTANTE, Meta-Harness, and Ong et al. *(iii)* Lifecycle hygiene is a precondition for descent, not an alternative to it: Ratchet establishes that a dirty artifact pool prevents the gate $G_t$ from receiving a meaningful signal. *(iv)* No surveyed system combines Loop-1 automation with cross-organisational Loop-2 governance — §9's four-property gap is not reduced by any member of the cluster; it is confirmed more strongly by the independent convergence of multiple research threads on the same single-organisation ceiling. The §3 picture is not aspirational. It is the limit that the field is converging on from multiple directions simultaneously, under multiple framings and for multiple substrates; what remains is the governance layer that would allow a locally-validated edit to be promoted to a cross-organisational scope without losing auditability, rollback safety, and evidence-radius discipline.

Appendix G expands the SkillOpt walkthrough, contrasts SkillOpt against each of the six baselines it measures, and walks each convergent cluster in detail with the §3 mappings stated explicitly.

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

Each substrate maps to a different Paper-2 residual class. S1 and S4 carry capability provisioning. S2 and S3 accumulate the patch-specific failure-mode catalogue. S5 lowers per-step hard-fraction by specialisation. S6 is the gate substrate — without it, none of the other five can be updated safely across deployments. *The substrates are not a taxonomy of nice-to-haves. They are the layers of the scaffold parameter vector, separately addressable by Loop 1 and Loop 2.* Score distributions and per-substrate exemplars are summarised in §6.1; the maturity-rubric details for practitioner adoption are deferred to follow-on work. We adopt this six-coordinate decomposition for the survey because each coordinate is independently editable in production systems (a Cursor rule can change without touching a tool schema; an eval threshold can change without touching a memory store); alternative partitions are possible (e.g., separating evals from governance, or merging instructions and skills) and the descent argument of §3 is invariant to the partition so long as the independent-editability property holds.

## 5. Survey method and evidence tiers

The survey covers approximately 130 unique LLM systems published or productionised between January 2023 and May 2026, split into two sets.[^count-note] The **core corpus** of approximately 90 candidate scaffold-learning systems satisfies the patch-plastic discriminator (score ≥ 3 on at least one substrate, indicating skills, memory, or multi-scope persistence beyond ephemeral prompts). The **contrast corpus** of approximately 38 systems is commonly described in the public discourse as agentic or self-improving but fails at least one discriminator — typically Loop 2 absent, no persistent artifact distinct from optimiser state, or in-context-only adaptation. Headline statistics quote the core corpus; the contrast set is preserved as asterisked entries in the matrices for definitional clarity.

[^count-note]: The master CSV (`supplementary/p3_master_scores.csv`) records each system as one row per scored substrate, so the row count exceeds the unique-system count. Cited figures throughout §§5–8 refer to unique systems; Appendix B reconciles the per-substrate row count, the unique-system count, and the patch-plastic core/contrast split.

**Inclusion.** Any system that (a) wraps a foundation model with at least one persistent artifact updated from deployment signal, or (b) is named in the public discourse as a "self-improving," "scaffolded," or "agentic" system. The contrast set (Self-Refine, ReAct, plain Mem0, DSPy/TextGrad, etc.) is included precisely so the discriminator has something to mark against.

**Exclusion.** Systems whose only update mechanism is weight-level fine-tuning or RLHF — these are model-side, not scaffold-side, and belong to the self-evolution literature this paper differentiates from. Systems with no public evidence of deployment (white papers without code, demos, or production claim).

**Evidence tiers.** Each system carries one or more of: (T1) peer-reviewed publication, (T2) arXiv preprint, (T3) production claim with metrics, (T4) open-source artifact (GitHub, registry), (T5) industry-blog or interview-level documentation. Systems with T1 or T4 evidence carry highest weight in the cluster analysis (§7); T3 systems are admissible where the claim is concrete (specific benchmark, named integration target); T5 systems are admissible only when corroborated by T1–T4 elsewhere. Tier flags are propagated to cluster claims through the per-row evidence column in Appendix A; T3 production claims are not pooled with T1/T2 evidence when computing cluster-level statistics. **Survey window and dating.** The corpus includes arXiv preprints published through May 2026; preprint-only systems carry T2 evidence and are flagged in Appendix A. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.

**Scoring.** Each system received a substrate-by-substrate 0–5 score against the rubric of §4 and an integrated patch-plasticity (PP) score in {0,1,2,3,3.5,4,4.5,5}. Half-scores were used sparingly for systems where one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). Scoring is single-rater; the supplementary CSV exposes every per-system score so reviewers can audit ambiguous classifications independently against the per-substrate evidence harvests (`supplementary/p3_harvest_s1_instructions.md` through `p3_harvest_s6_governance.md`).

**Composite two-loop criterion.** A separate, stricter audit applied to 22 candidate systems. A system qualifies as composite two-loop if and only if it satisfies both: Loop 1 modifies a persisted artifact from a session signal *and* Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage. Thirteen research systems passed the strict audit, with two additional industry exemplars (Sierra Agent OS 2.0, Cognition Devin) evaluated using vendor documentation as primary evidence and explicitly flagged in the matrix of §8; nine systems failed (MAE, MetaGen, MetaReflection, CLIN — Loop-2 absent; DSPy, TextGrad — no persistent artifact distinct from optimiser state; Mem0, Zep, ChatGPT Memory — no Loop-2 promotion path).

**Sensitivity analysis.** Under relaxation (a) — counting any of *versioning OR lineage OR rollback* as the Loop-2 governance criterion — the composite-two-loop count rises from thirteen research systems to approximately seventeen, by re-admitting MAE, MetaGen, MetaReflection, and CLIN that were excluded for lacking versioned promotion lineage. Under relaxation (b) — admitting session signal that updates optimizer state without persisting an artifact distinct from optimiser state — the count rises to approximately fifteen, by re-admitting DSPy and TextGrad. The qualitative findings (Auto×Auto well-populated, [Human × Human] and [Human × Auto] empty in the surveyed corpus, governance-first cluster in [None × Auto], cross-tenant governed-optimisation cell empty) survive both relaxations. The CSV bundled in `supplementary/` permits readers to re-run either relaxation.

**Audit trail.** The full per-system spreadsheet (`supplementary/p3_master_scores.csv`), per-substrate evidence harvests (`supplementary/p3_harvest_s1_instructions.md` through `p3_harvest_s6_governance.md`), integrated audit (`supplementary/p3_harvest_integrated.md`), composite-two-loop audit (`supplementary/p3_harvest_composite_two_loop.md`), failure-mode harvest (`supplementary/p3_harvest_failure_modes.md`), and prior-art check (`supplementary/p3_prior_art_check.md`) ship inside the arXiv source bundle. Reviewers can re-run the analysis from primary sources.

## 6. Survey findings: the scaffold is unevenly mature

The patch-plastic core corpus does not mature uniformly. Tools and integrated systems are the most mature substrates; skills and orchestration lag; instructions are ubiquitous but shallow; memory is the most paradoxical of the six. This section presents the headline distributions before the cluster interpretation of §7. The full per-system spreadsheet is `supplementary/p3_master_scores.csv`; Appendix A lists representative rows.

### 6.1 Substrate maturity is uneven

Aggregating the survey by substrate gives this distribution:

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|--------------|---:|----:|----------------------|-------------------------------------------------------|
| **S1 — Instructions** | 12 | 2.83 | *(none)* | Rules persist across IDEs and agents (Claude Code's CLAUDE.md, Cursor Rules, AGENTS.md, Windsurf, Continue.dev) but no surveyed instruction system closes both an automated inner loop and a governed two-loop promotion. Ceiling held at 4 by Claude Code and Replit |
| **S2 — Skills** | 16 | 2.62 | SAGE, COSPLAY | Research frontier is active (failure-triggered skill update); production governance is weaker. Anthropic's skills repository is one-pool with PR review but no automated eval gate |
| **S3 — Memory** | 19 | 3.16 | Cuadros et al. governed collaborative memory | Cross-session memory is widespread; *correctable, versioned* memory is rare. Production memory systems (ChatGPT Memory, Claude Memory, Mem0, Zep, MemGPT) treat memory as append-only |
| **S4 — Tools** | 19 | 3.63 | MCP, Harvey, Hippocratic AI | Most mature production substrate. Tool bundles are the commercial unit; MCP is the cross-vendor standard with broad public-server ecosystem and substantial enterprise adoption |
| **S5 — Orchestration** | 19 | 2.68 | *(none)* | Multi-agent topologies exist (LangGraph, AutoGen, CrewAI) but topology *evolution* is rare; MAE comes closest with RL co-evolution of Proposer/Solver/Judge population but lacks Loop-2 cross-context promotion and so does not satisfy the score-5 rubric; production rarely exposes governed promotion paths for emerging agent graphs |
| **S6 — Governance** | 21 | 3.05 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | High production maturity for prompts-as-code — immutable commits, eval-gated PR merge, sub-five-minute rollback — typically without inner-loop adaptation |
| **INTEGRATED** | 34 | 3.74 | NanoResearch, AutoAgent, SkillRL | The high-water mark when present, but the cluster is dominated by research systems lacking enterprise governance |

The unevenness is the survey's central empirical pattern. The field has independently converged on the six substrates, but no system matures all six at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation; vertical-bundle vendors solve patch specificity but rarely expose cross-tenant promotion. The missing architecture is not "agents with tools" or "memory with evals." It is *governed scaffold adaptation* — fast local learning paired with safe cross-context promotion.

### 6.2 Representative systems by cluster

Four clusters recur across the corpus. The grouping below maps each system to its gate types and to the structural lesson it carries. The matrix in §8 places the same systems on the 3×3 design space.

| Cluster | Representative systems (year, PP score) | Loop 1 / Loop 2 | What the cluster proves |
|--------------|------------------------------|--------------|------------------------------------------|
| Research full-auto | NanoResearch (2026, 5), SkillRL (2026, 5), AlphaEvolve (2025, 4), DGM (2025, 4), ADAS (2024, 4), Voyager (2023, 4) | Auto / Auto | Both loops can be fully automated under algorithmic gates; benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge (2026, 4), CASCADE (2025, 4.5), Sierra OS 2.0 (2025, 3)[^sierra-dual], Cognition Devin (2024, 3) | Auto / Human | Algorithmic Loop-1 gate plus reviewer-judgment Loop-2 gate is the production-viable cell; SkillForge is the architectural exemplar |
| Governance-first | Braintrust, Vellum, LangSmith Hub (all 2024, S6 = 5) | None / Auto | Eval-gated promotion exists; candidate generation is manual (engineers iterate prompts); no patch-plastic inner loop |
| Open standards | AGENTS.md (2025), MCP (2024), Claude Skills (2025), Cursor Rules (2024) | Mixed / Mixed | Vendor-cross convergence on artifact format and tool attachment; tens of thousands of AGENTS.md repositories; broad MCP server ecosystem with substantial enterprise adoption |

[^sierra-dual]: Sierra Agent OS 2.0 also appears in the *Open standards / vertical-bundle* discussion in §7 because its commercial product wraps a vertical workflow around the standardised agent-OS surface; we place it primarily in *Production hybrid* on the basis of its Loop-1/Loop-2 gate types.

### 6.3 Surprising absences

What is missing from the survey is as instructive as what is present. Five absences stand out across the patch-plastic core corpus:

1. **Failure-triggered memory is rare in production.** Deployed memory systems prefer recording preferences and successful facts; only Reflexion, the Voyager skill library, Gemini Code Assist's PR-rejection memory, and the classical SOAR chunking pattern explicitly record residuals. The most obvious Loop-1 signal is the one production memory systems mostly ignore.
2. **Cross-customer skill promotion is absent.** AGENTS.md is cross-vendor; Anthropic's skills repository is one-pool. No surveyed system has a vetted cross-organisational marketplace with eval-gated promotion.
3. **Memory versioning is mostly unsolved.** Only the @cuadros2026governed governed collaborative memory framework provides explicit provenance, versioning, and correction pathways. Production default is append-only with implicit retrieval-based forgetting — at odds with the patch-plastic discriminator's correction requirement.
4. **Scaffold-level curriculum is absent.** No surveyed system selects *which* sessions inform the gradient. Every session contributes equally; weighting by recency, severity, or representativeness has not been published.
5. **Overfitting detection at Loop-2 promotion is absent.** No surveyed system runs a held-out eval set per project to catch scaffolds that over-fit one deployment before they propagate to another.

Each absence is a Paper-4 target. The conclusion echoes them; the survey makes them visible.

## 7. Convergent patterns

The corpus, scored against the rubric of §4, produces four archetypal clusters that recur across both research and industry. We present the clusters here rather than walking every system; the full table is in `supplementary/p3_master_scores.csv`.

**Research full-auto.** Systems where both loops fire from algorithmic criteria and no human gates the routine update. **NanoResearch** [@xu2026nanoresearch] co-evolves Skills, Memory, and Policy with a semantic-merge orchestrator; Innovation 4.96 → 5.65 and Compliance 6.66 → 8.96 across three rounds. **SkillOpt** [@yang2026skillopt] operationalises the deep-learning-optimizer analogy explicitly, with held-out validation gating, rejected-edit buffers, cosine-decay textual learning rate, and epoch-wise slow/meta consolidation that together resemble standard SGD machinery applied to a markdown artifact (§3.5; Appendix G). **SkillRL** [@skillrl2026] uses RL reward distillation with a hard threshold at task-category accuracy below 0.4 and reports +15.3% over strong baselines. **AlphaEvolve** [@alphaevolve2025] runs a Gemini-driven ensemble with a cascade evaluator and a MAP-Elites archive, deployed at Google to gain +0.7% Borg compute worldwide, +23% on the Gemini training kernel, +32.5% on FlashAttention, and the first general-field, recursively applicable improvement over Strassen's 1969 bound on 4×4 complex matrix multiplication (48 scalar multiplications). The honest framing matters: AlphaTensor [@fawzi2022discovering] had already found a 47-multiplication algorithm over GF(2), and Winograd reported a 48-multiplication method for commutative rings that was not recursively applicable; AlphaEvolve's contribution is the first improvement that holds in general fields and admits recursive composition. **DGM** [@zhang2025darwin] modifies its own source code with archive-based parent selection; SWE-bench 20% → 50%. The cluster maximises velocity. Enterprise governance is uniformly absent.

**Production hybrid.** Systems where Loop 1 is Auto-gated (an algorithmic criterion) and Loop 2 is Human-gated (reviewer approval before propagation). **SkillForge** [@skillforge2026] drives auto-generated skill diffs through an LLM-judge with >90% human agreement (the Loop-1 gate); human support engineers then review what the LLM-judge passes (the Loop-2 gate). VFS version commits provide full lineage. **CASCADE** [@huang2025cascade] reports the largest within-benchmark ablation gain in the surveyed corpus — 93.3% vs. 35.4% on SciSkillBench (+57.9 pp) — driven by memory consolidation gated by human-agent collaboration. The headline gain is not directly comparable to AlphaEvolve's production +0.7% Borg or DGM's +30 pp on the broader SWE-bench: it is measured on a single benchmark designed to reward the very mechanism CASCADE adds, and should be read as evidence of mechanism-on-benchmark fit rather than as a cross-cluster effect size. **Sierra Agent OS 2.0** routes AI-driven Insights through human-authored Expert Answers in GitHub-style Workspaces. **Cognition Devin** ships dynamic in-session tool creation with a 67% PR-merge rate (the merged PRs are the Loop-2 promotion). This is the production-viable cell.

**Governance-first.** Systems where Loop 2 is Auto-gated by an eval criterion but Loop 1 is essentially absent — there is no automatic candidate-generation pipeline. **Braintrust**, **Vellum**, **LangSmith Hub**, **W&B Weave**, **Agenta**, **LangFuse**. The pattern is *prompts-as-code*: immutable commits, semantic-version tag pointers, PR-blocked merges on eval regression, sub-five-minute rollback. Engineers iterate the artifacts manually; the eval pipeline gates the promotion. We frame this as **MLOps for scaffolds**, distinct from MLOps for weights.

**Open standards.** Systems where the artifact format and the layering convention are open standards across vendors. **AGENTS.md** [@agentsmd2025] is now in over 60,000 GitHub repositories; @lulla2026empirical report −28.64% wall-clock and −16.58% tokens with no quality loss after adding an AGENTS.md scaffold. **MCP** [@anthropic2024mcp] has become the cross-vendor standard with thousands of public servers and substantial enterprise adoption. **Claude Agent Skills**, **Cursor Rules**, **GitHub Copilot custom instructions**, **Windsurf rules**, **Continue.dev rules**, **Zed AI rules**, **Replit `replit.md`** all converge on the same pattern: a git-tracked markdown artifact attached to a workspace, with an MCP-style tool layer for actions. Convergence across vendors is the strongest evidence the architecture is real rather than a single vendor's local optimum.

The four clusters do not partition the corpus — many systems sit between two clusters — but they capture the architectural variation. Vertical-bundle vendors (Harvey for legal, Hippocratic AI for healthcare, Sierra for customer experience) sit between *open standards* and *production hybrid*: the bundle is the commercial unit; the underlying model is mostly the same one a competitor would use.

One result from the orchestration literature bounds how strongly any of these clusters can be read as evidence for multi-agent architectures specifically. @tran2026singleagent report that single-agent LLMs match or beat multi-agent systems on multi-hop reasoning when thinking-token budgets are matched; the implication is that observed maturity gaps on S5 (orchestration) may reflect the rarity of governed topology *evolution* and the conflation of agent-count with compute-budget rather than a structural deficit of multi-agent designs. The orchestration cluster is therefore better read as evidence that production has converged on flat agent topologies and on tool-mediated rather than role-mediated decomposition, not as evidence that orchestration is the binding maturity constraint.

## 8. The two-loop design space

The composite-two-loop systems sit in a 3×3 matrix indexed by gate type on each loop. Thirteen research systems satisfy the strict criterion, with two production exemplars (Sierra Agent OS 2.0, Cognition Devin) included on the basis of vendor documentation as primary evidence and explicitly flagged.

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, ADAS, DGM[^dgm-dual], Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, Sierra OS 2.0†, Cognition Devin† | MAE\*, MetaGen\*, MetaReflection\*, CLIN\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in surveyed corpus]** | *(none)* |
| **Loop-1 None** | ExpeL (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repo\*, DSPy\*, TextGrad\* | Self-Refine\*, ReAct\*, Mem0\* |

*Asterisks fail at least one composite-two-loop criterion; included for contrast.* † Industry exemplar evaluated using vendor documentation as primary evidence.

[^dgm-dual]: DGM operates in both Auto×Auto (primary archive-based evolution) and Auto×Human (sandboxed code-modification review) modes depending on deployment configuration; we list it once in the dominant cell.

The matrix has three populated cells of interest. **[Auto × Auto]** is most populated (twelve systems). Every member has a machine-evaluated decision criterion on both loops. **[Auto × Human]** is the production-viable cell — Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. **[None × Auto]** holds the governance-first prompts-as-code systems. Three cells are empty for distinct reasons. **[Human × Auto]** is empty by engineering logic; if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping), but no published example exists. **[Human × Human]** is empty in the surveyed corpus; a candidate occupant would be a reviewer-authored-and-reviewer-promoted artifact pipeline targeting solo and small-team workflows where the marginal cost of a bad auto-merge exceeds the marginal cost of human latency — no public example was found during the May 2026 survey window. **[Human × None]** is structurally improbable: a system that requires human authorship on Loop 1 but has no Loop 2 at all collapses to "engineer-edits-a-config" and is not patch-plastic in the sense of §3.

The **[None × Auto-gated]** cell holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 — eval-gated CI blocks promotion on regression — but no Loop 1 in the patch-plastic sense, because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative precisely because it shows what survives when only the outer loop is automated.

Two cross-cutting findings sharpen the picture. **Noise reduction via batching is largely absent in the surveyed auto-gated systems**: every auto-gated system in [Auto × Auto] and [Auto × Human] fires at $n = 1$ per generation step, absorbing estimator noise statistically via the per-edit gate rather than aggregating evidence across multiple candidate edits. SkillOpt is a partial exception: it explicitly batches evidence (rollout batch $B$ and reflection minibatch $B_m{=}8$) and decays edits via a learning-rate schedule, so the noisy-estimator absorption is done by aggregation as well as by the per-edit gate; the $n{=}1$ characterisation still holds for the *single accepted edit per step*, but the proposal evidence is aggregated. Multi-sample agreement filters (accept only when $k$ independent dreams or trajectories converge on the same proposal) are a tractable design dimension that no surveyed system has formalised; the noise-reduction behaviour of such a filter is qualitatively different from mini-batch averaging — false-accept probability shrinks roughly as $p^k$ rather than variance shrinking as $1/k$ — and the two should not be conflated. **Multi-layer hierarchies are under-explored**: only AlphaEvolve demonstrates explicit depth in the auto-gated cluster, via the cascade evaluator and MAP-Elites archive. The other twelve composite-two-loop systems treat their artifact pool as flat. Adding a STACK-style intermediate layer to NanoResearch or a multi-archetype scope to Anthropic's skills repository is a tractable engineering direction. The full cell-by-cell discussion, the closest-approaches enumeration that supports §9, and the DGM dual-mode footnote are expanded in Appendix F.

## 9. The missing architecture: governed cross-tenant scaffold optimization

Four properties define the architecture that no surveyed system fully instantiates:

- (a) **Auto-gated Loop 1.** The commit criterion is an algorithmic threshold.
- (b) **Multi-tenant cross-org promotion.** Loop 2 routes artifacts between organisations.
- (c) **Versioned lineage with RBAC.** Promoted artifacts carry semantic versions, audit trails, and access-control policies.
- (d) **Rollback.** A bad promotion can be reverted without redeploy.

The closest approaches partition the requirements. AlphaEvolve has (a) and partial (b) within a single organisation. SkillForge has (a) and (b) within one enterprise with partial (c) via VFS commits. SkillOpt (§3.5; Appendix G) has (a) fully and partial (c) via the exported `best_skill.md` artifact and the protected slow-update field, and reports positive cross-model / cross-harness / cross-benchmark transfer as empirical evidence-radius measurement; it does not implement (b) cross-organisational promotion or (d) explicit rollback. CORAL [@qu2026coral; Appendix G.8] has partial (a) via heartbeat-gated promotion and asynchronous multi-agent Loop 2 within one system; no (b) cross-organisational scope, no formal (c) RBAC, no (d) rollback. PACE [@ling2026pace; Appendix G.8] has (a) at the small-model production timescale and a fast/slow two-timescale Loop-1 + Loop-2 that consolidates across one deployment's own episodes; no cross-deployment (b), no formal (c) or (d). Meta-Harness [@lee2026metaharness; Appendix G.6] has (a) over the harness substrate (S5) with a filesystem-of-candidates credit-assignment record; no Loop-2 cross-organisational promotion, no RBAC or rollback. Sierra Agent OS 2.0 has (b) and partial (a). The governance-first cluster has (c) and (d) explicitly but no (a) or (b) in the strict sense. The convergent evidence sharpens rather than reduces the §9 gap: every closest approach satisfies a non-trivial subset of (a) and (c), but no member yet provides (b) or (d) under any governance regime. The full enumeration is in Appendix F.

In ML terms, what is missing is a privacy-preserving cross-tenant aggregator with an automated eval gate at the scaffold layer. Such an architecture would carry five parts: per-tenant artifact pools, each tagged with where its artifacts came from; a way to aggregate across tenants that the operator can tune for privacy; an automated eval gate that blocks a promotion whenever it does not lower patch loss; versioned lineage with RBAC; and a rollback envelope on every promoted artifact. The DP-FedAvg framing from the federated-learning literature is a useful analogy for this target, but only if artifacts are first embedded as mergeable update representations. In surveyed practice, Loop 2 is selection and review rather than parameter averaging.

Naming the missing architecture converts a vague gap into a four-property audit criterion that any future system can be measured against. Whether it *should* be filled is deployment-dependent. In safety-critical domains, reviewer-judgment gates may be a design feature rather than a defect. But no public system currently fills it, and that is what matters for the next two years of architecture work. Whether the optimizer-equipped composite reaches deployment-level reliability is a deployment-by-deployment empirical question; the paper's contribution is to name what *would have to be true* of the optimizer for that question to even be testable.

### 9.1 Patch-completeness as an operational hypothesis

The two-tier architecture also raises a measurable question about the meaning of "general" capability in production. We define **patch-completeness** as a testable operational condition rather than a philosophical claim about generality:

> A model–scaffold composite is *(r, n, d)-patch-complete* for a deployment patch $D$ when its residual error rate on a stationary patch eval suite of size $n$ stays at or below $r$ over a deployment window of $d$ days.

This definition makes patch-completeness an empirical property of a specific deployment and a specific eval, not of a system in general. It is *not* a claim that any deployed system is patch-complete in the colloquial sense, nor that a patch-complete system in this sense is intelligent in any global sense. The values of $r$, $n$, and $d$ depend on the patch: a coding agent inside one repository, a legal agent inside one firm's due-diligence workflow, or a support agent on one product surface each implies its own choice.

We are not aware of any surveyed system that has formally demonstrated $(r, n, d)$-patch-completeness for a fixed $r$, $n$, $d$ with held-out evaluation and a stationary patch over a non-trivial $d$. The framework predicts such demonstrations should appear in narrow production verticals — a coding agent confined to one repository with stable conventions, a legal agent confined to a stable due-diligence workflow — once eval discipline catches up with deployment scope. The governance question is then operational: at what residual rate $r$ and over what window $d$ is local competence load-bearing enough to require governance attention even before global robustness is established? §10 catalogues the failure surface that the answer would have to account for.

## 10. A new failure surface

Patchwork scaffold maintenance introduces failure modes weight-only systems do not have; instrumenting the loop to Stage 3 (§2.5) is what mitigates them at the architectural level, with the specific countermeasures deferred to follow-on practitioner work. We name the failure surface here; the full taxonomy (nine categories A–I with severity ratings and counter-principles P1–P8) is deferred to that companion.

**Scaffold bloat** is the dominant near-term risk. IFScale [@jaroslawicz2025ifscale] reports latency growing roughly 35× for one reasoning model (o4-mini, 12.4s → 436s) as instruction count scales from 10 to 250, and the best-performing frontier model in that benchmark (Gemini 2.5 Pro) drops to 68% accuracy at 500 instructions; weaker models degrade further (GPT-4o to 15%). The result is a 2025 snapshot, and a 2026 follow-up using a later model generation reports the accuracy degradation softening substantially on the same task family, so the precise numerical collapse is model-generation-dependent; the underlying mechanism [lost-in-the-middle, instruction interference; @liu2023lostmiddle] persists, and scaffolds that accumulate hundreds of unpruned instructions remain exposed even when individual frontier-model scaling improves. Ratchet [@zhang2026ratchet] supplies direct empirical evidence that bloat is also a *signal-quality* problem and not only a latency one: prior evaluation reports LLM-authored skills at $+0.0$ pp over no-skill baselines while human-curated skills reach $+16.2$ pp, which Ratchet attributes to lifecycle management and addresses with four hygiene mechanisms (outcome-driven retirement, bounded active-cap, meta-skill authoring, pattern canonicalisation); in §3 vocabulary, lifecycle hygiene is a precondition for residual capture and mode discovery to function, not an alternative to descent (Appendix G.7). **Poisoned memory** is the dominant security risk: PoisonedRAG [@zou2024poisonedrag] reports 90%+ attack success rate against standard RAG; Memory Control Flow Attacks [@xu2026mcfa] report >90% vulnerability across major LLM agent frameworks. **Prompt injection via tools and MCP** is the dominant cross-vendor attack surface, with CVE-2025-54136 ("MCPoison") demonstrating a public MCP-server compromise pathway. **Eval fragility** is the dominant ecosystem risk: the Leaderboard Illusion [@singh2025leaderboard] documents up to 112% relative performance gains on the Chatbot Arena distribution under differential training-data access — a structural overfitting pathway, not benchmark error; eval suites are themselves patch-plastic artifacts and must survive Goodhart's Law. @ong2026harnesseval extend the diagnosis to scaffold optimisers themselves: evaluating harness optimisers solely by target-agent performance gains cannot distinguish *informed* Loop-1 updates from Stage-2 trial-and-error, leaving open whether reported gains are descent (§2.5 Stage 3) or random search (§2.5 Stage 2). **Coordination failures** in multi-agent systems are documented in MAST [@cemri2025mast] — 14 distinct failure modes with $\kappa = 0.88$ agreement, dominantly role-confusion / context-loss / coordination rather than prompt quality. **Overfitting to patch** is structural: scaffolds tuned to a deployment over-fit it, and the framework predicts but does not measure how badly. **Plasticity loss at the scaffold level** is the slow-moving risk: context rot, instruction conflict, memory pollution, and tool-version drift produce a scaffold-level analogue of weight-level plasticity loss [@dohare2024loss; @lyle2023understanding]. Scaffolds age; a six-month-old `CLAUDE.md` is often worse than a clean rebuild, and no surveyed system treats pruning or expiration as a first-class operation.

Taken together: the patch-plastic surface is real, quantified by 2024–2026 work, and largely unmitigated in production. Follow-on practitioner work walks the mitigation principles in detail.

## 11. Conclusion

The field has built an external adaptation layer for LLMs, but not the optimizer that should govern it. If reliability is increasingly repaired through persistent scaffold artifacts, then production AI needs a theory and engineering discipline for the discrete, gated, auditable learning that happens there — not just for the differentiable learning inside the model. This paper is one step toward that discipline: a survey of where production sits on the *patchwork → random-search → descent* gradient of §2.5, a formalisation of the Stage-3 limit under stated assumptions, and a named missing architecture where the optimizer most plainly does not yet exist.

The field did not wait for frontier weights to become perfectly reliable. It built a second learning system around them. That second system is made of markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, and rollback buttons. It looks like engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights — and most of them are still learning by patchwork.

The mechanisms were already there. A Claude Skill has been a procedural weight since Anthropic shipped progressive disclosure. A Cursor Rule has been a local parameter since `.cursor/rules/` became a directory. A PR against `agents.md` has been a promotion gate since the Linux Foundation took stewardship. What changed in 2025–2026 is that the *combination* — these substrates wrapping a frozen frontier model and updating from deployment signal — became dense enough across vendors that the convergence reads as architecture rather than coincidence. Once you name it, the empty cells of the design space become concrete engineering targets. The most consequential one is governed cross-tenant scaffold optimization: Auto-gated Loop 1 plus governed multi-tenant cross-org Loop 2, with versioned lineage, RBAC, and rollback. In ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer. Whether it should be filled is deployment-dependent; that it has not been is the survey's headline finding.

The five surveyed absences of §6.3 — failure-triggered memory rare in production, cross-customer skill promotion absent, memory versioning unsolved, scaffold-level curriculum unspecified, Loop-2 overfitting detection missing — are each a Paper-4 target. None of these is novel as a complaint; each is novel as a *gap the architecture makes visible*. If $(r, n, d)$-patch-complete systems begin to appear in narrow production verticals — as §9.1's operational definition makes possible to test — then scaffold governance becomes load-bearing before global robustness is demonstrated.

The deepest connection — back to Paper 2 — is structural. Patch-plasticity is plastic because residual errors are clustered; if mode discovery were not slow (Postulate 1 in *Architecture of Errors*), patches would not generalise across deployments and the architecture would collapse. The survey is consistent with the postulate at the system level: deployments do generalise enough of the patch to make scaffold investment pay off. Whether this remains true at agentic, scientific, and long-horizon scales is the empirical test the next paper should design.

Practical generality therefore arrives locally first: not measured at the global model level, but as model–scaffold systems whose competence is fitted to bounded worlds and is in principle measurable through the $(r, n, d)$-patch-completeness condition of §9.1. The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation. The mechanisms were already there — markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, rollback buttons — but they read as engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights, because under deployment-time constraints that is where patch-specific adaptation can be safely placed and audited.

---

## Appendix A. Representative survey rows

The full per-system spreadsheet is `p3_master_scores.csv` in the repository. The rows below are a representative spot-check of the corpus, covering all six substrates, both research and production, and all four clusters of §7 (and the five-cluster grouping of §6.2). *Loop 1* and *Loop 2* columns apply to systems satisfying the composite-two-loop criterion; *n/a* means the loop is absent for that system. The *PP* column is the integrated patch-local-adaptation score (0–5) used in the survey; the *Evidence* column abbreviates the strongest available source tier (T1 peer-reviewed; T2 arXiv; T3 production claim; T4 open-source artifact; T5 industry blog).

```{=latex}
\begingroup\small
```

| System | Year | Substrate | Loop 1 | Loop 2 | PP | Evidence | Why included |
|------------|---:|-----------|-------|-------|---:|------------------|------------------------------------|
| NanoResearch | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2605.10813) | Tri-level Skills/Memory/Policy co-evolution; cleanest full-auto exemplar |
| AutoAgent | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2603.09716) | Dual-cycle Execution+Evolution + elastic memory orchestration |
| SkillRL | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2602.08234) | Recursive skill-augmented RL with $\text{SR}<0.4$ threshold gate |
| SkillOpt | 2026 | Integrated (S2-led) | Auto | Auto | 5 | T2 (arXiv:2605.23904) | Explicit deep-learning-optimizer analogy; 52/52 cells best or tied; +23.5 / +24.8 / +19.1 GPT-5.5 avg over direct/Codex/Claude Code; cross-model + cross-harness + cross-benchmark transfer |
| AlphaEvolve | 2025 | Integrated | Auto | Auto | 4 | T2/T3 (arXiv:2506.13131) | Production proof-point: Borg +0.7%, Gemini kernel +23%, FlashAttention +32.5% |
| DGM | 2025 | Integrated | Auto | Auto | 4 | T2 (arXiv:2505.22954) | Recursive self-modifying code; SWE-bench 20%→50% |
| ADAS | 2024 | Integrated | Auto | Auto | 4 | T2 (arXiv:2408.08435) | Meta-agent search; Turing-complete agent representation |
| SkillForge | 2026 | Integrated | Auto | Human | 4 | T2 (arXiv:2604.08618) | Production hybrid exemplar; LLM-judge >90% + VFS versioning |
| CASCADE | 2025 | Integrated | Auto | Human | 4.5 | T2 (arXiv:2512.23880) | Largest within-benchmark ablation gain: +57.9 pp on SciSkillBench |
| EvolveR | 2025 | Integrated | Auto | Auto | 3 | T2 (arXiv:2510.16079) | Experience-driven lifecycle; accepted at ICML 2026 |
| PACE | 2026 | Integrated (small-model) | Auto | Auto | 4 | T2 (arXiv:2605.23019) | Two-timescale Loop-1 + Loop-2 self-evolution under small-frozen-model production constraints |
| CORAL | 2026 | Integrated (S5+S3 async) | Auto | Auto | 4 | T2 (arXiv:2604.01658) | Only async multi-agent Loop-2 mechanism in the corpus; shared persistent memory + heartbeat-gated promotion |
| MOSS | 2026 | Integrated (S2+S5 source) | Auto | n/a | 4 | T2 (arXiv:2605.22794) | Source-level rewriting; extends evolution to code routing / hook ordering / dispatch unreachable from the text layer |
| RCL | 2026 | Integrated (formalisation) | Auto | n/a | 4 | T2 (arXiv:2604.03189) | Independent formalisation of artifact-layer descent: credit assignment + $\Omega(z)$ + overfitting + plasticity in context space |
| GEPA | 2025 | (cross-substrate prompt opt) | Auto | n/a | 3 | T2 (arXiv:2507.19457) | Reflective prompt evolution; beats GRPO +6 avg / +20 max with 35× fewer rollouts; SkillOpt's immediate predecessor |
| Voyager | 2023 | Integrated | Auto | Auto | 4 | T2 (arXiv:2305.16291) | Foundational skill-library result; 3.3× items, 15.3× tech-tree milestones |
| AGENTS.md | 2025 | S1 Instructions | n/a | n/a | 2 | T3/T4 (agents.md) | Cross-vendor standard; 60k+ repos; Lulla 2026 measures −28.6% runtime |
| Claude Code CLAUDE.md | 2025 | S1 Instructions | n/a | n/a | 4 | T3/T4 (docs.anthropic.com) | Four scoping levels including org-IT policy + auto-memory layer; ceiling for S1 |
| Cursor Rules | 2024 | S1 Instructions | n/a | n/a | 3 | T3/T4 (\url{docs.cursor.com/rules}) | `.cursor/rules/*.mdc` multi-scope + MCP attach; git-tracked |
| Anthropic Agent Skills | 2025 | S2 Skills | n/a | Human | 3 | T3 (\url{anthropic.com/engineering}) | Progressive disclosure spec; LangChain replication 29%→95% pass-rate |
| SAGE | 2025 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2512.17102) | +8.9% SGC, 26% fewer steps, 59% fewer tokens on AppWorld |
| COSPLAY | 2026 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2604.20987) | Co-evolving decision agent + learnable skill bank; long-horizon tasks |
| Ratchet | 2026 | S2 Skills (lifecycle) | n/a | n/a | 3 | T2 (arXiv:2605.22148) | Hygiene-as-precondition: $+0.0$ pp without hygiene vs. $+16.2$ pp with four hygiene mechanisms; Stage-1 prerequisite for Stage-3 descent |
| Reflexion | 2023 | S3 Memory | Auto | n/a | 4 | T1 (NeurIPS 2023; arXiv:2303.11366) | Canonical failure-triggered episodic memory; +8% HotpotQA |
| Generative Agents | 2023 | S3 Memory | Auto | n/a | 4 | T1 (UIST 2023; arXiv:2304.03442) | Reflection + importance memory primitive |
| Cuadros et al. governed collaborative memory | 2026 | S3 Memory | Auto | Auto | 5 | T2 (arXiv:2605.04264) | Only surveyed memory system with full provenance + versioning + correction |
| MCP | 2024 | S4 Tools | n/a | n/a | 5 | T3 (modelcontextprotocol.io) | Cross-vendor standard; thousands of public servers; substantial enterprise adoption |
| Harvey | 2026 | S4 Tools | n/a | n/a | 5 | T3 (harvey.ai) | 400K queries/day; 18,000+ workflows; 200+ legal data sources |
| Hippocratic AI | 2026 | S4 Tools | n/a | n/a | 5 | T3 (hippocraticai.com) | \$3.5B valuation; 30% readmission reduction; 360% care-capacity boost |
| Meta-Harness | 2026 | S5 Orchestration | Auto | n/a | 4 | T2 (arXiv:2603.28052) | End-to-end harness optimisation; filesystem-of-candidates serves as accumulated history $H_t$ for credit assignment |
| Multi-Agent Evolve (MAE) | 2025 | S5 Orchestration | Auto | n/a | 4 | T2 (arXiv:2510.23595) | RL co-evolution of Proposer/Solver/Judge population; one loop closed, no Loop-2 |
| Cemri et al. (AG2) | 2025 | S5 Orchestration | n/a | n/a | 3 | T2 (arXiv:2503.13657) | Specialisation +4.5 pp on GSM-Plus ($p = 0.03$); MAST 14 failure modes |
| Braintrust | 2024 | S6 Governance | n/a | Auto | 5 | T3 (braintrust.dev) | Prompts-as-code: immutable commits, eval-gated PR merge, sub-5 min rollback |
| Vellum | 2024 | S6 Governance | n/a | Auto | 5 | T3 (vellum.ai) | Same governance pattern; production deployment with eval thresholds |
| LangSmith Hub | 2024 | S6 Governance | n/a | Auto | 5 | T3 (\url{smith.langchain.com}) | Prompt repository with environment promotion and eval blocking |
| Self-Refine\* | 2023 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2303.17651) | Fails the patch-local discriminator: in-context iteration only |
| Mem0\* | 2024 | (contrast) | n/a | n/a | 2 | T3/T4 (mem0.ai) | Fails Loop 2: per-user memory with no cross-context promotion path |
| Tran \& Kiela\* | 2026 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2604.02460) | Single-agent baselines match or beat multi-agent under matched thinking-token budgets; orthogonal finding constraining S5 claims |

```{=latex}
\endgroup
```

*Asterisks mark contrast systems included for definitional clarity.*

---

## Appendix B. Data appendix

**Corpus size.** The supplementary file `p3_master_scores.csv` contains approximately 130 unique LLM systems scored across the six substrates. Because a system can be scored on multiple substrates, the row count in the CSV exceeds the unique-system count; the system count cited throughout §§5–8 refers to unique systems.

**Core / contrast split.** Approximately 90 unique systems satisfy the patch-plastic discriminator (score ≥ 3 on at least one substrate) and form the **core corpus**. The remaining ≈ 38 systems form the **contrast corpus** — commonly described as agentic or self-improving in public discourse but failing at least one discriminator. Headline statistics quote the core corpus; the contrast set is preserved with asterisks for definitional clarity. Appendix D enumerates the contrast set.

**Evidence-tier distribution.** Of the core corpus, approximately one quarter carry T1 (peer-reviewed) evidence, roughly half carry T2 (arXiv preprint) evidence, and the remainder carry T3 (production claim with metrics) or T4 (open-source artifact) evidence as the primary tier. T5 (industry-blog/interview) is admissible only when corroborated by a higher tier elsewhere. The per-row evidence flag in Appendix A and in the CSV makes the propagation auditable.

**Sensitivity analysis (composite two-loop count).** The strict count of thirteen research systems satisfying the composite-two-loop criterion changes under two natural relaxations of the gate definition: under (a) — counting any of versioning, lineage, or rollback as Loop-2 governance — the count rises to approximately seventeen by re-admitting MAE, MetaGen, MetaReflection, and CLIN; under (b) — admitting session signal that updates optimizer state without persisting an artifact distinct from optimiser state — the count rises to approximately fifteen by re-admitting DSPy and TextGrad. The qualitative findings (Auto×Auto well-populated, [Human × Human] and [Human × Auto] empty in the surveyed corpus, governance-first cluster in [None × Auto], cross-tenant governed-optimisation cell empty) survive both relaxations.

**Scoring discipline.** Scoring is single-rater. The published 0–5 rubric in §4 is the canonical scoring criterion; half-scores were used sparingly when one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). The CSV exposes every per-system score so reviewers can audit ambiguous classifications independently against the per-substrate evidence harvests (`p3_harvest_s1_instructions.md` through `p3_harvest_s6_governance.md`, `p3_harvest_integrated.md`).

**Survey window.** January 2023 – May 2026. Preprint-only systems carry T2 evidence and are flagged in Appendix A. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.

**Supplementary files (shipped in the arXiv source bundle under `supplementary/`).**

| File | Contents |
|---|---|
| `p3_master_scores.csv` | Per-system, per-substrate 0–5 scores with evidence citations |
| `p3_harvest_s1_instructions.md` | Evidence harvest for S1 (instructions) |
| `p3_harvest_s2_skills.md` | Evidence harvest for S2 (skills) |
| `p3_harvest_s3_memory.md` | Evidence harvest for S3 (memory) |
| `p3_harvest_s4_tools.md` | Evidence harvest for S4 (tools) |
| `p3_harvest_s5_orchestration.md` | Evidence harvest for S5 (orchestration) |
| `p3_harvest_s6_governance.md` | Evidence harvest for S6 (governance) |
| `p3_harvest_integrated.md` | Cross-substrate integrated audit |
| `p3_harvest_composite_two_loop.md` | Strict composite-two-loop audit, 22 candidates |
| `p3_harvest_failure_modes.md` | Evidence harvest for §10 failure surface |
| `p3_prior_art_check.md` | Prior-art reconciliation against adjacent literatures |

---

## Appendix C. Gate type → estimator-family mapping

The §3 formalism collapses production gates into a single per-edit gate $G_t$ that estimates the directional loss change $\widehat{\Delta}_{z_t} L_D$. In practice, surveyed gates instantiate that abstraction in several distinct ways, and some are better read as *proposal-pruning* steps that precede the per-edit gate rather than as direct $\widehat{\Delta}$ estimators. The table below maps each surveyed gate family to its role in the formalism.

| Gate family | What it estimates | Slot in §3 formalism | Representative systems |
|---|---|---|---|
| **Eval-cascade** | $\widehat{\Delta} L_D$ on a held-out task suite; cascaded through cheap-to-expensive evaluators | Per-edit gate $G_t$ | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| **RL-threshold** | Reward improvement vs. a deployment threshold (e.g., task-category accuracy < 0.4 triggers replacement) | Per-edit gate $G_t$ | SkillRL, SAGE, EvolveR |
| **LLM-judge with calibration** | Pairwise- or rubric-scored quality, calibrated against human agreement (LLM-judge ≥ 90% agreement, etc.) | Per-edit gate $G_t$ | SkillForge (Loop 1), CASCADE (consolidation gate) |
| **Surrogate verifier** | Symbolic, learned, or test-case verifier producing a pass/fail or graded score | Per-edit gate $G_t$ | DGM (test-pass on sandboxed code), Voyager (in-game verifier) |
| **Reviewer-judgment** | Human credit assignment via PR review or expert sign-off; no algorithmic threshold | Per-edit gate $G_t$ (human-instantiated) | SkillForge (Loop 2), Sierra Agent OS 2.0, Anthropic skills repo |
| **Semantic-merge** | Whether a candidate is semantically duplicated by, or compatible with, existing scaffold artifacts | *Proposal-pruning* preceding $G_t$ | NanoResearch (orchestrator semantic-merge step) |
| **MAP-Elites / archive selection** | Whether a candidate populates a previously unfilled cell in a behavior-diversity archive | *Proposal-pruning* preceding $G_t$ | AlphaEvolve (archive), ADAS (meta-agent search) |
| **Multi-sample agreement** | Whether $k$ independent proposals or evaluations converge on the same direction; false-accept rate decays as $p^k$ rather than variance shrinking as $1/k$ | *Aggregation filter* (qualitatively distinct from mini-batch averaging) | Under-explored in the surveyed corpus |

The eval-cascade, RL-threshold, LLM-judge, surrogate-verifier, and reviewer-judgment families directly populate the per-edit gate $G_t$ of §3 and inherit its descent guarantees (under Assumptions A1–A5 of Appendix E). The semantic-merge and archive-selection families are not estimators of $\widehat{\Delta} L_D$ — they constrain the proposal distribution $Q_t$ rather than judging individual candidate quality, and the descent argument therefore applies to the composition (proposal-pruning ∘ per-edit gate) rather than to either step alone. Multi-sample agreement filters are not surveyed in production form; they are listed for completeness because they are the correct ML analogue for "wait for $k$ pieces of evidence before accepting an edit," which is *not* the same operation as mini-batch averaging and should not be conflated with it in scaffold-descent analyses.

---

## Appendix D. Contrast set

The contrast corpus of approximately 38 systems is included to make the patch-plastic discriminator audit-able. Each system here is commonly described in public discourse as agentic, self-improving, or scaffolded, but fails at least one discriminator. Representative entries:

| System | Year | Primary discriminator failure | Brief reason |
|---|---|---|---|
| Self-Refine [@madaan2023selfrefine] | 2023 | No persistent artifact | In-context iteration only; no scaffold delta survives the session |
| ReAct [@yao2023react] | 2023 | No persistent artifact | Thought-act-observe loop is intra-session; no Loop 1 persistence |
| Reflexion [@shinn2023reflexion] | 2023 | No Loop 2 (Loop 1 only) | Failure-triggered episodic memory persists per-agent but no cross-context promotion mechanism |
| Generative Agents [@park2023generative] | 2023 | No Loop 2 | Reflection + importance memory primitive; per-agent scope |
| AutoManual [@chen2024automanual] | 2024 | Passes (in core corpus) | Listed here only to flag boundary case; see Appendix A |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks, not in-deployment failures |
| Mem0 (vanilla deployment) | 2024 | No Loop 2 | Per-user memory store with no cross-context promotion path |
| Zep | 2024 | No Loop 2 | Temporal knowledge graph per agent/session, no promotion gate |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence; no inter-tenant promotion |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence; no inter-tenant promotion |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent; no promotion mechanism |
| DSPy | 2023 | No artifact distinct from optimiser state | Prompt-template optimization but optimised templates are optimiser state, not persisted scaffold; SkillOpt [@yang2026skillopt; §3.5; Appendix G] realises the artifact-bearing form |
| TextGrad | 2024 | No artifact distinct from optimiser state | Same boundary case as DSPy; SkillOpt [@yang2026skillopt; §3.5; Appendix G] adds the persistent `best_skill.md`, held-out validation gate, rejected-edit memory, and textual learning-rate schedule that TextGrad lacks |
| MetaGen | 2026 | No Loop 2; no cross-session persistence | Role pool dynamic within single inference call |
| MAE (Multi-Agent Evolve) | 2025 | No Loop 2 | Co-evolution within Proposer/Solver/Judge triplet; no external promotion |
| MetaReflection | 2024 | No Loop 2 | Per-agent semantic memory; no cross-agent promotion |
| CLIN | 2023 | No cross-instance promotion | Causal abstractions per-agent-per-environment |
| LangGraph | 2024 | Framework only | Orchestration framework; not a deployed patch-plastic system |
| AutoGen | 2023 | Framework only | Multi-agent framework; not a deployed patch-plastic system |
| CrewAI | 2024 | Framework only | Multi-agent framework; not a deployed patch-plastic system |
| Tran & Kiela | 2026 | Single-agent baseline | Listed because the result constrains S5 maturity claims (see §7) |
| W&B Weave | 2024 | No Loop 1 | Observability/eval-as-code; engineer-authored artifacts |
| Agenta | 2024 | No Loop 1 | Prompt-as-code platform; engineer-authored artifacts |
| LangFuse | 2024 | No Loop 1 | Observability/tracing; engineer-authored artifacts |
| Mobile-Agent-E | 2025 | Loop 2 absent | Self-evolving mobile assistant; no cross-tenant promotion |
| Cradle | 2024 | Loop 2 absent | Foundation agent for general computer control; per-session only |
| OS-Copilot | 2024 | Loop 2 absent | Computer-use generalist; per-deployment |
| Agent S, Agent S2 | 2024–2025 | Loop 2 absent | Computer-use agentic framework; no cross-context promotion |
| ACE [@ace2025agentic] | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook; per-deployment |
| Claude Code memory (vanilla CLAUDE.md) | 2025 | No Loop 2 (within-project only) | Lives in [None × None] without the cross-org governance layer |
| Cursor Rules (vanilla) | 2024 | No Loop 2 | Per-project artifacts; no cross-org promotion mechanism |
| GitHub Copilot custom instructions | 2024 | No Loop 1 | Engineer-authored at repo base branch |
| Windsurf rules | 2024 | No Loop 1 | Engineer-authored, no failure-triggered update |
| Continue.dev rules | 2024 | No Loop 1 | Same as above |
| Zed AI rules | 2024 | No Loop 1 | Same as above |
| Replit `replit.md` | 2025 | Loop 2 absent | Self-writing scaffold but per-workspace only |
| Aider conventions | 2024 | No Loop 1 | Engineer-authored convention file |
| Lovable knowledge | 2024 | No Loop 1 | Engineer-authored knowledge field |

The full per-system exclusion log lives in `supplementary/p3_master_scores.csv` (with one row per substrate scoring) and in the per-substrate evidence harvests. The list above is representative, not exhaustive; some contrast entries are excluded from the table for length and appear only in the CSV.

---

## Appendix E. Formalization of artifact-layer descent

This appendix supplies the verification machinery for §3. The body states the descent picture as a mechanism; this appendix derives the one-step descent inequality, states the convergence proposition with its assumptions, gives the full optimisation-analogy correspondence, walks four concrete cases, and clarifies what credit assignment without chain rule means.

### E.1 The mechanism stack

The abstract update rule of §3 expands into six operations that every patch-local system must perform, whether explicitly engineered or accidentally emergent.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, eval regressions, tool-call failures. The Loop-1 signal source. Without it, $z_t$ has no provenance.
2. **Mode discovery.** Cluster repeated failures into patch-specific error modes: the *Architecture of Errors* catalogue, instantiated locally per patch.
3. **Delta synthesis.** Convert a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, an eval case. This produces $z_t$.
4. **Delta validation.** Estimate whether the edit reduces $L_D$ without collateral damage on adjacent inputs. The gate $G_t$ is Auto-gated when the check is an algorithmic criterion, Human-gated when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted edit stays in the local fork or climbs the scope hierarchy: project, stack, organisation, cross-tenant. Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, detect over-fitting. Without this, accumulated edits produce the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline. Surveyed systems implement them partially and unevenly: research full-auto systems excel at (3) and (4); production governance leaders at (5); industry hybrids at most of (1)–(5) but rarely (6). Implementation patterns are deferred to follow-on practitioner work.

### E.2 Setup and notation

Let the frontier model have fixed parameters $\theta_M$. Let the scaffold be a structured parameter object
$$\theta_s \in \Theta_s = \Theta_1 \times \Theta_2 \times \Theta_3 \times \Theta_4 \times \Theta_5 \times \Theta_6,$$
where the six coordinates correspond to the six substrates of §4. The space $\Theta_s$ is discrete, symbolic, and versioned. For a deployment patch $D$, define patch loss as
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right].$$

A candidate edit $z_t \in \mathcal{A}(\theta_s^t)$ is drawn from a proposal process $z_t \sim Q_t(z \mid H_t, \theta_s^t)$, where $H_t$ is the accumulated history of failures, corrections, rejected outputs, eval regressions, reviewer comments, tool-call traces, and prior accepted deltas, and conditioning on $\theta_s^t$ ensures admissibility at the current scaffold. The finite directional difference induced by the edit is
$$\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s).$$
A useful edit is one with $\Delta_z L_D < 0$. The gate's noisy estimate of this quantity is $\widehat{\Delta}_z L_D$.

### E.3 Descent inequality

The gate operates on the *estimator*, not the truth. The descent argument distinguishes them.

**Assumption A1 (positive descent bias on accepted edits).** There exists $\gamma_t > 0$ such that
$$\mathbb{E}\!\left[\widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t\right] \leq -\gamma_t - \tau_t.$$
The gate's accept-threshold $\tau_t$ ensures accepted edits clear the margin under the estimator.

**Assumption A2 (bounded estimator bias on accepted edits).** There exists $\varepsilon_t \geq 0$ such that
$$\big|\mathbb{E}\!\left[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t\right]\big| \leq \varepsilon_t.$$

Combining A1 and A2 with the gated update rule of §3 and writing $p_t = \Pr(G_t = 1 \mid \theta_s^t)$,
$$\mathbb{E}\!\left[L_D(\theta_s^{t+1}) \mid \theta_s^t\right] \leq L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t \varepsilon_t.$$
This is descent under a noisy estimator: per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability.

### E.4 Convergence proposition

**Proposition (convergence of loss, informal).** Assume A1, A2, bounded loss $0 \leq L_D \leq B$, and additionally:

- **A3 (proposal coverage).** At every non-$G$-stable scaffold there exists $\delta > 0$ such that $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \leq -\delta$.
- **A4 (effective compactness).** The reachable scaffold orbit takes values in a finite or precompact subset of $\Theta_s$.
- **A5 (persistent acceptance with summable bias).** $\sum_t p_t (\gamma_t + \tau_t) = \infty$ and $\sum_t p_t \varepsilon_t < \infty$.

Then $L_D(\theta_s^t)$ is a non-negative supermartingale up to summable noise; $L_D(\theta_s^t) \to L_\infty$ almost surely for some random $L_\infty \geq 0$; and the limit set of $\{\theta_s^t\}$ is **$G$-stable**: no admissible edit clears the gate with negative expected directional loss in the limit.

The proposition claims convergence of the *loss* and stability of the *gate decision*, not convergence to a global or local optimum of $L_D$. A globally suboptimal $G$-stable scaffold is consistent with the result: $Q_t$ may never propose the improving edit, or $\widehat{\Delta}$ may be biased to reject an improving direction. This is the ordinary target of local stochastic optimization under noisy estimators rather than a guarantee of optimality.

### E.5 Optimisation-analogy correspondence

| Optimization concept | Scaffold analogue |
|---|---|
| Parameter vector | Instructions, skills, memories, tools, routing graphs, eval gates, governance rules |
| Forward pass | Model–scaffold composite executing on patch input |
| Loss | Failure, user correction, eval regression, retrieval miss, tool error, schema violation |
| Finite directional difference | $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$ |
| Gradient estimate | Credit assignment identifying the scaffold coordinate responsible for the failure |
| SGD step | Accepted scaffold edit |
| Aggregated update | Multiple recurring failures aggregated before update (either by sampling, *mini-batch averaging*, or by sign-of-direction agreement across $k$ proposals, *multi-sample voting*) |
| Learning rate | Edit magnitude under $\oplus$ |
| Update radius | Promotion scope: which loss is being descended on (USER, PROJECT, STACK, TENANT, CORE) |
| Validation loss | Held-out patch eval before merge |
| Regularization | Complexity penalty $\Omega(z)$, bloat control, cross-patch regression checks |
| Overfitting | Scaffold improves on this patch and degrades elsewhere |
| Rollback | Reverting a harmful accepted update |

### E.6 Credit assignment without chain rule

Scaffold systems do not compute chain-rule derivatives through markdown files or tool registries, and the correspondence above deliberately omits a "backpropagation" row. They do, however, perform *credit assignment* through a pipeline. If the final answer fails, the responsible coordinate may be a retrieval configuration three layers upstream, a missing tool schema constraint, an underspecified instruction, a stale memory, or a bad orchestration edge. Engineers do this manually; LLM-judges and surrogate verifiers do it semi-automatically. The operation is *attribution* (output error is assigned to an upstream coordinate) rather than backpropagation. The descent argument of §3 needs only that this attribution succeeds with non-zero probability per failure (assumption (iv) of the scope box), not that it is performed by chain rule.

### E.7 Worked cases

**RAG.** Suppose failures recur because retrieved context omits the decisive clause. The observed loss is not "the model hallucinated." Credit assignment traces the error to the retrieval coordinate: chunking, query rewrite, metadata filter, embedding model, reranker, citation policy, or context-packing rule. The candidate edit might tighten chunk boundaries, add a metadata constraint, change the reranker, or insert a regression eval containing the missed clause. The gate tests whether retrieval recall and answer accuracy improve on the patch eval without degrading adjacent cases. If accepted, the scaffold has moved downhill on the local loss surface.

**Pitch review.** Suppose the system repeatedly overrates decks claiming a "huge market" without numeric evidence. The failure cluster identifies an under-specified rubric coordinate. The candidate edit changes "evaluate TAM size" into "require a numeric market estimate and source; if absent, cap TAM score at 4/10." The gate runs the revised rubric against held-out decks with human scores. If agreement improves without damaging unrelated criteria, the edit is committed.

**Tool-using agent.** Suppose calls repeatedly fail because optional parameters are underspecified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The candidate edit adds required fields, constrained decoding, or a pre-call uncertainty check. The gate estimates whether tool-call failure decreases without increasing refusal, latency, or unnecessary clarification.

**Memory.** Suppose a stale customer preference is repeatedly retrieved and causes bad decisions. The failure is not a weight error. The responsible coordinate is a memory entry plus its provenance, priority, and expiry policy. The candidate edit corrects, expires, or version-tags the memory. The gate checks whether the correction improves future behavior without erasing useful history.

### E.8 Loop 1 and Loop 2 as descent steps of different radius

Loop 1 proposes and validates local descent steps on a single $L_D$. Loop 2 expands the update radius. It selects, merges, and promotes accepted local edits so that they apply to a larger averaging set of patch losses. USER-level acceptance descends on a single $L_D$. PROJECT promotion descends on a project-averaged loss. STACK promotion widens the average further. CORE or cross-tenant promotion descends on a federated average. The two-loop design space is therefore not just a taxonomy of engineering patterns: it is a taxonomy of *which loss each surveyed system is descending on*, gated by which estimator.

### E.9 Overfitting in scaffold adaptation

In weight training, overfitting is usually a defect. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve cross-patch generality; they must smooth over local conventions and rare workflow-specific failures. A deployment patch needs the opposite: selective specialization to local residuals. The scaffold is therefore an intentionally overfittable layer, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold that improves one repository, hospital workflow, or legal diligence process may degrade performance elsewhere. That is not a contradiction; it is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

In non-stationary patches ($D = D_t$), the same descent mechanism tracks a moving optimum rather than converging once. This is why recency weighting, replay, pruning, expiry, and rollback are not optional hygiene; they are the scaffold-level analogues of continual-learning machinery.

---

## Appendix F. Survey detail

This appendix carries the cell-by-cell discussion of the two-loop matrix from §8, the closest-approaches enumeration that supports §9, and the deployment-dependence argument. It supplies the verification material for §§8–9.

### F.1 Two-loop matrix: cell-by-cell discussion

**[Auto × Auto]** is most populated (twelve systems). Every member has a machine-evaluated decision criterion on both loops. Velocity is the cluster's defining property; the lack of cross-organisational governance is its uniform weakness.

**[Auto × Human]** is the production-viable cell: Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. The pattern reconciles automation velocity with reviewer accountability. SkillForge's LLM-judge + reviewer pipeline is the architectural exemplar. CASCADE, Sierra, and Devin instantiate variants; the industry exemplars (Sierra, Devin) are marked with † because vendor documentation rather than peer-reviewed metrics is the primary evidence.

**[None × Auto-gated]** holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 (eval-gated CI blocks promotion on regression), but no Loop 1 in the patch-local sense, because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated.

**[Human × Auto]** is empty by engineering logic: if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping); no published example exists.

**[Human × Human]** is empty in the surveyed corpus. A candidate occupant would be a reviewer-authored-and-reviewer-promoted artifact pipeline targeting solo and small-team workflows where automation cost exceeds review latency. No public example was found during the May 2026 survey window.

**[Human × None]** is structurally improbable: a system requiring human authorship on Loop 1 but with no Loop 2 collapses to "engineer-edits-a-config" and is not patch-local in the sense of §3.

**DGM dual-mode note.** DGM operates in both [Auto × Auto] (primary archive-based evolution) and [Auto × Human] (sandboxed code-modification review) modes depending on deployment configuration; we list it once in the dominant cell.

### F.2 Closest approaches to governed cross-tenant scaffold optimization

The four properties of governed cross-tenant scaffold optimization are (a) auto-gated Loop 1, (b) multi-tenant cross-org promotion, (c) versioned lineage with RBAC, (d) rollback. Closest approaches partition the requirements:

- **AlphaEvolve** has (a) and partial (b) within a single organisation; no cross-org promotion mechanism.
- **NanoResearch** has (a) at the research level; no enterprise governance layer described.
- **SkillOpt** has (a) fully and partial (c) via the exported `best_skill.md` artifact plus protected slow-update field; reports positive cross-model, cross-harness, and cross-benchmark transfer as empirical evidence-radius measurement; does not implement (b) cross-organisational promotion or (d) explicit rollback. The Appendix G walkthrough maps every SkillOpt design decision to its §3 counterpart.
- **CORAL** [@qu2026coral] has partial (a) via heartbeat-gated promotion and is the only system in the corpus that implements asynchronous multi-agent Loop 2 within one organisation through shared persistent memory; no (b) cross-organisational scope, no formal (c) RBAC, no (d) rollback.
- **PACE** [@ling2026pace] has (a) at the small-model production timescale and a fast/slow two-timescale Loop 1 + Loop 2 that consolidates across one deployment's own episodes rather than across deployments; no (b), no formal (c) or (d). PACE is the closest demonstration that the two-loop architecture is implementable under small-frozen-model constraints.
- **Meta-Harness** [@lee2026metaharness] has (a) over the harness substrate (S5) with a filesystem-of-candidates credit-assignment record that functions as the accumulated history $H_t$ of §3; no Loop-2 cross-organisational promotion, no RBAC, no rollback.
- **SkillForge** has (a) and (b) within one enterprise, partial (c) via VFS commits; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has (b) and partial (a); the GitHub-style Workspaces provide some lineage but not RBAC-with-rollback in the strict sense.
- **Vellum / Braintrust / LangSmith Hub** have (c) and (d) explicitly but no (a) or (b) in the strict sense; these are governance-first systems by construction.

No surveyed system combines (b), (c), and (d) under any gate type. The cross-organisational governance triad is itself unfilled, independently of whether Loop 1 is auto-gated.

### F.3 Deployment-dependence of the missing architecture

Whether the corner *should* be filled is deployment-dependent. In safety-critical domains (medical decision support, legal advice, financial advice), reviewer-judgment gates may be a design feature rather than a defect, and the human latency is the point. The narrower survey claim is what matters: no public system currently combines automated local scaffold evolution with governed cross-organisation promotion, versioned lineage with RBAC, and rollback. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. The shortest demonstrable path appears to build on AlphaEvolve's cascade evaluator and MAP-Elites archive, extending federation from within-DeepMind multi-target to cross-customer multi-tenant. The architectural surface, not the timeline, is what this paper claims.

---

## Appendix G. SkillOpt walkthrough and the convergent cluster

This appendix expands §3.5 along two axes. The first six subsections (G.1–G.3 on SkillOpt; G.4–G.8 on the convergent cluster) walk each system mechanism-by-mechanism, stating its §3 mapping explicitly and naming what it leaves open. The next subsection (G.9) synthesises four claims supported by the cluster as a whole. The final two subsections (G.10–G.11) carry the §9-property audit of SkillOpt and the published cost-per-point figure.

### G.1 The convergent landscape

SkillOpt [@yang2026skillopt] is the cleanest current instance of artifact-layer descent in our survey, but it is one of at least fourteen independent research threads in 2025–2026 that converge on the same disciplined gradient-like update mechanism for the scaffold layer. The cluster is striking because the convergence happens *from different starting points*: GEPA and Tiwari et al. start from prompt-optimisation and continual-learning respectively; RCL starts from cognitive-agent learning; Meta-Harness, AHE, MOSS, CANTANTE, and Ong et al. start from harness engineering; MOCHA and Ratchet start from skill-deployment constraints; ICT, Combee, CORAL, and PACE start from cross-task / multi-agent / production-deployment angles. Each system instantiates a different subset of §3's five conditions, and each exposes a different gap.

The table below indexes the cluster by §3 mechanism and by what each system leaves open. Subsequent subsections walk each cluster in detail.

| Cluster | Representative systems | What it instantiates in §3 | Substrate (§4) | What it leaves open |
|---|---|---|---|---|
| Reflective-evolution | GEPA [@agrawal2025gepa]; @tiwari2026fastandslow | $Q_t$ over trajectory evidence with Pareto-frontier proposal-pruning; two-timescale in-context / in-weights motivation | (cross-substrate prompt opt) | persistent $\theta_s$; $L_t$ budget; held-out $G_t$; rejected-edit buffer |
| Reflective context | RCL [@vassilyev2026rcl] | $\theta_s$ over context space; generalisation penalty = $\Omega(z)$; explicit naming of credit-assignment / overfitting / plasticity-loss in context space | S1+S2 (context) | cross-deployment Loop 2 |
| Harness optimisation | Meta-Harness [@lee2026metaharness]; AHE [@lin2026ahe]; MOSS [@cai2026moss]; CANTANTE [@zehle2026cantante]; @ong2026harnesseval | credit assignment (§3 op 3); filesystem-of-candidates as $H_t$; contrastive multi-agent attribution; source-level extension beyond text-mutable | S5 (orchestration); S2+S5 (MOSS) | governed Loop 2 across orgs; RBAC; rollback |
| Multi-objective + lifecycle | MOCHA [@tanjim2026mocha]; Ratchet [@zhang2026ratchet] | Pareto frontier as the true shape of $\Omega(z)$; hygiene as precondition for residual capture and mode discovery | S2 + deployment constraints | gradient-analogue closure; gate strictness |
| Cross-task transfer | ICT [@shalev2026ict]; Combee [@li2026combee]; CORAL [@qu2026coral]; PACE [@ling2026pace] | empirical evidence-radius (Loop-2 scope) measurement; async multi-agent Loop 2 within one org; two-timescale Loop 1 + Loop 2 under small-model constraints | Integrated; S3+S5 | cross-organisational gate, lineage, rollback |
| Worked instance | SkillOpt [@yang2026skillopt] | all five §3 conditions: $\theta_s$, $L_D$, $Q_t$/$z_t$, $L_t$, $G_t$ + rejected-edit buffer + slow/meta update | S2-led Integrated | cross-org Loop 2; RBAC; rollback |

Read against §9, no member of the cluster combines (a) auto-gated Loop 1 with (b) cross-organisational Loop 2, (c) versioned lineage with RBAC, and (d) rollback. The §3 picture is realised in fragments across the cluster; the §9 gap is confirmed by every member.

### G.2 SkillOpt: full correspondence

The table below extends the §3.5 compact correspondence with the §3 role of each component and an algorithm-level pointer into SkillOpt's published procedure (their Algorithm 1).

| §3 quantity | SkillOpt instantiation | §3 role explained | Algorithm pointer |
|---|---|---|---|
| $\theta_s$ (scaffold) | `best_skill.md` — a 379–1,995-token markdown document | the trainable external state of the frozen target model; persistent and exported as the deployment artifact | $s_{\text{best}}$ (Algorithm 1, lines 1, 22, 37) |
| $L_D$ (patch loss) | benchmark-native hard score / exact-match on a held-out test split | scalar quality signal that the optimiser is implicitly minimising | $\textsc{Evaluate}(M, h, s, D)$ (lines 2, 17, 37) |
| $Q_t$ (proposal) | optimizer-model reflection over failure and success minibatches; failures and successes analysed separately, then merged with priority on failure fixes | proposal distribution conditioned on accumulated rollout evidence and current scaffold | optimizer calls $O$ for failure analysis, success analysis, and merge (lines 9–11) |
| $z_t$ (edit) | structured add/delete/replace patch on the skill (or rewrite-from-suggestions in rewrite mode) | the candidate update applied via $\oplus$ to the current scaffold | rank/clip to $L_t$ edits, apply to obtain $\tilde s$ (lines 12–13) |
| $L_t$ (textual learning rate) | bounded per-step edit budget; constant / linear / cosine / autonomous schedules; default cosine with floor $L_t=2$ | edit-magnitude controller; the §3 *learning rate* in textual form | rank/clip step (line 12); schedule applied per epoch |
| $G_t$ (gate) | held-out selection-split accept gate, strictly greater than current selection score | the per-edit gate $G_t$ — accepts only when $\widehat{\Delta}_{z_t} L_D$ improves the selection score | comparison at line 20; cache lookup at lines 14–18 |
| rejected-edit buffer | epoch-local store of failed proposals and the score drop they caused | converts rejected steps into negative feedback for later proposals within the same epoch; zero deployment cost | $\mathcal B$ updated at line 26; reset at line 5 |
| slow/meta update | epoch-end longitudinal guidance written to a markup-fenced protected slow-update field, still passed through $D_{\text{sel}}$ | second-order consolidation across adjacent epochs; the §3 "step-level edits cannot overwrite the protected slow-update field" decomposition | lines 28–31; gate applied to injected guidance |
| optimizer-side meta skill | $m_{\text{meta}}$ — a prompt-side summary of which edits helped, which failed, and which failures persisted | training-time guidance for $Q_t$; never shipped with the deployed artifact | lines 33–34 (training-side only) |

The mapping is exact rather than analogical: every §3 quantity has a named, code-level counterpart in SkillOpt's Algorithm 1, and every SkillOpt control surface maps onto a §3 quantity. SkillOpt is therefore the cleanest published instance we are aware of of the §3 picture as *mechanism* rather than *metaphor* — the five conditions of §3 (measurable patch loss, residual capture, credit assignment, candidate delta synthesis, directional-loss-change gate) are all instantiated.

### G.3 What SkillOpt does that prior textual-optimisation systems do not

SkillOpt's own experiment design compares it against six baselines under an identical protocol (same target model, same held-out test split, same scorer). The differentiation below frames each baseline in §3 vocabulary and identifies the §3 mechanism the baseline lacks. The through-line is the thesis that the scaffold/evolution layer needs a disciplined gradient-like update mechanism, and the live distinction across baselines is which §3 conditions each one fails.

- **TextGrad** [@yuksekgonul2024textgrad]**.** Backpropagates textual feedback through `tg.Variable` objects in a compound system. In §3 terms: $z_t$-style edits exist, but $\theta_s$ does not — TextGrad has no artifact distinct from optimiser state. There is no $L_t$ schedule, no held-out $G_t$, and no rejected-edit buffer. SkillOpt's measured advantage over TextGrad on direct chat ranges from $+5.9$ to $+34.0$ points across benchmarks at GPT–5.5 scale and is uniformly positive at all seven target-model scales. This matches our Appendix D classification of TextGrad as failing the patch-local discriminator on persistence; SkillOpt closes precisely that gap.

- **GEPA** [@agrawal2025gepa]**.** Reflective prompt evolution with Pareto-style multi-candidate selection. Closer than TextGrad in that it carries multiple candidates and a selection step. In §3 terms: $Q_t$ is real, but the optimisation target is a prompt rather than a persistent skill artifact, $G_t$ is not the strictly-greater held-out gate of §3, and there is no $L_t$ bound — accepted edits can wholesale rewrite. SkillOpt outperforms GEPA in the reported comparison; the per-cell deltas should be read directly from SkillOpt's results table rather than summarised here.

- **Trace2Skill** [@ni2026trace2skill]**.** Distils trajectory-local lessons into reusable skill artifacts. In §3 terms: $\theta_s$ exists, but there is no iterative $G_t$ — Trace2Skill mines skills offline rather than running a held-out validation loop that accepts or rejects each candidate. Our §3 mechanism stack therefore loses *delta validation* (operation 4) and the *rejected-edit buffer*. SkillOpt's measured gap over Trace2Skill is $+5.0$ to $+19.0$ points across benchmarks at GPT–5.5 direct chat.

- **EvoSkill** [@alzubi2026evoskill]**.** Skill-folder evolution under failure analysis, deployed harness-side. The strongest baseline on the Codex and Claude Code harness rows. In §3 terms: $\theta_s$ is a folder rather than a single artifact, and credit assignment via failure analysis is genuine, but there is no $L_t$ bound on per-step folder edits and no rejected-edit buffer. SkillOpt beats EvoSkill by $+14.0$ inside Codex and $+3.2$ inside Claude Code on the GPT–5.5 five-benchmark average.

- **Human skill** (expert-written, 145–516 tokens per benchmark). In §3 terms: $\theta_s$ exists, but Loop 1 does not — the artifact is static at deployment. Provides the no-Loop-1 ceiling.

- **One-shot LLM skill** (generated zero-shot from a benchmark description by GPT–5.5, never updated). In §3 terms: $\theta_s$ exists; Loop 1 does not; $Q_t$ fires exactly once with no rollout evidence. The "untrained scaffold" baseline.

ABSTRAL [@song2026abstral] and EvoTest [@he2025evotest], referenced in SkillOpt's related work but not measured in their table, operate at the multi-agent design / test-time configuration layer rather than the persistent skill layer; they are out of scope for the artifact-layer-descent comparison.

Synthesising across all six measured baselines: the live difference is whether the loop has (i) a persistent edit-target distinct from optimiser state ($\theta_s$), (ii) a held-out validation gate on each accept ($G_t$ with $\widehat\Delta$ estimator and accept threshold $\tau_t$), (iii) negative-feedback retention (rejected-edit buffer feeding $Q_t$), and (iv) a bounded learning rate with a schedule ($L_t$ + cosine/linear/constant/autonomous). SkillOpt is the first published system in our survey that instantiates all four simultaneously, and it does so as a single offline training loop whose deployed artifact remains a 300–2,000-token markdown file requiring no inference-time optimiser calls.

### G.4 GEPA, Tiwari, and the reflective-evolution family

The immediate predecessor to SkillOpt's optimiser framing is **GEPA** [@agrawal2025gepa]. It shows that natural-language reflection over execution trajectories can provide a richer adaptation signal than sparse scalar rewards for prompt evolution in compound AI systems. GEPA samples trajectories containing reasoning steps, tool calls, and tool outputs; reflects on them to diagnose failures and propose prompt updates; and maintains a Pareto frontier of candidate prompts rather than greedily mutating only the current best. Across six tasks, GEPA outperforms GRPO by 6% on average and by up to 20% while using up to 35× fewer rollouts, and also outperforms MIPROv2 in the reported aggregate comparison. In §3 vocabulary, GEPA strongly instantiates the proposal side, $Q_t$, through trajectory-conditioned reflection, and uses Pareto-based candidate selection as a proposal/pruning mechanism. What it does not instantiate is the full SkillOpt-style artifact lifecycle: a bounded edit budget on a reusable skill document, a strictly-greater held-out gate on each accepted skill update, a rejected-edit buffer used as negative feedback, and an exported deployment artifact with governance hooks.

**@tiwari2026fastandslow** supply the broader theoretical framing from the optimisation side, arguing explicitly that restricting learning to *either* in-context (prompt optimisation) *or* in-weights (RL / fine-tuning) is unnecessary and costly. In-context adaptation is cheap and rapid but capacity-bounded; in-weights adaptation is expressive but induces catastrophic forgetting and loss of plasticity [@dohare2024loss]. The scaffold layer of §2 is precisely the substrate that absorbs what in-context adaptation can carry cheaply, leaving the weights free to generalise. Tiwari et al. supply the two-timescale motivation from the optimisation side; §2 supplies the matching motivation from the production-reliability side. The two framings are independent and mutually reinforcing.

### G.5 Reflective Context Learning: a parallel formalisation

The most direct independent convergence on the §3 formalisation comes from **Reflective Context Learning** [RCL; @vassilyev2026rcl]. Their opening observation is that "the fundamental problems of learning, including credit assignment, overfitting, forgetting, local optima, and high-variance learning signals, persist whether the learned object lies in parameter space or context space," and that current methods are "fragmented and ad hoc" precisely because they address these challenges one at a time rather than as a unified optimisation problem over the context. The parallel to §3's argument — that scaffold maintenance needs the discipline of weight-space optimisation applied to an external artifact layer — is exact and arrived at independently.

RCL maps onto §3 as follows. The *learned context* is $\theta_s$. The *reflection signal* is a form of credit assignment identifying which context coordinate caused a failure (§3 operation 3). The *generalisation penalty* that RCL introduces to prevent narrow sample-specific rules is structurally the complexity penalty $\Omega(z)$ of the gate condition. Where RCL and §3 differ is in Loop-2 scope: RCL is framed around single-agent cross-task generalisation, while §3's Loop 2 is cross-deployment, cross-tenant, and cross-organisational promotion. The convergence is nonetheless significant: two research threads starting from different motivations (production reliability in §3, cognitive agent learning in RCL) arrive at the same formal observation that the classical learning problems do not disappear when the learned object moves outside the weights.

### G.6 The harness-optimisation cluster

A second convergent cluster focuses on the *harness* — the code and configuration layer that wraps a frozen model — rather than on skill documents specifically. This cluster independently identifies credit assignment as the central unsolved problem of scaffold evolution, and its engineering solutions directly instantiate §3's operation 3 (mode discovery) and operation 4 (delta validation).

**Meta-Harness** [@lee2026metaharness] is the cleanest representative. Its opening claim — that "the performance of large language model systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model" — is §1's scaffold-versus-weights decomposition restated for the harness substrate specifically. Meta-Harness then identifies that existing text optimisers "compress feedback too aggressively," losing the fine-grained signal needed for credit assignment. Its solution is an outer-loop proposer with access to source code, scores, and execution traces of all prior candidates through a filesystem, so that the edit history itself becomes the credit-assignment signal. In §3 terms, the filesystem of prior candidates is a concrete form of the accumulated history $H_t$ that conditions the proposal distribution $Q_t$, and the outer loop is a Loop-1 closure over the harness substrate (§4, S5) rather than the skill substrate (S2).

**Agentic Harness Engineering** [AHE; @lin2026ahe] attacks the same problem from the observability side. The core diagnosis is that harness engineering "faces a heterogeneous action space across editable components, voluminous trajectories that bury actionable signal, and edits whose effect is hard to attribute." These three failure modes map precisely onto §3's mechanism stack: a heterogeneous action space is the coordinate-identification problem (op 2, mode discovery); voluminous trajectories that bury signal is the residual-capture problem (op 1); and effects that are hard to attribute is operation 3, credit assignment. AHE's response — three matched observability pillars giving every editable harness component a file-level representation — is an engineering instantiation of the coordinate decomposition that §3 assumes. The implicit claim is that artifact-layer descent requires not just the optimisation loop but also the instrumentation that makes scaffold coordinates individually observable and attributable.

**MOSS** [@cai2026moss] extends the harness argument by observing that all prior self-evolving agent systems "confine evolution to text-mutable artifacts — skill files, prompt configurations, memory schemas, workflow graphs — and leave the agent harness untouched." Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is, in MOSS's phrase, "physically unreachable from the text layer." MOSS therefore extends Loop-1 evolution to source-level code rewriting. In §4 terms, MOSS evolves S2 (Skills) and S5 (Orchestration) simultaneously, rather than treating the orchestration substrate as a fixed wrapper around an evolvable skill layer. This matters for §9: a governed cross-tenant scaffold optimiser that covers only text-mutable artifacts leaves the code substrate ungoverned, and MOSS's diagnosis suggests the gap is not merely inconvenient but structurally incomplete.

**CANTANTE** [@zehle2026cantante] attacks credit assignment directly in the multi-agent setting. Its observation is that "scores are available only at the system level, whereas the parameters governing agent behavior are local," making optimisation of multi-agent scaffolds "fundamentally a credit-assignment problem." CANTANTE's solution is contrastive: it decomposes system-level rewards into per-agent update signals by contrasting rollouts of multiple jointly acting configurations. In §3 vocabulary, CANTANTE provides a concrete mechanism for operation 3 in the case where the scaffold is distributed across agents rather than concentrated in a single artifact. The gap it closes is the same one §3 identifies in Appendix E.6 — that attribution (output error assigned to an upstream scaffold coordinate) must succeed with non-zero probability per failure — but instantiated for the multi-agent topology substrate (S5).

**Harness optimizer evaluation** [@ong2026harnesseval] provides independent empirical evidence for a failure mode this paper flags in §10: that evaluating scaffold optimisers "solely by observing target agents' performance gains" misses intermediate erroneous edits that hinder performance. Their finding — that it is "unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error" — is a direct empirical instantiation of the distinction between Stage 2 (random artifact search) and Stage 3 (artifact-layer descent) from §2.5's table. The credit-assignment problem is not merely theoretical: production harness optimisers that cannot distinguish informed updates from lucky trial-and-error are operating in Stage 2 even when they report benchmark improvements.

### G.7 Multi-objective and lifecycle constraints

Two papers expose constraints on the §3 picture that single-loss descent does not capture, both relevant to the §9 missing-architecture discussion.

**MOCHA** [@tanjim2026mocha] observes that agent skills are "multi-field artifacts subject to hard platform constraints: description fields are truncated for routing, instruction bodies are compacted via progressive disclosure, and co-resident skills compete for limited context windows." Skill optimisation is therefore not a single-loss descent problem but an inherently multi-objective one: a skill must simultaneously maximise task performance and satisfy platform limits, and optimising for task performance alone produces skills that pass benchmarks but violate deployment constraints. MOCHA introduces *Chebyshev annealing* to navigate the constraint frontier. In §3 terms, the complexity penalty $\Omega(z)$ in the gate condition is precisely the mechanism MOCHA is operationalising, but §3's scalar $\Omega$ is a simplification: in production, the constraint surface is a Pareto frontier, not a single penalty term. MOCHA's empirical contribution is to show that ignoring this frontier — treating skill optimisation as unconstrained single-loss descent — produces skills that degrade on real deployment infrastructure even when benchmark scores improve.

**Ratchet** [@zhang2026ratchet] makes an argument that is, in some respects, orthogonal to the gradient-analogue framing and for that reason worth engaging directly. Ratchet's opening finding — that LLM-authored skills deliver $+0.0$ pp over no-skill baselines while human-curated ones deliver $+16.2$ pp — suggests that the bottleneck in self-evolving skill libraries is not the optimisation algorithm (the mechanism for proposing and accepting edits) but *lifecycle management*: whether skills are written, retrieved, curated, and retired correctly. Ratchet introduces four hygiene mechanisms — outcome-driven retirement, a bounded active-cap, meta-skill authoring, and pattern canonicalisation — and shows that these lift the $+0.0$ pp floor substantially before any gradient-analogue optimiser is applied.

This finding is not a refutation of the §3 picture but a clarification of the precondition for it. Artifact-layer descent, as formalised in §3, presupposes that the scaffold is maintained well enough for the gate $G_t$ to have a meaningful signal: if skill retrieval is so noisy that the wrong skill is injected into every rollout, the proposal process $Q_t$ receives corrupted evidence and the descent guarantee degrades to random search. Ratchet's hygiene mechanisms are, in §3 vocabulary, prerequisites for operation 1 (residual capture) and operation 2 (mode discovery) to function: outcome-driven retirement prevents stale artifacts from polluting the residual signal; the bounded active-cap prevents scaffold bloat from making retrieval unreliable (the §10 failure mode); pattern canonicalisation collapses duplicate and near-duplicate skills so the proposal process conditions on a clean, deduplicated artifact set rather than competing variants of the same pattern. The practical implication is that the deployment path to Stage-3 artifact-layer descent runs through Stage-1 hygiene as a *prerequisite*, not as an alternative. A system with strong hygiene and no optimiser sits at Stage 1 with a clean scaffold; a system with a strong optimiser and poor hygiene sits at Stage 2 with a noisy loss signal. Stage 3 requires both.

### G.8 Cross-task transfer and evidence radius

Several papers independently measure what §3 calls the *evidence radius* of a scaffold artifact — how far an edit validated in one context continues to improve performance when redeployed elsewhere — without using that vocabulary.

**Training Language Agents to Learn from Experience** [ICT; @shalev2026ict] introduces the In-context Training framework specifically to evaluate *cross-task self-improvement*: whether experience distilled from one set of tasks transfers to unseen tasks. Their finding that "current reflection-based methods can only self-correct within a single task instance" is a measurement of evidence radius at its lower bound — a radius of exactly one task — and their ICT framework is a systematic attempt to expand that radius through supervised distillation of reflections into reusable lessons. In §3 terms, ICT is an attempt to instrument Loop 2 empirically: to measure whether a locally-validated edit (one that passed the gate on one task's $L_D$) continues to improve performance when the promotion radius is expanded to cover a distribution of unseen tasks.

**Combee** [@li2026combee] approaches the same measurement from the scaling direction. ACE [@ace2025agentic] established that context-as-living-artifact (a system prompt that accumulates, refines, and organises strategies through agentic interaction) could improve over static prompts on single-agent tasks. Combee extends this to high-parallelism settings, arguing that "existing methods primarily focus on single-agent or low-parallelism settings," which "fundamentally limits their ability to efficiently learn from a large set of collected agentic traces." The parallel scaling Combee addresses is a form of Loop-2 scope expansion: when many agents run simultaneously, the trace pool available for the next proposal step is drawn from a wider deployment distribution, and the promoted artifact is being tested against a larger averaging set of patch losses. This is not cross-organisational Loop-2 promotion, but it is a step toward it, and Combee's empirical results measure how much of the evidence-radius benefit can be captured by intra-organisation parallelism before the cross-organisational barrier is reached.

**CORAL** [@qu2026coral] addresses the Loop-2 problem from the multi-agent open-ended discovery angle. CORAL replaces rigid control with long-running agents that explore, reflect, and collaborate through shared persistent memory, asynchronous multi-agent execution, and heartbeat-based interventions. The shared persistent memory is the cross-agent promoted artifact: a finding validated in one agent's exploration that is written to the shared store becomes available to all agents, and the heartbeat mechanism provides a form of auto-gated Loop-2 promotion. CORAL does not implement the versioned lineage, RBAC, or rollback that §9 requires, but it provides the only fully asynchronous multi-agent Loop-2 promotion mechanism in the current survey corpus, and its open-ended discovery framing makes the evidence-radius question concrete.

**PACE** [@ling2026pace] closes this cluster with a production-oriented two-timescale design for small language model agents. The fast timescale adapts prompts, parsers, validators, and control logic from failure signals within a deployment; the slow timescale consolidates across episodes. The two-timescale structure maps cleanly onto the Loop-1 / Loop-2 distinction of §3: Loop 1 fires at the fast timescale, updating a single deployment's scaffold; Loop 2 fires at the slow timescale, consolidating across the deployment's own episodes rather than across deployments. PACE's contribution is to show that the two-loop architecture is implementable under the resource constraints of small, frozen production models — not only under frontier-model assumptions — and that the slow/fast consolidation structure persists even when the optimiser model and the target model are the same frozen small model.

### G.9 Synthesis: what the convergence establishes

Reading the full cluster against the §3 mechanism stack and the §9 four-property criterion, four claims are now well-supported by the convergent evidence:

1. **The scaffold-versus-weights decomposition is independently confirmed.** GEPA, Meta-Harness, MOSS, RCL, and PACE all begin from the observation that model weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope properties. No surveyed paper disputes this decomposition; the variation is in which substrate each paper targets (skill document, harness code, system prompt, shared memory).

2. **Credit assignment is the central engineering bottleneck.** AHE, CANTANTE, Meta-Harness, and @ong2026harnesseval all identify credit assignment — attributing a system-level failure to a specific scaffold coordinate — as the problem that distinguishes disciplined Loop-1 evolution from trial-and-error. This is §3's operation 3, and it remains unsolved in the general multi-substrate case.

3. **Lifecycle hygiene is a precondition for descent, not an alternative to it.** Ratchet establishes that the gradient-analogue mechanism of §3 requires a maintained scaffold as a precondition. A dirty artifact pool (stale, bloated, miscurated) prevents the gate $G_t$ from receiving a meaningful signal. Hygiene and optimisation are sequential dependencies, not competing paradigms.

4. **No surveyed system combines Loop-1 automation with cross-organisational Loop-2 governance.** SkillOpt has the strongest Loop-1 closure and the most systematic evidence-radius measurement, but it does not implement cross-organisational promotion, versioned lineage with RBAC, or rollback. CORAL implements asynchronous cross-agent promotion within one system but not across organisations. PACE implements two-timescale consolidation within one deployment. Meta-Harness implements Loop-1 closure over the harness substrate but no Loop-2 promotion mechanism. The four-property gap named in §9 is not reduced by any member of this cluster; it is, if anything, confirmed more strongly by the independent convergence of multiple research threads on the same single-organisation ceiling.

The §3 picture is not aspirational. It is the limit that the field is converging on from multiple directions simultaneously, under multiple framings and for multiple substrates. What remains is not the architecture — that exists, in fragments, across SkillOpt, GEPA, Meta-Harness, AHE, MOSS, CANTANTE, Ratchet, PACE, CORAL, and RCL — but the governance layer that would allow a locally-validated edit to be promoted to a cross-organisational scope without losing the auditability, rollback safety, and evidence-radius discipline that make it trustworthy.

### G.10 SkillOpt against §9's four properties

Mapped onto §9's four properties of governed cross-tenant scaffold optimization:

- (a) **Auto-gated Loop 1.** *Satisfied.* The held-out selection-split gate at strictly-greater margin instantiates $G_t$.
- (b) **Multi-tenant cross-org promotion.** *Absent.* SkillOpt is a single-organisation research system; there is no governed cross-tenant aggregator.
- (c) **Versioned lineage with RBAC.** *Partial.* The exported `best_skill.md` is a versioned artifact, and the protected slow-update field separates fast and slow consolidation. There is no documented RBAC layer or audit-trail policy, and `edit_apply_report.json` is an operational log rather than an access-controlled lineage system.
- (d) **Rollback.** *Absent.* The training loop selects the best validation-gated skill and exports it; no rollback envelope on deployed artifacts is reported.

The cross-model, cross-harness, and cross-benchmark transfer experiments reported by SkillOpt are *empirical evidence-radius measurements*: they tell us that a skill optimised in one (model, benchmark, harness) cell continues to improve performance when redeployed in nearby cells without further optimisation. In §3 vocabulary, this is a measured Loop-2 *radius* for the artifact, not a *governance mechanism* for promoting the artifact. Both readings are useful: SkillOpt is the strongest current Loop-1 proof and supplies the first systematic transfer evidence at the scaffold layer, while the §9 cross-tenant governance triad ((b), (c), (d)) remains unfilled.

### G.11 Cost and bloat

SkillOpt reports 0.6M to 46.4M training tokens per absolute test-point gain (their Table 6), with the procedural benchmarks (SpreadsheetBench, OfficeQA, LiveMath) at the cheap end and search/visual benchmarks (SearchQA, DocVQA) an order of magnitude more expensive per point. The deployed artifact remains 379–1,995 tokens regardless. This is, to our knowledge, the first published cost-per-point figure for scaffold-layer descent, and it complements the §10 scaffold-bloat discussion (and the Ratchet hygiene-precondition finding walked in G.7): the textual learning rate $L_t$ with cosine decay keeps the deployed skill compact even when the optimiser explores many more edits than are accepted (only 1–4 edits survive into the final skill across the six benchmarks). The mechanism that prevents the deployed artifact from bloating is exactly the complexity penalty $\Omega(z)$ of §3, instantiated as a hard cap on accepted edits per step rather than a soft regulariser.

---

## References

::: {#refs}
:::
