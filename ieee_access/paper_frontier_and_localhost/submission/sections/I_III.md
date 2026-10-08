## Introduction {#sec:intro}

The standard mental model of a system built on a large language model (LLM) is the model. Pre-training fixes the weights, fine-tuning nudges them, and deployment wraps a thin layer of prompts and tools around the result. Production in 2025 and 2026 has stopped behaving this way. Frontier weights change on a cycle of months; the systems built on them change daily, in instruction files checked into repositories, memories that persist across sessions, skills loaded on demand, registered tools, evaluation suites that block a merge, agent topologies, and pull-request gates on shared rule repositories. A growing share of the adaptation that makes a deployed system reliable now happens outside the weights, in a fast-changing local scaffold wrapped around a slow-changing frontier model.

Read one at a time, these artifacts look like unrelated engineering. A skill file is a procedure the model did not have; a repository rule is a convention for one project; a retrieval connector is memory access for one workflow; a tool registry provisions a capability the base model cannot reach; a pull-request review against a shared rule repository is a promotion gate. Read together, they are one adaptation surface, the non-model part of what Zaharia et al. call a compound AI system [@zaharia2024compound]. This survey asks what optimization discipline that surface needs, and finds that the field has built the layer and, as far as public evidence shows, not the optimizer that should govern it. Most deployments maintain the layer as patchwork: a failure happens, someone adds a rule, the pile grows, nobody knows which addition helped, and fixes leak into contexts that never validated them.

The disciplined alternative is one loop with two halves. Its first half turns a recurring failure into one tested edit to the scaffold and keeps the edit only if the deployment's own failure rate falls; the second decides how far the edit may travel, to a team, to an organization, or to every customer, and lets it travel only as far as evidence supports. The first half is routine: in most research systems and a growing number of production ones it closes under an automatic gate. None of the 256 systems surveyed has a second half governed by versioned lineage, access control, and rollback. What separates the two halves is the feedback the gate receives. A test or an observed outcome can gate an edit automatically; a judgment can only once the judge is calibrated against people; a reward that arrives months later cannot gate edits one at a time. The class of the signal decides which half of the loop a deployment can close.

This article makes five contributions.

1. The loop that turns patchwork into optimization, in plain language and as a gated update rule, with the five conditions under which it is an optimizer (Section REF(sec:loop)).
2. Four classes of feedback signal, from an exact check to a delayed reward, each fixing what the gate can be and which failure dominates (Section REF(sec:signal)).
3. A survey of 256 production and research systems, scored on six substrates against a published rubric, with the scores released (Sections REF(sec:method) and REF(sec:findings)).
4. A design space indexed by the gate on each half of the loop, and the convergence of five research families on the same loop (Sections REF(sec:design) and REF(sec:families)).
5. A four-property audit criterion for governed cross-organization scaffold optimization, which no surveyed system meets, with the failure surface its absence leaves open and the open problem each signal class poses (Sections REF(sec:gap) to REF(sec:open)).

The survey runs no experiments. Its evidence is the published behavior of 256 systems, scored on a released table.

## Why adaptation lives outside the weights {#sec:why}

### Breadth in the weights, depth in the scaffold

Frontier training optimizes for breadth. The weights are tuned to generalize across millions of unseen deployments, and the objective smooths over exactly what one deployment cares about: local naming conventions, contradictory preferences between customers, rare workflow-specific failures. Reinforcement learning from human feedback reduces output diversity and homogenizes preferred style across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data rewards patterns that generalize across the annotator pool, so the frontier model is trained to disfavor one customer's idiosyncrasies. Tiwari et al. [@tiwari2026fastandslow] reach the same place from the optimization side: in-context adaptation is cheap but capacity-bounded, in-weights adaptation is expressive but induces forgetting and loss of plasticity [@dohare2024loss], so a system that learns slowly in the weights needs a cheap outer layer that learns fast outside them.

Production reliability is won in depth, inside one deployment, and it turns on what global training had to smooth away. Encoding every deployment in the weights is ruled out three times over: fine-tuning per customer multiplies the training, evaluation, and serving lifecycle by the number of deployments; weights ship quarterly at best, while the deployment wants daily updates; and overfitting the weights to one customer degrades the neighbors whose preferences contradict. In principle, per-customer adapters [@hu2021lora], distilled models, and learned routing could absorb some of the residual, the failures that remain after training. In practice they are rare. Adaptation lands in the scaffold, the one substrate that is cheap, inspectable, reversible, scoped to one customer, and updatable daily.

### Why the scaffold is the right architecture: the two earlier results

