"""Assemble references.bib from the audited ledger bib parts, keeping only cited keys.

Usage (from the paper folder):
    C:/Users/mikea/anaconda3/python.exe tools/assemble_bib.py

Every entry comes from ledger_parts/*.bib, which hold BibTeX checked against the
source of record. The script fails loudly if a cited key has no audited entry or
if two parts define the same key.
"""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tex = (root / "main.tex").read_text(encoding="utf-8")

cited = []
for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", tex):
    for key in group.split(","):
        key = key.strip()
        if key and key not in cited:
            cited.append(key)

entries = {}
for part in sorted((root / "ledger_parts").glob("*.bib")):
    text = part.read_text(encoding="utf-8")
    for match in re.finditer(r"(@\w+\{([^,]+),.*?\n\})", text, re.S):
        key = match.group(2).strip()
        if key in entries:
            sys.exit(f"duplicate key {key} in {part.name} and {entries[key][0]}")
        entries[key] = (part.name, match.group(1).strip())

missing = [k for k in cited if k not in entries]
if missing:
    sys.exit(f"cited keys with no audited bib entry: {missing}")

out = [entries[k][1] for k in cited]
(root / "references.bib").write_text("\n\n".join(out) + "\n", encoding="utf-8", newline="\n")
unused = sorted(set(entries) - set(cited))
print(f"wrote {len(out)} entries (in order of first citation)")
print(f"audited but not cited ({len(unused)}): {unused}")
