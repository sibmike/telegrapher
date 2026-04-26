#!/usr/bin/env bash
# Build paper_telegraph_english for arXiv: Markdown -> LaTeX -> PDF
#
# Requires: pandoc, xelatex (MiKTeX or TeX Live)
# Produces: paper_telegraph_english.tex, paper_telegraph_english.pdf
#
# Zip for arXiv upload after build succeeds:
#   zip -r paper_telegraph_english.zip paper_telegraph_english.tex figures/

set -euo pipefail
cd "$(dirname "$0")"

# Common Windows install locations (harmless on macOS/Linux). winget installs
# sometimes don't add their bin dirs to the current shell's PATH.
export PATH="$PATH:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Pandoc:/c/Users/${USER:-${USERNAME:-}}/AppData/Local/Programs/MiKTeX/miktex/bin/x64:/c/Program Files/Pandoc:/c/Program Files/MiKTeX/miktex/bin/x64"

command -v pandoc  > /dev/null || { echo "ERROR: pandoc not found.  Install: winget install JohnMacFarlane.Pandoc  (Win), brew install pandoc  (Mac), apt install pandoc  (Linux)" >&2; exit 1; }
command -v xelatex > /dev/null || { echo "ERROR: xelatex not found. Install MiKTeX (Win), MacTeX (Mac), or TeX Live (Linux)." >&2; exit 1; }

# Title and author come from the YAML front-matter at the top of the .md, so
# pandoc renders a single \title{...}/\author{...}/\maketitle block rather
# than duplicating with --metadata.
#
# XeLaTeX is mandatory: §3.2's symbol vocabulary table contains Unicode
# logical operators (→ ⇒ ∴ ∵ ↑ ↓ ∧ ∨ ¬ ≈ ≠) that pdflatex cannot render
# without explicit \DeclareUnicodeCharacter declarations per glyph.
#
# mainfont=Cambria and monofont=Consolas are picked because Latin Modern
# (the pandoc/xelatex default) lacks the Unicode arrow and logical-operator
# glyphs the paper uses. Both fonts ship with Windows. Without these flags
# those glyphs render as missing-glyph boxes.

echo "[1/3] pandoc: paper_telegraph_english.md -> paper_telegraph_english.tex"
pandoc paper_telegraph_english.md \
  --from=markdown+tex_math_dollars+implicit_figures+pipe_tables+yaml_metadata_block \
  --to=latex \
  --standalone \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V graphics=true \
  -V mainfont="Cambria" \
  -V monofont="Consolas" \
  --output=paper_telegraph_english.tex

echo "[2/3] xelatex pass 1"
xelatex -interaction=nonstopmode -halt-on-error paper_telegraph_english.tex > /dev/null

echo "[3/3] xelatex pass 2 (for cross-refs and longtable settling)"
xelatex -interaction=nonstopmode -halt-on-error paper_telegraph_english.tex > /dev/null

echo "Build complete: paper_telegraph_english.pdf"
ls -la paper_telegraph_english.pdf
