---
# IEEE Access survey article body. Headings "## I. ..." become \section via --shift-heading-level-by=-1.
# Cites: [@key]; textual cites as "Author et al. [@key]" (the build turns every cite into plain \cite{}).
# Counts in {{DOUBLE_BRACES}} are filled from scripts/recount.py after the October-2026 rescoring.
---

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

## Where the signal comes from: four classes of feedback {#sec:signal}

Four scaffolds all run the loop of Section REF(sec:loop). A coding agent changes one line in its repository rule file; the test suite runs and reports pass or fail within seconds. A scheduling assistant changes how it phrases a booking request; the appointment either appears on the calendar or it does not, and the system learns which an hour later. A marketing assistant changes the tone rule in its instructions; nobody can say whether the next draft is better, only whether a reviewer prefers it. A research assistant changes how it chooses which direction to pursue; whether the choice was good becomes visible months later, after many other edits have landed. All four produce a candidate edit. They differ in what the gate can know about it.

That difference is the whole of this section. The gate needs an estimate of one quantity: whether the edit lowered the patch loss. That estimate comes from a feedback signal. Signals differ in three ways: how soon they arrive, how exact they are, and whether there is a fact of the matter at all. Those three differences sort every surveyed system into four classes (Table REF(tab:IV-1)), and the class fixes what the gate can be, which half of the loop can close automatically, and which failure dominates.

| Class | The signal the gate receives | What the gate can be | What stays hard | Corpus examples |
|---------|------------------------|--------------------|----------------------|--------------|
| C1 exact | A check that returns pass or fail, or an exact score, at once and repeatably: tests, compilers, answer keys | An automatic check; one run per case, repeated only to sample the task mix | The check names the failed output, not the coordinate that caused it; a check that is also the target can be gamed | DGM, AlphaEvolve, SkillOpt |
| C2 observable outcome | A real result one episode later: a booked slot, a merged pull request, a closed ticket; noisy and confounded | An automatic threshold over batched episodes; a person at promotion | The outcome says *that* the episode failed, not *why*; the channel can be poisoned | Devin, Sierra, SAGE, SkillRL, PACE, Voyager |
| C3 judged | A rater, a rubric, or a model judge; no ground truth | A judge calibrated against people; a person at promotion | The rubric is itself a scaffold coordinate, so the gate judges edits to itself; the proxy gets optimized past the point where it tracks quality | SkillForge, CASCADE, skills-repository review |
| C4 delayed | An outcome weeks or months later, once per many edits | No per-edit gate; proposals are pruned and milestones stand in | Credit across many edits; drift; the loop cannot be told from random search | NanoResearch, CORAL, the AI Scientist |

Table IV-1. The four feedback-signal classes. Reading across a row: what the gate receives, what it can therefore be, and what it cannot fix.

The classes are a partition, not three independent axes: a system is assigned by the property that binds its gate first. Delay binds before anything else, so an outcome that arrives months later is C4 even when it is objective; the absence of ground truth binds next, so an immediate judgment is C3; and among signals that are prompt and objective, exactness separates C1 from C2.

**C1, exact.** A deterministic checker returns pass or fail, or an exact score, immediately and repeatably: unit tests, compilers, type checkers, exact-match answer keys, proof checkers, schema validators. DGM accepts a self-modification only after it passes in a sandbox on coding benchmarks [@zhang2025darwin]; AlphaEvolve scores candidate programs with a cascade of exact evaluators [@alphaevolve2025]; SkillOpt gates a skill edit on a held-out exact-match split of a math benchmark [@yang2026skillopt]. Because the check is exact for the artifact and the test it runs, and repeating it returns the same answer, one run settles the checked case. What the check does not settle is the patch loss: the suite is a sample of the patch's task mix, and the agent that runs under the edited scaffold is stochastic, so the gate's estimate of the loss change still carries sampling error. The gate can be a program and its margin can be small, but the margin absorbs sampling error, not error in the check. Two things stay hard. A failing test localizes the output, not the scaffold coordinate that caused it, so credit assignment remains open; and a checker that is also the training target can be gamed. The dominant failures are test overfitting and scaffold bloat, because cheap acceptances accumulate.

**C2, observable outcome.** The environment or the user emits an outcome after an episode: a booked appointment, a closed ticket, a merged pull request, a tool call that returns without error, a retrieved document that contains the answer. The signal is real but one episode late, noisy, and confounded, since a user can accept a wrong answer and reject a right one. Gates of this class include Devin's merged pull requests [@cognition2025devinreview], SAGE's task success on AppWorld [@wang2025sage], SkillRL's success-rate threshold [@skillrl2026], and PACE's failure signals from a deployed small model [@ling2026pace]. The gate can still be a program (a reinforcement-learning threshold or a held-out task suite), but it needs a positive margin, and it absorbs the noise by batching episodes or by requiring agreement across samples (Appendix REF(app:gates)). Credit assignment takes its most stubborn form here: the outcome says *that* the episode failed, not *why*. Most production deployments live in this class, and its signal arrives through a channel an attacker can control, which is why poisoned memory and tool-output injection dominate.

**C3, judged.** There is no fact of the matter. An essay, a marketing page, a design, a pitch deck, or a code review for style can be scored only by a judge: a human rater, a language-model judge, a rubric, or a comparison against references. SkillForge accepts a skill diff when its judge agrees with human engineers more than nine times in ten [@skillforge2026]; CASCADE consolidates memory under a human-and-agent gate [@huang2025cascade]; Anthropic's skills repository promotes a skill when a reviewer approves the pull request. The gate can be a program only after the judge has been calibrated against people, because the judge's bias is now the estimator's bias. Residuals, meanwhile, are captured only when someone objects, so condition 2 depends on complaint channels rather than instrumentation. The dominant failure is Goodhart's law in the form measured for reward models: optimizing a proxy past a point lowers the true score [@gao2023overoptimization]. Once the judge is the target, the scaffold learns the judge. Nor is a human judge stable: Shankar et al. find that evaluators' criteria drift as they grade more outputs [@shankar2024validators].

**C4, delayed and sparse.** The outcome arrives after weeks or months, once per many edits, in a world that has moved on. Research programs, product strategy, and open-ended discovery are of this kind; the clearest instances are automated research pipelines such as the AI Scientist, which generates ideas, runs experiments, and writes the paper [@lu2024aiscientist]. NanoResearch merges candidate skills by semantic compatibility rather than by a measured loss change [@xu2026nanoresearch], and CORAL promotes findings into shared memory on a heartbeat rather than on an evaluation [@qu2026coral]. AlphaEvolve's evolutionary database can look like an instance, and is not one: it balances improving the best programs against diversity only after every candidate has been scored by its exact evaluators, so it is a search strategy inside the exact class, not a gate for a delayed signal [@alphaevolve2025]. With no per-edit estimate to gate on, the gate degenerates to proposal pruning plus proxy milestones, and the descent argument covers only the composition of pruning and whatever gate exists at the horizon (Appendix REF(app:gates)). Temporal credit assignment across many edits is open. The dominant failure is drift: the scaffold ages faster than the signal that would correct it. An optimizer in this class also cannot be told from random search by its outcomes alone; Ong et al. [@ong2026harnesseval] report the same indistinguishability for harness optimizers.

