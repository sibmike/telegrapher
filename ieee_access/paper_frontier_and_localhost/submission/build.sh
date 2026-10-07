#!/usr/bin/env bash
# Build the IEEE Access submission of "Frontier and Localhost":
#   paper_frontier_and_localhost_ieee.md  --pandoc-->  body.tex (fragment, natbib cites)
#   abstract.md                           --pandoc-->  abstract.tex (plain paragraph)
#   main.tex (ieeeaccess.cls shell)        --pdflatex/bibtex-->  main.pdf
#   supplementary.md                      --pandoc/pdflatex-->  supplementary.pdf
#
# Citations: pandoc --natbib emits \citep{a; b} / \citet{k}; the sed step turns them into
# plain \cite{a,b} so the official template's `cite` package + IEEEtran.bst render IEEE
# numeric references. Write textual cites in the .md as "Author et al. [@key]" so nothing
# depends on \citet. Headings: --shift-heading-level-by=-1 maps "## I. Title" to \section.
#
# Requires: pandoc, pdflatex, bibtex (MiKTeX or TeX Live).

set -euo pipefail
cd "$(dirname "$0")"

export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"

command -v pandoc   > /dev/null || { echo "ERROR: pandoc not found."   >&2; exit 1; }
command -v pdflatex > /dev/null || { echo "ERROR: pdflatex not found." >&2; exit 1; }
command -v bibtex   > /dev/null || { echo "ERROR: bibtex not found."   >&2; exit 1; }

FROM="markdown+tex_math_dollars+pipe_tables+implicit_figures+yaml_metadata_block+raw_tex"

fix_cites () {  # \citep{a; b} -> \cite{a,b}; \citet{a} -> \cite{a}; strip prefixes/suffixes pandoc may add
  python_exe="${PYTHON:-C:/Users/${USER:-${USERNAME:-}}/anaconda3/python.exe}"
  "$python_exe" - "$1" <<'PYEOF'
import re, sys
p = sys.argv[1]; t = open(p, encoding="utf-8").read()
def fix(m):
    keys = [k.strip() for k in m.group(2).split(";")]
    return "\\cite{" + ",".join(keys) + "}"
# prefixed groups: \citetext{\citealp[Name,][]{a}; \citealp[Other,][]{b}} -> (Name~\cite{a}; Other~\cite{b})
def citetext(m):
    parts = re.findall(r"\\citealp\[([^\]]*)\]\[([^\]]*)\]\{([^}]*)\}", m.group(1))
    if not parts:
        return m.group(0)
    out = []
    for pre, suf, key in parts:
        pre = pre.strip().rstrip(",")
        out.append((pre + "~" if pre else "") + "\\cite{" + key.strip() + "}" + ((" " + suf.strip()) if suf.strip() else ""))
    return "(" + "; ".join(out) + ")"
t = re.sub(r"\\citetext\{((?:[^{}]|\{[^{}]*\})*)\}", citetext, t)
t = re.sub(r"\\citealp\[([^\]]*)\]\[([^\]]*)\]\{([^}]*)\}", lambda m: (m.group(1).strip().rstrip(",") + "~" if m.group(1).strip() else "") + "\\cite{" + m.group(3).strip() + "}", t)
t = re.sub(r"\\cite([pt])(?:\[[^\]]*\])*\{([^}]*)\}", fix, t)
# pandoc writes \citeauthor / \citeyear only for odd constructs; make them plain cites too
t = re.sub(r"\\cite(?:author|year|alp|alt)\*?\{([^}]*)\}", lambda m: "\\cite{" + m.group(1) + "}", t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
PYEOF
}

PYX="${PYTHON:-C:/Users/${USER:-${USERNAME:-}}/anaconda3/python.exe}"
echo "[0/6] assemble sections -> paper_frontier_and_localhost_ieee.md"
"$PYX" ../scripts/assemble.py

echo "[1/6] pandoc: abstract.md -> abstract.tex"
pandoc abstract.md --from="$FROM" --to=latex --wrap=none --output=abstract.tex

echo "[2/6] pandoc: paper_frontier_and_localhost_ieee.md -> body.tex (fragment, natbib cites)"
pandoc paper_frontier_and_localhost_ieee.md \
  --from="$FROM" --to=latex --wrap=none \
  --shift-heading-level-by=-1 \
  --natbib \
  --output=body.tex
fix_cites body.tex
"$PYX" ../scripts/fix_tables.py body.tex

echo "[3/6] pdflatex pass 1"
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
echo "[4/6] bibtex"
bibtex main > /dev/null || true
echo "[5/6] pdflatex passes 2 and 3"
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
echo "Build complete: main.pdf ($(grep -o 'Output written on main.pdf ([0-9]* pages' main.log | tail -1))"

if [ -f supplementary.md ]; then
  echo "[6/6] supplementary.md -> supplementary.pdf"
  pandoc supplementary.md \
    --from="$FROM" --to=latex --standalone \
    --natbib --bibliography=references.bib -V biblio-style=IEEEtran -V natbiboptions='numbers,sort&compress' \
    -V geometry:margin=1in -V graphics=true \
    -V header-includes='\usepackage{longtable,booktabs}\DeclareUnicodeCharacter{200B}{\hskip0pt}\DeclareUnicodeCharacter{2260}{\ensuremath{\neq}}\DeclareUnicodeCharacter{2265}{\ensuremath{\geq}}\DeclareUnicodeCharacter{2264}{\ensuremath{\leq}}\DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}\DeclareUnicodeCharacter{2282}{\ensuremath{\subset}}\DeclareUnicodeCharacter{2248}{\ensuremath{\approx}}\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}\DeclareUnicodeCharacter{2211}{\ensuremath{\sum}}\DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}\DeclareUnicodeCharacter{03B5}{\ensuremath{\varepsilon}}\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}\DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}\DeclareUnicodeCharacter{03A9}{\ensuremath{\Omega}}\DeclareUnicodeCharacter{03B8}{\ensuremath{\theta}}\DeclareUnicodeCharacter{2208}{\ensuremath{\in}}\DeclareUnicodeCharacter{2026}{\ldots}\DeclareUnicodeCharacter{2020}{\dag}\DeclareUnicodeCharacter{2021}{\ddag}\DeclareUnicodeCharacter{00A7}{\S}\DeclareUnicodeCharacter{03BA}{\ensuremath{\kappa}}\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}\DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}\DeclareUnicodeCharacter{03B3}{\ensuremath{\gamma}}\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}\DeclareUnicodeCharacter{2218}{\ensuremath{\circ}}\DeclareUnicodeCharacter{2212}{-}\DeclareUnicodeCharacter{2019}{\textquoteright}\DeclareUnicodeCharacter{2018}{\textquoteleft}\DeclareUnicodeCharacter{201C}{\textquotedblleft}\DeclareUnicodeCharacter{201D}{\textquotedblright}\DeclareUnicodeCharacter{2070}{\ensuremath{^0}}\DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}\DeclareUnicodeCharacter{2264}{\ensuremath{\leq}}' \
    --output=supplementary.tex
  fix_cites supplementary.tex
  pdflatex -interaction=nonstopmode -halt-on-error supplementary.tex > /dev/null
  bibtex supplementary > /dev/null || true
  pdflatex -interaction=nonstopmode -halt-on-error supplementary.tex > /dev/null
  pdflatex -interaction=nonstopmode -halt-on-error supplementary.tex > /dev/null
  echo "Supplementary built: supplementary.pdf"
fi
