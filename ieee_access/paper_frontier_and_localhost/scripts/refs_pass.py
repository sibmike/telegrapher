"""Rewrite section drafts to the cross-reference scheme used by the build.

- Headings lose manual numerals/letters ("## IV. Title" -> "## Title {#sec:signal}"); the IEEE
  class numbers them. Section ids come from SECTION_IDS below (by Roman numeral or appendix letter).
- Subsection headings "### A. Title" -> "### Title".
- In-text references become REF tokens that fix_tables.py turns into \ref:
    "Section III" -> "Section REF(sec:loop)"; "Fig. 2" -> "Fig. REF(fig:scope)";
    "Table IV-1" -> "Table REF(tab:IV-1)"; "Appendix A" -> "Appendix REF(app:formal)";
    "(§VII)" -> "(Sec. REF(sec:design))".
- "Table IV-1." caption tags are kept (fix_tables.py uses them for \label{tab:IV-1}).
Idempotent: safe to run again on already-converted files.
"""
import os, re, glob

SEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "submission", "sections")
SECTION_IDS = {"I": "sec:intro", "II": "sec:why", "III": "sec:loop", "IV": "sec:signal", "V": "sec:method",
               "VI": "sec:findings", "VII": "sec:design", "VIII": "sec:families", "IX": "sec:gap",
               "X": "sec:failure", "XI": "sec:open", "A": "app:formal", "B": "app:gates"}
FIG_IDS = {"1": "fig:descent", "2": "fig:scope", "3": "fig:design", "4": "fig:corpus"}

def convert(t):
    # headings
    def h2(m):
        kind, num, title = m.group(1), m.group(2), m.group(3)
        key = num
        sid = SECTION_IDS.get(key)
        return f"## {title} {{#{sid}}}" if sid else f"## {title}"
    t = re.sub(r"^## (?:(Appendix) )?([IVX]+|[AB])\. (.+?)(?: \{#[^}]+\})?$", lambda m: h2(m) if not m.group(1) else f"## Appendix: {m.group(3)} {{#{SECTION_IDS[m.group(2)]}}}", t, flags=re.M)
    t = re.sub(r"^### [A-Z]\. ", "### ", t, flags=re.M)
    # references (skip caption tags like "Table IV-1." at line start)
    def sec_ref(m):
        return f"{m.group(1)} REF({SECTION_IDS[m.group(2)]})"
    t = re.sub(r"\b(Section|Sections)\s+([IVX]+)\b(?!-\d)", sec_ref, t)
    t = re.sub(r"(Sections REF\([^)]+\))\s+(and|to)\s+([IVX]+)\b", lambda m: f"{m.group(1)} {m.group(2)} REF({SECTION_IDS[m.group(3)]})", t)
    t = re.sub(r"\(§([IVX]+)\)", lambda m: f"(Sec. REF({SECTION_IDS[m.group(1)]}))", t)
    t = re.sub(r"§([IVX]+)\b(?!-)", lambda m: f"Sec. REF({SECTION_IDS[m.group(1)]})", t)
    t = re.sub(r"\bAppendix ([AB])\b(?! \{)", lambda m: f"Appendix REF({SECTION_IDS[m.group(1)]})", t)
    t = re.sub(r"\bFig\.\s+([1-4])\b", lambda m: f"Fig. REF({FIG_IDS[m.group(1)]})", t)
    t = re.sub(r"(?<!^)(?<!\n)\bTable ([IVXAB]+-\d)\b(?!\.)", lambda m: f"Table REF(tab:{m.group(1)})", t)
    return t

for f in sorted(glob.glob(os.path.join(SEC, "*.md"))):
    if os.path.basename(f) == "00_front.md":
        continue
    t = open(f, encoding="utf-8").read()
    t2 = convert(t)
    if t2 != t:
        open(f, "w", encoding="utf-8", newline="\n").write(t2)
        print("rewrote", os.path.basename(f))
