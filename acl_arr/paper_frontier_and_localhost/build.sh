#!/usr/bin/env bash
# Build the ACL Rolling Review version of "Frontier and Localhost".
#   abstract.md, body.md, limitations.md, appendix.md  --pandoc (natbib)-->  *.tex fragments
#   main.tex (acl.sty in review mode if present, else an ACL-geometry stand-in)  --pdflatex/bibtex-->  main.pdf
# Cites: [@key] -> \citep, @key -> \citet (ACL author-year). Cross-references: REF(label) -> \ref{label}.
# Inputs mirrored from the IEEE package: references.bib and three figure PDFs. Figure 1 is ACL-specific
# (its promotion box points to Section 6); regenerate it with
#   make_figures.py --ieee --out <dir> --promo-pointer "(Section 6)"   and copy fig1_descent_ieee.pdf to figures/fig1_descent.pdf
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"
PYX="${PYTHON:-C:/Users/${USER:-${USERNAME:-}}/anaconda3/python.exe}"
IEEE=../../ieee_access/paper_frontier_and_localhost

echo "[1/5] mirror references.bib and figures from the IEEE package"
mkdir -p figures
cp "$IEEE/submission/references.bib" references.bib
for f in fig2_scope fig3_design_space fig4_corpus_flow; do
  cp "$IEEE/submission/figures/${f}_ieee.pdf" "figures/${f}.pdf"
done

echo "[2/5] pandoc fragments"
FROM="markdown+tex_math_dollars+pipe_tables+raw_tex+raw_attribute"
for part in abstract body limitations appendix; do
  pandoc "$part.md" --from="$FROM" --to=latex --natbib --wrap=none --shift-heading-level-by=-1 --output="$part.tex"
done

echo "[3/5] post-process: cross-references"
"$PYX" - <<'PYEOF'
import re
for part in ["abstract", "body", "limitations", "appendix"]:
    p = part + ".tex"; t = open(p, encoding="utf-8").read()
    t = re.sub(r"(Section|Sections|Fig\.|Figs\.|Table|Tables|Appendix|Appendices)\s+REF\(([^)]+)\)", r"\1~\\ref{\2}", t)
    t = re.sub(r"REF\(([^)]+)\)", r"\\ref{\1}", t)
    open(p, "w", encoding="utf-8", newline="\n").write(t)
PYEOF

echo "[4/5] pdflatex -> bibtex -> pdflatex x2"
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null || { tail -30 main.log; exit 1; }
bibtex main > /dev/null || true
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

echo "[5/5] checks"
"$PYX" - <<'PYEOF'
import re, subprocess
log = open("main.log", encoding="latin-1").read()
pages = re.findall(r"Output written on main.pdf \((\d+) pages", log)
undef_ref = len(re.findall(r"Reference `[^']+' on page \d+ undefined", log))
undef_cit = len(re.findall(r"Citation `[^']+' on page \d+ undefined", log))
official = "acl.sty" in log
txt = subprocess.run(["pdftotext", "main.pdf", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
pp = txt.split("\f")
# the heading may share an extracted line with the other column, so look for a line that ends with it
lim = next((i + 1 for i, pg in enumerate(pp) if any(l.rstrip().endswith("Limitations") for l in pg.split("\n"))), None)
print(f"  style: {'official acl.sty (review)' if official else 'ACL-geometry stand-in'}")
print(f"  pages: {pages[-1] if pages else '?'} | undefined refs: {undef_ref} | undefined cites: {undef_cit}")
print(f"  Limitations heading on page {lim}; the body must end on page 8 or earlier: {'OK' if lim and lim <= 9 else 'CHECK'}")
PYEOF
ls -la main.pdf
