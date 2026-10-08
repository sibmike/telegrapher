"""Recount the survey corpus from the scores CSV(s).

Usage:  python recount.py [csv ...]
Default: ../supplementary/p3_master_scores.csv (May-2026 corpus) plus any
         ../supplementary/p3_refresh_*.csv (October-2026 refresh rows).

Prints: unique systems, core/contrast split (score >= 3 on any substrate),
per-substrate n / mean / score-5 systems, and the composite two-loop matrix
membership when the refresh columns loop1/loop2 are present.
"""
import csv, glob, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SUP = os.path.join(HERE, "..", "supplementary")
paths = sys.argv[1:] or [os.path.join(SUP, "p3_master_scores.csv")] + sorted(glob.glob(os.path.join(SUP, "p3_refresh_*.csv")))

rows = []
for p in paths:
    with open(p, encoding="utf-8", errors="replace", newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("system"): continue
            r["_src"] = os.path.basename(p)
            alias = (r.get("master_alias") or "").strip()
            if alias:  # a vendor refresh row overrides the May-corpus row of the same system/substrate
                r["system"] = alias
                rows = [x for x in rows if not (x["system"].strip() == alias and x["substrate"].strip() == r["substrate"].strip())]
            rows.append(r)

def score(r):
    try: return float(r["score"])
    except (TypeError, ValueError): return None

systems = defaultdict(list)
for r in rows: systems[r["system"].strip()].append(r)
core = {s for s, rs in systems.items() if any((score(r) or -1) >= 3 for r in rs)}
print(f"files: {[os.path.basename(p) for p in paths]}")
print(f"rows: {len(rows)}  unique systems: {len(systems)}  core: {len(core)}  contrast: {len(systems) - len(core)}")

# per-substrate maturity: ALL scored rows (the arXiv v3.2 Section 6 table counts every row on the
# substrate, contrast rows included); core-only numbers are printed alongside for reference.
def maturity(filter_core):
    by_sub = defaultdict(list)
    for r in rows:
        if score(r) is None: continue
        if filter_core and r["system"].strip() not in core: continue
        by_sub[r["substrate"].strip()].append(r)
    return by_sub
for label, bs in (("all rows", maturity(False)), ("core only", maturity(True))):
    print(f"\n[{label}] substrate         n   mean  score-5 systems")
    for sub in sorted(bs):
        rs = bs[sub]; sc = [score(r) for r in rs]
        five = sorted({r["system"].strip() for r in rs if score(r) == 5})
        print(f"{sub:18s} {len(rs):4d}  {sum(sc)/len(sc):5.2f}  {', '.join(five) or '(none)'}")

def norm_gate(s):
    s = (s or "").strip()
    if not s or s.lower() in ("n/a", "-"): return "n/a"
    head = s.split("(")[0].strip().lower()
    if "->human" in head or "-> human" in head or "+human" in head or "+ human" in head: return "Auto+Human"
    if head.startswith("auto"): return "Auto"
    if head.startswith("human"): return "Human"
    if head.startswith("none"): return "None"
    return s[:20]

# composite two-loop matrix from loop1/loop2 columns (refresh rows carry them), gate labels normalized
if any("loop1" in r for r in rows):
    cells = defaultdict(set)
    for r in rows:
        l1, l2 = norm_gate(r.get("loop1")), norm_gate(r.get("loop2"))
        if l1 != "n/a" and l2 != "n/a" and r["system"].strip() in core and r.get("loop1"):
            cells[(l1, l2)].add(r["system"].strip())
    print("\nnormalized loop1 x loop2 cells (refresh rows):")
    for k in sorted(cells):
        names = sorted(cells[k])
        print(f"  [{k[0]} x {k[1]}]: {len(names)}  {names if len(names) <= 12 else names[:12] + ['...']}")
    print("\ncomposite candidates (Loop 2 present) with their gov_props:")
    for r in rows:
        # a Loop-2 mechanism counts whether or not it is gated: an ungated push with lineage (Letta) is labelled None (ungated ...)
        if (norm_gate(r.get("loop2")) in ("Auto", "Human", "Auto+Human") or "ungated" in (r.get("loop2") or "").lower()) and r["system"].strip() in core:
            print(f"  {r['system'][:48]:48s} L1={norm_gate(r.get('loop1'))} L2={norm_gate(r.get('loop2'))}  {(r.get('gov_props') or '')[:70]}  [{r.get('tier','')}]")

# governance flags
flagged = [(r["system"], r.get("gov_props")) for r in rows if (r.get("gov_props") or "-").strip() not in ("-", "")]
if flagged:
    print("\ngovernance properties claimed:")
    for s, g in sorted(set(flagged)): print(f"  {s}: {g}")
