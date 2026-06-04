# Review Digest — *Frontier and Localhost: How Production AI Learns Outside the Weights*

> Digest of the full editorial review. Contains **the main idea** (takeaway · contribution · essence) and a **goal-driven summary of every section** (purpose + how it's achieved). The complete review — alignment analysis, redundancy/noise audit, micro-drainer catalog, and the per-section revision plan — lives in the planning report, not here.
>
> Source reviewed: `submission/body.tex` (2,613 lines) + abstract in `main.tex`, read end to end. Line numbers refer to `body.tex` unless noted.

---

## PART 0 — THE MAIN IDEA (takeaway · contribution · the thing to chew on)

### The single-line thesis (the paper's own words, 44–45)
> **The field has built an external adaptation layer for LLMs, but not the optimizer that should govern it.**

### The takeaway, stated plainly
Production AI in 2025–2026 has quietly grown a **second learning system** that lives *outside the model weights*. Frontier weights update in months; the systems built on top update continuously — in markdown instruction files, persistent memories, retrieved skills, registered tools, eval suites, agent topologies, version-controlled prompt repos, and PR-gated governance. That fast-changing wrapper around a slow-changing frontier is the **scaffold**. The field already built it. What it has *not* built is the **optimizer and governance** that the scaffold needs. Today the scaffold is run as **patchwork**: fixes proposed by intuition, committed with weak credit assignment, accumulated without pruning, and promoted beyond where they were validated.

### The contribution (what is actually new)
The contribution is explicitly **not** "prompts are weights." It is to **name a missing optimizer** for an adaptation layer the field has already built, and to give that optimizer a concrete shape:

1. **Artifact-layer descent** — the disciplined limit of scaffold maintenance, expressed as two loops:
   - **Loop 1** (local): a recurring failure → a candidate edit to one scaffold coordinate → a gate that accepts only if it lowers *patch loss* → persistence with rollback.
   - **Loop 2** (promotion): the *separate* decision of how far that fix should travel, bounded by **evidence radius** — a fix spreads only as far as its evidence reaches.
2. **A survey of ~130 systems (2023–2026)** that locates production on a *patchwork → random-search → descent* gradient (Stages 1/2/3), with an auditable discriminator and evidence tiers.
3. **A named missing architecture** — *governed cross-tenant scaffold optimization* — defined by four properties: (a) auto-gated Loop 1, (b) multi-tenant cross-org promotion, (c) versioned lineage with RBAC, (d) rollback. **No surveyed system fills it.**

### The "oh shit, I need to chew on this" essence
The field built a learning machine out of markdown files, evals, PRs, and rollback buttons **without noticing it was a learning machine** — so it has no theory, no optimizer, and no governance for the *discrete, gated, auditable* learning happening there. Once you name the surface, the classical learning problems (credit assignment, overfitting, forgetting, local optima) reappear in context space, and the single most consequential open architecture problem becomes obvious and concrete: an automated local optimizer married to auditable cross-tenant aggregation. The reframing is the payload; the gap is where it bites.

### Three coinages that carry the contribution (protect and elevate these)
- **artifact-layer descent** (the framework)
- **evidence radius** (the promotion bound — the most original and currently most under-served idea)
- **governed cross-tenant scaffold optimization** (the named gap — the climax)

---

## PART 1 — GOAL-DRIVEN SUMMARY OF EVERY SECTION (purpose + how it is achieved)

Format: **Goal** = the job the section must do for the argument. **How** = the mechanism by which it does it.

### Abstract (main.tex 89–91)
- **Goal:** Compress the full arc into one paragraph and pre-commit the reader to the thesis.
- **How:** problem (adaptation moved outside weights) → diagnosis (patchwork) → solution name (artifact-layer descent) → 4-step pipeline (residuals→coordinates→deltas→gated promotion bounded by evidence radius) → survey scale (~130) → finding (the gap) → disclaimer ("not the claim that prompts are weights").

### §1 — The gradient moved outside the model [1–50]
- **Goal:** Establish that deployment-time adaptation has migrated outside the weights, and reframe a pile of disparate engineering artifacts as **one adaptation surface** that needs an optimizer.
- **How:** kills the old "the model is the system" mental model → asserts production stopped behaving that way → reframes each artifact (Skill = procedural weight, Rule = local parameter, RAG = patch memory, etc.) as one surface → drops the bold single-line thesis (44–45) → previews the *patchwork→random-search→descent* roadmap. Includes an honest caveat that "gradient" is a metaphor, not calculus.

### §2 — Why patch errors live outside the weights [52–159]
- **Goal:** Justify *why* the scaffold — not the weights, not per-tenant fine-tunes — is the practical substrate for high-churn, tenant-specific, auditable adaptation; and introduce the Stage 1/2/3 maturity ladder.
- **How:** three bolded structural arguments — (1) frontier training optimizes for *breadth* and is trained-to-be-unable to encode one tenant's idiosyncrasies (cites RLHF homogenization + Tiwari two-timescale); (2) production reliability is achieved in *depth* on exactly what training smoothed away; (3) encoding every patch in weights is economically/release-cycle/interference infeasible → therefore scaffold dominates on four constraints at once (cheap, inspectable, reversible, locally scoped). Lands the "frontier generalises / scaffold specialises" tagline. Introduces the **Stage 1/2/3 table** (patchwork / random artifact search / artifact-layer descent) and the "becomes descent once five pieces are in place" hinge.

### §3 — Artifact-layer descent [161–332]
- **Goal:** Make the framework *precise* — define the loop, the loss, the gate, the two loops, the operating assumptions, and the scope hierarchy.
- **How:** plain-English single-loop narration (log→cluster→prioritize by recurrence×severity→locate coordinate→synthesize edit→gate on patch loss→keep/rollback→bound promotion by evidence radius) → "most production doesn't close it" → two-loop decomposition → assumptions box (i)–(vi) → patch scope hierarchy (USER⊂PROJECT⊂STACK⊂TENANT⊂CORE) → loss equation L_D(θ_s) → gated update rule → gate accept condition with complexity penalty Ω and margin τ → "two distinct knobs" (edit magnitude = learning rate; promotion radius = target) → FedAvg disambiguation → gate vocabulary (Auto/Human/None) anchoring §§5–9 → mechanism-vs-metaphor restatement + pointer to Appendix E.

### §3.5 — SkillOpt and the convergence on artifact-layer descent [334–543]
- **Goal:** Defend the framework against "you made this up" — show §3's picture is a real, independently-converged-upon mechanism, with SkillOpt as the canonical worked instance.
- **How:** SkillOpt walkthrough (markdown skill as trainable state; 7 DL-style controls) → compact §3↔SkillOpt correspondence table → headline empirics (52/52 cells best-or-tied; transfer numbers) → "the same pressure arrives from ≥14 independent directions" → 5-cluster convergence table → "what the convergence establishes" (four claims i–iv) → pointer to Appendix G.

### §4 — Six scaffold substrates [545–592]
- **Goal:** Define the coordinate system of θ_s — the six independently-editable substrates the survey scores against.
- **How:** S1–S6 table (Instructions, Skills, Memory, Tools, Orchestration, Governance) with "what persists" + "Score-5 mark" → uniform 0–5 rubric (0 ephemeral … 5 two-loop versioned promotion + governance) → invariance note (descent argument is partition-independent given independent editability).

### §5 — Survey method [594–632]
- **Goal:** Establish the survey's rigor and auditability so the empirical claims are defensible.
- **How:** scope/corpora (~130 systems, Jan 2023–May 2026; assembled by searching for "self-improving/scaffolded/agentic," filtered by the patch-local discriminator) → core (~90) vs contrast (~38) split → stricter composite two-loop criterion (22 audited, 13 pass) + two relaxations → evidence policy T1–T5 with pooling discipline.

### §6 — Substrate maturity is uneven [634–719]
- **Goal:** Deliver empirical finding #1 — the field converged on the six substrates, but no system matures all six at once.
- **How:** per-substrate aggregate table (n, mean score, Score-5 systems, finding) → "two things stand out" (universal six-substrate convergence; nobody matures all six; maturity tracks which constraints each system was built for) → "five absences" that recur as future-work targets (failure-triggered memory, cross-customer skill promotion, memory versioning, scaffold curriculum, held-out evals at Loop-2).

### §7 — Four clusters [721–842]
- **Goal:** Deliver empirical finding #2 — four architectural archetypes, located on the patchwork→descent gradient and by which loop is automated.
- **How:** cluster table (Research full-auto / Production hybrid / Governance-first / Open standards, with rep systems + Loop1/Loop2 + "what it proves") → per-cluster prose with exemplars (NanoResearch, SkillOpt, AlphaEvolve, DGM; SkillForge, CASCADE, Sierra, Devin; Braintrust/Vellum/LangSmith; AGENTS.md/MCP/Skills/Rules) → vertical-bundle placement + single-agent (Tran & Kiela) caveat constraining S5 claims.

### §8 — The two-loop design space [844–924]
- **Goal:** Re-cut the composite-two-loop subset into a 3×3 gate-type matrix and read off the **empty cells** — the direct setup for §9.
- **How:** 3×3 matrix (Loop-1 {Auto/Human/None} × Loop-2 {Auto/Human/None}) → three populated cells explained → three empty cells with distinct structural reasons → two cross-cutting findings (n=1 generation / batching largely absent; multi-layer hierarchies under-explored) → pointer to Appendix F.

### §9 — The missing architecture: governed cross-tenant scaffold optimization [926–1016]
- **Goal:** The payoff — convert a vague gap into a precise, auditable four-property criterion that no system satisfies.
- **How:** four properties (a)–(d) → "closest approaches partition the requirements" (AlphaEvolve, SkillForge, SkillOpt, CORAL, PACE, Meta-Harness, Sierra, governance-first — each holds a subset) → "in ML terms: a privacy-preserving cross-tenant aggregator with an automated eval gate" (five parts) → DP-FedAvg analogy with its caveat → deployment-dependence caveat → "names what would have to be true for the question to be testable."

### §10 — A new failure surface [1018–1101]
- **Goal:** Show the *cost* of running the scaffold without an optimizer — and tie each failure mode back to a missing optimizer piece.
- **How:** seven quantified failure modes, each with an "architectural mitigation": scaffold bloat (IFScale 35× latency, Ratchet signal-quality), poisoned memory (PoisonedRAG 90%+), prompt injection via tools/MCP (MCPoison CVE), eval fragility (Leaderboard Illusion + Goodhart + Ong harness-eval), coordination failures (MAST 14 modes), patch overfitting (structural), plasticity loss at scaffold level. Closes: "Every entry names a piece of the optimizer current systems don't yet have."

### §11 — Conclusion [1103–1134]
- **Goal:** Restate the thesis, bookend §1, and leave the reader holding the gap.
- **How:** para 1 restates "built the layer, not the optimizer" + the Stage ladder + the named gap; para 2 "the field built a second learning system … once named, the missing pieces become concrete targets"; para 3 the "frontier generalises / scaffold specialises … turning today's patchwork into tomorrow's optimizer" close.

### Appendices (verification machinery)
- **A** [1138–1297]: 30 representative survey rows (system, year, substrate, Loop1/Loop2, PP, evidence tier, why included).
- **B** [1301–1368]: corpus sizes, core/contrast split, inclusion/exclusion, evidence-tier distribution, scoring discipline, **composite-criterion sensitivity analysis**.
- **C** [1372–1443]: gate-type → estimator-family mapping (eval-cascade, RL-threshold, LLM-judge, surrogate, reviewer; semantic-merge & MAP-Elites as proposal-pruning; multi-sample agreement).
- **D** [1447–1529]: contrast set — systems that carry the name but fail the discriminator, with the failed criterion.
- **E** [1533–1801]: the formalization — mechanism stack (6 ops), setup/notation, descent inequality (A1–A2), convergence proposition (A3–A5), optimization-analogy correspondence, credit-assignment-without-chain-rule, four worked cases (RAG/pitch/tool/memory), Loop-1/Loop-2 as radii, overfitting.
- **F** [1804–1933]: cell-by-cell two-loop matrix, closest-approaches enumeration supporting §9, deployment-dependence argument.
- **G** [1937–2613]: SkillOpt walkthrough (G.1–G.3), convergent cluster detail (G.4–G.8), synthesis (G.9), SkillOpt vs §9 properties (G.10), cost/bloat (G.11).
