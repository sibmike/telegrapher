# Frontier and Localhost — IEEE Access survey article

Journal version of *Frontier and Localhost: How Production AI Learns Outside the Weights* (Arbuzov, Mosbacker, Bei, Dong, Kalaev, Shvets), restructured as an IEEE Access **survey article**. The arXiv short v3.2 in [`../../arxiv/frontier_and_localhost/short/`](../../arxiv/frontier_and_localhost/short/) is the source of record for the survey; this package rescoreds the corpus to an October-2026 cutoff, adds a feedback-signal classification (Section IV), and simplifies the argument for journal review. No new experiments.

## The argument, in one paragraph

Three papers. *Beyond Exponential Decay* (arXiv:2505.24187) shows that reliability over long outputs hinges on a sparse set of key decisions rather than on uniform per-token accuracy. *The Architecture of Errors* (arXiv:2605.30628) shows that inside a bounded deployment those key-decision failures cluster into a finite, slowly growing catalogue of recurring modes, so a small budget of targeted interventions covers them. This article shows where that budget is actually spent in production, in persistent artifacts outside the weights, and that doing so is the correct architecture rather than patchwork once the loop that edits those artifacts is gated and scoped. The new axis here is the **feedback signal**: code and mathematics give an exact check, completed tasks give an observable outcome, writing and design give only a judge, research gives a delayed and sparse reward, and that class fixes what the gate can be, which cells of the two-loop design space are reachable, and which failure dominates.

## Layout

