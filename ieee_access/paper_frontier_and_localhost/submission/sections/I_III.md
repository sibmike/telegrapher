## Introduction {#sec:intro}

The standard mental model of a system built on a large language model (LLM) is the model. Pre-training fixes the weights, fine-tuning nudges them, and deployment wraps a thin layer of prompts and tools around the result. Production in 2025 and 2026 has stopped behaving this way. Frontier weights change on a cycle of months. The systems built on them change daily, in instruction files checked into repositories, in memories that persist across sessions, in skills loaded on demand, in registered tools, in evaluation suites that block a merge, in agent topologies, and in pull-request gates on shared rule repositories. A growing share of the adaptation that makes a deployed system reliable now happens outside the weights, in a fast-changing local scaffold wrapped around a slow-changing frontier model.

Read one at a time, these artifacts look like unrelated engineering. A skill file is a procedure the model did not have. A repository rule is a local parameter for one project's conventions. A retrieval connector is memory access specific to one patch of work. A tool registry provisions a capability the base model cannot reach. A pull-request review against a shared rule repository is a promotion gate. An evaluation suite that blocks a merge is a validation check before promotion. Read together, they are one adaptation surface, and the question this survey asks is what optimization discipline that surface needs. The answer we find is that the field has built an external adaptation layer for LLMs but not the optimizer that should govern it. Most deployments maintain the layer as patchwork: a failure happens, someone adds a rule, the pile grows, nobody knows which addition helped, and fixes leak into contexts that never validated them.

This article makes five contributions.

1. It states the loop that turns patchwork into optimization in plain language, then as a gated update rule, with the five conditions under which the rule is a mechanism rather than a metaphor (Section REF(sec:loop)).
2. It introduces a classification of the feedback signal available to that loop, from an exact check to a delayed and sparse reward, and shows that the class fixes what the gate can be, which design-space cells are reachable, and which failure dominates (Section REF(sec:signal)).
3. It surveys 256 production and research systems from January 2023 to October 2026, scores each on six substrates with a published rubric and a released score table, and reports where maturity is uneven (Sections REF(sec:method) and REF(sec:findings)).
4. It places every system that closes both loops in a design space indexed by gate type and reads the empty cells structurally (Section REF(sec:design)), and it reads the convergence of five research families on the same loop as evidence that the architecture is real rather than one group's local optimum (Section REF(sec:families)).
5. It names, as a four-property audit criterion, the architecture no surveyed system instantiates, namely governed cross-tenant scaffold optimization with versioned lineage, access control, and rollback, and it maps the failure surface that the gap leaves open (Sections REF(sec:gap) and REF(sec:failure)).

The survey runs no experiments. Its evidence is the published behavior of the systems it scores, the released score table, and the audit of every absolute claim against the October-2026 literature (Supplementary Material).

## Why adaptation lives outside the weights {#sec:why}

### Breadth in the weights, depth in the scaffold

Frontier training optimizes for breadth. The weights are tuned to generalize across millions of unseen deployments, and the training objective smooths over exactly the things one deployment cares about: local naming conventions, contradictory tenant preferences, rare workflow-specific failures. Reinforcement learning from human feedback reduces output diversity and homogenizes preferred style across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data rewards patterns that generalize across the annotator pool rather than patterns specific to any one deployment. The frontier model is therefore trained in a way that systematically disfavors encoding one tenant's idiosyncrasies as preferred behavior. Tiwari et al. [@tiwari2026fastandslow] reach the same place from the optimization side: in-context adaptation is cheap and rapid but capacity-bounded, while in-weights adaptation is expressive but induces forgetting and loss of plasticity, so a two-timescale system needs a cheap outer layer that absorbs what context can carry.

Production reliability, by contrast, is achieved in depth. Inside one deployment, reliability is determined by what global training had to smooth away. Encoding every deployment in the weights is ruled out three times over: per-tenant fine-tuning multiplies the training, evaluation, and serving lifecycle by the number of deployments; weights ship quarterly at best while the deployment wants daily updates; and overfitting the weights to one tenant degrades adjacent tenants whose preferences contradict. Per-tenant adapters, distilled models, and learned routing each absorb some residual in principle. In practice the scaffold dominates, because it is the one substrate that is cheap, inspectable, reversible, tenant-scoped, and updatable on a daily cadence at once.

### Why the scaffold is the right architecture, not a workaround: three papers

