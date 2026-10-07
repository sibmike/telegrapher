#!/usr/bin/env bash
# Build the arXiv version of Frontier and Localhost (v4, October 2026).
#
#   IEEE Access package sections ──assemble_arxiv.py──► paper_frontier_and_localhost.md
#       ──pandoc (--natbib)──► .tex ──postprocess_tex.py──► pdflatex → bibtex → pdflatex ×2 ──► .pdf
#       ──zip──► paper_frontier_and_localhost.zip  (tex + bbl + figures/*.pdf + anc/)
#
# The source of truth is ../../../ieee_access/paper_frontier_and_localhost (its sections, abstract,
# generated supplementary, references.bib, figures, and score CSVs); this directory holds derived copies.
# pdflatex + article class, as in the series' earlier arXiv package (Beyond Exponential Decay); arXiv does
# not run BibTeX, so the .bbl ships in the zip.
#
# Requires: pandoc, pdflatex, bibtex (MiKTeX or TeX Live), python (PYTHON=... to override).

set -euo pipefail
cd "$(dirname "$0")"

export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"
PY="${PYTHON:-C:/Users/${USER:-${USERNAME:-}}/anaconda3/python.exe}"
IEEE="../../../ieee_access/paper_frontier_and_localhost"
STEM="paper_frontier_and_localhost"

command -v pandoc   > /dev/null || { echo "ERROR: pandoc not found" >&2; exit 1; }
command -v pdflatex > /dev/null || { echo "ERROR: pdflatex not found" >&2; exit 1; }

echo "[1/7] mirror inputs from the IEEE package"
cp "$IEEE/submission/references.bib" references.bib
for f in fig1_descent fig2_scope fig3_design_space fig4_corpus_flow; do
  cp "$IEEE/submission/figures/${f}_ieee.pdf" "figures/${f}.pdf"
done
cp "$IEEE/supplementary/p3_master_scores.csv" "$IEEE/supplementary/p3_refresh_2026-10.csv" anc/
cp "$IEEE/scripts/recount.py" anc/recount.py

echo "[2/7] assemble $STEM.md"
"$PY" assemble_arxiv.py

echo "[3/7] pandoc: $STEM.md -> $STEM.tex"
pandoc "$STEM.md" \
  --from=markdown+tex_math_dollars+implicit_figures+pipe_tables+yaml_metadata_block+raw_tex \
  --to=latex --standalone --natbib --number-sections \
  --shift-heading-level-by=-1 --wrap=none \
  -V biblio-style=IEEEtran -V natbiboptions='numbers,sort&compress' \
  -V geometry:margin=1in -V graphics=true -V fontsize=11pt -V colorlinks=true \
  --output="$STEM.tex"

echo "[4/7] post-process citations, tables, cross-references"
"$PY" postprocess_tex.py "$STEM.tex"

echo "[5/7] pdflatex -> bibtex -> pdflatex x2"
pdflatex -interaction=nonstopmode -halt-on-error "$STEM.tex" > /dev/null
bibtex "$STEM" > /dev/null || { echo "bibtex reported errors:"; grep -i "error\|warning--" "$STEM.blg" | head; }
pdflatex -interaction=nonstopmode -halt-on-error "$STEM.tex" > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error "$STEM.tex" > /dev/null

echo "[6/7] checks"
pages=$(grep -o "Output written on $STEM.pdf ([0-9]* pages" "$STEM.log" | grep -o "[0-9]* pages")
undef_ref=$(grep -c "Reference .* undefined" "$STEM.log" || true)
undef_cite=$(grep -c "Citation .* undefined" "$STEM.log" || true)
multiply=$(grep -c "multiply defined" "$STEM.log" || true)
bibitems=$(grep -c "^\\\\bibitem" "$STEM.bbl" || true)
cited=$(grep -o "\\\\citation{[^}]*}" "$STEM.aux" | sed 's/\\citation{//;s/}//' | tr ',' '\n' | sort -u | wc -l)
overfull=$(grep -c "Overfull .hbox" "$STEM.log" || true)
echo "  pages: $pages | undefined refs: $undef_ref | undefined cites: $undef_cite | multiply defined: $multiply"
echo "  cited keys: $cited | bibitems: $bibitems | overfull hboxes: $overfull"
bad=$(find . -type f -not -path "./.*" | grep -v -E '^\./[a-zA-Z0-9_./+-]+$' || true)
[ -z "$bad" ] || { echo "  filenames outside arXiv's character set:"; echo "$bad"; }

echo "[7/7] zip for arXiv upload"
rm -f "$STEM.zip"
zip -q -r "$STEM.zip" "$STEM.tex" "$STEM.bbl" figures/fig1_descent.pdf figures/fig2_scope.pdf figures/fig3_design_space.pdf figures/fig4_corpus_flow.pdf anc
ls -la "$STEM.pdf" "$STEM.zip"
