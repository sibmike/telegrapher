# NeurIPS 2026 Submission — Beyond Exponential Decay

This directory holds the NeurIPS 2026 main-track submission package for **"Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models."** The arXiv preprint version (non-anonymous) lives in [`../../arxiv/beyond exponential decay/`](../../arxiv/beyond%20exponential%20decay/); this directory holds the anonymized version formatted with `neurips_2026.sty` for double-blind review.

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
| **Title** | Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models |
| **Authors** | Anonymous (revealed in camera-ready as Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei) |
| **Primary subject area** | Theory / Long-context Modeling |
| **Page count** | 15 pages total: 6 pages main body + references + 2-page appendix + 7-page mandatory checklist |
| **Main-body limit** | 9 content pages — we use 6 |
| **Submission portal** | OpenReview (`NeurIPS.cc/2026/Conference`) |

### Key deadlines (shared with sibling papers)

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
- [x] Main body fits in 6 pages (under the 9-page limit; references begin on p. 6)
- [x] References render with author/year style (`natbib` default, `plainnat`)
- [x] Table 1 (framework→exemplar mapping) renders via `booktabs` in Appendix B
- [x] All three core equations render correctly: two-rate model (Eq. 1), union-bound disruptive-error inequality (Eq. 2), redundancy-gain factor (Eq. 3)
- [x] Mandatory paper checklist filled with paper-specific answers (16 questions: 5 Yes, 11 NA — synthesis paper, no new experiments)
- [x] No author-identifying information (no funding acknowledgments, no repo URLs, no institutional affiliations, no ORCID links — `pdftotext` scan returns 0 matches for `arbuzov|shvets|sisong|orcid`)
- [x] Bibliography produced from `references.bib` via `bibtex`
- [x] No fabricated citations: 4 placeholder arXiv IDs (`2402.XXXXX`, `2404.XXXXX`, `2312.XXXXX`) audited; one resolved to a real paper, three dropped (see Editorial flags)

Submission-time checks (do these in OpenReview):

- [ ] Upload `submission/main.pdf` as the paper
- [ ] Optionally upload `submission/supplementary.zip` as supplementary material
- [ ] Confirm anonymized author information on the OpenReview metadata form
- [ ] Select Main Track
- [ ] Set primary subject area (Theory or Long-context Modeling); cross-list as appropriate
- [ ] Disclose conflicts of interest

Post-submission:

- [ ] Record the OpenReview submission ID once assigned

## Anonymization notes

The paper has been anonymized for double-blind review:

1. **Author block**: `Anonymous Author(s) / Affiliation / Address / email` (no real names).
2. **ORCID links and `orcid.pdf` icon**: removed from author block.
3. **`\hypersetup{pdfauthor=...}` and `pdftitle=...`**: dropped from preamble; PDF metadata is empty rather than identifying.
4. **`\renewcommand{\shorttitle}{...}`** and **`\keywords{...}`**: removed (not used by NeurIPS template).
5. **First-person framing**: paper uses "we" only as authorial voice; no self-citations of prior work.
6. **Repository URL**: not referenced. The arXiv preprint URL and any code URL will be added to the camera-ready version.
7. **Acknowledgments**: omitted from the anonymized submission; will be added at camera-ready under `\begin{ack} ... \end{ack}` (auto-suppressed by `neurips_2026.sty` outside `[final]` mode).

When preparing the camera-ready (after acceptance), switch the `\usepackage{neurips_2026}` line to `\usepackage[main, final]{neurips_2026}` to reveal authors.

## Page budget

| Section | Approx. pages |
|---|---|
| §1 Introduction | 1.0 |
| §2 Related Work (4 `\paragraph{}` blocks) | 0.75 |
| §3 Theoretical Framework (two-rate model, manifold dynamics, redundancy gain) | 1.5 |
| §4 Empirical Evidence (3 subsections) | 1.25 |
| §5 Practical Implications (4 `\paragraph{}` blocks) | 1.0 |
| §6 Limitations | 0.25 |
| §7 Conclusion | 0.75 |
| **Main body total** | **~6 / 9 max** |
| References | 0.75 |
| Appendix A: Architectural Implications: Modular Reasoning | 0.5 |
| Appendix B: Extended Case Studies (incl. Table 1) | 1.5 |
| Mandatory paper checklist | 7.0 |
| **Document total** | 15 |

References, appendices, and the checklist do not count against the 9-page limit. We have 3 pages of slack under the cap, which is comfortable.

## Differences from the arXiv version (`../../arxiv/beyond exponential decay/`)

