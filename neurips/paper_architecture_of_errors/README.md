# NeurIPS Submission Package — The Architecture of Errors

This directory holds a NeurIPS-2026-format submission package for **"The Architecture of Errors: Logarithmic Mode Discovery and Polylogarithmic Intervention Budgets for Long-Context LLM Reliability"** (Part 2 of the error-clustering series, follow-on to "Beyond Exponential Decay"). Anonymized and formatted with `neurips_2026.sty` for double-blind review.

## Status

**Built 2026-05-21 as a format-ready artifact with no committed venue.** The NeurIPS 2026 main-track submission window (May 6, 2026 AOE) closed two weeks before this package was built; we have not submitted it. The package is preserved so it can be repurposed for:

- **NeurIPS 2027** — re-verify against the new `neurips_2027.sty` (typically released January–March); the body cut is already at 7.5 / 9 pages so it should survive minor template changes.
- **A workshop** with NeurIPS-compatible formatting — verify the workshop's specific template against our preamble.
- **Another conference** (ICLR, ACL, NAACL, EMNLP) — the page budget will need recutting since other venues use different limits; the body story, appendices, anonymization, and checklist substance carry over.

Before reusing for any of those, re-verify the active template, deadlines, and checklist version.

## Quick links

- **Paper PDF**: [`submission/main.pdf`](submission/main.pdf)
- **LaTeX source**: [`submission/main.tex`](submission/main.tex)
- **Bibliography**: [`submission/references.bib`](submission/references.bib)
- **Checklist**: [`submission/checklist.tex`](submission/checklist.tex)
- **Reproducible build**: `bash submission/build.sh`
- **Template reference (shared with sibling packages)**: [`../_template_reference/`](../_template_reference/)

## Submission metadata

| Field | Value |
|---|---|
| **Conference target** | NeurIPS 2026 main track (format-ready; not submitted) |
| **Track** | Main Track (double-blind) |
| **Style file** | `neurips_2026.sty` (official, dated 2026-01-29) |
| **Title** | The Architecture of Errors: Logarithmic Mode Discovery and Polylogarithmic Intervention Budgets for Long-Context LLM Reliability |
| **Authors** | Anonymous (double-blind) |
| **Primary subject area** | Theory / Long-context Modeling |
| **Page count** | 25 pages total: 7.5 pages main body + ~4.5 pages references + 5 pages appendix (A–C) + 8 pages mandatory checklist |
| **Main-body limit** | 9 content pages — we use 7.5 |
| **Submission portal** | OpenReview (`NeurIPS.cc/2026/Conference`) — N/A, deadline passed |

### Key deadlines (shared with sibling packages, all in AOE)

| Milestone | Date |
|---|---|
| **Abstract submission** | May 4, 2026 — passed |
| **Full paper submission** | May 6, 2026 — passed |
| Author notification | September 24, 2026 |
| Build date for this package | 2026-05-21 |

## Pre-submission checklist

Build verification (passed):

- [x] PDF builds via `bash submission/build.sh` (pdflatex → bibtex → pdflatex × 2)
- [x] Title page renders as `Anonymous Author(s) / Affiliation / Address / email` (anonymized correctly)
- [x] Line numbers visible down the left margin (added by `neurips_2026.sty` for review)
- [x] Main body fits in 7.5 pages (under the 9-page limit; references begin mid-page 8)
- [x] References render with author/year style (`natbib` default, `plainnat`)
- [x] All inline equations and the Proposition 1 displayed equation render correctly
- [x] Three appendices render with cross-references resolved (no `??` in PDF; verified via `pdftotext`)
- [x] Unicode operators (→ ⇒ ∴ ∵ ∧ ∨ ≈ ≠) render via `\teArrow`/`\teImplies`/... macros under pdflatex
- [x] Mandatory paper checklist filled with paper-specific answers (16 questions: 5 Yes, 11 NA — framework + synthesis paper, no original experiments)
- [x] No author-identifying information in the built PDF (no funding acknowledgments, no repository URLs, no institutional affiliations; verified via `pdftotext`)
- [x] Self-citations to the Part 1 preprint rewritten in third person and cited via anonymized `arbuzov2025beyond` bib entry
- [x] Bibliography produced from `references.bib` via `bibtex` (73 entries; one entry anonymized for the submission copy)

Submission-time checks (if reused for an open venue):

