# Plan: Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models (IEEE Access Topical Review)
Status: REVIEWED 2026-10-22 (P1–P4 passed; agent review; author sign-off pending on the open decisions and flags in §8) · clarity-and-grace, Full size, Revise mode
Source: `../main.tex`   Last checked against text: 2026-10-22, after the clarity-and-grace revision (pre-revision copy: IEEE version of 2026-10-12, 11:22). Diagnostic ledger: `main.ledger.md`; reverse outline: `main.reverse_outline.md`.
Intake: Full · Revise · genre: research paper (topical review) · readers: see the frame card · American spelling · house style: `telegrapher-style-profile`, which overrides this skill's defaults (`docs/STYLE_GUIDE.md` does not exist in this repository) · venue: IEEE Access, official `ieeeaccess.cls`, numeric citations · invariants: no claim, number, citation or cross-reference changes (every one was audited; see `../ledger_parts/K_final_wording_audit.md`).

## 1. Frame card

### Recovered from the text (S1-R)
| Field | Content | Status |
|---|---|---|
| Topic | Whether the reliability of LLM outputs must decay exponentially with their length | FOUND (abstract, I ¶1) |
| Shared context | A widely cited argument (LeCun; the step-level proofs of Dziri et al.) says that per-token errors compound into exponential failure, and that only a non-autoregressive architecture can escape it | FOUND (I ¶1) |
| Condition | **Two conditions in two places.** (a) I ¶2: "Whether it does, and under which conditions, is a practical question…", an unknown with no turn word. (b) II-D: no existing review composes these findings into the probability that a long output is correct. | FOUND, SPLIT |
| Cost | "a practical question for anyone building on these models" (I ¶2), which is vague. LeCun's conclusion, in I ¶1, carries the real stakes but is not tied to the reader. | WEAK |
| Point | The uniform argument's two assumptions both fail. A two-rate model that counts decisions instead of tokens is consistent with the evidence, and it says where exponential decay returns (when steps add decisions). So the argument cannot establish exponential decay as a general law. | FOUND (I ¶3) |
| Readers | Not named. Inferred: ML and NLP researchers and IEEE Access reviewers; engineers building long-output and agentic systems | INFERRED |
| Problem type | Conceptual, with a practical bridge (where reliability effort belongs) | INFERRED |

### Fresh frame (R-1), built from the readers and the problem
| Field | Content | Status |
|---|---|---|
| Readers | (1) ML and NLP researchers who cite or test the compounding-error argument, including IEEE Access reviewers. They know LLMs and decoding; they don't know all four literatures. They will decide whether to accept the argument's ceiling and what to measure next. (2) Engineers building long-reasoning or agentic systems. They know the systems, not the theory. They will decide where to spend reliability effort. | PROPOSED (the paper names no reader; its contributions and Section VIII imply both) |
| Problem type | Conceptual; the bridge to action runs through Section VIII | PROPOSED |
| Shared context | The uniform argument: a fixed, independent chance of error per token, so (1−e)^n. Its formal step-level versions (Dziri et al.). Its conclusion: training cannot remove the problem; only a different architecture can. | FOUND |
| Condition (but…) | **One condition:** the argument rests on two assumptions, uniform risk across positions and independent errors. The evidence on each is scattered across literatures reviewed separately (attention sparsity and compression; generation-time uncertainty; error dependence; representation geometry), and no review has composed it into the probability that a long answer is correct. | PROPOSED (merges I ¶2 and II-D) |
| Cost, per reader | Researchers: we cannot tell whether autoregressive generation has a length ceiling, and so whether the call for non-autoregressive models follows. Engineers: we cannot tell whether long outputs are doomed or where reliability effort belongs (more tokens, fewer tokens, or the decisions). | PROPOSED (built from I ¶1–¶2 and Section VIII; no new claim) |
| Point | Both assumptions fail. Risk concentrates at a minority of positions, and errors depend on one another. A two-rate model that counts decisions instead of tokens is consistent with the evidence. It predicts slow or bounded decay when decisions stay few and non-key risk stays summable, and exponential decay in decisions when every step adds decisions. So the uniform argument cannot establish exponential decay as a general law. Themes: **key positions** (importance and hardness), **dependence**, **the two-rate model**, **growth of k with n**. | FOUND |
| Motive / conflicts | The authors' own preprint is the origin, and a companion paper develops the intervention side. Both are disclosed (II-B, II-D). The AI-assistance disclosure is in the Acknowledgment. | FOUND |

