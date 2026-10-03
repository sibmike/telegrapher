"""Assemble submission/paper_frontier_and_localhost_ieee.md from submission/sections/*.md in PARTS order.

Parts that do not exist yet are skipped with a notice, so the build can be smoke-tested
while sections are still being written. Run from anywhere.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(HERE, "..", "submission")
SEC = os.path.join(SUB, "sections")
OUT = os.path.join(SUB, "paper_frontier_and_localhost_ieee.md")

PARTS = [
    "00_front.md",
    "I_III.md",
    "IV_feedback_signal_classes.md",
    "V_method.md",
    "VI_findings.md",
    "VII_design_space.md",
    "VIII_families.md",
    "IX_missing_architecture.md",
    "X_failure_surface.md",
    "XI_open_problems_conclusion.md",
    "appA_formal.md",
    "appB_gates.md",
]

chunks, missing = [], []
for p in PARTS:
    f = os.path.join(SEC, p)
    if os.path.exists(f):
        t = open(f, encoding="utf-8").read().strip("\n")
        # strip HTML comments (drafting notes) before pandoc sees them
        import re
        t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
        chunks.append(t + "\n")
    else:
        missing.append(p)
open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(chunks))
print(f"assembled {len(chunks)} parts -> {os.path.relpath(OUT, HERE)}")
if missing:
    print("  missing (skipped):", ", ".join(missing))
