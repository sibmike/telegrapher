## Introduction {#sec:intro}

The standard mental model of a system built on a large language model (LLM) is the model. Pre-training fixes the weights, fine-tuning nudges them, and deployment wraps a thin layer of prompts and tools around the result. Production in 2025 and 2026 has stopped behaving this way. Frontier weights change on a cycle of months; the systems built on them change daily, in instruction files checked into repositories, memories that persist across sessions, skills loaded on demand, registered tools, evaluation suites that block a merge, agent topologies, and pull-request gates on shared rule repositories. A growing share of the adaptation that makes a deployed system reliable now happens outside the weights, in a fast-changing local scaffold wrapped around a slow-changing frontier model.

Read one at a time, these artifacts look like unrelated engineering. A skill file is a procedure the model did not have. A repository rule is a local parameter for one project's conventions. A retrieval connector is memory access specific to one workflow. A tool registry provisions a capability the base model cannot reach. A pull-request review against a shared rule repository is a promotion gate, and an evaluation suite that blocks a merge is a validation check before promotion. Read together, they are one adaptation surface, the non-model part of what has been called a compound AI system [@zaharia2024compound]. The question this survey asks is what optimization discipline that surface needs. The answer we find is that the field has built an external adaptation layer for LLMs but not the optimizer that should govern it. Most deployments maintain the layer as patchwork: a failure happens, someone adds a rule, the pile grows, nobody knows which addition helped, and fixes leak into contexts that never validated them.

The disciplined alternative runs two loops, and only the first is routine. The local loop, which turns a recurring failure into a tested edit, closes under an automatic gate in most research systems and a growing number of production ones. The governed second loop, which would carry a validated edit across organizations under versioned lineage, access control, and rollback, appears in none of the 256 systems surveyed. What separates them is the signal the gate receives. The class of that signal fixes which loop a deployment can close: an exact check or an observed outcome can gate an edit automatically, a judgment only once the judge is calibrated against people, and a delayed reward not edit by edit at all.

This article makes five contributions.

1. The loop that turns patchwork into optimization, in plain language and as a gated update rule, with the five conditions under which it is an optimizer.
2. Four classes of feedback signal, from an exact check to a delayed reward, each fixing what the gate can be, which gate pairings are reachable, and which failure dominates.
3. A survey of 256 production and research systems, scored on six substrates against a published rubric, with the scores released.
4. A design space indexed by the gate on each loop, read structurally, and the convergence of five research families on the same loop as evidence that the architecture is real.
5. A four-property audit criterion for governed cross-organization scaffold optimization, which no surveyed system meets, and the failure surface its absence leaves open.

Section REF(sec:why) argues that adaptation belongs in the scaffold, Section REF(sec:loop) states the loop, and Section REF(sec:signal) classifies its signal; Sections REF(sec:method) to REF(sec:families) report the survey, and Sections REF(sec:gap) to REF(sec:open) name the missing architecture, its failure surface, and the open problems.

The survey runs no experiments. Its evidence is the published behavior of 256 systems, scored on a released table.

## Why adaptation lives outside the weights {#sec:why}

### Breadth in the weights, depth in the scaffold

Frontier training optimizes for breadth. The weights are tuned to generalize across millions of unseen deployments, and the objective smooths over exactly what one deployment cares about: local naming conventions, contradictory preferences between customers, rare workflow-specific failures. Reinforcement learning from human feedback reduces output diversity and homogenizes preferred style across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data rewards patterns that generalize across the annotator pool, so the frontier model is trained to disfavor one customer's idiosyncrasies. Tiwari et al. [@tiwari2026fastandslow] reach the same place from the optimization side: in-context adaptation is cheap but capacity-bounded, in-weights adaptation is expressive but induces forgetting and loss of plasticity [@dohare2024loss], so a two-timescale system, one that learns slowly in the weights and fast outside them, needs a cheap outer layer that absorbs what context can carry.

Production reliability is achieved in depth, inside one deployment, and it turns on what global training had to smooth away. Encoding every deployment in the weights is ruled out three times over: fine-tuning per customer multiplies the training, evaluation, and serving lifecycle by the number of deployments; weights ship quarterly at best, while the deployment wants daily updates; and overfitting the weights to one customer degrades the neighbors whose preferences contradict. Per-customer adapters [@hu2021lora], distilled models, and learned routing could absorb some of the residual, the failures that remain after training, but in practice they are rare. Adaptation lands in the scaffold, the one substrate that is cheap, inspectable, reversible, scoped to one customer, and updatable daily.

### Why the scaffold is the right architecture: the two earlier results