**Differences between the two frames:**
- **F1:** the condition is split across I ¶2 and II-D.
- **F2:** the cost is vague and not tied to a reader.
- **F3:** no reader is named.
- **F4:** I ¶2 places evidence with its own caveat (the chain-of-thought study, "no controlled test of length") before the point. That evidence counts as a reason for doubt, not as context.

## 2. Point outline
**Document point:** the uniform argument's two assumptions both fail. Risk concentrates at a minority of positions, and errors depend on one another. A two-rate model that counts decisions is consistent with the evidence and predicts exponential decay only when steps add decisions. So the argument cannot establish exponential decay as a general law.
**Themes:** key positions (importance, hardness) · dependence · the two-rate model · how k grows with n.
**Order:** logical. The model comes first, then a test of each premise, then reconciliation, then consequences and open measurements. This is a Topical Review template, as IEEE Access asks: RQs, comparison tables, reconciliation, grading, future directions.

| § | Heading (themes) | Point sentence | Protagonists |
|---|---|---|---|
| I | Introduction | (paragraph-level outline in §2.1) | the uniform argument; the evidence; the two-rate model |
| II | Scope and Method | The review covers work on three properties (importance, error origin, dependence), was assembled by a narrative search, was checked passage by passage, and differs from existing reviews by composing their findings into the probability that a long answer is correct. | this review; the evidence; existing reviews |
| III | A Simple Model of Sequence-Level Error | The uniform model rests on two assumptions. The two-rate model replaces it, and its prediction turns on how k grows with n and on whether non-key risk is summable. That turns the question about length into three questions (RQ1–RQ3). | the uniform model; key positions; k(n); the non-key factor |
| IV | RQ1: Token Importance | At each step a minority of earlier positions carries the information used. The set moves, high attention is not content, and aggressive compression breaks reasoning. So the evidence supports uneven risk but does not estimate k. | positions; studies (Fang, Quest, R-KV…); the important set |
| V | RQ2: Token Hardness | Errors originate disproportionately at a minority of decisions, and targeting those decisions helps. Uncertainty misses some, and some failures spread over a trace. So e_key belongs to decisions, not to high-entropy tokens. | decisions / forking and critical tokens; entropy; probes |
| VI | RQ3: Error Dependence and Representation Structure | Errors depend on one another within an answer and across samples and models. Geometry suggests why but is untested. Dependence concentrates failures in fewer answers and limits voting. | errors; models; representations; voting |
| VII | Reconciling the Evidence | The reported fractions measure different things and do not estimate k. Agent decay is decay in decisions. Six cases mark where the two-rate account fails. The grades show which premises are unmeasured. | fractions; agent evaluations; the argument; the evidence |
| VIII | Implications for System Design | If reliability is set by a few decisions, effort belongs at those decisions. Four practices follow; latent channels need the same scrutiny. | engineers' practices; methods |
| IX | Open Problems | Five measurements would turn the argument into a tested account, k(n) first. | the measurements |
| X | Conclusion | Restated point → significance (counting decisions changes the prediction) → now what (measure k(n)). | — |
| App A | Derivations | The algebra behind Table I, the non-key bound, the union/association bound and the vote. | — |
| App B | Adjacent Lines of Work | Each of the review's five choices meets an older line. Each subsection ends on how this review's question differs. | — |

### 2.1 Introduction: paragraph outline (target, from the fresh frame)
| ¶ | Role | Point (1 sentence) | Protagonist | Themes | Evidence / source |
|---|---|---|---|---|---|
| I.1 | shared context | The uniform argument: (1−e)^n per token, step-level proofs, and LeCun's conclusion that only a non-autoregressive model escapes. | the argument / its proponents | uniform model | lecun2023why, dziri2023faith (unchanged) |
| I.2 | problem: turn + condition + cost | **But** the argument rests on two assumptions, uniform risk and independent errors. The evidence on each lies in literatures reviewed separately, and token count is already a poor guide (the CoT case, with its caveat). Cost: reasoning models and agents now produce outputs long enough that, if the argument held, they would almost never be correct. We cannot tell whether they must fail, or where reliability effort belongs. | the argument's assumptions → the evidence → builders | uniform risk, independence | cai2025rkv, kwa2025measuring, wei2022chain (unchanged; no new claim) |
| I.3 | point | Both assumptions fail. A two-rate model that counts decisions fits the evidence and says where exponential decay returns. So the argument cannot establish a general law. | this review / the evidence | key positions, dependence, two-rate model, decisions | (unchanged) |
| I.4 | housekeeping | RQs, five contributions, preprint note, pointer to §II. | — | RQ1–RQ3 | (unchanged) |

