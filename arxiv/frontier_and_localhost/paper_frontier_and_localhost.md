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

This paper argues that scaffold evolution can be modeled as learning in a precise sense: scaffold artifacts are updated from failure signal, the updated artifacts reduce future failure probability on a local patch, and the update process — observe failure, generate candidate delta, gate it, persist it, optionally promote it — has the structure of discrete, gated, stochastic local optimization. The substrate is symbolic and human-readable rather than continuous and differentiable, and the gate stands in for the gradient; the model is best read as *artifact-layer optimization*, with descent-like behavior under the assumptions catalogued in §3.2. Where those assumptions fail (no measurable patch loss, no credit-assignment process, no persistent artifact distinct from optimiser state) the framing should be read as modeling language rather than a theorem.

Once you accept the framing, the field snaps into place. A Claude Skill is not "just a markdown file." It is a learned procedural weight kept outside the model. A Cursor Rule is not "just an instruction." It is a local parameter for one project's distribution shift. A RAG connector is not "just retrieval." It is patch-specific memory access. A tool registry is not "just integration." It is capability provisioning along an axis the base model cannot reach. A PR review against a shared rule repository is not "just governance." It is a promotion gate on a federated update. An eval suite that blocks merge is not "just testing." It is a validation-loss check before promotion. A cross-tenant artifact repository is not "just sharing." It is *federated-style artifact aggregation* across distributed shards — scope expansion under a gate, rather than arithmetic averaging of comparable updates (we sharpen the distinction in §3.2 and §9). The mechanisms were already there; only the name was missing.

We survey approximately 130 systems across six substrates (instructions, skills, memory, tools, orchestration, governance), score each on a 0–5 patch-plasticity rubric, and analyse the thirteen research systems (plus two industry exemplars) that satisfy a strict *composite two-loop* criterion: an inner loop that updates a persisted artifact from session feedback, an outer loop that promotes the artifact across scopes under explicit versioning. The two-loop design space is a 3×3 matrix on gate type — *Auto-gated* when the commit-or-promote decision is operationalised by an algorithmic criterion, *Human-gated* when it is reviewer judgment. The matrix has three populated cells; three are empty for distinct structural reasons. The fully automated, governed, cross-tenant cell has no surveyed occupant. That empty corner is the paper's open-question headline and a concrete Paper-4 target.

The architectural review of how to actually build such systems — five reference patterns, a five-level maturity model, a substrate-selection rubric, three migration paths, the full nine-category failure taxonomy, and eight design principles — is deferred to follow-on practitioner work. This paper is the survey and the framework.

## 2. Why patch errors must live outside the weights

The scaffold is not merely where production systems happen to store patches. Under the constraints production deployment imposes — high update cadence, per-tenant specificity, inspectability, reversibility, and auditable governance — it is the *dominant practical substrate* for patch-specific adaptation, because the weight substrate fails several of those constraints at once. Frontier training and production reliability optimise for objectives that are in tension, and that tension forces most adaptation outside the model. Per-tenant fine-tunes, LoRA adapters, distilled small models, and learned routing can in principle absorb some patch residuals; the survey finds that in practice the scaffold dominates because it is cheap, inspectable, reversible, locally scoped, and updatable on a daily cadence rather than a release cadence.

**Frontier training optimises for breadth.** The weights are tuned for cross-patch generalisation: they smooth over local conventions, contradictory tenant preferences, and rare workflow-specific failures in order to preserve broad competence across millions of unseen deployments. The smoothing is not incidental. It is the training objective. A model that overfits to one tenant's naming conventions or one team's preferred error-handling style loses transfer to the next tenant; a model that encodes every patch's idiosyncratic eval expectation loses the general-purpose competence that made it worth deploying in the first place. The smoothing dynamics have been measured directly: RLHF reduces output diversity and homogenises preferred styles across users (Kirk et al., 2024; Padmakumar & He, 2023), and instruction-tuning data distributions favour patterns that generalise across the annotator pool rather than patterns specific to any one deployment. The frontier model is therefore *trained to be unable* to encode a single tenant's idiosyncrasies as preferred behaviour; absorbing that idiosyncrasy without weight retraining is exactly what the scaffold layer is for.

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

Our previous work (Arbuzov, Shvets & Bei, 2025; *Architecture of Errors*, 2026) argued that LLM errors concentrate sparsely at key tokens and cluster into a finite catalogue of recurring modes whose size grows polylogarithmically in observed failures. The framework left a *placement* question — where do the interventions live? The answer follows from the tension above. Under deployment-time constraints (release cadence, tenant isolation, inspectability, rollback), the scaffold is the substrate that satisfies all four; the survey finds that production systems consequently locate the bulk of patch-residual interventions there. The frontier model generalises; the localhost scaffold specialises; reliability comes from governing that specialisation.

## 3. Artifact-layer descent

The remaining question is whether "scaffold evolution" is learning in any technical sense or just engineering practice. The answer depends on what one means by learning.

Let $D$ be a deployment patch — a specific application, user, or task distribution. *Patch* is used throughout this paper with a defined scope hierarchy: USER ⊂ PROJECT ⊂ STACK ⊂ TENANT ⊂ CORE. A USER patch is one human's account or fork; a PROJECT is one repository, workflow, or product workspace; a STACK is a curated bundle of projects under one team; a TENANT is an organisation or customer; CORE is the cross-tenant universal scope. Each level induces its own loss $L_{D_{\text{level}}}$ (the average over the patches inside that scope). When the text says "cross-tenant promotion" or "cross-organisation federation," it specifically means moving artifacts up to the CORE or cross-TENANT level; "patch-specific adaptation" without qualifier means descent on a USER or PROJECT-level $L_D$. Let $M$ be the frozen frontier model, accessed via inference but not updated. Let $S_t$ be the scaffold at time $t$: the layered collection $\{S_t^{(1)}, \ldots, S_t^{(6)}\}$ of instruction set, skill library, memory store, tool registry, orchestration graph, and governance configuration. Let $\pi(M, S_t, x)$ denote the system's behaviour on input $x$ — the model running on the model-plus-scaffold composite. Let $L_D(S_t) = \mathbb{E}_{x \sim D}[\ell(\pi(M, S_t, x))]$ be the expected residual failure rate on the patch.

A failure observation produces a candidate delta $\Delta S$: an instruction edit, a new skill, a memory correction, a tool re-registration, a topology change, or a governance-rule update. A gate $G_t$ accepts $\Delta S$ if the estimated patch-loss change clears an acceptance threshold *and* risk stays within tolerance:

$$
S_{t+1} = \begin{cases} S_t \oplus \Delta S, & G_t(\Delta S) = 1, \\ S_t, & G_t(\Delta S) = 0, \end{cases}
$$

where $\oplus$ denotes structured application of an admissible edit (an instruction rewrite, a skill insertion, a memory correction, etc.) to the current scaffold.

Different surveyed systems instantiate $G$ differently. NanoResearch's gate is a semantic-merge by the orchestrator (algorithmic). SkillRL's gate is an RL threshold at task-category accuracy below 0.4 (algorithmic). AlphaEvolve's gate is a cascade evaluator with MAP-Elites archive selection (algorithmic). SkillForge's gate is an LLM-judge with >90% human agreement *plus* a human support engineer (hybrid algorithmic + reviewer). Anthropic's skills repository uses reviewer judgment on a PR-by-PR basis with no algorithmic threshold (purely reviewer-judgment). DSPy's gate is gradient-like over prompt-template space without persistent commitment. Reflexion's gate is essentially absent: any reflection becomes a memory entry.

These gates serve related but not identical roles. Eval-gated, LLM-judge-gated, RL-threshold-gated, and reviewer-gated systems all estimate a directional loss change on the candidate edit and accept iff that estimate clears a margin — they instantiate the per-edit gate of §3.2 directly. Semantic-merge and MAP-Elites archive-selection gates are better interpreted as *proposal-pruning* steps that precede the per-edit gate: they bound which $z_t$ enter consideration rather than directly estimating $\widehat{\Delta} L_D$. Appendix C maps each surveyed gate type to its slot in the §3.2 formalism. Across the spectrum, each system is asking, by some method, whether $\Delta S$ moves $S_t$ toward lower $L_D$. The substrate is discrete: scaffold edits are typically textual, procedural, or symbolic, not differentiable in the backpropagation sense. The gate is mediated: humans, evals, LLM-judges, or surrogate verifiers stand in for the gradient. The update is governed: not every candidate $\Delta S$ propagates; some are rejected, some are quarantined to a single user's fork, some climb a layered hierarchy from local to shared scope before they take.

