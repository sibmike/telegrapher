"""Show, for one section, every sentence of the BEFORE text containing a given token that has no
exact counterpart in the AFTER text, and vice versa. Usage: diff_tokens.py <section.md> <token> [<token> ...]"""
import os, re, sys
SUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "submission")
name, tokens = sys.argv[1], sys.argv[2:]
b = open(os.path.join(SUB, "sections_before", name), encoding="utf-8").read()
a = open(os.path.join(SUB, "sections", name), encoding="utf-8").read()
def sents(t): return [s.strip() for s in re.split(r"(?<=[.;|])\s+", t) if s.strip()]
sb, sa = sents(b), sents(a)
for tok in tokens:
    print(f"=== token {tok!r}")
    for s in sb:
        if tok in s and s not in sa: print("  BEFORE only:", s[:220])
    for s in sa:
        if tok in s and s not in sb: print("  AFTER  only:", s[:220])
