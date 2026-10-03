"""Every key cited in main.aux must have a \\bibitem in main.bbl. Exit 1 otherwise."""
import os, re, sys
SUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "submission")
aux = open(os.path.join(SUB, "main.aux"), encoding="utf-8", errors="replace").read()
bbl = open(os.path.join(SUB, "main.bbl"), encoding="utf-8", errors="replace").read()
cited = {k.strip() for m in re.findall(r"\\citation\{([^}]*)\}", aux) for k in m.split(",") if k.strip()}
items = set(re.findall(r"\\bibitem\{([^}]*)\}", bbl))
missing = sorted(cited - items)
print(f"cited keys: {len(cited)}  bibitems: {len(items)}  missing: {len(missing)}")
for k in missing: print("  MISSING", k)
sys.exit(1 if missing else 0)
