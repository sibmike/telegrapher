## Introduction {#sec:intro}

A growing share of the adaptation that makes a deployed AI system reliable now happens in the layer of instructions, memories, skills, and tools around a frozen model, and this survey argues that the industry has built most of an optimizer for that layer without ever assembling it. Assembled, that optimizer would replace a pile of fixes that nobody can evaluate with a loop that keeps only what measurably helps.

The standard mental model of a system built on a large language model (LLM) is the model. Pre-training fixes the weights, fine-tuning nudges them, and deployment wraps a thin layer of prompts and tools around the result. Production in 2025 and 2026 has stopped behaving this way. Frontier weights change on a cycle of months; the systems built on them change daily, in instruction files checked into repositories, memories that persist across sessions, skills loaded on demand, registered tools, evaluation suites that block a merge, agent topologies, and pull-request gates on shared rule repositories. We call that fast-changing layer around a slow-changing model the scaffold.

Read one at a time, these artifacts look like unrelated engineering. A skill file is a procedure the model did not have; a repository rule is a convention for one project; a retrieval connector is memory access for one workflow; a tool registry provisions a capability the base model cannot reach; a pull-request review against a shared rule repository is a promotion gate. Read together, they are one adaptation surface, the non-model part of what Zaharia et al. call a compound AI system [@zaharia2024compound], and most deployments maintain it as patchwork. A failure happens, someone adds a rule, and the pile grows. Nobody knows which addition helped, a fix validated in one place leaks into another that never tested it, and every customer relearns the same lesson.

The optimizer is one loop with two halves. Take a coding agent that keeps misnaming a class in one repository. The local loop traces that recurring failure to the rule file responsible, proposes one edit, and keeps it only if the repository's own failure rate falls. The promotion loop decides how far the edit may travel, to a team template, to the company's shared instructions, or to a registry shared across companies, and lets it travel only as far as evidence supports. Five conditions make the loop an optimizer rather than good intentions. The decisive one, a measurable loss, carries two consequences the paper returns to throughout: an accepted edit improves only what its gate measured, and the loop descends to that measure's ceiling rather than evolving toward some better goal.

Set side by side, the 256 systems in this survey tell one story about that loop. The local loop closes under a program nearly everywhere a failure-driven loop runs, in most research systems and a growing number of production ones. It closes from the gate backward: the gate is the best-built step, and the least built are the log of failures and the trace from a failure to the scaffold coordinate (a rule, skill, memory entry, or tool binding) that caused it. Around the gate the newer systems wait for several pieces of evidence before keeping an edit, remove stale skills through the same check that admitted them, and keep a history of every change to memory.

The promotion loop exists only in parts. Beyond the deployment, the newer systems have settled on one artifact format and one tool protocol, and in a few cases carry edits between deployments of one operator, the organization that runs both sides with no customer boundary between them. None of the 256 assembles those parts into promotion across organizations under versioned lineage, access control, and rollback. The reason is structural rather than a matter of effort. What a deployment can automate is fixed by the feedback its gate receives: a test or an observed outcome can gate an edit by program, a judgment only once the judge is calibrated against people, and a reward that arrives months later cannot gate edits one at a time. Because the lift an edit earns is bounded by what its gate measured, that lift reaches another deployment only if the receiver measures the same thing or measures again.

The rest of the survey turns that story into checks a team can run on its own system. It first states the loop in plain language and as an update rule, with the five conditions that tell a team whether its own maintenance is an optimizer or a pile (Section REF(sec:loop)). It then gives the rule that decides, from the feedback a deployment can get, which half of the loop it may automate today and which failure it should expect (Section REF(sec:signal)). The corpus tests that rule: the field has converged on the local loop and sorted on the promotion loop as the rule predicts, with one qualification the data adds, and five research lines have arrived at the same loop from five different starting problems (Sections REF(sec:method) to REF(sec:families)). For the promotion loop, still unassembled, the survey ends with what any future system must show: four governance properties, the check without which no promotion is safe, the failures the literature has already measured in their absence, and, for each feedback class, the piece to build next (Sections REF(sec:gap) to REF(sec:open)). The survey runs no experiments; its evidence is the published behavior of 256 systems, scored on a released table.

