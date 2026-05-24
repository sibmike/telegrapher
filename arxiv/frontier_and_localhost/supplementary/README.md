# Supplementary materials for *Frontier and Localhost*

This directory ships with the arXiv source bundle so that reviewers can re-run the survey discriminator from primary sources. Contents:

| File | Purpose |
|---|---|
| `p3_master_scores.csv` | Per-system, per-substrate 0–5 scores with evidence citations |
| `p3_harvest_s1_instructions.md` | Evidence harvest for S1 (instructions) |
| `p3_harvest_s2_skills.md` | Evidence harvest for S2 (skills) |
| `p3_harvest_s3_memory.md` | Evidence harvest for S3 (memory) |
| `p3_harvest_s4_tools.md` | Evidence harvest for S4 (tools) |
| `p3_harvest_s5_orchestration.md` | Evidence harvest for S5 (orchestration) |
| `p3_harvest_s6_governance.md` | Evidence harvest for S6 (governance) |
| `p3_harvest_integrated.md` | Cross-substrate integrated audit |
| `p3_harvest_composite_two_loop.md` | Strict composite-two-loop audit, 22 candidates |
| `p3_harvest_failure_modes.md` | Evidence harvest for §10 failure surface |
| `p3_prior_art_check.md` | Prior-art reconciliation against adjacent literatures |

## Note on the OpenCore entry

The audit files reproduced here are the original working documents from the survey. They contain entries for **OpenCore** (a maintainer-authored open-source project) that were ultimately **omitted from the published paper** in revision v2. The OpenCore audit row is retained in the supplementary materials as part of the historical record but should be treated as informational only: the published headline counts (thirteen research systems passing the strict composite-two-loop criterion; ten in [Auto × Auto] / [Auto × Human] after OpenCore removal) reflect the post-omission corpus, and the §8 matrix in the paper places [Human × Human] as empty in the surveyed corpus.

Removing OpenCore from the published analysis avoids a conflict of interest (a maintainer-authored system being load-bearing in a survey by the same maintainer) and tightens the empty-corner argument by making it independent of any author-attached exemplar. The audit trail is preserved here so that this revision decision is visible rather than hidden.

## Reproducing the analysis

To re-derive the headline figures:

1. Read `p3_master_scores.csv` for per-system PP scores.
2. Apply the patch-plastic discriminator (PP ≥ 3 on at least one substrate) to derive the core corpus.
3. Apply the composite-two-loop criterion (Loop 1 modifies persisted artifact from session signal *and* Loop 2 has explicit cross-context promotion with versioning or lineage) to derive the strict audit count.
4. Omit the OpenCore row to match the published numbers.

The sensitivity analysis in §5 of the paper documents how the count shifts under two natural relaxations of the criteria.
