# arXiv Submission — The Architecture of Errors (Part 2)

Follow-on to *Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)).

Built from `paper_architecture_of_errors.md` via the `arxiv-paper-prep` skill (Markdown → pandoc → xelatex → PDF → zip).

## Quick links

- **Upload artifact:** [`paper_architecture_of_errors.zip`](paper_architecture_of_errors.zip)
- **Local PDF preview:** [`paper_architecture_of_errors.pdf`](paper_architecture_of_errors.pdf)
- **Source Markdown:** [`paper_architecture_of_errors.md`](paper_architecture_of_errors.md)
- **arXiv rules snapshot:** [`../arxiv_submission_guidelines.md`](../arxiv_submission_guidelines.md)

## Submission metadata

Copy these into the arXiv submission form verbatim.

| Field | Value |
|---|---|
| **Title** | The Architecture of Errors: Logarithmic Mode Discovery and Polylogarithmic Intervention Budgets for Long-Context LLM Reliability |
| **Authors** | Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei |
| **Affiliations** | Independent Researchers |
| **Primary category** | `cs.CL` (Computation and Language) |
| **Cross-list categories** | `cs.AI`, `cs.LG` |
| **License** | **CC-BY-4.0** |
| **MSC class** | (leave blank) |
| **ACM class** | (leave blank) |
| **Comments** | "Follow-on to arXiv:2505.24187. No figures; pure synthesis paper drawing on approximately sixty prior published results." |
| **Assigned arXiv ID** | _(fill in after submission)_ |
| **Submission date** | _(fill in after submission)_ |

### Abstract (paste-ready, plain text)

arXiv renders the abstract field as plain text — strip Markdown emphasis and inline LaTeX math before pasting. The version below is already cleaned.

> Our previous work (arXiv:2505.24187) argued that LLM reliability does not decay exponentially with output length because errors concentrate at sparse "key tokens" rather than spreading uniformly across the sequence. This paper extends that framework along an orthogonal axis. We observe that LLM errors are not only sparse but also repetitive: the same handful of failure patterns recur across models, datasets, and domains. We formalise this as a three-layer architecture — key-token sparsity (alpha approx 0.05–0.10), hard-fraction stratification within key tokens (beta approx 0.2–0.5), and a finite catalogue of recurring failure modes whose count grows slowly with the number of observed failures — and derive its consequences for intervention design. Under an empirical postulate of logarithmic mode discovery, anchored by the ErrorAtlas taxonomy (83 models x 35 datasets), the number of distinct interventions needed to bound per-hard-token residual error scales polylogarithmically in sequence length. We show that approximately fifty targeted interventions per domain — one per recurring pattern — suffice to reduce per-hard-token error by an order of magnitude, and we collect quantitative evidence from twelve intervention categories supporting this prediction. We carefully separate per-hard-token bounds from sequence-level reliability targets (the latter is strictly tighter), and we re-audit prominent counter-evidence (Faith and Fate, BABILong, METR) to show that observed steep decay curves are over variables distinct from raw token length. This reframing positions LLM reliability as a small-catalogue problem: bounded structurally rather than tamed asymptotically.

## Pre-submission checklist

Build verification (Phase 7 directional-honesty pass):

- [x] `paper_architecture_of_errors.pdf` builds via `bash build.sh`
- [x] PDF generated (~199 KB, 23 pages of body + references)
- [x] Title page renders once (no duplicate title/author block)
- [x] Authors render as: "Mikhail L. Arbuzov  Alexey A. Shvets  Sisong Bei"
- [x] No draft disclaimers anywhere in the PDF
- [x] No figures (synthesis paper)
- [x] Greek letters (α, β, σ, ε, Θ) render correctly via Cambria
- [x] All inline math `$...$` and display math `$$...$$` render correctly
- [x] **New §3.0 four-level glossary** (L1 events / L2 taxonomy / L3 latent modes / L4 capabilities) renders
- [x] **Theorem 1 → Proposition 1** rename consistent throughout
- [x] **New §3.6 Heaps-sensitivity table** showing polylog conclusion under four cluster-count laws
- [x] **§4.2.0 Pattern A/B/C** retiered: only constrained-decoding and formal verifiers in Pattern A; Acurai moved to Pattern B
- [x] **§6.2 reframed** as "relocation, not dissolution" with per-paper concession sentences
- [x] **§6.3 expanded** with 5 named limitations (mathematical, domain narrowness, single-point calibration, β identifiability, taxonomy granularity, goalpost-relocation)
- [x] Summary table in §4.2 renders with "Covering axis" column
- [x] References section renders (~67 entries) with consistent (Author, Year) inline citations
- [x] No `??` cross-reference placeholders
- [x] Filename audit: every file matches `^[a-zA-Z0-9_./+-]+$`
- [x] Zip uses forward-slash entries (Linux-friendly): `paper_architecture_of_errors.tex`
- [x] Zip is ~36 KB — well under arXiv limits

Submission-time checks (do these in the arXiv UI):

- [ ] arXiv preview PDF matches local PDF (no font fallback differences, all Greek letters intact)
- [ ] Abstract pasted as plain text (Markdown stripped; LaTeX math `$alpha$` rendered as `alpha`)
- [ ] License set to **CC-BY-4.0**
- [ ] Primary category cs.CL, cross-lists cs.AI and cs.LG selected
- [ ] Comments field populated per the metadata table above, including the link to arXiv:2505.24187
- [ ] All authors confirmed; ORCID added if available