We call this *artifact-layer descent*. In a differentiable relaxation — where scaffold edits are represented as coordinates in an artifact basis, proposals are generated from estimated negative-gradient directions over that basis, and the gate is a differentiable validation-loss estimator — artifact-layer descent reduces to a form of stochastic gradient-like local search. In ordinary deployments, where edits are discrete, proposals are LLM- or template-generated rather than gradient-driven, and gates are eval-, judge-, or reviewer-mediated, the process is a discrete, gated stochastic approximation to descent. The two are continuous with one another in modeling style; the difference is one of substrate, proposal mechanism, and gate signal-to-noise.

Two loops follow naturally. **Loop 1** is within-context: a session feedback signal triggers an update to a persisted local artifact. **Loop 2** is cross-context: a local artifact is promoted to a shared scope (cross-project, cross-user, cross-organisation) under explicit versioning. Loop 1 is the local descent step on a per-patch loss; Loop 2 is *federated-style artifact aggregation* — scope expansion under a gate, not arithmetic averaging of comparable numeric updates. The DP-FedAvg analogue applies only to the *target* design in §9 (the empty enterprise corner), which would additionally require artifacts to be embedded as mergeable update objects before averaging makes sense; surveyed Loop-2 mechanisms are selection, merge, curation, review, and distribution rather than averaging. Each loop has a gate; gates are **Auto-gated** when the decision is an operationalised algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement, surrogate verifier, benchmark cascade), **Human-gated** when the decision is reviewer judgment (automation often precedes the gate but the gate itself is reviewer discretion), and **None** when the loop is absent.

These five terms — Loop 1, Loop 2, Auto-gated, Human-gated, None — anchor the rest of the paper.

The framing positions the work against several adjacent literatures. CoALA (Sumers et al., 2023) proposes a static cognitive architecture of modular memory and structured action; we update CoALA's snapshot into a dynamic deployment architecture with governance. The self-evolution surveys (Gao et al. 2026; Fang et al. 2025) treat agents as learners that update weights, representations, or optimiser-selected artifacts — they locate the gradient inside the model. The memory-survey of Du (2026) and the skills-survey of Zhou et al. (2026) cover individual substrates with version-and-promotion machinery that mirrors S3 and S2 here but stops at the substrate boundary. ACE (2025) treats context as a single evolving playbook. Each adjacent work touches a piece of the picture; none develops the cross-substrate artifact-layer descent framing or the design space it implies.

### 3.1 The mechanism stack

The abstract update rule $S_{t+1} = S_t + G(\Delta S)$ expands into six operations that every patch-plastic system must perform — whether explicitly engineered or accidentally emergent.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, eval regressions, tool-call failures. The Loop-1 signal source. Without it, $\Delta S$ has no provenance.
2. **Mode discovery.** Cluster repeated failures into patch-specific error modes. The Paper-2 catalogue, instantiated locally per patch.
3. **Delta synthesis.** Convert a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, an eval case. This is the production of $\Delta S$.
4. **Delta validation.** Estimate whether the edit reduces $L_D$ without collateral damage on adjacent inputs. This is the gate $G$ — Auto-gated when the check is an algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement), Human-gated when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted $\Delta S$ stays in the local fork or climbs the scope hierarchy — project, stack, organisation, cross-tenant. This is Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, detect over-fitting to one patch. Without this layer, accumulated $\Delta S$ produces the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline that does not yet exist in coordinated form. Surveyed systems implement the operations partially and unevenly: research full-auto systems excel at (3) and (4), production governance leaders at (5), industry hybrids at most of (1)–(5) but rarely (6). Implementation patterns for each of the six are deferred to follow-on work; this paper's purpose is to make the discipline visible.

### 3.2 The mechanism made formal: scaffold updates as discrete stochastic descent

**Assumptions and scope of the formalization.** The descent argument below holds when: (i) $\theta_M$ is fixed during the adaptation window; (ii) scaffold edits are persistent, inspectable artifacts distinct from transient context; (iii) the patch admits a measurable operational loss; (iv) the proposal process can attribute failures to scaffold coordinates with non-zero probability; (v) gates are imperfect estimators of finite directional loss change rather than oracle access to $\Delta L_D$; (vi) Loop-2 promotion is *scope expansion under a gate*, not arithmetic averaging of comparable updates. Survey claims of the form "no surveyed system has X" are bounded by the audited public corpus and the survey cutoff of May 2026. Where the formalism is metaphor rather than mechanism (a deployment lacks measurable loss, or proposal generation cannot assign credit to a coordinate), the descent picture should be read as modeling language rather than a theorem about that deployment.

The mechanism stack above makes artifact-layer descent operational, but the word "descent" still needs to earn its keep. A skeptical reading is available: scaffold updates are just engineering edits, not gradients; PR review is not backpropagation; an LLM-judge is not a derivative; a markdown rule is not a differentiable parameter. All true. But they do not defeat the claim. They locate the claim in the correct optimization class.

Scaffold evolution is not backpropagation through continuous weights. It is discrete, gated, patch-local stochastic descent over a structured artifact space.

Let the frontier model have fixed parameters $\theta_M$. Let the scaffold be a structured parameter object

$$\theta_s \in \Theta_s = \Theta_1 \times \Theta_2 \times \Theta_3 \times \Theta_4 \times \Theta_5 \times \Theta_6,$$

where the six coordinates correspond to the six substrates of §4: instructions, skills, memory, tools, orchestration, and governance. A coordinate may be a line in a `CLAUDE.md` file, a Cursor rule, a skill file, a memory entry, a retrieval configuration, a tool schema, an agent-routing edge, an eval threshold, or a promotion rule. The space $\Theta_s$ is not smooth. It is discrete, symbolic, and versioned. But it is still a parameter space: changing $\theta_s$ changes the behavior of the model–scaffold composite.

For a deployment patch $D$, define patch loss as

$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$

where $\pi(\theta_M,\theta_s,x)$ is the output or action trace produced by the frozen frontier model under scaffold $\theta_s$, and $\ell$ is an operational loss. Depending on the patch, $\ell$ may be a hard-failure indicator, user-correction rate, eval-suite error, tool-call failure, retrieval miss, schema violation, reviewer disagreement, or graded task score. The important distinction is substrate: $\theta_M$ is fixed during deployment; $\theta_s$ is the object being fit.

A failure observation does not directly yield an analytic gradient. It yields a candidate edit. Let

$$z_t \in \mathcal{A}(\theta_s^t)$$

be an admissible scaffold edit proposed at time $t$, drawn from a proposal process

$$z_t \sim Q_t(z \mid H_t, \theta_s^t),$$

where $H_t$ is the accumulated history of failures, corrections, rejected outputs, eval regressions, reviewer comments, tool-call traces, and prior accepted deltas, and conditioning on $\theta_s^t$ ensures proposals are admissible at the current scaffold. The admissible edit set $\mathcal{A}(\theta_s^t)$ is the local neighborhood of the current scaffold: the rule can be rewritten, a skill added, a memory corrected, a tool schema tightened, an orchestration edge changed, an eval case inserted, a promotion policy modified.

Because the space is discrete, the relevant gradient analogue is not $\nabla_{\theta_s} L_D$. It is the *finite directional difference* in loss induced by an edit:

$$\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s),$$

where $\theta_s \oplus z$ denotes the scaffold obtained by applying edit $z$. A useful edit is one for which

$$\Delta_z L_D(\theta_s) < 0.$$

The gate estimates whether this inequality holds. Let $\widehat{\Delta}_z L_D$ be the gate's noisy estimate of the directional loss change. In an eval-gated system, $\widehat{\Delta}_z L_D$ is measured on a held-out task suite. In an LLM-judge system, it is estimated by model-mediated scoring, ideally calibrated against human agreement. In a reviewer-gated system, it is estimated by human credit assignment and PR review. In an RL-threshold system, it is estimated by reward improvement. In a verifier-gated system, it is estimated by a symbolic, learned, or surrogate verifier.

The update rule is therefore

$$\theta_s^{t+1} = \begin{cases} \theta_s^t \oplus z_t, & \text{if } G_t(z_t)=1, \\ \theta_s^t, & \text{if } G_t(z_t)=0, \end{cases}$$

where the gate $G_t$ accepts when the estimated improvement clears the deployment's threshold:

$$G_t(z_t)=1 \quad \Longleftrightarrow \quad \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \leq -\tau_t.$$

Here $\Omega(z_t) \geq 0$ is an optional complexity or risk penalty — longer instructions, broader tool permissions, larger memory writes, more invasive topology rewrites, wider promotion scope — while $\lambda \geq 0$ controls regularization and $\tau_t \geq 0$ is the required improvement margin. Production systems often implement this without writing the equation: an eval suite blocks a merge if regression appears; a reviewer rejects a vague rule; a governance system prevents a local artifact from becoming shared until evidence accumulates.

