# Revision log R: full clarity-and-grace review (2026-10-22)

Source revised: `submission/abstract.md` and `submission/sections/*.md` at commit 5038169 (the latest source; nothing newer existed on disk). Method: the `clarity-and-grace` skill at Full size in Revise mode, with the house style (`style/telegrapher_paper_style_guide.md`; the repository has no `docs/STYLE_GUIDE.md`) and the `writing-style` skill applied at R4 to R6. Claims, numbers, citation keys, cross-references, headings, tables, captions, display math, and bold terms are unchanged file by file (checked by a script that compares the frozen pre-revision copy with the result); every place where a better sentence would have needed one of them is an author flag below.

Artifacts kept beside the source:
- `submission/plans/paper_frontier_and_localhost.plan.md`: frame card (fresh and recovered), point outline, theme registry, claims ledger, decisions D1 to D13, review record (P1 to P4, S6).
- `submission/plans/paper_frontier_and_localhost.ledger.md`: the R-4 gap table, the S4 per-paragraph diagnostic ledger and the R-2 reverse outline for every section group, and the S5 change logs.

## Process

1. **S1-R and plan.** No plan file existed, so triage sent the paper to Restructure. The recovered frame showed the researcher's cost missing, the condition stated as a world condition rather than as what is unknown, and the point spread over three introduction paragraphs (plan 1c).
2. **P4 plan review** (Sonnet, plan only). Adopted: the knowledge gap as the primary condition, a sharper researcher cost, section openings that link IV to V and VI to VII. Not adopted: reordering V, VII, and IX (decision D8; the round-P order stands).
3. **S4 ledger and R-2 reverse outline** (five Opus readers, one per section group): every paragraph tested on every applicable test; 656 FLAG cells; 42 paragraphs met the re-draft threshold.
4. **R-6 re-draft and S5 polish** (five Opus writers on a working copy): the 42 paragraphs re-drafted from their target roles, every other paragraph polished R1 to R9, AI-failure-mode sweep on every rewritten sentence.
5. **S6 cold read** (Sonnet, text only). It recovered the problem and the point as the plan states them. Prose fixes applied from it: the Section VI opening now describes the grid before naming its rows; the introduction's closing point sentence is split in two; Section IX opens on why the loop is uneven.
6. **S7.** Invariant diff PASS; IEEE build, `check_revision.py`, `verify_ieee.py`, `check_cites.py` PASS; arXiv v4 rebuilt; all 22 IEEE pages rendered and inspected.

## What changed for the reader

- **Introduction.** The turn from context to problem is explicit ("But because edits are easy to make..."), and researchers now get their cost alongside practitioners: without knowing whether a system tests its edits, they cannot tell whether it improved or compare it with another. The paragraph on sharing opens on its finding. The point now closes I ¶7 in one place, naming the gate, the failure record and credit assignment, promotion, and feedback. The roadmap ends on the roadmap, not on a caveat.
- **Abstract.** Same sentences and numbers, reordered so it ends on the finding and its explanation rather than on the list of contributions; the locked terms (local loop, edit, observed and delayed outcomes, credit assignment) replace drifting synonyms.
- **Section openings.** IV opens on SkillForge and SkillRL and ends its opening on the 89-of-96 finding; V links back to IV and forecasts what the classes predict; VI forecasts the grid finding that used to arrive only in its last sentence; VII links back to promotion and states that no surveyed system runs the controls together; IX states why the loop is uneven; X states its five problems.
- **Repetition.** Each repeated caveat now has one home (D9): evidence bound to the measure and tasks tested (Section II), local success is not evidence for a recipient (II-C, VI-A), a delayed outcome cannot credit one edit (V-D). "Proposing an edit is not accepting it" is made once in IV. Restatements of Table 3 and Table 4 cells in prose are gone.
- **Placement.** IV's paragraph about proposing candidates moved into "Finding the right thing to change"; the AlphaEvolve note moved from the C4 paragraph to C1; EDDOps is no longer counted among "registries".
- **Appendices.** The convergence paragraph is split by job (assumptions, proof sketch, result, scope); Appendix XII's paragraph is split at "Read down the signal-class column." No math changed.
- Length is unchanged (13,997 words before and after across the twelve files); the IEEE PDF stays at 22 pages.

