"""Corrections to the May-2026 master score table applied for the IEEE Access version (logged in CLAIMS_AUDIT.md).

1. S5 scores of Multi-Agent Evolve (MAE) and Memento-Skills: 5 -> 4. Both close one loop with no cross-context
   promotion; the uniform rubric reserves 5 for "two-loop versioned promotion plus governance". The arXiv v3.2
   Section 6 table already listed no score-5 orchestration system; the CSV rows disagreed with it.
2. Substrate names normalized to the master spelling (INTEGRATED, S1_Instructions, ...) in the refresh file.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
SUP = os.path.join(HERE, "..", "supplementary")
M = os.path.join(SUP, "p3_master_scores.csv")
R = os.path.join(SUP, "p3_refresh_2026-10.csv")

with open(M, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
hdr, changed = rows[0], 0
for r in rows[1:]:
    if r[0] == "S5_Orchestration" and r[1] in ("Multi-Agent Evolve (MAE)", "Memento-Skills") and r[2] == "5":
        r[2] = "4"; changed += 1
        r[6] = (r[6] + "; re-scored 4 (2026-10): one loop closed, no cross-context promotion").strip("; ")
with open(M, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)
print("master S5 corrections applied:", changed)

CANON = {"integrated": "INTEGRATED", "s1_instructions": "S1_Instructions", "s2_skills": "S2_Skills", "s3_memory": "S3_Memory",
         "s4_tools": "S4_Tools", "s5_orchestration": "S5_Orchestration", "s6_governance": "S6_Governance"}
with open(R, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
fixed = 0
for r in rows[1:]:
    key = r[0].strip().lower().replace(" ", "_")
    if key in CANON and r[0] != CANON[key]:
        r[0] = CANON[key]; fixed += 1
with open(R, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)
print("refresh substrate names normalized:", fixed)