Two distinct quantities sit in the optimization analogy and the paper keeps them separate. **Edit magnitude** — how much a single accepted edit changes the local scaffold under $\oplus$ — plays the role of *learning rate*: a one-line rule patch is a small step, a full rubric rewrite is a large step, a tool-schema overhaul is a large step. **Promotion radius** — how many downstream patches the accepted edit affects — controls *which loss is being descended on*: USER-level acceptance descends on one patch's loss $L_D$; PROJECT promotion descends on an average $\tfrac{1}{|D_{\text{proj}}|}\sum_{D' \in D_{\text{proj}}} L_{D'}$ across a project's patches; STACK promotion widens the averaging set; CORE or cross-tenant promotion descends on a federated average over many tenants' losses. Learning rate (edit magnitude) and update radius (promotion scope) are independently controllable, and the gate must be calibrated against both. Governance is therefore not administrative overhead: it is the regularization system that prevents a small-magnitude edit from being descended on the wrong loss.

The correspondence to standard optimization is therefore not decorative:

| Optimization concept | Scaffold analogue |
|----------------------|------------------------------------------------------------|
| Parameter vector | Instructions, skills, memories, tools, routing graphs, eval gates, governance rules |
| Forward pass | Model–scaffold composite executing on patch input |
| Loss | Failure, user correction, eval regression, retrieval miss, tool error, schema violation |
| Finite directional difference | $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$, the loss change induced by a candidate edit |
| Gradient estimate | Credit assignment identifying the scaffold coordinate responsible for the failure |
| SGD step | Accepted scaffold edit |
| Aggregated update | Multiple recurring failures aggregated before update (either by sampling — *mini-batch averaging* — or by sign-of-direction agreement across $k$ proposals — *multi-sample voting*) |
| Learning rate | Edit magnitude under $\oplus$ (size of a single accepted edit) |
| Update radius | Promotion scope — which loss is being descended on (USER, PROJECT, STACK, TENANT, CORE) |
| Validation loss | Held-out patch eval before merge |
| Regularization | Complexity penalty $\Omega(z)$, bloat control, cross-patch regression checks |
| Overfitting | Scaffold improves on this patch and degrades elsewhere |
| Rollback | Reverting a harmful accepted update |

**Credit assignment without chain rule.** Scaffold systems do not compute chain-rule derivatives through markdown files or tool registries, and the correspondence above deliberately omits a "backpropagation" row. They do, however, perform *credit assignment* through a pipeline: if the final answer fails, the responsible coordinate may be a retrieval configuration three layers upstream, a missing tool schema constraint, an underspecified instruction, a stale memory, or a bad orchestration edge. Engineers do this manually; LLM-judges and surrogate verifiers do it semi-automatically. The operation is *attribution* — output error is assigned to an upstream coordinate — rather than backpropagation. The descent argument of §3.2 needs only that this attribution succeeds with non-zero probability per failure (assumption (iv) of the scope box), not that it is performed by chain rule.

Several concrete cases make the mechanism visible.

In a RAG system, suppose failures recur because retrieved context omits the decisive clause. The observed loss is not merely "the model hallucinated." Credit assignment traces the error to the retrieval coordinate: chunking, query rewrite, metadata filter, embedding model, reranker, citation policy, or context-packing rule. The candidate edit might tighten chunk boundaries, add a metadata constraint, change the reranker, or insert a regression eval containing the missed clause. The gate tests whether retrieval recall and answer accuracy improve on the patch eval without degrading adjacent cases. If accepted, the scaffold has moved downhill on the local loss surface.

In a pitch-review workflow, suppose the system repeatedly overrates decks that claim a "huge market" without numeric evidence. The failure cluster identifies an under-specified rubric coordinate. The candidate edit changes "evaluate TAM size" into "require a numeric market estimate and source; if absent, cap TAM score at 4/10." The gate runs the revised rubric against held-out decks with human scores. If agreement improves without damaging unrelated criteria, the edit is committed. The rubric is not commentary. It is a scaffold parameter updated in response to loss.

In a tool-using agent, suppose calls repeatedly fail because optional parameters are underspecified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The candidate edit adds required fields, constrained decoding, or a pre-call uncertainty check. The gate estimates whether tool-call failure decreases without increasing refusal, latency, or unnecessary clarification. If accepted, the scaffold has fit a recurring local failure mode.

In a memory system, suppose a stale customer preference is repeatedly retrieved and causes bad decisions. The failure is not a weight error. The responsible coordinate is a memory entry plus its provenance, priority, and expiry policy. The candidate edit corrects, expires, or version-tags the memory. The gate checks whether the correction improves future behavior without erasing useful history. Again: loss, credit assignment, candidate update, validation, commit.

Under bounded loss and a few additional regularity conditions, this is descent in the formal sense. The critical bookkeeping is that the gate sees an estimator $\widehat{\Delta}_{z_t} L_D$ of the directional loss change, not the true $\Delta_{z_t} L_D$; acceptance is conditional on the estimator, and the descent argument must therefore distinguish the two.

> **Assumption A1 (positive descent bias on accepted edits).** There exists $\gamma_t > 0$ such that
>
> $$\mathbb{E}\!\left[\widehat{\Delta}_{z_t} L_D(\theta_s^t) \mid G_t(z_t)=1,\theta_s^t\right] \leq -\gamma_t - \tau_t.$$
>
> The gate's accept-threshold $\tau_t$ ensures accepted edits clear the margin under the estimator.
>
> **Assumption A2 (bounded estimator bias on accepted edits).** There exists $\varepsilon_t \geq 0$ such that
>
> $$\big|\mathbb{E}\!\left[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t(z_t)=1,\theta_s^t\right]\big| \leq \varepsilon_t.$$

Combining A1 and A2 with the update rule and writing $p_t = \Pr(G_t(z_t)=1 \mid \theta_s^t)$,

$$\mathbb{E}\!\left[L_D(\theta_s^{t+1}) \mid \theta_s^t\right] \leq L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t \varepsilon_t.$$

This is descent under a noisy estimator: the per-step expected improvement is the gate's margin minus its estimator bias, weighted by the acceptance probability.

> **Proposition (convergence of loss, informal).** Assume A1, A2, bounded loss $0 \leq L_D(\theta_s) \leq B$, and additionally:
>
> - **A3 (proposal coverage).** At every non-$G$-stable scaffold there exists $\delta > 0$ such that the proposal distribution $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}\!\left[\Delta_z L_D\right] \leq -\delta$.
> - **A4 (effective compactness).** The reachable scaffold orbit $\{\theta_s^t\}$ takes values in a finite or precompact subset of $\Theta_s$.
> - **A5 (persistent acceptance with summable bias).** $\sum_t p_t(\gamma_t + \tau_t) = \infty$ and $\sum_t p_t \varepsilon_t < \infty$.
>
> Then $L_D(\theta_s^t)$ is a non-negative supermartingale up to summable noise; $L_D(\theta_s^t) \to L_\infty$ almost surely for some random $L_\infty \geq 0$; and the limit set of $\{\theta_s^t\}$ is **$G$-stable**: no admissible edit clears the gate with negative expected directional loss in the limit.

The proposition claims convergence of the *loss* and stability of the *gate decision*, not convergence to a global or even local optimum of $L_D$. A globally suboptimal $G$-stable scaffold is consistent with the result — for example, when the proposal distribution $Q_t$ never proposes the improving edit that would unlock further descent, or when the estimator $\widehat{\Delta}$ is biased in a way that consistently rejects an improving direction. This is the ordinary target of local stochastic optimization under noisy estimators rather than a guarantee of optimality.

In non-stationary patches, $D = D_t$, the same mechanism tracks a moving optimum rather than converging once. This is why recency weighting, replay, pruning, expiry, and rollback are not optional hygiene. They are the scaffold-level analogues of continual-learning machinery. Without them, accumulated edits create scaffold bloat, stale rules, memory pollution, and patch-level plasticity loss.

This formalization also clarifies the role of overfitting. In weight training, overfitting is usually a defect: the model becomes too specialized to the training distribution and loses transfer. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve cross-patch generality; they must smooth over local conventions, rare workflow-specific failures, contradictory tenant preferences, and hidden evaluator expectations. A deployment patch needs the opposite: selective specialization to local residuals. The scaffold is therefore an intentionally overfittable layer, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold that improves one repository, hospital workflow, legal diligence process, or support desk may degrade performance elsewhere. That is not a contradiction. It is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

Loop 1 and Loop 2 are now mathematically interpretable, and they map cleanly onto the *edit-magnitude* / *update-radius* split of the analogy table. Loop 1 proposes and validates local descent steps and operates on the per-patch loss $L_D$. Loop 2 expands the update radius — it selects, merges, and promotes accepted local edits so that they apply to a larger averaging set of patch losses (a project, a stack, a tenant, or a cross-tenant pool). USER-level acceptance descends on a single $L_D$. PROJECT-level promotion descends on a project-averaged loss. STACK-level promotion widens the average further. CORE or cross-tenant promotion descends on a federated average. The two-loop design space is therefore not just a taxonomy of engineering patterns: it is a taxonomy of *which loss each surveyed system is descending on*, gated by which estimator.