**The judge is part of the scaffold.** One feature of the judged class deserves its own paragraph, because it returns in the findings and in the open problems. The rubric that sets the loss is itself a scaffold coordinate. Suppose a pitch-review system keeps overrating decks that claim a large market without numbers. It traces the failure to its rubric and edits "evaluate market size" into "require a numeric estimate and a source". That edit changes the gate that will judge the next edit. We call this the *reflexive gate*, and nothing in the corpus calibrates one: three scaffold systems report judge calibration [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach], and none calibrates a judge that is itself being edited. The weight side faces the same question. Reinforcement learning from verifiable rewards lies outside the scored corpus, but pushing it into writing and other open-ended tasks has forced researchers to build judged gates. One group holds the gate fixed while the policy learns, as a checklist, a pairwise judge, a reference-anchored judge, or a fixed rubric [@gunjal2025rubrics; @jia2025writingzero; @shi2026references; @jin2026rlaes]; a second group lets the gate move with the policy, scoring by the policy's own probability of a reference or updating the rubric or judge during training [@yu2025rlpr; @xu2026rubricarm; @ding2026evorubrics; @zhu2026score; @li2026rubricem]. Fixed versus co-evolved is exactly the reflexive-gate question, and of the co-evolving methods only RLPR, whose reward is a probability rather than a rubric, reports agreement with human labels (Supplementary Material S6).

**What the class decides.** Read down the table and three consequences follow, each a prediction about the corpus that Section REF(sec:design) checks. First, which half of the loop can close automatically. An exact check or an observed outcome can gate a local edit by program. A judgment can do so only once the judge is calibrated, and a delayed reward cannot gate edits one at a time. Promotion is stricter. Only the exact class can gate it by program without a person on the receiving side, and only when the receiving side runs the same check, because only then does the sending side's evidence mean the same thing on arrival. In every other case the receiving-side evaluation of Section REF(sec:loop) is still owed. Second, which gate pairings a deployment can reach. [Auto × Auto] belongs to exact signals and simulated outcomes; [Auto × Human] belongs to observed outcomes and judgments, where the person on Loop 2 does the work the missing exact signal cannot; and the delayed class has no per-edit gate on either half. Third, which failure dominates, as the last column of the table records and Section REF(sec:failure) develops.

## The survey: substrates, corpus, and scoring {#sec:method}

To see which half of the loop the field has built, we scored 256 systems on where their scaffold adapts, whether a loop closes there, and under what gate.

### Six substrates

A deployment's scaffold is composed of six substrates (Table REF(tab:V-1)). They are the coordinates of $\theta_s$, and each can be edited independently of the others; the three kinds of memory on the memory substrate follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala]. Other partitions are possible, for instance separating evaluation suites from governance. The argument of Section REF(sec:loop) is invariant to the partition so long as the coordinates stay independently editable. This partition is the one that recurs in practice: every integrated system in the corpus has a recognizable instance of each substrate under some name.

| Substrate | What persists | A score of 5 requires |
|-----------|----------------------------|----------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned rules promoted under an automatic gate |
| S2 Skills | Procedures, as code or text, loaded on demand | A skill bank that edits itself on failure, test-gated, versioned, and promoted |
| S3 Memory | Experience kept across sessions: episodic, semantic, procedural | Provenance, versions, and a correction path for every entry |
| S4 Tools | The vetted action surface and its schemas | Evaluation-gated tool versions; a curated bundle as the product |
| S5 Orchestration | The multi-role graph and its routing | Topology updated from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Staged promotion with evaluation thresholds, an audit log, and rollback |

Table V-1. The six scaffold substrates, what each holds, and what a system must do on it to score 5.

Every substrate is scored on the same 0 to 5 scale: 0, ephemeral; 1, persistent and local; 2, persistent with tool attachment but no feedback; 3, multi-scope or feedback-driven but without automated promotion; 4, automated feedback updates the scaffold, so one half of the loop is closed; 5, the substrate's own top mark in Table REF(tab:V-1). Systems that adapt several substrates at once receive an additional integrated row. The top mark means different things on two kinds of substrate. On those that hold adaptable content (S1, S2, S5) it requires both halves of the loop. On those that hold governance machinery (S3 provenance and correction, S4 evaluation-gated tool versions, S6 evaluation-gated promotion with audit and rollback) it requires the machinery a second loop would need, not the loop itself. That is why tool registries and the prompt-management platforms of Section REF(sec:findings) can score 5 with no inner loop at all and still sit outside the two-loop cells of the design space.

### How the corpus was assembled

A system enters the corpus on either of these grounds: it wraps a foundation model with at least one persistent artifact updated from deployment signal, or it is described in public as self-improving, scaffolded, or agentic. All systems were found in arXiv, vendor documentation, and public repositories between January 2023 and the October 2026 cutoff. The corpus was assembled in two passes, the second adding 126 systems up to the cutoff, and each system was scored from its own method section or documentation, never from a secondary summary (Supplementary Material S2). Two kinds of system are excluded: those whose only update mechanism is weight-level fine-tuning or reinforcement learning, which are model-side and belong to the self-evolution literature this survey positions against, and those with no public evidence of deployment or release.

Two filters structure the corpus (Fig. REF(fig:corpus)). The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate, that is, when some artifact persists across scope or is updated from feedback; systems that carry the labels but fail it form a contrast corpus, kept so that the boundary can be audited rather than asserted. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus.

