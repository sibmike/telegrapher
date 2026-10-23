# Extended related work: spine and evidence cards

Working file for Appendix B of the IEEE Access Topical Review, built with the `extended-related-work` skill (2026-10-03). The evidence cards are the `J_*.md` files in `ledger_parts/`. They use the same format as the rest of the citation ledger, so `tools/build_ledger_index.py` indexes them with everything else. No citing sentence in Appendix B is written from memory.

## Phase 0: the review's spine

### Contribution claims (Section I, verbatim in substance)
1. One model connects long-context sparsity, generation-time uncertainty, and error dependence, which are usually reviewed separately.
2. Comparison tables report each result with the setting it holds in.
3. Calculations show how dependence between errors changes sequence-level reliability and the value of majority voting.
4. A reconciliation of apparently conflicting results, including agent evaluations that report exponential decay in task length.
5. A graded assessment of the evidence and a set of open problems, including a protocol for measuring k(n).

### Design commitments: choices another review could make differently
| # | Commitment | Neighbours a memory-based reviewer would name |
|---|---|---|
| C1 | **Reliability is judged on the whole answer.** An error is a token that changes final correctness. Surprisal and stylistic deviation are not errors. | Sequence-level uncertainty (semantic entropy); token-level uncertainty for fact-checking; step-level verification (process reward models) |
| C2 | **Sequence failure is a composition of per-position risks.** The two-rate product, not a per-step hazard fitted to tasks. | Compounding error in imitation learning (Ross and Bagnell; DAgger); exposure bias (Ranzato; Schmidt; He et al. on self-recovery); reliability over repeated trials (pass^k) |
| C3 | **Two empirical handles on key positions.** Importance (where information flows) and hardness (where mistakes are made). | Attention as explanation (Jain and Wallace; Wiegreffe and Pinter; Kobayashi et al.); computation allocation that presumes most tokens are easy (speculative decoding, early exit, adaptive depth) |
| C4 | **Dependence across samples and models, and what it does to voting.** | Condorcet jury theorem with correlated voters; ensemble diversity; algorithmic monoculture; repeated sampling and coverage; verifiers versus voting; multi-agent debate |
| C5 | **Representation structure as a candidate explanation.** What is shared across models is local, not global. | Representation similarity (SVCCA, CKA); model stitching; truthfulness probes (CCS, internal-state lie detection, "truth is universal"); non-linear features |

### What the review does not claim (Appendix B may not promise more)
- It runs no experiments. The parameters of the running example are illustrative.
- The geometric explanation of error clustering is not tested (Section VI-B, last paragraph; Table 5, last row).
- No study measures how far importance and hardness overlap (Sections V-C, IX).
- No single fixed fraction of key positions exists. Shares depend on criterion, unit, task, and whether the set is fixed (Section VII-A).
- Exponential decay returns when k grows in proportion to the number of steps (Table 1, last row; Section VII-B).
- Cross-model structure is shared locally, not as one universal manifold (Section VI-C).

## Phase 2: "missing XYZ" sweep
Two simulated memory-based reviewers were run. One saw the full manuscript; the other saw only the abstract and introduction. Their candidate lists are merged with the commitments above in `sweep_candidates.md`. Every candidate kept was then verified in full text (cards in `ledger_parts/J_*.md`). Candidates that could not be verified are listed there with the reason they were dropped.

## Phases 1 and 3–5: cards, writing, verification

- **Cards.** Eight verification batches (`ledger_parts/J1_*.md` … `J8_*.md`) checked 73 new works, plus new uses of two works already cited (Bachmann and Nagarajan; LeCun). 72 of the new works are cited, bringing the bibliography from 84 to 156. Two were limited by access: Lam and Suen (abstract only, so cited for no more than the abstract says) and Ladha (not opened, so not cited).
- **Appendix B.** It has five subsections, each following the skill's arc: lineage, what was established, the setting assumed, the hinge, and what the review inherits. The "what is and is not new" concession sits in Section II-D, which ties it to the contributions list in the Introduction.
- **Fact pass.** An independent auditor checked every sentence of Appendix B against its card and its source (`audits/citation_audit_part3_appB.md`). It found 1 HIGH, 9 MEDIUM and 22 LOW issues and no fabricated work, and all were resolved (`ledger_parts/K_final_wording_audit.md`).
- **Consistency pass.** The novelty statement in Section II-D matches the Introduction's contributions. It concedes the classical tools by name: the quadratic compounding bound, the jury theorem, and the failure of independence in multiversion software.