## Why adaptation lives outside the weights {#sec:why}

Deployed systems adapt outside the weights because frontier training is built for breadth while a deployment's reliability is won in depth, in the conventions and failures particular to it. That mismatch is why a team's fixes land in the scaffold, and why this survey studies how those fixes are kept and how far they travel rather than how the weights are trained. Two earlier results in this series suggest why a gated scaffold is the right architecture and not a workaround, and the question this survey asks of it is one its neighbors leave open.

### Breadth in the weights, depth in the scaffold

Frontier training optimizes the weights for breadth, across every deployment at once, so the depth that makes one deployment reliable ends up in the scaffold.

The weights are tuned to generalize across millions of unseen deployments, and the objective smooths over exactly what one deployment cares about: local naming conventions, contradictory preferences between customers, rare workflow-specific failures. Because reinforcement learning from human feedback reduces output diversity and homogenizes preferred style across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data rewards patterns that generalize across the annotator pool, the frontier model is trained to disfavor one customer's idiosyncrasies. Tiwari et al. [@tiwari2026fastandslow] reach the same place from the optimization side: in-context adaptation is cheap but capacity-bounded, in-weights adaptation is expressive but induces forgetting and loss of plasticity [@dohare2024loss], so a system that learns slowly in the weights needs a cheap outer layer that learns fast outside them.

Encoding every deployment in the weights is ruled out three times over: fine-tuning per customer multiplies the training, evaluation, and serving lifecycle by the number of deployments; weights ship quarterly at best, while the deployment wants daily updates; and overfitting the weights to one customer degrades the neighbors whose preferences contradict. In principle, per-customer adapters [@hu2021lora], distilled models, and learned routing could absorb some of the residual, the failures that remain after training. In practice they are rare. Adaptation lands in the scaffold, the one substrate that is cheap, inspectable, reversible, scoped to one customer, and updatable daily.

### Why the scaffold is the right architecture: the two earlier results

Two earlier papers in this series offer a hypothesis that makes the gated scaffold the right architecture rather than a workaround, namely that a deployment's errors hinge on a few key decisions that fail in a small, recurring set of ways. Without that hypothesis, the case for learning outside the weights would rest on cost alone.

*Beyond Exponential Decay* [@arbuzov2025beyond] argues that long outputs do not fail at the rate a uniform per-token error model predicts, because reliability hinges on a sparse set of key decisions. Its evidence is twofold: a direct measurement of long-range dependence on one natural-text corpus, where under a tenth of tokens depend on distant context, and the accuracy that majority voting recovers on reasoning benchmarks. The argument stops where the number of decisions grows with the task, as in long-horizon agentic work.

For a deployment that operates inside a bounded slice of recurring tasks, tools, and evaluator expectations, *The Architecture of Errors* [@arbuzov2026architecture] argues that those decisions fail in a small recurring catalogue of modes whose size grows only slowly with the number of observed failures. A targeted intervention budget then covers the residual; that budget grows polylogarithmically in sequence length and becomes constant once the catalogue saturates. The paper's own negative result marks the limit: no finite catalogue covers an unbounded domain.

If those results hold in general, a deployment's errors are few enough to fix one at a time, and a small catalogue of fixable modes is exactly what a cheap, inspectable, reversible artifact layer is for. This article asks where the fixes live, and the corpus answers: in persistent artifacts outside the weights, one recurring mode at a time, which is the pattern the hypothesis predicts. On that hypothesis the gated and scoped layer is not a workaround for an inadequate model. It is the architecture the error structure calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization. The survey's own findings, in Sections REF(sec:findings) to REF(sec:gap), stand without it.

### Relation to existing surveys

No neighboring survey asks the question this one is organized around, which is who decides that an edit is good and how far the edit may travel. It is the question a team faces each time it decides whether to keep a fix and whether to share it.