A stricter composite two-loop audit then asks two questions of each core system: does Loop 1 modify a persisted artifact from session signal, and does Loop 2 have an explicit mechanism that promotes the artifact beyond the deployment that produced it, with versioning or lineage? The audit was applied to the 204 core systems and to ten further systems that the text treats at mechanism level. Those ten were classified from their papers after the released table closed; they are not rows of it, and the corpus counts above exclude them (Supplementary Material S2). The audit admits 14 research systems and 3 industry exemplars. Of the research systems, 13 are rows of the released table and the fourteenth, SkillOpt, comes from the mechanism-level group; the industry exemplars are Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories. Only these are placed in the design space. Passing the audit is a weaker thing than having the governed second loop of the thesis: every passing system promotes across users, teams, or repositories inside one operator, none reaches another organization, and one of them, Letta, promotes with no gate at all (Section REF(sec:gap)).

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_corpus_flow_ieee}
\caption{Corpus flow. Every system is scored on the substrates it adapts, with an integrated row for systems that adapt several, giving 269 substrate-level rows for 256 systems; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

### Evidence and scoring discipline

Every classification rests on public evidence of uneven strength and on one rater. Each system carries one or more evidence tiers (T1 to T5 in the released table: peer-reviewed publication, arXiv preprint, production claim with metrics, open-source artifact, industry blog or interview). Peer-reviewed papers and open-source artifacts weigh most in cluster-level statements; a production claim counts when it names a benchmark or integration target; a blog post or interview counts only when a higher tier corroborates it; and production claims are never pooled with peer-reviewed evidence in a cluster-level statistic. Industry systems evaluated from vendor documentation rather than a paper are flagged wherever they appear. One author scored every system, used half-scores only when one criterion was clearly met and another partially, and rounded ambiguous cases down; the scores have not been independently re-rated, and that check is future work. The complete score table, with a one-line justification per row, is released so that every scored classification can be re-derived (Supplementary Material S1). The counts do move under natural relaxations of the composite audit (for instance, counting rollback alone as Loop-2 governance, asking for a promotion mechanism with no governance at all, or admitting a Loop 1 that persists only optimizer state); the qualitative findings survive every one of them (Supplementary Material S2).

## What the field has built {#sec:findings}

The corpus answers the question of Section REF(sec:intro) in one sentence: the local half of the loop is routine, and no surveyed system documents the governed second half. The evidence comes in three cuts: per substrate, where the top mark is reached and where it is not; per missing piece, which parts of the second half are absent and in which signal class; and per cluster, which kinds of system have which half.

### The local loop is routine, and no substrate is finished

Nine in ten of the most recently added core systems close the local loop under an automatic gate, and none of them reaches the top mark on any substrate (Table REF(tab:VI-1)).

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents; none closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | Most active research substrate; Loop 1 routinely automated; production repositories human-merged |
| S3 Memory | 50 | 3.06 | Cuadros et al. | Lineage shipped in products; enforced correction still absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | Most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies evolve under evaluation; one structurally gated instance; no two-loop system |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | Mature prompts-as-code; registries add lineage and rollback; no inner loop |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | High-water mark; research systems without enterprise governance |

Table VI-1. Substrate maturity across the 256-system corpus. Column n counts scored rows on each substrate, Mean is the average score, and Score-5 systems reach the substrate's top mark; the integrated row counts systems scored across several substrates as one composite row. Of the most recently added 126 systems, 31 are skill systems and 102 are core; 92 of the core systems close Loop 1 under an automatic gate, and none of the 126 scores 5 on any substrate.

On the three substrates that hold adaptable content, only two systems reach the top mark, and both reach it inside one research environment. Instruction files persist across IDEs and agents (Claude Code, Cursor, AGENTS.md [@agentsmd2025], Windsurf, Continue.dev) and appear in a fifth to a quarter of coding-agent projects [@robbes2026agenticmuch; @galster2026harnessconfig], yet in a controlled study they raise inference cost by about a fifth and buy nothing in task success [@gloaguen2026agentsmd].

Skills are the most active research substrate: SAGE and COSPLAY close both halves of the loop [@wang2025sage; @wu2026cosplay], Loop 1 is routinely automated, and SkillChain's judge-approved edits pass a human reflection gate before they enter its skill bank, a two-stage local gate rather than a promotion loop [@hu2026skillchain]. Eleven skill systems treat retirement as a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay], and the public skill repositories are merged by hand [@shen2026whomaintains].

On orchestration, automated workflow search came first, in GPTSwarm's optimizable agent graphs [@zhuge2024gptswarm] and AFlow's tree search over code-represented workflows [@zhang2024aflow]. Topologies evolve under evaluation [@cheng2026optimas; @chu2026agentgrad; @chen2026harnessforge]; TOCOMAS alone keeps a topology change only when it satisfies a structural invariant [@zhao2026tocomas], and Evo2Team promotes routing skills across teams [@wang2026evo2team].

Memory carries lineage without enforced correction. Production memory records its own history, in Letta's git-backed Context Repositories [@letta2026memfs], Mem0's per-memory history [@mem02026history], and Zep's bitemporal facts [@zep2026facts]. Research memory splits into write-gating and provenance on one side [@wang2026toki; @xu2026ppmf; @margalit2026governed] and verifier-gated failure loops on the other [@yu2026recuris; @wang2026memguard; @sun2026vermem]. Among the memory systems that gate writes or correct from failures, only Cuadros et al. does both, which is why it alone reaches the top mark.

Tools and governance hold the machinery of a second loop without the first, which is how they reach the top mark with no inner loop (Section REF(sec:method)). MCP registries split into catalogues (namespaces and version records, but no scanning) and control planes (scanning, access control, and quarantine) [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]; none has evaluation-gated promotion. The governance registries bring lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed], and none of them has an inner loop.

No system matures all six substrates at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation. This pattern is not a quirk of the corpus: it tracks which constraints each kind of system was built to satisfy.

### Where the second loop should be, five pieces are missing

Walk the second half of the loop from the failure that starts it to the promotion that ends it, and five pieces are missing or rare across the core corpus. Each is missing in a particular feedback-signal class, which is the first sign that the gap is not one gap but several.

- **Failures are not captured** (C2). Deployed memory systems record preferences and successful facts, not residuals, so the loop has nothing to cluster. The one field report of stores written from dead-ends to prevent recurrence describes a single, self-reported deployment [@helwig2026memory].
- **Which sessions inform the next edit is left to chance** (C2). Nearly every system takes failures in the order they arrive. Task-CoEvolve's variance-weighted task sampling and AutoSaddler's mini-batch failure signals are the exceptions [@miyai2026taskcoevolve; @park2026autosaddler].
- **Memory is versioned, but correction is not enforced** (C2, C3). Git-backed and bitemporal memory ship in products, and five production backends still return facts that were revoked [@shen2026revoked].
- **Promotion is rarely checked where the edit arrives** (C1, C2). ShareMem gives evaluation tasks to a different user, XRepoSkill verifies in at least two repositories, Evo2Team confirms at the target team, and VACE evaluates the candidate with the receiving model held fixed [@qi2026vace]; even Evo2Team's confirmation lets nearly a fifth of its transfers fail on new graphs. EvolveNet has no such check, and the federated optimization framework that proposes a receiving-client gate has not implemented it [@yang2026fao].
- **No promotion crosses an organization** (all classes). ShareMem, EvolveNet, XRepoSkill, and RASO promote across users, clients, or repositories inside one operator [@hu2026sharemem; @nie2026evolvenet; @guo2026xreposkill; @chu2026raso]. No system promotes across customers or organizations with evidence.