The artifact-layer descent framing is mechanism when five conditions hold: measurable patch loss, residual capture, failure-to-coordinate credit assignment, candidate delta synthesis, and a gate that estimates directional loss change before persistence or promotion. It is merely metaphor when those conditions are absent. This distinction explains the survey split. Research full-auto systems automate delta synthesis and validation but often lack governance. Production governance systems validate and promote but often lack failure-triggered candidate generation. Hybrid systems close more of the loop. The empty enterprise corner is the case where all pieces must hold across tenants.

The conclusion is simple: the frontier model is trained to avoid overfitting across patches. The scaffold exists to overfit safely inside one.

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

Each substrate maps to a different Paper-2 residual class. S1 and S4 carry capability provisioning. S2 and S3 accumulate the patch-specific failure-mode catalogue. S5 lowers per-step hard-fraction by specialisation. S6 is the gate substrate — without it, none of the other five can be updated safely across deployments. *The substrates are not a taxonomy of nice-to-haves. They are the layers of the scaffold parameter vector, separately addressable by Loop 1 and Loop 2.* Score distributions and per-substrate exemplars are summarised in §6.1; the maturity-rubric details for practitioner adoption are deferred to follow-on work. We adopt this six-coordinate decomposition for the survey because each coordinate is independently editable in production systems (a Cursor rule can change without touching a tool schema; an eval threshold can change without touching a memory store); alternative partitions are possible (e.g., separating evals from governance, or merging instructions and skills) and the descent argument of §3.2 is invariant to the partition so long as the independent-editability property holds.

## 5. Survey method and evidence tiers

The survey covers approximately 130 unique LLM systems published or productionised between January 2023 and May 2026, split into two sets.[^count-note] The **core corpus** of approximately 90 candidate scaffold-learning systems satisfies the patch-plastic discriminator (score ≥ 3 on at least one substrate, indicating skills, memory, or multi-scope persistence beyond ephemeral prompts). The **contrast corpus** of approximately 38 systems is commonly described in the public discourse as agentic or self-improving but fails at least one discriminator — typically Loop 2 absent, no persistent artifact distinct from optimiser state, or in-context-only adaptation. Headline statistics quote the core corpus; the contrast set is preserved as asterisked entries in the matrices for definitional clarity.

[^count-note]: The master CSV (`supplementary/p3_master_scores.csv`) records each system as one row per scored substrate, so the row count exceeds the unique-system count. Cited figures throughout §§5–8 refer to unique systems; Appendix B reconciles the per-substrate row count, the unique-system count, and the patch-plastic core/contrast split.

**Inclusion.** Any system that (a) wraps a foundation model with at least one persistent artifact updated from deployment signal, or (b) is named in the public discourse as a "self-improving," "scaffolded," or "agentic" system. The contrast set (Self-Refine, ReAct, plain Mem0, DSPy/TextGrad, etc.) is included precisely so the discriminator has something to mark against.

**Exclusion.** Systems whose only update mechanism is weight-level fine-tuning or RLHF — these are model-side, not scaffold-side, and belong to the self-evolution literature this paper differentiates from. Systems with no public evidence of deployment (white papers without code, demos, or production claim).

**Evidence tiers.** Each system carries one or more of: (T1) peer-reviewed publication, (T2) arXiv preprint, (T3) production claim with metrics, (T4) open-source artifact (GitHub, registry), (T5) industry-blog or interview-level documentation. Systems with T1 or T4 evidence carry highest weight in the cluster analysis (§7); T3 systems are admissible where the claim is concrete (specific benchmark, named integration target); T5 systems are admissible only when corroborated by T1–T4 elsewhere. Tier flags are propagated to cluster claims through the per-row evidence column in Appendix A; T3 production claims are not pooled with T1/T2 evidence when computing cluster-level statistics. **Survey window and dating.** The corpus includes arXiv preprints published through May 2026; preprint-only systems carry T2 evidence and are flagged in Appendix A. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.

**Scoring.** Each system received a substrate-by-substrate 0–5 score against the rubric of §4 and an integrated patch-plasticity (PP) score in {0,1,2,3,3.5,4,4.5,5}. Half-scores were used sparingly for systems where one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). Scoring is single-rater; the supplementary CSV exposes every per-system score so reviewers can audit ambiguous classifications independently against the per-substrate evidence harvests (`supplementary/p3_harvest_s1_instructions.md` through `p3_harvest_s6_governance.md`).

**Composite two-loop criterion.** A separate, stricter audit applied to 22 candidate systems. A system qualifies as composite two-loop if and only if it satisfies both: Loop 1 modifies a persisted artifact from a session signal *and* Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage. Thirteen research systems passed the strict audit, with two additional industry exemplars (Sierra Agent OS 2.0, Cognition Devin) evaluated using vendor documentation as primary evidence and explicitly flagged in the matrix of §8; nine systems failed (MAE, MetaGen, MetaReflection, CLIN — Loop-2 absent; DSPy, TextGrad — no persistent artifact distinct from optimiser state; Mem0, Zep, ChatGPT Memory — no Loop-2 promotion path).

**Sensitivity analysis.** Under relaxation (a) — counting any of *versioning OR lineage OR rollback* as the Loop-2 governance criterion — the composite-two-loop count rises from thirteen research systems to approximately seventeen, by re-admitting MAE, MetaGen, MetaReflection, and CLIN that were excluded for lacking versioned promotion lineage. Under relaxation (b) — admitting session signal that updates optimizer state without persisting an artifact distinct from optimiser state — the count rises to approximately fifteen, by re-admitting DSPy and TextGrad. The qualitative findings (Auto×Auto well-populated, [Human × Human] and [Human × Auto] empty in the surveyed corpus, governance-first cluster in [None × Auto], enterprise full-auto cell empty) survive both relaxations. The CSV bundled in `supplementary/` permits readers to re-run either relaxation.

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
3. **Memory versioning is mostly unsolved.** Only the Cuadros et al. (2026) governed collaborative memory framework provides explicit provenance, versioning, and correction pathways. Production default is append-only with implicit retrieval-based forgetting — at odds with the patch-plastic discriminator's correction requirement.
4. **Scaffold-level curriculum is absent.** No surveyed system selects *which* sessions inform the gradient. Every session contributes equally; weighting by recency, severity, or representativeness has not been published.
5. **Overfitting detection at Loop-2 promotion is absent.** No surveyed system runs a held-out eval set per project to catch scaffolds that over-fit one deployment before they propagate to another.

Each absence is a Paper-4 target. The conclusion echoes them; the survey makes them visible.

## 7. Convergent patterns

The corpus, scored against the rubric of §4, produces four archetypal clusters that recur across both research and industry. We present the clusters here rather than walking every system; the full table is in `supplementary/p3_master_scores.csv`.

**Research full-auto.** Systems where both loops fire from algorithmic criteria and no human gates the routine update. **NanoResearch** (Xu et al., 2026) co-evolves Skills, Memory, and Policy with a semantic-merge orchestrator; Innovation 4.96 → 5.65 and Compliance 6.66 → 8.96 across three rounds. **SkillRL** (arXiv:2602.08234) uses RL reward distillation with a hard threshold at task-category accuracy below 0.4 and reports +15.3% over strong baselines. **AlphaEvolve** (DeepMind, 2025) runs a Gemini-driven ensemble with a cascade evaluator and a MAP-Elites archive, deployed at Google to gain +0.7% Borg compute worldwide, +23% on the Gemini training kernel, +32.5% on FlashAttention, and the first general-field, recursively applicable improvement over Strassen's 1969 bound on 4×4 complex matrix multiplication (48 scalar multiplications). The honest framing matters: AlphaTensor (Fawzi et al., 2022) had already found a 47-multiplication algorithm over GF(2), and Winograd reported a 48-multiplication method for commutative rings that was not recursively applicable; AlphaEvolve's contribution is the first improvement that holds in general fields and admits recursive composition. **DGM** (Zhang et al., 2025) modifies its own source code with archive-based parent selection; SWE-bench 20% → 50%. The cluster maximises velocity. Enterprise governance is uniformly absent.

