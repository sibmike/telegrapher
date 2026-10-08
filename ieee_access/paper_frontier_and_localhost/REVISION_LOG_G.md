# Revision log G: style pass and humanization pass (2026-10-08)

Run after the review response (log F) and before the manuscript goes to human readers, as the house process requires: the Telegrapher style guide first (what is said and in what order), then its final-pass checklist (how it reads aloud). Scope: the abstract, Sections I to XI, and Appendices A and B. Supplementary S2 to S7 were not touched in this pass.

## Gate

`style_invariants.py` (session scratch) compared the pre-pass snapshot with the result file by file: citation-key multiset, number multiset, REF tokens, table lines, raw LaTeX blocks, display equations, headings, caption lines, the bold definition terms, the sentences `verify_ieee.py` greps for, and the abstract's word count. PASS on both passes. `scripts/check_revision.py` PASS; `verify_ieee.py` PASS; `check_cites.py` cited = bibitems; both packages rebuilt and the IEEE pages rendered and inspected.

## Pass 1: style guide (done by hand)

A register scan found no product-sheet verbs, no enthusiasm adverbs, and no bridge sentences. Density fixes, all wording only:

- II-B: the two prior-paper descriptions were one stacked sentence each; now two or three beats each, same claims, same scope statements.
- III-C: the convergence pointer sentence split in two.
- IV, "What the class decides": the first consequence unpacked into four sentences ("Promotion is stricter." as the pivot).
- V-B: the corpus walk split into two paragraphs at the composite audit.
- VI-A: the three-substrate tour split into three paragraphs (instructions, skills, orchestration).
- VIII: the four conclusions restored as a numbered list (intentional structure the story-first pass had flattened).

## Pass 2: humanization (Opus 5.5 on working copies; every change reviewed in a word diff before adoption)

61 interventions across 12 files; the per-entry change log follows. Register shifts: "without ever writing it down" (III), "buy nothing in task success" (VI), "the rest, it turns out, are stabilizers" (VIII), "Bloat is not only slow" (X). Vocabulary: "stubborn" (IV), "tidy" (IX), "lopsided" (XI). Attribution added in running text where the citation was impersonal (Zaharia et al., Shankar et al., Sculley et al., GPTSwarm, AFlow, EvolveNet, VaG, AutoSaddler), each checked against `references.bib`. Flagged and left: the family-by-family paragraph of VIII mirrors Table VIII-1 by design; the gated-retirement claim appears with the same four keys in VI and VIII; "most research systems and a growing number of production ones" recurs three times as a count, not a proportion; "catalogue" and "analogue" are the series' spellings and stay.

---

# Humanization pass: change log

Snapshot compared against: `scratchpad/pre_hum/`. `style_invariants.py pre_hum hum_work hum_work/abstract.md` reports PASS: citation keys, numbers, REF tokens, table lines, raw-LaTeX blocks, display equations, headings, and caption lines are all unchanged. The abstract is 248 words. No em-dashes were added. Every required string and bold term is present.

Format: file | paragraph (first five words) | code(s) | what changed. Where an entry carries two codes, the first is the primary one.

## abstract.md

1. abstract.md | "Production systems built on large" | C2, T1 | "...rather than patchwork. The decisive one..." is now joined with a semicolon. This breaks the pair of "The" openings and leaves the word count unchanged.

## I_III.md

