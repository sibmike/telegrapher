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
| `submission/sections/` | Drafts of new sections before they are merged into the body. |
| `submission/references.bib` | Bibliography (IEEEtran.bst, numeric). Seeded from the arXiv short; refresh entries verified against arXiv abs pages. |
| `submission/figures/` | `fig1_descent_ieee`, `fig2_scope_ieee`, `fig3_design_space_ieee`, `fig4_corpus_flow_ieee` — rendered by `../../arxiv/frontier_and_localhost/figures/make_figures.py --ieee`. |
| `submission/supplementary.md` | Supplementary material S1–S6 (representative rows, data appendix, mechanism stack, contrast set and matrix membership, per-family walks, SkillOpt correspondence). |
| `supplementary/p3_master_scores.csv`, `supplementary/p3_refresh_2026-10.csv` | Corpus scores: May-2026 corpus and October-2026 refresh rows. |
| `scripts/recount.py` | Recomputes corpus counts, per-substrate maturity, matrix membership from the CSVs. |
| `CLAIMS_AUDIT.md` | Every absolute claim of the arXiv version with its post-refresh verdict. |
| `related_work_cards.md` | Evidence cards (one per neighbouring work, verified from primary sources) behind Supplementary S7, the extended related work. |
| `submission/sections_before/` | Snapshot of the sections before the style and texture passes; `scripts/check_invariants.py` diffs numbers, citations, cross-references, and structure against it. |
| `cover_letter.md` | Cover letter for the submission portal. |
| `submission/build.sh` | pandoc → pdflatex → bibtex → pdflatex ×2; also builds `supplementary.pdf`. |

Class, font and logo files (`ieeeaccess.cls`, `IEEEtran.cls`, `IEEEtran.bst`, `spotcolor.sty`, `t1-*`, `*.fd`, `*.map`, `*.png`) are copied verbatim from the official template in `../paper_beyond_exponential_decay/template_original/`.

## Status (2026-10-03)

Draft complete and building: `main.pdf` 19 pages (two-column IEEE Access), 4 figures, 10 tables, 147 references; `supplementary.pdf` 40 pages (S1–S7). Corpus: 256 unique systems (130 by May 2026, 126 added by the October 2026 sweep), 204 core, 52 contrast; composite two-loop audit passed by 14 research systems and 3 industry exemplars. `scripts/verify_ieee.py` passes. The claims audit (`CLAIMS_AUDIT.md`) records 11 revised, 8 sharpened, 1 dropped, and the rest holding; the four-property gap of Section IX remains open.

Passes applied on 2026-10-03, in order: the `writing-style` and `humanization` skills over every section (claims, numbers, citations, and cross-references held fixed; `scripts/check_invariants.py` against `submission/sections_before/`); the `extended-related-work` skill, which produced Supplementary S7 (organized by the article's four design commitments) and `related_work_cards.md` (one verified evidence card per cited neighbor); a skeptical-reviewer pass whose consistency defects, three overclaims, and ~30 missing canonical citations were all resolved (the new entries are in `supplementary/new_refs_2026-10-03.bib`, merged into `references.bib`); and a float-layout pass (every page rendered and inspected: table captions above the table per the IEEE class, proportioned column widths from the Markdown separator rows, every table placed on the page after its first reference, Figure 3 boxes resized to hold their text, Figure 4 cells relabeled to match Section VII).

Still needed from the authors before submission: biographies and photos (six), city/country per address, funding statement and the Palo Alto Networks conflict note, approval of the AI-disclosure wording in the Acknowledgment, confirmation of the preprint/workshop disclosure in `cover_letter.md`, suggested reviewers, and a final read of the eleven revised claims.

## Build

```
bash submission/build.sh
```

Citations are written as `[@key]` in Markdown; textual cites are written as "Author et al. [@key]" because the build turns every pandoc cite into a plain `\cite{}` for the template's `cite` package.