**Production hybrid.** Systems where Loop 1 is Auto-gated (an algorithmic criterion) and Loop 2 is Human-gated (reviewer approval before propagation). **SkillForge** (Alibaba Cloud, arXiv:2604.08618) drives auto-generated skill diffs through an LLM-judge with >90% human agreement (the Loop-1 gate); human support engineers then review what the LLM-judge passes (the Loop-2 gate). VFS version commits provide full lineage. **CASCADE** (Huang et al., 2025) reports the largest within-benchmark ablation gain in the surveyed corpus — 93.3% vs. 35.4% on SciSkillBench (+57.9 pp) — driven by memory consolidation gated by human-agent collaboration. The headline gain is not directly comparable to AlphaEvolve's production +0.7% Borg or DGM's +30 pp on the broader SWE-bench: it is measured on a single benchmark designed to reward the very mechanism CASCADE adds, and should be read as evidence of mechanism-on-benchmark fit rather than as a cross-cluster effect size. **Sierra Agent OS 2.0** routes AI-driven Insights through human-authored Expert Answers in GitHub-style Workspaces. **Cognition Devin** ships dynamic in-session tool creation with a 67% PR-merge rate (the merged PRs are the Loop-2 promotion). This is the production-viable cell.

**Governance-first.** Systems where Loop 2 is Auto-gated by an eval criterion but Loop 1 is essentially absent — there is no automatic candidate-generation pipeline. **Braintrust**, **Vellum**, **LangSmith Hub**, **W&B Weave**, **Agenta**, **LangFuse**. The pattern is *prompts-as-code*: immutable commits, semantic-version tag pointers, PR-blocked merges on eval regression, sub-five-minute rollback. Engineers iterate the artifacts manually; the eval pipeline gates the promotion. We frame this as **MLOps for scaffolds**, distinct from MLOps for weights.

**Open standards.** Systems where the artifact format and the layering convention are open standards across vendors. **AGENTS.md** (Linux Foundation, December 2025) is now in over 60,000 GitHub repositories; Lulla et al. (2026) report −28.64% wall-clock and −16.58% tokens with no quality loss after adding an AGENTS.md scaffold. **MCP** (Anthropic, 2024) has become the cross-vendor standard with thousands of public servers and substantial enterprise adoption. **Claude Agent Skills**, **Cursor Rules**, **GitHub Copilot custom instructions**, **Windsurf rules**, **Continue.dev rules**, **Zed AI rules**, **Replit `replit.md`** all converge on the same pattern: a git-tracked markdown artifact attached to a workspace, with an MCP-style tool layer for actions. Convergence across vendors is the strongest evidence the architecture is real rather than a single vendor's local optimum.

The four clusters do not partition the corpus — many systems sit between two clusters — but they capture the architectural variation. Vertical-bundle vendors (Harvey for legal, Hippocratic AI for healthcare, Sierra for customer experience) sit between *open standards* and *production hybrid*: the bundle is the commercial unit; the underlying model is mostly the same one a competitor would use.

One result from the orchestration literature bounds how strongly any of these clusters can be read as evidence for multi-agent architectures specifically. Tran & Kiela (2026) report that single-agent LLMs match or beat multi-agent systems on multi-hop reasoning when thinking-token budgets are matched; the implication is that observed maturity gaps on S5 (orchestration) may reflect the rarity of governed topology *evolution* and the conflation of agent-count with compute-budget rather than a structural deficit of multi-agent designs. The orchestration cluster is therefore better read as evidence that production has converged on flat agent topologies and on tool-mediated rather than role-mediated decomposition, not as evidence that orchestration is the binding maturity constraint.

## 8. The two-loop design space

The composite-two-loop systems sit in a 3×3 matrix indexed by gate type on each loop. Thirteen research systems satisfy the strict criterion, with two production exemplars (Sierra Agent OS 2.0, Cognition Devin) included on the basis of vendor documentation as primary evidence and explicitly flagged.

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillRL, AlphaEvolve, ADAS, DGM[^dgm-dual], Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, Sierra OS 2.0†, Cognition Devin† | MAE\*, MetaGen\*, MetaReflection\*, CLIN\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in surveyed corpus]** | *(none)* |
| **Loop-1 None** | ExpeL (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repo\*, DSPy\*, TextGrad\* | Self-Refine\*, ReAct\*, Mem0\* |

*Asterisks fail at least one composite-two-loop criterion; included for contrast.* † Industry exemplar evaluated using vendor documentation as primary evidence.

[^dgm-dual]: DGM operates in both Auto×Auto (primary archive-based evolution) and Auto×Human (sandboxed code-modification review) modes depending on deployment configuration; we list it once in the dominant cell.

The matrix has three populated cells of interest. **[Auto × Auto]** is most populated (eleven systems). Every member has a machine-evaluated decision criterion on both loops. **[Auto × Human]** is the production-viable cell — Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. **[None × Auto]** holds the governance-first prompts-as-code systems. Three cells are empty for distinct reasons. **[Human × Auto]** is empty by engineering logic; if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping), but no published example exists. **[Human × Human]** is empty in the surveyed corpus; a candidate occupant would be a reviewer-authored-and-reviewer-promoted artifact pipeline targeting solo and small-team workflows where the marginal cost of a bad auto-merge exceeds the marginal cost of human latency — no public example was found during the May 2026 survey window. **[Human × None]** is structurally improbable: a system that requires human authorship on Loop 1 but has no Loop 2 at all collapses to "engineer-edits-a-config" and is not patch-plastic in the sense of §3.

The **[None × Auto-gated]** cell holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 — eval-gated CI blocks promotion on regression — but no Loop 1 in the patch-plastic sense, because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative precisely because it shows what survives when only the outer loop is automated.

Two cross-cutting findings sharpen the picture. **Noise reduction via batching is largely absent in the surveyed auto-gated systems**: every auto-gated system in [Auto × Auto] and [Auto × Human] fires at $n = 1$ per generation step, absorbing estimator noise statistically via the per-edit gate rather than aggregating evidence across multiple candidate edits. Multi-sample agreement filters (accept only when $k$ independent dreams or trajectories converge on the same proposal) are a tractable design dimension that no surveyed system has formalised; the noise-reduction behaviour of such a filter is qualitatively different from mini-batch averaging — false-accept probability shrinks roughly as $p^k$ rather than variance shrinking as $1/k$ — and the two should not be conflated. **Multi-layer hierarchies are under-explored**: only AlphaEvolve demonstrates explicit depth in the auto-gated cluster, via the cascade evaluator and MAP-Elites archive. The other twelve composite-two-loop systems treat their artifact pool as flat. Adding a STACK-style intermediate layer to NanoResearch or a multi-archetype scope to Anthropic's skills repository is a tractable engineering direction.

## 9. The empty corner

Four properties define what we call **enterprise full-auto**:

- (a) **Auto-gated Loop 1** — the commit criterion is an algorithmic threshold.
- (b) **Multi-tenant cross-org promotion** — Loop 2 routes artifacts between organisations, not just within one.
- (c) **Versioned lineage with RBAC** — promoted artifacts carry semantic versions, audit trails, and access-control policies.
- (d) **Rollback** — a bad promotion can be reverted without redeploy.

No surveyed system has all four. Closest approaches partition the requirements: **AlphaEvolve** has (a) and partial (b) within a single organisation; **NanoResearch** has (a) at the research level; **SkillForge** has (a) and (b) within one enterprise, partial (c) via VFS commits, undocumented (d); **Sierra Agent OS 2.0** has (b) and partial (a); **Vellum / Braintrust / LangSmith Hub** have (c) and (d) explicitly but no (a) or (b) in the strict sense. No surveyed system combines (b), (c), and (d) under any gate type — the cross-organisational governance triad is itself unfilled, independently of whether Loop 1 is auto-gated.

The empty corner is concrete in ML terms: a *DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer*. Differential-privacy federated averaging (DP-FedAvg) is the closest analogue in the federated-learning literature — gradient updates aggregated across distributed shards with privacy-preserving noise and an aggregation gate. At the scaffold layer this would mean: per-tenant artifact pools with tenant-tagged provenance, aggregation across tenants with operator-tunable privacy bounds, an automated eval gate (held-out task suite per tenant) blocking promotion when patch loss does not decrease, versioned lineage with RBAC carrying tenant access policies forward through the promotion, and a rollback envelope on every promoted artifact. Naming the corner converts a vague gap into a specific four-property audit criterion; the implementor's safety requirements are deferred to follow-on practitioner work. It is no longer "no system closes both loops" — too coarse — but a specific four-property combination that the survey can audit any future system against.

Whether this corner *should* be filled is deployment-dependent. In safety-critical domains — medical decision support, legal advice, financial advice — reviewer-judgment gates may be a design feature rather than a defect, and the human latency is the point. The narrower survey claim is what matters: no public system currently combines automated local scaffold evolution with governed cross-organisation promotion, versioned lineage with RBAC, and rollback. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. The shortest demonstrable path appears to build on AlphaEvolve's cascade evaluator + MAP-Elites archive, extending federation from within-DeepMind multi-target to cross-customer multi-tenant — but the architectural surface, not the timeline, is what this paper claims.

