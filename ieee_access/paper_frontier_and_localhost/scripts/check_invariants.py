"""Claims-invariance check for a style/texture pass: for each section file, the multiset of citation keys,
the set of numbers, the set of REF(...) cross-reference tokens, and the table/figure skeleton must be
identical between submission/sections_before/ and submission/sections/. Prose may change freely.

Usage: python check_invariants.py   (exit 1 on any difference)
"""
import os, re, sys, glob, collections
SUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "submission")
BEFORE, AFTER = os.path.join(SUB, "sections_before"), os.path.join(SUB, "sections")

def features(text):
    body = re.sub(r"```\{=latex\}.*?```", lambda m: m.group(0), text, flags=re.S)
    cites = collections.Counter(re.findall(r"@([A-Za-z][A-Za-z0-9_]+)", body))
    nums = collections.Counter(re.findall(r"(?<![A-Za-z@:_\-])\d[\d,]*(?:\.\d+)?%?", body))
    refs = collections.Counter(re.findall(r"REF\([^)]+\)", body))
    tables = len(re.findall(r"^\|---", body, re.M))
    captions = re.findall(r"^Table [IVXAB]+-\d+\.", body, re.M)
    figs = re.findall(r"\\includegraphics\[[^\]]*\]\{([^}]+)\}", body)
    heads = re.findall(r"^#{2,3} .*$", body, re.M)
    return cites, nums, refs, tables, captions, figs, heads

ok = True
for f in sorted(glob.glob(os.path.join(AFTER, "*.md"))):
    name = os.path.basename(f)
    b = os.path.join(BEFORE, name)
    if not os.path.exists(b):
        print(f"NEW  {name}"); continue
    fb, fa = features(open(b, encoding="utf-8").read()), features(open(f, encoding="utf-8").read())
    labels = ["citation keys", "numbers", "cross-refs", "table count", "table captions", "figures", "headings"]
    diffs = []
    for lab, x, y in zip(labels, fb, fa):
        if x != y:
            if isinstance(x, collections.Counter):
                gone, new = x - y, y - x
                diffs.append(f"{lab}: removed {dict(gone)} added {dict(new)}")
            else:
                diffs.append(f"{lab}: {x} -> {y}")
    if diffs:
        ok = False; print(f"DIFF {name}"); [print("   ", d) for d in diffs]
    else:
        print(f"OK   {name}")
print("\nINVARIANTS:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