## 3. Theme registry
| Concept | Locked term | Never use (drifting synonyms) |
|---|---|---|
| eq. (1) as a model | "the uniform model" | "the pessimistic model" |
| the argument from (1) to a ceiling | "the uniform argument" | "the pessimistic argument" (I ¶ / III-A opener may keep "pessimistic" once as a description, not as a name), "the case for exponential decay" |
| the k positions in eq. (2) | "key positions" | "key tokens" (keyword only), "critical positions" |
| what a key position carries | "decisions" / "key decisions" (the decisions at key positions) | "decision points" outside RQ2's literature summary |
| eq. (2) | "the two-rate model" | "the two-rate picture" (VII-C may keep "picture" for the whole account; the audit logged that) |
| the non-key factor | "non-key risk" (the summed error probability at non-key positions) | "residual risk", "other positions' cumulative risk", "residual error rate" (unify on first use; "residual" may gloss once) |
| RQ1 handle | "importance" | "salience" |
| RQ2 handle | "hardness" | "difficulty" (when meaning per-position hardness; "task difficulty" is a separate concept) |
| RQ3 | "dependence" | "non-independence", "correlation" (allowed for the statistical quantity) |
| growth law | "how k grows with n" / "k(n)" | "decision count" (allowed in Table V only), "number of key positions" (allowed as gloss) |

## 4. Claims ledger (the claims that carry the argument; the citation-level ledger is `../citation_ledger.md` + `../ledger_parts/`)
| Claim (where) | Supported where | Strength stated vs warranted | Qualifier required | Status |
|---|---|---|---|---|
| A minority of positions carries the long-range information at each step (IV, abstract, X) | Table II; IV-A | "mostly find"; strong behavioral evidence; Table V "Strong" | the set moves with the step; does not estimate k | OK (audited) |
| Errors originate at a minority of decisions (V) | Table III; V-A | "supported", qualified in V-B/V-C | sensitivity ≠ origin (Lin et al.); confident and distributed errors | OK |
| Errors within an answer are dependent (VI-A) | snowballing, self-conditioning, self-correction | Strong; reasoning models partly escape | 2023-era models | OK |
| Wrong answers are shared across samples and models (VI-C) | Kim; Goel; Table IV | Moderate | agreement ≠ dependence (App. A-D); shared difficulty is a simpler account | OK |
| Geometry explains clustering (VI-B) | indirect | "Hypothesis; indirect support" | untested | OK |
| Slow decay needs sublinear k and summable non-key risk (III-C, VII-B, VII-D, X) | III-C; Table V rows 6–7 | assumption; not measured | stated everywhere it is used | OK (reviewer pass 2026-10-12) |
| Exponential decay returns in decisions in agentic tasks (abstract, I, VII-B, X) | Kwa; Ord ("suggestive") | "as we argue" | Ord's rationale; consistent with | OK |
| The uniform argument cannot establish a general law (I ¶3, X) | follows from the above | argued | does not rule out exponential decay | OK |

