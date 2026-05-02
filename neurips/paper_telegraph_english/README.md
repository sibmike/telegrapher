# NeurIPS 2026 Submission — Telegraph English

This directory holds the NeurIPS 2026 main-track submission package for the Telegraph English paper, anonymized and formatted with `neurips_2026.sty` for double-blind review.

## Quick links

- **Paper PDF** (upload to OpenReview): [`submission/main.pdf`](submission/main.pdf)
- **Supplementary zip** (optional, source bundle): [`submission/supplementary.zip`](submission/supplementary.zip)
- **LaTeX source**: [`submission/main.tex`](submission/main.tex)
- **Reproducible build**: `bash submission/build.sh`
- **Template reference (untouched, shared with sibling papers)**: [`../_template_reference/`](../_template_reference/)

## Submission metadata

| Field | Value |
|---|---|
| **Conference** | NeurIPS 2026 |
| **Track** | Main Track (double-blind) |
| **Style file** | `neurips_2026.sty` (official, dated 2026-03-17) |
| **Title** | Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting |
| **Authors** | Anonymous (double-blind) |
| **Primary subject area** | Natural Language Processing / Efficient Methods for ML |
| **Page count** | 18 pages total: 8 pages main body + references + 3-page appendix + 7-page mandatory checklist |
| **Main-body limit** | 9 content pages — we use 8 |
| **Submission portal** | OpenReview (`NeurIPS.cc/2026/Conference`) |

### Key deadlines

| Milestone | Date (AOE) |
|---|---|
| **Abstract submission** | May 4, 2026 |
| **Full paper submission** | May 6, 2026 |
| Author notification | September 24, 2026 |

## Pre-submission checklist

Build verification (passed):

- [x] PDF builds via `bash submission/build.sh` (pdflatex → bibtex → pdflatex × 2)
- [x] Title page renders as `Anonymous Author(s) / Affiliation / Address / email` (anonymized correctly)
- [x] Line numbers visible down the left margin (added by `neurips_2026.sty` for review)
- [x] Main body fits in 8 pages (under the 9-page limit)
- [x] References render with author/year style (`natbib` default)
- [x] Two figures (compression-ratio histogram, compression-rate histogram) render correctly with side-by-side layout
- [x] Tables render via `booktabs` (no vertical rules)
- [x] Unicode operators ($\rightarrow$, $\Rightarrow$, $\therefore$, $\wedge$, $\vee$, $\neg$, $\uparrow$, $\downarrow$, $\approx$, $\neq$) render via math-mode commands wrapped in `\ttfamily` blocks
- [x] TE compression example (§1) renders as a `\footnotesize\ttfamily` quote block — fits cleanly on a single line
- [x] Mandatory paper checklist filled with paper-specific answers (16 questions: 9 Yes, 5 NA, 2 No)
- [x] No author-identifying information in the built PDF (no funding acknowledgments, no repository URLs, no institutional affiliations; verified via `pdftotext`)
- [x] Bibliography produced from `references.bib` via `bibtex` (12 entries)

Submission-time checks (do these in OpenReview):

- [ ] Upload `submission/main.pdf` as the paper
- [ ] Optionally upload `submission/supplementary.zip` as supplementary material
- [ ] Confirm anonymized author information on the OpenReview metadata form
- [ ] Select Main Track
- [ ] Set primary subject area; cross-list as appropriate
- [ ] Disclose conflicts of interest
- [ ] Acknowledge the funding/competing-interests disclosure (filled at camera-ready time, not submission)

Post-submission:

- [ ] Record the OpenReview submission ID once assigned

## Anonymization notes

The paper has been anonymized for double-blind review:

1. **Author block**: `Anonymous Author(s) / Affiliation / Address / email` (no real names).
2. **Repository URL**: not referenced in the paper or supplementary materials. The arXiv preprint URL and the public GitHub URL will be added to the camera-ready version.
3. **Acknowledgments**: omitted from the anonymized submission. The `\begin{ack} … \end{ack}` environment provided by `neurips_2026.sty` would auto-hide them anyway, but we have simply not written any in `main.tex` for the submission version.
4. **References**: refer to our own work in the third person if cited. (Currently we cite no work of our own.)