### 9.1 Patch-completeness as an operational hypothesis

The two-tier architecture also raises a measurable question about the meaning of "general" capability in production. We define **patch-completeness** as a testable operational condition rather than a philosophical claim about generality:

> A model–scaffold composite is *(r, n, d)-patch-complete* for a deployment patch $D$ when its residual error rate on a stationary patch eval suite of size $n$ stays at or below $r$ over a deployment window of $d$ days.

This definition makes patch-completeness an empirical property of a specific deployment and a specific eval, not of a system in general. It is *not* a claim that any deployed system is patch-complete in the colloquial sense, nor that a patch-complete system in this sense is intelligent in any global sense. The values of $r$, $n$, and $d$ depend on the patch: a coding agent inside one repository, a legal agent inside one firm's due-diligence workflow, or a support agent on one product surface each implies its own choice.

We are not aware of any surveyed system that has formally demonstrated $(r, n, d)$-patch-completeness for a fixed $r$, $n$, $d$ with held-out evaluation and a stationary patch over a non-trivial $d$. The framework predicts such demonstrations should appear in narrow production verticals — a coding agent confined to one repository with stable conventions, a legal agent confined to a stable due-diligence workflow — once eval discipline catches up with deployment scope. The governance question is then operational: at what residual rate $r$ and over what window $d$ is local competence load-bearing enough to require governance attention even before global robustness is established? §10 catalogues the failure surface that the answer would have to account for.

## 10. A new failure surface

Patch-plasticity introduces failure modes weight-only systems do not have. We name them here; the full taxonomy (nine categories A–I with severity ratings and counter-principles P1–P8) is deferred to follow-on practitioner work.

**Scaffold bloat** is the dominant near-term risk. IFScale (Jaroslawicz et al., 2025) reports latency growing roughly 35× for one reasoning model (o4-mini, 12.4s → 436s) as instruction count scales from 10 to 250, and the best-performing frontier model in that benchmark (Gemini 2.5 Pro) drops to 68% accuracy at 500 instructions; weaker models degrade further (GPT-4o to 15%). The result is a 2025 snapshot, and a 2026 follow-up using a later model generation reports the accuracy degradation softening substantially on the same task family, so the precise numerical collapse is model-generation-dependent; the underlying mechanism (lost-in-the-middle, instruction interference; Liu et al., 2023) persists, and scaffolds that accumulate hundreds of unpruned instructions remain exposed even when individual frontier-model scaling improves. **Poisoned memory** is the dominant security risk: PoisonedRAG (Zou et al., 2024) reports 90%+ attack success rate against standard RAG; Memory Control Flow Attacks (Xu et al., 2026) report >90% vulnerability across major LLM agent frameworks. **Prompt injection via tools and MCP** is the dominant cross-vendor attack surface, with CVE-2025-54136 ("MCPoison") demonstrating a public MCP-server compromise pathway. **Eval fragility** is the dominant ecosystem risk: the Leaderboard Illusion (Singh et al., 2025) documents up to 112% relative performance gains on the Chatbot Arena distribution under differential training-data access — a structural overfitting pathway, not benchmark error; eval suites are themselves patch-plastic artifacts and must survive Goodhart's Law. **Coordination failures** in multi-agent systems are documented in MAST (Cemri et al., 2025) — 14 distinct failure modes with $\kappa = 0.88$ agreement, dominantly role-confusion / context-loss / coordination rather than prompt quality. **Overfitting to patch** is structural: scaffolds tuned to a deployment over-fit it, and the framework predicts but does not measure how badly. **Plasticity loss at the scaffold level** is the slow-moving risk: context rot, instruction conflict, memory pollution, and tool-version drift produce a scaffold-level analogue of weight-level plasticity loss (Dohare et al. 2024, Lyle et al. 2023). Scaffolds age; a six-month-old `CLAUDE.md` is often worse than a clean rebuild, and no surveyed system treats pruning or expiration as a first-class operation.

Taken together: the patch-plastic surface is real, quantified by 2024–2026 work, and largely unmitigated in production. Follow-on practitioner work walks the mitigation principles in detail.

## 11. Conclusion

The field did not wait for frontier weights to become perfectly reliable. It built a second learning system around them. That second system is made of markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, and rollback buttons. It looks like engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights.

The mechanisms were already there. A Claude Skill has been a procedural weight since Anthropic shipped progressive disclosure. A Cursor Rule has been a local parameter since `.cursor/rules/` became a directory. A PR against `agents.md` has been a promotion gate since the Linux Foundation took stewardship. What changed in 2025–2026 is that the *combination* — these substrates wrapping a frozen frontier model and updating from deployment signal — became dense enough across vendors that the convergence reads as architecture rather than coincidence. Once you name it, the empty corners of the design space become concrete engineering targets. The most consequential one is enterprise full-auto: Auto-gated Loop 1 plus governed multi-tenant cross-org Loop 2, with versioned lineage, RBAC, and rollback. In ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer. Whether it should be filled is deployment-dependent; that it has not been is the survey's headline finding.

The five surveyed absences of §6.3 — failure-triggered memory rare in production, cross-customer skill promotion absent, memory versioning unsolved, scaffold-level curriculum unspecified, Loop-2 overfitting detection missing — are each a Paper-4 target. None of these is novel as a complaint; each is novel as a *gap the architecture makes visible*. If $(r, n, d)$-patch-complete systems begin to appear in narrow production verticals — as §9.1's operational definition makes possible to test — then scaffold governance becomes load-bearing before global robustness is demonstrated.

The deepest connection — back to Paper 2 — is structural. Patch-plasticity is plastic because residual errors are clustered; if mode discovery were not slow (Postulate 1 in *Architecture of Errors*), patches would not generalise across deployments and the architecture would collapse. The survey is consistent with the postulate at the system level: deployments do generalise enough of the patch to make scaffold investment pay off. Whether this remains true at agentic, scientific, and long-horizon scales is the empirical test the next paper should design.

Practical generality therefore arrives locally first: not as a universal mind, but as model–scaffold systems whose competence is fitted to bounded worlds and is in principle measurable through the $(r, n, d)$-patch-completeness condition of §9.1. The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation. The mechanisms were already there — markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, rollback buttons — but they read as engineering clutter until viewed as a scaffold parameter vector under update. Then the clutter resolves into architecture: production LLMs learn locally, outside the weights, because under deployment-time constraints that is where patch-specific adaptation can be safely placed and audited.

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
| EvolveR | 2025 | Integrated | Auto | Auto | 3 | T2 (arXiv:2510.16079) | Experience-driven lifecycle: episodic memory + skill consolidation + cross-task transfer; accepted at ICML 2026 |
| Voyager | 2023 | Integrated | Auto | Auto | 4 | T2 (arXiv:2305.16291) | Foundational skill-library result; 3.3× items, 15.3× tech-tree milestones |
| AGENTS.md | 2025 | S1 Instructions | n/a | n/a | 2 | T3/T4 (agents.md) | Cross-vendor standard; 60k+ repos; Lulla 2026 measures −28.6% runtime |
| Claude Code CLAUDE.md | 2025 | S1 Instructions | n/a | n/a | 4 | T3/T4 (docs.anthropic.com) | Four scoping levels including org-IT policy + auto-memory layer; ceiling for S1 |
| Cursor Rules | 2024 | S1 Instructions | n/a | n/a | 3 | T3/T4 (\url{docs.cursor.com/rules}) | `.cursor/rules/*.mdc` multi-scope + MCP attach; git-tracked |
| Anthropic Agent Skills | 2025 | S2 Skills | n/a | Human | 3 | T3 (\url{anthropic.com/engineering}) | Progressive disclosure spec; LangChain replication 29%→95% pass-rate |
| SAGE | 2025 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2512.17102) | +8.9% SGC, 26% fewer steps, 59% fewer tokens on AppWorld |
| COSPLAY | 2026 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2604.20987) | Co-evolving decision agent + learnable skill bank; skills discovered from rollouts form a structured skill library for long-horizon tasks |
| Reflexion | 2023 | S3 Memory | Auto | n/a | 4 | T1 (NeurIPS 2023; arXiv:2303.11366) | Canonical failure-triggered episodic memory; +8% HotpotQA |
| Generative Agents | 2023 | S3 Memory | Auto | n/a | 4 | T1 (UIST 2023; arXiv:2304.03442) | Reflection + importance memory primitive |
| Cuadros et al. governed collaborative memory | 2026 | S3 Memory | Auto | Auto | 5 | T2 (arXiv:2605.04264) | Only surveyed memory system with full provenance + versioning + correction |
| MCP | 2024 | S4 Tools | n/a | n/a | 5 | T3 (modelcontextprotocol.io) | Cross-vendor standard; thousands of public servers; substantial enterprise adoption |
| Harvey | 2026 | S4 Tools | n/a | n/a | 5 | T3 (harvey.ai) | 400K queries/day; 18,000+ workflows; 200+ legal data sources |
| Hippocratic AI | 2026 | S4 Tools | n/a | n/a | 5 | T3 (hippocraticai.com) | \$3.5B valuation; 30% readmission reduction; 360% care-capacity boost |
| Multi-Agent Evolve (MAE) | 2025 | S5 Orchestration | Auto | n/a | 4 | T2 (arXiv:2510.23595) | RL co-evolution of Proposer/Solver/Judge population; one loop closed, no Loop-2 cross-context promotion |
| Cemri et al. (AG2) | 2025 | S5 Orchestration | n/a | n/a | 3 | T2 (arXiv:2503.13657) | Specialisation +4.5 pp on GSM-Plus ($p = 0.03$); MAST 14 failure modes |
| Braintrust | 2024 | S6 Governance | n/a | Auto | 5 | T3 (braintrust.dev) | Prompts-as-code: immutable commits, eval-gated PR merge, sub-5 min rollback |
| Vellum | 2024 | S6 Governance | n/a | Auto | 5 | T3 (vellum.ai) | Same governance pattern; production deployment with eval thresholds |
| LangSmith Hub | 2024 | S6 Governance | n/a | Auto | 5 | T3 (\url{smith.langchain.com}) | Prompt repository with environment promotion and eval blocking |
| Self-Refine\* | 2023 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2303.17651) | Fails the patch-plastic discriminator: in-context iteration only |
| Mem0\* | 2024 | (contrast) | n/a | n/a | 2 | T3/T4 (mem0.ai) | Fails Loop 2: per-user memory with no cross-context promotion path |
| Tran \& Kiela\* | 2026 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2604.02460) | Single-agent baselines match or beat multi-agent systems under matched thinking-token budgets — orthogonal finding constraining S5 claims |

