r"""Post-process a pandoc LaTeX fragment for the two-column IEEE Access class.

pandoc renders pipe tables as `longtable`, which cannot be used inside a two-column
page. This converts each longtable into a `table*` float holding a `tabular`, drops
the longtable header/footer machinery, and keeps the column specification pandoc
chose (its \linewidth-relative p{} widths resolve to the full text width inside
table*). A table immediately followed by a "Table X-N." paragraph has that
paragraph turned into the float's \caption.

Usage: fix_tables.py body.tex
"""
import re, sys

p = sys.argv[1]
t = open(p, encoding="utf-8").read()

def convert(m):
    inner = m.group(1)
    # column spec is everything up to the first \toprule
    head, _, rest = inner.partition("\\toprule")
    colspec = head.strip()
    if colspec.startswith("[]"):
        colspec = colspec[2:].strip()
    # drop longtable-only directives
    rest = re.sub(r"\\endfirsthead|\\endhead|\\endlastfoot|\\endfoot", "", rest)
    rest = re.sub(r"\\caption\{.*?\}\\tabularnewline\n?", "", rest, flags=re.S)
    body = "\\toprule" + rest
    # IEEE convention: the table caption sits above the table (ieeeaccess sample and IEEEtran).
    return "\\begin{table*}[!t]\n%%CAPTION%%\n\\centering\\small\n\\begin{tabular}" + colspec + "\n" + body.strip() + "\n\\end{tabular}\n\\end{table*}"

# pandoc 3.x wraps each uncaptioned table in "{\def\LTcaptype{none} ... \end{longtable}\n}"; consume the wrapper too
t = re.sub(r"\{\\def\\LTcaptype\{none\}[^\n]*\n\\begin\{longtable\}(.*?)\\end\{longtable\}\n\}", convert, t, flags=re.S)
t = re.sub(r"\\begin\{longtable\}(.*?)\\end\{longtable\}", convert, t, flags=re.S)

# Attach the following "Table X-N. ..." paragraph as the caption + \label{tab:X-N}, if present.
def attach(m):
    table, label_par = m.group(1), m.group(2)
    tag = re.match(r"^Table\s+([IVXA-Z]+-\d+)\.\s*", label_par.strip())
    cap = label_par.strip()[tag.end():]
    return table.replace("%%CAPTION%%", "\\caption{" + cap + "}\\label{tab:" + tag.group(1) + "}")
t = re.sub(r"(\\begin\{table\*\}\[!t\]\n%%CAPTION%%(?:(?!\\end\{table\*\}).)*\\end\{table\*\})\n\n(Table\s+[IVXA-Z]+-\d+\.[^\n]*)\n", attach, t, flags=re.S)
t = t.replace("%%CAPTION%%\n", "")

# REF(x) tokens written in the Markdown become \ref{x}; a preceding word gets a non-breaking space.
t = re.sub(r"(Section|Sections|Sec\.|Fig\.|Figs\.|Table|Tables|Appendix)\s+REF\(([^)]+)\)", r"\1~\\ref{\2}", t)
t = re.sub(r"REF\(([^)]+)\)", r"\\ref{\1}", t)

# pandoc's relative widths assume \linewidth; inside table* use \textwidth explicitly
t = t.replace("\\linewidth - ", "\\textwidth - ")
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("fix_tables: converted", t.count("\\begin{table*}"), "tables")
