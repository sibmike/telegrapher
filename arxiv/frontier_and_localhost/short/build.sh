#!/usr/bin/env bash
# Build paper_frontier_and_localhost_short for arXiv: Markdown -> LaTeX -> PDF
#
# Short / compressed version of the Frontier and Localhost paper. Body fits a
# 9-page budget; appendix is unconstrained and absorbs every piece of
# verification-grade material from the long version. The arXiv source bundle
# (paper_frontier_and_localhost_short.zip) ships the .tex plus the full
# supplementary/ tree so reviewers can re-run the survey discriminator.
#
# Requires: pandoc, xelatex (MiKTeX or TeX Live)

set -euo pipefail
cd "$(dirname "$0")"

export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"

command -v pandoc  > /dev/null || { echo "ERROR: pandoc not found.  Install: winget install JohnMacFarlane.Pandoc  (Win), brew install pandoc  (Mac), apt install pandoc  (Linux)" >&2; exit 1; }
command -v xelatex > /dev/null || { echo "ERROR: xelatex not found. Install MiKTeX (Win), MacTeX (Mac), or TeX Live (Linux)." >&2; exit 1; }

echo "[1/3] pandoc: paper_frontier_and_localhost_short.md -> paper_frontier_and_localhost_short.tex"
pandoc paper_frontier_and_localhost_short.md \
  --from=markdown+tex_math_dollars+implicit_figures+pipe_tables+yaml_metadata_block \
  --to=latex \
  --standalone \
  --pdf-engine=xelatex \
  --citeproc \
  --bibliography=references.bib \
  -M link-citations=true \
  -V geometry:margin=1in \
  -V graphics=true \
  -V mainfont="Cambria" \
  -V mainfontoptions="Ligatures=TeX" \
  -V monofont="Consolas" \
  --output=paper_frontier_and_localhost_short.tex
# Citations: references.bib is now the single source of truth. pandoc --citeproc
# resolves [@key] inline cites and generates the reference list at conversion
# time (rendered directly into the .tex, so no .bib/.csl ships to arXiv).
# Style is citeproc's built-in default (Chicago author-date); add --csl=FILE.csl
# here to change it. Undefined [@key] cites surface as pandoc warnings above.

echo "[2/3] xelatex pass 1"
xelatex -interaction=nonstopmode -halt-on-error paper_frontier_and_localhost_short.tex > /dev/null

echo "[3/3] xelatex pass 2 (for cross-refs and longtable settling)"
xelatex -interaction=nonstopmode -halt-on-error paper_frontier_and_localhost_short.tex > /dev/null

echo "Build complete: paper_frontier_and_localhost_short.pdf"
ls -la paper_frontier_and_localhost_short.pdf

echo "[zip] Packaging arXiv source bundle (tex + supplementary)"
rm -f paper_frontier_and_localhost_short.zip
if [ -d supplementary ]; then
  zip -r paper_frontier_and_localhost_short.zip paper_frontier_and_localhost_short.tex supplementary > /dev/null
else
  zip paper_frontier_and_localhost_short.zip paper_frontier_and_localhost_short.tex > /dev/null
fi
ls -la paper_frontier_and_localhost_short.zip
