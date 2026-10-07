"""Checks for the readability revision (reorganize and reword; no new evidence).

Compares submission/sections_before/ (snapshot, incl. abstract.md) with submission/sections/ + submission/abstract.md:
  (a) document-wide citation multiset unchanged (keys may move between files);
  (b) every number that left the prose still appears in a table row, a caption tag, or the appendices;
  (c) banned process vocabulary absent outside the method subsection "How the corpus was assembled" and S2;
  (d) first use of each label system comes after its definition, in body order;
  (e) labels scheduled for removal are absent from the body;
  (f) supplementary pointers appear only as "(Supplementary Material S<n>)".

Usage: python check_revision.py [--quiet]     (exit 1 on any failure in a, e, f; b–d are reported)
"""
import os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(HERE, "..", "submission")
BEFORE, AFTER = os.path.join(SUB, "sections_before"), os.path.join(SUB, "sections")
BODY = ["I_III.md", "IV_feedback_signal_classes.md", "V_method.md", "VI_findings.md", "VII_design_space.md",
        "VIII_families.md", "IX_missing_architecture.md", "X_failure_surface.md", "XI_open_problems_conclusion.md"]
APPX = ["appA_formal.md", "appB_gates.md"]
SUPP = sorted(os.path.basename(p) for p in glob.glob(os.path.join(AFTER, "S[0-9]_*.md")))
ALL = BODY + APPX + SUPP

def rd(p): return open(p, encoding="utf-8").read() if os.path.exists(p) else ""
def after(name): return rd(os.path.join(SUB, "abstract.md")) if name == "abstract.md" else rd(os.path.join(AFTER, name))
def before(name): return rd(os.path.join(BEFORE, name))

NUM = r"(?<![A-Za-z@:_\-])\d[\d,]*(?:\.\d+)?%?"
def cites(t): return collections.Counter(re.findall(r"@([A-Za-z][A-Za-z0-9_]+)", t))
def nums(t): return collections.Counter(s.rstrip(",") for s in re.findall(NUM, t))
def prose_lines(t):
    """Lines that are prose: not table rows, not caption tags, not raw latex, not headings."""
    out, raw = [], False
    for ln in t.split("\n"):
        if ln.startswith("```"): raw = not raw; continue
        if raw or ln.startswith("|") or re.match(r"^Table [IVXA-Z]+-\d+\.", ln) or ln.startswith("#"): continue
        out.append(ln)
    return "\n".join(out)
def nonprose(t):
    return "\n".join(ln for ln in t.split("\n") if ln.startswith("|") or re.match(r"^Table [IVXA-Z]+-\d+\.", ln))

quiet = "--quiet" in sys.argv
fail = False
names = ["abstract.md"] + ALL

# ---- (a) citations, document-wide
cb = sum((cites(before(n)) for n in names), collections.Counter())
ca = sum((cites(after(n)) for n in names), collections.Counter())
ALLOWED_NEW = {"bhattarai2026rubricgrounded", "jia2026openrubric", "lv2026queryrubrics"}   # in the bib from the same sweep; cited in Appendix G so the 8/5 tally is checkable
gone, new = set(cb) - set(ca), set(ca) - set(cb) - ALLOWED_NEW      # the KEY SET must be unchanged; occurrence counts may move
print("(a) citations: before %d keys / after %d keys (%d -> %d occurrences)" % (len(cb), len(ca), sum(cb.values()), sum(ca.values())))
if gone or new:
    fail = True
    if gone: print("    REMOVED keys:", sorted(gone))
    if new: print("    ADDED keys:", sorted(new))
else:
    moved = {k: (cb[k], ca[k]) for k in cb if cb[k] != ca[k]}
    print("    OK: same key set" + ("; occurrence counts changed for " + str(moved) if moved else ""))

# ---- (b) numbers that left the prose
prose_b = sum((nums(prose_lines(before(n))) for n in ["abstract.md"] + BODY), collections.Counter())
prose_a = sum((nums(prose_lines(after(n))) for n in ["abstract.md"] + BODY), collections.Counter())
left = prose_b - prose_a
haven = "\n".join(nonprose(after(n)) for n in names) + "\n".join(after(n) for n in APPX + SUPP) + rd(os.path.join(SUB, "supplementary.md"))
haven_nums = nums(haven)
unaccounted = [k for k in left if k not in haven_nums and not re.fullmatch(r"20\d\d", k)]
print("(b) numbers: %d distinct left the prose; %d not found in any table, caption, or appendix" % (len(left), len(unaccounted)))
if unaccounted and not quiet:
    print("    not found:", sorted(unaccounted, key=lambda s: (len(s), s)))
added_nums = prose_a - prose_b
if added_nums and not quiet:
    print("    NEW numbers in prose (check each is a relocation, not new evidence):", dict(added_nums))

# ---- (c) banned vocabulary
BANNED = [r"\bsweeps?\b", r"\b(first|second) pass\b", r"\brefresh\b", r"May[- ]2026", r"May corpus", r"October[- ]2026",
          r"\b2026 (additions|entries|systems|sweep|registries|research|harness papers|retirement)", r"added in 2026", r"\bin 2026\b",
          r"we were (not )?looking for", r"\bwe checked\b", r"claims audit", r"\brescored\b", r"has arrived", r"has become routine",
          r"\bnow (exists|appears|shipped)\b"]
hits = []
for n in ["abstract.md"] + BODY + APPX:
    t = after(n)
    allowed = ""
    if n == "V_method.md":
        m = re.search(r"(?ms)^### How the corpus was assembled.*?(?=^### )", t)
        allowed = m.group(0) if m else ""
    for i, ln in enumerate(t.split("\n"), 1):
        if allowed and ln in allowed: continue
        for pat in BANNED:
            for m in re.finditer(pat, ln):
                hits.append((n, i, m.group(0), ln[max(0, m.start() - 50):m.end() + 50].replace("\n", " ")))