The case that learning belongs outside the weights does not rest on cost alone. It is the conclusion of three papers, of which this is the third. The first, *Beyond Exponential Decay* [@arbuzov2025beyond], asks why long LLM outputs do not fail at the rate a uniform per-token error model predicts, and finds that reliability hinges on a sparse set of key decisions, under a tenth of tokens by the available long-context measurement, rather than on uniform per-token accuracy. The second, *The Architecture of Errors* [@arbuzov2026architecture], asks what those key-decision failures look like inside a bounded deployment and finds that they cluster into a finite catalogue of recurring modes whose size grows only slowly with the number of observed failures, so a small, targeted budget of interventions covers the residual. Together they say where a deployment's errors are and that they are few enough to fix one at a time. This article asks where the fixes live. The answer the corpus gives is: in persistent artifacts outside the weights, which is where a small catalogue of recurring, tenant-specific modes can be addressed cheaply, inspected, and reversed. Once the loop that edits those artifacts is gated and scoped, the arrangement is not a patch on an inadequate model. It is the architecture that the error structure of the first two papers calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization.

### Three stages of scaffold maintenance

Three stages of scaffold maintenance recur across the corpus. They differ in how candidate updates are produced, whether credit assignment is explicit, and whether promotion is bounded by evidence. In the surveyed corpus, production deployments sit at Stage 1 or 2; the loop of Section REF(sec:loop) is Stage 3.

| Stage | Update mechanism | Credit assignment | Promotion discipline | Dominant failure |
|---|---|---|---|---|
| 1. Patchwork | Intuition-driven local edits | Implicit, ad hoc | None | Bloat |
| 2. Random artifact search | Many variants tried under an evaluation | Weak; the evaluation is the only signal | Evaluation-gated merge, no failure-to-coordinate tracing | Overfitting to the in-distribution patch |
| 3. Artifact-layer descent | Residual traced to a coordinate, then one edit | Explicit per failure mode | Bounded by evidence radius; reversible | (the discipline this article describes) |

Table II-1. Three stages of scaffold maintenance.

A patchwork loop becomes Stage 3 once the five conditions of Section REF(sec:loop) hold. The survey of Sections REF(sec:method) to REF(sec:design) asks which deployed systems meet which of them.

### Relation to existing surveys

Table REF(tab:II-2) places this survey against the surveys that cover neighboring ground. Existing surveys of self-evolving agents, agent memory, context engineering, skills, and harness design catalogue mechanisms by what they edit and when. None classifies systems by whether a feedback loop is closed, by whether the gate is algorithmic or human, or by the class of signal the gate receives; two carry a governance axis, and none a cross-organization promotion dimension. This survey classifies on those four axes and audits a named gap against them.

| Survey | Scope | Organizing axes | Loop closure | Gate type | Signal class | Governance |
|---|---|---|---|---|---|---|
| Gao et al. [@gao2026selfevolving] | self-evolving agents | what, when, how, where to evolve | partial | partial | no | no |
| Fang et al. [@fang2025comprehensive] | self-evolving agents | inputs, agent system, environment, optimizers | partial | no | no | no |
| Zhou et al. [@zhou2026selfevolvingcoding] | self-evolving coding agents (108 methods) | evolution target, timing, code signals | partial | partial | partial | partial (reversibility) |
| Ding et al. [@ding2026alwayson] | persistent-state agents (435 works) | authority, scope, mutability, provenance, recoverability | no | partial | no | yes (provenance, rollback) |
| Lin et al. [@lin2026memorysecurity] | memory security (~90 works) | lifecycle phases × security objectives | no | partial | no | yes (principal scoping, rollbackability) |
| Guo et al. [@guo2026harness] | agent system and harness design | six runtime responsibilities | partial | partial | partial | partial |
| Xia et al. [@xia2026harnessing] | skill-mediated agents (8 systems) | four responsibility layers, ten patterns | partial | no | no | partial |
| Ding et al. [@ding2026skilleval] | skill evaluation and evolution | four evolution paradigms × six benchmark classes | partial | partial | partial | partial |
| Mei et al. [@mei2025context] | context engineering (1,411 papers) | components × system implementations | no | no | no | no |
| This survey | 256 scaffold-adaptive systems | loop closure, gate type, signal class, governance | yes | yes | yes | yes (four-property audit) |

Table II-2. Related surveys and the axes they classify by ("partial": discussed but not a classification axis).

## The loop: artifact-layer descent {#sec:loop}

### The loop in plain language

