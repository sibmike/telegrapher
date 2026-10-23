## How adaptation can undermine its own evidence {#sec:failure}

Each edit the loop keeps or promotes changes the context of its next decision. New rules can conflict with old ones, a corrected memory can still be retrieved in its earlier form, and a frequently reused evaluator can become a target. These failures extend the technical-debt concerns that Sculley et al. identified for machine-learning systems [@sculley2015debt]. Table REF(tab:X-1) pairs each failure with its control in the loop. The literature documents six of them in a measured case; the seventh, overfitting to one deployment, follows from the scope of the loss rather than from a measurement. Production systems provide the individual controls, but no surveyed system runs them together.

| Failure | What goes wrong | The loop piece that answers it | Dominant class |
|------------|------------------------------|------------------------------|----------|
| Scaffold bloat | Rules and skills accumulate until the model follows them worse and the gate has no clean signal | Complexity penalty $\Omega$ in the gate; pruning and expiry as first-class gated operations | C1, C3 |
| Poisoned memory | An attacker writes an entry that later retrieval trusts | Provenance on every entry; write gating; a rollback envelope | C2 |
| Injection via tools and MCP | A tool's output or a connected server carries instructions into context | Narrow tool permissions; a privilege hierarchy over instructions; tool bindings pass the same promotion gate as any other coordinate | C2 |
| Evaluation fragility | The suite that gates edits is itself edited, gamed, and read non-independently | Held-out evaluations scoped within evidence radius, weighted toward recurring modes, re-read as the target drifts, checked against attribution | C3 (primary), C1 |
| Coordination failures | Multi-agent roles blur and context is lost between agents | Orchestration topology treated as a scaffold coordinate under the same gate and rollback discipline | C2 |
| Patch overfitting | A scaffold tuned to one deployment degrades another | Evidence-radius discipline at promotion; receiving-side held-out evaluation | C2 |
| Plasticity loss | Old rules, polluted memory, and drifting tool versions crowd out adaptation | Expiry and rollback as explicit loop operations rather than retrospective hygiene | C4 |

Table X-1. The failure surface of patchwork scaffold maintenance: what goes wrong, the piece of the loop that answers it, and the feedback-signal class in which it dominates.

### Accumulation and contamination

Accumulated instructions become harder to follow and slow the response [@jaroslawicz2025ifscale]. At the system level, Ratchet finds that model-written skills need lifecycle hygiene before they produce gains [@zhang2026ratchet]. Conflicting or obsolete artifacts also complicate attribution: an evaluation may detect a failure without revealing whether the new candidate or an older artifact caused it. Gated retirement, pruning, and expiry preserve the conditions under which a new edit can be meaningfully assessed.

Persistent memory and connected tools create another route to lasting error. PoisonedRAG demonstrates attacks on retrieved knowledge [@zou2024poisonedrag], AgentPoison plants backdoors in long-term memory or knowledge bases [@chen2024agentpoison], and memory control-flow attacks operate across major agent frameworks [@xu2026mcfa]. Tool outputs and connected servers can insert instructions into the model's context [@greshake2023injection; @debenedetti2024agentdojo]. In CVE-2025-54136, a previously approved MCP configuration could be changed without renewed approval [@checkpoint2025mcpoison].

These failures motivate the memory controls [@su2026chronomem; @yu2026rollbackrepair] and tool controls [@wallace2024hierarchy] listed in the table above, and also controlled revision of the tool binding itself. A check made only at the initial registration leaves later changes outside the decision that authorized the binding.

Rollback also needs to account for derivation: restoring a contaminated skill's earlier version does not remove the skills derived from it. VaG recovers little after such rollback [@shang2026vag], which supports checking for contamination before commitment and tracking consequences afterward. A version history is a prerequisite for this tracking but does not by itself perform the recovery.

### When the evaluator changes {#sec:reflexive}

Consider a pitch-review assistant that consistently overrates decks claiming a large market without supporting numbers. The team revises its rubric from "evaluate market size" to "require a numeric estimate and a source." The edit may improve reviews, but it also changes the standard used to evaluate subsequent behavior. If the same rubric judges future rubric revisions, the improvement process is modifying its own measuring instrument.

This is the reflexive-gate problem introduced with C3 feedback. Three scaffold systems (SkillForge, SkillChain, and SkillCoach) report calibrating a judge against people [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach], but no surveyed system reports calibration maintained across continuing rubric revisions and deployment drift. SkillCoach also evaluates its judge after editing it, in an offline audit that its authors describe as judge-assisted rather than a new human annotation study [@zhu2026skillcoach]. The audit compares the initial and evolved rubrics against human-gold references on 50 paired instances from 10 held-out task families, and trajectory-filtering consistency rises from 82% to 96%.

Weight-level reinforcement learning meets a related problem when it extends verifiable rewards to open-ended tasks; its methods, compared in the audit notes (Supplementary Material S6), are not included in the scaffold scores. Some hold the judge fixed, using checklists, pairwise preferences, references, or rubrics [@gunjal2025rubrics; @jia2025writingzero; @shi2026references; @jin2026rlaes]. Others update the reward, rubric, or judge alongside the policy [@yu2025rlpr; @xu2026rubricarm; @ding2026evorubrics; @zhu2026score; @li2026rubricem]. Among the co-evolving methods reviewed, only RLPR reports agreement with human labels, and its reward is a probability rather than a rubric.

Even a fixed evaluator can become unreliable through repeated use. It remains subject to the proxy overoptimization [@gao2023overoptimization] and the shifting human criteria [@shankar2024validators] described for judged feedback, and unequal exposure to evaluation data can create apparent performance gains [@singh2025leaderboard]. Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite stays fixed. A gate therefore needs its own held-out checks, calibration where judgment is involved, and a revision history.

The hypothesis in Section REF(sec:why), that failures in a bounded deployment fall into a catalogue of modes, has a conditional implication: if deployment failures concentrate in recurring modes, uniformly sampled tasks may underrepresent the modes that most need correction. Evaluation should then include those modes while preserving a held-out assessment. Score alone is not enough: it cannot tell a harness optimizer from trial and error [@ong2026harnesseval], so the evaluation must also test the claimed link between failures and edits.

### Scope, coordination, and drift

Some failures arise from the structure of the deployment. Cemri et al. identify fourteen failure modes in multi-agent systems, prominently including role confusion and context lost between agents [@cemri2025mast]. Treated as editable scaffold coordinates, routing and role assignments become subject to evaluation and rollback alongside instructions and skills.

Patch overfitting follows from specialization: a scaffold adapted to one deployment can degrade another, because the tasks and preferred behavior differ. Receiving-side evaluation limits this risk at promotion, and the evidence radius records where the improvement has been tested.

Finally, a scaffold can lose plasticity, becoming less adaptable as old and polluted artifacts accumulate. Long-context degradation [@liu2023lostmiddle] is one mechanism related to this loss. Expiry, pruning, and rollback must remain available throughout the system's lifetime, especially when delayed feedback arrives too slowly to keep the artifacts current.

No failure is exclusive to one feedback class, but the classes help organize the failure surface. Exact checks invite suite overfitting and cheap accumulation; observed outcomes depend on channels vulnerable to poisoning and injection; judged feedback is exposed to proxy optimization and moving criteria; delayed feedback makes drift difficult to correct promptly. Production systems provide individual controls, but the failure surface stays largely unmitigated because no surveyed system runs them together.
