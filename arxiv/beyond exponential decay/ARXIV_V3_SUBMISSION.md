# arXiv v3 upload notes (Beyond Exponential Decay, 2505.24187)

The upload is an account action and is done by hand. Everything below is prepared.

## Package

`arxiv_v3_submission.zip` (built by `bash build.sh` followed by the zip step in this folder). Contents:

- `main.tex` — preprint wrapper (5-author block, `[preprint]` option)
- `body.tex` — paper body, `\input` by `main.tex`
- `main.bbl` — pre-built bibliography (arXiv does not run BibTeX; keep `main.bbl` in sync with `references.bib`)
- `neurips_2026.sty`
- `figures/fig1_decay_regimes.pdf`

Not included on purpose: `references.bib` (optional; the `.bbl` is what is used), `.aux/.log/.out`, `figures/*.tex|*.dat|*.py`, `legacy_v1/`.

arXiv builds with `pdflatex`; no shell escape, no `pgfplots` needed because the figure is a pre-rendered PDF.

## Form fields

- **Replace** existing submission 2505.24187 (new version, not a new article).
- **Title / authors / abstract:** unchanged title and author order. Paste the abstract from `body.tex`. It changed in four places: the key-token fractions, the ensemble sentence (now marked as our reading), "learned compression of the key-value cache", and a closing sentence about long-horizon agentic tasks. arXiv abstracts are plain text, so remove the LaTeX math markup when pasting.
- **Comments:** `v3: every cited result re-checked against the full text of its source; corrected misattributed statistics and scopes (LongPPL, RetrievalAttention, Anchor-LLM, TextFooler, AIMO-2, Tree of Thoughts, and others) and marked interpretations as ours; fixed the union-bound and majority-vote derivations in Sec. 3; added Fig. 1, a related-work paragraph on decision-point tokens, and a Limitations discussion relating the token-level model to long-horizon agent results. 13 pages, 1 figure, 1 table.`
- **Categories:** keep cs.CL primary, cs.AI, cs.LG cross-lists.
- **License:** keep the one chosen for v1/v2.

## Pre-upload checklist

1. `bash build.sh` completes; `main.log` has no `undefined` warnings and `main.blg` no BibTeX warnings (verified 2026-10-03: 0 and 0).
2. Bibliography: 29 `\bibitem`s in `main.bbl`, 29 distinct cited keys (verified 2026-10-03).
3. `neurips/paper_beyond_exponential_decay/submission/body.tex` and `references.bib` are byte-identical to the files here (verified with `diff -q`, 2026-10-03).
4. The zip compiles on its own with plain `pdflatex` and no undefined references (verified 2026-10-03: 13 pages).
5. Page 1 shows five authors with line breaks between name, affiliation, email; footer reads "Preprint." (verified visually 2026-09-20; re-check after this rebuild).
6. Full-text citation review applied (2026-10-03): see `CHANGELOG.md` and the ledgers in `../../ieee_access/paper_beyond_exponential_decay/ledger_parts/`. Re-run `bash build.sh` after any bib edit so `main.bbl` is regenerated before zipping.
