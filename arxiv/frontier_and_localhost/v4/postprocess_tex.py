r"""Post-process the pandoc LaTeX of the arXiv manuscript (one-column article class).

1. natbib citations: \citep{a; b} -> \cite{a,b}, \citet -> \cite, prefixed groups unwrapped (same rules as
   the IEEE build, so the text's "Author et al. [n]" convention renders identically).
2. A pipe table followed by a "Table X-N. caption" paragraph becomes a `table` float with the caption
   above and \label{tab:X-N}; every other table stays a longtable (the score table spans pages).
3. REF(x) tokens written in the Markdown become \ref{x}.

Usage: postprocess_tex.py paper.tex
"""
import re, sys

p = sys.argv[1]
t = open(p, encoding="utf-8").read()

# ---- 1. citations
def fix(m):
    keys = [k.strip() for k in m.group(2).split(";")]
    return "\\cite{" + ",".join(keys) + "}"
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
t = re.sub(r"\\citealp\[([^\]]*)\]\[([^\]]*)\]\{([^}]*)\}",
           lambda m: (m.group(1).strip().rstrip(",") + "~" if m.group(1).strip() else "") + "\\cite{" + m.group(3).strip() + "}", t)
t = re.sub(r"\\cite([pt])(?:\[[^\]]*\])*\{([^}]*)\}", fix, t)
t = re.sub(r"\\cite(?:author|year|alp|alt)\*?\{([^}]*)\}", lambda m: "\\cite{" + m.group(1) + "}", t)

# ---- 2. captioned tables -> floats
def convert(m):
    inner, tag_par = m.group(1), m.group(2)
    head, _, rest = inner.partition("\\toprule")
    colspec = head.strip()
    if colspec.startswith("[]"):
        colspec = colspec[2:].strip()
    rest = re.sub(r"\\bottomrule\\noalign\{\}\s*\\endlastfoot", "", rest)      # pandoc's last-foot rule sits before the rows
    rest = re.sub(r"\\endfirsthead|\\endhead|\\endlastfoot|\\endfoot", "", rest)
    body = "\\toprule" + rest.rstrip() + "\n\\bottomrule\\noalign{}"
    tag = re.match(r"^Table\s+([IVXA-Z]+-\d+)\.\s*", tag_par.strip())
    cap = tag_par.strip()[tag.end():]
    size = "\\footnotesize" if colspec.count("\\real{") >= 6 else "\\small"     # six or more columns on a 6.5 in line
    return ("\\begin{table}[htbp]\n\\caption{" + cap + "}\\label{tab:" + tag.group(1) + "}\n\\centering" + size + "\n"
            "\\begin{tabular}" + colspec + "\n" + body.strip() + "\n\\end{tabular}\n\\end{table}\n")
pat = (r"\{\\def\\LTcaptype\{none\}[^\n]*\n\\begin\{longtable\}((?:(?!\\end\{longtable\}).)*)\\end\{longtable\}\n\}\n\n"
       r"(Table\s+[IVXA-Z]+-\d+\.[^\n]*)\n")
t, n_tables = re.subn(pat, convert, t, flags=re.S)

# ---- 3. cross-reference tokens
t = re.sub(r"(Section|Sections|Sec\.|Fig\.|Figs\.|Table|Tables|Appendix|Appendices)\s+REF\(([^)]+)\)", r"\1~\\ref{\2}", t)
t = re.sub(r"REF\(([^)]+)\)", r"\\ref{\1}", t)

open(p, "w", encoding="utf-8", newline="\n").write(t)
print("postprocess: %d captioned tables -> floats; %d longtables kept; %d REF tokens left" %
      (n_tables, t.count("\\begin{longtable}"), t.count("REF(")))
