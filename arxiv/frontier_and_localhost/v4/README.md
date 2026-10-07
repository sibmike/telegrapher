# Frontier and Localhost, v4 (October 2026): the arXiv package

*Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights*
(Arbuzov, Mosbacker, Bei, Dong, Kalaev, Shvets). This directory is the arXiv submission package. It is the canonical text of the paper as of October 2026 and supersedes `../short/` (v3.2, September 2026) and `../paper_frontier_and_localhost.*` (the long version).

## What it is

The same text as the IEEE Access survey article in `../../../ieee_access/paper_frontier_and_localhost/`, re-set as a one-column `article` with the supplementary material carried as appendices:

| Part | Pages | Source |
|---|---|---|
| Sections 1–11 | 1–22 | the IEEE package's `submission/sections/*.md` |
| References (177 cited works) | 22–33 | `references.bib` (copied from the IEEE package) |
| Appendix A, formal statement; B, gate families | 34–36 | `appA_formal.md`, `appB_gates.md` |
| Appendices C–H: data appendix, mechanism stack, contrast set and matrix membership (first pass), convergent families, audit of the first-pass draft's claims with the rubric-reward comparison, extended related work | 36–66 | the IEEE package's `submission/sections/S2_*.md` … `S7_*.md`, assembled into `submission/supplementary.md` |
| Appendix I: full score table (269 rows) | 66–73 | `supplementary.md` (S1, generated from the CSVs) |
| Ancillary files (`anc/`) | — | the two score CSVs and `recount.py`, with a README |

73 pages, 4 figures, 11 captioned tables, 11pt, 1 in margins, pdflatex with the IEEEtran bibliography style (numeric citations, as in the IEEE text). The text is the October 2026 readability revision of the IEEE article (body and appendices rewritten for first-read clarity; see the IEEE package's `REVISION_LOG_A.md` to `REVISION_LOG_D.md`).

## How it builds

```
bash build.sh
```

1. mirrors `references.bib`, the four figure PDFs, the CSVs, and `recount.py` from the IEEE package;
2. `assemble_arxiv.py` writes `paper_frontier_and_localhost.md`: YAML header (title, six authors, abstract), the body, Acknowledgments, the bibliography call, `\appendix`, then the appendices. It re-targets the IEEE text for one column: figure widths, `Supplementary Material S<n>` pointers and the supplementary's literal section labels become cross-reference tokens, IEEE-specific wording becomes neutral;
3. pandoc (`--natbib --number-sections --shift-heading-level-by=-1`) to LaTeX;
4. `postprocess_tex.py`: natbib cites to plain `\cite`, the ten "Table X-N." tagged tables to `table` floats with the caption above (the untagged appendix tables stay `longtable`), `REF(x)` tokens to `\ref`;
5. pdflatex, bibtex, pdflatex ×2; checks (undefined references and citations, cited keys = bibitems, overfull boxes, arXiv filename character set);
6. `paper_frontier_and_localhost.zip` = `.tex` + `.bbl` + `figures/*.pdf` + `anc/`.

The zip compiles standalone with pdflatex alone (arXiv does not run BibTeX; the `.bbl` is included). Edit the paper in the IEEE package's section files, never here; rerun the IEEE package's `scripts/generate_supplementary.py` and then this `build.sh`.

## arXiv submission metadata

| Field | Value |
|---|---|
| Title | Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights |
| Authors | Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey A. Shvets |
| Abstract | the text of `../../../ieee_access/paper_frontier_and_localhost/submission/abstract.md` (250 words, plain text, no markup) |
| Primary category (proposed) | cs.AI |
| Cross-lists (proposed) | cs.LG, cs.SE |
| License | CC BY 4.0 (the repository's paper license) |
| Comments | 73 pages, 4 figures, 11 tables. Part 3 of a series: Part 1 arXiv:2505.24187, Part 2 arXiv:2605.30628. Score tables and recount script as ancillary files. |
| Upload | `paper_frontier_and_localhost.zip` |

The categories are a proposal for the submitting author to confirm on the form. The series has no arXiv id for this paper yet; once assigned, record it in `../README.md` and in the IEEE package's cover letter.

## Checklist before upload

- [ ] `bash build.sh` reports 0 undefined references, 0 undefined citations, cited keys = bibitems.
- [ ] Page 1 shows title, six authors, abstract; no draft notice.
- [ ] Every figure and table page inspected (done 2026-10-07 for this build; redo after any edit).
- [ ] Acknowledgments wording (AI-assistance disclosure) approved by the authors.
- [ ] Categories confirmed; license chosen; abstract pasted as plain text.
