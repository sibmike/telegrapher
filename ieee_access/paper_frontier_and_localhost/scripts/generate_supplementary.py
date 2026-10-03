"""Generate submission/supplementary.md (IEEE Access Supplementary Material S1-S6).

S1  Full score table (May 2026 corpus + October 2026 sweep), generated from the CSVs.
S2  Data appendix: corpus assembly, tiers, scoring discipline, sensitivity (from the arXiv short, Appendix B).
S3  Mechanism stack and continual-learning notes (arXiv short, Appendix E.1, E.8, E.9).
S4  Contrast set, named matrix membership, closest approaches (arXiv short, Appendices D and F).
S5  The convergent research families, system by system (arXiv short, Appendix G).
S6  Claims audit (CLAIMS_AUDIT.md, verbatim) and the rubric-reward table from the sweep.

Sections are lifted by heading from the arXiv short v3.2 Markdown, so citation keys stay valid.
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(HERE, "..")
SHORT = os.path.join(PKG, "..", "..", "arxiv", "frontier_and_localhost", "short", "paper_frontier_and_localhost_short.md")
OUT = os.path.join(PKG, "submission", "supplementary.md")
SUP = os.path.join(PKG, "supplementary")

short = open(SHORT, encoding="utf-8").read()

def section(start_heading, end_heading):
    """Text from the line starting with start_heading up to (not including) the line starting with end_heading."""
    i = short.find("\n" + start_heading)
    j = short.find("\n" + end_heading, i + 1) if end_heading else len(short)
    assert i >= 0 and j > i, (start_heading, end_heading)
    return short[i + 1:j].strip("\n")

def sub(text, pairs):
    for a, b in pairs: text = text.replace(a, b)
    return text

# ---- S1: full score table from the CSVs
rows = []
for name in ("p3_master_scores.csv", "p3_refresh_2026-10.csv"):
    with open(os.path.join(SUP, name), encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("system"): rows.append((name, r))
def esc(s): return (s or "").replace("|", "/").replace("\n", " ").strip()
SUBS = {"INTEGRATED": "INT", "S1_Instructions": "S1", "S2_Skills": "S2", "S3_Memory": "S3", "S4_Tools": "S4", "S5_Orchestration": "S5", "S6_Governance": "S6"}
def src(s):
    """Source cell: the arXiv id when there is one; otherwise the host/path with parenthetical
    notes dropped, cut at a path boundary near 30 characters, and a zero-width space after
    each slash so pdflatex can break the URL inside the column (U+200B is declared in build.sh)."""
    s = esc(s)
    m = re.search(r"\d{4}\.\d{4,5}", s)
    if m:
        return "arXiv:" + m.group(0)
    s = s.split(" (")[0].strip()
    if len(s) > 30:
        s = s[:30].rsplit("/", 1)[0] if "/" in s[:30] else s[:30]
    return s.replace("/", "/​").replace(".", ".​")
# dash lengths set pandoc's relative column widths
lines = ["| Sub. | System | Score | Year | Source | Loop 1 | Loop 2 | Class | Added |",
         "|---|------------|---|---|------------|-----|-----|-----|----|"]
def gate(s):
    # "Auto+Human" gets a break opportunity after the plus so it wraps inside its column
    return esc(s).split("(")[0].strip()[:10].replace("+", "+​")
for name, r in sorted(rows, key=lambda x: (x[1]["substrate"], x[1]["system"].lower())):
    l1, l2 = gate(r.get("loop1", "")), gate(r.get("loop2", ""))
    yr = esc(r["year"])
    yr = yr if (yr.isdigit() and len(yr) == 4) else "—"      # SOAR's "classical" (pre-window)
    cls = esc(r.get("signal_class", "")).split("(")[0].strip()
    lines.append(f"| {SUBS.get(esc(r['substrate']), esc(r['substrate']))} | {esc(r['system'])[:48]} | {esc(r['score'])} | {yr} | {src(r['venue_or_source'])} | {l1} | {l2} | {cls} | {'Oct 26' if name.startswith('p3_refresh') else 'May 26'} |")
s1 = ("# S1. Full score table\n\nEvery scored (substrate, system) row of the corpus: 130 systems scored by May 2026 and 126 added by the October 2026 sweep. "
      "Scores follow the 0–5 rubric of the main text (Table V-1); Loop 1 / Loop 2 gate types and signal classes are recorded for the October rows "
      "(and for May rows re-audited in Section VII). Substrate codes: INT integrated, S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance. "
      "A year of “—” marks a classical system that predates the survey window. "
      "The CSV files with per-row justifications accompany this document.\n\n```{=latex}\n\\begingroup\\scriptsize\n```\n\n" + "\n".join(lines) + "\n\n```{=latex}\n\\endgroup\n```\n")

# ---- S2: data appendix (arXiv Appendix B)
s2 = "# S2. Data appendix\n\n" + sub(section("## Appendix B. Data appendix", "## Appendix C."), [
    ("## Appendix B. Data appendix\n", ""), ("§4", "Section V of the main text"), ("§§6–9", "Sections VI–IX"),
])

# ---- S3: mechanism stack + continual-learning notes (E.1, E.8, E.9)
e1 = section("### E.1 The mechanism stack", "### E.2")
e8 = section("### E.8 Loop 1 and Loop 2", "### E.9")
e9 = section("### E.9 Overfitting", "## Appendix F.")
s3 = "# S3. The mechanism stack and continual-learning notes\n\n" + sub(e1 + "\n\n" + e8 + "\n\n" + e9, [("### E.1", "## S3.1"), ("### E.8", "## S3.2"), ("### E.9", "## S3.3"), ("§3", "Section III"), ("§4", "Section V")])

# ---- S4: contrast set, matrix membership, closest approaches (D, F)
d = section("## Appendix D. Contrast set", "## Appendix E.")
f = section("## Appendix F. Survey detail", "## Appendix G.")
s4 = "# S4. Contrast set, matrix membership, and closest approaches (May 2026 corpus)\n\nThe October 2026 additions are placed in the cells of Section VII of the main text and listed in S1; the per-system discussion below is the May 2026 audit on which the main text's counts build.\n\n" + sub(d + "\n\n" + f, [
    ("## Appendix D. Contrast set", "## S4.1 Contrast set"), ("### D.1", "### S4.1.1"), ("### D.2", "### S4.1.2"),
    ("## Appendix F. Survey detail", "## S4.2 Survey detail"), ("### F.1", "### S4.2.1"), ("### F.2", "### S4.2.2"), ("### F.3", "### S4.2.3"),
    ("§8", "Section VII"), ("§9", "Section IX"), ("§3", "Section III"), ("§5", "Section V"), ("§7", "Section VI"), ("§3.5", "Section VIII"), ("§10", "Section X"),
])

# ---- S5: convergent families (G)
g = section("## Appendix G.", "## References")
s5 = "# S5. The convergent research families, system by system\n\n" + sub(g, [
    ("## Appendix G. SkillOpt walkthrough and the convergent families", "This section carries the May–September 2026 walkthroughs; the October 2026 additions to each family are described in Section VIII of the main text and scored in S1."),
    ("### G.", "## S5."), ("§3.5", "Section VIII"), ("§3", "Section III"), ("§9", "Section IX"), ("§10", "Section X"), ("§8", "Section VII"), ("§4", "Section V"), ("§2", "Section II"),
])

# ---- S6: claims audit + rubric table
audit = open(os.path.join(PKG, "CLAIMS_AUDIT.md"), encoding="utf-8").read()
audit = re.sub(r"^# .*\n", "", audit, count=1)
# the repository path is an unbreakable code span that overruns the margin; name the file in prose
audit = audit.replace("(`arxiv/frontier_and_localhost/short/paper_frontier_and_localhost_short.md`, line numbers as of 2026-09-20)",
                      "(the arXiv short v3.2 Markdown source, line numbers as of 2026-09-20)")
_s6n = [0]
def _s6head(m):
    _s6n[0] += 1
    return f"\n## S6.{_s6n[0]} "
s6 = "# S6. Claims audit and the rubric-reward comparison\n\n" + re.sub(r"\n## ", _s6head, audit)

# ---- S7: extended related work (drafted section file)
s7_path = os.path.join(PKG, "submission", "sections", "S7_extended_related_work.md")
s7 = open(s7_path, encoding="utf-8").read().strip("\n") if os.path.exists(s7_path) else ""

front = """---
title: "Supplementary Material for: Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights"
date: "October 2026"
---