The case for learning outside the weights does not rest on cost alone; it is the conclusion of the two papers that precede this one in the series. *Beyond Exponential Decay* [@arbuzov2025beyond] finds that long LLM outputs do not fail at the rate a uniform per-token error model predicts, because reliability hinges on a sparse set of key decisions, which make up under a tenth of tokens by the available long-context measurement. *The Architecture of Errors* [@arbuzov2026architecture] finds that inside a bounded deployment those decisions fail in a finite catalogue of recurring modes whose size grows only slowly with the number of observed failures, so a small, targeted budget of interventions covers the residual.

Together they say where a deployment's errors are and that they are few enough to fix one at a time. This article asks where the fixes live, and the corpus answers: in persistent artifacts outside the weights, where a fix for a recurring, deployment-specific mode is cheap to make, inspect, and reverse. Gated and scoped, that layer is not a workaround for an inadequate model. It is the architecture the error structure calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization.

### Relation to existing surveys

This survey classifies systems on four axes: whether a feedback loop closes at all, whether its gate is a program or a person, what the gate can observe, and whether promotion beyond one deployment is governed. No existing survey uses all four, and Table REF(tab:II-2) places this one against the surveys that cover neighboring ground.

| Survey | Scope | Organizing axes | Loop closure | Gate type | Signal class | Governance |
|------------|--------------|------------------------|----------|----------|----------|----------------|
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

Existing surveys of self-evolving agents, agent memory, context engineering, skills, and harness design catalogue mechanisms by what they edit and when. None classifies systems by loop closure, gate type, or signal class; two carry a governance axis, and none covers promotion across organizations. One of those two, Ding et al.'s survey of persistent-state agents, finds that literature concentrated on accumulating and retrieving state rather than on governing, recovering, or relinquishing it [@ding2026alwayson].

A reader will expect the prompt-optimization lineage here: OPRO, EvoPrompt, Promptbreeder, DSPy, and TextGrad [@yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad]. That lineage optimizes a prompt or program once against a development set and is not a deployed loop. The evolving playbook of agentic context engineering [@ace2025agentic] persists its artifact but keeps it inside one context and never promotes it.

The closest precedents optimize the scaffold itself. Agent symbolic learning updates prompts, tools, and pipeline as symbolic parameters from textual feedback [@zhou2024symbolic]; in STOP, a scaffolding program recursively improves its own improvement code [@zelikman2023stop]; and a coding agent edits its own harness to raise its benchmark score [@robeyns2025sica]. Each runs one deployment's loop under a benchmark score. What changes here is that the edited artifact persists in a deployment and must clear a second gate before it earns any scope beyond that deployment (Supplementary Material S7).

## The loop: artifact-layer descent {#sec:loop}

### The loop in plain language

The disciplined version of scaffold maintenance is one loop, which we call artifact-layer descent, run again and again over the life of a deployment. It does not react to single failures. As the deployment runs, it logs what went wrong: failed outputs, user corrections, rejected answers, evaluation regressions, tool-call errors. Reflecting over that record, it clusters the failures into recurring modes and takes up the ones that matter most, ranked by how often each recurs and how badly it fails. For such a mode it locates the scaffold coordinate responsible, which may be a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, or a misrouted agent edge. It then synthesizes one candidate edit to that coordinate. A deployment serves one **patch**: the slice of users, tasks, and conventions it handles. The failure rate on that patch's recurring tasks is the **patch loss**; the loop measures whether the edit lowers it, and a gate accepts or rejects the edit on that measurement. An accepted edit stays in the scaffold; one that a later check shows made things worse is pruned or rolled back.

