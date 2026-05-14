#!/usr/bin/env bash
# Build paper_architecture_of_errors for arXiv: Markdown -> LaTeX -> PDF
#
# Requires: pandoc, xelatex (MiKTeX or TeX Live)
# Produces: paper_architecture_of_errors.tex, paper_architecture_of_errors.pdf
#
# Zip for arXiv upload after build succeeds:
#   zip paper_architecture_of_errors.zip paper_architecture_of_errors.tex
# (No figures in this synthesis paper, so the zip is .tex only.)

set -euo pipefail
cd "$(dirname "$0")"

# Common Windows install locations (harmless on macOS/Linux). winget installs
# sometimes don't add their bin dirs to the current shell's PATH.
export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"

command -v pandoc  > /dev/null || { echo "ERROR: pandoc not found.  Install: winget install JohnMacFarlane.Pandoc  (Win), brew install pandoc  (Mac), apt install pandoc  (Linux)" >&2; exit 1; }
command -v xelatex > /dev/null || { echo "ERROR: xelatex not found. Install MiKTeX (Win), MacTeX (Mac), or TeX Live (Linux)." >&2; exit 1; }

# Title and author come from the YAML front-matter in the .md, so pandoc
# renders a single \title{...}/\author{...}/\maketitle block.
#
# XeLaTeX is mandatory: the paper uses Greek letters (alpha, beta, sigma,
# epsilon, Theta) and en/em dashes that pdflatex cannot render without
# explicit \DeclareUnicodeCharacter declarations per glyph.
#
# mainfont=Cambria and monofont=Consolas are picked because Latin Modern
# (the pandoc/xelatex default) lacks some Unicode glyphs the paper uses
# (currency, arrows in some prose). Both fonts ship with Windows.

echo "[1/3] pandoc: paper_architecture_of_errors.md -> paper_architecture_of_errors.tex"
pandoc paper_architecture_of_errors.md \
  --from=markdown+tex_math_dollars+implicit_figures+pipe_tables+yaml_metadata_block \
  --to=latex \
  --standalone \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V graphics=true \
  -V mainfont="Cambria" \
  -V monofont="Consolas" \
  --output=paper_architecture_of_errors.tex

echo "[2/3] xelatex pass 1"
xelatex -interaction=nonstopmode -halt-on-error paper_architecture_of_errors.tex > /dev/null

echo "[3/3] xelatex pass 2 (for cross-refs and longtable settling)"
xelatex -interaction=nonstopmode -halt-on-error paper_architecture_of_errors.tex > /dev/null

echo "Build complete: paper_architecture_of_errors.pdf"
ls -la paper_architecture_of_errors.pdf