- [ ] Re-verify the active conference template against `_template_reference/neurips_<YEAR>.sty`
- [ ] Re-verify the active checklist version (the checklist changes year to year)
- [ ] Upload `submission/main.pdf` as the paper
- [ ] Confirm anonymized author information on the venue's metadata form
- [ ] Select track and primary subject area
- [ ] Disclose conflicts of interest

## Anonymization notes

The paper has been anonymized for double-blind review:

1. **Author block**: `Anonymous Author(s) / Affiliation / Address / email` (no real names).
2. **Self-citations to Part 1** (the "Beyond Exponential Decay" preprint, arXiv:2505.24187): the source has nine first-person references ("Our previous work...", "In our previous paper..."). All nine have been rewritten in third person and cited via `\citep{arbuzov2025beyond}` or `\citet{arbuzov2025beyond}` to point at the public arXiv preprint. The `arbuzov2025beyond` bib entry in `references.bib` has been anonymized (`author = {{Anonymous}}`) for this submission copy only; the arXiv-side bib remains unchanged.
3. **Acknowledgments / funding**: none present in the source — nothing to suppress.
4. **Repository URL**: not referenced. The arXiv preprint URL and any code URL will be added to the camera-ready.
5. **`\hypersetup{pdfauthor=...}`**: not used; PDF metadata is empty rather than identifying.
6. **First-person framing**: verified absent by `grep -ni "our previous\|we previously\|our prior\|in our paper" main.tex` returning 0 matches.

When preparing a camera-ready (after acceptance to some venue), switch `\usepackage{neurips_2026}` to `\usepackage[main, final]{neurips_2026}` to reveal authors, and restore the real `author` field on the `arbuzov2025beyond` entry.

## Page budget

| Section | Approx. pages |
|---|---|
| Abstract + §1 Introduction | 1.5 |
| §2 Related Work (4 `\paragraph{}` blocks) | 0.5 |
| §3 Theoretical Framework (definitional para + 4 subsections, incl. Proposition 1) | 2.5 |
| §4 Empirical Evidence (Claims A, B, C as paragraph headers) | 1.0 |
| §5 Practical Implications (4 `\paragraph{}` blocks) | 0.75 |
| §6 Discussion (boundary case + counter-evidence summary + limitations) | 1.0 |
| §7 Conclusion | 0.25 |
| **Main body total** | **~7.5 / 9 max** |
| References (73 entries, `plainnat`) | 4.5 |
| Appendix A: Heaps Power-Law Variant and Cluster-Count Sensitivity | 1.0 |
| Appendix B: Full Failure-Mode Taxonomy (incl. 28-citation capability-elimination table + 12-cluster table) | 3.0 |
| Appendix C: Counter-Evidence Re-Audits (5 papers) | 1.0 |
| Mandatory paper checklist | 8.0 |
| **Document total** | 25 |

References, appendices, and the checklist do not count against the 9-page main-body limit. We have 1.5 pages of slack under the cap.

## Story-driven page cut (the key design choice)

The arXiv version of this paper is ~23 pages. The NeurIPS 9-page main-body cap required aggressive compression. Rather than amputating sections by lowest-payoff-to-cut, we cut by **story coherence**: the body reads as a clean argument chain from §1 through §7, with appendices supporting (not carrying) the argument. The argument chain in the body is:

1. **Setup** (§1): errors are not uniformly distributed — they cluster.
2. **Definition of |C|** (§3 opening paragraph, absorbing §3.0 of the source): four levels of "failure mode count" — without this, §3.1 has no antecedent.
3. **β-stratification** (§3.1): a small subset of key tokens drives most failures.
4. **Logarithmic-discovery postulate** (§3.2): the load-bearing empirical assumption of Proposition 1 — cannot live only in an appendix.
5. **Coverage** (§3.3): with the `min(1, ·)` cap preserved verbatim per the math-claims discipline.
6. **Proposition 1** (§3.4): polylog intervention budget, conditional on the postulate.
7. **Empirical anchor** (§4): claims A, B, C with one-paragraph evidence each.
8. **Payoff** (§5): practical implications.
9. **Critical qualifier** (§6): boundary case + counter-evidence summary (one paragraph in body, detail in Appendix C) + limitations.
10. **Close** (§7).

What moved to appendices is *supporting* material that a reader can defer without losing the thread:

