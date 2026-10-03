"""Clean supplementary/p3_refresh_2026-10.csv after ingesting the three M1 sweeps.

- Repairs rows whose venue field carried unquoted commas (field count 18 -> 15 by joining fields 4..7).
- Drops duplicate (arxiv_id, substrate) rows scored by two sweeps, keeping the first (the sweeps agree on score).
- Adds a `master_alias` column mapping "(2026 refresh)" vendor rows onto their May-corpus system names so
  recount.py treats them as overrides rather than new systems.
"""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "supplementary", "p3_refresh_2026-10.csv")
ALIASES = {
    "Letta MemFS + Context Repositories + Dreaming (2026 refresh)": "MemGPT / Letta",
    "Mem0 Platform (2026 refresh: history, feedback, expiration, decay)": "Mem0",
    "Zep / Graphiti bitemporal facts (2026 refresh)": "Zep / Graphiti",
    "LangGraph Store / LangMem (2026 refresh)": "LangGraph Long-Term Memory",
}
with open(P, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
header, body = rows[0], rows[1:]
fixed, seen, out = 0, set(), []
for r in body:
    if len(r) == 18:
        r = r[:4] + [", ".join(r[4:8])] + r[8:]; fixed += 1
    if len(r) != len(header):
        print("  still malformed:", len(r), r[1][:50]); continue
    d = dict(zip(header, r))
    key = (d["arxiv_id"].strip(), d["substrate"].strip())
    if key[0] not in ("", "-", "n/a"):
        if key in seen:
            print("  dropped duplicate:", d["system"][:40], key); continue
        seen.add(key)
    out.append(r)
if "master_alias" not in header:
    header = header + ["master_alias"]
    out = [r + [ALIASES.get(r[1].strip(), "")] for r in out]
else:
    i = header.index("master_alias")
    for r in out: r[i] = ALIASES.get(r[1].strip(), r[i])
with open(P, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(header); w.writerows(out)
print(f"repaired {fixed}; kept {len(out)} rows; aliases set: {sum(1 for r in out if r[-1])}")