Then comes the step most systems skip. The loop decides how far the edit should travel, promoting it to other deployments only as far as the evidence reaches; we call that limit the edit's **evidence radius**. The check that belongs at this step is **receiving-side evaluation**: a check run where the edit arrives, not where it was made. Fig. REF(fig:descent) draws the loop.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{fig1_descent_ieee}
\caption{Artifact-layer descent. Loop 1 turns a failure into a gated, persisted edit on one deployment's scaffold; Loop 2 promotes a validated edit to other deployments, only as far as its evidence radius supports.}
\label{fig:descent}
\end{figure*}
```

### Two loops, two knobs

An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repository's instruction file. The edit is small and its scope is one project. The same engineer could promote the rule to a team-wide template, to the company's core instructions, or to a skill registry shared across companies. The edit did not change; the scope did. And the gate that should let it through gets stricter at each step, because the loss it is tested against is now an average over more deployments, and a fix that helps one repository can hurt another.

Loop 1 is the local fix: a recurring failure produces a candidate edit, the edit is tested, and an accepted edit changes one deployment's scaffold. Loop 2 is the separate decision of whether that fix should be shared. In optimizer terms, Loop 1 sets the analogue of a step size: how much one accepted edit changes the local scaffold. Loop 2 sets how many deployments the edit applies to, which leaves the step alone and changes the target: the average failure rate the scaffold is tuned to reduce.

The scopes nest, USER within PROJECT within STACK within TENANT within CORE, and each level's loss is the average failure rate over the deployments it contains (Fig. REF(fig:scope)). USER is one person's account or fork; PROJECT, one repository, workflow, or product workspace; STACK, a curated bundle of projects under one team; a **tenant** is one organization or customer; CORE is the scope every tenant shares. Promotion that reaches CORE crosses tenants, and we call it cross-tenant promotion; reaching TENANT applies an edit across one tenant's deployments. Governance is therefore not administrative overhead. It is the regularization that keeps a small fix from being aimed at the wrong target.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{Patch scope hierarchy. Each level's loss averages the deployments it contains. Loop 1 descends a USER or PROJECT loss; Loop 2 promotes upward; cross-tenant promotion means reaching CORE.}
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

The conditions presuppose frozen frontier weights, edits that persist as inspectable artifacts rather than transient prompts, and promotion that widens an artifact's scope under a gate rather than averaging comparable updates as weight-space federated learning does.

Write the patch loss of deployment $D$ as
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$
where $\theta_M$ are the frontier weights, fixed during deployment, $\theta_s$ is the scaffold, a structured object over the six substrate coordinates of Section REF(sec:method), and $\ell$ is an operational loss. A failure yields no analytic gradient. It yields a candidate edit $z_t$, proposed by reflecting over the accumulated failure history, with modes taken in order of how often and how badly each fails. The gate accepts the edit when its noisy estimate of the change in loss clears a margin,
$$G_t(z_t) = 1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \le -\tau_t,$$
where $\Omega \ge 0$ penalizes the complexity of the edit and the breadth of its promotion, and $\tau_t \ge 0$ is the required margin. An accepted edit is applied; a rejected one leaves the scaffold unchanged.

Production systems implement this inequality without writing it: an evaluation blocks a merge on regression, a reviewer rejects a vague rule, a governance system holds an artifact back until evidence accumulates. Under further assumptions on the gate's bias and the proposal process, the update satisfies a one-step descent inequality and converges, informally, to a gate-stable scaffold, where no admissible edit that would lower the loss clears the gate (Appendix REF(app:formal)). Where a condition fails, the picture is an analogy, and the survey marks which systems meet which conditions.

Each loop has a gate, and we name three kinds by who decides. A gate is **Auto** when a program makes the decision, whether by an evaluation score, a verifier, a reinforcement-learning threshold, a language-model judge [@zheng2023judge] with a quantified agreement rate, or, at the degenerate end, an unconditional rule that accepts every candidate. It is **Human** when a person decides. It is **None** when the loop is absent. We write a system's two gates as a pair, Loop 1 first: [Auto × Human] means an algorithmic local gate and a human promotion gate. These pairs index the design space of Section REF(sec:design).

Condition 1 says the loss must be measurable. It does not say what measures it, and that turns out to be the question that sorts the corpus.

### Three stages of scaffold maintenance

Three stages of scaffold maintenance recur across the corpus (Table REF(tab:II-1)). They differ in how candidate updates are produced, whether credit assignment is explicit, and whether promotion is bounded by evidence. A patchwork loop becomes Stage 3, artifact-layer descent, once the five conditions hold. Production deployments that reach Stage 3 on the local loop promote either behind a human gate, as Spotify [@palumbo2026spotify] and SkillForge do, or, in one case, by an automatic push that carries lineage but no evaluation, as Letta's Context Repositories do.

| Stage | Update mechanism | Credit assignment | Promotion discipline | Dominant failure |
|--------------|--------------------|----------------------|------------------------|--------------------|
| 1. Patchwork | Intuition-driven local edits | Implicit, ad hoc | None | Bloat |
| 2. Random artifact search | Many variants tried under an evaluation | Weak; the evaluation is the only signal | Evaluation-gated merge, no failure-to-coordinate tracing | Overfitting to the in-distribution patch |
| 3. Artifact-layer descent | Residual traced to a coordinate, then one edit | Explicit per failure mode | Bounded by evidence radius; reversible | Evaluation fragility |

Table II-1. Three stages of scaffold maintenance.
