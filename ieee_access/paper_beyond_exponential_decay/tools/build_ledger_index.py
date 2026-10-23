"""Build citation_ledger.md: an index over ledger_parts/*.md for every key cited in main.tex.

Usage (from the paper folder):
    C:/Users/mikea/anaconda3/python.exe tools/build_ledger_index.py
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tex = (root / "main.tex").read_text(encoding="utf-8")

cited = []
for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", tex):
    for key in group.split(","):
        key = key.strip()
        if key and key not in cited:
            cited.append(key)

blocks = {}
for part in sorted((root / "ledger_parts").glob("*.md")):
    text = part.read_text(encoding="utf-8")
    pieces = re.split(r"^### +", text, flags=re.M)
    for piece in pieces[1:]:
        header, _, body = piece.partition("\n")
        key = header.split()[0].strip()
        blocks.setdefault(key, (part.name, body))

def summarize(body):
    verdicts = re.findall(r"Verdict:\s*\**\s*([A-Z][A-Za-z]+)", body)
    verdicts = [v.upper() for v in verdicts if v.upper() in {"ACCURATE", "NARROW", "DROP"}]
    access = "full text"
    if re.search(r"Access:\s*n/a", body, re.I):
        return verdicts, "n/a (tool, not a source of claims)"
    if re.search(r"abstract-only", body, re.I) and not re.search(r"Access:\s*full text", body, re.I):
        access = "abstract-only"
    if re.search(r"NOT accessible|paywalled", body, re.I) and not re.search(r"Access:\s*full text", body, re.I):
        access = "not opened (paywalled); metadata verified"
    return verdicts, access

rows, missing = [], []
for i, key in enumerate(cited, 1):
    if key not in blocks:
        missing.append(key)
        rows.append(f"| {i} | `{key}` | — | — | — | **no ledger entry** |")
        continue
    part, body = blocks[key]
    verdicts, access = summarize(body)
    counts = {v: verdicts.count(v) for v in ("ACCURATE", "NARROW", "DROP")}
    vtxt = ", ".join(f"{n} {v.lower()}" for v, n in counts.items() if n) or "see entry"
    rows.append(f"| {i} | `{key}` | `{part}` | {access} | {vtxt} | |")

out = [
    "# Citation ledger — Beyond Exponential Decay (IEEE Access Topical Review)",
    "",
    "Every reference cited in `main.tex` was read in full text at the passage the manuscript relies on, "
    "except where the Access column says otherwise. The per-use evidence (source passage, location, "
    "scope, verdict, and safe wording) lives in the part files under `ledger_parts/`; this file indexes them "
    "in order of first citation. Verdicts were recorded against the intended use before drafting; the "
    "final wording of each citing sentence was then re-checked by three independent auditors, whose "
    "reports are in `audits/` and whose findings, resolutions, and additional verified uses are recorded "
    "in `ledger_parts/K_final_wording_audit.md`.",
    "",
    "| # | Key | Ledger part | Access | Verdicts (per intended use) | Note |",
    "|---|---|---|---|---|---|",
    *rows,
    "",
    f"Cited keys: {len(cited)}. Keys without a ledger entry: {missing if missing else 'none'}.",
    "",
]
(root / "citation_ledger.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(f"indexed {len(cited)} keys; missing ledger entries: {missing}")