When preparing the camera-ready (after acceptance), switch the `\usepackage{neurips_2026}` line to `\usepackage[main, final]{neurips_2026}` to reveal authors.

For a non-anonymized preprint build (different from the NeurIPS submission), use the `[preprint]` option instead — that produces a version with "Preprint. Work in progress." in the footer.

## Tracks considered and not chosen

| Track | Why not |
|---|---|
| Position Paper | Empirical contribution + method; not a position piece. |
| Evaluations & Datasets | TE's contribution is the method itself; the QA-on-compressed-text methodology is a means to evaluate the method, not the contribution. |
| Creative AI | Not a creative-AI paper. |
| Workshop (single/double-blind) | Main track is appropriate; workshop submissions can come later if the main-track submission isn't accepted. |

## Page budget

| Section | Approx. pages |
|---|---|
| §1 Introduction | 1.5 |
| §2 Related Work | 0.75 |
| §3 The Telegraph English Grammar | 1.5 |
| §4 Experimental Setup (with 2 figures) | 1.5 |
| §5 Results (with 2 tables) | 1.25 |
| §6 Analysis (with 1 cost table) | 1.25 |
| §7 Implementation | 0.25 |
| §8 Limitations + §9 Conclusion | 0.75 |
| **Main body total** | **~8 / 9 max** |
| References | 0.5 |
| Appendix A: Compression as Semantic Chunking | 1.0 |
| Appendix B: Beyond Static Compression | 1.0 |
| Appendix C: Full Results Tables | 1.0 |
| Mandatory paper checklist | 7.0 |
| **Document total** | 18 |

References, appendices, and the checklist do not count against the 9-page limit.

## Submission-specific adaptations

This NeurIPS package is built from the same underlying paper content using the conference-specific format. Key differences from a generic preprint build:

| Item | NeurIPS submission |
|---|---|
| Style file | `neurips_2026.sty` |
| Page count | 18 (incl. checklist) |
| Main-body length | compressed to 8 pages |
| Bibliography | `natbib` author/year via `references.bib` |
| Sections moved to appendix | §3.6 Compression as Semantic Chunking, §6.5 Beyond Static Compression |
| Acknowledgments | omitted (per anonymization) |
| Mandatory checklist | included |
| Engine | pdflatex |

## Rebuilding

```bash
# from this directory
bash submission/build.sh
```

The build runs `pdflatex` → `bibtex` → `pdflatex` × 2 to resolve citations and cross-references. Requires MiKTeX (Windows) or TeX Live (Linux/macOS) with `pdflatex` and `bibtex` on `PATH`. The build script pre-extends `PATH` for the standard Windows MiKTeX install location.

To repackage the supplementary zip (with forward-slash paths suitable for Linux unzip):

```powershell
$d = "$PWD\submission"
Remove-Item "$d\supplementary.zip" -ErrorAction SilentlyContinue
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::Open("$d\supplementary.zip", 'Create')
foreach ($f in @(
  @('main.tex','main.tex'),
  @('references.bib','references.bib'),
  @('checklist.tex','checklist.tex'),
  @('neurips_2026.sty','neurips_2026.sty'),
  @('figures\figure1_compression_ratio.png','figures/figure1_compression_ratio.png'),
  @('figures\figure2_compression_rate.png','figures/figure2_compression_rate.png')
)) {
  [void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, "$d\$($f[0])", $f[1], 'Optimal')
}
$zip.Dispose()
```

## Source of truth and provenance

| Asset | Source | Date verified |
|---|---|---|
| `../_template_reference/neurips_2026.sty` | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` | 2026-04-29 |
| `../_template_reference/neurips_2026.tex` | (same ZIP) | 2026-04-29 |
| `../_template_reference/checklist.tex` | (same ZIP) | 2026-04-29 |
| Template last updated | `2026-03-17` (per file mtime in the official ZIP) | — |
| Call for papers | `https://neurips.cc/Conferences/2026/CallForPapers` | 2026-04-29 |
