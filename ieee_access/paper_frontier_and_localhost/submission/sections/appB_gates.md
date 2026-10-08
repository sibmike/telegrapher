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

The first five families populate $G_t$ directly and inherit the descent guarantee of Appendix REF(app:formal) under its assumptions. Semantic merge and archive selection are not estimators of $\widehat{\Delta} L_D$; they constrain the proposal distribution, and the descent argument applies to the composition of pruning and gate. Multi-sample agreement is listed because it is the correct analogue of "wait for $k$ pieces of evidence before accepting an edit", a different operation from mini-batch averaging and one that should not be conflated with it. Read down the signal-class column. The only families available to a judged (C3) deployment are the two whose estimator is a judge, and a delayed (C4) deployment has no family that estimates the loss change per edit at all: what it has is semantic merge before the gate and whatever proxy milestone stands at the horizon. That is the structural content of Section REF(sec:signal).
