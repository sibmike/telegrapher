# Beyond Exponential Decay — IEEE Access Topical Review

Journal version of *Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models* (Arbuzov, Bei, Dong, Kalaev, Shvets), restructured as an IEEE Access **Topical Review**. The preprint lives at [arXiv:2505.24187](https://arxiv.org/abs/2505.24187); its v3 source is frozen in [`../../arxiv/beyond exponential decay/`](../../arxiv/beyond%20exponential%20decay/).

## Layout

| Path | Role |
|---|---|
| `main.tex` | The manuscript, written against the official IEEE Access LaTeX class (`ieeeaccess.cls`, template dated 2026-05-13). |
| `references.bib` | Bibliography. Every entry is taken from the venue's own record or the arXiv abs page, and every cited claim is checked against the full text (see `citation_ledger.md`). |
| `citation_ledger.md` | One row per (citation, sentence) pair: the source passage, its location, its scope, and a verdict. No citing sentence enters `main.tex` without a row marked accurate or narrowed. |
| `ledger_parts/` | The per-batch working files that `citation_ledger.md` is assembled from. Parts A–I cover the main text, J1–J8 the works added for Appendix B, and K records the independent final-wording audit. |
| `audits/` | The three independent final-wording citation audits (2026-10-03). Each covers one range of the paper and gives every finding with its evidence and fix. |
| `sweep_candidates.md`, `related_work_cards.md` | How Appendix B ("Adjacent Lines of Work") was scoped: two simulated memory-based reviewer sweeps, the candidates they raised, and the decisions taken. |
| `humanization_log.md`, `humanization2_log.md` | Change logs of the two texture passes, which follow the telegrapher style profile. Each logs its edits rule by rule, with invariant checks. |
| `figures/` | Fig. 1 source (`fig1_decay_regimes.tex`, pgfplots) and its data generator (`make_fig1_data.py`, pure Python). |
| `template_original/` | The untouched official template zip and its unpacked sample. |
| `SUBMISSION_NOTES.md` | Manuscript type, keywords, cover letter, AI-disclosure text, number-check log, and the inputs still needed from the authors. |
| `build.sh` | `pdflatex → bibtex → pdflatex ×2`. |

Class, font and logo files (`ieeeaccess.cls`, `IEEEtran.cls`, `IEEEtran.bst`, `spotcolor.sty`, `t1-*.pfb/.tfm`, `*.fd`, `*.map`, `*.png`) are copied verbatim from the template.
