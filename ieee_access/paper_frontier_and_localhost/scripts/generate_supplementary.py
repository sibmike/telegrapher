"""Generate submission/supplementary.md (IEEE Access Supplementary Material S1-S6).

S1  Full score table (May 2026 corpus + October 2026 sweep), generated from the CSVs.
S2  Data appendix: corpus assembly, tiers, scoring discipline, sensitivity (from the arXiv short, Appendix B).
S3  Mechanism stack and continual-learning notes (arXiv short, Appendix E.1, E.8, E.9).
S4  Contrast set, named matrix membership, closest approaches (arXiv short, Appendices D and F).
S5  The convergent research families, system by system (arXiv short, Appendix G).
S6  Claims audit (CLAIMS_AUDIT.md, verbatim) and the rubric-reward table from the sweep.

Sections are lifted by heading from the arXiv short v3.2 Markdown, so citation keys stay valid.
"""
import csv, os, re, sys

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

# arXiv-short section numbers -> IEEE section numbers (longest patterns first, so "§3.5" is not read as "§3" + ".5")
SECMAP = [("§§8–10", "Sections VII–X"), ("§§8–9", "Sections VII–IX"), ("§§6–9", "Sections VI–IX"), ("§3.5", "Section VIII"), ("§11", "Section XI"),
          ("§10", "Section X"), ("§2", "Section II"), ("§3", "Section III"), ("§4", "Section V"), ("§5", "Section V"),
          ("§6", "Section VI"), ("§7", "Section VI"), ("§8", "Section VII"), ("§9", "Section IX"), ("§1", "Section I")]
# arXiv-short appendix letters that leak into the lifted prose -> this document's section labels
# ("Section S<n>" is the form the arXiv assembler re-targets to appendix cross-references)
LETTER_RULES = [
    (r"Appendix D\.1\b", "Section S4.1.1"), (r"Appendix D\.2\b", "Section S4.1.2"),
    (r"\*\*D\.1\*\*", "**Section S4.1.1**"), (r"\*\*D\.2\*\*", "**Section S4.1.2**"),
    (r"Appendix D\b", "Section S4.1"), (r"Appendix A\b", "Section S1"), (r"Appendix B\b", "Section S2"),
    (r"Appendix E\.1\b", "Section S3.1"), (r"\bE\.1\b", "Section S3.1"),
    (r"Appendix E\.6\b", "Appendix XII-D of the main text"), (r"\bE\.6\b", "Appendix XII-D of the main text"),
    (r"Appendix G walkthrough", "Section S5 walkthrough"), (r"Appendix G\b", "Section S5"),
    (r"\bG\.(\d+)–G\.(\d+)\b", r"Sections S5.\1–S5.\2"), (r"\bG\.(\d+)\b", r"Section S5.\1"),
]
def relabel(text):
    text = sub(text, SECMAP)
    for pat, rep in LETTER_RULES:
        text = re.sub(pat, rep, text)
    # "[@key; Section VIII; Section S5]" would print as a citation suffix "[[30]; ...]"; keep the pointer outside the cite
    text = re.sub(r"\[(@[\w:-]+); ((?:(?!@)[^\]])*)\]", r"[\1] (\2)", text)
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
    return s.replace("/", "/​").replace(".", ".​").replace(":", ":​")
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
      "Scores follow the 0–5 rubric of the main text (Table 3); Loop 1 / Loop 2 gate types and signal classes are recorded for the October rows "
      "(the gate pairs of the first-pass systems audited under the composite criterion are in the matrix of Section S4.2.1). Substrate codes: INT integrated, S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance. "
      "A year of “—” marks a classical system that predates the survey window. "
      "The CSV files with per-row justifications accompany this document.\n\n```{=latex}\n\\begingroup\\scriptsize\n```\n\n" + "\n".join(lines) + "\n\n```{=latex}\n\\endgroup\n```\n")

# ---- S2: data appendix (arXiv Appendix B)
s2 = "# S2. Data appendix\n\n" + relabel(sub(section("## Appendix B. Data appendix", "## Appendix C."), [
    ("## Appendix B. Data appendix\n", ""), ("§4", "Section V of the main text"),
]))

