# IEEE Access submission notes — Beyond Exponential Decay

## At a glance

| Field | Value |
|---|---|
| Manuscript type | **Topical Review**. Select it in the submission form; it is printed on the published article. |
| Title | Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models |
| Length | 22 pages in the official two-column template, including references and biography placeholders. Topical Reviews are exempt from the over-20-page guidance. |
| External pre-review | Points from an outside reader (2026-10-12) were addressed surgically; see `ledger_parts/K_final_wording_audit.md`, "External pre-submission review". |
| Abstract | 249 words; IEEE limit 150–250 |
| References | 156, every one indexed in `citation_ledger.md` |
| Keywords (alphabetical, 7) | Error accumulation; key tokens; large language models; long-context reliability; representation geometry; sparse attention; uncertainty quantification |
| Template | Official IEEE Access LaTeX template dated 2026-05-13 (`template_original/`) |
| Files to upload | `main.tex` and `main.pdf` (contents must match); `references.bib` / `main.bbl`; `figures/fig1_decay_regimes.pdf`; class, font and logo files; author photos; supplementary material (see below) |
| APC | USD 2,160 on acceptance. IEEE members get 5% off; IEEE society members get 20% off. |

## Inputs still needed from the authors

1. **Affiliation addresses.** Replace each `CITY, COUNTRY` in the `\address` lines. Confirm "Independent Researcher" for four authors and Palo Alto Networks for A. Shvets.
2. **Biographies and photos for all five authors.** Each biography is 100–150 words and goes after the references. The `IEEEbiographynophoto` placeholders are in `main.tex`; switch them to `IEEEbiography` with a photo of at least 100×120 px. This adds about half a page.
3. **ORCID** for the submitting author, public and populated.
4. **Funding statement** for the first-page footnote (`\tfootnote`), for example "This work received no external funding."
5. **AI disclosure.** Approve or edit the Acknowledgment paragraph. IEEE asks that sections using AI-generated text cite the AI system. The draft says the tool was used in all sections and cites it once there. If the editor prefers per-section citations, add `\cite{anthropic2026claude}` at the start of each section.
6. **Author names.** The arXiv record and this manuscript use "Alexey Shvets"; the preprint's own bib entry uses "Alexey A. Shvets". Pick one form for the byline, the biographies and the self-citation.
7. **Co-author consent** to submit, and the corresponding author's choice of opposed reviewers, if any.

## Prior publication disclosure and changes from the preprint

IEEE requires the submitting author to disclose prior publication. An earlier version is on arXiv:
- 2505.24187 v1, May 2025;
- v2, May 2026;
- v3, prepared October 2026, to be uploaded before submission.

IEEE allows preprints on arXiv. State this in the submission form and in the cover letter. The manuscript cites the preprint in Section II-B.

**Changes relative to arXiv v3**, for the cover letter and the form:
- **Format.** Recast from a position paper into a Topical Review: three research questions (Section III-D), a scope-and-method section with an explicit search and inclusion rule (Section II), and the same claim–evidence–limits–meaning structure for each pillar (Sections IV–VI).
- **Literature.** Expanded from 29 to 156 references, including the cross-model representation literature (Section VI-C) and Appendix B, "Adjacent Lines of Work". Appendix B places the review against imitation-learning compounding, exposure bias, self-correction, uncertainty and verification, uneven computation, jury theorems and ensemble diversity, multiversion software, and representation similarity.
- **Comparison and grading tables.** Comparison tables of reported results with their settings (Tables II–IV) and a graded strengths-and-weaknesses table (Table V).
- **Sharper framework.** The chain-rule form of the uniform model (Section III-A), which states when independence matters. A redefinition of error as a wrong commitment, with the finality premise stated. An ordered-hazard argument beside the positive-association argument (Appendix A-C). The jury-theorem framing of voting (Appendix A-D).
- **Balance.** Counter-evidence now carries more weight (Section VII-C), with the shared-difficulty alternative to geometric explanations (Section VI-C) and trained self-correction (Section VI-A).
- **Citation checking.** Every citing sentence was checked against the full text of its source and then audited independently on its final wording. The ledger and audit reports are supplementary material.

## Supplementary material

