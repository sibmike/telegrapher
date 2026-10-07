---
title: "Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights"
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
abstract: |
  Production systems built on large language models increasingly adapt outside the model weights: after a failure, teams change instructions, skills, memories, tools, orchestration graphs, evaluation suites, and governance rules faster than any weight update. Two earlier results explain why this is the right place to adapt: reliability over long outputs hinges on a sparse set of key decisions, and inside a bounded deployment those decisions fail in a small, recurring catalogue of modes that a targeted budget of fixes can cover. This article surveys 256 production and research systems from January 2023 to October 2026 and reads the scaffold layer as one adaptation surface governed by one loop: a recurring failure is traced to a scaffold coordinate, a candidate edit is proposed, a gate accepts or rejects it on measured loss, and a second decision sets how far the edit may travel. We state the five conditions under which this loop is an optimizer rather than patchwork, classify systems by which loops they close and whether each gate is algorithmic or human, and add a further axis: the class of feedback signal the gate receives. Exact signals (code, mathematics), observable outcomes (completed tasks), judged signals (writing, design), and delayed signals (research) fix what the gate can be, which design-space cells are reachable, and which failure dominates. No surveyed system combines automated local adaptation with governed cross-organizational promotion, versioned lineage, access control, and rollback. We map the failure surface this gap leaves open and state the open problems for closing it.
header-includes:
  - \usepackage{xurl}
  - \usepackage{calc}
  - \DeclareUnicodeCharacter{2260}{\ensuremath{\neq}}
  - \DeclareUnicodeCharacter{2265}{\ensuremath{\geq}}
  - \DeclareUnicodeCharacter{2264}{\ensuremath{\leq}}
  - \DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}
  - \DeclareUnicodeCharacter{2282}{\ensuremath{\subset}}
  - \DeclareUnicodeCharacter{2248}{\ensuremath{\approx}}
  - \DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
  - \DeclareUnicodeCharacter{2211}{\ensuremath{\sum}}
  - \DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}
  - \DeclareUnicodeCharacter{03B5}{\ensuremath{\varepsilon}}
  - \DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
  - \DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
  - \DeclareUnicodeCharacter{03A9}{\ensuremath{\Omega}}
  - \DeclareUnicodeCharacter{03B8}{\ensuremath{\theta}}
  - \DeclareUnicodeCharacter{2208}{\ensuremath{\in}}
  - \DeclareUnicodeCharacter{2026}{\ldots}
  - \DeclareUnicodeCharacter{2020}{\dag}
  - \DeclareUnicodeCharacter{2021}{\ddag}
  - \DeclareUnicodeCharacter{00A7}{\S}
  - \DeclareUnicodeCharacter{03BA}{\ensuremath{\kappa}}
  - \DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
  - \DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
  - \DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}
  - \DeclareUnicodeCharacter{03B3}{\ensuremath{\gamma}}
  - \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
  - \DeclareUnicodeCharacter{2218}{\ensuremath{\circ}}
  - \DeclareUnicodeCharacter{2212}{-}
  - \DeclareUnicodeCharacter{2070}{\ensuremath{^0}}
  - \DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}
  - \DeclareUnicodeCharacter{200B}{\hskip0pt}
---
## Introduction {#sec:intro}

The standard mental model of a system built on a large language model (LLM) is the model. Pre-training fixes the weights, fine-tuning nudges them, and deployment wraps a thin layer of prompts and tools around the result. Production in 2025 and 2026 has stopped behaving this way. Frontier weights change on a cycle of months; the systems built on them change daily, in instruction files checked into repositories, in memories that persist across sessions, in skills loaded on demand, in registered tools, in evaluation suites that block a merge, in agent topologies, and in pull-request gates on shared rule repositories. A growing share of the adaptation that makes a deployed system reliable now happens outside the weights, in a fast-changing local scaffold wrapped around a slow-changing frontier model.

Read one at a time, these artifacts look like unrelated engineering. A skill file is a procedure the model did not have. A repository rule is a local parameter for one project's conventions. A retrieval connector is memory access specific to one patch of work. A tool registry provisions a capability the base model cannot reach. A pull-request review against a shared rule repository is a promotion gate, and an evaluation suite that blocks a merge is a validation check before promotion. Read together, they are one adaptation surface, the non-model part of what has been called a compound AI system [@zaharia2024compound], and the question this survey asks is what optimization discipline that surface needs. The answer we find is that the field has built an external adaptation layer for LLMs but not the optimizer that should govern it. Most deployments maintain the layer as patchwork: a failure happens, someone adds a rule, the pile grows, nobody knows which addition helped, and fixes leak into contexts that never validated them.

This article makes five contributions.

1. It states the loop that turns patchwork into optimization in plain language, then as a gated update rule, with the five conditions under which the rule is a mechanism rather than a metaphor (Section REF(sec:loop)).
2. It introduces a classification of the feedback signal available to that loop, from an exact check to a delayed and sparse reward, and shows that the class fixes what the gate can be, which design-space cells are reachable, and which failure dominates (Section REF(sec:signal)).
3. It surveys 256 production and research systems from January 2023 to October 2026, scores each on six substrates with a published rubric and a released score table, and reports where maturity is uneven (Sections REF(sec:method) and REF(sec:findings)).
4. It places every system that closes both loops in a design space indexed by gate type and reads the empty cells structurally (Section REF(sec:design)), and it reads the convergence of five research families on the same loop as evidence that the architecture is real rather than one group's local optimum (Section REF(sec:families)).
5. It names, as a four-property audit criterion, the architecture no surveyed system instantiates, namely governed cross-tenant scaffold optimization with versioned lineage, access control, and rollback, and it maps the failure surface that the gap leaves open (Sections REF(sec:gap) and REF(sec:failure)).

The survey runs no experiments. Its evidence is the published behavior of the systems it scores, the released score table, and an audit of every absolute claim against the October-2026 literature (Supplementary Material).

## Why adaptation lives outside the weights {#sec:why}

### Breadth in the weights, depth in the scaffold

Frontier training optimizes for breadth. The weights are tuned to generalize across millions of unseen deployments, and the training objective smooths over exactly the things one deployment cares about: local naming conventions, contradictory tenant preferences, rare workflow-specific failures. Reinforcement learning from human feedback reduces output diversity and homogenizes preferred style across users [@kirk2024understanding; @padmakumar2023diversity], and instruction-tuning data rewards patterns that generalize across the annotator pool rather than patterns specific to any one deployment. The frontier model is therefore trained in a way that systematically disfavors encoding one tenant's idiosyncrasies as preferred behavior. Tiwari et al. [@tiwari2026fastandslow] reach the same place from the optimization side: in-context adaptation is cheap and rapid but capacity-bounded, in-weights adaptation is expressive but induces forgetting and loss of plasticity [@dohare2024loss], so a two-timescale system needs a cheap outer layer that absorbs what context can carry.

Production reliability, by contrast, is achieved in depth. Inside one deployment, reliability is determined by what global training had to smooth away. Encoding every deployment in the weights is ruled out three times over. Per-tenant fine-tuning multiplies the training, evaluation, and serving lifecycle by the number of deployments. Weights ship quarterly at best, while the deployment wants daily updates. And overfitting the weights to one tenant degrades the adjacent tenants whose preferences contradict. Per-tenant adapters [@hu2021lora], distilled models, and learned routing each absorb some residual in principle. In the surveyed corpus they appear rarely, and the scaffold is where adaptation lands; the reason the systems themselves give is that it is the one substrate that is cheap, inspectable, reversible, tenant-scoped, and updatable on a daily cadence at once.

### Why the scaffold is the right architecture, not a workaround: three papers

The case that learning belongs outside the weights does not rest on cost alone. It is the conclusion of three papers, of which this is the third. The first, *Beyond Exponential Decay* [@arbuzov2025beyond], asks why long LLM outputs do not fail at the rate a uniform per-token error model predicts, and finds that reliability hinges on a sparse set of key decisions, under a tenth of tokens by the available long-context measurement, rather than on uniform per-token accuracy. The second, *The Architecture of Errors* [@arbuzov2026architecture], asks what those key-decision failures look like inside a bounded deployment and finds that they cluster into a finite catalogue of recurring modes whose size grows only slowly with the number of observed failures, so a small, targeted budget of interventions covers the residual. Together they say where a deployment's errors are and that they are few enough to fix one at a time.

This article asks where the fixes live. The answer the corpus gives is: in persistent artifacts outside the weights, which is where a small catalogue of recurring, tenant-specific modes can be addressed cheaply, inspected, and reversed. Once the loop that edits those artifacts is gated and scoped, the arrangement is not a patch on an inadequate model. It is the architecture the error structure of the first two papers calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization.

### Three stages of scaffold maintenance

Three stages of scaffold maintenance recur across the corpus (Table REF(tab:II-1)). They differ in how candidate updates are produced, whether credit assignment is explicit, and whether promotion is bounded by evidence. In the surveyed corpus, production deployments sit at Stage 1 or 2; the loop of Section REF(sec:loop) is Stage 3.

| Stage | Update mechanism | Credit assignment | Promotion discipline | Dominant failure |
|--------------|--------------------|----------------------|------------------------|--------------------|
| 1. Patchwork | Intuition-driven local edits | Implicit, ad hoc | None | Bloat |
| 2. Random artifact search | Many variants tried under an evaluation | Weak; the evaluation is the only signal | Evaluation-gated merge, no failure-to-coordinate tracing | Overfitting to the in-distribution patch |
| 3. Artifact-layer descent | Residual traced to a coordinate, then one edit | Explicit per failure mode | Bounded by evidence radius; reversible | (the discipline this article describes) |

Table II-1. Three stages of scaffold maintenance.

A patchwork loop becomes Stage 3 once the five conditions of Section REF(sec:loop) hold. The survey of Sections REF(sec:method) to REF(sec:design) asks which deployed systems meet which of them.

### Relation to existing surveys

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

Table REF(tab:II-2) places this survey against the surveys that cover neighboring ground. Existing surveys of self-evolving agents, agent memory, context engineering, skills, and harness design catalogue mechanisms by what they edit and when. None classifies systems by whether a feedback loop is closed, by whether the gate is algorithmic or human, or by the class of signal the gate receives; two carry a governance axis, and none a cross-organization promotion dimension. This survey classifies on those four axes and audits a named gap against them. The prompt-optimization lineage that a reader will expect here, OPRO, EvoPrompt, Promptbreeder, DSPy, and TextGrad [@yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad], optimizes a prompt or program once against a development set and sits in the contrast corpus, and the evolving-playbook line of agentic context engineering [@ace2025agentic] sits at the single-loop boundary. The closest precedents for optimization over the scaffold itself are agent symbolic learning, which treats prompts, tools, and pipeline as symbolic parameters updated from textual feedback [@zhou2024symbolic]; STOP, in which a scaffolding program recursively improves its own improvement code [@zelikman2023stop]; and a coding agent that edits its own harness to raise its benchmark score [@robeyns2025sica]. Each runs one deployment's loop under a benchmark score, and Section REF(sec:loop) states what that loop becomes once persistence, scope, and promotion are added. Appendix REF(app:related) traces each neighboring line and states what this survey inherits from it.

## The loop: artifact-layer descent {#sec:loop}

### The loop in plain language

