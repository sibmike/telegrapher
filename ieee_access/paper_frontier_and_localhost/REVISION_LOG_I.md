# Revision log I: the loading pass (2026-10-08, evening)

The author's verdict on the synthesis build (`e6d7e07`): the contributions list was "a table of contents, and even as a table of contents boring"; the Section VI opener was watery; and the standard for the whole paper is that every sentence adds value and compounds the story, with no sentence that merely announces, routes, or restates. Decisions already taken in conversation and applied here: the abstract the author rated "Better" (stakes before the finding; the earlier-papers clause dropped from the abstract, the three-paper argument stays load-bearing in II-B and the conclusion); a new Introduction that defines "scaffold" in its first paragraph, puts the stakes before the question, shows the coding-agent example before naming the loop, and ends without a numbered contributions list.

## The rule applied

A sentence stays if a reader who already has the previous sentence learns something from it. Sentences that only say what a section will do, that enumerate what follows, that bridge to the next subsection, or that restate the paragraph were rewritten to carry a claim or cut. Promises are kept where a section opens, but each promise is itself a claim about the corpus, not a list of what the subsections contain.

## What changed

- **Abstract** (249 words). Opens on the phenomenon and its speed ("the system changes within the hour; the weights change on a cycle of months"), states the finding, the loop, the stakes ("every customer relearns the same fixes and nobody can say which rule helped"), the structural reason, and closes on what the survey gives the reader as tools rather than as a list of sections. "256 production and research systems" kept for `verify_ieee.py`. The clause about the two earlier papers is gone from the abstract; II-B and the conclusion carry it.
- **I, paragraph 1.** "We call that fast-changing layer around a slow-changing model the scaffold": the paper's central term is now introduced where it first appears.
- **I, paragraph 2.** The patchwork picture, with its cost, comes before the question; the answer follows in one sentence.
- **I, paragraph 3.** The loop is shown on the coding agent that keeps misnaming a class (traced, one edit, kept only if the repository's own failure rate falls; then promoted to a team template, the company's core instructions, or a cross-company registry) before it is named; the five conditions and the two consequences of the measurable loss follow.
- **I, paragraph 4.** The corpus story in plain words (the first half routine; the second in parts, each part named in words rather than in the paper's own labels; none assembled; the structural reason; the measure bound applied to transfer).
- **I, paragraph 5.** Replaces the five-item contributions list. One paragraph in which each section pointer carries the claim it defends or the use the reader gets from it (the five conditions a team can check its own maintenance against; the rule that says which half a deployment may automate today; the corpus found converged on the first half and sorted on the second as the feedback predicts; five research lines arriving at one loop; the four properties, the measured failures, the piece to build next per class). The no-experiments sentence and the practitioner/researcher routing sentence close it. Openers vary (What follows / Section III / The rule / For the half / The survey / A practitioner).
- **IV.** "One feature of the judged class deserves its own paragraph" replaced by the feature itself: the judged class has one feature the other three lack, and it is the rubric being a scaffold coordinate.
- **V.** The opener now states why the section exists as a claim ("Every claim in Section VI rests on a released table") rather than "is set out here".
- **VI, intro.** Rewritten from an enumeration ("show three things. First... Second... Third...") into the finding: the industry has built most of an optimizer one piece at a time; the six pieces named in words; what is missing is narrower than the vocabulary of evolution suggests and sits entirely on the promotion side; the four kinds of system divide the loop between them, which is how a routine first half coexists with an unassembled second half.
- **VI-A, closing paragraph.** The bridge ("the shape the next two subsections unpack") replaced by the reason the split exists: each kind of system was built to satisfy one constraint and matured only the substrates that constraint touches, which is why the missing pieces sort by feedback class and every cluster holds part of the loop.
- **VI-A, retirement paragraph.** "In other words" dropped; the sentence it introduced stands on its own.
- **VII, intro.** "It shows which combinations the field has built, which it has not" replaced by the question the grid answers that the cluster table cannot: whether the unbuilt combinations are missing by accident or by the rule of Section IV.
- **VIII, intro.** The "This section says what each family started from..." sentence cut; in its place, what each of the five lines arrived at (reflection over failures; the generalization penalty; credit assignment; gated retirement; the receiving-side check) and that none set out to build an optimizer for the scaffold. The convergence caveat kept.
- **IX, intro.** "This section turns it into two things a reader can use" replaced by the claims themselves: four properties define it, no surveyed system holds all four, and which of them a deployment should expect to meet follows from its feedback rather than its domain. The closing summary sentence ("Naming the four properties turns a vague gap into an audit criterion...") cut; the section now ends on the measure bound.
- **X, closing.** "The failure surface is real... Every row names a piece..." replaced by the claim that none of the seven needs a new mechanism, every response is a piece of the second loop or its governance, and the surface stays largely unmitigated in production because no surveyed system runs those pieces together. The audited phrase "largely unmitigated in production" (CLAIMS_AUDIT row 266; S6) is retained verbatim.
- **XI, opener.** "Five open problems follow from the survey, one per class and one for the architecture" replaced by: each class leaves one problem open and the architecture a fifth; none is a general agenda, each is the specific step its class is blocked on.

Unchanged: II-A, II-B, II-C, III-A to III-D, the body of IV, V-A to V-C, VI-A trends and VI-B and VI-C, the body of VII, VIII, IX, X, the open problems and conclusion of XI, both appendices, all tables, figures, captions, and the supplementary files.

## Gates

`check_revision.py` PASS (a, e, f); (b) 0 numbers unaccounted; (c) 0 hits; (d) every label defined before use. `style_invariants.py` against `scratchpad/pre_load/`: the only differences are one fewer "256" in I_III.md (four mentions became three) and one fewer in V_method.md (the opener), both relocations; "Of the 256 systems" stays in V-B. `verify_ieee.py` PASS: 21 pages, 4 figures, 10 tables, 148 references, abstract 249 words. `check_cites.py` cited = bibitems = 148. arXiv v4: 78 pages, 178 references, 0 undefined. Every page rendered and inspected; every float sits on the page after its first reference.

## Texture review

House rule: the style and humanization checks run before any human review. The style rules were applied in the loading pass itself (structure, threading, no bridges, clean section endings, mechanism voice, density discipline). The texture checklist was then run by an Opus 5.5 reviewer in review-only mode on the changed passages (diffed against `scratchpad/pre_load/`), at Light intensity, with the invariants fixed: no claim, number, key, REF token, bold term, table line, heading, or caption; no em-dashes; no bridges, pointers, hedges, or restatements; no softened declaratives. Its report is `scratchpad/texture_review_I.md`. Decisions:

Adopted (ten proposals, all Pass 2a, L2, L3, or R1):
- Abstract: "Its first half is routine" (four consecutive "The" openers broken); the four feedback classes now follow a colon and "An accepted edit improves only what that feedback measured" is its own sentence. In the same pass the abstract's dangling "its gate" became "the feedback that decides whether an edit is kept", "the half nobody has built" became "the half still unassembled" (it sat next to "exists in parts"), and "built most of an optimizer for it without assembling one" became "built most of its optimizer and never assembled it". 249 words.
- I, paragraph 3: the five-conditions sentence split before "The decisive one".
- I, paragraph 4: "Its first half is routine"; sentence-initial "And" dropped; the because-clause no longer repeats paragraph 3 word for word ("Because the lift an edit earns is bounded by what its gate measured, that lift reaches another deployment only if...").
- I, paragraph 5: "in the order the argument needs them" cut as watery; the long roadmap sentence split at its verb; "exactly as the feedback predicts" corrected to "exactly as the rule predicts"; the practitioner/researcher routing sentence cut because it repeated the section pointers two sentences earlier.
- IV: the reflexive-gate paragraph names the feature at the colon and puts "it returns in the findings and in the open problems" after it.
- V: "go straight there" became "skip ahead to the findings".
- VI, intro: "a second half whose parts all exist" contradicted "five pieces are still missing" two sentences earlier (reviewer's most important flag); now "a second half that exists in parts and has never been assembled".
- VI-A, closing paragraph: the constraint list reads "fast learning or safe change or portability"; the "which is why... and why" tail is its own sentence ("That is why...").
- VIII, intro: "None of them set out to build an optimizer for the scaffold" is its own sentence; the vendors' convergence is its own sentence; "shows no more than that:" became "shows only that".
- IX, intro: split after "no surveyed system holds all four".
- X, closing: the "and / because / so" chain split into three sentences; "largely unmitigated in production" kept verbatim.

Not adopted:
- "descends to that measure's ceiling" (loss descends, improvement has a ceiling): the author's own wording for the concept in III-D; left for the author.
- VI intro's six-clause sentence "repeats the six subsection lead sentences": that is the promise-and-delivery structure the author asked for; kept.
- "patchwork" contains the substring "patch": `check_revision.py` (d) matches the whole word and passes.

Gates after the texture decisions: `style_invariants.py` differs from `pre_load/` only in the two "256" relocations noted above; `check_revision.py` PASS; `verify_ieee.py` PASS (21 pages, 10 tables, 148 references, abstract 249 words); `check_cites.py` 148 = 148; arXiv v4 78 pages, 178 references, 0 undefined; every page re-rendered and inspected.