print("(c) banned process vocabulary outside V-B: %d hits" % len(hits))
if not quiet:
    for h in hits[:60]: print("    %s:%d  [%s]  ...%s..." % h)

# ---- (c2) appendix files: the strict process words and the audit's author-instruction phrasing (report only;
#      "first pass" / "second pass" are allowed there as scope statements)
APPX_BANNED = [r"\bsweeps?\b", r"\brefresh\b", r"we were (not )?looking for", r"\bwe checked\b", r"\brescored\b",
               r"IEEE (version|text)", r"Removed from the", r"\bSay \"", r"\bRestate\b", r"\bSee \d{3}\b", r"\b127\b", r"\bPP\b",
               r"single-loop boundary", r"Appendix XII-D"]
hits2 = [(n, i, m.group(0)) for n in SUPP for i, ln in enumerate(after(n).split("\n"), 1) for pat in APPX_BANNED for m in re.finditer(pat, ln)]
print("(c2) appendix files, process or author-instruction phrasing: %d hits" % len(hits2))
if not quiet:
    for h in hits2[:40]: print("    %s:%d  [%s]" % h)

# ---- (d) label order (first use must follow its definition), in body order
order = ["abstract.md"] + BODY
def first_use(pat, exclude=None):
    for n in order:
        for i, ln in enumerate(after(n).split("\n"), 1):
            for m in re.finditer(pat, ln):
                if exclude and re.search(exclude, ln[max(0, m.start() - 25):m.start()]): continue
                return n, i
    return None
def first_def(pat):
    return first_use(pat)
checks = [
    ("[L1 x L2] cell notation", r"\[(Auto|Human|None) × (Auto|Human|None)\]", r"Loop 1 first", None),
    ("C1-C4 classes", r"\bC[1-4]\b", r"\*\*C1, exact\.\*\*|C1 exact", r"Table IV-1|CVE"),
    ("properties (a)-(d)", r"propert(y|ies) \((a|b|c|d)\)|\((a|b|c|d)\) \*\*", r"- \(a\) \*\*auto-gated Loop 1", None),
    ("tenant", r"\btenant", r"one organization or customer", None),
    ("patch", r"\bpatch\b", r"patch\*\* |\*\*patch\*\*|a patch is|call a patch|the patch, the slice|\bpatch\b[^.]*slice", None),
    ("evidence radius", r"evidence radius", r"evidence radius\*\*|\*\*evidence radius|call[^.]*evidence radius", None),
    ("receiving-side evaluation", r"receiving-side", r"receiving-side[^.]*(arrives|where the edit)", None),
    ("S1-S6 substrate codes", r"\bS[1-6]\b", r"\| S1 Instructions", r"Supplementary Material|Section "),
]
print("(d) label order (definition must precede first use):")
for label, use_pat, def_pat, excl in checks:
    u, d = first_use(use_pat, excl), first_def(def_pat)
    ok = (u is None) or (d is not None and (order.index(d[0]), d[1]) <= (order.index(u[0]), u[1]))
    print("    %-28s first use %-34s definition %-34s %s" % (label, u, d, "OK" if ok else "BEFORE DEFINITION"))

# ---- (e) removed labels
REMOVED = [r"Claim IV-", r"\(A2\)", r"single-loop boundary", r"Loop 1 = None", r"\$n = 1\$", r"\bPP\b", r"assumption \((i|ii|iii|iv|v|vi)\)", r"Condition \((iii|iv|v)\)"]
APPX_REMOVED = [r"assumption \((i|ii|iii|iv|v|vi)\) of Section"]      # Appendix A keeps its own (A1)-(A5)
rem_hits = [(n, i, m.group(0)) for n in ["abstract.md"] + BODY for i, ln in enumerate(after(n).split("\n"), 1) for pat in REMOVED for m in re.finditer(pat, ln)]
rem_hits += [(n, i, m.group(0)) for n in APPX for i, ln in enumerate(after(n).split("\n"), 1) for pat in APPX_REMOVED for m in re.finditer(pat, ln)]
print("(e) removed labels still present: %d" % len(rem_hits))
for h in rem_hits: print("    %s:%d  %s" % h); fail = True

# ---- (f) supplementary pointers
ptr_bad = []
for n in ["abstract.md"] + BODY + APPX:
    for i, ln in enumerate(after(n).split("\n"), 1):
        for m in re.finditer(r"Supplementary( Material)? S\d(\.\d+)?", ln):
            ctx = ln[max(0, m.start() - 1):m.end() + 1]
            if not (ctx.startswith("(") and ctx.endswith(")")):
                ptr_bad.append((n, i, ln[max(0, m.start() - 40):m.end() + 20]))
print("(f) supplementary pointers not in '(Supplementary Material S<n>)' form: %d" % len(ptr_bad))
for h in ptr_bad: print("    %s:%d  ...%s..." % h); fail = True

words_b = sum(len(prose_lines(before(n)).split()) for n in ["abstract.md"] + BODY)
words_a = sum(len(prose_lines(after(n)).split()) for n in ["abstract.md"] + BODY)
print("body prose words: %d -> %d (%+.0f%%)" % (words_b, words_a, 100.0 * (words_a - words_b) / max(words_b, 1)))
print("\nREVISION CHECK:", "FAIL" if fail else "PASS (a, e, f); review b-d above")
sys.exit(1 if fail else 0)