The disciplined version of scaffold maintenance is one loop, run again and again over the life of a deployment. It does not react to single failures. As the deployment runs, it logs what went wrong: failed outputs, user corrections, rejected answers, evaluation regressions, tool-call errors. Reflecting over that record, it clusters the failures into recurring modes and takes up the ones that matter most, where a mode earns attention in proportion to how often it recurs and how badly it fails. For such a mode it locates the single scaffold coordinate responsible, which may be a stale memory entry, an under-specified instruction, a missing tool argument, a brittle retrieval rule, or a misrouted agent edge, and it synthesizes one candidate edit to that coordinate. It measures whether the edit lowers the deployment's failure rate on its own recurring tasks, which we call the patch loss, and a gate accepts or rejects the edit on that measurement. An accepted edit stays in the scaffold; one that a later check shows made things worse is pruned or rolled back. Then comes the step most systems skip. The loop decides how far the edit should travel, promoting it to other deployments only as far as the evidence reaches. That limit is the edit's evidence radius. Fig. REF(fig:descent) draws the loop.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{figures/fig1_descent}
\caption{Artifact-layer descent. Loop 1 turns a failure into a gated, persisted edit on one deployment's scaffold; Loop 2 promotes a validated edit to other deployments, only as far as its evidence radius supports.}
\label{fig:descent}
\end{figure*}
```

### Two loops, two knobs

An engineer notices that a coding agent keeps misnaming a class in one repository. The fix is a one-line rule in that repository's instruction file. The edit is small and its scope is one project. The same engineer could promote the rule to a team-wide template, to the company's core instructions, or to a cross-tenant skill registry. The edit did not change; the scope did. And the gate that should let it through gets stricter at each step, because the loss it is tested against is now an average over more deployments, and a fix that helps one repository can hurt another.

Loop 1 is the local fix: a recurring failure produces a candidate edit, the edit is tested, and an accepted edit changes one deployment's scaffold. Loop 2 is the separate decision of whether that fix should be shared. The two loops turn different knobs. Loop 1 sets how much one accepted edit changes the local scaffold, the analogue of a step size. Loop 2 sets how many deployments the edit applies to, which does not change the step but changes the target: which average failure rate the scaffold is being tuned to reduce. The scopes nest, USER within PROJECT within STACK within TENANT within CORE, and each level has its own loss, the average failure rate over the deployments it contains (Fig. REF(fig:scope)). "Cross-tenant promotion" means reaching the TENANT or CORE level. This is why governance is not administrative overhead. It is the regularization that keeps a small fix from being aimed at the wrong target.

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\textwidth]{figures/fig2_scope}
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

Each loop has a gate, and we name three kinds. A gate is **Auto** when the decision is an algorithmic criterion: an evaluation score, a verifier, a reinforcement-learning threshold, or a language-model judge [@zheng2023judge] with a quantified agreement rate. It is **Human** when the decision is reviewer judgment. It is **None** when the loop is absent. These labels index the design space of Section REF(sec:design).

### Assumptions

The descent reading holds when (i) the frontier weights stay frozen while the scaffold adapts; (ii) each edit is a persistent, inspectable artifact rather than a transient prompt; (iii) the deployment exposes a loss that can be measured; (iv) the proposal process can, at least sometimes, trace a failure to the responsible coordinate; (v) the gate is a noisy estimator of whether an edit helps, not an oracle; and (vi) promotion widens an artifact's scope under a gate rather than averaging comparable updates the way weight-space federated learning does. Under these assumptions Appendix REF(app:formal) states a one-step descent inequality and an informal convergence proposition to a gate-stable scaffold. Where a condition fails, the same picture should be read as an analogy, and the survey marks which systems meet which conditions. Condition (iii) says the loss must be measurable. It does not say what measures it, and that turns out to be the question that sorts the corpus.

## Where the signal comes from: four classes of feedback {#sec:signal}

Four scaffolds all run the loop of Section REF(sec:loop). A coding agent changes one line in its repository rule file; the test suite runs and reports pass or fail within seconds. A scheduling assistant changes how it phrases a booking request; the appointment either appears on the calendar or it does not, and the system learns which an hour later. A marketing assistant changes the tone rule in its instructions; nobody can say whether the next draft is better, only whether a reviewer prefers it. A research assistant changes how it chooses which direction to pursue; whether the choice was good becomes visible months later, after many other edits have landed. All four produce a candidate edit $z_t$. They differ in what the gate $G_t$ can know about it.

That difference is the subject of this section. The gate of Section REF(sec:loop) accepts an edit when its estimate $\widehat{\Delta}_{z_t} L_D$ of the loss change clears a margin. Condition (1) of the loop says a patch loss must be measurable; it does not say how. We distinguish four classes of feedback signal by what produces the estimate, and the class turns out to fix three things at once: what the gate can be, which cells of the two-loop design space of Section REF(sec:design) a deployment can reach, and which entry of the failure surface of Section REF(sec:failure) dominates. Table REF(tab:IV-1) summarizes; the paragraphs that follow give one example per class from the corpus.

| Class | Signal | Gate $G_t$ becomes | Conditions (1)–(5) of Sec. REF(sec:loop) satisfied | Reachable cells (Sec. REF(sec:design)) | Dominant failure (Sec. REF(sec:failure)) | Corpus examples |
|----------|--------------|--------------|----------------|------------------|-------------|---------------|
| C1 exact | deterministic pass/fail or exact score, immediate | surrogate verifier; exact eval cascade; $\tau_t \approx 0$ | (1)(2)(4)(5) directly; (3) credit assignment open | [Auto × Auto], [Auto × Human], [None × Auto]; only class where auto-gated Loop 2 needs no receiving-side human | test overfitting; scaffold bloat | DGM, AlphaEvolve kernels, SkillOpt on math |
| C2 observable outcome | success/failure event after one episode; noisy, confounded | RL threshold; held-out task suite; batching or agreement filter; $\tau_t > 0$ | (1) noisy; (2) only if logged; (3) hardest; (4)(5) | [Auto × Auto] in simulators; [Auto × Human] in production | patch overfitting; poisoned memory; tool-output injection | Devin, Sierra, SAGE, SkillRL, PACE, Voyager |
| C3 judged | judge, rubric, rating, reference comparison; no ground truth | calibrated LLM-judge or reviewer; the rubric is itself a coordinate (reflexive gate) | (1) by proxy; (2) via complaints; (3) via rubric decomposition; (4); (5) proxy | [Auto × Human] naturally; [Auto × Auto] only with calibration; [Human × Human] for high stakes (registries and curation only) | Goodhart / eval fragility; rubric accretion | SkillForge, CASCADE, skills-repository review |
| C4 delayed, sparse | outcome at a long horizon, once per many edits | proposal pruning (semantic merge, archive selection) plus proxy milestones; no per-edit gate | (1) only at horizon; (2) rarely as a failure event; (3) temporal, open; (4); (5) replaced by novelty or taste | [Auto × Auto] through archive selection; otherwise [None × Auto] or human on both loops | drift; indistinguishable from random search | NanoResearch, CORAL, AlphaEvolve archive |

Table IV-1. The four feedback-signal classes and what each fixes.

**C1, exact.** A deterministic checker returns pass or fail, or an exact score, immediately and repeatably. Unit tests, compilers, type checkers, exact-match answer keys, proof checkers, and schema validators are all of this kind. DGM accepts a self-modification only after it passes in a sandbox on coding benchmarks [@zhang2025darwin]; AlphaEvolve scores candidate programs with a cascade of exact evaluators [@alphaevolve2025]; SkillOpt gates a skill edit on a held-out exact-match split of a math benchmark [@yang2026skillopt]. In the formalism the estimator bias $\varepsilon_t$ is close to zero, the margin $\tau_t$ can be set near zero, and accepting on a single evaluation ($n = 1$, Section REF(sec:design)) is defensible because repeating the check would return the same answer. Two of the five conditions still need work even here. A failing test localizes the output, not the scaffold coordinate that caused it, so credit assignment remains open; and a checker that is also the training target can be gamed. The dominant failures are test overfitting and scaffold bloat, because cheap acceptances accumulate.

**C2, observable outcome.** The environment or the user emits an outcome after an episode: the appointment is booked, the ticket is closed, the pull request is merged, the tool call returns without error, the retrieved document contains the answer. The signal is real, but it arrives one episode late, it is noisy, and it is confounded, because a user can accept a wrong answer and reject a right one. Devin's merged pull requests [@cognition2025devinreview], SAGE's task success on AppWorld [@wang2025sage], SkillRL's success-rate threshold [@skillrl2026], and PACE's failure signals from a deployed small model [@ling2026pace] are gates of this class. The gate becomes a reinforcement-learning threshold or a held-out task suite; $\tau_t$ must be strictly positive, and the noise is absorbed by batching episodes or by requiring agreement across samples (Appendix REF(app:gates)) rather than by the per-edit check alone. The bottleneck is credit assignment in its hardest form: the outcome says *that* the episode failed, not *why*, so tracing it to one coordinate is an inference the loop must make on its own. This is the class most production deployments live in. It is also the class in which the signal arrives through the same channel an attacker controls, which is why poisoned memory and tool-output injection (Section REF(sec:failure)) dominate here.

**C3, judged.** There is no fact of the matter. An essay, a marketing page, a blog post, a design, a pitch deck, or a code review for style can be scored only by a judge: a human rater, a language-model judge, a rubric, or a comparison against references. SkillForge accepts a skill diff when its judge agrees with human engineers more than nine times in ten [@skillforge2026]; CASCADE consolidates memory under a human-and-agent gate [@huang2025cascade]; Anthropic's skills repository promotes a skill when a reviewer approves the pull request. Three things change. The estimator bias $\varepsilon_t$ is now the judge's bias, which is bounded only by calibration against people, so assumption (A2) of Appendix REF(app:formal) has to be bought rather than assumed. Residuals are captured only when someone objects, so condition (2) depends on complaint channels rather than on instrumentation. And the rubric that defines the loss is itself a scaffold coordinate. When the pitch-review worked case of Appendix REF(app:formal) edits the rubric from "evaluate market size" to "require a numeric estimate and a source", the edit changes the gate that will judge the next edit. We call this the *reflexive gate*. Its dominant failure is Goodhart's law in the form the eval-fragility entry of Section REF(sec:failure) describes, and in the form measured for reward models, where optimizing a proxy past a point lowers the true score [@gao2023overoptimization]: once the judge is the target, the scaffold learns the judge. The judge's criteria are not stable even when the judge is a person; evaluators' criteria drift as they grade more outputs [@shankar2024validators].

**C4, delayed and sparse.** The outcome exists but arrives after weeks or months, once per many edits, in a world that has moved on. Research programs, product strategy, and open-ended discovery are of this kind, and automated research pipelines such as the AI Scientist, which generates ideas, runs experiments, and writes the paper, are its clearest instance [@lu2024aiscientist]. NanoResearch merges candidate skills by semantic compatibility rather than by a measured loss change [@xu2026nanoresearch]; CORAL promotes findings into shared memory on a heartbeat rather than on an evaluation [@qu2026coral]; AlphaEvolve's MAP-Elites archive keeps candidates for their diversity, not their score [@alphaevolve2025]. There is no per-edit estimate to gate on, so $G_t$ degenerates to proposal pruning plus proxy milestones, and the descent argument applies only to the composition of pruning and whatever gate exists at the horizon (Appendix REF(app:gates)). Temporal credit assignment across many edits is open. The dominant failure is drift. The scaffold ages faster than the signal that would correct it, and an optimizer in this class cannot be told from random search by its outcomes alone, which is the indistinguishability Ong et al. [@ong2026harnesseval] report for harness optimizers.

**The same four classes on the weight side.** Reinforcement learning from verifiable rewards trains model weights on C1 signals: a math answer matches or it does not. The effort to push that recipe into writing and other open-ended tasks has had to build C3 gates, and the constructions are worth naming because they are the only gates a C3 scaffold loop can borrow. Rubrics as Rewards scores a response against an instance-specific checklist generated before training and judged by a fixed model [@gunjal2025rubrics]; Writing-Zero trains a pairwise generative judge on writing principles and then holds it fixed while the policy learns [@jia2025writingzero]; reference-anchored judging improves agreement with human labels where no verifier exists [@shi2026references]; an essay scorer trained against a fixed rubric of binary items reaches the agreement of a single human rater [@jin2026rlaes]. A second group lets the gate move with the policy. RLPR scores a response by the policy's own probability of a fixed reference, so the scorer co-evolves by construction [@yu2025rlpr]; Rubric-ARM alternates updates of a rubric generator and a judge before freezing them for policy training [@xu2026rubricarm]; EvoRubrics, SCORE, and RubricEM update rubrics adversarially or from a rubric buffer within training [@ding2026evorubrics; @zhu2026score; @li2026rubricem]. Of fourteen such papers we checked, thirteen are methods and one is a survey; of the methods, eight hold the rubric or judge fixed during policy optimization and five co-evolve it, five report agreement with human judgment, and none of the co-evolving ones does (Appendix REF(app:audit)). These are weight-space methods and this survey does not score them. The point is narrower: whether the rubric is fixed or co-evolved with the policy is exactly the reflexive-gate question, and a co-evolved rubric is a gate under descent whose calibration nobody has yet measured. On the scaffold side, three systems report judge calibration, SkillForge's agreement with engineers, SkillChain's judge-human kappa, and SkillCoach's trajectory-filter consistency against human gold [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach], and none of them calibrates a judge that is itself being edited.

**What the class does to the design space.** Read the matrix of Section REF(sec:design) by class and its empty cells stop being accidents. Every system in the [Auto × Auto] cell whose gate is a per-edit estimator runs on a C1 signal or on a simulated C2 environment where the outcome is cheap to observe; the [Auto × Auto] systems that work in C4 domains gate by pruning, not by an estimate (Claim IV-1). The production-viable cell [Auto × Human] is populated only by C2 and C3 systems, where the human on Loop 2 substitutes for the exact signal that Loop 1 lacks (Claim IV-2). And the weight-side rubric work supplies gate constructions that no scaffold-side system has yet calibrated under the reflexive condition (Claim IV-3). The claims audit in the Supplementary Material checks all three against the rescored corpus; the first two hold without exception and the third is sharpened by the three scaffold-side calibration figures named above.

The class also settles a question Section REF(sec:gap) leaves open: whether the missing cross-tenant architecture *should* be filled. The answer is by class rather than by domain. In C1 an automatically gated cross-tenant promotion of a test-validated code skill is low-risk, and the held-out receiving-side evaluation that Section REF(sec:findings) finds absent is cheap to add. In C2 the corner should be filled only with that receiving-side evaluation, because the sending side's outcome signal does not transfer. In C3 a human gate on Loop 2 is a design feature, not a defect, and governance means lineage and rollback around a human decision. In C4 property (a) of Section REF(sec:gap) cannot be met, so what remains of governance is lineage and rollback without an automatic gate. Safety-critical domains, which Section REF(sec:gap) names as the case for human gates, are C3 or C4 domains with high stakes; the class, not the domain, is what carries the argument.

## Substrates, corpus, and scoring {#sec:method}

### Six substrates

A deployment's scaffold is composed of six substrates. They are the coordinates of $\theta_s$, and each can be edited independently of the others. The three kinds of memory on S3 follow the cognitive-architecture taxonomy of Sumers et al. [@sumers2023coala].

| Substrate | What persists | Score-5 mark |
|------------|----------------------------|------------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned, two-loop, auto-gated promotion |
| S2 Skills | Procedural artifacts (code or text) loaded on demand | Skill bank self-modifies on failure, test-gated, versioned, promoted |
| S3 Memory | Cross-session experience (episodic, semantic, procedural) | Provenance, versioning, and correction pathways |
| S4 Tools | Vetted action surface and context schemas | Domain-curated bundle is the product; evaluation-gated tool versions |
| S5 Orchestration | Multi-role graph and routing | Population or policy updates from an outer-loop signal |
| S6 Governance | Versioning, promotion, audit, rollback | Dev-to-staging-to-production with evaluation thresholds, audit log, and rollback |

Table V-1. The six scaffold substrates and the mark a system must reach to score 5.

The 0 to 5 rubric is the same on every substrate: 0, ephemeral; 1, persistent and local; 2, persistent with tool attachment but no feedback; 3, multi-scope or feedback-driven but without automated promotion; 4, automated feedback updates the scaffold, so one loop is closed; 5, the substrate's own top mark in Table REF(tab:V-1). On the substrates that hold adaptable content (S1, S2, S5) the top mark requires both loops; on the substrates that hold governance machinery (S3 provenance and correction, S4 evaluation-gated tool versions, S6 evaluation-gated promotion with audit and rollback) it requires the machinery a second loop would need, which is why a registry or a prompts-as-code platform can score 5 on S6 while having no inner loop at all. Systems that adapt several substrates at once receive an additional integrated row. Other partitions are possible, for instance separating evaluation suites from governance; the argument of Section REF(sec:loop) is invariant to the partition so long as the coordinates stay independently editable.

### How the corpus was assembled

The corpus was built in two passes with one rubric. The first pass (January 2023 to May 2026) searched arXiv, vendor documentation, and public repositories for systems described as self-improving, scaffolded, or agentic, and kept those that wrap a foundation model with at least one persistent artifact updated from deployment signal. The second pass (June to October 2026) ran query families for self-evolving skills and skill lifecycle, harness and context optimization, agent memory governance, prompt-as-code and evaluation-gated promotion, federated or multi-tenant skill sharing, and multi-agent topology evolution, and it followed the citations of the systems the first pass had identified as closest to the gap of Section REF(sec:gap). Every system admitted in either pass was scored from its own method section or documentation, never from a secondary summary. The first pass scored 130 systems; the second added 126, for 256 unique systems and 269 substrate-level rows. The cutoff is October 2026.

Two filters structure the corpus (Fig. REF(fig:corpus)). The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate, that is, when some artifact persists across scope or is updated from feedback; systems that carry the labels but fail it are kept as a contrast corpus so the boundary is auditable rather than rhetorical. A stricter composite two-loop audit then asks whether Loop 1 modifies a persisted artifact from session signal and Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage; only systems passing both enter the design space of Section REF(sec:design). Of the 256 systems, 204 pass the discriminator and 52 form the contrast corpus; 14 research systems and 3 industry exemplars pass the composite audit, and 7 systems added in 2026 promote across contexts without versioning or lineage and enter only under the relaxations below. Industry systems evaluated from vendor documentation rather than from a paper are flagged as such wherever they appear.

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\textwidth]{figures/fig4_corpus_flow}
\caption{Corpus flow. Every system is scored on the six substrates; the discriminator splits core from contrast; the composite two-loop audit selects the systems placed in the design space of Section REF(sec:design).}
\label{fig:corpus}
\end{figure}
```

Two kinds of system are excluded. Those whose only update mechanism is weight-level fine-tuning or reinforcement learning are model-side and belong to the self-evolution literature this survey positions against; those with no public evidence of deployment or release are not scored at all.

### Evidence and scoring discipline

Each system carries one or more evidence tiers: T1 peer-reviewed publication; T2 arXiv preprint; T3 production claim with metrics; T4 open-source artifact; T5 industry blog or interview. T1 and T4 carry the most weight in cluster-level statements; T3 is admissible when the claim is concrete (a named benchmark or integration target); T5 only when corroborated by a higher tier. Production claims are never pooled with peer-reviewed evidence when a cluster-level statistic is computed. Scoring is single-rater. One author scored every system, half-scores were used only when one criterion was clearly met and another partially, and ambiguous cases were rounded down. The complete score table, with a one-line justification per row, is released as Appendix REF(app:scores) so that every classification can be re-derived. The counts reported in Section REF(sec:findings) move under two natural relaxations of the composite criterion, counting any of versioning, lineage, or rollback as Loop-2 governance, or admitting updates that persist only optimizer state as Loop 1; the qualitative findings survive both (Appendix REF(app:data)).

## Findings: substrate maturity and four clusters {#sec:findings}

### Maturity is uneven, and the 2026 additions did not change the ceiling

Table REF(tab:VI-1) aggregates the corpus by substrate. The column $n$ counts scored rows on that substrate, *Mean* is the average score, and *Score-5 systems* are those that reach the substrate's top mark in Table REF(tab:V-1).

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents; none closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | Most active research substrate; Loop 1 routinely automated; production repositories human-merged |
| S3 Memory | 50 | 3.06 | Cuadros et al. | Lineage now shipped in products; enforced correction still absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | Most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies evolve under evaluation; one structurally gated instance; no two-loop system |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | Mature prompts-as-code; 2026 registries add lineage and rollback; no inner loop |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | High-water mark; research systems without enterprise governance |

Table VI-1. Substrate maturity across the 256-system corpus (all scored rows; May 2026 corpus plus October 2026 sweep). The integrated row counts systems scored across several substrates as one composite row. No system added in 2026 scores 5 on any substrate.

The rows behind the table read as follows. On S1, rules persist across IDEs and agents (Claude Code, Cursor, AGENTS.md [@agentsmd2025], Windsurf, Continue.dev) and adoption is measured at a fifth to a quarter of coding-agent projects [@robbes2026agenticmuch; @galster2026harnessconfig], yet context files raise inference cost by about a fifth without raising task success in a controlled study [@gloaguen2026agentsmd]. On S2, the two systems at the top mark, SAGE and COSPLAY, close both loops inside one research environment [@wang2025sage; @wu2026cosplay]; 31 of the 2026 additions are skill systems, almost all closing Loop 1 under an automatic gate, and eleven treat retirement as a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops]; the public skill repositories, by contrast, are human-merged with one deprecation in 254 edits [@shen2026whomaintains]. On S3, lineage has arrived in production memory, in Letta's git-backed Context Repositories [@letta2026memfs], Mem0's per-memory history [@mem02026history], and Zep's bitemporal facts [@zep2026facts], while five production backends still return revoked facts [@shen2026revoked]; the 2026 research splits into write-gating and provenance on one side [@wang2026toki; @xu2026ppmf; @margalit2026governed] and verifier-gated failure loops on the other [@yu2026recuris; @wang2026memguard; @sun2026vermem], and no system carries both. On S4, MCP registries split into catalogs (the official registry: namespaces and version records, no scanning, no private servers) and control planes with scanning, access control, and quarantine [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]; none has evaluation-gated promotion. On S5, automated workflow search predates the corpus's topology evolution, in optimizable agent graphs [@zhuge2024gptswarm] and in tree search over code-represented workflows [@zhang2024aflow]; topologies now evolve under evaluation [@cheng2026optimas; @chu2026agentgrad; @chen2026harnessforge], TOCOMAS alone retains a topology change only when it satisfies a structural invariant [@zhao2026tocomas], and Evo2Team promotes routing skills across teams with target-side confirmation [@wang2026evo2team]. On S6, the 2026 registries bring lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed], and every one of them has Loop 1 = None.

Three things stand out. First, the six substrates recur: every integrated system in the corpus has a recognizable instance of each, under different names, and a score of 5 on S4 or S6 marks governance maturity rather than a closed inner loop, which is why MCP and the prompts-as-code platforms score 5 there and still sit outside the two-loop cells of Section REF(sec:design). Second, no system matures all six at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation. Third, and this was the result we were not looking for, the 2026 sweep added 126 systems, 92 of its 102 core systems close Loop 1 under an automatic gate, and not one of them reaches the top mark on any substrate. The local loop has become routine. The governed second loop has not moved. The maturity gradient is not a quirk of the corpus; it tracks which constraints each kind of system was built to satisfy.

### Five absences, read by signal class

Five absences fall out of the discriminator, and each sits in a particular feedback-signal class (Section REF(sec:signal)).

- **Failure-triggered memory is rare in production** (C2). Deployed memory systems record preferences and successful facts, not residuals; the one field report of anti-recurrence stores written from dead-ends is a single self-reported deployment [@helwig2026memory].
- **Cross-customer promotion is nearly absent** (all classes). ShareMem, EvolveNet, XRepoSkill, and RASO promote across users, clients, or repositories inside one operator [@hu2026sharemem; @nie2026evolvenet; @guo2026xreposkill; @chu2026raso]; no system promotes across customers or organizations with evidence.
- **Versioned memory has arrived; enforced correction has not** (C2, C3). Git-backed and bitemporal memory ship in products, and five backends still return revoked facts [@shen2026revoked].
- **Scaffold-level curriculum is unspecified in nearly every system** (C2). Which sessions inform the next edit is left to the order they arrive in; Task-CoEvolve's variance-weighted task sampling and AutoSaddler's mini-batch failure signals are the exceptions [@miyai2026taskcoevolve; @park2026autosaddler].
- **Receiving-side evaluation at promotion is rare** (C1, C2). It now exists in ShareMem (evaluation tasks belong to a different user), XRepoSkill (verification in at least two repositories), Evo2Team (target-side confirmation, which still misses four of twenty-two transfers on new graphs), and VACE (candidate evaluated with the receiving model held fixed) [@qi2026vace]; EvolveNet has none, and the federated optimization framework that proposes a receiving-client gate has not implemented it [@yang2026fao]. This is the missing piece that would catch a scaffold over-fitting one deployment before it propagates to another.

### Four clusters

Four archetypal clusters recur across the core corpus (Table REF(tab:VI-2)). They differ in where on the patchwork-to-descent gradient each sits and in which loop is automated.

| Cluster | Representative systems | Loop 1 / Loop 2 | What the cluster shows |
|------------|------------------------|----------|------------------------------|
| Research full-auto | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, DGM, ADAS, Voyager; in 2026 EvolveNet, Evo2Team, XRepoSkill | Auto / Auto | Both loops can run under algorithmic gates and benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge, CASCADE, Sierra Agent OS 2.0, Cognition Devin; in 2026 Spotify's recommendation loop [@palumbo2026spotify], SkillChain [@hu2026skillchain] | Auto / Human | An algorithmic Loop-1 gate with a reviewer on Loop 2 is the production-viable cell; the 2026 entries add online A/B gating and reported judge agreement |
| Governance-first | Braintrust, Vellum, LangSmith Hub; in 2026 EDDOps, Agentic Configuration Management, Governed Capability Evolution | None / Auto or Human | Evaluation-gated promotion, lineage, and rollback exist; candidate generation is manual and no inner loop fires from session signal |
| Open standards and registries | AGENTS.md, MCP, Anthropic Agent Skills, Cursor Rules; in 2026 the MCP control planes | Mixed, or Human / Human | Cross-vendor convergence on artifact format and tool attachment; registries govern admission and access but do not evaluate |

Table VI-2. Four clusters of the core corpus.

*Research full-auto* systems show that the architecture works under fully algorithmic gates. NanoResearch co-evolves skills, memory, and policy with a semantic-merge orchestrator [@xu2026nanoresearch]; AutoAgent runs an execution cycle and an evolution cycle over elastic memory [@wang2026autoagent]; SkillOpt runs held-out gating, a rejected-edit buffer, and a bounded textual learning rate on a markdown skill (Section REF(sec:families)); AlphaEvolve, and FunSearch before it [@romeraparedes2024funsearch], pairs an evaluator with an evolutionary archive and reports production gains at Google [@alphaevolve2025]; DGM modifies its own code under sandboxed tests [@zhang2025darwin]; ADAS searches over agent designs expressed as code [@hu2024adas], and Voyager, the 2023 precursor, grows a skill library in a game environment [@wang2023voyager]. The 2026 entries move the cluster's frontier from a single deployment to a federation of them. Every member still lacks access control and audited promotion.

*Production hybrid* systems pair an algorithmic Loop-1 gate with a reviewer on Loop 2. SkillForge routes judge-passed skill diffs to support engineers, with the judge agreeing with people more than nine times in ten [@skillforge2026]; Sierra routes agent-generated insights through human-authored expert answers [@sierra2025os20] and Devin's merged pull requests are its promotion step [@cognition2025devinreview]; Spotify optimizes prompts and planning automatically and launches only behind an online A/B test [@palumbo2026spotify]; SkillChain applies judge-monotone edits and then a human reflection gate, with judge-human agreement reported as a kappa between 0.72 and 0.91 [@hu2026skillchain]. The human on Loop 2 is doing the work that the missing exact signal cannot.

*Governance-first* systems automate Loop 2 alone. The prompts-as-code platforms [@braintrust2026docs; @vellum2026docs; @langsmith2026hub] and the 2026 registries [@kang2026registry; @quessadavial2026acm; @qin2026governed] have immutable versions, evaluation thresholds, and rollback; they lack a Loop 1 because candidates are authored by engineers rather than triggered by session feedback. This is MLOps for scaffolds, distinct from MLOps for weights.

*Open standards and registries* converge across vendors on format and attachment. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit all keep a git-tracked markdown artifact attached to a workspace with an MCP-style tool layer [@galster2026harnessconfig; @barbaste2026harnessengineering]. Convergence across vendors is independent evidence, complementary to the research-side convergence of Section REF(sec:families), that the architecture is real rather than any one vendor's local optimum. Two measured facts temper the optimism. Context files raise cost without raising success in a controlled study [@gloaguen2026agentsmd], and the runtime state of autonomous loops sits outside version control in the repositories that run them [@lulla2026loopengineering].

## The two-loop design space {#sec:design}