- **Appendix A** (Heaps variant + sensitivity): alternative cluster-count laws and a symbolic-form robustness check. The qualitative polylog conclusion survives across the candidate-law family; the doubly-logarithmic rate of Proposition 1 is the optimistic special case.
- **Appendix B** (full taxonomy): the 28 capability-elimination citations across six axes (stratified into Patterns A/B/C), with the table; the 12 named clusters with their interventions; the additivity caveats; the irreducible-semantic residual analysis.
- **Appendix C** (counter-evidence re-audits): per-paper walk-throughs of Dziri, BABILong, METR, Wan, NoCha showing the relocation-not-dissolution pattern.

## Math-claims discipline (preserved during compression)

Per the project's math-claims-discipline note, the following caveats are preserved verbatim from the source and were not silently strengthened during compression:

- §3.2 states `k_hard ~ ln n` as an **empirical postulate**, not a derivation. `ln/ln` framing is an empirical fit, not a discrete Zipf theorem.
- §3.3's coverage formula keeps the `min(1, ·)` cap on per-hard-token coverage.
- Proposition 1 is conditional on the postulate of §3.2 — **not** on "Zipf's law" or "Heaps' law" (Heaps is a power law and does *not* yield logarithmic growth; that's the whole point of Appendix A being a *variant*).
- Per-hard-token coverage and sequence-level coverage are kept as distinct quantities throughout §3.4.
- Finite-`α` regime (the empirical 5–10% sparsity at typical `n`) is kept separate from the asymptotic `k ~ log n` regime.

## Submission-specific adaptations vs.\ the arXiv version

| Item | NeurIPS-format adaptation |
|---|---|
| Format | `neurips_2026.sty` (pdflatex) instead of xelatex+Cambria |
| Unicode operators | `\teArrow` / `\teImplies` / ... macros instead of OpenType Cambria glyphs |
| Page count | 25 (incl. references, 3-appendix appendix, and 8-page mandatory checklist) |
| Main-body length | compressed from 23 pages to 7.5 pages |
| Sections moved to appendix | §3.5 (Heaps variant) + §3.6 (sensitivity) → Appendix A; §4.2 detailed 12-category taxonomy + 28-citation table → Appendix B; §6.2 per-paper counter-evidence re-audits → Appendix C |
| §3.0 (Four levels of \|C\|) | Absorbed into the §3 opening paragraph (not an appendix; story-critical antecedent) |
| §3.2 (Logarithmic-discovery postulate) | Kept in body as a named subsection (load-bearing for Proposition 1; cannot be appendix-only) |
| Bibliography | `plainnat` author/year via `references.bib`; one entry (`arbuzov2025beyond`) author-field anonymized |
| Self-citations | 9 first-person references to the Part 1 preprint rewritten in third person |
| Acknowledgments | none in source; nothing to suppress |
| Mandatory checklist | filled (5 Yes, 11 NA; framework + synthesis paper with no original experiments) |
| Engine | pdflatex |

## Rebuilding

```bash
# from this directory
bash submission/build.sh
```

The build runs `pdflatex` → `bibtex` → `pdflatex` × 2 to resolve citations and cross-references. Requires MiKTeX (Windows) or TeX Live (Linux/macOS) with `pdflatex` and `bibtex` on `PATH`. The build script pre-extends `PATH` for the standard Windows MiKTeX install location.

## Source of truth and provenance

| Asset | Source | Date verified |
|---|---|---|
| `submission/neurips_2026.sty` | Copied from `../_template_reference/`, originally from `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` | 2026-04-29 |
| `submission/checklist.tex` | Adapted from `../_template_reference/checklist.tex` (same ZIP) | 2026-04-29 |
| `submission/build.sh` | Byte-identical to sibling package `paper_beyond_exponential_decay/submission/build.sh` | 2026-05-21 |
| `submission/references.bib` | Derived from `../../arxiv/architecture_of_errors/paper_architecture_of_errors.bib` with `arbuzov2025beyond` author field anonymized | 2026-05-21 |
| Source paper (Markdown) | `../../arxiv/architecture_of_errors/paper_architecture_of_errors.md` | 2026-05-21 |
| Template style file `\ProvidesPackage` date | `2026-01-29` | — |
| Call for papers | `https://neurips.cc/Conferences/2026/CallForPapers` | 2026-05-21 |