The last piece is the thesis of this article. The four before it are the reasons a system that tried to add it would have little to promote and no way to check what it promoted.

### Four kinds of system, each with half the loop

Sort the core corpus by which half of the loop it automates and four clusters appear (Table REF(tab:VI-2)). Each has one half of the loop; none has both halves governed.

| Cluster | Representative systems | Loop 1 / Loop 2 | What the cluster shows |
|------------|------------------------|----------|------------------------------|
| Research full-auto | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, DGM, ADAS, Voyager, EvolveNet, Evo2Team, XRepoSkill | Auto / Auto | Both loops can run under algorithmic gates and benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge, CASCADE, Sierra Agent OS 2.0, Cognition Devin, Spotify's recommendation loop [@palumbo2026spotify] | Auto / Human | An algorithmic Loop-1 gate with a reviewer on Loop 2 is the production-viable cell; Spotify adds online A/B gating |
| Governance-first | Braintrust, Vellum, LangSmith Hub, EDDOps, Agentic Configuration Management, Governed Capability Evolution | None / Auto or Human | Evaluation-gated promotion, lineage, and rollback exist; candidate generation is manual and no inner loop fires from session signal |
| Open standards and registries | AGENTS.md, MCP, Anthropic Agent Skills, Cursor Rules, the MCP control planes | None / Human, or None / None | Cross-vendor convergence on artifact format and tool attachment; registries govern admission and access but do not evaluate |

Table VI-2. Four clusters of the core corpus.

*Research full-auto* systems show that the architecture works when both gates are algorithmic [@xu2026nanoresearch; @wang2026autoagent; @romeraparedes2024funsearch; @alphaevolve2025; @zhang2025darwin; @hu2024adas; @wang2023voyager]. AlphaEvolve is the clearest case: it pairs an evaluator with an evolutionary archive, as FunSearch did before it, and reports production gains at Google. EvolveNet, Evo2Team, and XRepoSkill extend the loop from a single deployment to a federation of deployments. What every member lacks is governance: no access control and no audited promotion.

*Production hybrid* systems show that the production-viable pairing is an algorithmic gate on Loop 1 with a reviewer on Loop 2. SkillForge illustrates it most plainly: a judge that agrees with people more than nine times in ten passes each skill diff, and support engineers decide whether it ships [@skillforge2026]. Sierra routes agent-generated insights through human-authored expert answers [@sierra2025os20], Devin's merged pull requests are its promotion step [@cognition2025devinreview], and Spotify launches automatically optimized prompts and plans only behind an online A/B test. In every member, a person on Loop 2 stands in for the exact signal the cluster lacks.

*Governance-first* systems automate Loop 2 alone. The prompts-as-code platforms [@braintrust2026docs; @vellum2026docs; @langsmith2026hub] and the governance registries [@kang2026registry; @quessadavial2026acm; @qin2026governed] keep immutable versions, evaluation thresholds, and rollback, but they have no Loop 1: engineers author the candidates, and session feedback never triggers one. This is MLOps for scaffolds, distinct from MLOps for weights.

*Open standards and registries* converge across vendors on format and attachment. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit all keep a git-tracked markdown artifact attached to a workspace with an MCP-style tool layer [@galster2026harnessconfig; @barbaste2026harnessengineering], a convergence that Section REF(sec:families) reads as evidence that the architecture is real. Adaptation is what the cluster lacks: its registries govern admission and access but do not evaluate, and in the repositories that run autonomous loops, the runtime state of those loops sits outside version control [@lulla2026loopengineering].

## The two-loop design space {#sec:design}

Index each system by the gate on each half of the loop and the field collapses into two gated cells, one half-cell, and one ungated passer (Fig. REF(fig:design)).

```{=latex}
\begin{figure}[!t]
\centering
\includegraphics[width=0.9\columnwidth]{fig3_design_space_ieee}
\caption{The two-loop design space. Rows give the Loop 1 gate and columns the Loop 2 gate, so a cell [Loop 1 $\times$ Loop 2] such as [Auto $\times$ Human] pairs an algorithmic local gate with a human promotion gate; a gate is None when the step is absent or runs unchecked. Two cells hold every audit passer whose promotion has a gate; a third holds the governance-first platforms, which have the gated second loop but no inner loop; Letta's Context Repositories pass the audit on lineage and promote with no gate at all. The human-gated row holds only curation workflows, and no surveyed system puts a person on the local gate and then promotes. No populated system adds governed cross-tenant promotion.}
\label{fig:design}
\end{figure}
```

[Auto × Auto] holds the research full-auto systems, machine-evaluated on both loops. [Auto × Human], the production-viable cell, holds SkillForge, CASCADE, Sierra Agent OS 2.0, and Cognition Devin: Loop 1 fires at machine speed under an algorithmic criterion, and Loop 2 waits for a person. The governance-first platforms sit in [None × Auto]: they gate promotion on evaluation but generate no candidates from failures, so they pass only the Loop-2 half of the audit and enter the matrix as contrast entries (Supplementary Material S4).

One audit passer sits in neither gated cell. Letta's Context Repositories push shared memory across agents automatically, with git lineage and no evaluation of any kind, so the audit admits them on lineage and the matrix places them in [Auto × None]: a local loop with a gate, and a promotion with none. The cell makes the point the pair notation exists for. A push that carries every edit is not a gate, and the column records that nothing decides.

Seven systems promote across users, clients, teams, or repositories with no versioning or lineage on what they promote, and fail the audit on that alone. If the audit asked for a promotion mechanism and nothing more, six of them would enter, all in [Auto × Auto] except Spotify's production loop, which would land in [Auto × Human]; none would open a new cell. The seventh, Future AGI's prompt lifecycle, rests on a vendor blog alone, which the tier rule does not count, and is not admitted under any rule (Supplementary Material S2).

The human-gated row holds only curation. In [Human × None] an agent drafts and a person decides what is kept: VerificAgent's agent-drafted memories pass a human fact-check and are frozen [@nguyen2025verificagent], and SkillChain's judge-approved skill edits re-enter a human reflection gate before they are deployed. Nothing in the row promotes. [Human × Auto] and [Human × Human] are empty: no surveyed system puts a person on the local gate of a failure-driven loop and then promotes the result, by program or by person. The systems that look like human-gated promotion on a first reading are registries, in which a person registers an artifact and a person, or an admission scan, approves its use, and no failure-driven loop runs at all. They sit in [None × Human]: the MCP registries and a community hub [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway; @jiang2026buildrix], and, in practice, the five public skill repositories of one field study, where every substantive edit is human-authored and human-merged and one deprecation appears in 254 edits [@shen2026whomaintains].