# The lifted data appendix described the May-2026 pass alone; its corpus paragraphs now describe both passes
# (numbers from scripts/recount.py on the two CSVs: 256 unique / 269 rows / 204 core / 52 contrast; May pass
# 130 / 140 / 99 / 31; October rows 133, four of them re-audits of May systems).
def replace_par(text, label, new):
    pat = re.compile(r"\*\*" + re.escape(label) + r"\*\*.*?(?=\n\n)", re.S)
    if not pat.search(text):
        raise SystemExit("S2 paragraph not found: " + label)
    return pat.sub(lambda m: new, text, count=1)
s2 = replace_par(s2, "Corpus size.",
    "**Corpus size.** The corpus was assembled in two passes. The May-2026 pass scored 130 unique systems (140 substrate-level rows in `p3_master_scores.csv`); "
    "the October-2026 pass added 126 systems (133 rows in `p3_refresh_2026-10.csv`, four of which re-audit May systems rather than adding one), for 256 unique systems "
    "and 269 substrate-level rows. A system may be scored on several substrates, so row counts exceed system counts; the maturity table of Section VI counts rows.")
s2 = replace_par(s2, "Core / contrast split.",
    "**Core / contrast split.** 204 of the 256 systems satisfy the patch-local discriminator (score ≥ 3 on at least one substrate) and form the core corpus, 99 of them from the May pass. "
    "The remaining 52 (31 from the May pass) form the contrast corpus: commonly described as agentic or self-improving in public discourse but failing at least one discriminator. "
    "Section S4.1 enumerates representative contrast systems from the May pass; each October contrast row carries its exclusion reason in the released CSV.")
s2 = replace_par(s2, "Survey window and dating.",
    "**Survey window and dating.** January 2023 to May 2026 for the first pass; June to October 2026 for the second, a systematic sweep in three parallel strands "
    "(skills and skill lifecycle; harness, context, and LLMOps governance; memory governance, competing surveys, and rubric rewards) rather than a targeted refresh, "
    "so the per-substrate statistics of Section VI are computed on both passes together. The cutoff is October 2026. Preprint-only systems carry T2 evidence, recorded per row "
    "in the released CSV. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.")
s2 = replace_par(s2, "Composite two-loop criterion (sensitivity analysis).",
    "**Composite two-loop criterion (sensitivity analysis).** The strict count of fourteen research systems satisfying the composite two-loop criterion changes under two natural relaxations. "
    "Relaxation (a) counts any of versioning, lineage, or rollback as Loop-2 governance: on the May pass the count rises to approximately eighteen by re-admitting MAE, MetaGen, MetaReflection, and CLIN, "
    "and on the October pass it admits the seven systems that promote across users, clients, teams, or repositories without versioning or lineage (EvolveNet, Evo2Team, XRepoSkill, ShareMem, RASO, "
    "Spotify's recommendation loop, and Future AGI's prompt lifecycle). Relaxation (b) admits session signal that updates optimizer state without persisting an artifact distinct from optimizer state: "
    "on the May pass the count rises to approximately sixteen by re-admitting DSPy and TextGrad; it adds no October system, because the October contrast rows are benchmarks, evaluation and attack studies, "
    "registries, audits, and conceptual frameworks, plus one orchestrator whose adaptation lives in the weights, none of which persists optimizer state as its only artifact. "
    "The qualitative findings ([Auto × Auto] well populated; [Human × Auto] empty; the other human-authored cells occupied only by registries and curation workflows that fail the composite audit; "
    "the governance-first cluster in [None × Auto]; the cross-tenant governed-optimization corner empty) survive both relaxations.")
assert "per-row evidence column in Section S1" in s2
s2 = s2.replace("per-row evidence column in Section S1", "per-row evidence column of the released CSV")

# ---- S3: mechanism stack + continual-learning notes (E.1, E.8, E.9)
e1 = section("### E.1 The mechanism stack", "### E.2")
e8 = section("### E.8 Loop 1 and Loop 2", "### E.9")
e9 = section("### E.9 Overfitting", "## Appendix F.")
s3 = "# S3. The mechanism stack and continual-learning notes\n\n" + relabel(sub(e1 + "\n\n" + e8 + "\n\n" + e9, [("### E.1", "## S3.1"), ("### E.8", "## S3.2"), ("### E.9", "## S3.3")]))