Systems that pass the composite audit sit in a 3×3 matrix indexed by the gate type on each loop (Fig. REF(fig:design)); Appendix REF(app:contrast) lists the named membership of every cell.

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.5\textwidth]{figures/fig3_design_space}
\caption{The two-loop design space. Two cells hold every system that passes the composite audit; a third holds the governance-first platforms, which have the gated second loop but no inner loop; the human-authored cells are occupied only by registries and curation workflows that have no session-signal loop. No populated system adds governed cross-tenant promotion.}
\label{fig:design}
\end{figure}
```

Two cells hold every system that passes the composite audit. [Auto × Auto] holds the research full-auto systems, twelve from the May corpus with machine-evaluated criteria on both loops. [Auto × Human] is the production-viable cell: Loop 1 fires at machine speed under an algorithmic criterion and Loop 2 waits for a person; SkillForge and CASCADE sit here with the three industry exemplars. Those twelve plus two are the fourteen research systems of Section REF(sec:method). A third cell, [None × Auto], holds the governance-first platforms, which have evaluation-gated promotion and no failure-triggered candidate generation; they pass the Loop-2 half of the audit only and enter the matrix as contrast entries. The 2026 sweep did not add a cell. Its seven cross-context promoters land in [Auto × Auto] without versioning or lineage, and so enter the strict audit only under relaxation; its one production loop lands in [Auto × Human].

The other cells are not all empty. Those that are occupied hold only systems that fail the composite audit, and the lopsided pattern of occupancy is itself a finding. [Human × Auto] remains empty: nobody authors candidates by hand and promotes them automatically, because manual authorship offers automated promotion little leverage. [Human × Human] is occupied by MCP registries and a community hub [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway; @jiang2026buildrix], where a person registers an artifact and a person approves its use; the field study of five public skill repositories finds the same shape in practice, with every substantive edit human-merged and one deprecation in 254 edits [@shen2026whomaintains]. [Human × None] is the curation cell. An agent drafts, a person fact-checks, and the result is frozen [@nguyen2025verificagent]. These are single-loop by construction, and read by signal class the occupancy is what Section REF(sec:signal) predicts: automatic gates on both loops appear only where the signal is exact or cheaply observable, and the human cells fill where it is not.

Two cross-cutting findings sharpen the picture. *Evidence is now batched before acceptance.* In the May corpus nearly every automatic gate fired on a single evaluation, absorbing estimator noise through the per-edit margin alone. By mid-2026 statistical acceptance is common: a paired per-item test that commits an edit only when its wins are reliable [@wang2026sagegate], a merge accepted only when the held-out items it fixes outnumber those it breaks [@nie2026evolvenet], three heterogeneous critics that must all pass [@shang2026vag], and mini-batch failure signals with validation-based selection [@park2026autosaddler]. The agreement form of batching, where $k$ independent proposals must converge, shrinks the false-accept rate as $p^k$ rather than shrinking variance as $1/k$, and the two should not be conflated (Appendix REF(app:gates)). *Multi-layer hierarchies remain rare.* AlphaEvolve is still the only system that combines a cascade evaluator with a diversity archive; the 2026 systems that keep archives use them for lineage, not for staged evaluation.

## Convergent research families {#sec:families}

The loop of Section REF(sec:loop) is not a prescription the field has yet to adopt. Five research families, starting from different substrates and under different names, have arrived independently at parts of it, and we read that convergence as evidence that the loop is a shared attractor rather than one group's local optimum. Convergence on a design is not evidence that the design is optimal; what it shows is that the same constraints keep producing the same shape.

The clearest single instance is SkillOpt [@yang2026skillopt]. It treats one markdown skill document as the trainable external state of a frozen agent and edits it with explicit optimizer controls: rollout and reflection batches, add/delete/replace edits, a bounded textual learning rate with cosine decay, a held-out selection gate that accepts only a strictly better score, a rejected-edit buffer kept as negative feedback, and an epoch-wise slow update. Across six benchmarks, seven target models, and three harnesses it is best or tied on every cell its authors evaluate, and it reports transfer across models, harnesses, and benchmarks that reads as an empirical measurement of evidence radius rather than as a governance mechanism. Its own follow-up, SkillOpt-Lite [@shen2026skilloptlite], removes the buffer, the slow update, and the schedule, keeps the held-out gate and a consensus filter across rollouts, and matches or beats it. The gate and a consensus form of credit assignment are load-bearing; the rest are stabilizers.

Five research families instantiate complementary parts of the loop (Table REF(tab:VIII-1)). The *reflective-evolution* family proposes edits by reflecting over trajectories [GEPA, @agrawal2025gepa] and supplies the two-timescale motivation [@tiwari2026fastandslow]. *Reflective context learning* [@vassilyev2026rcl] is the most direct independent formalization: it observes that credit assignment, overfitting, forgetting, and high-variance signals persist whether the learned object lies in parameter space or context space, and its generalization penalty is the complexity term $\Omega$ of Section REF(sec:loop). The *harness-optimization* family targets orchestration rather than skills [Meta-Harness, @lee2026metaharness; AHE, @lin2026ahe; MOSS, @cai2026moss; CANTANTE, @zehle2026cantante; HARNESSEVO, @nguyen2026harnessevo] and names credit assignment as the bottleneck; by October 2026 it is the largest family in the corpus, with roughly two hundred papers citing its founding entries and a dozen scored here, among them HarnessForge and Growing Harness [@chen2026harnessforge; @li2026growingharness]. The *lifecycle* family shows that hygiene is a precondition for descent. LLM-authored skills add nothing over no skill until retirement and a bounded active set are in place [@zhang2026ratchet]; MOCHA shows that the complexity penalty $\Omega$ is a constraint frontier rather than a scalar once platform limits bind [@tanjim2026mocha]; SkillsVote attributes each outcome to skill, exploration, or environment before admitting an update [@liu2026skillsvote]; and eleven 2026 systems make retirement a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay]. The *transfer* family instruments Loop 2: measuring evidence radius one task at a time [@shalev2026ict], pooling evidence across parallel agents [@li2026combee], promoting through shared memory on a heartbeat [@qu2026coral], consolidating across a deployment's own episodes [@ling2026pace], and, in 2026, federating skill patches across clients with an auditable decision log [@yang2026federatedskill] or across deployments with a held-out merge gate and round rollback [@nie2026evolvenet].

| Family | Representative systems | What it instantiates | What it leaves open |
|------------|----------------------|------------------------|----------------------|
| Reflective evolution | GEPA; Tiwari et al. | proposal by reflection over trajectory evidence; two-timescale motivation | persistent artifact; bounded step; held-out gate |
| Reflective context | RCL | the learned object in context space; generalization penalty as $\Omega$ | cross-deployment Loop 2 |
| Harness optimization | Meta-Harness; AHE; MOSS; CANTANTE; HARNESSEVO; HarnessForge; Growing Harness | credit assignment over orchestration; source-level edits; slot attribution | governed Loop 2; access control; rollback |
| Lifecycle and multi-objective | Ratchet; MOCHA; SkillsVote; Library Drift; SkillSmith; ASSAY | hygiene as precondition; constraint frontier as the shape of $\Omega$; gated retirement | gradient-analogue closure; retirement of a promoted artifact's descendants |
| Transfer and federation | ICT; Combee; CORAL; PACE; FederatedSkill; EvolveNet; Evo2Team; XRepoSkill | empirical evidence radius; cross-client aggregation; receiving-side confirmation | cross-organization gate, lineage, rollback |

Table VIII-1. Five research families converging on artifact-layer descent, with the part of the loop each instantiates.

Read against the loop and against the four properties of Section REF(sec:gap), four claims are well supported.

1. The scaffold-versus-weights decomposition is independently confirmed. GEPA, Meta-Harness, MOSS, RCL, PACE, and the 2026 harness papers all begin from the observation that weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope; a system that updates both keeps them as separate levers [@hebbar2026sia].
2. Credit assignment is the central engineering bottleneck. AHE, CANTANTE, Meta-Harness, HARNESSEVO, SkillsVote, and the harness-optimizer evaluation of Ong et al. [@ong2026harnesseval] all identify attributing a system-level failure to one scaffold coordinate as what separates descent from trial-and-error, and it remains unsolved in the general multi-substrate case.
3. Lifecycle hygiene is a precondition for descent, not an alternative to it. A dirty artifact pool starves the gate of signal; the 2026 retirement mechanisms are the field's answer, and the one negative result cuts deeper. Once a contaminated skill has descendants, rolling it back recovers little, so gating must happen before commit [@shang2026vag].
4. No surveyed system combines automated local adaptation with governed cross-organization promotion. FederatedSkill narrows the gap on cross-client promotion and lineage, EvolveNet on the merge gate and rollback, and neither meets all four properties of Section REF(sec:gap).

## The missing architecture: governed cross-tenant scaffold optimization {#sec:gap}

Four properties define an architecture that no surveyed system instantiates:

- (a) **auto-gated Loop 1**: the commit criterion is an algorithmic threshold;
- (b) **cross-organization promotion**: Loop 2 routes artifacts between organizations (we use *cross-tenant* and *cross-organizational* interchangeably);
- (c) **versioned lineage with access control**: promoted artifacts carry versions, audit trails, and role-based access policies;
- (d) **rollback**: a bad promotion can be reverted without redeploy.

The closest approaches partition the requirements, and the October-2026 sweep sharpened the partition without closing it. FederatedSkill has (a), the strongest partial (b) in the corpus (privacy-preserving aggregation of skill patches across heterogeneous clients that sit under one operator), and partial (c) through an auditable per-modification decision log [@yang2026federatedskill]. EvolveNet has (a), a held-out merge gate at the aggregator, and (d) in the form of a rollback to the previous shared harness after a failed round, with no lineage, no access control, and clients that are benchmark partitions rather than organizations [@nie2026evolvenet]. SkillForge has (a) and (b) within one enterprise with partial (c) [@skillforge2026]. The governance-first registries have (c) without access control and (d) with evidence [@kang2026registry; @qin2026governed; @quessadavial2026acm]; the MCP control planes have access control without evaluation-gated promotion [@agenticcommunity2026mcpgateway]. Rollback, which was almost absent in the May corpus, now appears inside single deployments, as edit-level reversal [@wei2026skillsmith; @gao2026skillaudit] and as an admission test that rejects edits which cannot be undone [@sah2026evoundo], and inside one federated round. No system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion. Appendix REF(app:contrast) gives the per-system enumeration.

In machine-learning terms, what is missing is a cross-tenant aggregator with an automated evaluation gate at the scaffold layer. It would carry five parts: per-tenant artifact pools, each tagged with provenance; an aggregation step across tenants that respects tenant isolation; a held-out evaluation at the receiving tenant that blocks a promotion whenever it does not lower that tenant's patch loss; versioned lineage with access control; and a rollback envelope on every promoted artifact. The federated-learning analogy [@mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated] is useful only in the limit where artifacts are mergeable update representations; federated prompt tuning, in which participants learn a shared prompt rather than shared weights [@guo2022promptfl], is the weight-side precedent closest to that limit. In surveyed practice Loop 2 is selection and merge, and the nearest systems aggregate program edits with a language model, not by averaging.

Whether the architecture *should* be built is a question the feedback-signal class answers (Section REF(sec:signal)). Where the signal is exact, an automatically gated cross-tenant promotion of a test-validated skill is low-risk and the receiving-side evaluation is cheap. Where the signal is an observable outcome, the corner should be filled only with that receiving-side evaluation, because the sending side's outcome does not transfer; Evo2Team's four failed transfers out of twenty-two after target-side confirmation show that even a receiving-side check is necessary rather than sufficient [@wang2026evo2team]. Where the signal is judged, a human gate on Loop 2 is a design feature, and governance means lineage and rollback around a human decision. Where the signal is delayed, property (a) cannot be met and what remains is lineage and rollback without an automatic gate. Naming the four properties converts a vague gap into an audit criterion that any future system can be measured against. Naming the signal class says, for a given deployment, which of the four it should expect to meet.

## The failure surface {#sec:failure}

Patchwork scaffold maintenance introduces failure modes that weight-only systems do not have; they are the scaffold-layer entries in the technical-debt ledger that machine-learning systems have carried for a decade [@sculley2015debt]. Each is also a missing piece of the optimizer, and each dominates in a particular feedback-signal class (Table REF(tab:X-1)). This section surveys the documented attacks and degradations; it proposes no new threat model.

| Failure | What has been measured | Architectural response | Dominant class |
|------------|--------------------------------|--------------------------|----------|
| Scaffold bloat | Instruction-following accuracy falls and latency grows sharply as instruction count scales [@jaroslawicz2025ifscale]; LLM-authored skills add nothing over no skill until lifecycle hygiene is applied [@zhang2026ratchet] | Complexity penalty $\Omega$ in the gate; pruning and expiry as first-class gated operations | C1, C3 |
| Poisoned memory | High attack success against standard retrieval-augmented generation [@zou2024poisonedrag]; backdoors planted in long-term memory or knowledge bases [@chen2024agentpoison]; memory control-flow attacks across major agent frameworks [@xu2026mcfa] | Provenance on every entry; write gating; a rollback envelope [@su2026chronomem; @yu2026rollbackrepair] | C2 |
| Injection via tools and MCP | A tool's output or a connected server can smuggle instructions into context [@greshake2023injection; @debenedetti2024agentdojo]; one approved MCP configuration could later be modified without re-approval (CVE-2025-54136) [@checkpoint2025mcpoison] | Narrow tool permissions; a privilege hierarchy over instructions [@wallace2024hierarchy]; tool bindings pass the same promotion gate as any other coordinate | C2 |
| Evaluation fragility | Optimizing a proxy reward past a point lowers the true score [@gao2023overoptimization]; access asymmetries alone produce large relative gains that reflect exposure to the test [@singh2025leaderboard]; harness optimizers cannot be told from trial-and-error by downstream score alone [@ong2026harnesseval] | Held-out evaluations scoped within evidence radius, weighted toward recurring modes, re-read as the target drifts, and checked against an update's attribution | C3 (primary), C1 |
| Coordination failures | Fourteen failure modes in multi-agent systems, dominated by role confusion and context loss [@cemri2025mast] | Orchestration topology treated as a scaffold coordinate under the same gate and rollback discipline | C2 |
| Patch overfitting | A scaffold tuned to one deployment over-fits it by construction (Appendix REF(app:formal)) | Evidence-radius discipline at promotion; receiving-side held-out evaluation | C2 |
| Plasticity loss | Context rot (long-context degradation [@liu2023lostmiddle]), instruction conflict, memory pollution, tool-version drift | Expiry and rollback as explicit loop operations rather than retrospective hygiene | C4 |

Table X-1. The failure surface of patchwork scaffold maintenance, the measured evidence, the architectural response, and the feedback-signal class in which each failure dominates.

Two rows deserve a sentence beyond the table. Bloat is a signal-quality problem as well as a latency problem. Ratchet reports LLM-authored skills at no gain over a no-skill baseline against a double-digit gain for human-curated ones, and attributes the gap to lifecycle management, which in the vocabulary of Section REF(sec:loop) means that residual capture and mode discovery cannot work on a messy artifact pool [@zhang2026ratchet]. Evaluation fragility compounds because the evaluation suite is itself a patch-local artifact rather than a fixed instrument. It is optimized against: once a metric becomes the target it is gamed. It is read non-independently, because the gate scores path-dependent agent trajectories whose readings do not compose like ordinary test-set statistics. It goes stale, because the suite adapts on the same cadence as the scaffold it gates. And because failures concentrate in a finite catalogue of recurring modes, a suite that samples tasks at random under-weights exactly the families that drive the failure rate. The response in the table follows from those four properties: held-out, scoped, mode-weighted, re-read, and checked against attribution rather than only against score.

The failure surface is real, quantified by 2024 to 2026 work, and largely unmitigated in production; a survey of persistent-state agents coded from 435 works reaches the same verdict, finding the literature concentrated on accumulating and retrieving state rather than on governing, recovering, or relinquishing it [@ding2026alwayson]. Every row names a piece of the optimizer that current systems do not yet have.

## Open problems and conclusion {#sec:open}

Five open problems follow from the survey, one per feedback-signal class and one for the architecture.

1. **Exact signals: credit assignment from a failing check to a scaffold coordinate.** A test tells the loop that an output failed, not which instruction, skill, or tool binding caused it. Slot attribution [@nguyen2026harnessevo], intervention-based attribution [@chu2026agentgrad], and contrastive multi-agent attribution [@zehle2026cantante] each solve one substrate's case; a general method is the bottleneck named by every harness-optimization paper.
2. **Observable outcomes: receiving-side evaluation before promotion.** Four systems now evaluate at the receiving side and one of them still misses nearly a fifth of its transfers; the gate that a federated scaffold optimizer needs is a held-out test at the receiving tenant, proposed but not yet built [@yang2026fao].
3. **Judged signals: calibrating a gate that is itself being edited.** Of thirteen weight-side rubric-reward methods, five co-evolve the rubric with the policy, and none of those five reports agreement with human judgment; on the scaffold side three systems report judge calibration and none calibrates a judge under edit. The nearest measurement is on the human side, where evaluators' criteria drift as they grade [@shankar2024validators]; the reflexive gate of Section REF(sec:signal) has no measured instance on the scaffold side.
4. **Delayed signals: telling descent from search.** Where the outcome arrives after many edits, an optimizer's gains cannot be distinguished from trial-and-error by outcome alone [@ong2026harnesseval]; evaluating harness optimizers against their attribution claims rather than their scores is the open method.
5. **The governed cross-tenant corner.** Properties (a) through (d) of Section REF(sec:gap), with the receiving-side gate of problem 2 as the piece that would make cross-organization promotion safe in the two classes where it should be automatic.

The field has built an external adaptation layer for language models but not the optimizer that should govern it. The reason the layer belongs where it is was established by the two papers this article completes: reliability over long outputs hinges on a sparse set of key decisions, and inside a bounded deployment those decisions fail in a small, recurring catalogue of modes that a targeted budget of fixes can cover. The place to spend that budget is a persistent, inspectable, reversible artifact outside the weights. Once the loop that edits it is gated and scoped, the arrangement is not a patch on an inadequate model but the architecture that the error structure calls for.

The survey shows how far practice has come toward that loop, and the distance is uneven. The local loop closes automatically in most research systems and in a growing number of production ones; evidence is batched before acceptance; retirement and expiry have become first-class; lineage has reached production memory. What has not moved is the second loop. No surveyed system promotes a validated edit across an organization boundary under an automatic gate with lineage, access control, and rollback, and the signal-class analysis says this is not one gap but four, each with its own reachable answer. The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization, and the instruments that judge each edit are themselves part of the moving scaffold, so the same evidence-radius and lifecycle discipline the optimizer needs must extend to the gates that judge it.

## Acknowledgments {-}

The authors used an AI assistant (Claude, Anthropic) to help search the literature, check citations, and edit prose; all claims, scores, and classifications were reviewed and approved by the authors.

```{=latex}
\bibliography{references}
\appendix
```

## Formal statement of artifact-layer descent {#app:formal}

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
Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability. In the feedback-signal classes of Section REF(sec:signal), $\varepsilon_t$ is near zero for an exact check (C1), bounded by batching for an observable outcome (C2), equal to the judge's bias and bounded only by calibration for a judged signal (C3), and unavailable per edit for a delayed signal (C4).

### Convergence (informal)

Add (A3) proposal coverage, that at every non-gate-stable scaffold $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \le -\delta$; (A4) effective compactness of the reachable orbit; and (A5) persistent acceptance with summable bias, $\sum_t p_t(\gamma_t + \tau_t) = \infty$ and $\sum_t p_t \varepsilon_t < \infty$; and let $0 \le L_D \le B$. Then $L_D(\theta_s^t)$ is a non-negative supermartingale up to summable noise, it converges almost surely, and the limit set of $\{\theta_s^t\}$ is gate-stable: no admissible edit clears the gate with negative expected directional loss in the limit. This is convergence of the loss and stability of the gate decision, not convergence to an optimum; a globally suboptimal gate-stable scaffold is consistent with the result, because $Q_t$ may never propose the improving edit or $\widehat{\Delta}$ may be biased to reject it. In a non-stationary deployment ($D = D_t$) the same mechanism tracks a moving optimum rather than converging once, which is why recency weighting, pruning, expiry, and rollback are the scaffold-level analogues of continual-learning machinery rather than optional hygiene.

### Correspondence

Table REF(tab:A-1) pairs each optimization concept with its scaffold analogue. Credit assignment here is attribution, not backpropagation. Scaffold systems do not differentiate through instruction files; they trace an output error to an upstream coordinate, manually or with a judge or verifier. The descent argument needs only that this attribution succeeds with non-zero probability per failure, assumption (iv) of Section REF(sec:loop).

### Worked cases

*Retrieval.* Failures recur because retrieved context omits the decisive clause. Attribution traces the error to the retrieval coordinate: chunking, query rewriting, metadata filter, embedding model, reranker, or context-packing rule. The candidate edit tightens chunk boundaries or adds a metadata constraint, and the gate checks that recall and answer accuracy improve on the patch evaluation without degrading adjacent cases. Signal class C1 or C2.

*Pitch review.* The system repeatedly overrates decks that claim a large market without numbers. The failure cluster points at an under-specified rubric coordinate. The edit changes "evaluate market size" into "require a numeric estimate and a source; if absent, cap the score". The gate runs the revised rubric against held-out decks with human scores. The edit changed the gate that will judge the next edit: the reflexive gate of Section REF(sec:signal), class C3.

*Tool use.* Calls fail because optional parameters are under-specified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The edit adds required fields or a pre-call uncertainty check; the gate checks that tool-call failures fall without raising refusals or latency. Class C2.

*Memory.* A stale customer preference is repeatedly retrieved and causes bad decisions. The responsible coordinate is a memory entry together with its provenance, priority, and expiry policy. The edit corrects, expires, or version-tags the entry; the gate checks that future behavior improves without erasing useful history. Class C2, with the correction itself observable only when a later outcome reveals it.

## Gate families and feedback-signal classes {#app:gates}

Section REF(sec:loop) collapses every production gate into one per-edit test $G_t$ on an estimate of the loss change. Surveyed systems instantiate that test in several distinct ways, and some of them are better read as proposal pruning that precedes the per-edit gate than as estimators of $\widehat{\Delta} L_D$. Table REF(tab:B-1) lists the families, the slot each occupies, representative systems, and the feedback-signal class (Section REF(sec:signal)) each family serves.

| Gate family | What it estimates | Slot in Section REF(sec:loop) | Signal class | Representative systems |
|------------|----------------------|--------------|--------------|--------------------|
| Surrogate verifier | Pass or fail from tests, a symbolic checker, or an exact match | Per-edit gate $G_t$ | C1 | DGM (sandboxed code), SkillOpt (held-out exact match), Voyager (game-state check: C2) |
| Evaluation cascade | $\widehat{\Delta} L_D$ on a held-out task suite, cheap-to-expensive evaluators | Per-edit gate $G_t$ | C1 when the suite is exact; C2 when it is a task suite | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| RL threshold | Reward improvement against a deployment threshold | Per-edit gate $G_t$ | C2 | SkillRL, SAGE, EvolveR, PACE |
| LLM judge with calibration | Pairwise or rubric score, calibrated against human agreement | Per-edit gate $G_t$ | C3 | SkillForge (Loop 1), CASCADE (consolidation gate) |
| Reviewer judgment | Human credit assignment by pull-request review or expert sign-off | Per-edit gate $G_t$, human-instantiated | C3 (and C2 when the reviewer has outcome data) | SkillForge (Loop 2), Sierra Agent OS 2.0, Anthropic skills repository |
| Semantic merge | Whether a candidate duplicates or conflicts with existing artifacts | Proposal pruning before $G_t$ | C4 (also a pre-filter in C2, C3) | NanoResearch orchestrator, FederatedSkill server agent |
| Archive selection | Whether a candidate fills an unfilled cell in a behavior-diversity archive | Proposal pruning before $G_t$ | C4 | AlphaEvolve (MAP-Elites), ADAS |
| Multi-sample agreement | Whether $k$ independent proposals or evaluations agree; false-accept rate decays as $p^k$ rather than variance as $1/k$ | Aggregation filter on the estimate | C2, C3 noise absorption | Under-explored; SkillOpt-Lite's consensus attribute mining is the nearest instance |

Table B-1. Gate families, their slot in the formalism, and the feedback-signal class each serves.

The first five families populate $G_t$ directly and inherit the descent guarantee of Appendix REF(app:formal) under its assumptions. Semantic merge and archive selection are not estimators of $\widehat{\Delta} L_D$; they constrain the proposal distribution, and the descent argument applies to the composition of pruning and gate. Multi-sample agreement is listed because it is the correct analogue of "wait for $k$ pieces of evidence before accepting an edit", a different operation from mini-batch averaging and one that should not be conflated with it. Read down the signal-class column. The only families available to a judged (C3) deployment are the two whose estimator is a judge, and the only families available to a delayed (C4) deployment are the two that do not estimate the loss change at all. That is the structural content of Section REF(sec:signal).

## Data appendix {#app:data}


**Corpus size.** The corpus was assembled in two passes. The May-2026 pass scored 130 unique systems (140 substrate-level rows in `p3_master_scores.csv`); the October-2026 pass added 126 systems (133 rows in `p3_refresh_2026-10.csv`, four of which re-audit May systems rather than adding one), for 256 unique systems and 269 substrate-level rows. A system may be scored on several substrates, so row counts exceed system counts; the maturity table of Section REF(sec:findings) counts rows.

**Core / contrast split.** 204 of the 256 systems satisfy the patch-local discriminator (score ≥ 3 on at least one substrate) and form the core corpus, 99 of them from the May pass. The remaining 52 (31 from the May pass) form the contrast corpus: commonly described as agentic or self-improving in public discourse but failing at least one discriminator. Appendix REF(app:contrast-1) enumerates representative contrast systems from the May pass; each October contrast row carries its exclusion reason in the released CSV.

**Inclusion criteria.** Any system that (a) wraps a foundation model with at least one persistent artifact updated from deployment signal, or (b) is named in the public discourse as a "self-improving," "scaffolded," or "agentic" system. The contrast set (Self-Refine, ReAct, TextGrad, OPRO, engineer-authored convention files; Appendix REF(app:contrast-1-1)) is included so the discriminator has something to mark against; Appendix REF(app:contrast-1-2) separately lists core-corpus systems that fail the composite two-loop criterion.

**Exclusion criteria.** Systems whose only update mechanism is weight-level fine-tuning or RLHF: these are model-side, not scaffold-side, and belong to the self-evolution literature this paper differentiates from. Systems with no public evidence of deployment (white papers without code, demos, or production claim).

**Evidence tiers.** Each system carries one or more of: (T1) peer-reviewed publication; (T2) arXiv preprint; (T3) production claim with metrics; (T4) open-source artifact; (T5) industry-blog or interview-level documentation. T1/T4 carry highest weight in cluster analysis; T3 is admissible where the claim is concrete (specific benchmark, named integration target); T5 is admissible only when corroborated by T1–T4 elsewhere. Tier flags are propagated to cluster claims through the per-row evidence column of the released CSV; T3 production claims are not pooled with T1/T2 evidence when computing cluster-level statistics.

**Evidence-tier distribution.** Of the core corpus, approximately one quarter carry T1 evidence, roughly half carry T2 evidence, and the remainder carry T3 or T4 evidence as the primary tier.

**Survey window and dating.** January 2023 to May 2026 for the first pass; June to October 2026 for the second, a systematic sweep in three parallel strands (skills and skill lifecycle; harness, context, and LLMOps governance; memory governance, competing surveys, and rubric rewards) rather than a targeted refresh, so the per-substrate statistics of Section REF(sec:findings) are computed on both passes together. The cutoff is October 2026. Preprint-only systems carry T2 evidence, recorded per row in the released CSV. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.

**Scoring discipline.** Each system received a substrate-by-substrate 0–5 score against the rubric of Section REF(sec:method) of the main text and an integrated patch-local-adaptation score (PP) in {0,1,2,3,3.5,4,4.5,5}. Half-scores were used sparingly when one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). Scoring is single-rater; Appendix REF(app:scores) and Appendix REF(app:contrast-1) together expose representative per-system scores and exclusion reasons so readers can audit ambiguous classifications independently.

**Composite two-loop criterion (sensitivity analysis).** The strict count of fourteen research systems satisfying the composite two-loop criterion changes under two natural relaxations. Relaxation (a) counts any of versioning, lineage, or rollback as Loop-2 governance: on the May pass the count rises to approximately eighteen by re-admitting MAE, MetaGen, MetaReflection, and CLIN, and on the October pass it admits the seven systems that promote across users, clients, teams, or repositories without versioning or lineage (EvolveNet, Evo2Team, XRepoSkill, ShareMem, RASO, Spotify's recommendation loop, and Future AGI's prompt lifecycle). Relaxation (b) admits session signal that updates optimizer state without persisting an artifact distinct from optimizer state: on the May pass the count rises to approximately sixteen by re-admitting DSPy and TextGrad; it adds no October system, because the October contrast rows are benchmarks, evaluation and attack studies, registries, audits, and conceptual frameworks, plus one orchestrator whose adaptation lives in the weights, none of which persists optimizer state as its only artifact. The qualitative findings ([Auto × Auto] well populated; [Human × Auto] empty; the other human-authored cells occupied only by registries and curation workflows that fail the composite audit; the governance-first cluster in [None × Auto]; the cross-tenant governed-optimization corner empty) survive both relaxations.

---

## The mechanism stack and continual-learning notes {#app:mechanism}

### The mechanism stack {#app:mechanism-1}

The abstract update rule of Section REF(sec:loop) expands into six operations that every patch-local system must perform, whether explicitly engineered or accidentally emergent.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, eval regressions, tool-call failures. The Loop-1 signal source. Without it, $z_t$ has no provenance.
2. **Mode discovery and credit assignment.** Cluster repeated failures into patch-specific error modes (the *Architecture of Errors* catalog [@arbuzov2026architecture], instantiated locally per patch) and attribute each mode to the scaffold coordinate responsible for it (Appendix REF(app:formal)).
3. **Delta synthesis.** Convert a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, an eval case. This produces $z_t$.
4. **Delta validation.** Estimate whether the edit reduces $L_D$ without collateral damage on adjacent inputs. The gate $G_t$ is Auto-gated when the check is an algorithmic criterion, Human-gated when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted edit stays in the local fork or climbs the scope hierarchy: project, stack, organization, cross-tenant. Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, detect over-fitting. Without this, accumulated edits produce the scaffold-level analog of plasticity loss.

Each operation is the locus of a separate engineering discipline. Surveyed systems implement them partially and unevenly: research full-auto systems excel at (3) and (4); production governance leaders at (5); industry hybrids at most of (1)–(5) but rarely (6). Implementation patterns are deferred to follow-on practitioner work.

### Loop 1 and Loop 2 as descent steps of different radius {#app:mechanism-2}

Loop 1 proposes and validates local descent steps on a single $L_D$. Loop 2 expands the update radius. It selects, merges, and promotes accepted local edits so that they apply to a larger averaging set of patch losses. USER-level acceptance descends on a single $L_D$. PROJECT promotion descends on a project-averaged loss. STACK promotion widens the average further. CORE or cross-tenant promotion descends on a federated average. The two-loop design space is therefore not just a taxonomy of engineering patterns: it is a taxonomy of *which loss each surveyed system is descending on*, gated by which estimator.

### Overfitting in scaffold adaptation {#app:mechanism-3}

In weight training, overfitting is usually a defect. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve cross-patch generality; they must smooth over local conventions and rare workflow-specific failures. A deployment patch needs the opposite: selective specialization to local residuals. The scaffold is therefore an intentionally overfittable layer, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold that improves one repository, hospital workflow, or legal diligence process may degrade performance elsewhere. That is not a contradiction; it is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

In non-stationary patches ($D = D_t$), the same descent mechanism tracks a moving optimum rather than converging once. This is why recency weighting, replay, pruning, expiry, and rollback are not optional hygiene; they are the scaffold-level analogs of continual-learning machinery.

---

## Contrast set, matrix membership, and closest approaches (May 2026 corpus) {#app:contrast}

The October 2026 additions are placed in the cells of Section REF(sec:design) of the main text and listed in Appendix REF(app:scores); the per-system discussion below is the May 2026 audit on which the main text's counts build.

### Contrast set {#app:contrast-1}

Appendix REF(app:contrast-1) serves two audits. **Appendix REF(app:contrast-1-1)** lists representative members of the contrast corpus (31 systems that fail the patch-local discriminator, score < 3 on every substrate), so the discriminator has something to mark against. **Appendix REF(app:contrast-1-2)** lists core-corpus systems (score ≥ 3 on at least one substrate) that nonetheless fail the stricter composite two-loop criterion of Section REF(sec:method), so the asterisked entries of the Section REF(sec:design) matrix are auditable. Systems named in the text but not scored as rows in `supplementary/p3_master_scores.csv` (ReAct, MetaGen, MetaReflection, CLIN, ACE) are classified from their papers and marked with a dagger.

#### Contrast corpus: fails the patch-local discriminator {#app:contrast-1-1}

| System | Year | Discriminator failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Self-Refine [@madaan2023selfrefine] | 2023 | No persistent artifact | In-context iteration only |
| ReAct [@yao2023react]† | 2023 | No persistent artifact | Thought-act-observe loop is intra-session |
| TextGrad [@yuksekgonul2024textgrad] | 2024 | No artifact distinct from optimizer state | Textual-gradient optimization; SkillOpt [@yang2026skillopt] (Section REF(sec:families); Appendix REF(app:families)) adds the persistent `best_skill.md`, held-out validation gate, rejected-edit memory, and textual learning-rate schedule that TextGrad lacks. |
| OPRO, Toolformer | 2023 | No persistent deployment artifact | Optimization or tool use inside a single training or inference run |
| Aider conventions, Lovable knowledge | 2024 | No feedback loop | Engineer-authored convention files |
| AGENTS.md (as a standard) | 2025 | No feedback loop | Cross-vendor artifact format; adoption measured, adaptation absent (Section REF(sec:findings)) |
| LangChain Skills, HuggingFace Agent Skills, CrewAI Skills | 2025–2026 | No feedback loop | Curated skill packs without failure-triggered update |
| Tran & Kiela [@tran2026singleagent] | 2026 | Not a system | Single-agent baselines match or beat multi-agent under matched thinking-token budgets; constrains S5 claims (see Section REF(sec:findings)) |

#### Core corpus, fails the composite two-loop criterion {#app:contrast-1-2}

| System | Year | Composite-criterion failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Reflexion [@shinn2023reflexion] | 2023 | No Loop 2 | Per-agent episodic memory without promotion |
| Generative Agents | 2023 | No Loop 2 | Per-agent reflection + importance memory |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks |
| Mem0 (vanilla) | 2024 | No Loop 2 | Per-user memory; no cross-context promotion |
| Zep | 2024 | No Loop 2 | Per-agent/session knowledge graph |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent |
| DSPy | 2023 | No artifact distinct from optimizer state | Prompt-template optimization; SkillOpt [@yang2026skillopt] (Section REF(sec:families); Appendix REF(app:families)) realizes the artifact-bearing form. |
| MetaGen† | 2026 | No Loop 2; no cross-session persistence | Role pool dynamic within single inference call |
| MAE (Multi-Agent Evolve) | 2025 | No Loop 2 | Co-evolution within Proposer/Solver/Judge triplet |
| MetaReflection† | 2024 | No Loop 2 | Per-agent semantic memory |
| CLIN† | 2023 | No cross-instance promotion | Causal abstractions per-agent-per-environment |
| LangGraph, AutoGen, CrewAI | 2023–2024 | Framework only | Orchestration frameworks; not deployed systems |
| W&B Weave, Agenta, Langfuse | 2024 | No Loop 1 | Observability / eval-as-code |
| Mobile-Agent-E, Cradle, OS-Copilot | 2024–2025 | No Loop 2 | Self-evolving but per-session/per-deployment |
| Agent S, Agent S2 | 2024–2025 | No Loop 2 | Computer-use agentic framework |
| ACE [@ace2025agentic]† | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook |
| Cursor Rules (vanilla) | 2024 | No Loop 2 | Per-project artifacts |
| GitHub Copilot custom instructions, Windsurf, Continue.dev, Zed AI rules | 2024 | No Loop 1 | Engineer-authored at repo base branch |
| Replit `replit.md` | 2025 | Loop 2 absent | Self-writing scaffold but per-workspace |

The entries above cover the main exclusion families (in-context-only; no feedback loop; not a system) and the main composite failures (no Loop 2; framework-only; engineer-authored without failure trigger; optimizer-state-only); finer-grained per-system breakdowns are deferred to follow-on practitioner work.


### Survey detail {#app:contrast-2}

This appendix carries the cell-by-cell discussion of the two-loop matrix from Section REF(sec:design), the closest-approaches enumeration that supports Section REF(sec:gap), and the deployment-dependence argument. It supplies the verification material for Sections REF(sec:design)–REF(sec:gap).

#### Two-loop matrix: cell-by-cell discussion {#app:contrast-2-1}

The named membership of the Section REF(sec:design) matrix (Figure 3):

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, Sierra Agent OS 2.0†, Cognition Devin† | MAE\*, MetaGen\*, MetaReflection\*, CLIN\*, DSPy\*, TextGrad\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in the May-2026 pass]** | *(none)* |
| **Loop-1 None** | ExpeL (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repository\* | Self-Refine\*, ReAct\*, Mem0\* |

*Asterisks fail at least one composite-two-loop criterion; included for contrast.* † Industry exemplar evaluated using vendor documentation as primary evidence. DSPy and TextGrad sit in [Auto × None] because their Loop 1 is automated but persists only optimizer state (Appendix REF(app:data), relaxation (b)). The matrix is restricted to the 22 systems of the strict composite audit plus SkillOpt; Appendix REF(app:scores) also assigns Loop-1 / Loop-2 entries to systems outside that audit (COSPLAY, Cuadros et al., PACE, CORAL, GEPA, Meta-Harness, MOSS, and RCL from the May pass, and every October-2026 row), but those entries are read from the papers and were not re-audited under the composite criterion, so they are neither placed in the matrix nor counted in Section REF(sec:method).

**[Auto × Auto]** is most populated (twelve systems). Every member has a machine-evaluated decision criterion on both loops. Velocity is the cluster's defining property; the lack of cross-organizational governance is its uniform weakness.

**[Auto × Human]** is the production-viable cell: Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. The pattern reconciles automation velocity with reviewer accountability. SkillForge's LLM-judge + reviewer pipeline is the architectural exemplar. CASCADE, Sierra Agent OS 2.0, and Devin instantiate variants; the industry exemplars (Agent OS 2.0, Devin) are marked with † because vendor documentation rather than peer-reviewed metrics is the primary evidence.

**[None × Auto-gated]** holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 (eval-gated CI blocks promotion on regression), but no Loop 1 in the patch-local sense, because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated.

**[Human × Auto]** is empty by engineering logic: if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping); no published example exists.

**[Human × Human]** is empty in the May-2026 pass; the October-2026 pass places MCP registries and a community hub here (Section REF(sec:design) of the main text). A candidate occupant would be a reviewer-authored-and-reviewer-promoted artifact pipeline targeting solo and small-team workflows where automation cost exceeds review latency. No public example was found in the survey window.

**[Human × None]** was judged structurally improbable in the May-2026 pass, on the argument that a system requiring human authorship on Loop 1 but with no Loop 2 collapses to "engineer-edits-a-config" and is not patch-local in the sense of Section REF(sec:loop); the October-2026 pass found its occupants in the curation workflows of Section REF(sec:design) of the main text.

**DGM dual-mode note.** DGM operates in both [Auto × Auto] (primary archive-based evolution) and [Auto × Human] (sandboxed code-modification review) modes depending on deployment configuration; we list it once in the dominant cell.

#### Closest approaches to governed cross-tenant scaffold optimization {#app:contrast-2-2}

The four properties of governed cross-tenant scaffold optimization are (a) auto-gated Loop 1, (b) multi-tenant cross-org promotion, (c) versioned lineage with RBAC, (d) rollback. Closest approaches partition the requirements:

- **AlphaEvolve** has (a) and partial (b) within a single organization; no cross-org promotion mechanism.
- **NanoResearch** has (a) at the research level; no enterprise governance layer described.
- **SkillOpt** has (a) fully and partial (c) via the exported `best_skill.md` artifact plus protected slow-update field; reports positive cross-model, cross-harness, and cross-benchmark transfer as empirical evidence-radius measurement; does not implement (b) cross-organizational promotion or (d) explicit rollback. The Appendix REF(app:families) walkthrough maps every SkillOpt design decision to its Section REF(sec:loop) counterpart.
- **CORAL** [@qu2026coral] has partial (a) via heartbeat-gated promotion and is the only system in the corpus that implements asynchronous multi-agent Loop 2 within one organization through shared persistent memory; no (b) cross-organizational scope, no formal (c) RBAC, no (d) rollback.
- **PACE** [@ling2026pace] has (a) at the small-model production timescale and a fast/slow two-timescale Loop 1 + Loop 2 that consolidates across one deployment's own episodes rather than across deployments; no (b), no formal (c) or (d). PACE is the closest demonstration that the two-loop architecture is implementable under small-frozen-model constraints.
- **Meta-Harness** [@lee2026metaharness] has (a) over the harness substrate (S5) with a filesystem-of-candidates credit-assignment record that functions as the accumulated history $H_t$ of Section REF(sec:loop); no Loop-2 cross-organizational promotion, no RBAC, no rollback.
- **SkillForge** has (a) and (b) within one enterprise, partial (c) via VFS commits; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has (b) and partial (a); the GitHub-style Workspaces provide some lineage but not RBAC-with-rollback in the strict sense.
- **FederatedSkill** [@yang2026federatedskill] has (a) and the strongest partial (b) in the corpus: heterogeneous clients (backbone-plus-harness profiles under one federation operator) exchange semantic skill diffs, and a server-side evolution agent applies, adapts, or rejects each patch per client; partial (c) via an auditable decision log recording source patch, reward, and justification per modified path; no RBAC, no (d).
- **SkillClaw** [@ma2026skillclaw] has partial (a) via a nightly validation step and partial (b) across users of one shared, synchronized skill repository; no (c) or (d) reported.
- **ChronoMem** [@su2026chronomem] has (d) and the versioning half of (c) for the memory substrate alone (whole-memory snapshots, version histories, natural-language rollback inside Google's Agent Development Kit); no Loop 1, no (b), no RBAC.
- **Vellum / Braintrust / LangSmith Hub** have (c) and (d) explicitly but no (a) or (b) in the strict sense; these are governance-first systems by construction.

No surveyed system combines (b), (c), and (d) under any gate type. The cross-organizational governance triad is itself unfilled, independently of whether Loop 1 is auto-gated.

#### Deployment-dependence of the missing architecture {#app:contrast-2-3}

Whether the corner *should* be filled is deployment-dependent. In safety-critical domains (medical decision support, legal advice, financial advice), reviewer-judgment gates may be a design feature rather than a defect, and the human latency is the point. The narrower survey claim is what matters: no public system currently combines automated local scaffold evolution with governed cross-organization promotion, versioned lineage with RBAC, and rollback. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. The shortest demonstrable path appears to build on AlphaEvolve's cascade evaluator and MAP-Elites archive, extending federation from within-DeepMind multi-target to cross-customer multi-tenant. The architectural surface, not the timeline, is what this paper claims.

---

## The convergent research families, system by system {#app:families}

This section carries the May–September 2026 walkthroughs; the October 2026 additions to each family are described in Section REF(sec:families) of the main text and scored in Appendix REF(app:scores).

This appendix expands Section REF(sec:families) along two axes. Appendix REF(app:families-1) indexes the landscape; Appendices REF(app:families-2)–REF(app:families-3) walk SkillOpt mechanism-by-mechanism; Appendices REF(app:families-4)–REF(app:families-8) walk each convergent research family, stating its Section REF(sec:loop) mapping explicitly and naming what it leaves open; Appendix REF(app:families-9) synthesizes four claims supported by the families as a whole; Appendices REF(app:families-10)–REF(app:families-11) carry the Section REF(sec:gap)-property audit of SkillOpt and its published cost-per-point figure.

### The convergent landscape {#app:families-1}

SkillOpt [@yang2026skillopt] is the cleanest current instance of artifact-layer descent in our survey, but it sits alongside at least eighteen independent research threads in 2025–2026 that converge on the same disciplined gradient-like update mechanism for the scaffold layer. The convergence is striking because it happens *from different starting points*: GEPA and Tiwari et al. start from prompt-optimization and continual-learning respectively; RCL starts from cognitive-agent learning; Meta-Harness, AHE, MOSS, CANTANTE, and Ong et al. start from harness engineering; MOCHA and Ratchet start from skill-deployment constraints; ICT, Combee, CORAL, and PACE start from cross-task / multi-agent / production-deployment angles. Each system instantiates a different subset of Section REF(sec:loop)'s five conditions, and each exposes a different gap.

The landscape table of Section REF(sec:families) indexes the families by Section REF(sec:loop) mechanism and by what each leaves open; the subsections below walk each family in detail. By substrate (Section REF(sec:method)), GEPA and RCL operate on the prompt and context layer (S1–S2); the harness family on orchestration (S5), with MOSS extending to source code (S2+S5); MOCHA and Ratchet on skills under deployment constraints (S2); the transfer family on integrated memory-plus-orchestration stacks (S3+S5); and SkillOpt on an S2-led integrated stack.

Read against Section REF(sec:gap), no member of any family combines (a) auto-gated Loop 1 with (b) cross-organizational Loop 2, (c) versioned lineage with RBAC, and (d) rollback. The Section REF(sec:loop) picture is realized in fragments across the families; the Section REF(sec:gap) gap is confirmed by every member.

### SkillOpt: full correspondence {#app:families-2}

The table below extends the Section REF(sec:families) compact correspondence with the Section REF(sec:loop) role of each component and an algorithm-level pointer into SkillOpt's published procedure (their Algorithm 1).

| Section REF(sec:loop) quantity | SkillOpt instantiation | Section REF(sec:loop) role explained | Algorithm pointer |
|--------------|------------------------|------------------------|------------------------|
| $\theta_s$ (scaffold) | `best_skill.md` — a 379–1,995-token markdown document | the trainable external state of the frozen target model; persistent and exported as the deployment artifact | $s_{\text{best}}$ (Algorithm 1, lines 1, 22, 37) |
| $L_D$ (patch loss) | benchmark-native hard score / exact-match on a held-out test split | scalar quality signal that the optimizer is implicitly minimizing | $\textsc{Evaluate}(M, h, s, D)$ (lines 2, 17, 37) |
| $Q_t$ (proposal) | optimizer-model reflection over failure and success minibatches; failures and successes analyzed separately, then merged with priority on failure fixes | proposal distribution conditioned on accumulated rollout evidence and current scaffold | optimizer calls $O$ for failure analysis, success analysis, and merge (lines 9–11) |
| $z_t$ (edit) | structured add/delete/replace patch on the skill (or rewrite-from-suggestions in rewrite mode) | the candidate update applied via $\oplus$ to the current scaffold | rank/clip to $\eta_t$ edits, apply to obtain $\tilde s$ (lines 12–13) |
| $\eta_t$ (textual learning rate) | bounded per-step edit budget; constant / linear / cosine / autonomous schedules; default cosine with floor $\eta_t=2$ | edit-magnitude controller; the Section REF(sec:loop) *learning rate* in textual form | rank/clip step (line 12); schedule applied per epoch |
| $G_t$ (gate) | held-out selection-split accept gate, strictly greater than current selection score | the per-edit gate $G_t$ — accepts only when $\widehat{\Delta}_{z_t} L_D$ improves the selection score | comparison at line 20; cache lookup at lines 14–18 |
| rejected-edit buffer | epoch-local store of failed proposals and the score drop they caused | converts rejected steps into negative feedback for later proposals within the same epoch; zero deployment cost | $\mathcal B$ updated at line 26; reset at line 5 |
| slow/meta update | epoch-end longitudinal guidance written to a markup-fenced protected slow-update field, still passed through $D_{\text{sel}}$ | second-order consolidation across adjacent epochs; the Section REF(sec:loop) "step-level edits cannot overwrite the protected slow-update field" decomposition | lines 28–31; gate applied to injected guidance |
| optimizer-side meta skill | $m_{\text{meta}}$ — a prompt-side summary of which edits helped, which failed, and which failures persisted | training-time guidance for $Q_t$; never shipped with the deployed artifact | lines 33–34 (training-side only) |

The mapping is one-to-one at the level of Algorithm 1: every Section REF(sec:loop) quantity has a named, code-level counterpart, and every SkillOpt control surface maps onto a Section REF(sec:loop) quantity. SkillOpt is therefore the cleanest published instance we are aware of in which the Section REF(sec:loop) picture is *mechanism* rather than *metaphor*: all five Section REF(sec:loop) conditions are instantiated.

### What SkillOpt does that prior textual-optimization systems do not {#app:families-3}

SkillOpt's own experiment design compares it against six baselines under an identical protocol (same target model, same held-out test split, same scorer). The differentiation below frames each baseline in Section REF(sec:loop) vocabulary and identifies the Section REF(sec:loop) mechanism the baseline lacks. The through-line is the paper's thesis: *the scaffold/evolution layer needs a disciplined gradient-like update mechanism*, and the live distinction across baselines is which Section REF(sec:loop) conditions each one fails.

- **TextGrad** [@yuksekgonul2024textgrad]**.** Backpropagates textual feedback through `tg.Variable` objects in a compound system. In Section REF(sec:loop) terms: $z_t$-style edits exist, but $\theta_s$ does not — TextGrad has no artifact distinct from optimizer state. There is no $\eta_t$ schedule, no held-out $G_t$, and no rejected-edit buffer. SkillOpt's measured advantage over TextGrad on direct chat ranges from $+5.9$ to $+34.0$ points across benchmarks at GPT-5.5 scale and is uniformly positive at all seven target-model scales. This matches our Appendix REF(app:contrast-1) classification of TextGrad as failing the patch-local discriminator on persistence; SkillOpt closes precisely that gap.

- **GEPA** [@agrawal2025gepa]**.** Reflective prompt evolution with Pareto-style multi-candidate selection. Closer than TextGrad in that it carries multiple candidates and a selection step. In Section REF(sec:loop) terms: $Q_t$ is real, but the optimization target is a prompt rather than a persistent skill artifact, $G_t$ is not the strictly-greater held-out gate of Section REF(sec:loop), and there is no $\eta_t$ bound — accepted edits can wholesale rewrite. SkillOpt matches or outperforms GEPA in every reported cell of its main results table [@yang2026skillopt]; we do not restate the per-cell deltas here.

- **Trace2Skill** [@ni2026trace2skill]**.** Distils trajectory-local lessons into reusable skill artifacts. In Section REF(sec:loop) terms: $\theta_s$ exists, but there is no iterative $G_t$ — Trace2Skill mines skills offline rather than running a held-out validation loop that accepts or rejects each candidate. Our Section REF(sec:loop) mechanism stack therefore loses *delta validation* (operation 4) and the *rejected-edit buffer*. SkillOpt's measured gap over Trace2Skill is $+5.0$ to $+19.0$ points across benchmarks at GPT-5.5 direct chat.

- **EvoSkill** [@alzubi2026evoskill]**.** Skill-folder evolution under failure analysis, deployed harness-side. The strongest baseline on the Codex and Claude Code harness rows. In Section REF(sec:loop) terms: $\theta_s$ is a folder rather than a single artifact, and credit assignment via failure analysis is genuine, but there is no $\eta_t$ bound on per-step folder edits and no rejected-edit buffer. SkillOpt beats EvoSkill by $+14.0$ inside Codex and $+3.2$ inside Claude Code on the GPT-5.5 five-benchmark average.

- **Human skill** (expert-written, 145–516 tokens per benchmark). In Section REF(sec:loop) terms: $\theta_s$ exists, but Loop 1 does not — the artifact is static at deployment. Provides the no-Loop-1 ceiling.

- **One-shot LLM skill** (generated zero-shot from a benchmark description by GPT-5.5, never updated). In Section REF(sec:loop) terms: $\theta_s$ exists; Loop 1 does not; $Q_t$ fires exactly once with no rollout evidence. The "untrained scaffold" baseline.

ABSTRAL [@song2026abstral] and EvoTest [@he2025evotest], referenced in SkillOpt's related work but not measured in their table, operate at the multi-agent design / test-time configuration layer rather than the persistent skill layer; they are out of scope for the artifact-layer-descent comparison.

Synthesizing across all six measured baselines: the live difference is whether the loop has (i) a persistent edit-target distinct from optimizer state ($\theta_s$), (ii) a held-out validation gate on each accept ($G_t$ with $\widehat\Delta$ estimator and accept threshold $\tau_t$), (iii) negative-feedback retention (rejected-edit buffer feeding $Q_t$), and (iv) a bounded learning rate with a schedule ($\eta_t$ + cosine/linear/constant/autonomous). SkillOpt is the first published system in our survey that instantiates all four simultaneously, and it does so as a single offline training loop whose deployed artifact remains a 379–1,995-token markdown file requiring no inference-time optimizer calls.

A follow-up, SkillOpt-Lite [@shen2026skilloptlite], asks which of these controls are necessary. It reformulates skill optimization as zeroth-order optimization, keeps three principles (file-system-based trajectory exploration, consensus attribute mining that extracts attributes common across heterogeneous rollouts and discards single-sample eccentricities, and an independent held-out validation gate that is strictly disjoint from the training failures), and removes minibatch reflection pooling, the rejected-edit buffer, the slow/meta update, and the textual learning-rate schedule. It reports faster convergence and higher scores than full SkillOpt (LiveMath +8.8 points at GPT-5.5 and +25.4 at GPT-5.4-nano). Read against the four conditions above, this is evidence that (ii) the gate and a consensus form of credit assignment are load-bearing, while (iii) negative-feedback retention and (iv) the bounded learning rate are stabilizers whose value is benchmark-dependent; the finding does not touch the Section REF(sec:gap) governance properties.

### GEPA, Tiwari, and the reflective-evolution family {#app:families-4}

The immediate predecessor to SkillOpt's optimizer framing is **GEPA** [@agrawal2025gepa]. It shows that natural-language reflection over execution trajectories can provide a richer adaptation signal than sparse scalar rewards for prompt evolution in compound AI systems. GEPA samples trajectories containing reasoning steps, tool calls, and tool outputs; reflects on them to diagnose failures and propose prompt updates; and maintains a Pareto frontier of candidate prompts rather than greedily mutating only the current best. Across six tasks, GEPA outperforms GRPO by 6% on average and by up to 20% while using up to 35× fewer rollouts, and also outperforms MIPROv2 in the reported aggregate comparison. In Section REF(sec:loop) vocabulary, GEPA strongly instantiates the proposal side, $Q_t$, through trajectory-conditioned reflection, and uses Pareto-based candidate selection as a proposal/pruning mechanism. What it does not instantiate is the full SkillOpt-style artifact lifecycle: a bounded edit budget on a reusable skill document, a strictly-greater held-out gate on each accepted skill update, a rejected-edit buffer used as negative feedback, and an exported deployment artifact with governance hooks.

**@tiwari2026fastandslow** supply the broader theoretical framing from the optimization side, arguing explicitly that restricting learning to *either* in-context (prompt optimization) *or* in-weights (RL / fine-tuning) is unnecessary and costly. In-context adaptation is cheap and rapid but capacity-bounded; in-weights adaptation is expressive but induces catastrophic forgetting and loss of plasticity [@dohare2024loss]. The scaffold layer of Section REF(sec:why) is precisely the substrate that absorbs what in-context adaptation can carry cheaply, leaving the weights free to generalize. Tiwari et al. supply the two-timescale motivation from the optimization side; Section REF(sec:why) supplies the matching motivation from the production-reliability side. The two framings are independent and mutually reinforcing.

### Reflective Context Learning: a parallel formalization {#app:families-5}

The most direct independent convergence on the Section REF(sec:loop) formalization comes from **Reflective Context Learning** [RCL; @vassilyev2026rcl]. Their opening observation is that "the fundamental problems of learning, including credit assignment, overfitting, forgetting, local optima, and high-variance learning signals, persist whether the learned object lies in parameter space or context space," and that current methods are "fragmented and ad hoc" precisely because they address these challenges one at a time rather than as a unified optimization problem over the context. The parallel to Section REF(sec:loop)'s argument — that scaffold maintenance needs the discipline of weight-space optimization applied to an external artifact layer — is exact and arrived at independently.

RCL maps onto Section REF(sec:loop) as follows. The *learned context* is $\theta_s$. The *reflection signal* is a form of credit assignment identifying which context coordinate caused a failure (Appendix REF(app:mechanism-1), operation 2). The *generalization penalty* that RCL introduces to prevent narrow sample-specific rules is structurally the complexity penalty $\Omega(z)$ of the gate condition. Where RCL and Section REF(sec:loop) differ is in Loop-2 scope: RCL is framed around single-agent cross-task generalization, while Section REF(sec:loop)'s Loop 2 is cross-deployment, cross-tenant, and cross-organizational promotion. The convergence is nonetheless significant: two research threads starting from different motivations (production reliability in Section REF(sec:loop), cognitive agent learning in RCL) arrive at the same formal observation that the classical learning problems do not disappear when the learned object moves outside the weights.

### The harness-optimization cluster {#app:families-6}

A second convergent family focuses on the *harness* — the code and configuration layer that wraps a frozen model — rather than on skill documents specifically. This family independently identifies credit assignment as the central unsolved problem of scaffold evolution, and its engineering solutions directly instantiate Appendix REF(app:mechanism-1)'s operation 2 (mode discovery and credit assignment) and operation 4 (delta validation).

**Meta-Harness** [@lee2026metaharness] is the cleanest representative. Its opening claim — that "the performance of large language model systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model" — is Section REF(sec:intro)'s scaffold-versus-weights decomposition restated for the harness substrate specifically. Meta-Harness then identifies that existing text optimizers "compress feedback too aggressively," losing the fine-grained signal needed for credit assignment. Its solution is an outer-loop proposer with access to source code, scores, and execution traces of all prior candidates through a filesystem, so that the edit history itself becomes the credit-assignment signal. In Section REF(sec:loop) terms, the filesystem of prior candidates is a concrete form of the accumulated history $H_t$ that conditions the proposal distribution $Q_t$, and the outer loop is a Loop-1 closure over the harness substrate (Section REF(sec:method), S5) rather than the skill substrate (S2).

**Agentic Harness Engineering** [AHE; @lin2026ahe] attacks the same problem from the observability side. The core diagnosis is that harness engineering "faces a heterogeneous action space across editable components, voluminous trajectories that bury actionable signal, and edits whose effect is hard to attribute." These three failure modes map precisely onto Section REF(sec:loop)'s mechanism stack: a heterogeneous action space is the coordinate-identification problem (Appendix REF(app:mechanism-1) op 2); voluminous trajectories that bury signal is the residual-capture problem (op 1); and effects that are hard to attribute is the credit-assignment half of op 2 (Appendix REF(app:formal)). AHE's response — three matched observability pillars giving every editable harness component a file-level representation — is an engineering instantiation of the coordinate decomposition that Section REF(sec:loop) assumes. The implicit claim is that artifact-layer descent requires not just the optimization loop but also the instrumentation that makes scaffold coordinates individually observable and attributable.

**MOSS** [@cai2026moss] extends the harness argument by observing that all prior self-evolving agent systems "confine evolution to text-mutable artifacts — skill files, prompt configurations, memory schemas, workflow graphs — and leave the agent harness untouched." Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is, in MOSS's phrase, "physically unreachable from the text layer." MOSS therefore extends Loop-1 evolution to source-level code rewriting. In Section REF(sec:method) terms, MOSS evolves S2 (Skills) and S5 (Orchestration) simultaneously, rather than treating the orchestration substrate as a fixed wrapper around an evolvable skill layer. This matters for Section REF(sec:gap): a governed cross-tenant scaffold optimizer that covers only text-mutable artifacts leaves the code substrate ungoverned, and MOSS's diagnosis suggests the gap is not merely inconvenient but structurally incomplete.

**CANTANTE** [@zehle2026cantante] attacks credit assignment directly in the multi-agent setting. Its observation is that "scores are available only at the system level, whereas the parameters governing agent behavior are local," making optimization of multi-agent scaffolds "fundamentally a credit-assignment problem." CANTANTE's solution is contrastive: it decomposes system-level rewards into per-agent update signals by contrasting rollouts of multiple jointly acting configurations. In Section REF(sec:loop) vocabulary, CANTANTE provides a concrete mechanism for the credit-assignment step (Appendix REF(app:mechanism-1) op 2; Appendix REF(app:formal)) in the case where the scaffold is distributed across agents rather than concentrated in a single artifact. The gap it closes is the same one Section REF(sec:loop) identifies in Appendix REF(app:formal) — that attribution (output error assigned to an upstream scaffold coordinate) must succeed with non-zero probability per failure — but instantiated for the multi-agent topology substrate (S5).

**Harness optimizer evaluation** [@ong2026harnesseval] provides independent empirical evidence for a failure mode this paper flags in Section REF(sec:failure): that evaluating scaffold optimizers "solely by observing target agents' performance gains" misses intermediate erroneous edits that hinder performance. Their finding — that it is "unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error" — is a direct empirical instantiation of the distinction between Stage 2 (random artifact search) and Stage 3 (artifact-layer descent) from Section REF(sec:why)'s table. The credit-assignment problem is not merely theoretical: production harness optimizers that cannot distinguish informed updates from lucky trial-and-error are operating in Stage 2 even when they report benchmark improvements.

**HARNESSEVO** [@nguyen2026harnessevo] turns the same diagnosis into a measurement. It splits the harness into four separately evolvable slots (role, task strategy, tool and format rules, reflection and control) and attributes value by leave-one-in and leave-one-out evolution. On ALFWorld with a 7B target model nearly all of the gain lives in the reflection/control slot (leave-one-in +0.119; the other slots individually null), and dividing a fixed 64-rollout budget evenly across the four slots leaves each below the optimizer's effective search floor, so every slot freezes at its seed; concentrating the budget on the high-value slot recovers the gain (0.642 to 0.761). On WebShop the effect is absent. In Section REF(sec:loop) vocabulary this is direct evidence that credit assignment over scaffold coordinates must precede budget allocation, and that the coordinate decomposition of Section REF(sec:method) is not merely descriptive: which coordinate carries value is task-dependent and must be measured, not assumed.

### Multi-objective and lifecycle constraints {#app:families-7}

Two papers expose constraints on the Section REF(sec:loop) picture that single-loss descent does not capture, both relevant to the Section REF(sec:gap) missing-architecture discussion.

**MOCHA** [@tanjim2026mocha] observes that agent skills are "multi-field artifacts subject to hard platform constraints: description fields are truncated for routing, instruction bodies are compacted via progressive disclosure, and co-resident skills compete for limited context windows." Skill optimization is therefore not a single-loss descent problem but an inherently multi-objective one: a skill must simultaneously maximize task performance and satisfy platform limits, and optimizing for task performance alone produces skills that pass benchmarks but violate deployment constraints. MOCHA introduces *Chebyshev annealing* to navigate the constraint frontier. In Section REF(sec:loop) terms, the complexity penalty $\Omega(z)$ in the gate condition is precisely the mechanism MOCHA is operationalizing, but Section REF(sec:loop)'s scalar $\Omega$ is a simplification: in production, the constraint surface is a Pareto frontier, not a single penalty term. MOCHA's empirical contribution is to show that ignoring this frontier — treating skill optimization as unconstrained single-loss descent — produces skills that degrade on real deployment infrastructure even when benchmark scores improve.

**Ratchet** [@zhang2026ratchet] makes an argument that is, in some respects, orthogonal to the gradient-analog framing and for that reason worth engaging directly. Ratchet's opening finding — that LLM-authored skills deliver $+0.0$ pp over no-skill baselines while human-curated ones deliver $+16.2$ pp — suggests that the bottleneck in self-evolving skill libraries is not the optimization algorithm (the mechanism for proposing and accepting edits) but *lifecycle management*: whether skills are written, retrieved, curated, and retired correctly. Ratchet introduces four hygiene mechanisms — outcome-driven retirement, a bounded active-cap, meta-skill authoring, and pattern canonicalization — and shows that these lift the $+0.0$ pp floor substantially before any gradient-analog optimizer is applied.

This finding is not a refutation of the Section REF(sec:loop) picture but a clarification of the precondition for it. Artifact-layer descent, as formalized in Section REF(sec:loop), presupposes that the scaffold is maintained well enough for the gate $G_t$ to have a meaningful signal: if skill retrieval is so noisy that the wrong skill is injected into every rollout, the proposal process $Q_t$ receives corrupted evidence and the descent guarantee degrades to random search. Ratchet's hygiene mechanisms are, in Section REF(sec:loop) vocabulary, prerequisites for operation 1 (residual capture) and operation 2 (mode discovery) to function: outcome-driven retirement prevents stale artifacts from polluting the residual signal; the bounded active-cap prevents scaffold bloat from making retrieval unreliable (the Section REF(sec:failure) failure mode); pattern canonicalization collapses duplicate and near-duplicate skills so the proposal process conditions on a clean, deduplicated artifact set rather than competing variants of the same pattern. The practical implication is that the deployment path to Stage-3 artifact-layer descent runs through Stage-1 hygiene as a *prerequisite*, not as an alternative. A system with strong hygiene and no optimizer sits at Stage 1 with a clean scaffold; a system with a strong optimizer and poor hygiene sits at Stage 2 with a noisy loss signal. Stage 3 requires both.

**SkillsVote** [@liu2026skillsvote] carries the lifecycle argument to the scale of an open ecosystem. It profiles a million-scale open-source skill corpus for environment requirements, quality, and verifiability, synthesizes tasks for the verifiable subset, exposes skills through agentic library search before execution, and after execution decomposes each trajectory into skill-linked subtasks whose outcomes are attributed to skill guidance, agent exploration, environment, or result signals; only successful, reusable discoveries pass into evidence-gated updates. Two Section REF(sec:loop) points follow. First, attribution is performed at the admission gate rather than inside the optimizer, which is credit assignment (Appendix REF(app:mechanism-1) op 2) used as a filter on residual capture (op 1). Second, the redundancy and environment-sensitivity SkillsVote measures in open skill ecosystems are the same bloat and drift that Section REF(sec:failure) names, arising this time from many authors rather than one loop.

### Cross-task transfer and evidence radius {#app:families-8}

Several papers independently measure what Section REF(sec:loop) calls the *evidence radius* of a scaffold artifact — how far an edit validated in one context continues to improve performance when redeployed elsewhere — without using that vocabulary.

**Training Language Agents to Learn from Experience** [ICT; @shalev2026ict] introduces the In-context Training framework specifically to evaluate *cross-task self-improvement*: whether experience distilled from one set of tasks transfers to unseen tasks. Their finding that "current reflection-based methods can only self-correct within a single task instance" is a measurement of evidence radius at its lower bound — a radius of exactly one task — and their ICT framework is a systematic attempt to expand that radius through supervised distillation of reflections into reusable lessons. In Section REF(sec:loop) terms, ICT is an attempt to instrument Loop 2 empirically: to measure whether a locally-validated edit (one that passed the gate on one task's $L_D$) continues to improve performance when the promotion radius is expanded to cover a distribution of unseen tasks.

**Combee** [@li2026combee] approaches the same measurement from the scaling direction. ACE [@ace2025agentic] established that context-as-living-artifact (a system prompt that accumulates, refines, and organizes strategies through agentic interaction) could improve over static prompts on single-agent tasks. Combee extends this to high-parallelism settings, arguing that "existing methods primarily focus on single-agent or low-parallelism settings," which "fundamentally limits their ability to efficiently learn from a large set of collected agentic traces." The parallel scaling Combee addresses is a form of Loop-2 scope expansion: when many agents run simultaneously, the trace pool available for the next proposal step is drawn from a wider deployment distribution, and the promoted artifact is being tested against a larger averaging set of patch losses. This is not cross-organizational Loop-2 promotion, but it is a step toward it, and Combee's empirical results measure how much of the evidence-radius benefit can be captured by intra-organization parallelism before the cross-organizational barrier is reached.

**CORAL** [@qu2026coral] addresses the Loop-2 problem from the multi-agent open-ended discovery angle. CORAL replaces rigid control with long-running agents that explore, reflect, and collaborate through shared persistent memory, asynchronous multi-agent execution, and heartbeat-based interventions. The shared persistent memory is the cross-agent promoted artifact: a finding validated in one agent's exploration that is written to the shared store becomes available to all agents, and the heartbeat mechanism provides a form of auto-gated Loop-2 promotion. CORAL does not implement the versioned lineage, RBAC, or rollback that Section REF(sec:gap) requires, but it provides the only fully asynchronous multi-agent Loop-2 promotion mechanism in the current survey corpus, and its open-ended discovery framing makes the evidence-radius question concrete.

**PACE** [@ling2026pace] closes this family with a production-oriented two-timescale design for small language model agents. The fast timescale adapts prompts, parsers, validators, and control logic from failure signals within a deployment; the slow timescale consolidates across episodes. The two-timescale structure maps cleanly onto the Loop-1 / Loop-2 distinction of Section REF(sec:loop): Loop 1 fires at the fast timescale, updating a single deployment's scaffold; Loop 2 fires at the slow timescale, consolidating across the deployment's own episodes rather than across deployments. PACE's contribution is to show that the two-loop architecture is implementable under the resource constraints of small, frozen production models — not only under frontier-model assumptions — and that the slow/fast consolidation structure persists even when the optimizer model and the target model are the same frozen small model.

**SkillClaw** [@ma2026skillclaw] and **FederatedSkill** [@yang2026federatedskill] are the two systems in the corpus whose Loop 2 crosses users rather than tasks or agents. SkillClaw treats cross-user, over-time interaction as the primary improvement signal: trajectories from many users are aggregated, an autonomous evolver identifies recurring behavioral patterns and translates them into skill-set updates, and the updated skills live in a shared repository synchronized across users; its evaluation protocol runs a day-night cycle in which simulated concurrent users generate trajectories by day and the system reflects, proposes bundles, validates, and deploys by night. FederatedSkill starts from the observation that isolated single-user task streams lack the diversity to build comprehensive skills, while raw trajectory sharing compromises privacy and a uniform global library ignores client heterogeneity. Its unit of communication is the semantic skill diff (a structured patch over a local library, shipped with the task reward that produced it); a server-side evolution agent aggregates patches into a per-client capability matrix (covered, absorbing, broken, gap) and emits a personalized update for each client, applying, adapting, or rejecting peer patches with an auditable decision log that records source patch, reward, and justification for every modified path. Across 20 task families it reports up to +44.4% success and −37.5% compute against isolated self-evolution. In Section REF(sec:loop) terms FederatedSkill is the first surveyed system in which Loop 2 is a federated aggregation of artifact updates rather than a promotion of a single artifact, and its decision log is the first lineage record at the aggregator. It remains inside one operator's federation (clients are backbone-plus-harness profiles, not organizations), its acceptance decision uses the source client's reward rather than a held-out evaluation at the receiving client, and it reports neither RBAC nor rollback; Section REF(sec:gap)'s properties (b), (c), and (d) are each partially or wholly open.

### Synthesis: what the convergence establishes {#app:families-9}

The four claims stated in Section REF(sec:families) are supported as follows:

1. **The scaffold-versus-weights decomposition is independently confirmed.** GEPA, Meta-Harness, MOSS, RCL, and PACE all begin from the observation that model weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope properties. No surveyed paper disputes this decomposition; the variation is in which substrate each paper targets (skill document, harness code, system prompt, shared memory).

2. **Credit assignment is the central engineering bottleneck.** AHE, CANTANTE, Meta-Harness, @ong2026harnesseval, HARNESSEVO, and SkillsVote all identify credit assignment — attributing a system-level failure to a specific scaffold coordinate — as the problem that distinguishes disciplined Loop-1 evolution from trial-and-error. This is the credit-assignment step of Appendix REF(app:mechanism-1) (operation 2; Appendix REF(app:formal)), and it remains unsolved in the general multi-substrate case.

3. **Lifecycle hygiene is a precondition for descent, not an alternative to it.** Ratchet establishes that the gradient-analog mechanism of Section REF(sec:loop) requires a maintained scaffold as a precondition. A dirty artifact pool (stale, bloated, miscurated) prevents the gate $G_t$ from receiving a meaningful signal. Hygiene and optimization are sequential dependencies, not competing paradigms.

4. **No surveyed system combines Loop-1 automation with cross-organizational Loop-2 governance.** SkillOpt has the strongest Loop-1 closure and the most systematic evidence-radius measurement, but it does not implement cross-organizational promotion, versioned lineage with RBAC, or rollback. CORAL implements asynchronous cross-agent promotion within one system but not across organizations. PACE implements two-timescale consolidation within one deployment. Meta-Harness implements Loop-1 closure over the harness substrate but no Loop-2 promotion mechanism. FederatedSkill federates skill patches across clients under one operator, with a decision log but no RBAC or rollback. The four-property gap named in Section REF(sec:gap) is narrowed on property (b) by FederatedSkill and closed on none; it is, if anything, confirmed more strongly by the independent convergence of multiple research threads on the same single-organization ceiling.

### SkillOpt against Section 9's four properties {#app:families-10}

Mapped onto Section REF(sec:gap)'s four properties of governed cross-tenant scaffold optimization:

- (a) **Auto-gated Loop 1.** *Satisfied.* The held-out selection-split gate at strictly-greater margin instantiates $G_t$.
- (b) **Multi-tenant cross-org promotion.** *Absent.* SkillOpt is a single-organization research system; there is no governed cross-tenant aggregator.
- (c) **Versioned lineage with RBAC.** *Partial.* The exported `best_skill.md` is a versioned artifact, and the protected slow-update field separates fast and slow consolidation. There is no documented RBAC layer or audit-trail policy, and `edit_apply_report.json` is an operational log rather than an access-controlled lineage system.
- (d) **Rollback.** *Absent.* The training loop selects the best validation-gated skill and exports it; no rollback envelope on deployed artifacts is reported.

The cross-model, cross-harness, and cross-benchmark transfer experiments reported by SkillOpt are *empirical evidence-radius measurements*: they tell us that a skill optimized in one (model, benchmark, harness) cell continues to improve performance when redeployed in nearby cells without further optimization. In Section REF(sec:loop) vocabulary, this is a measured Loop-2 *radius* for the artifact, not a *governance mechanism* for promoting the artifact. Both readings are useful: SkillOpt is the strongest current Loop-1 proof and supplies the first systematic transfer evidence at the scaffold layer, while the Section REF(sec:gap) cross-tenant governance triad ((b), (c), (d)) remains unfilled.

### Cost and bloat {#app:families-11}

SkillOpt reports 0.6M to 46.4M training tokens per absolute test-point gain (their Table 6), with the procedural benchmarks (SpreadsheetBench, OfficeQA, LiveMath) at the cheap end and search/visual benchmarks (SearchQA, DocVQA) an order of magnitude more expensive per point. The deployed artifact remains 379–1,995 tokens regardless. This is, to our knowledge, the first published cost-per-point figure for scaffold-layer descent, and it complements the Section REF(sec:failure) scaffold-bloat discussion (and the Ratchet hygiene-precondition finding walked in Appendix REF(app:families-7)): the textual learning rate $\eta_t$ with cosine decay keeps the deployed skill compact even when the optimizer explores many more edits than are accepted (only 1–4 edits survive into the final skill across the six benchmarks). The mechanism that prevents the deployed artifact from bloating is exactly the complexity penalty $\Omega(z)$ of Section REF(sec:loop), instantiated as a hard cap on accepted edits per step rather than a soft regularizer.

---

## Claims audit and the rubric-reward comparison {#app:audit}


Every absolute claim of the May-2026 draft of this survey (the version whose corpus closed in May 2026) of the form *no surveyed system / only X / first / absent / empty cell*, with its verdict after the October-2026 literature sweep (three parallel sweeps: skills; harness, context, and LLMOps governance; memory governance, competing surveys, rubric rewards; 126 systems added, scored from their own method sections) and the recount script released with the score table. Verdicts: **holds** (unchanged), **sharpened** (true, now stated more precisely), **revised** (wording must change), **dropped** (not carried into this version). Evidence names the system(s) that forced the verdict; arXiv ids are in the reference list.

**Corpus after the sweep:** 256 unique systems (130 May + 126 October), 204 core, 52 contrast. No October addition scores 5 on any substrate. Composite two-loop audit: 14 research systems + 3 industry exemplars (Sierra Agent OS 2.0, Cognition Devin, and now Letta Context Repositories, whose shared-memory push carries git lineage but no gate) pass; 7 October systems promote across contexts without versioning or lineage and enter only under relaxation (a) or not at all (EvolveNet, Evo2Team, XRepoSkill, ShareMem, RASO, Spotify, Future AGI (T5 only)).

**Corrections to the May data applied here (applied before the recount):** (1) the row "Governed Collaborative Memory / SSGM" conflated Cuadros et al. (2605.04264) with SSGM (Lam et al., 2603.11768); split, SSGM scored 2 (conceptual framework). (2) MAE and Memento-Skills were scored 5 on S5 in the CSV while the published table said no orchestration system reaches 5; both close one loop only, so they are re-scored 4 per the uniform rubric. S5 mean for the May corpus moves from 2.68 to 2.58.

### The Section 9 corner (a)–(d) {#app:audit-1}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| No public system combines (a) auto-gated Loop 1, (b) cross-organization promotion, (c) versioned lineage with RBAC, (d) rollback | **holds** | Three sweeps, 126 systems: (b) is unclaimed by any evidenced system (EvolveNet's clients are benchmark partitions, "organizations" only in motivation; MemClaw is single-tenant in its evaluation; Buildrix is an open community hub with no gate); (c) appears as lineage without RBAC everywhere (EDDOps, ACM, MemClaw, Letta, Mem0 history) and as RBAC without versioned promotion in MCP control planes (agentic-community gateway, TrueFoundry); (d) is demonstrated by Governed Capability Evolution and EDDOps and claimed by EvolveNet (round rollback) and EvoUndo (recoverability as admission), none of which has (a)+(b). |
| "No surveyed system meets the FedAvg limit; FederatedSkill comes closest" | **sharpened** | EvolveNet (2608.04968) is now the nearest: broadcast, client-local optimization, server-side merge accepted iff fixed ≥ broken on a held-out slice, rollback to the previous shared harness. Still selection-and-merge over program edits, not averaging; cite both. |
| "(iv) … FederatedSkill comes closest … narrowed on one property, closed on none" | **revised** | Two closest approaches now: FederatedSkill (decision log, no gate at receiver) and EvolveNet (held-out merge gate and round rollback, no lineage or RBAC). Say "narrowed on (b) and (d) by different systems, closed on none." |
| "no member of the Section REF(sec:families) research families provides (d), and only FederatedSkill provides even a partial (b)" | **revised** | (d): EvolveNet (round rollback), SkillSmith and SkillAudit (edit-level rollback inside one agent), Growing Harness and WDA (within-optimization rollback), EvoUndo (recoverability as an admission test). (b): EvolveNet and RASO partial. New sentence: "rollback now appears inside single deployments and inside one federated round; no system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion." |

### Matrix cells {#app:audit-2}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| "Three cells are populated; the rest are empty for structural reasons" | **revised** | Among composite-passing systems the three cells hold; but single-loop and governance-only systems now occupy [Human × Human] (MCP registries: Azure API Center, agentic-community MCP Gateway & Registry, TrueFoundry; Buildrix; Enoch), [Human × None] (VerificAgent, revocation guard, Davis et al. governance conversion, Continual Harness human phase), [Auto+Human × None] (SkillChain, Learning on the Job), [None × Auto] (Governed Capability Evolution), [None × Auto+Human] (EDDOps), [None × Human] (ACM). Restate as: three cells hold every system that passes the composite audit; the human-authored cells are occupied only by registries and curation workflows with no session-signal loop. |
| "[Human × Auto] is empty by engineering logic … no published example exists" | **holds** | No system with human-authored candidates and automated promotion was found; the closest, MCP Gateway & Registry, adds an automated security scan to a human admission, which is [Human(+scan) × Human]. |
| "[Human × Human] is empty in the surveyed corpus" | **revised** | Occupied by MCP registries and a community hub; see above. The paper's predicted occupant (solo or small-team workflows) is also now documented empirically by "Who Maintains Agent Skills?" (2609.05677): across five public skill repositories every substantive edit is human-merged, 62% AI co-authored, 1 deprecation in 254 edits. |
| "[Human × None] is structurally improbable" | **revised** | Occupied: VerificAgent (agent-drafted memories, human fact-check, frozen bank), the revocation guard of Shen et al., and human-in-the-loop harness phases. Restate: it is the human-curation cell, single-loop by construction. |
| "Nearly every auto-gated system fires at n = 1" | **revised** | Batched or statistical acceptance is now common: SAGE-gate (paired per-item test), Future AGI (paired bootstrap CI), AutoSaddler (mini-batch failure signals), MGM, ModularRSI (evidence across tasks), VaG (3-of-3 critics), EvolveNet (fixed ≥ broken on held-out), VACE, HackProbe, PROCTOR. Say "common since mid-2026" and cite SAGE-gate and VaG. |
| "no surveyed system has formalized agreement as a k-of-n acceptance rule" | **revised** | VaG requires all three heterogeneous critics to pass (3-of-3); SkillSpec is consensus-gated. Keep the p^k-vs-1/k distinction, drop "no surveyed system". |
| "Only AlphaEvolve demonstrates explicit multi-layer depth" | **sharpened** | Still the only system with cascade evaluator plus diversity archive; HarnessBank, JIT-Agent, MGM keep archives (lineage), VaG adds tiered subset selection. Say "AlphaEvolve remains the only system combining a cascade evaluator with a diversity archive." |

### "Only" and "first" {#app:audit-3}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| CORAL "the only asynchronous multi-agent Loop-2 mechanism in the corpus" | **revised** | Evo2Team (2609.34135) promotes routing and communication skills across 4–32-agent teams with target-side confirmation; ShareMem pools memory across users. Say "CORAL was the only one in the May corpus; Evo2Team and ShareMem add cross-team and cross-user promotion without versioning." |
| AlphaEvolve Strassen claim | **holds** (attributed) | Third-party; attribute to the AlphaEvolve report in the same sentence. |
| "CASCADE reports the largest within-benchmark ablation gain in the corpus" | **dropped** | Not re-checked across 127 new systems; comparing ablation gains across benchmarks is not meaningful. Removed from this version. |
| ChronoMem and rollback repair "the first surveyed instances of the rollback envelope" | **revised** | Rollback of memory is now in VerMem (soft-delete/restore ops), Mi-Memory (design), Letta (git history); and shown unsafe in checkpoint-rollback studies (2608.29381, 2608.15939). Say "among the first" and cite the counter-evidence. |
| Cuadros "only surveyed memory system with full provenance + versioning + correction" | **holds** | Memory governance additions (TOKI, PPMF, TMA-NM, MemClaw, He & Yu) each carry provenance or lineage without correction loops or versioning, and the auto-gated memory loops (Recuris, MemGuard, VerMem, Compiled Memory) carry no lineage. |
| SkillOpt "cleanest published instance" / "first to instantiate all four simultaneously" | **sharpened** | SkillOpt-Lite (2607.03451) removes two of the four and matches it; VALVE, SkillSmith, SkillAudit instantiate held-out gates with rollback. Say "the first system we found that instantiates all four, and its own follow-up shows two of them are stabilizers rather than necessities." |
| FederatedSkill "first … federated aggregation … first lineage record at the aggregator" | **holds** | EvolveNet (Aug 2026) postdates it and has no lineage record. |
| SkillOpt "first published cost-per-point figure" | **holds** | No earlier figure found. |

### Absences {#app:audit-4}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| "production deployments sit at Stage 1 or 2; none reaches Stage 3" | **sharpened** | Spotify (2609.30297) runs automated prompt and planning optimization gated by human launch and A/B metrics; SkillChain (Alibaba) runs judge-monotone edits behind a human reflection gate with reported agreement. Both are Stage 3 on Loop 1 with a human Loop 2; say "production deployments reach Stage 3 on the local loop only behind a human promotion gate". |
| S1 score-5 none; "no instruction system closes both loops" | **holds** | S1 n=15, max 4; adoption studies cut the other way (Gloaguen: context files raise cost >20% without raising success; Galster: context files dominate configuration, skills rare). |
| "Anthropic's skills repository is one-pool with PR review but no automated eval gate" | **holds** | Confirmed by 2609.05677 (human-merged, no eval gate observed). |
| "correctable, versioned memory is rare; production memory lacks failure-triggered correction and versioned lineage" | **revised** | Letta Context Repositories (git-backed memory, every edit committed, shared memory auto-pushed), Mem0 per-memory history and feedback endpoint, Zep bitemporal invalidation: lineage is now common in production memory; failure-triggered correction is not, and 2609.08258 shows revoked facts still outrank their replacements in five backends. Say "versioned lineage has arrived in production memory; enforced correction has not." |
| S5 score-5 none; "topology evolution is rare" | **sharpened** | After the correction S5 has no 5 in either corpus. Gated topology evolution now exists: TOCOMAS retains only candidates satisfying structural invariants; Evo2Team promotes across teams; OptiMAS, AgentGrad, HarnessForge update S5 under evaluation. Say "rare and, where it exists, gated by evaluation alone except TOCOMAS." |
| "no system matures all six at once" | **holds** | No October addition scores 5 on any substrate. |
| "Failure-triggered memory is rare in production" | **holds** | One field report (SIx Harness, N=1, self-reported); Letta dreaming writes from conversation history, not failures. |
| "Cross-customer skill promotion is nearly absent" | **holds** | ShareMem, EvolveNet, XRepoSkill, RASO promote across users, clients, or repositories inside one operator; none across customers or organizations with evidence. |
| "Memory versioning is mostly unsolved outside Cuadros et al. and ChronoMem" | **revised** | See 190: Letta, Mem0 history, Zep bitemporal facts, TOKI audit rows, MemClaw supersession chains. |
| "Scaffold-level curriculum is unspecified in nearly every surveyed system" | **sharpened** | Task-CoEvolve (variance-weighted task sampling) and AutoSaddler (mini-batch failure signals) specify it; still the exception. |
| "Held-out evals at Loop-2 promotion are absent" | **revised** | Receiving-side evaluation now exists: ShareMem (evaluation tasks belong to a different user), XRepoSkill (independent verification in ≥2 repositories), Evo2Team (target-side confirmation; 4 of 22 transfers still fail on new graphs), VACE (candidate evaluated with the receiving model fixed). EvolveNet explicitly has none; Federated Agent Optimization (2610.01195) proposes a receiving-client gate without implementing it. |
| research full-auto: "enterprise governance is uniformly absent" | **holds** | No October [Auto × Auto] system reports RBAC or audited promotion. |
| governance-first: "no patch-local inner loop" | **holds** | EDDOps, ACM, GCE, MCP control planes all have Loop 1 = None. |
| "AGENTS.md in over 60,000 repositories" | **revised** | Newer counts: 2,853-repository study (Galster), 128,018-project adoption study (Robbes: 22–29% of coding-agent projects), 36,710 repositories mined for loop engineering (Lulla 2608.21884). Replace the single count with these studies and the cost finding (Gloaguen). |
| "no surveyed system treats pruning or expiration as a first-class gated operation (outside Ratchet, SkillOpt, ChronoMem)" | **revised** | Retirement is a gated operation in at least eleven skill systems (Library Drift: retire when n ≥ 100 and contribution ≤ −0.10 with a cap of 50; SkillSmith; SkillOps; ASSAY; HiSME; SkeMex; MUSE-Autoskill; SkillMAS; SafeEvolve; Double Ratchet; SkillGen) and expiry is a product control in Mem0, Zep, and LangGraph Platform. Say "pruning and expiry became first-class in 2026; what remains rare is pruning of a promoted artifact's descendants, which VaG shows is structurally irreversible." |
| failure surface "largely unmitigated in production" | **holds** | Revocation unenforced in five production backends (2609.08258); checkpoint rollback unsafe in three frameworks (2608.29381); no evidentiary record in 16 deployed frameworks (Hearsay 2609.32495). |
| multi-sample agreement "under-explored; SkillOpt-Lite nearest" | **revised** | See 231: SAGE-gate, VaG, SkillSpec. |
| "No surveyed paper disputes the scaffold-vs-weights decomposition" | **holds** | SIA (2605.27276) updates harness and weights together but keeps them distinct levers. |
| credit assignment "remains unsolved in the general multi-substrate case" | **holds** | HARNESSEVO (slot attribution), AgentGrad (intervention-based), CANTANTE (contrastive) each solve one substrate's case. |

### Section 4 claims (checked against the rescored corpus) {#app:audit-5}

| Claim | Statement | Verdict | Evidence |
|-----|-----------------------|----------|------------------------------------------|
| IV-1 | Every [Auto × Auto] system with a per-edit estimator gate runs on a C1 signal or a simulated C2 environment; [Auto × Auto] systems in C4 domains gate by proposal pruning | **holds** | May [Auto × Auto]: DGM, Voyager, AlphaEvolve, SkillOpt, SkillRL, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual (C1/simulated C2); NanoResearch (semantic merge, C4) and CORAL (heartbeat, C4) prune. October: EvolveNet, Evo2Team, XRepoSkill (C1 code/benchmark signals); ShareMem (C2 Mind2Web); RASO (target execution feedback, C1/C2); Letta (no gate). |
| IV-2 | [Auto × Human] is populated only by C2/C3 systems | **holds** | SkillForge (C3 judge, human Loop 2), CASCADE (C3), Sierra (C2/C3), Devin (C2 merge outcome), Spotify (C2 A/B behind human launch). No C1 system occupies the cell. |
| IV-3 | Rubric-as-reward builds C3 gates on the weight side; scaffold-side judge calibration under the reflexive condition is rare | **sharpened** | 14 reward papers: 8 fix the rubric or judge during policy optimization, 5 co-evolve it (RLPR by construction, EvoRubrics, SCORE, RubricEM, Rubric-ARM at the reward-model stage); only 5 report any human-agreement number and none of the co-evolving ones does. Scaffold side: SkillForge (>90% agreement), SkillChain (κ 0.72–0.91), SkillCoach (trajectory-filter consistency 82→96% against human gold) now report calibration; none calibrates a judge that is itself being edited. |

### Recount output (merged corpus, all rows) {#app:audit-6}

```{=latex}
\begingroup\footnotesize
```

```
rows: 269  unique systems: 256  core: 204  contrast: 52
substrate            n   mean  score-5 systems
INTEGRATED           52   3.81  AutoAgent, NanoResearch, SkillRL
S1_Instructions      15   3.07  (none)
S2_Skills            50   3.34  COSPLAY, SAGE
S3_Memory            50   3.06  Governed Collaborative Memory (Cuadros et al.)
S4_Tools             20   3.65  Harvey, Hippocratic AI, MCP
S5_Orchestration     37   3.08  (none)
S6_Governance        45   3.02  AGENTS.md / AAIF, Braintrust, LangSmith Hub, Vellum
May corpus alone (after corrections): 130 / 99 / 31; S5 mean 2.58.
```

```{=latex}
\endgroup
```

## Extended related work {#app:related}

The main article makes four design commitments that another survey could make differently: it classifies systems by whether a feedback loop closes over a persisted artifact, rather than by which mechanism is edited; it labels the gate on each of two loops as algorithmic, human, or absent; it classifies the signal that feeds the gate by verifiability; and it audits governance against four named properties. Each commitment meets a separate line of prior work. This section traces what each line established, the setting it assumed, and the condition that changes here, so that a reader can see the differences without the article having to argue for them. Every description below is taken from the cited work's own abstract, method section, or documentation; the evidence record is released with the article.

### Loop closure as the unit of classification {#app:related-1}

The surveys of self-evolving agents organize the field by what is evolved and when. Gao et al. [@gao2026selfevolving] ask what, when, how, and where to evolve, with a timing axis that separates adaptation inside a test-time episode from adaptation between episodes, and they note that a human in the loop can validate a newly created tool. Fang et al. [@fang2025comprehensive] give a unified frame of system inputs, agent system, environment, and optimizers, and cover single-agent, multi-agent, and domain-specific settings. Zhou et al. [@zhou2026selfevolvingcoding] taxonomize 108 self-evolving coding methods by evolution target, timing, and code-specific signal, and they come closest to a gate: their admission rule accepts an update when it improves a metric by a margin and passes a check, and they observe that a passing test "checks only selected behavior". Ren et al. [@ren2026selfimprovementsurvey] describe an agent as a foundation model times an operational scaffold and treat self-improvement as a self-induced update operator organized by target and driving signal. Surveys of agent memory [@du2026memory; @huang2026secondhalf; @luo2026storage], context engineering [@mei2025context; @hua2025context2], and agent skills [@zhou2026agentskills; @ding2026skilleval; @xia2026harnessing] do the same for their substrate: each catalogues mechanisms and, in the skills surveys, lifecycle stages.

What this line established is the inventory. The substrates this article scores are the ones these surveys name, and the mechanisms it finds in the corpus are the ones they catalogue. The setting they assume is a mechanism-centered one: a system is described by what it edits. The condition that changes here is the question asked of each system. Whether a loop closes at all, whether it closes under a gate, and whether a second loop promotes the result are properties that the mechanism inventory does not determine, and they are what the two-loop audit of Section REF(sec:method) measures. Zhou et al.'s admission rule is the nearest precedent for the gate; it is stated for one domain, code, where the check is a test, and this article asks what the rule becomes when the check is a judge or a delayed outcome.

### The gate as algorithmic, human, or absent {#app:related-2}

Three lines bear on gate type. The first is prompt and program optimization, which a reader will expect to see named. APE treats the instruction as a program and selects among LLM-proposed candidates [@zhou2022ape]; ProTeGi forms natural-language "gradients" from minibatches that criticize the current prompt and searches edits with beam search [@pryzant2023protegi]; OPRO has the language model propose new instructions from a prompt that lists previous candidates with their scores and reports gains of up to 8% on GSM8K and up to 50% on Big-Bench Hard over human-designed prompts [@yang2023opro]; EvoPrompt applies evolutionary operators to a prompt population and improves it against a development set, with gains of up to 25% on BBH across 31 datasets [@guo2023evoprompt]; Promptbreeder evolves task prompts and the mutation prompts that modify them, evaluated on arithmetic and commonsense reasoning and on hate-speech classification [@fernando2023promptbreeder]. DSPy compiles pipelines of language-model calls into text-transformation graphs and optimizes each pipeline to a metric by creating and collecting demonstrations [@khattab2023dspy], MIPRO proposes instructions and demonstrations jointly for multi-stage programs under a stochastic mini-batch surrogate [@opsahlong2024miprov2], TextGrad backpropagates textual feedback through the variables of a compound system [@yuksekgonul2024textgrad], and Trace generalizes the pattern to any computation whose execution trace can be shown to an optimizer [@cheng2024trace]. This line established that a development-set score is a usable gate for an algorithmic proposer and that the proposer can be the model itself. The setting it assumes is a single optimization run against a fixed task distribution. The condition that changes here is persistence and scope: these optimizers produce a prompt or program as the optimizer's output, not a versioned deployment artifact edited from session signal and promoted under a second gate, which is why they sit in the contrast corpus or at the single-loop boundary (Appendix REF(app:contrast)). SkillOpt is the point where the lineage crosses into the corpus, by adding a persistent skill document, a held-out acceptance gate, and a rejected-edit buffer to the same proposer (Section REF(sec:families)).

The second line optimizes the scaffold as a whole rather than one prompt, and it is the nearest precedent for the loop of Section REF(sec:loop). Agent symbolic learning treats prompts, tools, and the pipeline that connects them as symbolic parameters and updates them with textual losses and gradients [@zhou2024symbolic]; STOP has a scaffolding program recursively rewrite the code that improves it [@zelikman2023stop]; a self-improving coding agent edits its own harness and raises its benchmark score as a result [@robeyns2025sica]; and workflow search optimizes the orchestration graph itself, by node and edge optimization over agent graphs [@zhuge2024gptswarm] or by tree search over code-represented workflows [@zhang2024aflow]. These established that the whole scaffold is an optimizable object and that textual feedback can drive its updates. Each runs within one deployment under a benchmark score, with no promotion to other deployments and no governance of the artifact it produces; the two-loop audit of Section REF(sec:method) is the measurement of exactly those two absences.

The third line is the classic single-loop agents and their memories: Reflexion's verbal reinforcement into episodic memory [@shinn2023reflexion], the reflection-and-importance memory of generative agents [@park2023generative], Voyager's growing skill library [@wang2023voyager], the experience bank ExpeL extracts from training tasks [@zhao2024expel], MemGPT's virtual context management [@packer2023memgpt], Agent Workflow Memory's induced and reused workflows [@wang2024awm], the Zettelkasten-style organization of A-MEM [@xu2025amem], the persistent test-time memory of Dynamic Cheatsheet [@suzgun2025cheatsheet], the evolving context playbook of agentic context engineering [@ace2025agentic], and the in-context iteration of Self-Refine and ReAct [@madaan2023selfrefine; @yao2023react]. They established that a frozen model can improve across episodes through an artifact it writes, and the cognitive-architecture framing of Sumers et al. [@sumers2023coala] gave that artifact the episodic, semantic, and procedural division this article's memory substrate uses. Reflexion, generative agents, Voyager, ExpeL, MemGPT, Agent Workflow Memory, A-MEM, Dynamic Cheatsheet, and the context playbook persist the artifact and close Loop 1; Self-Refine and ReAct do not persist it. None promotes the artifact beyond the agent that wrote it, which is the absence the second loop of this article is defined to measure.

### Verifiability of the feedback signal {#app:related-3}

No surveyed work classifies systems by the verifiability of the signal that feeds the gate, but three lines come near it. Guo et al. [@guo2026harness] note that software engineering provides mechanical feedback, in the form of builds, unit tests, linters, and execution logs, that most other domains lack; Zhou et al. [@zhou2026selfevolvingcoding] note that even a passing test is incomplete feedback. The judged end of the spectrum has its own measurements: language-model judges agree with human preference at rates that make them usable evaluators of open-ended answers [@zheng2023judge], a proxy reward optimized past a point lowers the true score [@gao2023overoptimization], and people who grade model outputs revise their own criteria as they grade, so that the evaluator drifts along with the evaluated [@shankar2024validators]. The second line is the weight-side effort to extend reinforcement learning from verifiable rewards into domains without verifiers. Rubrics as Rewards generates an instance-specific checklist before training and scores responses with a fixed judge [@gunjal2025rubrics]; Writing-Zero trains a pairwise generative judge on writing principles and holds it fixed during policy training [@jia2025writingzero]; reference-guided evaluation reaches 79.1% agreement with human annotations across the datasets its authors test [@shi2026references]; an essay scorer trained against a fixed rubric reaches a quadratic weighted kappa of 0.803 against a single human rater's 0.805 [@jin2026rlaes]. A second group moves the gate with the policy: RLPR scores by the policy's own probability of a fixed reference [@yu2025rlpr], Rubric-ARM alternates updates of a rubric generator and a judge [@xu2026rubricarm], and EvoRubrics, SCORE, and RubricEM update rubrics adversarially or from a rubric buffer within training [@ding2026evorubrics; @zhu2026score; @li2026rubricem]. Of the fourteen papers in this line that were checked, eight hold the rubric or judge fixed during policy optimization and five co-evolve it; five report agreement with human judgment and none of the co-evolving ones does; one calibrates against language-model golden judges rather than people [@plesner2026cheapverifier]; and a survey of rubric evaluation names the dynamic regime as the trend [@chen2026rubricsurvey].

This line established the gate constructions for judged signals: checklists, references, pairwise judges, and rubric buffers. The setting it assumes is weight-space optimization with the policy as the learner. The condition that changes here is the learner: when the scaffold is what learns, the rubric is itself a scaffold coordinate, so the fixed-versus-co-evolved distinction becomes the question of whether a gate under edit can be calibrated at all. The article borrows the constructions and the distinction; it does not score the methods.

### Governance: lineage, access control, rollback, and promotion across organizations {#app:related-4}

Three lines bear on the four-property audit. The first is governance surveys. Ding et al. [@ding2026alwayson] code 435 works on six dimensions per state item, including provenance and recoverability, and find the literature "concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it". Lin et al. [@lin2026memorysecurity] organize memory security by lifecycle phase and name five primitives, among them principal-scoped retrieval and rollbackability. Neither carries a promotion dimension, and neither scores whether an inner loop fires from session signal.

The second line is the systems that come closest to the four properties. FederatedSkill exchanges semantic skill diffs between clients that are agent instances under one operator, and a server-side evolution agent applies, adapts, or rejects each patch per client while writing an auditable decision log of source patch, reward, and justification; it reports up to 44.4% higher success than isolated self-evolution across 20 task families [@yang2026federatedskill]. EvolveNet broadcasts a shared harness, optimizes it locally at each client, and merges only when the held-out items a merge fixes outnumber those it breaks, rolling back to the previous shared harness after a failed round; its authors describe clients as spanning users and organizations, evaluate on benchmark partitions, and note that a program edit can itself encode client information [@nie2026evolvenet]. The registries supply the remaining properties without an inner loop: EDDOps promotes through automatic evaluation thresholds and human sign-off with supersession lineage and emergency rollback, and states that it does not address role-based access control [@kang2026registry]; Agentic Configuration Management keeps immutable revisions and baselines that enable rollback [@quessadavial2026acm]; Governed Capability Evolution gates activation and rolls back on monitoring, recovering in 72.4% of drift cases in its proof of concept [@qin2026governed]; and the MCP control planes add role-based access and quarantine without an evaluation gate [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. Letta's Context Repositories commit every memory edit to git and push shared memory across agents without a gate [@letta2026memfs].

The third line is federated learning. FedAvg averages client updates in parameter space [@mcmahan2017fedavg], DP-FedAvg adds user-level differential privacy [@mcmahan2018dpfedavg], the field's open problems are catalogued in Kairouz et al. [@kairouz2021federated], and PromptFL moves the federated object from weights to a shared prompt that participants learn cooperatively [@guo2022promptfl]. The setting is numeric updates that are comparable by construction. The condition that changes here is the artifact: scaffold promotion is selection and merge over symbolic objects, and the nearest systems aggregate program edits with a language model rather than by averaging, which is why the article uses the federated analogy only as a limit.

### What is and is not new {#app:related-5}

The ingredients have precedent, and the article says so. The six substrates are the inventory of the self-evolving-agent, memory, context, skill, and harness surveys, and the memory taxonomy is CoALA's. The gate as a development-set score is the prompt-optimization lineage; the scaffold as an optimizable object is agent symbolic learning, STOP, and workflow search; the persisted artifact that closes Loop 1 is Reflexion, Voyager, and the agent-memory line; the admission rule with a margin and a check is Zhou et al.'s; the gate constructions for judged signals are the rubric-reward line; provenance, recoverability, and rollback as governance dimensions are Ding et al. and Lin et al.; federated aggregation of artifact patches is FederatedSkill and EvolveNet. What is new is the combination and the measurement: a corpus of 256 systems scored on one rubric and released; a classification of each by which of two loops it closes and under which gate type; a classification of the signal that feeds the gate into four verifiability classes, with the demonstration that the class fixes the reachable cells of the design space and the dominant failure; and an audit of every system against four governance properties, with the finding that none meets all four and that the two nearest, FederatedSkill and EvolveNet, each narrow different properties without meeting the set. These are the claims of the abstract and the introduction, and the limitations in Section REF(sec:method) (single-rater scoring, two-pass corpus with an October-2026 cutoff, no new experiments) bound them.

## Full score table {#app:scores}

Every scored (substrate, system) row of the corpus: 130 systems scored by May 2026 and 126 added by the October 2026 sweep. Scores follow the 0–5 rubric of the main text (Table REF(tab:V-1)); Loop 1 / Loop 2 gate types and signal classes are recorded for the October rows (and for May rows re-audited in Section REF(sec:design)). Substrate codes: INT integrated, S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance. A year of “—” marks a classical system that predates the survey window. The CSV files with per-row justifications are released as ancillary files with this preprint.

```{=latex}
\begingroup\scriptsize
```

| Sub. | System | Score | Year | Source | Loop 1 | Loop 2 | Class | Added |
|---|------------|---|---|------------|-----|-----|-----|----|
| INT | ADAS / Meta Agent Search | 4 | 2024 | arXiv:2408.08435 |  |  |  | May 26 |
| INT | Agent S / S2 | 4.5 | 2024 | arXiv:2410.08164 |  |  |  | May 26 |
| INT | Agent Workflow Memory (AWM) | 3.5 | 2024 | arXiv:2409.07429 |  |  |  | May 26 |
| INT | AlphaEvolve | 4 | 2025 | arXiv:2506.13131 |  |  |  | May 26 |
| INT | AutoAgent | 5 | 2026 | arXiv:2603.09716 |  |  |  | May 26 |
| INT | AutoManual | 3.5 | 2024 | NeurIPS 2024 |  |  |  | May 26 |
| INT | AutoSaddler | 4 | 2026 | arXiv:2608.23041 | Auto | None | C2 | Oct 26 |
| INT | CaptainAgent | 2.5 | 2024 | arXiv:2405.19425 |  |  |  | May 26 |
| INT | CASCADE | 4.5 | 2025 | arXiv:2512.23880 |  |  |  | May 26 |
| INT | ChatDev | 3 | 2023 | arXiv:2307.07924 |  |  |  | May 26 |
| INT | Co-Harness | 4 | 2026 | arXiv:2607.22688 | Auto | None | C2 | Oct 26 |
| INT | CoEvoSkills | 3.5 | 2026 | arXiv:2604.01687 |  |  |  | May 26 |
| INT | Cognition Devin | 3 | 2024 | cognition.​ai |  |  |  | May 26 |
| INT | Continual Harness | 4 | 2026 | arXiv:2605.09998 | None | None | C4 | Oct 26 |
| INT | Cradle | 4 | 2024 | arXiv:2403.03186 |  |  |  | May 26 |
| INT | Darwin Gödel Machine | 4 | 2025 | arXiv:2505.22954 |  |  |  | May 26 |
| INT | Double Ratchet | 4 | 2026 | arXiv:2607.12790 | Auto | None | C3 anchored by C1 | Oct 26 |
| INT | EvolveNet | 4 | 2026 | arXiv:2608.04968 | Auto | Auto | C1,C2 | Oct 26 |
| INT | EvolveR | 4 | 2025 | arXiv:2510.16079 |  |  |  | May 26 |
| INT | ExpeL | 3.5 | 2023 | arXiv:2308.10144 |  |  |  | May 26 |
| INT | Generative Agents | 4 | 2023 | arXiv:2304.03442 |  |  |  | May 26 |
| INT | GenericAgent | 4 | 2026 | arXiv:2604.17091 | Auto | None | C2 | Oct 26 |
| INT | GITM | 3 | 2023 | arXiv:2305.17144 |  |  |  | May 26 |
| INT | HarnessBank | 4 | 2026 | arXiv:2607.13683 | Auto | None | C2 | Oct 26 |
| INT | HarnessX | 4 | 2026 | arXiv:2606.14249 | Auto | None | C2 | Oct 26 |
| INT | Hippocratic AI Polaris | 3.5 | 2024 | hippocraticai.​com |  |  |  | May 26 |
| INT | JARVIS-1 | 3.5 | 2023 | arXiv:2311.05997 |  |  |  | May 26 |
| INT | JIT-Agent | 4 | 2026 | arXiv:2608.25593 | Auto | None | C2 | Oct 26 |
| INT | Life-Harness | 4 | 2026 | arXiv:2605.22166 | Auto | None | C2 | Oct 26 |
| INT | Mendel Gödel Machine (MGM) | 4 | 2026 | arXiv:2608.07645 | Auto | None | C1 | Oct 26 |
| INT | MetaGPT | 3.5 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| INT | Mobile-Agent-E | 4.5 | 2025 | arXiv:2501.11733 |  |  |  | May 26 |
| INT | ModularRSI | 4 | 2026 | arXiv:2609.14857 | Auto | None | C2 | Oct 26 |
| INT | NanoResearch | 5 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| INT | OpenCore | 4 | 2025 | github.​com/​sibmike/​opencore |  |  |  | May 26 |
| INT | OpenHands / CodeAct | 3 | 2024 | arXiv:2407.16741 |  |  |  | May 26 |
| INT | OS-Copilot / FRIDAY | 4 | 2024 | arXiv:2402.07456 |  |  |  | May 26 |
| INT | Plan4MC | 2.5 | 2023 | GitHub/​arXiv |  |  |  | May 26 |
| INT | SAGE | 4 | 2025 | arXiv:2512.17102 |  |  |  | May 26 |
| INT | Sakana AI Scientist | 3 | 2024 | arXiv:2408.06292 |  |  |  | May 26 |
| INT | ScholarEvolve | 4 | 2026 | arXiv:2609.40169 | Auto | None | C2 | Oct 26 |
| INT | SIA | 4 | 2026 | arXiv:2605.27276 | Auto | None | C2 | Oct 26 |
| INT | Sierra Agent OS | 4 | 2024 | sierra.​ai |  |  |  | May 26 |
| INT | Sierra Agent OS 2.0 | 3 | 2025 | sierra.​ai/​blog/​agent-os-2-0 |  |  |  | May 26 |
| INT | SkillForge | 4 | 2026 | arXiv:2604.08618 |  |  |  | May 26 |
| INT | SkillMAS | 4 | 2026 | arXiv:2605.09341 | Auto | None | C2 | Oct 26 |
| INT | SkillOS | 3 | 2026 | SemanticScholar:​2653e4c7 |  |  |  | May 26 |
| INT | SkillRL | 5 | 2026 | arXiv:2602.08234 |  |  |  | May 26 |
| INT | TTHE | 4 | 2026 | arXiv:2607.08124 | Auto | None | C3 | Oct 26 |
| INT | VACE | 4 | 2026 | arXiv:2609.37105 | Auto | None | C2 | Oct 26 |
| INT | Voyager | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| INT | Workspace Optimization (DreamTeam) | 3 | 2026 | arXiv:2605.09650 | Auto | None | C1 | Oct 26 |
| S1 | AGENTS.md | 2 | 2026 | arXiv:2601.20404 |  |  |  | May 26 |
| S1 | Aider Conventions | 2 | 2024 | aider.​chat |  |  |  | May 26 |
| S1 | Claude Code CLAUDE.md | 4 | 2025 | docs.​anthropic.​com |  |  |  | May 26 |
| S1 | Cody / Sourcegraph | 2 | 2024 | sourcegraph.​com |  |  |  | May 26 |
| S1 | Continue.dev Rules | 3 | 2024 | docs.​continue.​dev |  |  |  | May 26 |
| S1 | Cursor Rules | 3 | 2024 | docs.​cursor.​com/​rules |  |  |  | May 26 |
| S1 | GitHub Copilot Custom Instructions | 3 | 2024 | docs.​github.​com |  |  |  | May 26 |
| S1 | GRACE | 4 | 2026 | arXiv:2607.09175 | Auto | None | C2 | Oct 26 |
| S1 | Lovable Knowledge | 2 | 2024 | docs.​lovable.​dev |  |  |  | May 26 |
| S1 | Meta Context Engineering (MCE) | 4 | 2026 | arXiv:2601.21557 | Auto | None | C2 | Oct 26 |
| S1 | Replit replit.md | 4 | 2025 | docs.​replit.​com |  |  |  | May 26 |
| S1 | Spotify conversational-recommendation loop | 4 | 2026 | arXiv:2609.30297 | Auto | Human | C3 | Oct 26 |
| S1 | VS Code Copilot Instructions | 3 | 2024 | code.​visualstudio.​com |  |  |  | May 26 |
| S1 | Windsurf Cascade Rules | 3 | 2024 | docs.​windsurf.​com |  |  |  | May 26 |
| S1 | Zed AI Rules | 3 | 2024 | zed.​dev/​docs |  |  |  | May 26 |
| S2 | AgentVerse | 1 | 2023 | arXiv:2308.10848 |  |  |  | May 26 |
| S2 | Anthropic Claude Agent Skills | 3 | 2025 | anthropic.​com/​engineering |  |  |  | May 26 |
| S2 | Anthropic/skills GitHub repo | 2 | 2025 | github.​com/​anthropics/​skills |  |  |  | May 26 |
| S2 | ASSAY | 4 | 2026 | arXiv:2606.15390 | Auto | None | C2 | Oct 26 |
| S2 | AutoSkill | 3 | 2026 | arXiv:2603.01145 | Auto | None | C3 | Oct 26 |
| S2 | Buildrix | 3 | 2026 | arXiv:2606.25139 | Human | Human | C3 | Oct 26 |
| S2 | ChatGPT Plugins (legacy) | 1 | 2023 | openai.​com |  |  |  | May 26 |
| S2 | Claude Code Skills | 3 | 2025 | docs.​anthropic.​com |  |  |  | May 26 |
| S2 | COSPLAY | 5 | 2026 | arXiv:2604.20987 |  |  |  | May 26 |
| S2 | CrewAI Skills | 2 | 2025 | docs.​crewai.​com |  |  |  | May 26 |
| S2 | HiSME | 4 | 2026 | arXiv:2605.28390 | Auto | None | C1,C3 | Oct 26 |
| S2 | HuggingFace Agent Skills | 2 | 2025 | huggingface.​co |  |  |  | May 26 |
| S2 | LangChain Skills | 2 | 2025 | langchain.​com |  |  |  | May 26 |
| S2 | Library Drift curator | 4 | 2026 | arXiv:2605.19576 | Auto | None | C1 | Oct 26 |
| S2 | Meta Context Engineering (MCE) | 4 | 2026 | arXiv:2601.21557 | Auto | None | C2 | Oct 26 |
| S2 | MetaGPT (SOP-as-skill) | 3 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| S2 | MetaSkill-Evolve | 4 | 2026 | arXiv:2607.05297 | Auto | None | C2 | Oct 26 |
| S2 | Microsoft Semantic Kernel Plugins | 2 | 2024 | learn.​microsoft.​com |  |  |  | May 26 |
| S2 | MUSE-Autoskill | 4 | 2026 | arXiv:2605.27366 | Auto | None | C1,C2 | Oct 26 |
| S2 | NanoResearch Skill Bank | 4 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S2 | OpenAI Custom GPTs / Actions | 2 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S2 | Personalized developer skills (Huang-Du-Lan) | 3 | 2026 | arXiv:2608.10319 | Auto | None | C3 | Oct 26 |
| S2 | RASO | 4 | 2026 | arXiv:2609.38024 | Auto | Auto | C2 | Oct 26 |
| S2 | SAGE | 5 | 2025 | arXiv:2512.17102 |  |  |  | May 26 |
| S2 | SCAFFOLD | 4 | 2026 | arXiv:2609.05511 | Auto | None | C2 | Oct 26 |
| S2 | SE-GoS | 4 | 2026 | arXiv:2609.08228 | Auto | None | C2 | Oct 26 |
| S2 | SkeMex | 4 | 2026 | arXiv:2606.09365 | Auto | None | C2 | Oct 26 |
| S2 | Skill Issues (Bauplan) | 4 | 2026 | arXiv:2606.01185 | Auto | None | C1,C3 | Oct 26 |
| S2 | SKILL.md smells (Hong-Imani-Ahmed) | 1 | 2026 | arXiv:2607.01456 | None | None | - | Oct 26 |
| S2 | SkillAudit | 4 | 2026 | arXiv:2606.14239 | Auto | None | C3,C1-partial | Oct 26 |
| S2 | SkillBoost | 4 | 2026 | arXiv:2607.26643 | Auto | None | C1 | Oct 26 |
| S2 | SkillChain | 4 | 2026 | arXiv:2606.12984 | Auto->Huma | None | C3,C2 | Oct 26 |
| S2 | SkillComposer | 4 | 2026 | arXiv:2606.06079 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillEvoReg | 4 | 2026 | arXiv:2609.30861 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillFoundry | 3 | 2026 | arXiv:2604.03964 | Auto | None | C1 | Oct 26 |
| S2 | SkillGen | 4 | 2026 | arXiv:2605.10999 | Auto | None | C2 | Oct 26 |
| S2 | SkillGLoW | 4 | 2026 | arXiv:2609.02217 | Auto | None | C2 | Oct 26 |
| S2 | SkillLift | 4 | 2026 | arXiv:2609.15396 | Auto | None | C3 inner, C2 outer | Oct 26 |
| S2 | SkillOps | 4 | 2026 | arXiv:2605.13716 | Auto | None | C2 | Oct 26 |
| S2 | SkillSmith | 4 | 2026 | arXiv:2606.01314 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillSpec (consensus-gated) | 4 | 2026 | arXiv:2610.00704 | Auto | None | C1,C2 | Oct 26 |
| S2 | SuperAGI Toolkits | 1 | 2024 | github.​com/​TransformerOptimus |  |  |  | May 26 |
| S2 | TRUSS | 3 | 2026 | arXiv:2608.17588 | Auto | None | C1,C2 | Oct 26 |
| S2 | VALVE | 4 | 2026 | arXiv:2609.32990 | Auto | None | C1 | Oct 26 |
| S2 | VCE-Skill | 4 | 2026 | arXiv:2608.16544 | Auto | None | C1,C2 | Oct 26 |
| S2 | Voyager | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| S2 | Web2BigTable | 3 | 2026 | arXiv:2604.27221 | Auto | None | C1,C2 | Oct 26 |
| S2 | Who Maintains Agent Skills? (empirical) | 2 | 2026 | arXiv:2609.05677 | Human | None | C3 | Oct 26 |
| S2 | WikiSkill | 4 | 2026 | arXiv:2608.27454 | Auto | None | C2 | Oct 26 |
| S2 | XRepoSkill | 4 | 2026 | arXiv:2609.36807 | Auto | Auto-parti | C1 | Oct 26 |
| S3 | A-MEM | 3 | 2025 | NeurIPS 2025 |  |  |  | May 26 |
| S3 | Agent-native memory system evaluation (Zhou et a | 2 | 2026 | arXiv:2606.24775 | n/a | n/a | n/a | Oct 26 |
| S3 | AIM privacy-aware interoperable memory (Johnson  | 3 | 2026 | arXiv:2609.12320 | Auto | None | C3 | Oct 26 |
| S3 | Beyond the Harness (enterprise Text-to-SQL cards | 3 | 2026 | arXiv:2608.22830 | Auto | None | C2 | Oct 26 |
| S3 | ChatGPT Memory | 3 | 2024 | openai.​com |  |  |  | May 26 |
| S3 | Claude Memory | 3 | 2025 | anthropic.​com |  |  |  | May 26 |
| S3 | Cognee | 3 | 2024 | github.​com/​topoteretes/​cognee |  |  |  | May 26 |
| S3 | Compiled Memory (Rhodes & Kang) | 4 | 2026 | arXiv:2603.15666 | Auto-gated | None | C1 | Oct 26 |
| S3 | Control-plane placement / ForgetEval (Yang) | 2 | 2026 | arXiv:2606.15903 | n/a | n/a | n/a | Oct 26 |
| S3 | FRESH failure-aware heterogeneous graph memory ( | 4 | 2026 | arXiv:2609.28003 | Auto | None | C2 | Oct 26 |
| S3 | GateMem multi-principal memory-governance benchm | 2 | 2026 | arXiv:2606.18829 | n/a | n/a | n/a | Oct 26 |
| S3 | Gemini Code Assist Memory | 4 | 2025 | cloud.​google.​com |  |  |  | May 26 |
| S3 | Generative Agents | 3 | 2023 | arXiv:2304.03442 |  |  |  | May 26 |
| S3 | Governed Collaborative Memory (Cuadros et al.) | 5 | 2026 | arXiv:2605.04264 |  |  |  | May 26 |
| S3 | HippoRAG | 2 | 2024 | arXiv |  |  |  | May 26 |
| S3 | Honest Lying mitigation / programmatic failure s | 4 | 2026 | arXiv:2605.29463 | Auto | None | C1/C2 | Oct 26 |
| S3 | KV-cache rollback consistency (Zhang & Yang) | 2 | 2026 | arXiv:2608.15939 | n/a | n/a | n/a | Oct 26 |
| S3 | LangChain Primitives (legacy) | 1 | 2023 | langchain.​com |  |  |  | May 26 |
| S3 | LangGraph Long-Term Memory | 3 | 2024 | langchain.​com |  |  |  | May 26 |
| S3 | LangGraph Store / LangMem (2026 refresh) | 3 | 2026 | docs.​langchain.​com/​oss/​python | None | None | n/a | Oct 26 |
| S3 | Learning on the Job | 4 | 2026 | arXiv:2607.22157 | Auto+​Human | None | C2,C3 | Oct 26 |
| S3 | Letta MemFS + Context Repositories + Dreaming (2 | 4 | 2026 | docs.​letta.​com/​letta-code | Auto | Auto | C3 | Oct 26 |
| S3 | Mem0 | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | Mem0 Platform (2026 refresh: history, feedback,  | 3 | 2026 | docs.​mem0.​ai/​api-reference | Auto | None | C3 | Oct 26 |
| S3 | MemAudit post-hoc poisoned-memory audit (Tan et  | 3 | 2026 | arXiv:2605.23723 | Auto | None | C2 | Oct 26 |
| S3 | MemClaw / Governed Shared Memory (Margalit et al | 3 | 2026 | arXiv:2606.24535 | Auto | None | C3 | Oct 26 |
| S3 | MemGPT / Letta | 3 | 2023 | arXiv:2310.08560 |  |  |  | May 26 |
| S3 | MemGuard persisted verifier signals (Wang et al. | 4 | 2026 | arXiv:2608.21867 | Auto-gated | None | C3 | Oct 26 |
| S3 | MemoryBank | 3 | 2023 | Zhong et al.​ |  |  |  | May 26 |
| S3 | Mi-Memory lifecycle framework (Liu et al.; Xiaom | 3 | 2026 | arXiv:2607.18975 | Auto | None | C3 | Oct 26 |
| S3 | MIRIX | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | MPBench memory-poisoning study (Dash et al.) | 2 | 2026 | arXiv:2606.04329 | n/a | n/a | n/a | Oct 26 |
| S3 | NanoResearch Memory Module | 3 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S3 | PPMF provenance-preserving memory firewall (Xu e | 3 | 2026 | arXiv:2607.29167 | Auto | None | C1 | Oct 26 |
| S3 | REALM retrieval-driven memory reconsolidation (S | 4 | 2026 | arXiv:2609.16053 | Auto | None | C2/C3 | Oct 26 |
| S3 | Recuris recursive experiential-working memory (Y | 4 | 2026 | arXiv:2608.24876 | Auto-gated | None | C2 | Oct 26 |
| S3 | Reflexion | 4 | 2023 | arXiv:2303.11366 |  |  |  | May 26 |
| S3 | Revocation guard / Revoked but Still Authoritati | 3 | 2026 | arXiv:2609.08258 | Human | None | C1 | Oct 26 |
| S3 | Safe to Resume? checkpoint-rollback continuity ( | 2 | 2026 | arXiv:2608.29381 | n/a | n/a | n/a | Oct 26 |
| S3 | ShareMem | 4 | 2026 | arXiv:2609.32511 | Auto | Auto-parti | C3 | Oct 26 |
| S3 | SIx Harness / Memory as Infrastructure (Helwig) | 3 | 2026 | arXiv:2609.05510 | Auto | None | C2 | Oct 26 |
| S3 | SOAR Cognitive Architecture | 4 | — | Newell/​Laird |  |  |  | May 26 |
| S3 | SSGM stability-and-safety governed memory (Lam e | 2 | 2026 | arXiv:2603.11768 | None | None | n/a | Oct 26 |
| S3 | Stale constraints in inherited memory (Nakayashi | 2 | 2026 | arXiv:2608.25553 | n/a | n/a | n/a | Oct 26 |
| S3 | TMA-NM origin-bound memory authority (Louck) | 3 | 2026 | arXiv:2606.24322 | Auto | None | C1 | Oct 26 |
| S3 | TOKI bitemporal operator algebra (Wang) | 3 | 2026 | arXiv:2606.06240 | Auto or Hu | None | C3 | Oct 26 |
| S3 | Trust-scored memory sanitization (Devarangadi Su | 2 | 2026 | arXiv:2601.05504 | Auto gate | None | n/a | Oct 26 |
| S3 | Typed provenance + assertion guardrails / Stored | 3 | 2026 | arXiv:2609.02127 | Auto | None | C1 | Oct 26 |
| S3 | Utility Under Attack (Karunanidhi) | 2 | 2026 | arXiv:2608.21230 | n/a | n/a | n/a | Oct 26 |
| S3 | VerificAgent human-verified frozen memory (Nguye | 3 | 2025 | arXiv:2506.02539 | Human | None | C3 | Oct 26 |
| S3 | VerMem verifiable memory management (Sun et al.) | 4 | 2026 | arXiv:2608.03137 | Auto-gated | None | C2/C3 | Oct 26 |
| S3 | Voyager Skill Library | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| S3 | Zep / Graphiti | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | Zep / Graphiti bitemporal facts (2026 refresh) | 3 | 2026 | help.​getzep.​com | Auto | None | C3 | Oct 26 |
| S4 | Anthropic Tool Use API | 4 | 2024 | docs.​anthropic.​com |  |  |  | May 26 |
| S4 | Browser Tools (Playwright/Computer Use) | 3 | 2024 | anthropic.​com |  |  |  | May 26 |
| S4 | Claude Code Tool API | 4 | 2024 | docs.​anthropic.​com |  |  |  | May 26 |
| S4 | Code Interpreter | 3 | 2023 | openai.​com |  |  |  | May 26 |
| S4 | Cursor MCP Integration | 4 | 2024 | docs.​cursor.​com |  |  |  | May 26 |
| S4 | Devin / SWE-agent Tool Harness | 4 | 2024 | cognition.​ai |  |  |  | May 26 |
| S4 | Gemini Function Calling | 3 | 2024 | ai.​google.​dev |  |  |  | May 26 |
| S4 | GPT Actions | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | Harvey (Legal Vertical) | 5 | 2024 | harvey.​ai |  |  |  | May 26 |
| S4 | Hippocratic AI | 5 | 2024 | hippocraticai.​com |  |  |  | May 26 |
| S4 | LangChain Tools Abstraction | 3 | 2023 | langchain.​com |  |  |  | May 26 |
| S4 | LangGraph Tool Nodes | 4 | 2024 | langchain.​com |  |  |  | May 26 |
| S4 | LlamaIndex Tool Ecosystem | 4 | 2023 | llamaindex.​ai |  |  |  | May 26 |
| S4 | Model Context Protocol (MCP) | 5 | 2024 | modelcontextprotocol.​io |  |  |  | May 26 |
| S4 | OpenAI Assistants API | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | OpenAI Function Calling | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | Sierra | 4 | 2024 | sierra.​ai |  |  |  | May 26 |
| S4 | SkillSmith | 4 | 2026 | arXiv:2606.01314 | Auto | None | C1 | Oct 26 |
| S4 | Toolformer | 2 | 2023 | arXiv:2302.04761 |  |  |  | May 26 |
| S4 | ToolLLM / ToolBench | 3 | 2023 | arXiv:2307.16789 |  |  |  | May 26 |
| S5 | AgentConductor | 0 | 2026 | arXiv:2602.17100 | None | None | C2 | Oct 26 |
| S5 | AgentGrad | 4 | 2026 | arXiv:2609.08572 | Auto | None | C2 | Oct 26 |
| S5 | AgentVerse | 2 | 2023 | arXiv:2308.10848 |  |  |  | May 26 |
| S5 | AutoGen / MagenticOne | 3 | 2024 | arXiv:2308.08155 |  |  |  | May 26 |
| S5 | AWS Bedrock Multi-Agent | 2 | 2024 | aws.​amazon.​com |  |  |  | May 26 |
| S5 | Bilevel Autoresearch | 4 | 2026 | arXiv:2603.23420 | Auto | None | C1 | Oct 26 |
| S5 | CAMEL | 1 | 2023 | arXiv |  |  |  | May 26 |
| S5 | ChatDev | 2 | 2023 | arXiv:2307.07924 |  |  |  | May 26 |
| S5 | ContextEvo | 4 | 2026 | arXiv:2609.34649 | Auto | None | C2 | Oct 26 |
| S5 | Control System for Frozen Agents (Paul) | 4 | 2026 | arXiv:2607.25415 | Auto | None | C2 | Oct 26 |
| S5 | CrewAI | 3 | 2025 | docs.​crewai.​com |  |  |  | May 26 |
| S5 | Evo2Team | 4 | 2026 | arXiv:2609.34135 | Auto | Auto | C2 | Oct 26 |
| S5 | Growing Harness | 4 | 2026 | arXiv:2609.26760 | Auto | None | C2 | Oct 26 |
| S5 | HARBOR | 4 | 2026 | arXiv:2604.20938 | Auto | None | C2 | Oct 26 |
| S5 | HarnessForge | 4 | 2026 | arXiv:2606.01779 | Auto | None | C2 | Oct 26 |
| S5 | Inspect AI | 2 | 2024 | ukgovernmentbeis.​github.​io |  |  |  | May 26 |
| S5 | Institutional MAS architectures (Fei et al.) | 1 | 2026 | arXiv:2604.27691 | None | None | C2 | Oct 26 |
| S5 | LangGraph | 3 | 2024 | langchain.​com |  |  |  | May 26 |
| S5 | Letta | 3 | 2025 | letta.​com |  |  |  | May 26 |
| S5 | LlamaIndex Workflows | 2 | 2024 | llamaindex.​ai |  |  |  | May 26 |
| S5 | Memento-Skills | 4 | 2026 | arXiv |  |  |  | May 26 |
| S5 | MetaGPT | 2 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| S5 | Microsoft Semantic Kernel | 2 | 2024 | learn.​microsoft.​com |  |  |  | May 26 |
| S5 | Multi-Agent Evolve (MAE) | 4 | 2025 | arXiv |  |  |  | May 26 |
| S5 | OpenAI AgentKit | 4 | 2025 | openai.​com |  |  |  | May 26 |
| S5 | OpenAI Swarm | 1 | 2024 | openai.​com |  |  |  | May 26 |
| S5 | OpenHands / CodeAct | 3 | 2024 | arXiv:2407.16741 |  |  |  | May 26 |
| S5 | OptiMAS | 4 | 2026 | arXiv:2608.21918 | Auto | None | C2 | Oct 26 |
| S5 | PluginRSI | 4 | 2026 | arXiv:2609.32423 | Auto | None | C2 | Oct 26 |
| S5 | Pydantic AI | 2 | 2024 | pydantic.​dev |  |  |  | May 26 |
| S5 | Recursive Harness Self-Improvement (RHI) | 4 | 2026 | arXiv:2607.15524 | Auto | None | C3 | Oct 26 |
| S5 | Skill-MAS (meta-skill) | 4 | 2026 | arXiv:2606.18837 | Auto | None | C2 | Oct 26 |
| S5 | TACO | 4 | 2026 | arXiv:2604.19572 | Auto | None | C2 | Oct 26 |
| S5 | Task-CoEvolve | 4 | 2026 | arXiv:2608.20169 | Auto | None | C2 | Oct 26 |
| S5 | TOCOMAS | 4 | 2026 | arXiv:2609.37953 | Auto | None | C2 | Oct 26 |
| S5 | Vertex AI Agent Builder | 4 | 2024 | cloud.​google.​com |  |  |  | May 26 |
| S5 | Workflow-Designing Agents (WDA) | 4 | 2026 | arXiv:2609.32458 | Auto | None | C2 | Oct 26 |
| S6 | Agenta | 3 | 2024 | agenta.​ai |  |  |  | May 26 |
| S6 | Agentic Configuration Management ACM (Quessada-V | 3 | 2026 | arXiv:2608.11166 | None | Human | n/a | Oct 26 |
| S6 | AGENTS.md / AAIF | 5 | 2025 | agents.​md |  |  |  | May 26 |
| S6 | Anthropic skills repo | 4 | 2025 | github.​com/​anthropics/​skills |  |  |  | May 26 |
| S6 | Azure API Center MCP registry | 3 | 2026 | learn.​microsoft.​com | Human | Human | - | Oct 26 |
| S6 | Braintrust | 5 | 2024 | braintrust.​dev |  |  |  | May 26 |
| S6 | Cleric.ai | 2 | 2025 | cleric.​ai |  |  |  | May 26 |
| S6 | Competence Not Accuracy | 2 | 2026 | arXiv:2608.18719 | None | None | - | Oct 26 |
| S6 | Constitutional AI | 2 | 2022 | Anthropic |  |  |  | May 26 |
| S6 | Cursor Rules | 3 | 2024 | cursor.​com |  |  |  | May 26 |
| S6 | Decagon | 2 | 2026 | decagon.​ai |  |  |  | May 26 |
| S6 | DSPy compile | 3 | 2024 | dspy.​ai |  |  |  | May 26 |
| S6 | EvolveNet | 4 | 2026 | arXiv:2608.04968 | Auto | Auto | C2 | Oct 26 |
| S6 | EvoUndo | 4 | 2026 | arXiv:2608.28363 | Auto | None | C1 | Oct 26 |
| S6 | From Prompts to Contracts | 2 | 2026 | arXiv:2607.08028 | None | None | C1 | Oct 26 |
| S6 | Future AGI prompt lifecycle | 4 | 2026 | futureagi.​com/​blog | Auto | Auto | C3 | Oct 26 |
| S6 | GitHub Copilot enterprise | 4 | 2026 | github.​com |  |  |  | May 26 |
| S6 | Governance conversion (Davis et al. case study) | 3 | 2026 | arXiv:2607.01087 | Human | None | C2 | Oct 26 |
| S6 | Governed Capability Evolution (Qin et al.) | 3 | 2026 | arXiv:2604.08059 | None | Auto | C2 | Oct 26 |
| S6 | HackProbe | 3 | 2026 | arXiv:2609.04665 | Auto | None | C1 | Oct 26 |
| S6 | Inspect AI | 3 | 2024 | ukgovernmentbeis.​github.​io |  |  |  | May 26 |
| S6 | LangFuse | 3 | 2024 | langfuse.​com |  |  |  | May 26 |
| S6 | LangSmith Hub | 5 | 2024 | smith.​langchain.​com |  |  |  | May 26 |
| S6 | MCP Gateway & Registry (agentic-community) | 3 | 2026 | github.​com/​agentic-community | Human | Human | C1 | Oct 26 |
| S6 | NanoResearch | 2 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S6 | Official MCP Registry | 2 | 2026 | modelcontextprotocol.​io | Human | None | - | Oct 26 |
| S6 | OpenAI AgentKit Evals | 3 | 2025 | openai.​com |  |  |  | May 26 |
| S6 | OPRO | 2 | 2023 | arXiv |  |  |  | May 26 |
| S6 | Organizational Control Layer (Shi et al.) | 2 | 2026 | arXiv:2606.04306 | None | None | n/a | Oct 26 |
| S6 | Registry-Governed Agent Lifecycle / EDDOps on AW | 3 | 2026 | arXiv:2607.00345 | None | Auto+​Human | C3 | Oct 26 |
| S6 | Reward-Free Pairwise Validator | 4 | 2026 | arXiv:2607.14408 | Auto | None | C3 | Oct 26 |
| S6 | Runtime Skill Audit | 2 | 2026 | arXiv:2606.11671 | None | None | - | Oct 26 |
| S6 | Runtime-Independent Persistent Agents (Enoch) | 3 | 2026 | arXiv:2609.00546 | Human | Human | C1 | Oct 26 |
| S6 | SafeEvolve | 4 | 2026 | arXiv:2608.12851 | Auto | None | C3,C2 | Oct 26 |
| S6 | SAGE statistical acceptance gate (≠ SAGE 2512.17 | 4 | 2026 | arXiv:2609.36043 | Auto | None | C2 | Oct 26 |
| S6 | Self-Refine | 1 | 2023 | Madaan et al.​ |  |  |  | May 26 |
| S6 | Sierra Ghostwriter | 2 | 2026 | sierra.​ai |  |  |  | May 26 |
| S6 | SkillCoach | 3 | 2026 | arXiv:2607.01874 | Auto | None | C3,C1 | Oct 26 |
| S6 | SkillProbe | 2 | 2026 | arXiv:2603.21019 | None | None | - | Oct 26 |
| S6 | SkillSpec (intent-masked correctness) | 2 | 2026 | arXiv:2609.06052 | None | None | - | Oct 26 |
| S6 | TextGrad | 2 | 2024 | arXiv |  |  |  | May 26 |
| S6 | TrueFoundry MCP Gateway | 3 | 2026 | truefoundry.​com/​docs | Human | Human | - | Oct 26 |
| S6 | Vellum | 5 | 2024 | vellum.​ai |  |  |  | May 26 |
| S6 | Verifier-as-Gatekeeper (VaG) | 4 | 2026 | arXiv:2608.05810 | Auto | None | C2 | Oct 26 |
| S6 | W&B Weave (Prompts) | 3 | 2024 | weave-docs.​wandb.​ai |  |  |  | May 26 |

```{=latex}
\endgroup
```
