# Revision log H: synthesis rewrite, promise and delivery (2026-10-08)

The author's reading of the post-review build: the information was there and the presentation failed. The abstract did not sell; II-C was unclear and its table chopped; III-D was good but shorthanded; the signal-class table was cramped; V-B read as a swamp; Section VI opened with no promise and VI-A was evidence pointers without a story; the tables hid structure behind references; Section VII was unmotivated; the whole should read as a synthesis of what is happening in the industry, every section serving one statement and every section opening as a promise its subsections keep. Decisions taken with the author: the measure-bound idea becomes part of the loop's definition; optimization versus evolution is stated conceptually, no experiment cited; Section VII stays and becomes the comparison; Tables 5, 6, and 8 lose their reference columns; Table 1 goes to three columns; Table 2 gets row spacing.

## The holistic statement

The industry has built, piece by piece, most of an optimizer for the layer around the model: the local loop is automated nearly everywhere, evidence is batched before acceptance, retirement is gated, lineage ships in products, formats and registries have converged, and the first federations of deployments exist. What it has not assembled is the governed second half, and the reason is structural: the feedback a deployment can get fixes the gate it can build, and only an exact signal carries its own measure to the place an edit arrives. The loop is an optimizer toward a measure, bounded by that measure, not an evolution toward an unknown better state.

## What changed, by section