The occupancy bears out the three consequences of Section REF(sec:signal). Every [Auto × Auto] system whose gate estimates the loss change per edit runs on an exact signal or a simulated outcome, and those that work on delayed signals prune proposals instead. [Auto × Human] holds only systems whose signal is an observed outcome or a judgment; no exact-signal system sits there. Nor does any system in the matrix calibrate a judge that is itself under edit.

Two further patterns cut across the cells. Earlier systems accepted an edit on one evaluation and absorbed estimator noise through the per-edit margin alone; the newer ones batch evidence before acceptance. A paired per-item test commits an edit only when its wins are reliable [@wang2026sagegate]; EvolveNet accepts a merge only when it fixes at least as many held-out items as it breaks [@nie2026evolvenet]; in VaG, three heterogeneous critics must all pass [@shang2026vag]; and AutoSaddler feeds mini-batch failure signals into validation-based selection [@park2026autosaddler]. Requiring agreement among independent proposals and averaging over them are different operations that reduce error at different rates (Appendix REF(app:gates)). Multi-layer hierarchies remain rare: AlphaEvolve is the only system that combines a cascade evaluator with a diversity archive, and the other systems that keep archives use them for lineage, not for staged evaluation.

## Five research families converge on the loop {#sec:families}

The loop is not a prescription the field has yet to adopt. Five research families, starting from different substrates and under different names, have arrived independently at parts of it, which we read as evidence that the loop is a shared attractor rather than one group's local optimum. The vendors' convergence on one artifact format and tool attachment (Section REF(sec:findings)) is independent evidence of the same kind. Convergence does not show that the design is optimal, only that the same constraints keep producing the same shape.

The clearest single instance is SkillOpt [@yang2026skillopt]. It treats one markdown skill document as the trainable external state of a frozen agent and edits it with explicit optimizer controls: rollout and reflection batches, add/delete/replace edits, a bounded textual learning rate with cosine decay, a held-out selection gate that accepts only a strictly better score, a rejected-edit buffer kept as negative feedback, and an epoch-wise slow update. Across six benchmarks, seven target models, and three harnesses it is best or tied on every cell its authors evaluate. It also reports transfer across models, harnesses, and benchmarks, which reads as an empirical measurement of evidence radius rather than as a governance mechanism. Its own follow-up, SkillOpt-Lite [@shen2026skilloptlite], removes the buffer, the slow update, and the schedule, keeps the held-out gate and a consensus filter across rollouts, and matches or beats it. So the gate and a consensus form of credit assignment are load-bearing; the rest, it turns out, are stabilizers.

The five families instantiate complementary parts of the loop (Table REF(tab:VIII-1)), and each was pushed into its part by the constraint it started from. Reflective evolution started from trajectories and proposes edits by reflecting over them, with a two-timescale argument for keeping those edits outside the weights [@agrawal2025gepa; @tiwari2026fastandslow]. Reflective context learning, the most direct independent formalization, started from the observation that credit assignment, overfitting, forgetting, and high-variance signals persist whether the learned object lies in parameter space or context space; its generalization penalty is the complexity term $\Omega$ of the gate [@vassilyev2026rcl]. Harness optimization started from orchestration rather than skills and names credit assignment as its bottleneck; it is also the largest family in the corpus: roughly two hundred papers cite its founding entries, and a dozen are scored here [@lee2026metaharness; @lin2026ahe; @cai2026moss; @zehle2026cantante; @nguyen2026harnessevo; @chen2026harnessforge; @li2026growingharness]. The lifecycle family started from artifact pools that bloat and found hygiene to be a precondition for descent [@zhang2026ratchet]: the complexity penalty becomes a constraint frontier once platform limits bind [@tanjim2026mocha], each outcome is attributed to skill, exploration, or environment before an update is admitted [@liu2026skillsvote], and eleven systems make retirement a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay]. The transfer family started from how far an edit travels and instruments Loop 2, from measuring evidence radius one task at a time to federating skill patches across clients or deployments [@shalev2026ict; @li2026combee; @qu2026coral; @ling2026pace; @yang2026federatedskill; @nie2026evolvenet].

| Family | Representative systems | What it instantiates | What it leaves open |
|------------|----------------------|------------------------|----------------------|
| Reflective evolution | GEPA; Tiwari et al. | proposal by reflection over trajectory evidence; two-timescale motivation | persistent artifact; bounded step; held-out gate |
| Reflective context | RCL | the learned object in context space; generalization penalty as $\Omega$ | cross-deployment Loop 2 |
| Harness optimization | Meta-Harness; AHE; MOSS; CANTANTE; HARNESSEVO; HarnessForge; Growing Harness | credit assignment over orchestration; source-level edits; slot attribution | governed Loop 2; access control; rollback |
| Lifecycle and multi-objective | Ratchet; MOCHA; SkillsVote; Library Drift; SkillSmith; ASSAY | hygiene as precondition; constraint frontier as the shape of $\Omega$; gated retirement | gradient-analogue closure; retirement of a promoted artifact's descendants |
| Transfer and federation | ICT; Combee; CORAL; PACE; FederatedSkill; EvolveNet; Evo2Team; XRepoSkill | empirical evidence radius; cross-client aggregation; receiving-side confirmation | cross-organization gate, lineage, rollback |

Table VIII-1. Five research families converging on artifact-layer descent, with the part of the loop each instantiates.

Read against the loop, the families support four conclusions.

1. The scaffold-versus-weights decomposition is independently confirmed. GEPA, Meta-Harness, MOSS, RCL, PACE, and the harness-optimization papers all begin from the observation that weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope, and a system that updates both keeps them as separate levers [@hebbar2026sia].
2. Credit assignment is the central engineering bottleneck. AHE, CANTANTE, Meta-Harness, HARNESSEVO, SkillsVote, and the harness-optimizer evaluation of Ong et al. [@ong2026harnesseval] all name the same step as what separates descent from trial-and-error: attributing a system-level failure to one scaffold coordinate. That step remains unsolved in the general multi-substrate case.
3. Lifecycle hygiene is a precondition for descent, not an alternative to it. A dirty artifact pool starves the gate of signal (Table REF(tab:X-1)), gated retirement is the field's answer, and the one negative result cuts deeper: once a contaminated skill has descendants, rolling it back recovers little, so gating must happen before commit [@shang2026vag].
4. No family documents the governed second loop. FederatedSkill and EvolveNet each narrow the gap on different properties, and neither meets the four that Section REF(sec:gap) sets out.

## The missing architecture: governed cross-tenant scaffold optimization {#sec:gap}

What is missing is specific. Four properties define an architecture that no surveyed system instantiates:

- (a) **auto-gated Loop 1**: the commit criterion is an algorithmic threshold;
- (b) **cross-organization promotion**: Loop 2 routes artifacts between organizations (we use *cross-tenant* and *cross-organizational* interchangeably);
- (c) **versioned lineage with access control**: promoted artifacts carry versions, audit trails, and role-based access policies;
- (d) **rollback**: a bad promotion can be reverted without redeploy.