```{=latex}
\endgroup
```

*Asterisks mark contrast systems included for definitional clarity.*

---

## Appendix B. Data appendix

**Corpus size.** The supplementary file `p3_master_scores.csv` contains approximately 130 unique LLM systems scored across the six substrates. Because a system can be scored on multiple substrates, the row count in the CSV exceeds the unique-system count; the system count cited throughout §§5–8 refers to unique systems.

**Core / contrast split.** Approximately 90 unique systems satisfy the patch-plastic discriminator (score ≥ 3 on at least one substrate) and form the **core corpus**. The remaining ≈ 38 systems form the **contrast corpus** — commonly described as agentic or self-improving in public discourse but failing at least one discriminator. Headline statistics quote the core corpus; the contrast set is preserved with asterisks for definitional clarity. Appendix D enumerates the contrast set.

**Evidence-tier distribution.** Of the core corpus, approximately one quarter carry T1 (peer-reviewed) evidence, roughly half carry T2 (arXiv preprint) evidence, and the remainder carry T3 (production claim with metrics) or T4 (open-source artifact) evidence as the primary tier. T5 (industry-blog/interview) is admissible only when corroborated by a higher tier elsewhere. The per-row evidence flag in Appendix A and in the CSV makes the propagation auditable.

**Sensitivity analysis (composite two-loop count).** The strict count of thirteen research systems satisfying the composite-two-loop criterion changes under two natural relaxations of the gate definition: under (a) — counting any of versioning, lineage, or rollback as Loop-2 governance — the count rises to approximately seventeen by re-admitting MAE, MetaGen, MetaReflection, and CLIN; under (b) — admitting session signal that updates optimizer state without persisting an artifact distinct from optimiser state — the count rises to approximately fifteen by re-admitting DSPy and TextGrad. The qualitative findings (Auto×Auto well-populated, [Human × Human] and [Human × Auto] empty in the surveyed corpus, governance-first cluster in [None × Auto], enterprise full-auto cell empty) survive both relaxations.

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

The §3.2 formalism collapses production gates into a single per-edit gate $G_t$ that estimates the directional loss change $\widehat{\Delta}_{z_t} L_D$. In practice, surveyed gates instantiate that abstraction in several distinct ways, and some are better read as *proposal-pruning* steps that precede the per-edit gate rather than as direct $\widehat{\Delta}$ estimators. The table below maps each surveyed gate family to its role in the formalism.

| Gate family | What it estimates | Slot in §3.2 | Representative systems |
|---|---|---|---|
| **Eval-cascade** | $\widehat{\Delta} L_D$ on a held-out task suite; cascaded through cheap-to-expensive evaluators | Per-edit gate $G_t$ | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| **RL-threshold** | Reward improvement vs. a deployment threshold (e.g., task-category accuracy < 0.4 triggers replacement) | Per-edit gate $G_t$ | SkillRL, SAGE, EvolveR |
| **LLM-judge with calibration** | Pairwise- or rubric-scored quality, calibrated against human agreement (LLM-judge ≥ 90% agreement, etc.) | Per-edit gate $G_t$ | SkillForge (Loop 1), CASCADE (consolidation gate) |
| **Surrogate verifier** | Symbolic, learned, or test-case verifier producing a pass/fail or graded score | Per-edit gate $G_t$ | DGM (test-pass on sandboxed code), Voyager (in-game verifier) |
| **Reviewer-judgment** | Human credit assignment via PR review or expert sign-off; no algorithmic threshold | Per-edit gate $G_t$ (human-instantiated) | SkillForge (Loop 2), Sierra Agent OS 2.0, Anthropic skills repo |
| **Semantic-merge** | Whether a candidate is semantically duplicated by, or compatible with, existing scaffold artifacts | *Proposal-pruning* preceding $G_t$ | NanoResearch (orchestrator semantic-merge step) |
| **MAP-Elites / archive selection** | Whether a candidate populates a previously unfilled cell in a behavior-diversity archive | *Proposal-pruning* preceding $G_t$ | AlphaEvolve (archive), ADAS (meta-agent search) |
| **Multi-sample agreement** | Whether $k$ independent proposals or evaluations converge on the same direction; false-accept rate decays as $p^k$ rather than variance shrinking as $1/k$ | *Aggregation filter* (qualitatively distinct from mini-batch averaging) | Under-explored in the surveyed corpus |

The eval-cascade, RL-threshold, LLM-judge, surrogate-verifier, and reviewer-judgment families directly populate the per-edit gate $G_t$ of §3.2 and inherit its descent guarantees (under Assumptions A1–A5). The semantic-merge and archive-selection families are not estimators of $\widehat{\Delta} L_D$ — they constrain the proposal distribution $Q_t$ rather than judging individual candidate quality, and the descent argument therefore applies to the composition (proposal-pruning ∘ per-edit gate) rather than to either step alone. Multi-sample agreement filters are not surveyed in production form; they are listed for completeness because they are the correct ML analogue for "wait for $k$ pieces of evidence before accepting an edit," which is *not* the same operation as mini-batch averaging and should not be conflated with it in scaffold-descent analyses.

---

## Appendix D. Contrast set

The contrast corpus of approximately 38 systems is included to make the patch-plastic discriminator audit-able. Each system here is commonly described in public discourse as agentic, self-improving, or scaffolded, but fails at least one discriminator. Representative entries:

| System | Year | Primary discriminator failure | Brief reason |
|---|---|---|---|
| Self-Refine (Madaan et al.) | 2023 | No persistent artifact | In-context iteration only; no scaffold delta survives the session |
| ReAct (Yao et al.) | 2023 | No persistent artifact | Thought-act-observe loop is intra-session; no Loop 1 persistence |
| Reflexion (Shinn et al.) | 2023 | No Loop 2 (Loop 1 only) | Failure-triggered episodic memory persists per-agent but no cross-context promotion mechanism |
| Generative Agents (Park et al.) | 2023 | No Loop 2 | Reflection + importance memory primitive; per-agent scope |
| AutoManual (Chen et al.) | 2024 | Passes (in core corpus) | Listed here only to flag boundary case; see Appendix A |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks, not in-deployment failures |
| Mem0 (vanilla deployment) | 2024 | No Loop 2 | Per-user memory store with no cross-context promotion path |
| Zep | 2024 | No Loop 2 | Temporal knowledge graph per agent/session, no promotion gate |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence; no inter-tenant promotion |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence; no inter-tenant promotion |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent; no promotion mechanism |
| DSPy | 2023 | No artifact distinct from optimiser state | Prompt-template optimization but optimised templates are optimiser state, not persisted scaffold |
| TextGrad | 2024 | No artifact distinct from optimiser state | Same boundary case as DSPy |
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
| ACE (Zhang et al.) | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook; per-deployment |
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

## References