## 5. Decisions log
| # | Question | Options | Decision | By / date |
|---|---|---|---|---|
| D1 | Name the readers in the introduction? | (a) name both reader types implicitly through the cost; (b) leave as is | PROPOSED (a), with no new claim: cost sentences in reader terms only | agent, 2026-10-22, for author confirmation |
| D2 | Keep the chain-of-thought example in the introduction? | keep as a reason for doubt / move to VII-C / cut | KEEP, placed as the reason for doubt that motivates the condition. The author kept it after the 2026-10-12 reviewer pass, and cutting it would remove the citation. | author 2026-10-12 (kept); placement agent 2026-10-22 |
| D3 | Keep the commercial-bridge (Mostik) footnote? | keep / delete | KEEP | author (the original request), 2026-10-03; reaffirmed 2026-10-12 |
| D4 | Reorder the five contributions by importance? | keep order / reorder | KEEP order (structural reordering of the author's contributions needs the author) | open → carried, no change |
| D5 | Merge the condition (I ¶2 + II-D) into one stated condition in the introduction? | merge / leave split | PROPOSED merge: the introduction states the condition, and II-D keeps the detailed review comparison | agent, 2026-10-22, for author confirmation |

## 6. Review record

**Triage (R-0), 2026-10-22: RESTRUCTURE.** There was no plan file. The recovered frame has two conditions (I ¶2 and II-D) and no named reader (F1–F3). Scope of the re-draft: the introduction's problem paragraph (I ¶2). The other units are decided in the gap table (§7).

**P1 Frame: PASS after the R-1 fixes.** Topic, why it matters and the point each fit in one sentence. There is one condition: the evidence on the two assumptions has never been assembled, so whether they hold is unknown. Cost is stated per reader. Problem type is conceptual, with a practical bridge (VIII). Motive and conflicts are disclosed (preprint, companion paper, AI use).

**P2 Outline: PASS.** Read alone, the point sentences make an argument. The order is logical. Intro roles run context → problem → point → housekeeping. The CoT evidence inside the problem paragraph is the turn ("reasons for doubt"), kept by D2.

**P3 Registry and claims: PASS.** Drift instances are listed in §3, and the polish pass fixes those that are prose. No claim in §4 is stronger than its support. One possible cross-section ambiguity is logged as A3.

**P4 Cold reader on the plan (Sonnet, 2026-10-22): PASS on recoverability.** It stated the problem, the point and the argument in substance. Its objections and how each was handled:
| # | Objection | Kind | Disposition |
|---|---|---|---|
| P4-1 | The condition has two prongs (the assumptions are untested; no review composes the evidence) | prose | FIX in the I ¶2 re-draft. One condition: the evidence on each assumption sits in separately reviewed literatures, so whether they hold is unknown. The review gap (II-D) stays as housekeeping detail in II-D. |
| P4-2 | The CoT example in I ¶2 reads as a stray anecdote | structure | KEEP (D2, the author's 2026-10-12 decision). The re-draft makes it the explicit reason for doubt that motivates the turn. |
| P4-3 | The cost to engineers is stated two ways ("almost never correct" vs "where effort belongs") | prose | FIX: one cost per reader in the re-draft. |
| P4-4 | "Both assumptions fail" is flat, while k and summability are unmeasured | claim | FLAG A1, no change. The text separates the qualitative failure of the assumptions (supported, Table V rows 1–4) from the unmeasured quantities of the prediction (rows 6–7). |
| P4-5 | Dependence is not in eq. (2) | claim/structure | NO CHANGE. Already handled in the text: III-A chain rule; "if failures are still treated as independent" (III-B); III-D "the independence that (2) still assumes"; VI-D. |
| P4-6 | "Minority" ≠ "few" (a minority can still grow linearly) | claim | FLAG A2. The text already separates them: IV-D "does not estimate k", VII-A. |
| P4-7 | VII-C "When the Argument Fails" and the abstract's "identify where the argument fails": which argument? The body says it is the two-rate picture. | referent | FLAG A3. Changing the object of a stated contribution is the author's call. |
| P4-8 | VIII prescribes while the account is unmeasured | claim | NO CHANGE. VIII opens conditionally ("If reliability is set by…") and cites published methods for each practice. |

Update to P4-7: VII-C's heading now reads "Where the Two-Rate Model Does Not Hold", which matches the subsection's own first sentence. The abstract's "identify where the argument fails" is unchanged and still flagged (A3).

## 7. Gap table (R-4)
Paragraph IDs follow `main.reverse_outline.md` and `main.ledger.md`. The ledger proposed 21 re-draft candidates. Decisions follow one rule: re-order, split, merge and move are allowed, but no claim verb, number, citation or cross-reference changes. A candidate whose fix would need one of those is **flagged**, not re-drafted.

| ¶ | Current role | Target | Decision | Reason |
|---|---|---|---|---|
| I.2 | doubt (CoT) → assumptions → condition → stakes → cost | turn + condition → cost → reason for doubt, leading into the point | **re-draft** (twice; final order: assumptions → *but* not assembled → open → stakes → cost → CoT doubt) | P4-1/P4-3; ledger top-4. The CoT is kept (D2) and placed last, as the bridge to the point. |
| I.3 | point | point; defined terms | keep + polish | "the uniform model fails at both of its assumptions" → "both assumptions fail" (the assumptions are now named in I.2; the uniform model is not yet defined); hidden doer in S6 removed |
| III (opening) | none | section point | **add** one sentence built from III-B.2 S5 and III-C.3 | highlight read (ledger top-3) |
| III-A.2 | definition + assumptions + third premise | two paragraphs | **split** | threshold (2.5, 3.1, 3.2, 3.6); the definition and the assumptions are separate jobs |
| III-D.1 | RQ list lead-in | names the two premises | keep + polish | the "first/second premise of (2)" in IV-C and V-C now has an antecedent (ledger top-13) |
| VII (opening) | none | section point | **add** two sentences built from VII-A S2, VII-B S6 and VII-D S5 | highlight read (ledger top-3) |
| VI-A.2 | recovery + training + locating | two paragraphs | **split** at "Training changes the picture." | one claim per paragraph (house style) |
| VI-C.2 | evidence + four cautions (268 words) | evidence ¶ + cautions ¶ | **split** at "These results come with cautions." | role/threshold; the cautions keep their order (re-ranking was left to the author) |
| VI-D.1 | "three findings limit the reading above", but two of the three bear on accumulation | geometry-limit ¶ + accumulation/summability ¶ | **split + reframe opening** | ledger top-2. The summability evidence now has its own labelled paragraph. It is not moved to III-C/VII-D, which would be a cross-section structural move. |
| VII-C list | Gema sentence inside the Tower of Hanoi bullet | Gema in "Additions that must be weighed" | **move** (one sentence, same citation) | illustration (ledger top-7); "this is the last row of Table I" is FLAG A6 |
| A-D.1 | ~11 claims in one paragraph | tail and table / correlation and shared cause / agreement ≠ dependence | **split** ×2 | threshold |
| B-B.2 | seven sources, 335 words | meaning-level uncertainty / relevance and self-knowledge / the floor | **split** ×2 | threshold |
| B-D.3 | voting limits + trials + decomposition | voting limits ¶ + reliability over trials and decomposition ¶ | **split**, plus one sentence split at the colon | threshold; 66-word sentence |
| IV-B.3, V-A.2 (S4), V-A.3 (S5–S6), V-B.2 (S3–S4), VI-B.2 (S5) | sentences supporting a neighboring claim | regroup | **flag, no move** (A9) | moving these across subsections changes what each "Evidence"/"Limits" block cites. The audit tied each sentence to its location; the author decides. |
| V.0 / V-C.1 | claim "originate" vs conclusion "sensitivity, not origin" | one verb | **flag** (A4) | a claim verb |
| VI (order) | within → why → across | within → across → why | **flag** (A8) | structural: moving VI-C.3 reorders subsections |
| VII-A.1, II-B.1, II-C.1, IV-A.2, V-A.1, B.0, B-A.3 | threshold candidates | — | **polish only** | each fails on redundancy and topic strings. Cutting the restatements would remove cross-references or caveats the audits placed deliberately, so the redundancy cluster (ledger top-8) is left to the author (A10). |
| All other paragraphs | — | — | keep → polish | — |

## 8. Change log and author flags (2026-10-22)

### Structural (re-drafted / split / moved / added)
1. I ¶2 re-drafted. One condition: the evidence on both assumptions is not assembled, so whether they hold is open. One cost per reader: whether LeCun's conclusion follows (researchers), and where to spend effort on reliability (builders). The CoT reason for doubt now leads into the point. *Interpretation to confirm:* "mostly for other ends, such as shrinking caches and prompts or quantifying uncertainty" condenses II-D (the reviews "each cover one of the mechanisms…usually as an efficiency or control technique").
2. Section III and Section VII each gained a short opening built only from claims already in the text.
3. Splits: III-A.2, VI-A.2, VI-C.2, VI-D.1 (with the new opening "Two results limit the geometric reading above." and a bridge sentence, "Other findings bear on how errors accumulate over a generation, and so on the summability assumption."), A-D.1 ×2, B-B.2 ×2, B-D.3.
4. Gema et al. moved from the Tower of Hanoi bullet to "Additions that must be weighed" (VII-C).
5. VII-C retitled "Where the Two-Rate Model Does Not Hold" (was "When the Argument Fails").

### R3–R6 (passage flow, sentence clarity, concision, shape)
- **R3 referents:**
  - VI-B.3 "the two kinds of error in Section III" → "errors at non-key positions from errors at key positions (Section III)".
  - II-C "recorded in the ledger" → "recorded in the citation ledger described below".
  - III-D.1 now names the two premises, which IV-C and V-C refer to by number.
- **R3 registry:**
  - "residual risk" → "risk at non-key positions" (VII-B, X).
  - "decision count / risk elsewhere" → "number of key decisions / non-key risk" (VII-D).
  - "pessimistic argument" → "uniform argument" (III-A).
  - "two-rate picture" → "two-rate model" (VII-C, B-B).
  - "pillar" → "line of evidence" (VII-D) and "the claims under each research question" (Table V caption).
  - "PaLM-540B" → "PaLM 540B" (VIII).
- **R4/R6 sentence shape:**
  - V-A.1 dangling modifier fixed ("when decoding branched…").
  - Bogdan: the qualifier ("preliminary") moved forward.
  - ProcessBench sentence split, with the doer named ("Experts who annotated…").
  - V-B.2: the 9 supporting settings now lead and the 14 follow, numbers unchanged.
  - VI-A.1: the 64-word snowballing sentence split.
  - IV-A.3: two long-subject sentences reshaped.
  - VIII.3: the three recovery tools enumerated with semicolons.
  - IX.1: the two paired measurements split into their own sentences.
  - B-D.3: split at the colon.
  - Abstract S3: split.
- **R5/R6 terms glossed on first use:**
  - "hazard" (III-A.3).
  - "coverage" (VIII.4). Checked against the Costello et al. ledger card: Pass@20/Pass@50.
  - "error mass" → "risk of error" (VII-A).
- **R6 wording:**
  - "raised its correlation … from −0.18 to −0.96" → "strengthened". The numbers are unchanged; the old verb fought the falling value. *Author to confirm.*
  - X.1 S2 no longer repeats I.3 S6 verbatim ("Exponential decay remains possible; what fails is the inference from per-token risk to a general law.").

### Invariant diff (S7)
Run `check_invariants.py` against the pre-revision copy. Results:
- 247 citation uses, 156 keys, 99 cross-references, 25 labels, 155 inline-math spans, 11 display/tabular blocks and 397 numerals: all identical.
- The only table difference is the Table V caption ("pillar").
- The abstract is 249 words.
- The build is clean, with the same 22 pages.

### Author flags (claim-level; the text is unchanged)
- **A1:** "both assumptions fail" (I.3, X) is flat, while k(n) and summability are unmeasured. The text keeps the two apart (Table V), so this is fine if intended.
- **A2:** "minority" vs "few". A minority can still grow linearly with n. IV-C and VII-A say so; consider one explicit sentence in III-B.
- **A3:** the abstract's "identify where the argument fails" refers to the two-rate model's failure cases (VII-C), but "the argument" elsewhere in the abstract is the uniform argument. Suggest "identify where the two-rate model fails".
- **A4:** V's claim says errors "originate" at a minority of decision points. V-C concludes that the studies show "where outcomes are sensitive, not where errors begin". Pick one verb and align V.0, Table V row 2 and VII-D S2.
- **A5:** VII-D S2 calls the evidence that "a minority of positions decides the outcome" "strong", while Table V grades RQ2 "Moderate to strong".
- **A6:** VII-C, Tower of Hanoi: a collapse beyond a complexity threshold is called "the last row of Table I", which predicts smooth exponential decay. Consider "is closer to the last row … than to a bounded budget". A cross-reference to the MAKER Hanoi result (B-D.3) is optional.
- **A7:** II-C counts "two exceptions … a classical inequality … and one paywalled paper". The Acknowledgment says "two paywalled sources were checked only against their abstract or bibliographic record". SUBMISSION_NOTES lists Hoeffding (paywalled, bibliographic record) and Lam and Suen (abstract only). The counts agree only if the "classical inequality" is the paywalled Hoeffding paper; consider saying so in II-C.
- **A8:** Section VI's claim announces within → across → why, but the subsections run within → why (geometry) → across. Moving VI-C.3 ("Models also fail together") up behind VI-A would match. This is structural.
- **A9:** sentences that support a neighboring claim: IV-B.3 S3–S4; V-A.2 S4 (Rho-1 training loss); V-A.3 S5–S6 (per-prompt compute; TokenSkip); V-B.2 S3–S4 (Candussio, an importance result); VI-B.2 S5 (planning features). Regroup or cut. Cutting would drop citations.
- **A10:** repeated caveats: "geometry untested" appears 7 times, "does not estimate k" 4, "importance ≠ hardness" 4, the voting condition 5. The house rule is honest accounting in one place. Trimming them removes cross-references, so the author decides.
- **A11:** notation. K (window length) sits next to k in IX.1, and B-D.3 uses k for τ-bench trials. Consider "$K$-token window" and "pass$^{\wedge}k$ over $k$ trials", or rename.
- **A12:** B-D.4 S7 reads agent decay curves as mixtures that decline more slowly than an exponential; VII-B never mentions it. B-C.3 puts input-side studies out of scope, while VII-C bullet 4 uses input additions as a failure case. Consider one cross-reference in each.
- **A13:** Appendix B's frame promises "five choices", but its sentences list six clauses that don't map one-to-one onto subsections A–E.

### S6 cold reader (Sonnet, text only, 2026-10-22): G6 PASS
It recovered the problem, the point, and every section's point (I–X, App. A–B), in substance. The role swap passes for the conclusion, but the reader is less sure what the paper asks practitioners to do (see A20).

Fixed after the cold read (prose only):
- **I.2:** "Whether the assumptions hold is therefore open" contradicted I.3's "both assumptions fail" and was introduced by this revision. It now reads "The evidence as a whole has therefore not been weighed against the assumptions".
- **I.2:** "Whether it does" → "Whether reliability does decay that way".
- **III opening:** "summable" was used before its definition → "the total risk at the other positions stays bounded".
- **VII-A:** "the *set* differs" → "the selected *set* differs".

Left as is, with reasons:
- The III-A independence paragraph and VI-D.2 ("dependence cuts both ways") are dense but carry exact probability reasoning. Further compression risks the meaning, so they stay.
- Near-synonyms such as forking, critical and pivotal tokens are the cited authors' own terms, so they are kept.

Claim-level objections from the cold read (FLAGS, no change):
- **A14:** "Risk is not uniform across positions" (I.3) vs "none of the studies estimates k or the hazard at the positions it finds" (V-C). The evidence shows information sparsity and outcome sensitivity, not measured hazard.
- **A15:** the RQ1 shares are fractions of tokens, and a constant fraction is the k ∝ n regime. The abstract and I.3 lean on the shares, while IV-C says they do not estimate k. Consider one sentence in the abstract or I.3 saying the slow-decay prediction rests on the unmeasured k(n).
- **A16:** the abstract calls IX's protocol "a direct test of how key positions grow", while IX calls it "a proxy on the importance side, not a count of errors".
- **A17:** "wrong answers agree across samples" (I.3) vs App. A-D "agreement among wrong answers does not by itself show dependence between samples". The cross-sample evidence is thinner than the cross-model evidence.
- **A18:** X, "The evidence suggests that the structure of internal representations is what makes errors cluster", vs Table V "Hypothesis; indirect support … no causal test of clustering". Consider "is a candidate explanation for why errors cluster".
- **A19:** Table III lists ProcessBench and the Li et al. entropy-gated beam search as support, while V-A notes the null reading (short solutions plus a constant rate) and that uniform beam search achieves most of the gain. VII-B's "k grows in proportion to the number of steps" for agents is an assumption that IX.5 still needs to test. This links to A12 (the mixture reading in B-D.4).
- **A20:** practitioners lack a plain "what to do" statement. VIII lists practices but does not say how to estimate k or e_key for one's own system. That would be a content addition, which is the author's call.

### Open decisions carried
D1 (readers named only through the cost), D4 (order of the contributions) and D5 (the condition now lives in I.2; II-D keeps the detailed comparison): agent-applied, for author confirmation.