2. I_III.md | "Read one at a time," | C4 | "what has been called a compound AI system" becomes "what Zaharia et al. call a compound AI system". The citation group stays in place.
3. I_III.md | "The disciplined alternative is one" | C3, C2 | Breaks the run of five "The" openings (the fix target): "Its first half ...; the second decides how far the edit may travel...". The two half-descriptions are now joined with a semicolon.
4. I_III.md | "The disciplined alternative is one" | T8, C3 | "The second half, governed by ..., appears in none of the 256 systems surveyed" becomes the flat declarative "None of the 256 systems surveyed has a second half governed by versioned lineage, access control, and rollback."
5. I_III.md | "Production reliability is won in" | T1, T3 | "In principle, per-customer adapters ... could absorb some of the residual..." is followed by the short flat sentence "In practice they are rare." The hedge "could" is unchanged; the leading marker pairs with the flat sentence.
6. I_III.md | "The case for learning outside" | 2a | "Its evidence is twofold:" now announces the count. The semicolon chain is split, and "The argument stops where..." is its own sentence.
7. I_III.md | "The case for learning outside" | T1, C3 | The condition is front-loaded: "For a deployment that operates inside a bounded slice ..., *The Architecture of Errors* [@...] argues that those decisions fail...".
8. I_III.md | "The case for learning outside" | C2, T8 | Colon pivot: "The paper's own negative result marks the limit: no finite catalogue covers an unbounded domain."
9. I_III.md | "A reader will expect the" | C4, C3 | "Agentic context engineering [@ace2025agentic] does persist its artifact, an evolving playbook, but keeps it inside one context...". The system is now the subject, with an emphatic "does".
10. I_III.md | "Loop 2 is the step" | C3 | "The same rule" becomes "That same rule", which breaks a run of three "The" openings.
11. I_III.md | "The scopes nest (Fig. REF(fig:scope))." | T1 | "and we call it cross-tenant promotion" becomes "which is what cross-tenant promotion means here". This avoids two consecutive "we call" sentences.
12. I_III.md | "The scopes nest (Fig. REF(fig:scope))." | 2a | The appositive glosses for step and target move into parentheses: "Loop 1 sets the step (how much ...) and Loop 2 sets the target (which average failure rate ...)".
13. I_III.md | "Written out, the patch loss" | T5 | "without writing it" becomes "without ever writing it down".
14. I_III.md | "Each half of the loop" | 2a | "Who writes the candidate is recorded separately and is not a gate: the author may be an agent ..., an engineer ..., or a contributor ...". The main clause now comes before the list.
15. I_III.md | "Three stages of scaffold maintenance" | T1 | The third-stage sentence is split ("Its dominant failure becomes evaluation fragility..."). The At-the-first/second/third anaphora is kept.
16. I_III.md | "Three stages of scaffold maintenance" | 2a | "then promote in one of two ways: behind a human gate, ..., or, in Letta's Context Repositories alone, by an ungated push...". The count is announced, and "in one case" is now named.

## IV_feedback_signal_classes.md

17. IV | "That difference is the whole" | T1, C2, T8 | "The gate needs an estimate of one quantity: whether the edit lowered the patch loss. That estimate comes from a feedback signal." The sentence now pivots on a colon and is split.
18. IV | "**C1, exact.** A deterministic checker" | T1 | Periodic sentence: "Because the check is exact ..., one run settles the checked case."
19. IV | "**C2, observable outcome.** The environment" | B2 (class-paragraph analogue), 2a | The predicate comes first: "Gates of this class include Devin's ... [@...], SAGE's ... [@...], SkillRL's ... [@...], and PACE's ... [@...]". Each citation stays attached to its system.
20. IV | "**C2, observable outcome.** The environment" | 2a | The gate examples move into parentheses: "(a reinforcement-learning threshold or a held-out task suite)".
21. IV | "**C2, observable outcome.** The environment" | C1 | "takes its hardest form" becomes "takes its most stubborn form here".
22. IV | "**C3, judged.** There is no" | T1 | A two-idea sentence is split: "Residuals, meanwhile, are captured only when someone objects...".
23. IV | "**C3, judged.** There is no" | C4, C2, T8 | "Nor is a human judge stable: Shankar et al. find that evaluators' criteria drift... [@shankar2024validators]". The author is named and the sentence now turns on a colon instead of a semicolon.
24. IV | "**C4, delayed and sparse.** The" | T1 | The concession comes first: "AlphaEvolve's evolutionary database can look like an instance, and is not one:".
25. IV | "**The judge is part of" | 2a | "has forced the construction of judged gates" becomes "has forced researchers to build judged gates".
26. IV | "**What the class decides.** Read" | T4 | The pointer to Section REF(sec:design) moves into the opening sentence ("three consequences follow, each a prediction about the corpus that Section REF(sec:design) checks"). The section now ends on the third consequence instead of a forward bridge.
27. IV | "**What the class decides.** Read" | T1 | The semicolon triple is split: "A judgment can do so only once the judge is calibrated, and a delayed reward cannot gate edits one at a time." This avoids a verbatim echo of the Introduction.

## V_method.md