The neighboring surveys explain how agents evolve, what their memories store, how context is engineered, how skills are evaluated, and how harnesses are built. The question asked here has four parts: whether a feedback loop closes at all, whether its gate is a program or a person, what the gate can observe, and whether promotion beyond one deployment is governed. Table REF(tab:II-2) says, for each neighbor, what it classifies by and where this survey departs from it.

On the governance part, two neighbors come close. Ding et al.'s survey of persistent-state agents finds the literature concentrated on accumulating and retrieving state rather than on governing, recovering, or relinquishing it [@ding2026alwayson], and the memory-security survey of Lin et al. scopes and rolls back memory for safety [@lin2026memorysecurity]; neither asks who gates an edit, and neither covers promotion across organizations.

| Survey | Scope | How this survey differs |
|-------------|---------------|----------------------------------------------|
| Gao et al. [@gao2026selfevolving] | self-evolving agents | organizes by what, when, how, and where an agent evolves; the gate that accepts an edit, and the edit's scope, are mentioned but not classified |
| Fang et al. [@fang2025comprehensive] | self-evolving agents | organizes by inputs, agent system, environment, and optimizer; loop closure appears in passing, gates and promotion do not |
| Zhou et al. [@zhou2026selfevolvingcoding] | self-evolving coding agents (108 methods) | organizes by evolution target, timing, and code signal; closest on reversibility, with no gate or promotion axis |
| Ding et al. [@ding2026alwayson] | persistent-state agents (435 works) | organizes by authority, scope, mutability, provenance, and recoverability of state; governance is an axis, the gate on an edit is not |
| Lin et al. [@lin2026memorysecurity] | memory security (~90 works) | organizes by lifecycle phase and security objective; principal scoping and rollback are axes, feedback and promotion are not |
| Guo et al. [@guo2026harness] | agent system and harness design | organizes by six runtime responsibilities; touches all four questions without classifying by any |
| Xia et al. [@xia2026harnessing] | skill-mediated agents (8 systems) | organizes by four responsibility layers and ten patterns; loop closure and governance appear as patterns, not as axes |
| Ding et al. [@ding2026skilleval] | skill evaluation and evolution | organizes by four evolution paradigms and six benchmark classes; evaluation is the subject, the gate it feeds is not |
| Mei et al. [@mei2025context] | context engineering (1,411 papers) | organizes by components and system implementations; adaptation loops lie outside its scope |

Table II-2. Neighboring surveys and where this one departs from each. This survey classifies by loop closure, gate type, signal class, and governance, and is the only one to cover promotion across organizations.

A reader will also expect the prompt-optimization lineage: OPRO, EvoPrompt, Promptbreeder, DSPy, and TextGrad [@yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad]. That lineage optimizes a prompt or program once against a development set and is not a deployed loop; agentic context engineering [@ace2025agentic] does persist its artifact, an evolving playbook, but never promotes it. The closest precedents optimize the scaffold itself under a benchmark score: agent symbolic learning updates prompts, tools, and pipeline as symbolic parameters from textual feedback [@zhou2024symbolic], STOP's scaffolding program improves its own improvement code [@zelikman2023stop], and a coding agent edits its own harness to raise its score [@robeyns2025sica]. What changes here is that the edited artifact persists in a deployment and must clear a second gate before it earns any scope beyond it (Supplementary Material S7).

## The loop: artifact-layer descent {#sec:loop}

Scaffold maintenance becomes an optimizer, which this survey calls artifact-layer descent, when every fix is tested against a measured failure rate before it is kept and again before it travels. That definition gives a team a test it can apply to its own maintenance, and it gives the survey the yardstick it holds every system in the corpus against. Below, the loop appears in plain words, as five conditions with an update rule, and in one coding agent's path from patchwork to descent.

### The loop in plain language

Artifact-layer descent is one loop with two halves, run again and again over the life of a deployment. The local loop fixes a recurring failure inside one deployment; the promotion loop decides how far the fix may travel. (Figures and the released table label them Loop 1 and Loop 2.)

