# Revision log O: named loops and plain openings (2026-10-09)

The author's verdict on the previous state: "Loop 1" and "Loop 2" were used so often that they needed names; Section VIII's opening was cryptic ("I can read it ten times and still won't understand"); every section and subsection must open by saying plainly what it is trying to say and then develop it, as in good essay writing; the "(condition 4)"-style tags were annoying references. They also asked that the writing follow the skills in `ICLR_normalize/skills`, which add to the installed ones the paper-compression discipline: write the story spine in prose first and rebuild each section from the spine rather than patching paragraphs.

## What was done

1. **A story spine was written first** (`scratchpad/brief_O.md`): nine plain sentences that carry the whole argument, with no section numbers, citations, or tags. Every section's opening was then derived from the sentence(s) it serves.
2. **The loops have names.** The local loop (what the text called Loop 1) and the promotion loop (Loop 2), defined once in Section III-A with the parenthetical "(Figures and the released table label them Loop 1 and Loop 2.)" and used by name everywhere else in the article: prose, headings (VI and VII), table cells and captions (V-2, VII-1, VIII-1, IX-1), the figure captions, property (a) ("auto-gated local loop"), and the gate grid's axes ("Local gate" / "Promotion gate"). Figures 1, 2, and 3 carry the names; the supplementary keeps the Loop 1 / Loop 2 column labels of the released table, with the key stating the correspondence.
3. **Every section and subsection opens on its point.** Six Opus writers, one per file group, each working from the spine and the project style guide, rewrote each opening to say in plain words what the section establishes and why it matters, with no citation, cross-reference, or colon-list in the opening, and reorganized the body to deliver in the announced order. The "(condition N)" tags are gone; the five conditions are named (a measurable loss, a failure log, credit assignment or the trace, a candidate edit, a gate), with the numbered list in III-B as the definition.
4. **A tightening pass** removed the mechanical residue of step 3: the "The subsection takes X first and Y second" sentences and the second-paragraph restatements of the new openings (1,260 words). Four sections with subsections keep a one-sentence promise.
5. **Invariants** (`scratchpad/invariants_O.py`): citation-key and number multisets, REF token sets, headings, table lines, caption lines, raw blocks, and equations compared after normalizing the loop names; bold definition terms; no em-dash; no loop numbers in prose; no condition tags; the abstract's verify sentence and length; V's required sentences. All pass; the only structural change outside the loop names is the two figure captions dropping "the local half" / "the promotion half" next to the new names.

## Numbers

IEEE `main.pdf` 24 pages (the plain openings cost two pages; the verifier's target is now 16 to 24), 4 figures, 10 tables, 148 main references, abstract 250 words; arXiv v4 85 pages, 0 undefined. `check_revision.py` PASS, `check_cites.py` 148 = 148. Floats on pages 4, 5, 7, 10, 14 to 17, 19, 20; Table 10 sits above the references.

## Left for the author

- Section VII's bottom-row sentence says the row holds "the systems with no failure-driven loop" and then places SkillRL and SkillForge, which have one, in its last cell; the writer flagged the tension and did not resolve it because the fix is a claim decision (name the exception in that sentence, or move the two to a sentence of their own).
- Section XI's numbered problems open by restating their bold labels; the tightening pass left numbered lists alone.
