## How adaptation can undermine its own evidence {#sec:failure}

An improvement loop changes the context in which its next decision is made. New rules can conflict with old ones, a corrected memory can still be retrieved in its earlier form, and a frequently reused evaluator can become a target. These failures extend the technical-debt concerns identified for machine-learning systems by Sculley et al. [@sculley2015debt]. The literature documents six of these failures in a measured case; a seventh, overfitting to one deployment, follows from the scope of the loss rather than from a measurement. Table REF(tab:X-1) connects each to the control that addresses it.

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

As instructions accumulate, following them becomes harder and latency increases [@jaroslawicz2025ifscale]. Ratchet's finding that model-written skills need lifecycle hygiene before producing gains makes the consequence visible at the system level [@zhang2026ratchet]. Conflicting or obsolete artifacts also complicate attribution: an evaluation may detect failure without revealing whether the cause is the new candidate or an older artifact. Gated retirement, pruning, and expiry preserve the conditions under which a new edit can be meaningfully assessed.

Persistent memory creates another route to lasting error. PoisonedRAG demonstrates attacks on retrieved knowledge [@zou2024poisonedrag], AgentPoison plants backdoors in long-term memory or knowledge bases [@chen2024agentpoison], and memory control-flow attacks operate across major agent frameworks [@xu2026mcfa]. Tool outputs and connected servers can also insert instructions into the model's context [@greshake2023injection; @debenedetti2024agentdojo]. In CVE-2025-54136, a previously approved MCP configuration could be changed without renewed approval [@checkpoint2025mcpoison].

These failures motivate provenance, write gating, and reversible memory changes [@su2026chronomem; @yu2026rollbackrepair], together with restricted tool permissions and an instruction privilege hierarchy [@wallace2024hierarchy]. The tool binding itself must be subject to controlled revision. Checking only the initial registration leaves later changes outside the decision that authorized it.

Rollback also needs to account for derivation. If a contaminated skill has been used to create other skills, restoring its earlier version does not remove those descendants. VaG's limited recovery after such rollback [@shang2026vag] supports checking contamination before commitment and tracking consequences after it. A version history is a prerequisite for this work, but it does not perform the recovery by itself.

### When the evaluator changes {#sec:reflexive}

Consider a pitch-review assistant that consistently overrates decks claiming a large market without supporting numbers. The team revises its rubric from "evaluate market size" to "require a numeric estimate and a source." The edit may improve reviews, but it also changes the standard used to evaluate subsequent behavior. If the same rubric judges future rubric revisions, the improvement process is modifying its own measuring instrument.

This is the reflexive-gate problem introduced with C3 feedback. The survey finds three scaffold systems reporting calibration of a judge against people: SkillForge, SkillChain, and SkillCoach [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach]. None reports calibration for a judge that is itself being edited. The missing result is therefore more specific than an absence of calibrated judges. It concerns maintaining calibration while the criterion changes.

Weight-level reinforcement learning has encountered a related problem in extending verifiable rewards to open-ended tasks. Some methods hold the judge fixed, using checklists, pairwise preferences, references, or rubrics [@gunjal2025rubrics; @jia2025writingzero; @shi2026references; @jin2026rlaes]. Others update the reward, rubric, or judge alongside the policy [@yu2025rlpr; @xu2026rubricarm; @ding2026evorubrics; @zhu2026score; @li2026rubricem]. Among the co-evolving methods reviewed, only RLPR reports agreement with human labels, and its reward is a probability rather than a rubric. The comparison is tabulated in the audit notes (Supplementary Material S6); these weight-side methods are not included in the scaffold scores.

Even a fixed evaluator can become unreliable through repeated use. Optimizing a proxy beyond a point can reduce the underlying quality [@gao2023overoptimization]. Unequal exposure to evaluation data can create apparent performance gains [@singh2025leaderboard]. Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite remains fixed. Human criteria themselves can shift during grading [@shankar2024validators]. Consequently, a gate needs its own held-out checks, calibration where judgment is involved, and revision history.

The failure-mode hypothesis discussed in Section REF(sec:why) adds a conditional implication: if deployment failures concentrate in recurring modes, uniformly sampled tasks may underrepresent the modes that most need correction. Evaluation should then include those modes while preserving a held-out assessment. The requirement is broader than improving a benchmark score: score alone cannot tell a harness optimizer from trial and error [@ong2026harnesseval], so the evaluation must also test the claimed link between failures and edits.

### Scope, coordination, and drift

Some failures arise from the structure of the deployment. A study of multi-agent systems identifies fourteen failure modes, prominently including role confusion and context lost between agents [@cemri2025mast]. Treating routing and role assignments as editable scaffold coordinates makes them subject to evaluation and rollback alongside instructions and skills.

Specialization creates a related boundary. A scaffold adapted to one deployment can degrade another because the tasks and preferred behavior differ. Receiving-side evaluation limits this risk at promotion; the evidence radius records where the improvement has been tested. This does not eliminate uncertainty outside the evaluated cases.

Finally, the scaffold can become less adaptable as old rules, polluted memories, and drifting tool versions accumulate. Long-context degradation [@liu2023lostmiddle] provides one related mechanism. Expiry, pruning, and rollback must remain available throughout the system's lifetime, especially when delayed feedback arrives too slowly to keep the artifacts current.

The feedback classes help organize these risks without making them exclusive to one class. Exact checks invite suite overfitting and cheap accumulation; observable outcomes depend on channels vulnerable to poisoning and injection; judged feedback is exposed to proxy optimization and moving criteria; delayed feedback makes drift difficult to correct promptly. Production systems provide individual controls, but the surface stays largely unmitigated because no surveyed system runs them together.
