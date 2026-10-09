"""Verification for the IEEE Access package: numbers in the text match the recount; build artifacts are clean."""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(HERE, "..")
SUB = os.path.join(PKG, "submission")
ok = True
def check(c, msg):
    global ok; print(("PASS " if c else "FAIL ") + msg); ok = ok and c

# recount
out = subprocess.run([sys.executable, os.path.join(HERE, "recount.py")], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
m = re.search(r"unique systems: (\d+)\s+core: (\d+)\s+contrast: (\d+)", out)
total, core, contrast = map(int, m.groups())
body = open(os.path.join(SUB, "paper_frontier_and_localhost_ieee.md"), encoding="utf-8").read()
abstract = open(os.path.join(SUB, "abstract.md"), encoding="utf-8").read()
check(f"{total} production and research systems" in abstract and f"Of the {total} systems" in body, f"corpus total {total} stated in body and abstract")
check(f"{core} form the core corpus and {contrast} the contrast corpus" in body, f"core/contrast {core}/{contrast} stated")
check(len(abstract.split()) <= 250, f"abstract {len(abstract.split())} words <= 250")
check("{{" not in re.sub(r"^---.*?\n---\n", "", body, flags=re.S), "no {{placeholders}} in the assembled body")
check("KEY_" not in body, "no KEY_ placeholder citation keys")
# per-substrate numbers in Table VI-1 match recount (all rows)
tbl = re.search(r"\[all rows\].*?(?=\n\[core only\])", out, re.S).group(0)
for sub, n, mean in re.findall(r"^(\S+)\s+(\d+)\s+([\d.]+)", tbl, re.M):
    name = {"INTEGRATED": "Integrated", "S1_Instructions": "S1 Instructions", "S2_Skills": "S2 Skills", "S3_Memory": "S3 Memory",
            "S4_Tools": "S4 Tools", "S5_Orchestration": "S5 Orchestration", "S6_Governance": "S6 Governance"}[sub]
    check(f"| {name} | {n} | {mean} |" in body, f"Table VI-1 row {name}: n={n} mean={mean}")
# build logs
log = open(os.path.join(SUB, "main.log"), encoding="utf-8", errors="replace").read()
check("Citation `" not in log.split("bibtex")[-1] and "undefined on input" not in log, "no undefined citations/references in main.log")
check("Float too large" not in log, "no float too large for page")
pages = re.findall(r"Output written on main.pdf \((\d+) pages", log)
check(pages and 16 <= int(pages[-1]) <= 24, f"main.pdf pages = {pages[-1] if pages else '?'} (target 16-24)")
tex = open(os.path.join(SUB, "body.tex"), encoding="utf-8").read()
check(tex.count("\\includegraphics") == 4, f"4 figures embedded ({tex.count(chr(92)+'includegraphics')})")
check(tex.count("\\begin{table*}") == 10, f"10 tables ({tex.count(chr(92)+'begin{table*}')})")
check(os.path.exists(os.path.join(SUB, "supplementary.pdf")), "supplementary.pdf built")
bbl = open(os.path.join(SUB, "main.bbl"), encoding="utf-8", errors="replace").read()
print("   references in main.bbl:", bbl.count("\\bibitem"))
print("\nOVERALL:", "PASS" if ok else "FAIL")