Section II-C says the citation ledger "is available as supplementary material". Upload one zip containing:
- `citation_ledger.md`: the index of all 156 keys;
- `ledger_parts/*.md`: per-source cards A–J, plus the final-wording audit record K;
- `audits/*.md`: the three independent final-wording audit reports;
- `sweep_candidates.md` and `related_work_cards.md`: how the adjacent-work appendix was scoped.

## Number-check log

Every number in Tables II–V and in the prose comes from a full-text reading recorded in `ledger_parts/`, and was re-checked against its source in the final-wording audit (`audits/`).

| Where | Ledger parts |
|---|---|
| Table II (importance) | `C_importance.md`, `A_v3_carryover.md` (Fang), `B_v3_carryover.md` (TextFooler) |
| Table III (hardness) | `B_v3_carryover.md`, `D_hardness.md` |
| Table IV (cross-model) | `F_crossmodel.md` |
| Table V (grading) | the review's own synthesis of Sections IV–VI |
| Tables I and VI, the running example | computed by the authors (Appendix A), recomputed in audit Part 2; Fig. 1 data from `figures/make_fig1_data.py` |
| Appendix B | `J1_compounding.md` through `J8_heterogeneity.md` |

Checks run on 2026-10-03:
- 156 cited keys = 156 bib entries = 156 indexed ledger entries;
- 0 undefined references;
- 0 BibTeX warnings;
- no retraction notices for any cited work (Crossref and arXiv).

For NeurIPS 2025 entries, page ranges follow the Crossref record of each DOI. They differ from the neurips.cc listing for that year only.

## Known residual risks

- **Two sources not opened**, as stated in Section II-C and the Acknowledgment:
  - **Hoeffding (1963)**: paywalled. Cited for the standard inequality.
  - **Lam and Suen (1997)**: abstract only. The citing sentence claims no more than the abstract.
- **Substitute versions read**:
  - Eckhardt and Lee (1985): the NASA TM 86369 precursor.
  - Knight and Leveson (1986): the authors' manuscript.
  - Three COLM papers: their arXiv camera-ready versions, because OpenReview was bot-protected.
- **Preprints.** About twenty references are arXiv-only, and each is labeled as a preprint in the reference list. Examples: Vakilian et al., Phi-4, Thought Anchors, Obeso et al., Thoria et al., Candussio et al., Yeom et al., Li and Sarwate, Ord, Cheng et al., Liu (latent communication survey), Costello et al., Kaplan et al., Kadavath et al., Cobbe et al., Lanham et al., Mixture-of-Depths, Brown et al., MAKER, and the authors' own preprint.
- **Non-archival sources.** The opening argument is cited to its author's LinkedIn post (the only source for its exact wording). Its formal versions, Dziri et al. and the imitation-learning bounds of Appendix B, are cited beside it. The industry note (Mostik) appears in a footnote only, with no numbers used.

## Rebuild

```bash
cd "telegrapher_repo/ieee_access/paper_beyond_exponential_decay"
/c/Users/mikea/anaconda3/python.exe tools/assemble_bib.py
bash build.sh
/c/Users/mikea/anaconda3/python.exe tools/build_ledger_index.py
```

## Cover letter (draft)

> Dear Editor,
>
> We submit "Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models" for consideration as a Topical Review in IEEE Access.
>
> A widely cited argument holds that large language models must fail on long outputs because per-token errors compound exponentially. The review examines the published evidence on the two assumptions behind that argument, uniform risk across positions and independence of errors, across four literatures that are usually reviewed separately:
> - attention sparsity and context compression;
> - generation-time uncertainty;
> - error dependence and self-correction;
> - the geometry of internal representations, including recent work on mapping representations between models.
>
> The review organizes the evidence around a two-rate model and compares reported results within their settings. It also grades the strength of each line of evidence, weighs the counter-evidence, and proposes a direct test. An appendix places the review against older and adjacent work, from compounding error in imitation learning to jury theorems and coincident failures in multiversion software.
>
> Every cited result was checked against its source. The final wording of every citing sentence was then audited independently, and the per-sentence record is provided as supplementary material. An earlier version of this argument is available as an arXiv preprint (arXiv:2505.24187). The manuscript has been substantially revised and extended for this submission, and it is not under consideration elsewhere.
>
> Sincerely,
> Mikhail L. Arbuzov, on behalf of all authors