# ---- S4: contrast set, matrix membership, closest approaches (D, F)
d = section("## Appendix D. Contrast set", "## Appendix E.")
f = section("## Appendix F. Survey detail", "## Appendix G.")
s4 = "# S4. Contrast set, matrix membership, and closest approaches (May 2026 corpus)\n\nThe October 2026 additions are placed in the cells of Section VII of the main text and listed in Section S1; the per-system discussion below is the May 2026 audit on which the main text's counts build.\n\n" + relabel(sub(d + "\n\n" + f, [
    ("## Appendix D. Contrast set", "## S4.1 Contrast set"), ("### D.1", "### S4.1.1"), ("### D.2", "### S4.1.2"),
    ("## Appendix F. Survey detail", "## S4.2 Survey detail"), ("### F.1", "### S4.2.1"), ("### F.2", "### S4.2.2"), ("### F.3", "### S4.2.3"),
]))

_old = "(COSPLAY, Cuadros et al., PACE, CORAL, GEPA, Meta-Harness, MOSS, RCL, marked ‡ there, and the September-2026 refresh additions marked §)"
assert _old in s4, "S4 matrix note changed"
s4 = s4.replace(_old, "(COSPLAY, Cuadros et al., PACE, CORAL, GEPA, Meta-Harness, MOSS, and RCL from the May pass, and every October-2026 row)")
# the May-pass matrix discussion: point the two cells the October pass filled to the main text
assert "empty in surveyed corpus" in s4 and "**[Human × Human]** is empty in the surveyed corpus." in s4
s4 = s4.replace("empty in surveyed corpus", "empty in the May-2026 pass")
s4 = s4.replace("**[Human × Human]** is empty in the surveyed corpus.",
                "**[Human × Human]** is empty in the May-2026 pass; the October-2026 pass places MCP registries and a community hub here (Section VII of the main text).")
s4, _n = re.subn(r"\*\*\[Human × None\]\*\* is structurally improbable: a system(.*?)Section III\.",
                 r"**[Human × None]** was judged structurally improbable in the May-2026 pass, on the argument that a system\1Section III; the October-2026 pass found its occupants in the curation workflows of Section VII of the main text.",
                 s4, count=1, flags=re.S)
assert _n == 1, "S4 [Human x None] sentence changed"

# ---- S5: convergent families (G)
g = section("## Appendix G.", "## References")
s5 = "# S5. The convergent research families, system by system\n\n" + relabel(sub(g, [
    ("## Appendix G. SkillOpt walkthrough and the convergent families", "This section carries the May–September 2026 walkthroughs; the October 2026 additions to each family are described in Section VIII of the main text and scored in Section S1."),
    ("### G.", "## S5."),
]))

# ---- S6: claims audit + rubric table
audit = open(os.path.join(PKG, "CLAIMS_AUDIT.md"), encoding="utf-8").read()
audit = re.sub(r"^# .*\n", "", audit, count=1)
# The audit file is the authors' working record (it keys claims to source lines of the May-2026 draft and
# names repository scripts). The published appendix describes the draft and the released files in prose.
audit = audit.replace("Every absolute claim in the arXiv short v3.2 (`arxiv/frontier_and_localhost/short/paper_frontier_and_localhost_short.md`, line numbers as of 2026-09-20)",
                      "Every absolute claim of the May-2026 draft of this survey (the version whose corpus closed in May 2026)")
audit = audit.replace("the recount in `scripts/recount.py`", "the recount script released with the score table")
audit = audit.replace("(`scripts/apply_corrections.py`)", "(applied before the recount)")
audit = re.sub(r"arXiv ids are in `[^`]*`", "arXiv ids are in the reference list", audit)
audit = audit.replace("## Recount output (scripts/recount.py, merged corpus, all rows)", "## Recount output (merged corpus, all rows)")
audit = relabel(audit)
# drop the draft-line-number column of the claim tables
_out, _strip = [], False
for _ln in audit.split("\n"):
    if _ln.strip() == "| Line | Claim | Verdict | Evidence |":
        _strip = True; _out.append("| Claim | Verdict | Evidence |"); continue
    if _strip and _ln.startswith("|"):
        _out.append("|" + "|".join(_ln.split("|")[2:])); continue
    _strip = False
    _out.append(_ln)
