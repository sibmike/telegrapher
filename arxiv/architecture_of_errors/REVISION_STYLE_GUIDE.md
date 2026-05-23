# Revision Style Guide for *The Architecture of Errors*

The one-line rule:

> **The body should make the reader understand why the framework matters; the appendix should make the reader trust that the math checks out.**

This guide governs every future edit to both the arXiv preprint and the NeurIPS submission package for *The Architecture of Errors*. It exists so the paper stops drifting back into math-first compression and stays in the frame:

> **Meaning first. Formal machinery second. Full proof in appendix.**

---

## 1. Every section must answer: "What does this mean?"

Each major section opens with the engineering meaning before the notation.

**Bad pattern:**

> Let $C_D$, $C_{\text{seen},D}(T)$, and $C_{\text{active},D}(n)$ be...

**Better pattern:**

> A deployed system does not face every possible failure. It faces the failures reachable inside its operational patch. We therefore distinguish the full patch catalogue, the modes already discovered from samples, and the modes a single sequence can activate.

Then introduce notation.

Rule:

> **Meaning → notation → result → implication.**

Never:

> **Notation → derivation → implication buried at the end.**

---

## 2. Body carries the argument; appendix carries verification

The body persuades the reader that the framework is useful. The appendix lets a skeptical reader verify the math.

**Body contains:**

- Plain-English claim.
- Minimal formal statement.
- Proof sketch.
- Engineering interpretation.
- Pointer to appendix.

**Appendix contains:**

- Full proof.
- Full derivation.
- Edge cases.
- Alternative assumptions.
- Sensitivity analysis.
- Algebraic steps.

This is especially important for Proposition 1, Proposition 2, and the sequence-level derivation. The body must never crash all of that into one dense block.

---

## 3. Each proposition gets five parts

Every formal result follows this format.

**A. Motivation.** One short paragraph: why do we need this result?

**B. Statement.** Formal but compact.

**C. Proof sketch.** No full algebra. No multi-line derivation unless absolutely necessary.

**D. Engineering meaning.** Plain English.

**E. Appendix pointer.** "Full derivation in Appendix A.x."

Example body voice:

> **Engineering meaning.** Universal reliability is not a finite-library problem. Patch-local reliability is. The operational task is to estimate the local catalogue and deploy enough interventions to cover the head mass.

---

## 4. Never let a formula appear before its job is clear

Before every important equation, one sentence explaining what the equation is doing.

**Bad:**

$$
m \geq \lceil |C_{\text{eff}}|^{1 - \varepsilon / e_{\text{hard}}} \rceil
$$

**Better:**

> The budget question is: how many top modes must the library cover so that the remaining hard-error mass falls below the target $\varepsilon$? Under the log-coverage approximation, that requirement becomes:
>
> $$ m \geq \lceil |C_{\text{eff}}|^{1 - \varepsilon / e_{\text{hard}}} \rceil. $$

Rule:

> **No naked equations.** Every equation needs a job description.

---

## 5. Use "patch-local" everywhere the claim depends on $D$

The paper lives or dies on not sounding universal.

**Use:**

- "patch-local catalogue"
- "fixed deployment patch"
- "reachable catalogue inside $D$"
- "domain-constant after saturation"
- "local mode-discovery curve"
- "patch-indexed planning prior"

**Avoid:**

- "the failure catalogue"
- "the intervention dictionary"
- "LLM failures are finite"
- "50 interventions cover failures"
- "reliability is solved"

The claim is:

> **Finite or effectively capped inside a fixed operational patch. Not finite universally.**

---

## 6. Empirical claims are evidence, not proof

The empirical layer supports the model. It does not prove the model.

**Prefer:**

- "suggests"
- "is consistent with"
- "motivates"
- "supports the modelling choice"
- "provides an anchor"
- "is evidence against the naive independent-error model"

**Avoid:**

- "establishes"
- "proves"
- "demonstrates conclusively"
- "dissolves"
- "decisively shows"

---

## 7. Keep the central narrative visible in every section

The paper's core story:

> **Universal finite reliability is impossible. Deployed systems are patch-local. In patches, failures repeat. Repeated failures can be catalogued. Catalogued failures can be targeted. Therefore reliability becomes local catalogue engineering, not universal token-length doom.**

Section jobs:

- **Introduction:** why universal framing is wrong.
- **Related work:** evidence that failures cluster and interventions are selective.
- **Theory:** formal transition from universal impossibility to patch-local budget.
- **Evidence:** why the assumptions are plausible.
- **Practical implications:** how an engineer uses the framework.
- **Discussion:** where the framework breaks.
- **Appendix:** verification and derivation.

If a paragraph does not serve one of these jobs, cut or move it.