| Item | arXiv preprint | NeurIPS submission |
|---|---|---|
| Format | `arxiv.sty` (single-column, custom) | `neurips_2026.sty` |
| Authors visible | Yes (Arbuzov, Shvets, Bei) | No (Anonymous) |
| ORCID block | Yes (with `orcid.pdf` icons) | Removed |
| Page count | 16 | 15 (incl. checklist) |
| Main-body length | 14 pages, no cap | compressed to 6 pages |
| Bibliography | `unsrtnat` numeric | `plainnat` author/year via `references.bib` |
| Sections moved to appendix | none | §4.4 "Integrated Evidence" → Appendix B; §5.5 "Modular Reasoning Architecture" → Appendix A |
| Limitations | brief mention in Conclusion | dedicated §6 Limitations section |
| Acknowledgments | n/a | omitted (per anonymization) |
| Mandatory checklist | n/a | included |
| Citations | 33 entries; 4 placeholder arXiv IDs | 30 entries; placeholders resolved or dropped |
| Engine | xelatex (via arxiv.sty) | pdflatex |
| License | (preprint) | NeurIPS submission terms |

## Style and humanization passes

The compressed prose has been through three editorial passes:

1. **Pass 1: page-budget compression** — moved §4.4 and §5.5 to appendix, compressed §2 and §5 to `\paragraph{}` blocks, inlined enumerate lists, dropped bridge sentences.
2. **Pass 2: telegrapher style guide** (`telegrapher_paper_style_guide.md`) — mechanism over capability; one claim per paragraph; comparisons over absolutes in prose; voice precise/dry, never breathless. Audit: 0 occurrences of `remarkably / dramatically / compelling evidence / perhaps most convincingly / the remainder of this paper / having established / we now turn to`.
3. **Pass 3: humanization** (`telegrapher_final_pass_checklist.md`) — vary clause architecture (T1), asymmetric hedging (T3), register micro-shifts (T5), uneven paragraph density (T7), vocabulary burstiness (C1: "brittle", "lopsided", "stubborn"), punctuation texture (C2), sentence-opening variation (C3), citation integration variety (C4).

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
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::Open("$d\supplementary.zip", 'Create')
foreach ($f in @('main.tex','references.bib','checklist.tex','neurips_2026.sty')) {
  [void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, "$d\$f", $f, 'Optimal')
}
$zip.Dispose()
```

## Editorial flags (post-build, for camera-ready review)

1. **Citations resolved during preparation.** The arXiv source had four entries with `XXXXX` arXiv-ID placeholders. We audited each:
   - `wu2024tokenselect` → resolved to the real paper at `arXiv:2411.02886` (Wu et al., 2024).
   - `lin2024dynamic` → no matching paper found; replaced with `zhu2024hotorcold` (`arXiv:2309.02772`, AAAI 2024) which makes the same architectural point about adaptive temperature decoding.
   - `nistar2024token` → no matching paper found; citation dropped from §5 (Evaluation) and Table 1; the success-plateau reference now relies on `costello2025think` alone.
   - `si2023mixture` ("Mixture of Reasoning Experts / MoRE") → no matching paper found; the Appendix A modular-architecture argument was rewritten to depend only on `costello2025think`'s alignment-not-scale results, with the routing question framed as open.

2. **Non-arXiv citations.** Two entries (`nvidia2023scaling`, NVIDIA Tech Blog; `venture2025test`, "Technology Research Report") cite non-peer-reviewed sources for the small-model-with-test-time-compute-beats-large-model claim. These were already in the arXiv source and we kept them in Appendix B. Reviewers may flag them; consider replacing with a peer-reviewed equivalent at camera-ready.

3. **Punchier closing line.** The arXiv version ended §5 with "*The exponential decay hypothesis is dead.*" The NeurIPS Conclusion uses a cooler register (per the telegrapher style guide); if reviewers respond well to declarative closes, consider restoring the punchier line at camera-ready.

4. **Table 1 location.** The framework→exemplar mapping table is in Appendix B. Some reviewers prefer such tables in the main body; main-body §5 already covers each row in prose.

## Source of truth and provenance

| Asset | Source | Date verified |
|---|---|---|
| `../_template_reference/neurips_2026.sty` | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` | 2026-04-29 |
| `../_template_reference/checklist.tex` | (same ZIP) | 2026-04-29 |
| Template last updated | `2026-03-17` (per file mtime in the official ZIP) | — |
| Call for papers | `https://neurips.cc/Conferences/2026/CallForPapers` | 2026-05-02 |
| `wu2024tokenselect` real arXiv ID | `https://arxiv.org/abs/2411.02886` | 2026-05-02 |
| `zhu2024hotorcold` real arXiv ID | `https://arxiv.org/abs/2309.02772` | 2026-05-02 |
