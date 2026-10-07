# Ancillary files: the released score table

These files accompany *Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights* (v4, October 2026). Appendix I of the paper prints every row; the CSVs carry the per-row justification that the printed table omits, and `recount.py` reproduces every number in Section 6 from them.

| File | Contents |
|---|---|
| `p3_master_scores.csv` | The May-2026 corpus: 130 systems scored 0–5 on the six substrates (with the two corrections described in Appendix G). |
| `p3_refresh_2026-10.csv` | The October-2026 sweep: 126 further systems, with the Loop 1 / Loop 2 gate type, feedback-signal class, governance properties, arXiv id, evidence tier, and admission decision per row. A `master_alias` value marks a row that re-audits a May-2026 system rather than adding one. |
| `recount.py` | Recomputes the maturity table (rows per substrate, mean score, score-5 systems), the core/contrast split, and the composite two-loop audit. |

Rerun the recount with the two CSVs beside the script:

```
python recount.py p3_master_scores.csv p3_refresh_2026-10.csv
```

Scores are single-rater. The rubric is Table 4 of the paper; the discriminator (a persistent artifact updated from deployment signal) and the composite two-loop criterion are defined in Section 5.
