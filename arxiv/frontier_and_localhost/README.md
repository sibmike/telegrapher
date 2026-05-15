# arXiv Submission — Frontier and Localhost (Part 3)

Follow-on to *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)) and *The Architecture of Errors* (Part 2, forthcoming).

Built from `paper_frontier_and_localhost.md` via the `arxiv-paper-prep` skill (Markdown → pandoc → xelatex → PDF → zip).

## Quick links

- **Upload artifact:** [`paper_frontier_and_localhost.zip`](paper_frontier_and_localhost.zip)
- **Local PDF preview:** [`paper_frontier_and_localhost.pdf`](paper_frontier_and_localhost.pdf)
- **Source Markdown:** [`paper_frontier_and_localhost.md`](paper_frontier_and_localhost.md)
- **arXiv rules snapshot:** [`../arxiv_submission_guidelines.md`](../arxiv_submission_guidelines.md)

## Submission metadata

Copy these into the arXiv submission form verbatim.

| Field | Value |
|---|---|
| **Title** | Frontier and Localhost: How Production AI Learns Outside the Weights |
| **Authors** | Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei |
| **Affiliations** | Independent Researchers |
| **Primary category** | `cs.AI` (Artificial Intelligence) |
| **Cross-list categories** | `cs.LG` (Machine Learning), `cs.SE` (Software Engineering) |
| **License** | **CC-BY-4.0** |
| **MSC class** | (leave blank) |
| **ACM class** | (leave blank) |
| **Comments** | "19 pages, no figures. Survey of 142 production and research LLM systems (2023–2026). Part 3 in the series following arXiv:2505.24187 and *The Architecture of Errors* (Part 2). A practitioner-facing companion paper covering reference architectures, maturity ladders, design principles, and the full failure taxonomy is forthcoming." |
| **Assigned arXiv ID** | _(fill in after submission)_ |
| **Submission date** | _(fill in after submission)_ |

