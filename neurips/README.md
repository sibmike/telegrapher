# NeurIPS 2026 Submissions

This directory holds NeurIPS 2026 main-track submission packages for papers from this repo. Each paper lives in its own `paper_<slug>/` subfolder; the official template is shared across all papers in `_template_reference/`.

## Papers

| Paper | Folder | Status |
|---|---|---|
| Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting | [`paper_telegraph_english/`](paper_telegraph_english/) | Built; ready to upload |
| Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models | [`paper_beyond_exponential_decay/`](paper_beyond_exponential_decay/) | Built; ready to upload |

Each paper folder contains its own `README.md` (submission metadata, anonymization notes, page-budget table, rebuild instructions) and a `submission/` directory holding the upload artifacts.

## Shared deadlines (NeurIPS 2026 main track)

| Milestone | Date (AOE) |
|---|---|
| **Abstract submission** | May 4, 2026 |
| **Full paper submission** | May 6, 2026 |
| Author notification | September 24, 2026 |

Verified against `https://neurips.cc/Conferences/2026/CallForPapers` on 2026-05-02.

## Shared template

`_template_reference/` holds the unmodified official NeurIPS 2026 formatting bundle. All paper subfolders copy `neurips_2026.sty` into their own `submission/` directory so each build is self-contained, but treat `_template_reference/` as the source of truth for any future paper added here.

| Asset | Source | Date verified |
|---|---|---|
| `_template_reference/neurips_2026.sty` | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` | 2026-04-29 |
| `_template_reference/neurips_2026.tex` | (same ZIP) | 2026-04-29 |
| `_template_reference/checklist.tex` | (same ZIP) | 2026-04-29 |
| Template last updated | `2026-03-17` (per file mtime in the official ZIP) | — |
| Call for papers | `https://neurips.cc/Conferences/2026/CallForPapers` | 2026-05-02 |

## Adding a new paper

1. `mkdir paper_<slug>/submission`
2. Copy `_template_reference/neurips_2026.sty` and `_template_reference/checklist.tex` into `paper_<slug>/submission/`.
3. Write `main.tex` against the proven preamble (see `paper_telegraph_english/submission/main.tex` for a working example).
4. Adapt `paper_telegraph_english/submission/build.sh` (project-agnostic; no edits typically needed).
5. Write `paper_<slug>/README.md` modeled on the existing per-paper README.
6. Add the new paper to the table at the top of this file.
