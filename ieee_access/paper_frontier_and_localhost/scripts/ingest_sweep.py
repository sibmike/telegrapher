"""Ingest an M1 sweep report (scratchpad/m1_*.md) into the package.

- Every ```csv block whose header starts with "substrate,system," is appended to
  supplementary/p3_refresh_2026-10.csv (header written once; exact-duplicate rows skipped).
- Every ```bibtex / ```bib block is appended to submission/references.bib, skipping keys
  that already exist. Prints the keys added.

Usage: python ingest_sweep.py <report.md> [<report.md> ...]
"""
import os, re, sys, csv, io

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(HERE, "..")
CSV_OUT = os.path.join(PKG, "supplementary", "p3_refresh_2026-10.csv")
BIB = os.path.join(PKG, "submission", "references.bib")

def blocks(text, langs):
    return [m.group(1) for m in re.finditer(r"```(?:" + "|".join(langs) + r")\s*\n(.*?)\n```", text, re.S)]

existing_rows = set()
header = None
if os.path.exists(CSV_OUT):
    with open(CSV_OUT, encoding="utf-8", newline="") as f:
        r = csv.reader(f); header = next(r, None)
        for row in r: existing_rows.add(tuple(row))

bib = open(BIB, encoding="utf-8").read() if os.path.exists(BIB) else ""
have = set(re.findall(r"^@\w+\{([^,\s]+),", bib, re.M))

added_rows, added_keys = 0, []
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for blk in blocks(text, ["csv"]):
        rdr = csv.reader(io.StringIO(blk))
        rows = list(rdr)
        if not rows or not rows[0] or rows[0][0] != "substrate": continue
        if header is None:
            header = rows[0]
            with open(CSV_OUT, "w", encoding="utf-8", newline="") as f: csv.writer(f).writerow(header)
        with open(CSV_OUT, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            for row in rows[1:]:
                if not row or tuple(row) in existing_rows: continue
                if len(row) != len(header):
                    print(f"  WARN column count {len(row)} != {len(header)}: {row[1][:50]}")
                w.writerow(row); existing_rows.add(tuple(row)); added_rows += 1
    for blk in blocks(text, ["bibtex", "bib"]):
        for m in re.finditer(r"(@\w+\{([^,\s]+),.*?\n\})", blk, re.S):
            entry, key = m.group(1), m.group(2)
            if key in have: continue
            bib = bib.rstrip("\n") + "\n\n" + entry + "\n"
            have.add(key); added_keys.append(key)
open(BIB, "w", encoding="utf-8", newline="\n").write(bib)
print(f"rows added: {added_rows} -> {os.path.relpath(CSV_OUT, HERE)}")
print(f"bib keys added ({len(added_keys)}):", ", ".join(added_keys))