audit = "\n".join(_out)
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

This document accompanies the main article. S1 is the released score table; S2–S5 carry the verification material behind the survey (the data appendix, the mechanism stack, the contrast set and matrix membership, and the walkthrough of the convergent research families); S6 audits every absolute claim of the first-pass draft against the full corpus and holds the rubric-reward comparison that Section IV of the main text summarizes; S7 is the extended related work, organized by the article's four design commitments. Section numbers in the form "Section N" refer to the main article.

**Key to the labels used throughout.** The substrate codes S1 to S6 name the six scaffold substrates of the main article (S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance) and are distinct from the section labels S1 to S7 of this document; INT marks a row scored across several substrates. C1 to C4 are the four feedback-signal classes of Section IV: exact, observable outcome, judged, and delayed and sparse. A system's two gates are written [Loop 1 × Loop 2] with the values Auto, Human, or None; Auto+Human marks a two-stage local gate, an algorithmic check followed by a reviewer. Stages 1 to 3 are the three stages of scaffold maintenance of Section III: patchwork, random artifact search, artifact-layer descent. Scopes nest USER within PROJECT within STACK within TENANT within CORE, where a tenant is one organization or customer; promotion that reaches CORE crosses tenants. Properties (a) to (d) are the four properties of the missing architecture in Section IX, and the five conditions are those of Section III. A system named without a citation is a row of the score table in Section S1, which gives its source.

"""
# S2-S6 are editable section files once materialized (python generate_supplementary.py --materialize writes
# them from the lifted text above, once). When a file exists it is the source of truth and the lifted
# text is ignored, so the appendices can be revised like any other section.
SFILES = {2: "S2_data.md", 3: "S3_mechanism.md", 4: "S4_contrast.md", 5: "S5_families.md", 6: "S6_audit.md"}
SEC_DIR = os.path.join(PKG, "submission", "sections")
lifted = {2: s2, 3: s3, 4: s4, 5: s5, 6: s6}
parts = {}
for n, fname in SFILES.items():
    path = os.path.join(SEC_DIR, fname)
    if os.path.exists(path):
        parts[n] = open(path, encoding="utf-8").read().strip("\n")
    else:
        parts[n] = lifted[n]
body = front + "\n\n".join([p for p in (s1, parts[2], parts[3], parts[4], parts[5], parts[6], s7) if p]) + "\n"

# Lifted tables carry equal-dash separators, which pandoc turns into equal column widths; give
# the long-text columns the width (dash counts are relative; cell text is untouched).
WIDTHS = {
    "| System | Year | Discriminator failure | Brief reason |": (16, 7, 24, 40),
    "| System | Year | Composite-criterion failure | Brief reason |": (16, 7, 24, 40),
    "| Section III quantity | SkillOpt instantiation | Section III role explained | Algorithm pointer |": (14, 24, 24, 24),
    "| Claim | Verdict | Evidence |": (28, 10, 46),
    "| Claim | Statement | Verdict | Evidence |": (5, 23, 10, 42),
}
for header, widths in WIDTHS.items():
    sep = "|" + "|".join("-" * w for w in widths) + "|"
    body = re.sub(r"(?m)^" + re.escape(header) + r"\n\|[-:|]+\|$", header + "\n" + sep, body)

if "--materialize" in sys.argv:
    # write S2-S6 as section files (post-substitution text, i.e. exactly what renders today); never overwrite
    for n, fname in SFILES.items():
        path = os.path.join(SEC_DIR, fname)
        if os.path.exists(path):
            print("exists, not overwritten:", fname); continue
        m = re.search(r"(?ms)^# S%d\. .*?(?=^# S%d\. |\Z)" % (n, n + 1), body)
        if not m:
            raise SystemExit("could not isolate S%d in the assembled body" % n)
        open(path, "w", encoding="utf-8", newline="\n").write(m.group(0).strip("\n") + "\n")
        print("materialized", fname, len(m.group(0).split()), "words")

open(OUT, "w", encoding="utf-8", newline="\n").write(body)
print("wrote", os.path.relpath(OUT, HERE), "rows:", len(rows))