28. V | "A deployment's scaffold is composed" | T1, C2, T8 | The last sentence is split: "This partition is the one that recurs in practice: every integrated system ...".
29. V | "The corpus holds systems that" (now "A system enters the corpus") | 2a | The inclusion criterion is restated as "A system enters the corpus on either of these grounds: it wraps ..., or it is described in public as ...". The source window is now its own sentence ("All systems were found in ..."), and "It was assembled" becomes "The corpus was assembled" so the referent is clear.
30. V | "A stricter composite two-loop audit" | 2a | The clause chain about the mechanism-level group of ten is split into two sentences ("Those ten were classified ...; they are not rows of it, and the corpus counts above exclude them").
31. V | "A stricter composite two-loop audit" | 2a | "The audit admits 14 research systems and 3 industry exemplars. Of the research systems, 13 are rows ... and the fourteenth, SkillOpt, comes from the mechanism-level group; the industry exemplars are ...".
32. V | "Every classification rests on public" | 2a, T1 | The relaxations move into a parenthetical "(for instance, ...)", followed by "The counts do move ...; the qualitative findings survive every one of them". This puts the concession before the flat claim.

## VI_findings.md

33. VI | "The corpus answers the question" | T4 | The roadmap sentence "This section gives the evidence in three cuts." is removed. It is now "The evidence comes in three cuts: per substrate, ...".
34. VI | "On the three substrates that" | T5 | "without raising task success" becomes "and buy nothing in task success".
35. VI | "On orchestration, automated workflow search" | C4, 2a | "GPTSwarm's optimizable agent graphs [@zhuge2024gptswarm] and AFlow's tree search ... [@zhang2024aflow]" now name their systems. The one-sentence paragraph is split in two.
36. VI | "Tools and governance hold the" | 2a | The catalogue and control-plane features move into parentheses.
37. VI | "*Production hybrid* systems show that" | T1 | "In every member, a person on Loop 2 stands in for the exact signal the cluster lacks." This avoids repeating the Section IV phrase word for word.
38. VI | "*Open standards and registries* converge" | T1, T8 | "Adaptation is what the cluster lacks:" breaks the parallel with "What every member lacks is governance:".

## VII_design_space.md

39. VII | "[Auto × Auto] holds the" | C3, T1 | The third "[X × Y] holds" opener becomes "The governance-first platforms sit in [None × Auto]: they gate promotion ..., so they pass only the Loop-2 half ...".
40. VII | "The occupancy bears out the" | C3 | "And no system in the matrix calibrates..." becomes "Nor does any system in the matrix calibrate...". This keeps "And" openers at two in the whole paper.
41. VII | "Two further patterns cut across" | T1 | The contrast is front-loaded: "Earlier systems accepted an edit on one evaluation ...; the newer ones batch evidence before acceptance."
42. VII | "Two further patterns cut across" | C4, T2 | The four parallel clauses are varied. EvolveNet, VaG, and AutoSaddler become subjects, named as the paper names them elsewhere (Sections VI and IX, Appendix B). The citation groups do not move.

## VIII_families.md

43. VIII | "The clearest single instance is" | T1 | The transfer clause becomes its own sentence: "It also reports transfer across models, harnesses, and benchmarks, ...".
44. VIII | "The clearest single instance is" | T5, T8 | "So the gate and a consensus form of credit assignment are load-bearing; the rest, it turns out, are stabilizers."
45. VIII | "The five families instantiate complementary" | C2, T1 | "it is also the largest family in the corpus: roughly two hundred papers cite its founding entries, and a dozen are scored here".
46. VIII | "Read against the loop, the" (list item 2) | 2a | A colon now introduces the step ("...trial-and-error: attributing a system-level failure to one scaffold coordinate."), and "That step remains unsolved..." is its own sentence. The item and its order are unchanged.

## IX_missing_architecture.md

47. IX | "Row by row, the partition" | C1 | "plain" becomes "tidy".
48. IX | "In machine-learning terms, what is" | C2, T8 | Colon pivot: "Loop 2 is selection and merge: the nearest systems aggregate program edits with a language model, not by averaging."
49. IX | "Whether the architecture *should* be" | T1 | The fourth "Where it is ..." becomes "With a delayed signal, property (a) cannot be met; what remains ...". This breaks the four-fold anaphora once.

## X_failure_surface.md

50. X | "Until the governed second loop" | C4 | "the technical-debt ledger that Sculley et al. opened for machine-learning systems a decade ago [@sculley2015debt]".
51. X | "Bloat is a signal-quality problem" | T5, T8 | "Bloat is not only slow; it is a signal-quality problem."
52. X | "Bloat is a signal-quality problem" | B3, C2 | The case comes first: "Ratchet reports what that looks like: LLM-authored skills gain nothing ..., human-curated ones show a double-digit gain, and the authors attribute the gap to lifecycle management". The verb stays "reports".
(The "It is optimized against. It is read non-independently... It goes stale" anaphora is kept unchanged.)