The disciplined version of scaffold maintenance is one loop, run again and again over the life of a deployment. It does not react to single failures. As the deployment runs, it logs what went wrong: failed outputs, user corrections, rejected answers, evaluation regressions, tool-call errors. Reflecting over that record, it clusters the failures into recurring modes and takes up the ones that matter most, where a mode earns attention in proportion to how often it recurs and how badly it fails. For such a mode it locates the single scaffold coordinate responsible, which may be a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, or a misrouted agent edge, and it synthesizes one candidate edit to that coordinate. It measures whether the edit lowers the deployment's failure rate on its own recurring tasks, which we call the patch loss, and a gate accepts or rejects the edit on that measurement. An accepted edit stays in the scaffold; one that a later check shows made things worse is pruned or rolled back. Then comes the step most systems skip: the loop decides how far the edit should travel, promoting it to other deployments only as far as the evidence reaches. That limit is the edit's evidence radius. Fig. REF(fig:descent) draws the loop.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{fig1_descent_ieee}
\caption{Artifact-layer descent. Loop 1 turns a failure into a gated, persisted edit on one deployment's scaffold; Loop 2 promotes a validated edit to other deployments, only as far as its evidence radius supports.}
\label{fig:descent}
\end{figure*}
```

### Two loops, two knobs

Consider a concrete case. An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repository's instruction file. The edit is small and its scope is one project. The same engineer could promote the rule to a team-wide template, to the company's core instructions, or to a cross-tenant skill registry. The edit did not change; the scope did. And the gate that should let it through gets stricter at each step, because the loss it is tested against is now an average over more deployments, and a fix that helps one repository can hurt another.

Loop 1 is the local fix: a recurring failure produces a candidate edit, the edit is tested, and an accepted edit changes one deployment's scaffold. Loop 2 is the separate decision of whether that fix should be shared. The two loops turn different knobs. Loop 1 sets how much one accepted edit changes the local scaffold, the analogue of a step size. Loop 2 sets how many deployments the edit applies to, which does not change the step but changes the target: which average failure rate the scaffold is being tuned to reduce. The scopes nest, USER within PROJECT within STACK within TENANT within CORE, and each level has its own loss, the average failure rate over the deployments it contains (Fig. REF(fig:scope)). "Cross-tenant promotion" means reaching the TENANT or CORE level. This is why governance is not administrative overhead. It is the regularization that keeps a small fix from being aimed at the wrong target.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{Patch scope hierarchy. Each level's loss averages the deployments it contains. Loop 1 descends a USER or PROJECT loss; Loop 2 promotes upward; cross-tenant promotion means reaching TENANT or CORE.}
\label{fig:scope}
\end{figure}
```

### When the loop is an optimizer

The loop is an optimization process, rather than a description of good practice, when five conditions hold:

1. a measurable patch loss, such as a failure rate, a correction rate, or an evaluation score;
2. captured residuals, so that failures are logged rather than lost;
3. credit assignment, so that a failure can be traced, at least sometimes, to the scaffold coordinate that caused it;
4. a synthesized candidate edit to that coordinate; and
5. a gate that checks whether the edit lowers the loss before the edit is kept or promoted.

Write the patch loss of deployment $D$ as
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$
where $\theta_M$ are the frontier weights, fixed during deployment, $\theta_s$ is the scaffold, a structured object over the six substrate coordinates of Section REF(sec:method), and $\ell$ is an operational loss. A failure yields no analytic gradient. It yields a candidate edit $z_t$, proposed by reflection over the accumulated failure history in order of how often and how badly each mode fails. The gate accepts the edit when its noisy estimate of the change in loss clears a margin,
$$G_t(z_t) = 1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \le -\tau_t,$$
where $\Omega \ge 0$ penalizes the complexity of the edit and the breadth of its promotion and $\tau_t \ge 0$ is the required margin. An accepted edit is applied; a rejected one leaves the scaffold unchanged. Production systems implement this inequality without writing it: an evaluation blocks a merge on regression, a reviewer rejects a vague rule, a governance system holds a local artifact back until evidence accumulates.

Each loop has a gate, and we name three kinds. A gate is **Auto** when the decision is an algorithmic criterion: an evaluation score, a verifier, a reinforcement-learning threshold, or a language-model judge with a quantified agreement rate. It is **Human** when the decision is reviewer judgment. It is **None** when the loop is absent. These labels index the design space of Section REF(sec:design).

### Assumptions

The descent reading holds when (i) the frontier weights stay frozen while the scaffold adapts; (ii) each edit is a persistent, inspectable artifact rather than a transient prompt; (iii) the deployment exposes a loss that can be measured; (iv) the proposal process can, at least sometimes, trace a failure to the responsible coordinate; (v) the gate is a noisy estimator of whether an edit helps, not an oracle; and (vi) promotion widens an artifact's scope under a gate rather than averaging comparable updates the way weight-space federated learning does. Under these assumptions Appendix REF(app:formal) states a one-step descent inequality and an informal convergence proposition to a gate-stable scaffold. Where a condition fails, the same picture should be read as an analogy, and the survey marks which systems meet which conditions. Condition (iii) says the loss must be measurable; Section REF(sec:signal) asks what measures it.