The case for learning outside the weights does not rest on cost alone. The two papers that precede this one in the series supply the hypothesis that explains the pattern the corpus shows, and each states the scope on which it rests. *Beyond Exponential Decay* [@arbuzov2025beyond] argues that long outputs do not fail at the rate a uniform per-token error model predicts, because reliability hinges on a sparse set of key decisions. Its evidence is twofold: a direct measurement of long-range dependence on one natural-text corpus, where under a tenth of tokens depend on distant context, and the accuracy that majority voting recovers on reasoning benchmarks. The argument stops where the number of decisions grows with the task, as in long-horizon agentic work. For a deployment that operates inside a bounded slice of recurring tasks, tools, and evaluator expectations, *The Architecture of Errors* [@arbuzov2026architecture] argues that those decisions fail in a small recurring catalogue of modes whose size grows only slowly with the number of observed failures. A targeted intervention budget that grows polylogarithmically in sequence length, and becomes constant once the catalogue saturates, then covers the residual. The paper's own negative result marks the limit: no finite catalogue covers an unbounded domain.

If those results hold in general, a deployment's errors are few enough to fix one at a time, and a small catalogue of fixable modes is exactly what a cheap, inspectable, reversible artifact layer is for. This article asks where the fixes live, and the corpus answers: in persistent artifacts outside the weights, one recurring mode at a time, which is the pattern the hypothesis predicts. On that hypothesis the gated and scoped layer is not a workaround for an inadequate model. It is the architecture the error structure calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization. The survey's own findings, in Sections REF(sec:findings) to REF(sec:gap), stand without it.

### Relation to existing surveys

This survey classifies systems on four axes: whether a feedback loop closes at all, whether its gate is a program or a person, what the gate can observe, and whether promotion beyond one deployment is governed. Surveys of self-evolving agents, agent memory, context engineering, skills, and harness design catalogue mechanisms by what they edit and when; none uses all four axes, and none covers promotion across organizations (Table REF(tab:II-2)). The one closest in spirit, Ding et al.'s survey of persistent-state agents, finds that literature concentrated on accumulating and retrieving state rather than on governing, recovering, or relinquishing it [@ding2026alwayson].

| Survey | Scope | Organizes by | Of the four axes here |
|------------|--------------|------------------------|----------------------|
| Gao et al. [@gao2026selfevolving] | self-evolving agents | what, when, how, where to evolve | loop closure and gate type, in passing |
| Fang et al. [@fang2025comprehensive] | self-evolving agents | inputs, agent system, environment, optimizers | loop closure, in passing |
| Zhou et al. [@zhou2026selfevolvingcoding] | self-evolving coding agents (108 methods) | evolution target, timing, code signals | all four in passing; reversibility as a governance axis |
| Ding et al. [@ding2026alwayson] | persistent-state agents (435 works) | authority, scope, mutability, provenance, recoverability | governance (provenance, rollback) as an axis; gate type in passing |
| Lin et al. [@lin2026memorysecurity] | memory security (~90 works) | lifecycle phases × security objectives | governance (principal scoping, rollback) as an axis; gate type in passing |
| Guo et al. [@guo2026harness] | agent system and harness design | six runtime responsibilities | all four, in passing |
| Xia et al. [@xia2026harnessing] | skill-mediated agents (8 systems) | four responsibility layers, ten patterns | loop closure and governance, in passing |
| Ding et al. [@ding2026skilleval] | skill evaluation and evolution | four evolution paradigms × six benchmark classes | all four, in passing |
| Mei et al. [@mei2025context] | context engineering (1,411 papers) | components × system implementations | none |
| This survey | 256 scaffold-adaptive systems | loop closure, gate type, signal class, governance | all four, as classification axes |

Table II-2. Related surveys. The last column says which of this survey's four axes each one carries, as a classification axis or only in passing.

A reader will expect the prompt-optimization lineage here: OPRO, EvoPrompt, Promptbreeder, DSPy, and TextGrad [@yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad]. That lineage optimizes a prompt or program once against a development set and is not a deployed loop. Agentic context engineering [@ace2025agentic] does persist its artifact, an evolving playbook, but keeps it inside one context and never promotes it. The closest precedents optimize the scaffold itself: agent symbolic learning updates prompts, tools, and pipeline as symbolic parameters from textual feedback [@zhou2024symbolic]; in STOP, a scaffolding program recursively improves its own improvement code [@zelikman2023stop]; and a coding agent edits its own harness to raise its benchmark score [@robeyns2025sica]. Each runs one deployment's loop under a benchmark score. What changes here is that the edited artifact persists in a deployment and must clear a second gate before it earns any scope beyond that deployment (Supplementary Material S7).

## The loop: artifact-layer descent {#sec:loop}

### The loop in plain language

We call the disciplined version of scaffold maintenance artifact-layer descent. It is one loop with two halves, run again and again over the life of a deployment: Loop 1 fixes a recurring failure inside one deployment, and Loop 2 decides how far the fix may travel. Fig. REF(fig:descent) draws the first half. The deployment runs and logs what goes wrong: failed outputs, user corrections, rejected answers, evaluation regressions, tool-call errors. The loop does not react to single failures. It clusters the log into recurring modes and takes up the ones that matter most, ranked by how often each recurs and how badly it fails. For such a mode it locates the scaffold coordinate responsible, which may be a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, or a misrouted agent edge, and it proposes one candidate edit to that coordinate.