## XI_open_problems_conclusion.md

53. XI | "The field has built an" | T3 | The same hedge moves mid-sentence: "but not, as far as public evidence shows, the optimizer that should govern it". This also stops it echoing the Introduction's wording.
54. XI | "The field has built an" | C3 | "The two earlier papers" becomes "Both earlier papers", which breaks the run of three "The" openings (the fix target).
55. XI | "The field has built an" | T1, T8 | "The corpus is consistent with that hypothesis." now stands alone. It is followed by "If it holds, the gated and scoped artifact layer is not a workaround but the architecture the error structure calls for."
56. XI | "The survey shows how far" | C1 | "the distance is uneven" becomes "the progress is lopsided".
57. XI | "The survey shows how far" | C3 | "The signal-class analysis says this is not one gap but four" becomes "Read by signal class, this is not one gap but four". This removes the third "The" before the triad.
58. XI | "The frontier model generalizes. The" | T7 | The triad and the closing sentence now form their own short final paragraph. The triad is word-for-word unchanged.

## appA_formal.md (Setup, Descent inequality, Convergence untouched)

59. appA | "Table REF(tab:A-1) pairs each" | T1 | Correspondence: the semicolon is split into two sentences. This is a rhythm change only.
60. appA | "*Pitch review.* The system repeatedly" | C3, T1 | The five "The" openings become two joined clauses plus "What the edit changed was the gate that will judge the next edit:". This is a rhythm change only, and the quoted rubric strings are byte-identical.

## appB_gates.md

61. appB | "The first five families populate" | T3 | The same qualifier moves mid-sentence: "and, under the assumptions of Appendix REF(app:formal), inherit its descent guarantee."

## Tried and reverted on read-aloud

- I_III intro paragraph 3, last sentence: an inverted passive ("Which half of the loop a deployment can close is decided by the class of its signal.") read stiffly, and the "The" run was already broken. It is reverted to the original.
- XI paragraph 2: fronting "In most research systems and in a growing number of production ones" made the prepositional phrase seem to cover all four semicolon clauses, which would be a scope change. It is reverted.
- X Ratchet: "Ratchet shows the effect plainly" would have strengthened the attribution from "reports" to "shows". It is reverted to "reports".

## Counts by code (an entry with two or three codes counts under each)

T1 22 | 2a 14 | C3 10 | T8 10 | C2 9 | C4 6 | T5 4 | T3 3 | C1 3 | T4 2 | T7 1 | T2 1 | B2 1 | B3 1 | B1 0 | T6 0

That is 61 entries across 12 files.

Several sections already met the T4, T7, T3, and T6 targets before this pass, so no new change was added there:
- T4: IX opens on "What is missing is specific."; VI-A, VII, and VIII open on a number or concrete claim; III ends on the Letta fact.
- T7: compressed paragraphs already exist in IV ("The classes are a partition"), VI ("The last piece is the thesis"), VII ("Seven systems promote"), IX ("The closest approaches split"), and X (closing paragraph).
- T6: examples are already introduced in several ways (example-first in IV and III-A, "Suppose" in IV, case-first in Appendix A).

## Flagged, not changed

1. VIII_families.md, "The five families instantiate complementary parts of the loop ..." narrates Table VIII-1 family by family, in table order (B1 mirror). Breaking the mirror would mean dropping or merging per-family claims and their citation groups, which violates the claim and citation invariants.
2. VI_findings.md "Eleven skill systems treat retirement as a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay]" and VIII_families.md "eleven systems make retirement a gated operation [same four keys]" state the same claim with an identical citation group in two sections. Trimming one would remove a citation group.
3. "most research systems and a growing number of production ones/systems" appears almost word for word in Introduction paragraph 3, III-A ("Then it measures."), and XI paragraph 2. Varying it (for example, "a growing share") would change the claim, from a count to a proportion, so all three are left as they are.
4. Spelling: "catalogue/catalogues" (abstract, II-B, VI, X, XI) and "analogue/analogues" (VIII, Appendices A and B, including the Table A-1 header row) are British-leaning forms. US usage would be "catalog/analog". They are left unchanged: "catalogue" is the series' established term, the Table A-1 header line must stay byte-identical, and changing only the prose would make the paper inconsistent. This is the author's call.
5. IV "**What the class decides.**", second consequence: "where the person on Loop 2 does the work the missing exact signal cannot". It is kept because it is the source phrasing; the verbatim echo in VI (entry 37) was varied instead. No invariant issue; noted for awareness.
