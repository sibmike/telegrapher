# Supplementary data: released score table

This archive accompanies the anonymized submission "Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights".

- `data/p3_master_scores.csv`: the first 130 systems, one row per scored (substrate, system) pair: substrate, system, score (0 to 5), year, venue or source, category, and a one-line justification (`key_evidence`).
- `data/p3_refresh_2026-10.csv`: the 126 systems added later, with the same columns plus the gate on each half of the loop (`loop1` is the local gate, `loop2` the promotion gate: Auto, Human, or None), the feedback-signal class (C1 exact check, C2 observed outcome, C3 judgment, C4 delayed reward), the governance properties (a) to (d), the evidence tier (T1 to T5), and the core/contrast admission.
- `scripts/recount.py`: recomputes the corpus counts reported in the paper (256 systems, 204 core and 52 contrast, 269 scored rows, the per-substrate means and score-5 systems, and the gate-pair membership of the later rows) from the two files. Run `python scripts/recount.py data/p3_master_scores.csv data/p3_refresh_2026-10.csv`.

Substrate codes: INTEGRATED (a system scored across several substrates as one row), S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance. Every classification is one rater's reading of the cited public source; a reader who disagrees with a score can locate the evidence it rests on in the justification column.
