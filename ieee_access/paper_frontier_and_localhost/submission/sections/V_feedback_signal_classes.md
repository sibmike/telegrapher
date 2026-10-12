## What the feedback allows a gate to know {#sec:signal}

A coding agent changes a repository rule and receives a test result within seconds. A scheduling assistant changes its booking procedure and learns later whether an appointment was made. A marketing assistant changes its tone instructions and receives a reviewer's preference. A research assistant changes its strategy and may wait months to learn whether the direction was productive.

All four systems can propose a persistent edit. What differs is the evidence available for accepting it. The signal's timing, exactness, and dependence on judgment determine how well a gate can estimate the change in loss. We divide the surveyed systems into four feedback classes, summarized in Table REF(tab:IV-1).

| Class | The signal the gate receives | What the gate can be | What stays hard | Corpus examples |
|---------|------------------------|--------------------|----------------------|--------------|
| C1 exact | A check that returns pass or fail, or an exact score, at once and repeatably: tests, compilers, answer keys | An automatic check, run over enough cases, and enough repeated runs of a stochastic agent, to sample the task mix | The lift is bounded and specific, an improvement in what the check measures on the cases it ran; the check names the failed output, not the coordinate that caused it; a check that is also the target can be gamed | DGM, AlphaEvolve, SkillOpt |
| C2 observable outcome | A real result one episode later: a booked slot, a merged pull request, a closed ticket; noisy and confounded | An automatic threshold over batched episodes; a person at promotion | The outcome says *that* the episode failed, not *why*; the channel can be poisoned | Devin, Sierra, SAGE, SkillRL, PACE, Voyager |
| C3 judged | A rater, a rubric, or a model judge; no ground truth | A judge calibrated against people; a person at promotion | The rubric is itself a scaffold coordinate, so the gate judges edits to itself; the proxy gets optimized past the point where it tracks quality | SkillForge, CASCADE, skills-repository review |
| C4 delayed | An outcome weeks or months later, once per many edits | No immediate per-edit gate; proposals are pruned and milestones stand in until the outcome arrives | Credit across many edits; drift; the loop cannot be told from random search | NanoResearch, CORAL, the AI Scientist |

Table IV-1. The four feedback-signal classes. Reading across a row: what the gate receives, what it can therefore be, and what it cannot fix.

The classes are assigned by the constraint that binds first. A long delay makes a signal C4 even when the eventual outcome is objective. Among timely signals, the absence of an independent ground truth makes the signal C3. Among timely objective signals, repeatable exact checks distinguish C1 from noisy observed outcomes in C2. A system may use several signals, but its operative acceptance decision must be read against the signal that supports it.

### Exact checks: C1

A compiler, proof checker, schema validator, or exact-match answer key can decide a specified property immediately and repeatably. This makes an automatic gate straightforward to implement. AlphaEvolve scores candidates through a cascade of exact evaluators [@alphaevolve2025], and SkillOpt uses held-out exact-match evaluation [@yang2026skillopt]. DGM makes a narrower acceptance decision: it retains self-modifications that pass a sandboxed compile-and-edit functionality check on ten benchmark tasks. The broader benchmark score weights parent selection from the archive rather than determining retention [@zhang2025darwin].

Exactness applies to the check, not to the deployment as a whole. Repeating a deterministic check on the same output yields the same answer, but an agent produces stochastic outputs, and a finite suite samples only part of the task distribution. Estimating the change in patch loss still requires accounting for that variation. Passing the suite also establishes only the properties the suite tests.

Two problems remain even with a reliable checker. A failed test may not identify the instruction or skill that caused the failure, and repeated optimization against the same suite can overfit it. Cheap acceptance can also allow the artifact pool to grow without sufficient pruning. Exact feedback makes evaluation easier; it does not supply attribution or lifecycle management.

### Observed outcomes: C2

A booked appointment, closed ticket, merged pull request, or successful tool call provides an observable result after an episode. The result is meaningful but may be noisy or confounded. A user can accept an incorrect answer or reject a correct one, and a merged pull request reflects more than the agent's technical performance.