Post-announcement:

- [ ] Record the assigned arXiv ID in the metadata table above
- [ ] Update Part 1's arXiv comments via the "Replace" flow to add the Part 2 arXiv ID (optional but useful for series linkage)

## Submission procedure

1. Log in at <https://arxiv.org/user/>.
2. Start a new submission, source format **TeX/LaTeX**.
3. Upload `paper_architecture_of_errors.zip`.
4. Wait for arXiv's auto-compilation; download the preview PDF.
5. Diff the preview against the local PDF (`paper_architecture_of_errors.pdf`). Pay particular attention to:
   - Greek letters — if arXiv falls back to a font without Greek coverage you may see `□` boxes; remediate by switching the YAML or build script to `mainfont="DejaVu Serif"` and rebuilding.
   - Math rendering for Theorem 1's polylog bound expression $m \geq |C|^{1 - \varepsilon / e_{\text{hard}}}$.
   - The summary table in §4.2 — long tables may break across pages differently than locally.
6. Fill in the metadata fields from the table above.
7. Pick license: **CC-BY-4.0**.
8. Accept arXiv's submission agreement and submit.
9. Record the assigned arXiv ID here once announced.

Submissions made before 14:00 US Eastern (Mon–Fri) announce at 20:00 the same day. Later submissions roll to the next announcement.

## Series linkage

This is **Part 2** of a planned series following *Beyond Exponential Decay* ([arXiv:2505.24187](https://arxiv.org/abs/2505.24187)). Anticipated future papers in the series:

- Part 3 (planned): empirical measurement of σ on new domains; sequence-level extension of Theorem 1.
- Part 4 (planned): attention-mechanism / stratified-manifold geometric underpinnings of Postulate 1.

arXiv has no formal series metadata; series linkage is maintained via the `comments` field and in-paper references.

## Rebuilding

If `paper_architecture_of_errors.md` changes:

```bash
bash build.sh
```

Then repackage the zip. On Linux/macOS or Git Bash on Windows:

```bash
cd "$(dirname build.sh)"
rm -f paper_architecture_of_errors.zip
zip paper_architecture_of_errors.zip paper_architecture_of_errors.tex
```

On native PowerShell, use `[System.IO.Compression.ZipFile]::Open(...)` with explicit forward-slash entry names (see Part 1's `arxiv/README.md` for the exact incantation). Default `Compress-Archive` writes backslash entries that break arXiv's Linux unzip.

## Editorial notes

- **Phase 7 (directional-honesty pass)**: this version is a substantive revision responding to two rounds of reviewer feedback. Headline changes: (a) §3.0 four-level glossary distinguishes L1 events / L2 taxonomy categories / L3 latent modes / L4 capability axes; (b) Theorem 1 renamed to Proposition 1 to surface its conditional nature; (c) β reframed as a latent stratification parameter (the prior calibration from category concentration confused two conditionals); (d) §3.4 sequence-level theorem now states the `e_non = o(k/n)` assumption explicitly; (e) §3.6 sensitivity table shows the polylog conclusion is stable under four cluster-count laws (logarithmic discovery, Heaps b∈{0.3, 0.5, 0.6}, saturating exponential); (f) §6.2 reframed from "we domesticate the counter-papers" to "we relocate the practical worry, we do not dissolve it"; (g) §6.3 limitations expanded to surface domain narrowness, single-point σ calibration, β identifiability, taxonomy granularity, and goalpost-relocation explicitly.
- The Postulate 1 / Heaps' law distinction in §3.2 reflects a reviewer correction during drafting: an earlier version claimed logarithmic cluster growth followed from Zipf, which is mathematically wrong (Heaps' law is power-law). The current draft clearly labels logarithmic mode discovery as an empirical postulate, with the Heaps power-law variant included as §3.5 to demonstrate that the qualitative polylog result is robust to the choice.
- Per-hard-token vs sequence-level reliability is now distinguished explicitly in §3.4: the "~50 patterns → ~90%" claim is per-hard-token; sequence-level targets are strictly stronger.
- §4.2 has a two-tier structure as of the Phase 6 integration: §4.2.0 introduces the six capability axes and three structural patterns (A by-construction, B class-disappearance, C class-shift), with 27 GOLD citations from the parallel capability harvest; §4.2.1+ retains the original 12-cluster taxonomy with a "Covering axis" column linking the two views. The cluster-orthogonality argument is now anchored in both the axis-level and class-level evidence.
- §6 was reorganised in Phase 6 to lead with by-construction elimination (Pattern A from the capability harvest) as a strengthening boundary case of Theorem 1, followed by the counter-evidence re-audit, and closing with the irreducible-semantic residual and the DebugBench falsifiability test (capability provisioning correctly predicts both what it can and cannot erase).
- Counter-evidence (Dziri, BABILong, METR, Wan, NoCha) is re-audited in §6.2 with the unifying observation that every counter-paper decays over a variable other than raw token length.
- The internal working files used to compile this paper live in `internal/error_architecture/` of the source repo: `harvest_clustering.md`, `harvest_interventions.md`, `harvest_scaling.md`, `harvest_counter_evidence.md`, `theorem_zipf_log_reliability.md`, `N16_fusion_plan (1).md`, plus the Phase 6 capability harvest under `internal/error_architecture/capabilities/` (master `N16_capability_elimination_report.md` + six axis-specific files).