This document accompanies the main article. S1 is the released score table; S2–S5 carry the verification material of the survey (data appendix, mechanism stack, contrast set and matrix membership, and the per-system walkthrough of the convergent research families); S6 is the audit of every absolute claim of the earlier preprint against the October-2026 literature, with the rubric-reward comparison that Section IV of the main text summarizes; S7 is the extended related work, organized by the article's four design commitments. Section numbers in the form "Section N" refer to the main article.

"""
body = front + "\n\n".join([p for p in (s1, s2, s3, s4, s5, s6, s7) if p]) + "\n"

# Lifted tables carry equal-dash separators, which pandoc turns into equal column widths; give
# the long-text columns the width (dash counts are relative; cell text is untouched).
WIDTHS = {
    "| System | Year | Discriminator failure | Brief reason |": (16, 5, 24, 40),
    "| System | Year | Composite-criterion failure | Brief reason |": (16, 5, 24, 40),
    "| Section III quantity | SkillOpt instantiation | Section III role explained | Algorithm pointer |": (16, 24, 26, 20),
    "| Line | Claim | Verdict | Evidence |": (5, 23, 10, 42),
    "| Claim | Statement | Verdict | Evidence |": (5, 23, 10, 42),
}
for header, widths in WIDTHS.items():
    sep = "|" + "|".join("-" * w for w in widths) + "|"
    body = re.sub(r"(?m)^" + re.escape(header) + r"\n\|[-:|]+\|$", header + "\n" + sep, body)

open(OUT, "w", encoding="utf-8", newline="\n").write(body)
print("wrote", os.path.relpath(OUT, HERE), "rows:", len(rows))
