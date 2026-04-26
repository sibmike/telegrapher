# arXiv Submission — Telegraph English

This directory holds the arXiv-ready submission package for the Telegraph English preprint. Built from `paper/telegraph_english.md` via the `arxiv-paper-prep` skill (Markdown → pandoc → xelatex → PDF → zip).

## Quick links

- **Upload artifact:** [`paper_telegraph_english/paper_telegraph_english.zip`](paper_telegraph_english/paper_telegraph_english.zip)
- **Local PDF preview:** [`paper_telegraph_english/paper_telegraph_english.pdf`](paper_telegraph_english/paper_telegraph_english.pdf)
- **arXiv rules snapshot:** [`arxiv_submission_guidelines.md`](arxiv_submission_guidelines.md)

## Submission metadata

Copy these into the arXiv submission form verbatim.

| Field | Value |
|---|---|
| **Title** | Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting |
| **Authors** | Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei |
| **Affiliations** | Independent Researchers |
| **Primary category** | `cs.CL` (Computation and Language) |
| **Cross-list categories** | `cs.AI`, `cs.LG` |
| **License** | **CC-BY-SA-4.0** (matches the repo's `LICENSE-docs`) |
| **MSC class** | (leave blank) |
| **ACM class** | (leave blank) |
| **Comments** | "15 pages, 2 figures. Code: https://github.com/sibmike/telegrapher . Reference implementation under MIT, benchmark data under CC0, paper text and grammar specification under CC-BY-SA-4.0." |
| **Assigned arXiv ID** | _(fill in after submission)_ |
| **Submission date** | _(fill in after submission)_ |

### Abstract (paste-ready, plain text)

arXiv renders the abstract field as plain text — strip Markdown emphasis before pasting. The version below is already cleaned.

> We introduce Telegraph English (TE), a compression protocol that rewrites natural-language text into a symbol-rich, formally-structured format. Where token-deletion methods like LLMLingua-2 train a classifier to remove low-information tokens at a fixed ratio, TE performs a full semantic rewrite: decomposing text into atomic fact lines, substituting verbose phrases with ~40 logical and relational symbols, and letting the compression ratio adapt to each document's information density.
>
> A consequence of this design — one we did not initially set out to achieve — is that compression and semantic chunking collapse into a single operation. Each output line is an independently addressable fact, which means the compressed representation is simultaneously a semantic index. Individual lines can be retained at full fidelity, reduced to headings, updated with new information, or pruned when they become redundant. The expensive LLM rewrite happens once; everything after that is string manipulation.
>
> We evaluate TE on 4,081 question-answer pairs from LongBench-v2 across five OpenAI models and two difficulty levels. At roughly 50% token reduction, TE preserves 99.1% accuracy on key facts with GPT-4.1 and outperforms LLMLingua-2 at matched compression ratios on every model and task tested. The gap widens on smaller models — up to 11 percentage points on fine-detail tasks — suggesting that explicit relational structure compensates for limited model capacity. We release the grammar specification (CC-BY-SA 4.0), compression prompt, benchmark data, and a reference implementation (MIT License).

## Pre-submission checklist

Build verification (already passed):

- [x] `paper_telegraph_english.pdf` builds via `bash paper_telegraph_english/build.sh`
- [x] PDF has 15 pages, ~170 KB, valid metadata (Title + Author present in `pdfinfo`)
- [x] Title page renders once (no duplicate title/author block)
- [x] Authors render as: "Mikhail L. Arbuzov  Alexey A. Shvets  Sisong Bei"
- [x] No draft disclaimers anywhere in the PDF
- [x] Figures 1–2 render with histograms and clean captions in §4.2
- [x] Unicode operators (→ ⇒ ∴ ∵ ↑ ↓ ∧ ∨ ¬ ≈ ≠) render correctly via Cambria + Consolas (visually verified — pdftotext extraction drops them but the rendered glyphs are present)
- [x] All tables render via longtable (Symbol Vocabulary, Models, Tables 1–2, Pipeline-Level Cost, Tables A1–A4)
- [x] References section renders (12 entries)
- [x] No `??` cross-reference placeholders
- [x] Filename audit: every file matches `^[a-zA-Z0-9_./+-]+$`
- [x] Zip uses forward-slash entries (Linux-friendly): `figures/figure1_compression_ratio.png`, `figures/figure2_compression_rate.png`, `paper_telegraph_english.tex`
- [x] Zip is 47 KB — well under arXiv limits

Submission-time checks (do these in the arXiv UI):

- [ ] arXiv preview PDF matches local PDF (no font fallback differences, all symbols intact)
- [ ] Abstract pasted as plain text (Markdown stripped)
- [ ] License set to **CC-BY-SA-4.0**
- [ ] Primary category cs.CL, cross-lists cs.AI and cs.LG selected
- [ ] Comments field populated per the metadata table above
- [ ] All authors confirmed; ORCID added if available

Post-announcement:

- [ ] Record the assigned arXiv ID in the metadata table above
- [ ] Optional: update the comments field via the "Replace" flow once the next paper in the series gets an ID

## Submission procedure

1. Log in at <https://arxiv.org/user/>.
2. Start a new submission, source format **TeX/LaTeX**.
3. Upload `paper_telegraph_english/paper_telegraph_english.zip`.
4. Wait for arXiv's auto-compilation; download the preview PDF.
5. Diff the preview against the local PDF (`paper_telegraph_english/paper_telegraph_english.pdf`). Pay particular attention to:
   - The Unicode logical operators in §3.2 — if arXiv falls back to a font without arrow coverage you may see `□` boxes; remediate by adding the font to the upload (unlikely with Cambria, since arXiv supports common Microsoft fonts).
   - Figure placement and caption text.
   - Tables — long ones may break across pages differently than locally.
6. Fill in the metadata fields from the table above.
7. Pick license: **CC-BY-SA-4.0**.
8. Accept arXiv's submission agreement and submit.
9. Record the assigned arXiv ID here once announced.

Submissions made before 14:00 US Eastern (Mon–Fri) announce at 20:00 the same day. Later submissions roll to the next announcement.

## Rebuilding

If `paper/telegraph_english.md` changes, regenerate the package. Always rebuild the cleaned arXiv source from the canonical `paper/` copy — don't drift the two:

```bash
# from repo root
cp paper/telegraph_english.md arxiv/paper_telegraph_english/paper_telegraph_english.md
# re-apply YAML front-matter and figure embeds (manual diff against the
# previous arxiv/ copy, or re-run the arxiv-paper-prep skill)
bash arxiv/paper_telegraph_english/build.sh
```

Then repackage the zip with forward-slash entries — PowerShell's `Compress-Archive` writes backslash entry names that break arXiv's Linux unzip:

```powershell
$d = "$PWD\arxiv\paper_telegraph_english"
Remove-Item "$d\paper_telegraph_english.zip" -ErrorAction SilentlyContinue
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::Open("$d\paper_telegraph_english.zip", 'Create')
[void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, "$d\paper_telegraph_english.tex", 'paper_telegraph_english.tex', 'Optimal')
[void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, "$d\figures\figure1_compression_ratio.png", 'figures/figure1_compression_ratio.png', 'Optimal')
[void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, "$d\figures\figure2_compression_rate.png", 'figures/figure2_compression_rate.png', 'Optimal')
$zip.Dispose()
```

On Linux/macOS the regular `cd arxiv/paper_telegraph_english && zip -r paper_telegraph_english.zip paper_telegraph_english.tex figures/` works.

## Editorial notes

- §4.5 now includes a clarifying paragraph documenting which model subset runs which evaluation suite, and notes that the fine-tuned GPT-4o variant is used as a sanity check rather than a separate accuracy benchmark. This addresses the earlier "five-vs-three-vs-two models" inconsistency between abstract, §4.5, and the results tables.
- The paper has been through a style-guide pass (`telegrapher_paper_style_guide.md`) and the final-pass checklist (`telegrapher_final_pass_checklist.md`) for human-texture interventions before this build. Future revisions should re-run both passes after substantive content edits.