The closest approaches split these properties among them, and no row of Table REF(tab:IX-1) is full on promotion across organizations.

| System | (a) auto-gated Loop 1 | (b) cross-organization promotion | (c) versioned lineage with access control | (d) rollback |
|----------------|----------|------------------------|----------------------|------------------|
| FederatedSkill [@yang2026federatedskill] | full | partial: privacy-preserving aggregation of skill patches across heterogeneous clients that sit under one operator | partial: auditable per-modification decision log | none |
| EvolveNet [@nie2026evolvenet] | full | partial: held-out merge gate at the aggregator, but clients are benchmark partitions, not organizations | none: no lineage, no access control | full: rollback to the previous shared harness after a failed round |
| SkillForge [@skillforge2026] | full | partial: cross-team within one enterprise | partial | not documented |
| Governance-first registries [@kang2026registry; @qin2026governed; @quessadavial2026acm] | none: no inner loop | none | partial: lineage without access control | full, with evidence |
| MCP control planes [@agenticcommunity2026mcpgateway] | none: no inner loop | none | partial: access control without evaluation-gated promotion | not reported |

Table IX-1. The closest approaches to governed cross-organization scaffold optimization, scored against the four properties.

Row by row, the partition is tidy: the systems with a local loop carry the automatic gate and part of the promotion, the registries carry lineage and rollback without an inner loop, and the control planes carry access control alone. Rollback appears inside one federated round and inside single deployments, as edit-level reversal [@wei2026skillsmith; @gao2026skillaudit] and as an admission test that rejects edits which cannot be undone [@sah2026evoundo]. No system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion (Supplementary Material S4).

In machine-learning terms, what is missing is a cross-tenant aggregator with an automated evaluation gate at the scaffold layer. It would carry five parts: per-tenant artifact pools, each tagged with provenance; an aggregation step across tenants that respects tenant isolation; a held-out evaluation at the receiving tenant that blocks a promotion whenever it does not lower that tenant's patch loss; versioned lineage with access control; and a rollback envelope on every promoted artifact. The federated-learning analogy [@mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated] is useful only in the limit where artifacts are mergeable update representations; federated prompt tuning, in which participants learn a shared prompt rather than shared weights [@guo2022promptfl], is the weight-side precedent closest to that limit. In surveyed practice Loop 2 is selection and merge: the nearest systems aggregate program edits with a language model, not by averaging.

Whether the architecture *should* be built depends on the feedback-signal class, not on the application domain (Section REF(sec:signal)). Where the signal is exact, automatically gated cross-tenant promotion of a test-validated skill would be low-risk, and receiving-side evaluation is cheap to add. Where it is an observable outcome, the sending side's outcome does not transfer, so promotion should be automated only behind receiving-side evaluation, the check that would catch a scaffold over-fitted to one deployment before it propagates to another. Even that check is necessary rather than sufficient: some of Evo2Team's transfers still fail on new graphs after target-side confirmation [@wang2026evo2team]. Where it is judged, a human gate on Loop 2 is a design feature, and governance means lineage and rollback around a human decision. With a delayed signal, property (a) cannot be met; what remains is lineage and rollback without an automatic gate. Safety-critical domains, the usual case for human gates, are judged or delayed domains with high stakes. Naming the four properties turns a vague gap into an audit criterion that any future system can be measured against; naming the signal class says which of the four a given deployment should expect to meet.

## The failure surface {#sec:failure}

Until the governed second loop exists, scaffold maintenance carries failure modes that weight-only systems do not have; they are the scaffold-layer entries in the technical-debt ledger that Sculley et al. opened for machine-learning systems a decade ago [@sculley2015debt]. Each is a missing piece of the optimizer, and each dominates in a particular feedback-signal class (Table REF(tab:X-1)). The entries are documented attacks and degradations, not a new threat model.

| Failure | What has been measured | Architectural response | Dominant class |
|------------|--------------------------------|--------------------------|----------|
| Scaffold bloat | Instruction-following accuracy falls and latency grows sharply as instruction count scales [@jaroslawicz2025ifscale]; LLM-authored skills add nothing over no skill until lifecycle hygiene is applied [@zhang2026ratchet] | Complexity penalty $\Omega$ in the gate; pruning and expiry as first-class gated operations | C1, C3 |
| Poisoned memory | High attack success against standard retrieval-augmented generation [@zou2024poisonedrag]; backdoors planted in long-term memory or knowledge bases [@chen2024agentpoison]; memory control-flow attacks across major agent frameworks [@xu2026mcfa] | Provenance on every entry; write gating; a rollback envelope [@su2026chronomem; @yu2026rollbackrepair] | C2 |
| Injection via tools and MCP | A tool's output or a connected server can smuggle instructions into context [@greshake2023injection; @debenedetti2024agentdojo]; one approved MCP configuration could later be modified without re-approval (CVE-2025-54136) [@checkpoint2025mcpoison] | Narrow tool permissions; a privilege hierarchy over instructions [@wallace2024hierarchy]; tool bindings pass the same promotion gate as any other coordinate | C2 |
| Evaluation fragility | Optimizing a proxy reward past a point lowers the true score [@gao2023overoptimization]; access asymmetries alone produce large relative gains that reflect exposure to the test [@singh2025leaderboard]; harness optimizers cannot be told from trial-and-error by downstream score alone [@ong2026harnesseval] | Held-out evaluations scoped within evidence radius, weighted toward recurring modes, re-read as the target drifts, and checked against an update's attribution | C3 (primary), C1 |
| Coordination failures | Fourteen failure modes in multi-agent systems, dominated by role confusion and context loss [@cemri2025mast] | Orchestration topology treated as a scaffold coordinate under the same gate and rollback discipline | C2 |
| Patch overfitting | A scaffold tuned to one deployment over-fits it by construction (Supplementary Material S3) | Evidence-radius discipline at promotion; receiving-side held-out evaluation | C2 |
| Plasticity loss | Context rot (long-context degradation [@liu2023lostmiddle]), instruction conflict, memory pollution, tool-version drift | Expiry and rollback as explicit loop operations rather than retrospective hygiene | C4 |

Table X-1. The failure surface of patchwork scaffold maintenance, the measured evidence, the architectural response, and the feedback-signal class in which each failure dominates.

Bloat is not only slow; it is a signal-quality problem. Ratchet reports what that looks like: LLM-authored skills gain nothing over a no-skill baseline, human-curated ones show a double-digit gain, and the authors attribute the gap to lifecycle management [@zhang2026ratchet]. In the vocabulary of Section REF(sec:loop), that means residual capture and mode discovery cannot work on a messy artifact pool.