- **Abstract.** Rewritten as the promise: the finding and its stakes first, then the loop, the signal rule, the trends, the missing half, and what the reader gets. 249 words.
- **I.** Paragraph 3 is now the synthesis in miniature: the six trends, the unassembled second half, the signal rule, the measure bound. Contribution 1 names the two implications of the conditions; contribution 3 is a synthesis, not a survey with scores.
- **II-C.** Rewritten in words (what the neighbors explain; the one question none asks). Table II-2 is three columns: Survey | Scope | How this survey differs, one sentence per row; the "This survey" row moved into the caption. Same nine keys plus Lin et al. named in prose.
- **III-D.** The coding-agent example traced through the three stages. Two new paragraphs: the measure bounds the lift (why Loop 2 cannot carry Loop 1's evidence; receiving-side evaluation as re-establishing the lift); the loop optimizes and does not evolve (a defined measure, a ceiling, gate stability, no convergence to one version, the reflexive gate as moving the destination).
- **IV.** C1 cell and paragraph: the lift is bounded and specific. "What the class decides": only the exact class carries its own measure to the receiver.
- **V.** Section promise sentence. V-B compressed to the inclusion rule, the two filters with counts, the audit with its denominator, and the weaker-than-thesis sentence; the sourcing detail stays in S2.
- **VI.** Rewritten as the synthesis. Intro promises three things. VI-A "Six things that changed": one paragraph per trend with an unpacked example (the local loop automated, with instruction files as the counter-example; evidence batched, with agreement versus averaging, moved from VII; retirement gated, with Ratchet's result as the reason; lineage shipped without correction; formats and registries converged; federations begun, with AlphaEvolve as the production proof). VI-B's five pieces each unpacked by a sentence. VI-C "Four ways the field builds it": Table VI-2 is Cluster | Which half is automated | What the cluster shows; systems moved into the paragraphs with one example each; the cluster sentence corrected (three clusters hold one half, the fourth both halves without governance).
- **VII.** "The four approaches side by side": opens by introducing the grid as the loop's two decisions on two axes; states its finding (the field varies almost only along the promotion-gate axis, and the signal class sets that gate; IV's three predictions confirmed); reads the empty cells and the lower rows; the seven-promoters bookkeeping is one sentence with its pointer. Figure caption shortened and made consistent with the figure's shading.
- **VIII.** Intro as promise. Table VIII-1 is Family | Started from | What it built | What it leaves open; systems moved into the families paragraph with one example each (Meta-Harness's candidate filesystem; FederatedSkill's server agent). Pointer to S5 added.
- **IX.** Promise sentence (an audit criterion and a prescription). The by-class paragraph picks up the measure bound.
- **X.** Intro as promise. Table X-1 is Failure | What goes wrong | Architectural response | Dominant class; the measured evidence and its sixteen citations moved into four prose paragraphs (bloat; poisoning and injection; evaluation fragility; coordination, overfitting, plasticity), each with its unpacked example.
- **XI.** The conclusion restates the holistic statement in the synthesis voice; the triad stays.

## Mechanics

`scripts/fix_tables.py` and `v4/postprocess_tex.py` insert `\addlinespace[2.5pt]` between body rows of every converted table. Keys moved from tables into prose: the nine survey keys stay in Table II-2; `palumbo2026spotify` from Table VI-2 into the production-hybrid paragraph; the sixteen measured-evidence keys of Table X-1 into the prose of Section X. Document-wide key set unchanged (148 body keys before and after; `check_revision.py` (a) PASS). Numbers relocated from tables to prose: CVE-2025-54136 (X); none else.

## Passes and gates

Register scan clean. Humanization pass by an Opus 5.5 agent on working copies of the ten rewritten files: 49 interventions, all reviewed in a word diff; adopted with three adjustments (AlphaEvolve sentence returned to its original framing; the cluster sentence corrected as above; "previous subsection" made "described above"). `style_invariants.py` PASS; `check_revision.py` PASS; `verify_ieee.py` PASS; `check_cites.py` cited = bibitems; arXiv build 0 undefined; every page rendered and inspected. The agent's per-entry change log follows.

---

# Humanization pass 2 (rewritten passages): change log

Snapshot compared against: `scratchpad/pre_hum2/`, which is byte-identical to the working copies before this pass. Running `style_invariants.py pre_hum2 hum_work2 hum_work2/abstract.md` reports PASS. Citation keys, numbers, REF tokens, table lines, raw-LaTeX blocks, display equations, headings, and caption lines are all unchanged, and all eight bold terms are present. The required V strings are present. The abstract is 249 words, down from 250. The paper has no em- or en-dashes. Every "(Supplementary Material S<n>)" pointer now ends a sentence; before this pass two did not (VII's S4 and X's S3). Sentence-initial "And" now appears twice in the whole paper, down from five.

The scope was the passages rewritten for synthesis, identified by diffing `pre_synth/` against `pre_hum2/`. Paragraphs that kept the first pass's texture were left alone.

Format: file | paragraph (first five words as they read now; "was:" gives the old opener where it changed) | code(s) | what changed.

## abstract.md

1. abstract | "Production AI now learns mostly" | 2a, T1, C2 | A colon now introduces the list of four feedback kinds after "receives". "An accepted edit improves only what that gate measured." is its own short sentence. The abstract drops from 250 to 249 words.

## I_III.md

2. I_III | "The disciplined alternative is one" | C3 | "Read together, the 256 systems..." becomes "Set side by side, the 256 systems...". This was the third "Read ..." opener in two paragraphs, and the tic recurs across the paper.
3. I_III | "The disciplined alternative is one" | C2, C3 | "Much of the second half exists in parts: the newer systems batch evidence...". The colon join removes one "The" opener.
4. I_III | "The disciplined alternative is one" | T1, T3, T8 | "...access control, and rollback. The reason is structural rather than a matter of effort." The unhedged claim now stands as its own short sentence.
5. I_III | "The disciplined alternative is one" | C3, T1 | "And an accepted edit ..., so a lift ..." becomes the periodic sentence "Because an accepted edit is an improvement only in what its gate measured, a lift earned in one deployment does not travel...". The logic is unchanged.
6. I_III | "3. A synthesis of 256" (contribution 3) | 2a | "against a published rubric and released, read as" becomes "against a published rubric, with the scores released, and read as". This unpacks the stacked participles. The item's order and content are unchanged.
7. I_III | "The neighboring surveys explain how" | 2a, C2 | The four-part question follows a colon. The Table II-2 pointer is now its own sentence.
8. I_III | "The neighboring surveys explain how" | C4 | "The persistent-state survey of Ding et al. finds" becomes "Ding et al.'s survey of persistent-state agents finds". The two neighbor citations no longer share one template.
9. I_III | "Three stages of scaffold maintenance" | C1 | "the file grows with every incident" becomes "the file sprawls with every incident".
10. I_III | "Three stages of scaffold maintenance" | T1, C2 | Second stage: "...and keeps the best. The suite is the only signal and no failure is traced to the rule that caused it; the winning variant has learned the suite as much as the task." This breaks the "X; A, B, and C" shape the second stage shared with the first. The At-the-first/second/third anaphora is kept.
11. I_III | "Two consequences of condition 1" | T1, T8, C2 | "Every loss has a scope." now stands alone. The next sentence pivots on a colon: "That is why Loop 2 cannot carry Loop 1's evidence: the receiving scope measures...".
12. I_III | "The second is that the" | T1 | "It needs ..., it descends ..., and at the ceiling ..." becomes "It needs ... and descends ...; at the ceiling ...". "It does not discover a better goal ..." and "Two scaffolds ... need not converge ..." are now separate sentences.
13. I_III | "The second is that the" | T5 | "what the gated systems in it actually do is descent".

## IV_feedback_signal_classes.md

14. IV | "**C1, exact.** A deterministic checker" | C3 | "And the improvement the check certifies is bounded" becomes "The improvement the check certifies is also bounded".
15. IV | "**What the class decides.** Read" | T1, C2 | The triple "only" chain is reworked: "...and only when the receiving side runs the same check: that is the one case in which the sending side's evidence means the same thing on arrival."

## V_method.md

16. V | "How the 256 systems were" (was: "This section says how the") | T4 | The section now opens on its subject, not on "This section says".
17. V | "A system enters the corpus" | 2a | The inclusion criterion and the sourcing statement, previously joined by a semicolon, are now two sentences. "(Supplementary Material S2)" still ends the sourcing sentence.
18. V | "A stricter composite two-loop audit" | 2a | "it admits 14 research systems, 13 table rows and SkillOpt, and 3 industry exemplars, Sierra ..." could be misread as a three-item list. It is now "it admits 14 research systems (13 table rows and SkillOpt) and 3 industry exemplars (Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories). Only these are placed in the design space."

## VI_findings.md

19. VI | "Two years of systems, read" | T4 | ", and this section takes them in turn" is removed. The First/Second/Third enumeration already does the signposting.
20. VI | "Two years of systems, read" | C2, C3 | "The shape the three make together is the gap ..., a first half ..." becomes "Between them, the three trace the gap the rest of the article is about: a first half that is routine, and a second half ...".
21. VI | "The local loop is automated" | T1 | A long sentence is split between the SAGE/COSPLAY clause and the SkillChain clause. The flat opener is unchanged.
22. VI | "Evidence is batched before an" | T2, C4 | The four-clause semicolon parallel is broken up. SAGE-gate and EvolveNet are joined with "and", and VaG becomes "In VaG, three heterogeneous critics must pass". Each citation stays with its system. The flat opener is unchanged.
23. VI | "Retirement is gated. Eleven skill" | 2a, T8 | The inference that trailed the citation (", which says that a pool nobody prunes...") is now its own sentence: "In other words, a pool nobody prunes starves the gate of signal before the loop can run (Section REF(sec:failure))."
24. VI | "Retirement is gated. Eleven skill" | T1 | "LLM-authored skills ... human-curated skills" becomes "skills written by a language model ... human-curated ones". VI no longer repeats X's Ratchet sentence word for word.
25. VI | "Formats and registries have converged." | 2a, T1 | The format-convergence fact and the hand-merge fact are split. The redundant "are merged by hand, every substantive edit human-authored and human-merged" becomes "In the public skill repositories, every substantive edit is human-authored and human-merged".
26. VI | "The first federations of deployments" | T2, C4 | In the third clause the rule becomes the subject ("a rule in XRepoSkill survives only if it is verified..."). The last clause becomes "..., then evaluates them there". The semicolon series is otherwise kept, so it does not copy the restructure in entry 22.
27. VI | "The first federations of deployments" | 2a | "AlphaEvolve is the production proof ..., an evaluator cascade paired with ..., as FunSearch did before it, with production gains at Google" becomes "AlphaEvolve pairs an evaluator cascade with an evolutionary archive, as FunSearch did before it; its production gains at Google make it the production proof that both gates can be algorithmic at once". The original attached the gains with "with". "Make it" states the same basis explicitly. Please review the wording.
28. VI | "*Research full-auto* systems show that" | C1 | "DGM is the plainest example" becomes "DGM is the textbook case". This also breaks the "plainest"/"plainly" echo with the next paragraph.
29. VI | "*Open standards and registries* hold" | T1, T8 | "...that the architecture is real. Adaptation is what the cluster lacks: its registries...". The second sentence pivots on a colon.

## VII_design_space.md

30. VII | "One thing jumps out of" (was: "Read the grid and one") | T5, C3 | "Read the grid and one thing stands out" becomes "One thing jumps out of the grid". This removes another "Read ..." opener.
31. VII | "One thing jumps out of" | 2a | "what distinguishes them is the column, which is what gates their promotion:" becomes "what tells them apart is the column, the gate on their promotion:".
32. VII | "One thing jumps out of" | C3 (fix target) | "The column is not a free design choice." becomes "Which column a system lands in is not a free design choice."
33. VII | "One thing jumps out of" | C3, C2 (fix target) | "The grid therefore says something the cluster table could not. The industry has converged..." is now one sentence joined by a colon. The paragraph's "The" openers drop from three to one, and the content is the same.
34. VII | "The empty cells and the" | C3 | "The human-gated row holds only curation, where" becomes "Only curation sits in the human-gated row, where".
35. VII | "The empty cells and the" | 2a, T1 | "(Supplementary Material S4)" moves from mid-sentence, before a colon, to the end of its sentence. The two bottom-row cells become their own sentence: "In [None × Auto] sit the governance-first platforms, ...; in [None × Human], the registries and community hubs ... [@...]". The citation group stays with the registries.
36. VII | "The empty cells and the" | C4 | "The five public skill repositories of one field study have the same shape in practice," becomes "One field study finds the same shape in practice: in its five public skill repositories every substantive edit is ...".
37. VII | "Adding the seven systems that" (was: "The seven systems that promote") | T7, C3 | The last two sentences are now a short closing paragraph, opening "Adding the seven systems...".

## VIII_families.md

38. VIII | "Five research lines, each started" | T8 | "and this section reads them as evidence" becomes "and we read them as evidence", which was the authors' phrasing before the synthesis rewrite. To keep a clear referent, "It says what each family..." becomes "This section says what each family...".
39. VIII | "The five families instantiate complementary" | 2a, C2 | "records which edit helped, which is the accumulated history" becomes "records which edit helped; that record is the accumulated history". The ambiguous "It is also the largest family in the corpus", which followed a Meta-Harness sentence, becomes "The family is also the largest in the corpus".
40. VIII | "The five families instantiate complementary" | C4, C3, T6 | The second "for instance" in the paragraph is removed: "FederatedSkill's server agent, for instance, applies" becomes "in FederatedSkill, a server agent applies". The citation group stays at the end of the sentence.

## IX_missing_architecture.md

41. IX | "What is missing is specific." | T4, 2a | The flat opener stands as its own sentence again. The appositive pair, which read as a four-item list, now uses parentheses: "an audit criterion (four properties ...) and a prescription (which of the four ..., given the feedback it has)".
42. IX | "Whether the architecture *should* be" | C3 | "And under every class the measure bound ... holds" becomes "Whatever the class, the measure bound ... holds". "Which is the usual case across organizations" becomes "as they usually do across organizations", because the preceding sentence already says "the usual case".

## X_failure_surface.md

43. X | "While the second loop is" | 2a, T1 | The roadmap clause ", and this section does three things with them: it names the seven, shows ..., and says ..." is replaced. That sentence now ends at the citation, and a new one follows: "There are seven, each shown below in a measured case and paired with the piece of the optimizer that would close it (Table REF(tab:X-1))."
44. X | "Bloat is not only slow;" | T1 | The instruction-scaling result and the Ratchet result are now separate sentences.
45. X | "Poisoning and injection are the" | C4 | "backdoors can be planted ... [@chen2024agentpoison]" becomes "AgentPoison shows that backdoors can be planted ...". The system name was confirmed against the title of chen2024agentpoison in references.bib, and the modality "can be planted" is kept.
46. X | "Evaluation fragility compounds because the" | C3 | "The response follows from those facts:" becomes "From those facts the response follows:". This breaks two consecutive "The ...:" sentences. The "It is optimized against. It is read non-independently. It goes stale" anaphora is untouched.
47. X | "The remaining three are the" | T1, 2a | "(Supplementary Material S3); the measure bounds the lift, so the response is ..." becomes "(Supplementary Material S3). Because the measure bounds the lift, the answer at promotion is evidence-radius discipline, with a held-out evaluation at the receiving side." The pointer now ends a sentence, and "the response is" no longer repeats across consecutive sentences. "And a scaffold that only grows ..." is kept as one of the two remaining sentence-initial "And"s, because it closes a group of three.

## XI_open_problems_conclusion.md

48. XI | "Seen whole, the corpus says" (was: "Read as one story, the") | C1, C3 | "Read as one story, ... one piece at a time" becomes "Seen whole, ... piecemeal". This removes the second "Read ..." opener in the paragraph and the paper's third "piece by piece / one piece at a time".
49. XI | "Seen whole, the corpus says" | T1 | The closing rule is now its own sentence: "Under every class the same rule holds: a lift travels only as far as its measure does." The triad paragraph that follows is untouched.

## Tried and reverted on read-aloud

- V, entry 18: the mechanism-level clause was also put in parentheses. That made three parentheticals in one sentence, so the clause went back to its original relative form.
- VI, entry 26: the first version of the federations paragraph used the same ", and" join plus a new sentence as entry 22. That repeated one template in two adjacent paragraphs, so a lighter variation replaced it.
- VI, entry 21: "SkillChain shows the local gate at its most careful: judge-approved edits re-enter..." made two colon sentences in a row. The original "with ... re-entering" construction is back; the sentence split is kept.
- VI, entry 20: "Together the three trace..." echoed "that together amount to" two sentences earlier, so it became "Between them".
- VI, entry 27: "and with its production gains at Google it is the production proof" read clumsily and was replaced by the semicolon version.
- VII, entry 34: "Only curation sits in the human-gated row: an agent drafts..." put a third colon in the paragraph and was changed back to "where".
- VIII, entry 39: "records which edit helped: the accumulated history..." put two colon sentences back to back and was changed to a semicolon.
- I_III, entry 12: "need not even converge" was considered and dropped, because "even" adds emphasis to a hedged claim.

## Counts by code (an entry with several codes counts under each)

T1 16 | 2a 14 | C3 14 | C2 9 | C4 6 | T8 5 | T4 3 | C1 3 | T2 2 | T5 2 | T3 1 | T6 1 | T7 1 | B1 0 | B2 0 | B3 0

There are 49 entries across 10 files. The rewritten passages total about 6,000 words.

Where a target was not met by a new change, the passage already met it:
- T3 (one per section): hedging in the rewritten passages is already uneven. Some findings are flat ("All four promote inside one operator."; "Registries govern what may be used, not whether it works."). The scope sits mid-sentence in "in the one controlled study". VIII qualifies at the end ("only that the same constraints keep producing the same shape"), and XI qualifies mid-sentence ("as far as public evidence shows"). Adding or moving more hedges would risk the hedge invariant.
- T7 (one per section): compressed paragraphs already exist in I-III ("The survey runs no experiments."), IV ("The classes are a partition"), VI ("The last piece is the thesis"), X (the closing two sentences), and XI (the triad). VII had none and now has one (entry 37).
- T5 (two or three): this pass adds two. The first pass's four ("without ever writing it down", "buy nothing in task success", "it turns out", "Bloat is not only slow") all survive in the paper.
- C1 (two or three): this pass adds three: sprawls, textbook, piecemeal. The first pass's "stubborn" (IV), "tidy" (IX), and "messy" (X) remain, along with the original "brittle" (III-A). Adding more would read as inconsistent.
- The deliberate parallels the caller listed are kept byte-for-byte: the Section IV four-scaffold opener, the At-the-first/second/third stages, X's "It is optimized against..." anaphora, the six flat trend openers in VI-A, and the XI triad.

## Flagged, not changed

1. VI_findings.md, VI-C intro: "Each has one half of the loop; none has both halves governed." Table VI-2's first row says the research full-auto cluster automates "Both, under algorithmic gates", and the next paragraph agrees. A reader may see a contradiction. Rewording it, for example to "Each governs at most one half of the loop", would change a claim, so this is the author's call.
2. VI_findings.md, VI-C, *Research full-auto*: "The federations of the previous subsection belong here too." The federations are described in VI-A, two subsections back. VI-B mentions them only in passing ("The four federations above"). "described above" would be safer, but this is reference wording, so it is left for the author.
3. VIII_families.md, "The five families instantiate complementary": the paragraph still narrates Table VIII-1 family by family, in table order (B1 mirror). The rewrite added more detail per family. Breaking the mirror would mean dropping or merging per-family claims and their citation groups. This was also flagged in the first pass.
4. VI_findings.md, VI-C: the four cluster paragraphs follow Table VI-2 row by row, in order (B1). This is a parallel taxonomy; reordering or merging would move claims away from their citation groups.
5. Repeated claims with identical citations across sections. The Ratchet result appears in VI ("Retirement is gated") and X ("Bloat"), both citing @zhang2026ratchet; the VI wording is now varied (entry 24). The eleven-systems retirement claim with the same four-key group appears in VI-A and VIII. The SkillForge "more than nine times in ten" judge appears in IV and VI-C. Removing any of these would remove a citation group.
6. "most research systems and a growing number of production ones/systems" appears almost verbatim in the Introduction (paragraph 3), III-A, and XI paragraph 2. Varying it would risk changing a count into a proportion. This is unchanged from the first pass's flag.
7. "Read ..." openers remain in passages outside this pass's scope: I_III paragraph 2 ("Read one at a time ... Read together", a deliberate contrast), IV ("Read down the table"), VIII ("Read against the loop"), and XI ("Read by signal class"). This pass removed three of them. The remaining ones are spread out but still noticeable on a full read.
