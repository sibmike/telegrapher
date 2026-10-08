# Revision log F: response to the external review (2026-10-08)

Review of the story-first build (`063e1b6`); verdicts and the authors' response in `REVIEW_RESPONSE_2026-10-07.md`. No evidence added; one classic reference added for the proof repair (`robbins1971convergence`, allowed in `scripts/check_revision.py`).

## Data

- `supplementary/p3_refresh_2026-10.csv`: nine rows re-coded by `recode_gates.py` (session scratch) under the strict gate definition. Letta's Loop 2 Auto → None (ungated push; still an audit passer on lineage, and `recount.py` now counts an "ungated" Loop-2 mechanism as present). Loop 1 Human → None for Azure API Center, MCP Gateway & Registry, Official MCP Registry, TrueFoundry, Buildrix, the revocation guard, and the skills field study; Enoch → None on both loops; MCP Gateway's Loop 2 records the admission scan beside the human approval; the field study's Loop 2 records that maintainers merge. No score changed. Recorded in S6.7 and `CLAIMS_AUDIT.md`.

## Body

- **III-C.** Auto = a program applies a check; Human = a person decides; None = nothing decides (absent or unchecked step). Candidate source is recorded, not an axis. The convergence pointer sentence reworded (gate stability, not optimality). III-D: Letta's push is "ungated".
- **IV.** Assignment rule for the classes (delay, then absence of ground truth, then exactness). C1: one run settles the checked case; the margin absorbs sampling error over the patch. Table IV-1 C1 cell and C4 examples changed (AlphaEvolve's archive out, the AI Scientist in). C4 paragraph: AlphaEvolve's database is a search strategy inside C1. Automatic promotion without a receiving-side person now conditioned on the receiving side running the same check.
- **V-B.** Denominator stated once: audit applied to 204 core + 10 mechanism-level systems; 14 research passers = 13 table rows + SkillOpt; 3 industry exemplars; Letta promotes with no gate. **V-C.** Disclosure that scores have not been independently re-rated.
- **VI.** Opening: "no surveyed system documents the governed second half". Table VI-2 last row: "None / Human, or None / None".
- **VII.** Rewritten around the strict axes: two gated cells, one half-cell, one ungated passer (Letta in [Auto × None]); registries in [None × Human]; curation (VerificAgent, SkillChain) in [Human × None]; [Human × Auto] and [Human × Human] empty with one interpretable meaning. Figure 4 cells and caption updated in `make_figures.py`.
- **II-B.** Reframed: the two earlier papers supply the hypothesis the corpus is consistent with; each paper's scope stated from its own abstract; conclusion conditional; the survey's findings stand without it. **Abstract**: "suggest why"; "the governed second loop is undocumented". **I ¶2**: "as far as public evidence shows". **XI**: problem 5 and the conclusion reworded to match.

## Appendices

- **A.** (A3) now includes a positive acceptance probability for an improving edit; (A5) is summable bias alone; the Robbins–Siegmund form gives almost-sure convergence of the loss and finite cumulative descent as the conclusion; the gate-stable limit follows. The per-class bias sentence narrowed for C1.
- **B.** Archive selection: inherits the class of its evaluator (C1 in AlphaEvolve); the closing sentence on C4 families corrected.
- **S2.** Final paragraph names the empty and occupied cells under the strict axes. **S4.2.1.** Convention paragraph replaced; [Auto × None] paragraph added; [Human × Human]/[Human × Auto] empty; registries moved to [None × Human]; occupant table with candidate source, Loop 1 gate, promotion mechanism, Loop 2 gate. **S6.2.** Four rows updated; **S6.7.** re-coding paragraph added.

## Other

- `cover_letter.md`: the Supplementary Material is uploaded with the submission.
- `references.bib`: `robbins1971convergence` (Crossref record: Optimizing Methods in Statistics, 1971, pp. 233–257, DOI 10.1016/B978-0-12-604550-5.50015-8).