Evaluation fragility compounds because the evaluation suite is itself a patch-local artifact rather than a fixed instrument. It is optimized against: once a metric becomes the target, it is gamed. It is read non-independently, because the gate scores path-dependent agent trajectories whose readings do not compose like ordinary test-set statistics. It goes stale, because the suite adapts on the same cadence as the scaffold it gates. And because failures concentrate in a finite catalogue of recurring modes, a suite that samples tasks at random under-weights exactly the families that drive the failure rate. The response in the table follows from those four facts: held-out and scoped, mode-weighted, re-read, and checked against attribution rather than only against score.

The failure surface is real, quantified in the cited measurements, and largely unmitigated in production. Every row names a piece of the optimizer that current systems do not yet have.

## Open problems and conclusion {#sec:open}

Five open problems follow from the survey, one per feedback-signal class and one for the architecture.

1. **Exact signals: credit assignment from a failing check to a scaffold coordinate.** A test tells the loop that an output failed, not which instruction, skill, or tool binding caused it. Slot attribution [@nguyen2026harnessevo], intervention-based attribution [@chu2026agentgrad], and contrastive multi-agent attribution [@zehle2026cantante] each solve one substrate's case; a general method is the bottleneck the harness-optimization family names.
2. **Observable outcomes: receiving-side evaluation before promotion.** The outcome that justified an edit on the sending side does not transfer, and even where a promoted edit is checked on arrival, some transfers still fail (Section REF(sec:findings)). The gate a federated scaffold optimizer needs, a held-out test at the receiving tenant, has been proposed but not built [@yang2026fao].
3. **Judged signals: calibrating a gate that is itself being edited.** When the rubric is a scaffold coordinate, each accepted edit to it moves the instrument that judges the next edit. No method that co-evolves a rubric or judge reports agreement with human judgment, and no scaffold system calibrates a judge under edit (Section REF(sec:signal)); the nearest measurement is on the human side, where evaluators' criteria drift as they grade [@shankar2024validators].
4. **Delayed signals: telling descent from search.** Where the outcome arrives after many edits, an optimizer's gains cannot be distinguished from trial-and-error by outcome alone [@ong2026harnesseval]; evaluating harness optimizers against their attribution claims rather than their scores is the open method.
5. **The governed cross-organization loop.** The architecture of Section REF(sec:gap), properties (a) through (d), is documented by no surveyed system; the receiving-side gate of problem 2 is the piece that would make cross-organization promotion safe in the two classes where it should be automatic.

The field has built an external adaptation layer for language models but not, as far as public evidence shows, the optimizer that should govern it. Both earlier papers of this series supply the hypothesis for why the layer belongs where it is: errors concentrate in a few key decisions; inside a bounded deployment, those decisions fail in a small and recurring catalogue of modes; and such a catalogue can be fixed one mode at a time in a persistent, inspectable, reversible artifact outside the weights. The corpus is consistent with that hypothesis. If it holds, the gated and scoped artifact layer is not a workaround but the architecture the error structure calls for.

The survey shows how far practice has come toward that optimizer, and the progress is lopsided. The local loop closes automatically in most research systems and in a growing number of production ones; evidence is batched before acceptance; retirement and expiry are first-class operations; production memory carries lineage. What has not moved is the second loop. No surveyed system promotes a validated edit across an organization boundary under an automatic gate with lineage, access control, and rollback. Read by signal class, this is not one gap but four, each with its own reachable answer.

The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization. Because the instruments that judge each edit are themselves part of the moving scaffold, the same evidence-radius and lifecycle discipline the optimizer needs must extend to the gates that judge it.

## Appendix: Formal statement of artifact-layer descent {#app:formal}

This appendix states the setup behind Section REF(sec:loop), a one-step descent inequality under a noisy gate, an informal convergence proposition, the optimization-analogy correspondence, and four worked cases. No new theorem is claimed; the proposition is the ordinary target of local stochastic optimization under noisy estimators, restated for a discrete, versioned parameter.

| Optimization concept | Scaffold analogue |
|--------------|----------------------------------------------|
| Parameter vector | Instructions, skills, memories, tools, routing graphs, evaluation gates, governance rules |
| Loss | Failure, user correction, evaluation regression, retrieval miss, tool error, schema violation |
| Gradient estimate | Credit assignment identifying the coordinate responsible for a failure |
| Step | Accepted scaffold edit; step size is edit magnitude under $\oplus$ |
| Aggregated update | Several recurring failures combined before an update, by averaging or by agreement across $k$ proposals |
| Update radius | Promotion scope: which loss is descended (USER, PROJECT, STACK, TENANT, CORE) |
| Validation loss | Held-out patch evaluation before merge |
| Regularization | Complexity penalty $\Omega(z)$, bloat control, cross-patch regression checks |
| Overfitting | Scaffold improves on this deployment and degrades elsewhere |
| Rollback | Reverting a harmful accepted update |

Table A-1. Optimization concepts and their scaffold analogues.

### Setup

Let the frontier model have fixed parameters $\theta_M$ and let the scaffold be a structured object $\theta_s \in \Theta_s = \Theta_1 \times \cdots \times \Theta_6$ over the six substrate coordinates of Section REF(sec:method); $\Theta_s$ is discrete, symbolic, and versioned. For a deployment $D$, $L_D(\theta_s) = \mathbb{E}_{x \sim D}[\ell(\pi(\theta_M, \theta_s, x))]$. A candidate edit $z_t \sim Q_t(z \mid H_t, \theta_s^t)$ is drawn from a proposal process conditioned on the accumulated history $H_t$ of failures, corrections, rejected outputs, evaluation regressions, and prior accepted edits. $Q_t$ is not uniform: for a mode $m$ that recurs with frequency $f_m$ and carries per-occurrence loss $s_m$, its expected contribution to the failure rate is $f_m s_m$, so high-frequency or high-severity modes are proposed first. The finite directional difference is $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$; the gate sees only a noisy estimate $\widehat{\Delta}_z L_D$. The update is
$$\theta_s^{t+1} = \theta_s^t \oplus z_t \text{ if } G_t(z_t) = 1, \quad \theta_s^{t+1} = \theta_s^t \text{ otherwise.}$$

### Descent inequality

Assume (A1) positive descent bias on accepted edits, $\mathbb{E}[\widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t] \le -\gamma_t - \tau_t$ for some $\gamma_t > 0$, and (A2) bounded estimator bias on accepted edits, $|\mathbb{E}[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t]| \le \varepsilon_t$. With $p_t = \Pr(G_t = 1 \mid \theta_s^t)$,
$$\mathbb{E}[L_D(\theta_s^{t+1}) \mid \theta_s^t] \le L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t\,\varepsilon_t.$$
Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability. In the feedback-signal classes of Section REF(sec:signal), $\varepsilon_t$ is near zero for the check itself in C1, with the sampling error of a finite suite over the patch remaining, bounded by batching for an observable outcome (C2), equal to the judge's bias and bounded only by calibration for a judged signal (C3), and unavailable per edit for a delayed signal (C4).

