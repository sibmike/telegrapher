# Frontier and Localhost: ACL Rolling Review version

Standalone long-paper version for ACL Rolling Review, with NAACL 2027 as the primary target (COLING 2027 as the alternative). Built with the official ACL style (`acl.sty` in `[review]` mode, anonymized, line-numbered), copied from `C:\Users\mikea\SCRIPTS\templates\acl-style-files`.

## Status (2026-10-10)

`main.pdf`, 33 pages: an eight-page body (the Limitations section starts at the end of page 8), references, and Appendices A to I. Abstract 200 words. 0 undefined references or citations. Every one of the IEEE source's 148 citation keys appears in the body or the appendices. `supplementary_data.zip` is the anonymized supplementary material: the two released score tables and the recount script, which reproduces 256 systems, 204 core, 52 contrast, and 269 rows.

## How it was made

The `paper-compression` skill at n_pages = 8 (`BRIEF.md` holds the spine, the outline with its page budget, and the detail ledger). The body was rebuilt from a nine-sentence story spine, not shortened from the IEEE text. Its central contribution is the analytic distinction (persistence, demonstrated local improvement, and justified transfer are three different things; the feedback a deployment receives fixes what an acceptance gate can know). Governed cross-organization promotion is a consequence of the findings, in one discussion paragraph, with its audit in Appendix F. That emphasis follows the venue assessment the authors obtained. The body was cut from 9.1 to 8 pages with every removed sentence either moved to an appendix or recorded as a restatement (`LOSS_AUDIT.md`). A fact screen against the released table, the IEEE sections, and the dated correction notes found the numbers and cell placements clean, and corrected framing stated as fact ("the literature calls almost any system self-improving" became "often described as"), dropped hedges, CASCADE presented as production, the error-structure argument called an "answer" rather than a hypothesis, and one real mistake shared with the IEEE text: only the 126 most recently added systems carry an evidence tier in the released table (corrected in both packages).

## Build

```
bash build.sh
```

The build mirrors `references.bib` and three figures from the IEEE package. Figure 1 is ACL-specific, because its promotion box points to Section 6. Regenerate it with `make_figures.py --ieee --out <dir> --promo-pointer "(Section 6)"`. The build reports the page on which the Limitations heading falls; it must be 8 or earlier.

## For the authors before submission

- **Multiple submission.** The same corpus and claims are in the IEEE Access package and on arXiv (v4). Check the current ARR policy on simultaneous submission to a journal before submitting; the arXiv preprint itself is allowed under ACL's current policy, but confirm for the cycle you target.
- **Responsible NLP checklist.** Declare the AI writing assistance in the checklist (and, at camera-ready, in the acknowledgments). Report the single-rater classification and the released data there too.
- **References.** ACL asks for DOIs or ACL Anthology URLs where they exist; most entries are arXiv preprints and vendor documentation, so this is a cleanup pass, not a blocker.
- **Self-citation.** The two prior analyses are cited in the third person, as ACL allows. The term "patch loss" echoes one of their titles, a soft signal only.
- **Camera-ready.** Switch to `\usepackage[final]{acl}`, add the authors and the acknowledgments, and use the ninth page that accepted papers receive.