---

## 8. Separate three different "counts"

Never blur these:

1. **Events:** raw failures observed.
2. **Modes/categories:** recurring kinds of failures.
3. **Capabilities/interventions:** engineering fixes.

The paper defines L1–L4 for this reason. Future edits preserve this distinction.

**Preferred wording:**

> $F(m)$ tracks cumulative hard-error mass over ranked L2 categories, while deployed capabilities operate at the coarser L4 level.

**Avoid:**

> "$m$ categories" / "$m$ interventions" / "$m$ modes"

unless the unit is explicit.

---

## 9. Always distinguish per-hard-token from sequence-level

Any claim about "90% reduction," "50 patterns," or "polylog budget" must say whether it is:

- per-hard-token, or
- sequence-level.

Rule:

> If the claim is about intervention budget, default to **per-hard-token** unless explicitly stated otherwise.

For body text, use:

> This is a per-hard-token result. One-shot sequence-level reliability is stricter and may require near-full catalogue coverage.

The warning lives in the body; the derivation lives in the appendix.

---

## 10. Replace "proof voice" with "engineering voice" in the body

**Body voice:**

> This result tells an engineering team what object to measure.

**Not body voice:**

> By substituting Eq. 2 into Eq. 3 and rearranging...

That algebra belongs in the appendix.

Use body sentences like:

> The bound is not a universal law of LLM behavior. It is the consequence of three modelling choices: a fixed patch, a head-heavy coverage curve, and slow active-mode discovery.

Then the appendix does the math.

---

## 11. Use "rule of thumb" language for numbers

For numbers like $\sigma \approx 1.85$, $\approx 50$ interventions, 17 categories, 28 citations:

**Use:**

- "planning prior"
- "anchor"
- "rule of thumb"
- "current-taxonomy estimate"
- "not a universal constant"

**Avoid:**

- "the required number"
- "the true catalogue size"
- "the exact rate"
- "guarantees"

Example:

> $\approx 50$ named interventions is a planning prior calibrated to current taxonomies, not a universal constant.

---

## 12. Each paragraph has one job

Heaviness usually comes from paragraphs doing three jobs at once: formal definition, empirical claim, caveat, and implication.

Paragraph discipline:

- Paragraph 1: claim.
- Paragraph 2: evidence.
- Paragraph 3: caveat.
- Paragraph 4: implication.

Not all four compressed into one monster paragraph.

---

## 13. Citation density: body conclusion, appendix anchors

Dense citation blocks get the same treatment as dense proof blocks:

> **Body = conclusion and why it matters.**
>
> **Appendix/table = exact anchors, numbers, citations, caveats.**

**Pattern:**

> **Body paragraph:** one claim, 1–3 representative citations, meaning.
>
> **Appendix table:** full citation harvest, numbers, dataset sizes, assumptions, caveats.

Each empirical paragraph follows this shape:

1. **Claim:** what do we learn?
2. **Representative evidence:** 1–3 examples.
3. **Caveat:** what does this not prove?
4. **Pointer:** full table / details in appendix.

---

## Editing checklist for every future pass

For each section, ask:

1. Does the section open with meaning before notation?
2. Are universal claims explicitly blocked?
3. Are patch-local claims clearly labeled?
4. Are formulas introduced by their engineering purpose?
5. Are full derivations moved to appendix?
6. Are empirical claims phrased as evidence, not proof?
7. Are per-hard-token and sequence-level claims separated?
8. Are events, modes, and interventions kept distinct?
9. Are numbers framed as anchors / planning priors, not constants?
10. Does the section advance the central story?

If any answer is "no," revise.

---

## Appendix structure (paper-specific)

The paper currently uses this appendix layout. Future edits preserve it:

| Appendix | Contents |
|---|---|
| A | Formal Proofs, Derivations, and Sensitivity Analysis (A.1 Prop 1 proof, A.2 Prop 2 derivation, A.3 sequence-level, A.4 propositions-vs-theorems, A.5 Heaps variant) |
| B | Full Failure-Mode Taxonomy and the Capability-Elimination Harvest (the 28-citation table, 12 clusters, additivity caveats, irreducible-semantic residual) |
| C | Counter-Evidence Re-audits (Dziri, BABILong, METR, Wan, NoCha) |
| D | Patch Evidence Detail (the table of evidence types supporting patch-indexing) |
| E | Empirical Calibration Detail (the σ-calibration table with sources, $T$, $|C|$, implied σ, role) |

Body cross-references use the standard letter form: "Appendix A.2", "Appendix B", "Appendix D", "Appendix E".

---

## Voice rule, restated

> **The body makes the reader understand why the framework matters.**
>
> **The appendix makes the reader trust that the math checks out.**
