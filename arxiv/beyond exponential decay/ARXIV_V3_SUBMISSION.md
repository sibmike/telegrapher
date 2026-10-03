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
- **Title / authors / abstract:** unchanged title and author order. Paste the abstract from `body.tex` (it changed: "KV-cache reduction" wording, and one new closing sentence about long-horizon agentic tasks).
- **Comments:** `v3: corrected misattributed statistics (LongPPL key-token fraction and window, TextFooler perturbation rates, Anchor-LLM KV-cache reduction, AIMO-2 tool integration); fixed the union-bound and majority-vote derivations in Sec. 3; added Fig. 1, a related-work paragraph on decision-point tokens (Bigelow 2025, Lin 2024, Wang 2025), and a Limitations discussion reconciling the token-level model with long-horizon agent results (Kwa 2025, Ord 2025, Sinha 2026). 11 pages, 1 figure, 1 table.`
- **Categories:** keep cs.CL primary, cs.AI, cs.LG cross-lists.
- **License:** keep the one chosen for v1/v2.

## Pre-upload checklist

1. `bash build.sh` completes; `main.log` has no `undefined` warnings (verified 2026-09-20: 0).
2. Bibliography: 29 `\bibitem`s in `main.bbl`, 29 distinct cited keys (verified).
3. `neurips/paper_beyond_exponential_decay/submission/body.tex` is byte-identical to `body.tex` here (verified with `diff -q`).
4. Page 1 shows five authors with line breaks between name, affiliation, email; footer reads "Preprint." (verified visually).
5. Figure 1 legend is in the upper-right, no label overlaps (verified visually).
6. Citation-audit report reviewed and any flagged fixes applied — see the session recap; re-run `bash build.sh` after any bib edit so `main.bbl` is regenerated before zipping.