### Convergence (informal)

Add (A3) proposal coverage with acceptance: at every non-gate-stable scaffold, $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \le -\delta$, and the gate accepts such an edit with probability at least $q' > 0$, so that $p_t(\gamma_t + \tau_t) \ge q q' \delta$ there; (A4) effective compactness of the reachable orbit; and (A5) summable bias, $\sum_t p_t \varepsilon_t < \infty$; and let $0 \le L_D \le B$. The one-step inequality is then of the Robbins–Siegmund form, a non-negative process that decreases in expectation up to a summable perturbation $p_t \varepsilon_t$, so $L_D(\theta_s^t)$ converges almost surely and $\sum_t p_t(\gamma_t + \tau_t) < \infty$ almost surely [@robbins1971convergence]. The finite sum carries the content: a bounded loss cannot pay for infinitely many accepted edits with a positive expected margin, so under (A3) the process visits non-gate-stable scaffolds only finitely often, and with (A4) the limit set of $\{\theta_s^t\}$ is gate-stable: no admissible edit clears the gate with negative expected directional loss in the limit. This is convergence of the loss and stability of the gate decision, not convergence to an optimum; a globally suboptimal gate-stable scaffold is consistent with the result, because $Q_t$ may never propose the improving edit or $\widehat{\Delta}$ may be biased to reject it. In a non-stationary deployment ($D = D_t$) the same mechanism tracks a moving optimum rather than converging once, which is why recency weighting, pruning, expiry, and rollback are the scaffold-level analogues of continual-learning machinery rather than optional hygiene.

### Correspondence

Table REF(tab:A-1) pairs each optimization concept with its scaffold analogue. Credit assignment here is attribution, not backpropagation. Scaffold systems do not differentiate through instruction files. They trace an output error to an upstream coordinate, manually or with a judge or verifier. The descent argument needs only that this attribution succeeds with non-zero probability per failure, which is the credit-assignment condition of Section REF(sec:loop).

### Worked cases

*Retrieval.* Failures recur because retrieved context omits the decisive clause. Attribution traces the error to the retrieval coordinate: chunking, query rewriting, metadata filter, embedding model, reranker, or context-packing rule. The candidate edit tightens chunk boundaries or adds a metadata constraint, and the gate checks that recall and answer accuracy improve on the patch evaluation without degrading adjacent cases. Signal class C1 or C2.

*Pitch review.* The system repeatedly overrates decks that claim a large market without numbers, and the failure cluster points at an under-specified rubric coordinate. The edit changes "evaluate market size" into "require a numeric estimate and a source; if absent, cap the score"; the gate runs the revised rubric against held-out decks with human scores. What the edit changed was the gate that will judge the next edit: the reflexive gate of Section REF(sec:signal), class C3.

*Tool use.* Calls fail because optional parameters are under-specified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The edit adds required fields or a pre-call uncertainty check; the gate checks that tool-call failures fall without raising refusals or latency. Class C2.

*Memory.* A stale customer preference is repeatedly retrieved and causes bad decisions. The responsible coordinate is a memory entry together with its provenance, priority, and expiry policy. The edit corrects, expires, or version-tags the entry; the gate checks that future behavior improves without erasing useful history. Class C2, with the correction itself observable only when a later outcome reveals it.

## Appendix: Gate families and feedback-signal classes {#app:gates}

Section REF(sec:loop) collapses every production gate into one per-edit test $G_t$ on an estimate of the loss change. Surveyed systems instantiate that test in several distinct ways, and some of them are better read as proposal pruning that precedes the per-edit gate than as estimators of $\widehat{\Delta} L_D$. Table REF(tab:B-1) lists the families, the slot each occupies, representative systems, and the feedback-signal class (Section REF(sec:signal)) each family serves.

| Gate family | What it estimates | Slot in Section REF(sec:loop) | Signal class | Representative systems |
|------------|----------------------|--------------|--------------|--------------------|
| Surrogate verifier | Pass or fail from tests, a symbolic checker, or an exact match | Per-edit gate $G_t$ | C1 | DGM (sandboxed code), SkillOpt (held-out exact match), Voyager (game-state check: C2) |
| Evaluation cascade | $\widehat{\Delta} L_D$ on a held-out task suite, cheap-to-expensive evaluators | Per-edit gate $G_t$ | C1 when the suite is exact; C2 when it is a task suite | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| RL threshold | Reward improvement against a deployment threshold | Per-edit gate $G_t$ | C2 | SkillRL, SAGE, EvolveR, PACE |
| LLM judge with calibration | Pairwise or rubric score, calibrated against human agreement | Per-edit gate $G_t$ | C3 | SkillForge (Loop 1), CASCADE (consolidation gate) |
| Reviewer judgment | Human credit assignment by pull-request review or expert sign-off | Per-edit gate $G_t$, human-instantiated | C3 (and C2 when the reviewer has outcome data) | SkillForge (Loop 2), Sierra Agent OS 2.0, Anthropic skills repository |
| Semantic merge | Whether a candidate duplicates or conflicts with existing artifacts | Proposal pruning before $G_t$ | C4 (also a pre-filter in C2, C3) | NanoResearch orchestrator, FederatedSkill server agent |
| Archive selection | Whether a candidate improves on, or diversifies, an archive of already-scored programs | Proposal pruning before $G_t$ | Any; inherits the class of the evaluator that scored the archive (C1 in AlphaEvolve) | AlphaEvolve (MAP-Elites-style database), ADAS |
| Multi-sample agreement | Whether $k$ independent proposals or evaluations agree; false-accept rate decays as $p^k$ rather than variance as $1/k$ | Aggregation filter on the estimate | C2, C3 noise absorption | VaG (three heterogeneous critics must all pass); SkillOpt-Lite (consensus filter across rollouts) |

Table B-1. Gate families, their slot in the formalism, and the feedback-signal class each serves.

The first five families populate $G_t$ directly and, under the assumptions of Appendix REF(app:formal), inherit its descent guarantee. Semantic merge and archive selection are not estimators of $\widehat{\Delta} L_D$; they constrain the proposal distribution, and the descent argument applies to the composition of pruning and gate. Multi-sample agreement is listed because it is the correct analogue of "wait for $k$ pieces of evidence before accepting an edit", a different operation from mini-batch averaging and one that should not be conflated with it. Read down the signal-class column. The only families available to a judged (C3) deployment are the two whose estimator is a judge, and a delayed (C4) deployment has no family that estimates the loss change per edit at all: what it has is semantic merge before the gate and whatever proxy milestone stands at the horizon. That is the structural content of Section REF(sec:signal).