AGENTS.md. (2025). AGENTS.md: A cross-vendor open standard for agent instructions. Linux Foundation. <https://agents.md>

Agashe, S., Han, J., Gan, S., Yang, J., Li, A., & Wang, X. E. (2024). Agent S: An open agentic framework that uses computers like a human. *arXiv preprint arXiv:2410.08164*.

Agashe, S., et al. (2025). Agent S2: A compositional generalist-specialist framework for computer use agents. *arXiv preprint arXiv:2504.00906*.

Anthropic. (2024). Model Context Protocol specification. <https://modelcontextprotocol.io>

Arbuzov, M. L., Bei, S., Dong, Z., Kalaev, D., & Shvets, A. A. (2025). Beyond exponential decay: Rethinking error accumulation in large language models. *arXiv preprint arXiv:2505.24187*.

Arbuzov, M. L., Shvets, A. A., & Bei, S. (2026). The architecture of errors: Logarithmic mode discovery and polylogarithmic intervention budgets for long-context LLM reliability. *arXiv preprint* (forthcoming).

Cemri, M., et al. (2025). Why do multi-agent LLM systems fail? *arXiv preprint arXiv:2503.13657*. Introduces the MAST taxonomy.

Chen, M., Li, Y., Yang, Y., Yu, S., Lin, B., & He, X. (2024). AutoManual: Constructing instruction manuals by LLM agents via interactive environmental learning. *NeurIPS 2024*. arXiv:2405.16247.

Chen, Y., et al. (2025). Multi-Agent Evolve: LLM self-improve through co-evolution. *arXiv preprint arXiv:2510.23595*.

Cuadros, D. F., Maiga, A.-A., Meskhidze, H., & Curtis-Trudel, A. (2026). Governed collaborative memory as artificial selection in LLM-based multi-agent systems. *arXiv preprint arXiv:2605.04264*.

Dohare, S., et al. (2024). Loss of plasticity in deep continual learning. *Nature*, 632(8026), 768–774.

Du, P. (2026). Memory for autonomous LLM agents: Mechanisms, evaluation, and emerging frontiers. *arXiv preprint arXiv:2603.07670*.

Fang, J., Peng, Y., Zhang, X., et al. (2025). A comprehensive survey of self-evolving AI agents: A new paradigm bridging foundation models and lifelong agentic systems. *arXiv preprint arXiv:2508.07407*.

Fawzi, A., Balog, M., Huang, A., et al. (2022). Discovering faster matrix multiplication algorithms with reinforcement learning. *Nature*, 610(7930), 47–53. (DeepMind AlphaTensor.)

Gao, H.-a., Geng, J., Hua, W., et al. (2026). A survey of self-evolving agents: What, when, how, and where to evolve on the path to artificial super intelligence. *Transactions on Machine Learning Research*. arXiv:2507.21046.

Harada, K., et al. (2025). Curse of instructions: Large language models cannot follow multiple instructions at once. *ICLR 2025*. <https://openreview.net/forum?id=R6q67CDBCH>

Harvey. (2026). Harvey product overview. <https://www.harvey.ai>

Hippocratic AI. (2026). Polaris clinical outcome evidence. <https://www.hippocraticai.com>

Hu, S., Lu, C., & Clune, J. (2024). Automated design of agentic systems (ADAS). *arXiv preprint arXiv:2408.08435*.

Huang, X., et al. (2025). CASCADE: Cumulative agentic skill creation through autonomous development and evolution. *arXiv preprint arXiv:2512.23880*.

Jaroslawicz, D., et al. (2025). How many instructions can LLMs follow at once? *arXiv preprint arXiv:2507.11538*. Introduces the IFScale benchmark.

Jiang, P., Lin, J., Shi, Z., et al. (2025). Adaptation of agentic AI: A survey of post-training, memory, and skills. *arXiv preprint arXiv:2512.16301*.

Kirk, R., Mediratta, I., Nalmpantis, C., et al. (2024). Understanding the effects of RLHF on LLM generalisation and diversity. *ICLR 2024*. arXiv:2310.06452.

Liu, N. F., et al. (2023). Lost in the middle: How language models use long contexts. *TACL*. arXiv:2307.03172.

Liu, X., et al. (2026). SkillForge: Forging domain-specific, self-evolving agent skills in cloud technical support. *arXiv preprint arXiv:2604.08618*. Accepted at ACM SIGIR 2026 Industry Track.

Lulla, J. L., et al. (2026). On the impact of AGENTS.md files on the efficiency of AI coding agents. *arXiv preprint arXiv:2601.20404*.

Lyle, C., Zheng, Z., Nikishin, E., Avila Pires, B., Pascanu, R., & Dabney, W. (2023). Understanding plasticity in neural networks. *ICML 2023* (oral). arXiv:2303.01486.

Madaan, A., et al. (2023). Self-Refine: Iterative refinement with self-feedback. *NeurIPS 2023*. arXiv:2303.17651.

Newell, A. (1990). *Unified theories of cognition*. Harvard University Press.

Novikov, A., et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. *arXiv preprint arXiv:2506.13131*. (DeepMind.)

Padmakumar, V., & He, H. (2023). Does writing with language models reduce content diversity? *arXiv preprint arXiv:2309.05196*.

Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *UIST 2023*. arXiv:2304.03442.

Press, O., et al. (2022). Measuring and narrowing the compositionality gap in language models. *arXiv preprint arXiv:2210.03350*.

Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*. arXiv:2303.11366.

Sierra. (2024). Sierra Agent OS. <https://sierra.ai>

Sierra. (2025). Agent OS 2.0: From answers to memory and action. <https://sierra.ai/blog/agent-os-2-0>

Singh, S., et al. (2025). The leaderboard illusion. *arXiv preprint arXiv:2504.20879*.

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive architectures for language agents (CoALA). *Transactions on Machine Learning Research*. arXiv:2309.02427.

Tan, W., et al. (2024). Cradle: Empowering foundation agents towards general computer control. *arXiv preprint arXiv:2403.03186*.

Tran, D., & Kiela, D. (2026). Single-agent LLMs outperform multi-agent systems on multi-hop reasoning under equal thinking token budgets. *arXiv preprint arXiv:2604.02460*.

Wang, G., et al. (2023). Voyager: An open-ended embodied agent with large language models. *arXiv preprint arXiv:2305.16291*.

Wang, J., et al. (2025). Reinforcement learning for self-improving agent with skill library. *arXiv preprint arXiv:2512.17102*. Method named SAGE (Skill Augmented GRPO for self-Evolution).

Wang, X., et al. (2026). AutoAgent: Evolving cognition and elastic memory orchestration for adaptive agents. *arXiv preprint arXiv:2603.09716*.

Wang, Z., et al. (2025). Mobile-Agent-E: Self-evolving mobile assistant for complex tasks. *arXiv preprint arXiv:2501.11733*.

Wu, R., et al. (2025). EvolveR: Self-evolving LLM agents through an experience-driven lifecycle. *arXiv preprint arXiv:2510.16079*. Accepted at ICML 2026.

Wu, X., et al. (2026). Co-evolving LLM decision and skill bank agents for long-horizon tasks. *arXiv preprint arXiv:2604.20987*. Framework named COSPLAY.

Wu, Z., et al. (2024). OS-Copilot: Towards generalist computer agents with self-improvement. *arXiv preprint arXiv:2402.07456*.

Xia, P., et al. (2026). SkillRL: Evolving agents via recursive skill-augmented reinforcement learning. *arXiv preprint arXiv:2602.08234*.

Xu, Jinhang, et al. (2026). NanoResearch: Co-evolving skills, memory, and policy for personalized research automation. *arXiv preprint arXiv:2605.10813*.

Xu, Zhenlin, et al. (2026). From storage to steering: Memory control flow attacks on LLM agents. *arXiv preprint arXiv:2603.15125*. Introduces the MCFA attack class.

Zhang, H., et al. (2026). CoEvoSkills: Self-evolving agent skills via co-evolutionary verification. *arXiv preprint arXiv:2604.01687*.

Zhang, J., et al. (2025). Darwin Gödel machine: Open-ended evolution of self-improving agents. *arXiv preprint arXiv:2505.22954*. (Body text refers to this as DGM.)

Zhang, Q., Hu, C., Upasani, S., et al. (2025). Agentic Context Engineering: Evolving contexts for self-improving language models. *arXiv preprint arXiv:2510.04618*.

Zhou, Y., Shu, W., Su, Y., et al. (2026). A comprehensive survey on agent skills: Taxonomy, techniques, and applications. *arXiv preprint arXiv:2605.07358*.

Zou, W., et al. (2024). PoisonedRAG: Knowledge corruption attacks to retrieval-augmented generation of large language models. *arXiv preprint arXiv:2402.07867*. Accepted at USENIX Security 2025.
