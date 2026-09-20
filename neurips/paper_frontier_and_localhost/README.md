# Frontier and Localhost — NeurIPS-formatted version

Conference-formatted (NeurIPS 2026 preprint style) version of *Frontier and Localhost: How Production AI Learns Outside the Weights*. Part 3 of the series, following *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)) and *The Architecture of Errors* (Part 2).

This is a **format-only** port of the arXiv "short" version — same content, NeurIPS layout. **Revision lag:** the port reflects short v3.1 (June 2026) plus the v3.2 count fixes (twelve [Auto × Auto] systems, fourteen strict passes, "paper's thesis"); the v3.2 figures, literature refresh (FederatedSkill, SkillClaw, ChronoMem, HARNESSEVO, SkillsVote), Appendix D split, American-spelling pass, and `$\eta_t$` notation are **not** ported. Regenerate `body.tex` from the short `.md` before any actual submission. NeurIPS 2026 deadlines (May 2026) have passed, so the package is kept **format-ready**: real author names are shown via the `[preprint]` option, and the mandatory paper checklist is filled in [`submission/checklist.tex`](submission/checklist.tex) but its `\input` is commented out in `main.tex` (uncomment the two lines at the end of `main.tex` to render it for an actual submission).

For the argument overview and the canonical reference for reading and citation, see [`../../arxiv/frontier_and_localhost/short/`](../../arxiv/frontier_and_localhost/short/).

## Read

- **PDF**: [`submission/main.pdf`](submission/main.pdf)
- **LaTeX source**: [`submission/main.tex`](submission/main.tex)
- **References**: [`submission/references.bib`](submission/references.bib)

To rebuild the PDF locally: `bash submission/build.sh` (requires `pdflatex` and `bibtex` on `PATH`).