## Author flags (nothing below was changed)

Claims and strength:
1. **Conclusion coda** (X, last paragraph): "Reliability comes from governing that specialization" states without condition what IX-A calls a hypothesis the survey does not test. Restore "on that hypothesis" or keep (D12).
2. **X, open problem 3**: "The neighboring reward literature also reports no human-agreement result..." is wider than VII-A's "Among the co-evolving methods reviewed".
3. **VI-B**: "the production-viable pairing rather than a compromise" rests on a few vendor descriptions.
4. **VII, closing**: "largely unmitigated because no surveyed system runs them together" is a causal claim.
5. **Cold reader's reviewer objections**: the single rater and the public-documentation scope are stated in III but not in the abstract; the feedback classes are assigned "by the constraint that binds first" and then said to "predict" placements; the research lines "converge" on the authors' five-condition reading; "Eleven surveyed skill systems" has no stated denominator.

Numbers and consistency:
6. **III**: "the eight systems without an audit": the audit leaves 2 of 204 core systems out, so the reader cannot tell where the other six come from (S4.2.1 names the eight).
7. **V-A**: "Two problems remain" introduces attribution plus two side effects of cheap acceptance (overfitting, pool growth); the re-draft groups the latter two, so confirm "Two" or change it.
8. **IV-D**: averaging "reduces the variance of their mean by a factor of $1/k$" (the variance falls by a factor of $k$); which of SAGE-gate, VaG, and AutoSaddler averages and which requires agreement is not stated.
9. **SkillOpt**: "one markdown skill document" (IV-E) vs "the shared skill bank" (IV, last paragraph).
10. **X**: the conclusion lists four components of governed promotion; VIII and the abstract list five.
11. **III**: "contrast set" and "contrast corpus" may name two different sets; III's "human local gate holds only curation and registries" vs IV's registries "have no local gate".

Math and terms:
12. **II-C**: $\pi$, $x$, $\lambda$ are not defined; "improving edits eventually stop clearing the gate" reads as if good edits are rejected.
13. **Appendix XI**: "the gate's margin" names $\gamma_t+\tau_t$, while II defines the margin as $\tau_t$; "high-frequency or high-severity modes are proposed first" is an assumption stated as a consequence; "the gate checks that future behavior improves".
14. **Appendix XII**: "inherit its descent guarantee" and "the correct analogue" are stronger than Appendix XI's one-step inequality supports.
15. **Heading vs term**: the II subsection heading says "artifact-layer optimization" while the defined term is "artifact-layer descent" (the abstract keeps "optimization").

Citations (no key was added or moved between files):
16. Sentences without an in-sentence citation: V-B (poisoned channels), V-C (review of Anthropic's skills repository), VI-B (AlphaEvolve gains used within Google), VI-B (AutoManual, Letta), VI-C (EDDOps), VII-B (path-dependent trajectory evaluations), IX-A ("persistent artifacts offer the cheaper path").
17. The scaffold definition attributed to [@zaharia2024compound] (I ¶2) and IV's "An evaluation of harness optimizers reaches the same conclusion" [@ong2026harnesseval] should be checked against the sources; the wording of both attributions is unchanged.
18. VII's "major agent frameworks": confirm "major" is the source's word.

Structure (proposals, not applied):
19. D8: the P4 reviewer's reorder (V before IV, VII after IV, IX folded into V).
20. D11: IX-A ("Why specialization remains outside the weights") and IX-B ("Relation to neighboring surveys") sit under "How the research lines fit together"; VII cites IX-A forward.
21. Section IV has five subsections (house limit four).

The full list (about 90 items, many minor) is in the S5 change logs inside the ledger file.

## Numbers

IEEE `main.pdf` 22 pages, 148 references, 10 tables, 4 figures; abstract 236 words; `check_revision.py` PASS (a, e, f; its (b) note on `92` and `102` is unchanged from HEAD), `verify_ieee.py` PASS, `check_cites.py` 148 = 148. arXiv v4 83 pages, 0 undefined references or citations, 180 keys = 180 bibitems. The ACL version was not touched in this round.