| Path | Role |
|---|---|
| `submission/paper_frontier_and_localhost_ieee.md` | Manuscript body (Markdown; pandoc → `body.tex` fragment). |
| `submission/abstract.md` | Abstract (≤250 words, no subheadings). |
| `submission/main.tex` | Official `ieeeaccess.cls` shell: authors, keywords, acknowledgment with AI disclosure, biographies. |
| `submission/sections/` | **Source of truth for the text.** `I_III.md` … `XI_open_problems_conclusion.md` and `appA_formal.md`, `appB_gates.md` are the body (assembled by `scripts/assemble.py`); `S2_data.md` … `S6_audit.md` and `S7_extended_related_work.md` are Supplementary S2–S7 (assembled by `scripts/generate_supplementary.py`, which generates S1 from the CSVs). Edit here; never edit the assembled files. |
| `submission/references.bib` | Bibliography (IEEEtran.bst, numeric). Seeded from the arXiv short; refresh entries verified against arXiv abs pages. |
| `submission/figures/` | `fig1_descent_ieee`, `fig2_scope_ieee`, `fig3_design_space_ieee`, `fig4_corpus_flow_ieee` — rendered by `../../arxiv/frontier_and_localhost/figures/make_figures.py --ieee`. |
| `submission/supplementary.md` | Assembled Supplementary Material S1–S7 (score table; data appendix; mechanism stack; contrast set and matrix membership; convergent families walkthrough; audit of the first-pass draft's absolute claims with the rubric-reward comparison; extended related work), with a key to the labels in its front matter. |
| `scripts/check_revision.py` | Gate for the readability revision: document-wide citation key set unchanged, every number that left the prose still present in a table or appendix, no process vocabulary outside V-B, labels defined before use, supplementary pointers in the required form. |
| `REVISION_LOG_A.md` … `REVISION_LOG_E.md` | Change logs of the 2026-10-07 revisions (A body, B appendices C–E, C appendices F–H, D light style pass, E the story-first rewrite of the body with the reworked tables and figures and the seven-promoters correction). |
| `supplementary/p3_master_scores.csv`, `supplementary/p3_refresh_2026-10.csv` | Corpus scores: May-2026 corpus and October-2026 refresh rows. |
| `scripts/recount.py` | Recomputes corpus counts, per-substrate maturity, matrix membership from the CSVs. |
| `CLAIMS_AUDIT.md` | Every absolute claim of the arXiv version with its post-refresh verdict. |
| `related_work_cards.md` | Evidence cards (one per neighbouring work, verified from primary sources) behind Supplementary S7, the extended related work. |
| `submission/sections_before/` | Snapshot of the sections before the style and texture passes; `scripts/check_invariants.py` diffs numbers, citations, cross-references, and structure against it. |
| `cover_letter.md` | Cover letter for the submission portal. |
| `submission/build.sh` | pandoc → pdflatex → bibtex → pdflatex ×2; also builds `supplementary.pdf`. |

Class, font and logo files (`ieeeaccess.cls`, `IEEEtran.cls`, `IEEEtran.bst`, `spotcolor.sty`, `t1-*`, `*.fd`, `*.map`, `*.png`) are copied verbatim from the official template in `../paper_beyond_exponential_decay/template_original/`.

## Status (2026-10-07, story-first rewrite)

Story-first rewrite complete (2026-10-07, `REVISION_LOG_E.md`): the body now reads as a structured essay around one spine (one loop with two halves; the local half is routine, the governed second half unbuilt, the feedback-signal class decides which half closes), every section opening with the sentence that advances it. Table 1 (related surveys) is four columns, the three-stages table is a paragraph, the signal-class table is five columns, the substrate table has short cells; Figures 1 and 2 were redrawn (Loop 1 as six stations; Loop 2 as a ladder of scopes with a gate per rung). Section VII's seven-promoters sentence was corrected against the released rows (only EvolveNet carries rollback; five carry no governance property at all). Current numbers: `main.pdf` 19 pages, 4 figures, 10 tables, 147 references; `supplementary.pdf` 36 pages; arXiv v4 72 pages, 177 references.

Earlier readability revision (2026-10-07, morning). The body was rewritten so that it reads on the first pass: the thesis is stated in the Introduction, every label is defined before its first use, counts live in tables and captions, process narration is confined to the corpus subsection of Section V, and each subsection opens with what it establishes. The appendices were rewritten on the same rules and now live as section files; the audit appendix states what the corpus shows instead of instructing the authors. Along the way several body statements were corrected against the released data (SkillChain's human gate is local, not a promotion gate; EvolveNet merges on "at least as many" fixed items; Future AGI rests on vendor-blog evidence and enters under no rule; cross-tenant promotion means reaching CORE), and Section V now states that ten systems treated at mechanism level (SkillOpt among them) are classified from their papers and are not rows of the released table. Current numbers: `main.pdf` 19 pages (two-column IEEE Access), 4 figures, 11 tables, 147 references; `supplementary.pdf` 36 pages (S1–S7, one reference list).

Earlier state (2026-10-03): `main.pdf` 19 pages, 4 figures, 10 tables, 147 references; `supplementary.pdf` 40 pages (S1–S7). Corpus: 256 unique systems (130 by May 2026, 126 added by the October 2026 sweep), 204 core, 52 contrast; composite two-loop audit passed by 14 research systems and 3 industry exemplars. `scripts/verify_ieee.py` passes. The claims audit (`CLAIMS_AUDIT.md`) records 11 revised, 8 sharpened, 1 dropped, and the rest holding; the four-property gap of Section IX remains open.

Passes applied on 2026-10-03, in order: the `writing-style` and `humanization` skills over every section (claims, numbers, citations, and cross-references held fixed; `scripts/check_invariants.py` against `submission/sections_before/`); the `extended-related-work` skill, which produced Supplementary S7 (organized by the article's four design commitments) and `related_work_cards.md` (one verified evidence card per cited neighbor); a skeptical-reviewer pass whose consistency defects, three overclaims, and ~30 missing canonical citations were all resolved (the new entries are in `supplementary/new_refs_2026-10-03.bib`, merged into `references.bib`); and a float-layout pass (every page rendered and inspected: table captions above the table per the IEEE class, proportioned column widths from the Markdown separator rows, every table placed on the page after its first reference, Figure 3 boxes resized to hold their text, Figure 4 cells relabeled to match Section VII).

Still needed from the authors before submission: biographies and photos (six), city/country per address, funding statement and the Palo Alto Networks conflict note, approval of the AI-disclosure wording in the Acknowledgment, confirmation of the preprint/workshop disclosure in `cover_letter.md`, suggested reviewers, and a final read of the eleven revised claims.

## Build

```
bash submission/build.sh
```

Citations are written as `[@key]` in Markdown; textual cites are written as "Author et al. [@key]" because the build turns every pandoc cite into a plain `\cite{}` for the template's `cite` package.