Then it measures. A deployment serves one **patch**: the slice of users, tasks, and conventions it handles. The failure rate on that patch's recurring tasks is the **patch loss**. A gate accepts the edit if the patch loss falls and rejects it otherwise. An accepted edit stays in the scaffold, versioned; one that a later check shows made things worse is rolled back. That is the whole of Loop 1, and it is what most research systems and a growing number of production systems now do.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{fig1_descent_ieee}
\caption{Loop 1, the local half of artifact-layer descent. A recurring failure is traced to one scaffold coordinate, one edit is proposed, and a gate keeps the edit only if the deployment's patch loss falls. An accepted edit then enters Loop 2 (Fig.~\ref{fig:scope}).}
\label{fig:descent}
\end{figure*}
```

Loop 2 is the step most systems skip. An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repository's instruction file. That same rule could be promoted to a team-wide template, to the company's core instructions, or to a skill registry shared across companies. The edit did not change; its scope did. And the gate that should let it through gets stricter at each step, because the loss it is tested against is now an average over more deployments, and a fix that helps one repository can hurt another.

The scopes nest (Fig. REF(fig:scope)). USER is one person's account or fork; PROJECT is one repository, workflow, or product workspace; STACK is a curated bundle of projects under one team; a **tenant** is one organization or customer; CORE is the scope every tenant shares. Each level's loss is the average failure rate over the deployments it contains. Promotion that reaches CORE crosses tenants, which is what cross-tenant promotion means here. Loop 2 promotes an edit upward only as far as the evidence reaches; we call that limit the edit's **evidence radius**. The check that belongs at each rung is **receiving-side evaluation**: a check run where the edit arrives, not where it was made. In optimizer terms, Loop 1 sets the step (how much one accepted edit changes the local scaffold) and Loop 2 sets the target (which average failure rate the scaffold is tuned to reduce). Governance is therefore not administrative overhead. It is the regularization that keeps a small fix from being aimed at the wrong target.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{Loop 2, the promotion half. Scopes nest from USER to CORE, each rung's loss averages the deployments it contains, and an edit rises one rung at a time, only while a check at the receiving side shows the wider loss falling and only as far as its evidence radius. Promotion into CORE crosses tenants.}
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

Written out, the patch loss of deployment $D$ is
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$
where $\theta_M$ are the frontier weights, fixed during deployment, $\theta_s$ is the scaffold, a structured object over the six substrate coordinates of Section REF(sec:method), and $\ell$ is an operational loss. A failure yields no analytic gradient. It yields a candidate edit $z_t$, proposed by reflecting over the accumulated failure history. The gate accepts the edit when its noisy estimate of the change in loss clears a margin,
$$G_t(z_t) = 1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \le -\tau_t,$$
where $\Omega \ge 0$ penalizes the complexity of the edit and the breadth of its promotion, and $\tau_t \ge 0$ is the required margin. Production systems implement this inequality without ever writing it down: an evaluation blocks a merge on regression, a reviewer rejects a vague rule, a governance system holds an artifact back until evidence accumulates. Under a bounded-bias assumption on the gate, the update satisfies a one-step descent inequality. When that bias is summable over the run, the loss converges and improving edits stop clearing the gate; the scaffold is then gate-stable, which is a statement about the gate, not about optimality (Appendix REF(app:formal)). Where a condition fails, the picture is an analogy, and the survey marks which systems meet which conditions.

Each half of the loop has a gate, and we name three kinds by who decides. A gate is **Auto** when a program applies a check before the edit goes through: an evaluation score, a verifier, a reinforcement-learning threshold, or a language-model judge [@zheng2023judge] with a quantified agreement rate. It is **Human** when a person decides. It is **None** when nothing decides, either because that half of the loop is absent or because the step runs unchecked, as when a system pushes every edit to its neighbors without a test. Who writes the candidate is recorded separately and is not a gate: the author may be an agent reflecting over failures, an engineer at a desk, or a contributor registering an artifact. We write a system's two gates as a pair, Loop 1 first: [Auto × Human] means an algorithmic local gate and a human promotion gate. These pairs index the design space of Section REF(sec:design).

Condition 1 says the loss must be measurable. It does not say what measures it, and that turns out to be the question that sorts the corpus.

### From patchwork to descent

Three stages of scaffold maintenance recur across the corpus, and the five conditions separate them. At the first stage, patchwork, edits are made by intuition after a failure, credit assignment is implicit, nothing is promoted on evidence, and the scaffold bloats. At the second stage, random artifact search, many variants are tried under an evaluation and the best is merged; the evaluation is the only signal, no failure is traced to a coordinate, and the dominant failure is overfitting to the in-distribution patch. At the third stage, artifact-layer descent, a residual is traced to a coordinate, one edit is made, promotion is bounded by evidence radius and reversible. Its dominant failure becomes evaluation fragility, because the suite that gates the edits is itself a scaffold artifact that drifts and can be gamed (Section REF(sec:failure)). A loop reaches the third stage once the five conditions hold. Production deployments that reach it on Loop 1 then promote in one of two ways: behind a human gate, as Spotify [@palumbo2026spotify] and SkillForge do, or, in Letta's Context Repositories alone, by an ungated push that carries lineage but no evaluation.
