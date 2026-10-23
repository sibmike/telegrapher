## What the feedback allows a gate to know {#sec:signal}

A coding agent changes a repository rule and receives a test result within seconds. A scheduling assistant changes its booking procedure, and whether an appointment was made is known only later. A marketing assistant changes its tone instructions and receives a reviewer's preference. A research assistant changes its strategy and may learn whether the direction was productive only after months.

All four can propose a persistent edit, and the previous section found a gate on such edits nearly everywhere a local loop exists. What the gate can establish depends on the evidence it receives as a feedback signal: how soon the signal arrives, whether it is exact, and whether it depends on judgment determine how well the gate can estimate the change in loss. We divide the surveyed systems into four feedback classes by this signal (Table REF(tab:IV-1)); the class predicts where automatic acceptance and automatic promotion occur.

| Class | The signal the gate receives | What the gate can be | What stays hard | Corpus examples |
|---------|------------------------|--------------------|----------------------|--------------|
| C1 exact | A check that returns pass or fail, or an exact score, at once and repeatably: tests, compilers, answer keys | An automatic check, run over enough cases, and enough repeated runs of a stochastic agent, to sample the task mix | The lift is bounded and specific, an improvement in what the check measures on the cases it ran; the check names the failed output, not the coordinate that caused it; a check that is also the target can be gamed | DGM, AlphaEvolve, SkillOpt |
| C2 observed outcome | A real result one episode later: a booked slot, a merged pull request, a closed ticket; noisy and confounded | An automatic threshold over batched episodes; a person at promotion | The outcome says *that* the episode failed, not *why*; the channel can be poisoned | Devin, Sierra, SAGE, SkillRL, PACE, Voyager |
| C3 judged | A rater, a rubric, or a model judge; no ground truth | A judge calibrated against people; a person at promotion | The rubric is itself a scaffold coordinate, so the gate judges edits to itself; the proxy gets optimized past the point where it tracks quality | SkillForge, CASCADE, skills-repository review |
| C4 delayed | An outcome weeks or months later, once per many edits | No immediate per-edit gate; proposals are pruned and milestones stand in until the outcome arrives | Credit across many edits; drift; the loop cannot be told from random search | NanoResearch, CORAL, the AI Scientist |

Table IV-1. The four feedback-signal classes. Reading across a row: what the gate receives, what it can therefore be, and what it cannot fix.

We assign each system to a class by the constraint that binds first. A long delay makes a signal C4 even when the eventual outcome is objective. Among timely signals, a signal with no independent ground truth is C3. Among timely objective signals, repeatable exact checks distinguish C1 from noisy observed outcomes in C2. A system may use several signals, but its operative acceptance decision must be read against the signal that supports that decision.

### Exact checks: C1

A compiler, proof checker, schema validator, or exact-match answer key can decide a specified property immediately and repeatably. Such a check is straightforward to implement as an automatic gate. AlphaEvolve scores candidates through a cascade of exact evaluators [@alphaevolve2025]. Its archive's diversity does not make it a delayed-signal example: the candidates are already scored, so archive selection is a search strategy within C1 [@alphaevolve2025]. SkillOpt uses held-out exact-match evaluation [@yang2026skillopt]. DGM decides acceptance more narrowly: it retains self-modifications that pass a sandboxed compile-and-edit functionality check on ten benchmark tasks. DGM's broader benchmark score weights parent selection from the archive rather than determining retention [@zhang2025darwin].

An exact check is exact about the output it scores, not about the deployment. The check returns the same answer each time it runs on the same output, but the agent produces stochastic outputs, and a finite suite samples only part of the patch. A gate that estimates the change in patch loss must account for both, and passing the suite establishes only what the suite tests.

Two problems remain even with a reliable checker: attribution, and the side effects of cheap, repeated acceptance. A failed test may not identify the instruction or skill that caused the failure. Repeated optimization against the same suite can overfit the scaffold to it, and cheap acceptance can let the artifact pool grow without sufficient pruning. Exact feedback makes evaluation easier but supplies neither attribution nor lifecycle management.

### Observed outcomes: C2