Fig. REF(fig:descent) draws the local loop. The deployment runs and logs what goes wrong: failed outputs, user corrections, rejected answers, evaluation regressions, tool-call errors. The loop does not react to single failures. It clusters the log into recurring modes and takes up the ones that matter most, ranked by how often each recurs and how badly it fails. For such a mode it locates the scaffold coordinate responsible, which may be a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, or a misrouted agent edge, and it proposes one candidate edit to that coordinate.

Then it measures. A deployment serves one **patch**: the slice of users, tasks, and conventions it handles. The failure rate on that patch's recurring tasks is the **patch loss**. The local gate accepts the edit if the patch loss falls and rejects it otherwise. An accepted edit stays in the scaffold, versioned; one that a later check shows made things worse is rolled back. That is the whole of the local loop, and most research systems and a growing number of production systems now run it, though rarely every step of it (Section REF(sec:findings)).

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{fig1_descent_ieee}
\caption{The local loop of artifact-layer descent. A recurring failure is traced to one scaffold coordinate, one edit is proposed, and a gate keeps the edit only if the deployment's patch loss falls. An accepted edit then enters the promotion loop (Fig.~\ref{fig:scope}).}
\label{fig:descent}
\end{figure*}
```

The promotion loop is the half most systems skip. An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repository's instruction file. That same rule could be promoted to a team-wide template, to the company's shared instructions, or to a skill registry shared across companies. The edit did not change; its scope did. And the gate that should let it through gets stricter at each step, because the loss it is tested against is now an average over more deployments, and a fix that helps one repository can hurt another.

The scopes nest (Fig. REF(fig:scope)). USER is one person's account or fork; PROJECT is one repository, workflow, or product workspace; STACK is a curated bundle of projects under one team; a **tenant** is one organization or customer; CORE is the scope every tenant shares. Each scope's loss is the average failure rate over the deployments it contains. Promotion that reaches CORE crosses tenants, which is what cross-tenant promotion means here. The promotion loop moves an edit upward only as far as the evidence reaches; we call that limit the edit's **evidence radius**. The check that belongs at each rung is **receiving-side evaluation**: a check run where the edit arrives, not where it was made. In optimizer terms, the local loop sets the step (how much one accepted edit changes the local scaffold) and the promotion loop sets the target (which average failure rate the scaffold is tuned to reduce). Governance is therefore not administrative overhead. It is the regularization that keeps a small fix from being aimed at the wrong target.

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_scope_ieee}
\caption{The promotion loop. Scopes nest from USER to CORE, each rung's loss averages the deployments it contains, and an edit rises one rung at a time, only while a check at the receiving side shows the wider loss falling and only as far as its evidence radius. Promotion into CORE crosses tenants.}
\label{fig:scope}
\end{figure}
```

### When the loop is an optimizer

The loop is an optimizer, and not a description of good practice, only when five conditions hold, the last of them a gate that decides which edits are kept.

The five conditions are these:

1. a measurable patch loss, such as a failure rate, a correction rate, or an evaluation score;
2. a failure log, so that residuals are captured rather than lost;
3. credit assignment, so that a failure can be traced, at least sometimes, to the scaffold coordinate that caused it;
4. a synthesized candidate edit to that coordinate; and
5. a gate that checks whether the edit lowers the loss before the edit is kept or promoted.

The conditions presuppose frozen frontier weights, edits that persist as inspectable artifacts rather than transient prompts, and promotion that widens an artifact's scope under a gate rather than averaging comparable updates as weight-space federated learning does.

Written out, the patch loss of deployment $D$ is
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$
where $\theta_M$ are the frontier weights, fixed during deployment, $\theta_s$ is the scaffold, a structured object over the six substrate coordinates of Section REF(sec:method), and $\ell$ is an operational loss. A failure yields no analytic gradient. It yields a candidate edit $z_t$, proposed by reflecting over the accumulated failure history. The gate accepts the edit when its noisy estimate of the change in loss clears a margin,
$$G_t(z_t) = 1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \le -\tau_t,$$
where $\Omega \ge 0$ penalizes the complexity of the edit and the breadth of its promotion, and $\tau_t \ge 0$ is the required margin. Production systems implement this inequality without ever writing it down: an evaluation blocks a merge on regression, a reviewer rejects a vague rule, a governance system holds an artifact back until evidence accumulates. The update satisfies a one-step descent inequality under a bounded-bias assumption on the gate. When that bias is summable over the run, the loss converges and improving edits stop clearing the gate; the scaffold is then gate-stable, which is a statement about the gate, not about optimality (Appendix REF(app:formal)). Where a condition fails, the picture is an analogy, and the survey marks which systems meet which conditions.

Each half of the loop has a gate, the local gate and the promotion gate, and we name three kinds by who decides. A gate is **Auto** when a program applies a check before the edit goes through: an evaluation score, a verifier, a reinforcement-learning threshold, or a language-model judge [@zheng2023judge], whether or not its agreement with people has been measured, a question Section REF(sec:signal) returns to. It is **Human** when a person decides. It is **None** when nothing decides, either because that half of the loop is absent or because the step runs unchecked, as when a system pushes every edit to its neighbors without a test. Who writes the candidate is recorded separately and is not a gate: the author may be an agent reflecting over failures, an engineer at a desk, or a contributor registering an artifact. We write a system's two gates as a pair, the local gate first: [Auto × Human] means an algorithmic local gate and a human promotion gate. These pairs index the design space of Section REF(sec:design).

The first condition says the loss must be measurable. It does not say what measures it, and that turns out to be the question that sorts the corpus.

### From patchwork to descent

Scaffold maintenance passes through three stages that recur across the corpus (patchwork, random artifact search, and artifact-layer descent), and the five conditions are what separate them. The stages matter because a loop that reaches descent stops failing like a pile of fixes and starts failing through its gate.

Take the coding agent above that keeps misnaming a class. At the first stage, patchwork, an engineer adds a rule to the instruction file after noticing the failure; nobody measures whether it helped, nothing is promoted on evidence, and the file sprawls with every incident until nobody knows which rule does what. At the second stage, random artifact search, the system tries many variants of the file under the test suite and keeps the best. The suite is the only signal and no failure is traced to the rule that caused it; the winning variant has learned the suite as much as the task. At the third stage, artifact-layer descent, the recurring failure is traced to the one rule responsible, one edit is proposed, the gate checks that the patch loss falls, and promotion stops at the evidence radius and can be reversed.

At the third stage, the suite or judge that gates the edits is itself a scaffold artifact that drifts and can be gamed. Which failure dominates depends on the signal the gate receives (Sections REF(sec:signal) and REF(sec:failure)). Production deployments that reach the third stage in the local loop then promote in one of two ways: behind a human gate, as Spotify does [@palumbo2026spotify], or, in Letta's Context Repositories alone, by an ungated push that carries lineage but no evaluation.

A measurable loss has two consequences that follow the loop everywhere. The first is that the measure bounds the lift. An accepted edit is an improvement in what the gate measured, on the tasks the gate sampled, and nothing more; a rule that lowers the failure rate on one repository's suite has earned nothing about another repository's. Every loss has a scope. That is why the promotion loop cannot carry the local loop's evidence: the receiving scope measures a different mix of tasks, so a promoted edit either travels under a measure the scopes share or re-establishes its lift where it arrives, which is what receiving-side evaluation is for. Where tenants measure different things, a lift does not transfer at all without it.

The second is that the loop optimizes and does not evolve. It needs a defined measure before it can start and descends toward that measure's ceiling; at the ceiling no edit clears the gate, which is what gate stability means. It does not discover a better goal than the one its measure encodes. Two scaffolds optimized for the same goal under the same measure need not converge to one version; each stops at the ceiling by its own route. A system that edits its own measure, the reflexive gate of Section REF(sec:signal), moves the destination rather than evolving toward an unknown truth. The distinction matters because the corpus is often described in the vocabulary of evolution. What the gated systems in it actually do is descent.
