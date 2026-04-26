# arXiv Submission Guidelines — Local Snapshot

Captured from <https://info.arxiv.org/help/submit/index.html> per the `arxiv-paper-prep` skill (Step 1). Re-fetch and update if more than a few months stale — arXiv's rules drift.

This is a project-local reference so future submissions don't need to re-fetch the upstream docs. The 12 points below cover the practical surface of what arXiv accepts and rejects.

---

## 1. Accepted source formats (preferred order)

1. **(La)TeX** — strongly preferred. arXiv auto-compiles. Markdown is *not* accepted; convert via pandoc.
2. **PDF** — accepted but discouraged for new submissions. Loses the source-distribution benefit.
3. **HTML** — accepted in limited circumstances; generally avoid.

For this project: source lives in Markdown (`paper/telegraph_english.md`), gets converted via `pandoc → xelatex → PDF`, and the `.tex` (with bundled figures) is what we upload.

## 2. Figure formats

- **PDFLaTeX engine**: accepts PNG, JPG, GIF, PDF.
- **Plain LaTeX engine**: accepts only PS / EPS.
- **XeLaTeX (what we use)**: accepts PNG, JPG, PDF.

arXiv does **not** auto-convert image formats. Bundle figures in a format your engine accepts.

## 3. Filename rules (case-sensitive)

- Allowed characters only: `a-z A-Z 0-9 _ + - . , =`
- **No spaces.** No Unicode. No parentheses.
- Lowercase preferred (avoids cross-OS case-sensitivity bugs).
- Suggested pattern: `figureN_short_label.png`.

## 4. Figures must be bundled

arXiv rejects submissions that reference figures by URL or that omit them. Every `\includegraphics{...}` path must resolve inside the uploaded archive. Relative paths only — absolute paths are an instant rejection.

## 5. Packaging

- Format: ZIP or TAR.GZ, preserving relative paths with **forward slashes** (Linux convention). Windows PowerShell's `Compress-Archive` writes backslash entries which break on arXiv's Linux processor — use `.NET ZipArchive` with explicit forward-slash entry names instead.
- arXiv auto-detects the file containing `\documentclass` as the main `.tex`.
- Include `.bib`, `.sty`, `.cls`, and any custom packages alongside the `.tex`.

## 6. Required submission metadata

- Title (plain text, no LaTeX).
- Abstract (plain text — arXiv strips Markdown / LaTeX from this field).
- Authors with affiliations.
- Primary subject category + optional cross-lists.
- License selection.
- Acceptance of arXiv's submission agreement.

## 7. License options

| Option | Use when |
|---|---|
| arXiv non-exclusive | Default. You retain all rights; arXiv just gets distribution. Most restrictive of the four. |
| CC-BY-4.0 | Standard permissive choice. Allows reuse with attribution. |
| **CC-BY-SA-4.0** (this paper) | Share-alike: derivatives must use the same license. Matches the repo's `LICENSE-docs`, which already declares `paper/` content as CC-BY-SA-4.0. |
| CC-BY-NC-SA-4.0 | Non-commercial + share-alike. Restrictive; uncommon. |
| CC0 | Public domain dedication. Fewest restrictions on reusers. |

Match the repo's existing `LICENSE-docs` where possible.

## 8. Endorsement

First-time submitters to a category may need endorsement from an existing author in that category. Endorsement requests are emailed and usually clear within a day or two. cs.* categories are commonly auto-endorsed for active arXiv users.

## 9. Common rejection causes

- Missing figures (referenced but not bundled).
- Filename case mismatch between `\includegraphics` and the actual file.
- Spaces or non-ASCII in filenames.
- Absolute paths in `\includegraphics`.
- Mixing PS/EPS with PNG/PDF figures (engine mismatch).
- Pandoc run without `--standalone` → no `\documentclass` → "no top-level TeX file" error.
- Unicode in source compiled with pdflatex without `\DeclareUnicodeCharacter` declarations → use xelatex instead.
- Missing `.sty` for custom packages.
- ZIP entries with Windows backslashes — Linux unzip treats the whole thing as a single filename.

## 10. Timing

- Submissions by **14:00 US Eastern** (Mon–Fri) announce at **20:00** the same day.
- Later submissions roll to the next announcement window.
- arXiv has no holidays except major US public holidays.

## 11. Replacements

Post-announcement corrections use the **"Replace"** flow on the original arXiv ID. Never submit a new entry to fix a typo — that creates an orphaned record. Replacements preserve the arXiv ID; only the version number increments (`v2`, `v3`, …).

## 12. Series linkage

arXiv has no formal "series" or "supersedes" metadata. Link related papers via:
- The `comments` field on each submission (e.g. "Companion paper: arXiv:XXXX.XXXXX").
- In-paper references after IDs are assigned — submit in dependency order so later papers can cite earlier IDs.

---

## Engine choice for this project

We use **xelatex** (not pdflatex) because §3.2's symbol vocabulary table contains Unicode logical operators (→, ∴, ∧, ∨, ¬, ≈, ≠, ↑, ↓, ⇒). XeLaTeX handles Unicode natively via `fontspec`; pdflatex would require a `\DeclareUnicodeCharacter` declaration per glyph.

`build.sh` sets `mainfont=Cambria` and `monofont=Consolas` because Latin Modern (the default) lacks coverage of the arrow and logical-operator Unicode blocks. Cambria and Consolas both ship with Windows; on Linux/macOS substitute DejaVu Serif / DejaVu Sans Mono or any Unicode-capable serif/mono pair.

## Quick mental model

1. Read these rules → write a snapshot once → reference locally.
2. For each paper: copy source → embed figures → strip drafts → build → eyeball PDF → zip.
3. For each submission: log in → upload zip → fill metadata → record assigned ID.