Devin reads merged pull requests as feedback [@cognition2025devinreview]. SAGE measures task success in AppWorld [@wang2025sage], and PACE uses failure signals from a deployed small model [@ling2026pace]. SkillRL uses a success-rate threshold only to trigger proposals, without testing whether the proposed skills should remain [@skillrl2026]. The same kind of outcome can therefore support different operations in different systems.

Simulated outcomes, such as those in Voyager's game world or SAGE's AppWorld, remove the user confound and can be sampled repeatedly. They are treated as a distinguishable case within C2. For observed outcomes more generally, an automatic gate needs a positive margin and enough episodes or independent evidence to absorb noise. Even then, the result usually reveals that the task failed more readily than why it failed.

Promotion is harder because another deployment may differ in users, tasks, and acceptance behavior. A sender's successful outcome is not an evaluation of the recipient. This class also depends on channels that can carry poisoned memories or injected tool instructions, connecting the reliability of feedback to the integrity of its source.

### Judgments: C3

For style, persuasion, design, or other preference-dependent tasks, a gate relies on a person, rubric, reference comparison, or model judge. There is no independent exact answer to the preference being measured. CASCADE uses a human-and-agent gate for memory consolidation [@huang2025cascade], and a reviewer approves promotion into Anthropic's skills repository. SkillForge uses its calibrated judge earlier in the process, to identify replies that motivate a rewrite [@skillforge2026].

A program can make these decisions, but its score must be calibrated against the human judgment it is intended to represent before the score is treated as evidence of that preference. The gate labels deliberately do not record this distinction: an uncalibrated model judge is still an Auto gate, though the meaning of its acceptances is less established. SkillForge, SkillChain, and SkillCoach report calibration measurements [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach]; no other surveyed judge does.

Optimization introduces another risk. A scaffold can become better at satisfying the judge while becoming worse at the underlying task. Reward-model research measures this form of proxy overoptimization [@gao2023overoptimization]. Human evaluation is not fixed either: Shankar et al. find that evaluators' criteria change as they grade more outputs [@shankar2024validators]. If the system also edits the rubric, it changes the instrument used to assess subsequent edits. This **reflexive gate** is developed in Section REF(sec:reflexive).

### Delayed and sparse outcomes: C4

Research programs and open-ended discovery may produce meaningful outcomes only after weeks or months and many intervening edits. The AI Scientist illustrates the broad setting by generating ideas, conducting experiments, and writing a paper [@lu2024aiscientist]. The eventual outcome cannot usually be assigned to each preceding scaffold change.

Systems in this class consequently use intermediate decisions. NanoResearch merges skills by semantic compatibility [@xu2026nanoresearch]. CORAL promotes findings into shared memory on a heartbeat [@qu2026coral]. These operations can prune or consolidate proposals, but they do not estimate each edit's contribution to the eventual loss. AlphaEvolve's archive diversity does not make it a delayed-signal example: its candidates have already been scored by exact evaluators, so archive selection is a search strategy within C1 [@alphaevolve2025].

For C4, the descent interpretation applies only to whatever proxy gate is available or to an evaluation at the longer horizon. Temporal credit assignment remains unresolved, and the environment can change before the result arrives. Outcome gains alone are also insufficient to distinguish directed improvement from a successful search, a limitation emphasized in the evaluation of harness optimizers [@ong2026harnesseval].

### Consequences for the two loops

The classification yields three expectations that can be checked against the corpus. First, local automatic acceptance is most directly supported by exact checks and observed outcomes. Judged acceptance depends on calibration, while delayed feedback cannot evaluate edits individually until the outcome arrives. Second, automatic promotion that estimates a loss change should occur only where a comparable check can be applied at the recipient, in exact and re-runnable simulated settings, and human promotion should hold the observed outcomes and judgments. Delayed feedback supports no immediate per-edit gate on either half. Third, the main failure risks should differ: overfitting to a suite and bloat under exact feedback, corrupted outcome channels under C2, proxy optimization under C3, and drift under C4.

These are expectations about the evidence a gate can establish, not restrictions on whether software can execute a decision. A program can merge two judged artifacts or prune a delayed proposal without estimating a loss change. Section REF(sec:design) makes this qualification explicit in the gate grid. In every class, sharing remains an additional empirical question: even the same exact checker must be applied to the recipient's relevant cases before broader performance is established.
