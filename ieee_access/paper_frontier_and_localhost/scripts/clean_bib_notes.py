"""Remove annotation-style `note` fields from references.bib (IEEEtran.bst prints notes in the reference list).

Keeps notes that carry publication information (an arXiv id, a DOI, 'accepted', 'to appear', 'forthcoming');
drops tier tags, verification remarks, one-line summaries, and access dates (access dates belong in `howpublished`
or `urldate`, which the sweeps already set where relevant).
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "..", "submission", "references.bib")
t = open(B, encoding="utf-8").read()
KEEP = re.compile(r"arXiv:\d|doi|accepted|to appear|forthcoming|in press|published as", re.I)
removed = []
def strip(m):
    note = m.group(2)
    if KEEP.search(note):
        return m.group(0)
    removed.append(note[:60])
    return ""
t2 = re.sub(r"^(\s*note\s*=\s*\{)((?:[^{}]|\{[^{}]*\})*)\},?\s*\n", strip, t, flags=re.M)
# tidy trailing commas before closing braces left by removed last fields
t2 = re.sub(r",(\s*\n\})", r"\1", t2)
open(B, "w", encoding="utf-8", newline="\n").write(t2)
print("notes removed:", len(removed))
for n in removed[:12]: print("  -", n)