> **Note on primary category.** The earlier two papers in this series went under `cs.CL` because their core was language processing (compression in Part 1's TE; reliability of language generation in Part 2). Part 3's core is the *systems and architectures* built around language models, not language processing itself — `cs.AI` fits the substance better. If you prefer continuity with the series, swap primary to `cs.CL` and cross-list `cs.AI` first.

### Abstract (paste-ready, plain text)

arXiv renders the abstract field as plain text — strip Markdown emphasis before pasting. The version below is already cleaned.

> Reliability has moved from the weights to the scaffold. Surveying production and research LLM systems from 2023-2026, we show that practitioners repeatedly wrap frozen frontier models in local, persistent, feedback-updated artifacts: instructions, skills, memories, tools, orchestration graphs, and governance pipelines. We argue that these artifacts form a deployment-time learning layer — a localhost scaffold — that adapts a general model to the recurring failure topology of a specific patch. We formalise this as artifact-layer descent: failures provide noisy loss signals, candidate scaffold deltas are generated, gates accept or reject them, accepted deltas persist and may be promoted across contexts. The resulting two-loop architecture explains the convergence of modern agent systems across IDE plugins, vertical-bundle vendors, and self-evolving research agents, and it reveals an unfilled design corner: automated local scaffold evolution combined with governed, auditable, cross-organisation promotion — a DP-FedAvg-style aggregator with an automated eval gate at the scaffold layer. The contribution is conceptual and survey-based. A practitioner-facing companion paper will handle reference architectures, maturity ladders, design principles, and the full failure taxonomy.

## Pre-submission checklist

Build verification:

- [x] `paper_frontier_and_localhost.pdf` builds via `bash build.sh`
- [x] PDF generated (~178 KB, 19 pages)
- [x] Title and Author metadata present (`pdfinfo` reports Title: *Frontier and Localhost…*, Author: *Mikhail L. Arbuzov; Alexey A. Shvets; Sisong Bei*)
- [x] Title page renders once (no duplicate title/author block)
- [x] No draft disclaimers anywhere in the PDF
- [x] No figures (survey paper)
- [x] Greek and special characters render correctly via Cambria + `mainfontoptions="Ligatures=TeX"` (the latter prevents Cambria's `fi`-ligature from rendering as a Greek beta variant)
- [x] **§3.2 The mechanism made formal** renders: ten display equations, thirteen-row Optimization↔Scaffold table, all inline math
- [x] **§9.1 patch-completeness clarifier** renders: three-paragraph insert reframing production "general intelligence" as patch-completeness; "AGI" appears exactly once, used to dismiss it as the wrong first unit
- [x] **Conclusion sentence** "Practical generality therefore arrives locally first…" renders as opener of the final paragraph
- [x] All five longtables (§4 substrates, §6.1 maturity, §6.2 clusters, §3.2 optimization↔scaffold, §8 3×3 matrix) render with proper column widths — no single-word wraps
- [x] Appendix A 30-row table renders at `\small` font; URL cells (OpenCore, Cursor Rules, Anthropic Agent Skills, LangSmith Hub) break cleanly via `xurl`
- [x] `\$3.5B` in the Hippocratic AI row renders literally (was previously opening an unbalanced math mode)
- [x] References section renders (~60 entries)
- [x] No `??` cross-reference placeholders
- [x] Filename audit: every file matches `^[a-zA-Z0-9_./+-]+$`
- [x] Zip uses forward-slash entries (Linux-friendly): `paper_frontier_and_localhost.tex`
- [x] Zip is ~30 KB — well under arXiv limits

Submission-time checks (do these in the arXiv UI):

- [ ] arXiv preview PDF matches local PDF (table widths preserved, no font-fallback artifacts)
- [ ] Abstract pasted as plain text (em-dashes preserved; markdown emphasis stripped)
- [ ] License set to **CC-BY-4.0**
- [ ] Primary category `cs.AI`, cross-lists `cs.LG` and `cs.SE` selected (or override per the note above)
- [ ] Comments field populated per the metadata table
- [ ] All authors confirmed; ORCID added if available

Post-announcement:

- [ ] Record the assigned arXiv ID in the metadata table above
- [ ] Update Part 1 and Part 2 arXiv comments via "Replace" flow to add the Part 3 arXiv ID (optional but useful for series linkage)

## Submission procedure

1. Log in at <https://arxiv.org/user/>.
2. Start a new submission, source format **TeX/LaTeX**.
3. Upload `paper_frontier_and_localhost.zip`.
4. Wait for arXiv's auto-compilation; download the preview PDF.
5. Diff the preview against the local PDF. Pay particular attention to:
   - **Table column widths** — five longtables use proportional separator-dash counts in the Markdown to drive column widths; arXiv's pandoc/xelatex chain should reproduce the local rendering exactly, but verify §6.1 (Survey-finding column dominant), §6.2 (What-the-cluster-proves dominant), and Appendix A (Why-included dominant at `\small`).
   - **URL line-breaks** — Appendix A wraps four bare URLs in `\url{…}` and loads `xurl` for arbitrary breakpoints; confirm no Evidence/Why-included overlap.
   - **Math rendering** — §3.2's ten display equations and the cases-environment update rule.
6. Fill in the metadata fields from the table above.
7. Pick license: **CC-BY-4.0**.
8. Accept arXiv's submission agreement and submit.
9. Record the assigned arXiv ID here once announced.

Submissions made before 14:00 US Eastern (Mon–Fri) announce at 20:00 the same day. Later submissions roll to the next announcement.

## Series linkage

This is **Part 3** of a planned series:

- **Part 1**: *Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models* — [arXiv:2505.24187](https://arxiv.org/abs/2505.24187).
- **Part 2**: *The Architecture of Errors: Logarithmic Mode Discovery and Polylogarithmic Intervention Budgets for Long-Context LLM Reliability* — preprint forthcoming, see [`../architecture_of_errors/`](../architecture_of_errors/).
- **Part 3** (this paper): *Frontier and Localhost: How Production AI Learns Outside the Weights* — survey + formal framework for scaffold-as-parameter-vector.
- **Part 4** (planned, practitioner-facing): reference architectures, maturity ladders, design principles, and the full nine-category failure taxonomy referenced in §10.

arXiv has no formal series metadata; series linkage is maintained via the `comments` field and in-paper references.

## Rebuilding

If `paper_frontier_and_localhost.md` changes:

```bash
bash build.sh
```

Then repackage the zip. On Linux/macOS or Git Bash on Windows:

```bash
cd "$(dirname build.sh)"
rm -f paper_frontier_and_localhost.zip
zip paper_frontier_and_localhost.zip paper_frontier_and_localhost.tex
```

On native PowerShell, use `[System.IO.Compression.ZipFile]::Open(...)` with explicit forward-slash entry names (see Part 1's `arxiv/README.md` for the exact incantation). Default `Compress-Archive` writes backslash entries that break arXiv's Linux unzip.

## Editorial notes

- **§3.2 The mechanism made formal: scaffold updates as discrete stochastic descent** (added this revision). Strengthens §3/§3.1's `S_{t+1} = S_t + G(\Delta S)` rule by locating scaffold evolution in the correct optimization class — discrete, gated, patch-local stochastic descent over a structured artifact space. Defines patch loss $L_D(\theta_s)$, the candidate-edit proposal process $z_t \sim Q_t(z \mid H_t)$, the finite directional loss change $\Delta_z L_D(\theta_s)$ as the gradient analogue, the gate acceptance condition with complexity penalty and threshold, and the convergence statement to a local $G$-stable scaffold under bounded loss and positive gate descent bias. Includes a thirteen-row standard-optimization ↔ scaffold-analogue correspondence table and four concrete cases (RAG, pitch-review, tool-using agent, memory system) that walk the mechanism end-to-end.
- **§9.1 patch-completeness clarifier** (added this revision). Three paragraphs reframing what many production deployments experience as "general intelligence" as patch-completeness — language-mediated local function approximation over a bounded patch, with the scaffold supplying the patch-specific feature engineering, memory, tools, rules, and loss surface. The manuscript mentions "AGI" exactly once, to argue it is the wrong first unit for production systems. The punchier private framing ("AGI is a patch-specific NLP LightGBM in disguise") is intentionally not in the paper.
- **Conclusion** (added this revision). One sentence inserted before the existing triplet *"The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation."* The new opener is: *"Practical generality therefore arrives locally first: not as a universal mind, but as patch-complete model–scaffold systems whose competence is fitted to bounded worlds."*
- **Table rendering fixes** (commit `9abea92`, prior revision). Five longtables had columns collapsed to single-word wraps because pandoc derives pipe-table column widths from the character count of each separator-row cell (dashes plus alignment colons). The fix encodes desired proportions in the separator dashes for §6.1, §6.2, and Appendix A; the Appendix table is additionally wrapped in `\begingroup\small` and four long bare URLs are wrapped in `\url{…}` with `xurl` loaded via YAML `header-includes`. A stray unescaped `$3.5B` in the Hippocratic AI row, which previously opened a math-mode escape that swallowed three subsequent rows, was escaped to `\$3.5B`.
- The paper has been through the style-guide pass ([`telegrapher_paper_style_guide.md`](../../../telegrapher_ai/texts/telegrapher_paper_style_guide.md)) and the final-pass checklist ([`telegrapher_final_pass_checklist.md`](../../../telegrapher_ai/texts/telegrapher_final_pass_checklist.md)) for human-texture interventions. The new §3.2, §9.1 inserts, and conclusion sentence were calibrated to the paper's voice at draft time; the post-insertion review found no further edits required.