An observed outcome records what happened after an episode: whether an appointment was booked, a ticket closed, a pull request merged, or a tool call succeeded. It is meaningful but may be noisy or confounded: a user can accept an incorrect answer or reject a correct one, and a merged pull request reflects more than the agent's technical performance.

In different systems, the same kind of outcome supports different operations. Devin reads merged pull requests as feedback [@cognition2025devinreview]. SAGE measures task success in AppWorld [@wang2025sage], and PACE uses failure signals from a deployed small model [@ling2026pace]. SkillRL uses a success-rate threshold only to trigger proposals, without testing whether the proposed skills should remain [@skillrl2026].

Simulated outcomes remove the user confound and can be sampled repeatedly, as in Voyager's game world or SAGE's AppWorld. We treat them as a separate case within C2. For observed outcomes generally, an automatic gate needs a positive margin and enough episodes or independent evidence to absorb noise. Even then, the outcome usually reveals that the task failed more readily than why it failed.

Promotion is harder: another deployment may differ in users, tasks, and acceptance behavior, so a sender's successful outcome does not evaluate the recipient. Feedback in this class is also only as reliable as its source, because its channels can carry poisoned memories or injected tool instructions.

### Judgments: C3

For style, persuasion, design, or other preference-dependent tasks, a gate relies on a person, rubric, reference comparison, or model judge. No independent exact answer exists for the preference being measured. CASCADE uses a human-and-agent gate for memory consolidation [@huang2025cascade], and a reviewer approves promotion into Anthropic's skills repository. SkillForge applies its calibrated judge to replies, identifying those that motivate a rewrite [@skillforge2026].

A program can make these decisions, but its score must first be calibrated against the human judgment it is meant to represent; only then is the score evidence of that preference. The gate labels deliberately do not record calibration: an uncalibrated model judge is still an Auto gate, though what its acceptances mean is less established. SkillForge, SkillChain, and SkillCoach report calibration measurements [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach]; no other surveyed judge does.

A judge can also be gamed, and it can move. A scaffold optimized against a judge can become better at satisfying it while becoming worse at the underlying task. Reward-model research measures this proxy overoptimization [@gao2023overoptimization]. Human judges move as well: Shankar et al. find that evaluators' criteria change as they grade more outputs [@shankar2024validators]. A system that also edits the rubric changes the instrument used to assess its subsequent edits. Section REF(sec:reflexive) develops this **reflexive gate**.

### Delayed outcomes: C4

Research programs and open-ended discovery may produce meaningful outcomes only after weeks or months and many intervening edits. The AI Scientist illustrates the setting by generating ideas, conducting experiments, and writing a paper [@lu2024aiscientist]. The eventual outcome cannot usually be assigned to each preceding edit.

Systems in this class consequently decide at intermediate points, with operations that can prune or consolidate proposals but do not estimate each edit's contribution to the eventual loss. NanoResearch merges skills by semantic compatibility [@xu2026nanoresearch], and CORAL periodically promotes findings into shared memory [@qu2026coral].

For C4, the descent interpretation applies only to whatever proxy gate is available or to an evaluation at the longer horizon. Besides the credit problem, the environment can change before the result arrives. As the evaluation of harness optimizers emphasizes, outcome gains alone cannot distinguish directed improvement from a successful search [@ong2026harnesseval].

### Consequences for the two loops

The classification yields three expectations that can be checked against the corpus. First, exact checks and observed outcomes support local automatic acceptance most directly, while judged acceptance depends on calibration. Second, automatic promotion that estimates a loss change should occur only where a comparable check can be applied at the recipient, in exact and re-runnable simulated settings. Human promotion should hold the observed outcomes and judgments, and delayed feedback supports no immediate per-edit gate in either loop. Third, the main failure risks should differ: overfitting to a suite and pool growth under exact feedback, corrupted outcome channels under C2, proxy overoptimization under C3, and drift under C4.

These are expectations about the evidence a gate can establish, not restrictions on whether software can execute a decision. The gate grid in Section REF(sec:design) makes this qualification explicit: a program can merge two judged artifacts or prune a delayed proposal without estimating a loss change.
