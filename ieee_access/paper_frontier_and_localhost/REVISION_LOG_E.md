# Revision log E: story-first rewrite (2026-10-07)

Author's verdict on the previous build: Tables 1 and 4 overcrowded, Table 2 better as a paragraph, Figures 1 and 2 hard to read, Section IV must be understandable on the first read, Sections V and VI read as evidence without a thesis, and the rest sacrificed story for evidence. This pass rewrites the body as a structured essay: every section opens with the sentence that advances the argument, and the evidence serves that sentence. No evidence added; the document-wide citation key set is unchanged (`scripts/check_revision.py` (a) PASS); every number that left the prose lives in a table, caption, or appendix ((b) 0 unaccounted).

## Spine

Deployed AI learns by editing the scaffold around the model, not the model. Done right, that editing is one loop with two halves: Loop 1 fixes a recurring failure locally under a gate; Loop 2 decides how far the fix may travel. The first half is routine; the governed second half has not been built; the feedback-signal class decides which half a deployment can close. Stated in the abstract, Introduction ¶3, the opening of Section VI, Section IX, and the conclusion.

## Section by section

- **I.** ¶3 now states the two halves, the finding, and the signal rule in plain words. Contributions carry their section pointers; the separate roadmap sentence is gone.
- **II-C.** Table 1 (related surveys) reduced from seven columns to four: the four yes/partial/no columns became one text column, "Of the four axes here". Ding et al.'s verdict moved into the opening paragraph; the prompt-optimization and nearest-precedent paragraphs merged.
- **III.** Loop 1 and Loop 2 named in the first paragraph. Figure 1 redrawn as Loop 1 alone (six stations, one idea each, with the return path and a hand-off box to Fig. 2). Figure 2 redrawn as a ladder of the five scopes with a gate per rung, the evidence radius as a dashed line, and the cross-tenant rung marked. The three-stages table (old Table 2) became the paragraph "From patchwork to descent".
- **IV.** New second paragraph states the principle (the gate needs one estimate; signals differ in timing, exactness, and whether there is a fact of the matter). Table (old Table 3, seven columns) reduced to five: signal, what the gate can be, what stays hard, examples; the conditions column and the gate-pairs column became prose. Each class paragraph follows one pattern: signal, examples, what the gate can be, what stays hard, dominant failure. The reflexive gate has its own paragraph, with the weight-side comparison folded into it. "What the class decides" replaces the three predictions with three plain consequences, which Section VII then confirms.
- **V.** Opens with why the corpus was scored. Table (old Table 4) reduced to short cells. V-B now says in one sentence that passing the composite audit is weaker than having the governed second loop (every passing system promotes inside one operator), which closes the gap a first-time reader fell into between the 17 audit passers and the thesis. The mechanism-level note is one sentence.
- **VI.** Retitled "What the field has built"; opens with the one-sentence answer and names the three cuts. VI-A retitled by its finding; "judge-monotone" replaced with plain words. VI-B reordered to walk the second loop from failure capture to cross-organization promotion, with the thesis piece last and a closing sentence tying the four others to it. VI-C retitled "Four kinds of system, each with half the loop".
- **VII.** Opens with the one-sentence shape of the matrix. The seven-promoters sentence corrected (see below). The human-authored cells paragraph states the Loop 1 convention up front. The predictions paragraph refers to the three consequences of Section IV.
- **VIII.** Retitled "Five research families converge on the loop"; the four conclusions are prose, not a numbered list.
- **IX, X.** Opening sentences tied to the spine ("What is missing is specific"; "Until the governed second loop exists").

## Correction against the data

The previous text said seven systems promote across contexts "without versioning or lineage" and that six "would enter the matrix if any of versioning, lineage, or rollback counted as Loop-2 governance", which is self-contradictory. Against `p3_refresh_2026-10.csv` (gov_props), only EvolveNet carries rollback (and so enters under the governance relaxation as defined); Evo2Team, XRepoSkill, ShareMem, RASO, and Spotify carry none of the three and enter only if the governance requirement is dropped altogether; Future AGI is T5-only. Section VII, S2, S4, and S6.7 now say so, and `CLAIMS_AUDIT.md` carries a dated correction note.

## Build

IEEE: 19 pages, 4 figures, 10 tables, 147 references; `verify_ieee.py` PASS (table count updated to 10), `check_cites.py` 147 = 147, `check_revision.py` PASS. Every page rendered and inspected. arXiv v4 rebuilt from the same sections.
