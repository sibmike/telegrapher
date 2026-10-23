# Ledger part K: final-wording audit (2026-10-03)

The cards in parts A–J record each source against the sentence the authors *intended* to write. This part records the independent check of the sentences as they were finally written. Three auditors, none of whom wrote the text, each covered one range:

| Report | Range |
|---|---|
| `audits/citation_audit_part1_sections_I-V.md` | Abstract and Sections I–V |
| `audits/citation_audit_part2_sections_VI-X_appA.md` | Sections VI–X, Appendix A and the Acknowledgment |
| `audits/citation_audit_part3_appB.md` | Appendix B and the Section II-D pointer |

For each range, the auditor did three things:
- compared every citing sentence with its card;
- read the source itself, from locally extracted full text, wherever the sentence and the card differed or the card was thin;
- checked every bib entry online (Crossref, the arXiv API, venue BibTeX).

No bot check, CAPTCHA, or paywall was bypassed.

This file has no `### key` headings, so `tools/build_ledger_index.py` does not index it as a card.

## Results

| | Part 1 | Part 2 | Part 3 |
|---|---|---|---|
| Citation uses checked | 72 | 106 | 61 |
| Bib entries checked online | 47 | 55 | 64 |
| Hallucinated references | 0 | 0 | 0 |
| HIGH / MEDIUM / LOW findings | 3 / 5 / 22 | 1 / 7 / 24 | 1 / 9 / 22 |

The mathematics was checked in Part 2 and is correct:
- the chain rule;
- the step h_j ≤ P(F_j);
- Esary–Proschan–Walkup Th. 4.1, with the pinpoint confirmed on p. 1470;
- the binomial tail with Hoeffding's bound;
- all twelve values in Table VI;
- the running example.

## Resolution

Every HIGH and MEDIUM finding was applied to `main.tex`, using the auditor's wording or a tighter version. The text LOW findings were applied too; the exception is two bib-style items that became moot. The most consequential changes:

1. **Sentence-level overlap of importance and hardness.** Thought Anchors compares receiver-head attention with counterfactual influence, so the "no study" claims in V-C, IX and Appendix B are narrowed to the token level (`bogdan2025anchors`, Abstract; Sec. 1; Sec. 4.2; the confound by position in Sec. 8).
2. **Yeom et al.'s second use.** The 20% figure concerns the answer-emission step, over 500 one-sentence answers, correct and wrong alike.
3. **Chain of thought.** The length point is now marked as the review's reading, uncited.
4. **Arora et al.** The weak correlation with perplexity belongs to the accumulated divergence; the per-token divergence tracks perplexity closely.
5. **Voting.** The condition is now that the correct answer is the most likely single answer; this means e_key < ½ only at a two-way decision (VI-D, VIII, App. B). This removes a contradiction with App. A-D.
6. **Method statements** in II-C and the Acknowledgment now name the exceptions:
   - two sources were not opened (`hoeffding1963probability`, and `lam1997application`, abstract only);
   - for a few sources a preprint, technical report, or author manuscript was read instead of the published version.
7. **Appendix B corrections:**
   - `foster2024behavior`: the bounded-reward condition is restored.
   - `ross2010efficient`: the reading now covers both tight examples. The quadratic cost comes from lock-in, not from uniform risk.
   - `yao2025taubench`: scoped to retail and gpt-4o, with the "just under 25%" wording.
   - `kalai2024calibrated`: the reading is limited to the average e_key over arbitrary facts, for models that stay calibrated.
   - `dietrich2023jury`: the Tendency-to-Competence premise is restored, and the limit is stated.
   - `wiegreffe2019attention`, `duan2024shifting`, `kadavath2022language` and `chen2024more`: the dropped comparators and hedges are restored.
8. **Bib corrections:**
   - **NeurIPS 2025 pages.** Seven entries with DOI prefix 10.52202/085713 now use the page range of the DOI's own Crossref record. A scripted check found that the neurips.cc and Crossref ranges differ for that year only.
   - **ferrando2025know**: corrected to "Oscar Obeso", with proceedings pages added.
   - **mirzadeh2025gsmsymbolic**: corrected to "Keivan Alizadeh", as in the PDF byline.
   - **kleinberg2021algorithmic**: the article number is given as a note.
   - **ICLR booktitles**: harmonized to the ordinal form.
   - **arXiv-only entries**: set as `@misc` with the arXiv DOI.

## Additional uses verified by the auditors (not recorded as Uses in parts A–J)

| Key | Sentence (where) | Source location confirmed |
|---|---|---|
| `bogdan2025anchors` | Sentence-level receiver-head comparison (V-C; IX) | Abstract; Sec. 1; Sec. 4.2 (paired t-tests, ts > 4.0); Sec. 8 (confound by position) |
| `cai2025rkv` | Reasoning models write thousands of tokens (I) | Sec. 4.2: average generation of 2,833–15,536 tokens |
| `cai2025rkv` | Attention-only selection falls short (IV-B) | Sec. 5.1: attention-only and redundancy-only scoring perform worst |
| `kwa2025measuring` | Tasks graded by human-expert time (I) | Humans "with relevant domain expertise" were timed |
| `li2025scbench` (2 uses) | The important set moves; follow-up queries (IV-B) | Sec. 1, findings 1 and 4 |
| `lin2024rho1` | About a quarter of tokens drop in loss; about half already learned (V-A) | Sec. 2.1: 26% and 51% |
| `abdin2024phi4` (2nd use) | One worked example: pivotal tokens are not low-probability tokens (V-B) | Fig. 3 caption; Sec. 4.3 |
| `chen2026pitfalls` | Eviction policies on instructions (IV-B) | Sec. 6 |
| `zou2026latentmas` | Latent collaboration is harder to inspect; a debug mode (VIII) | Sec. 5, "Intermediate Error Tracking" |
| `lecun2023why` (Use 2) | LeCun's conclusion that training cannot remove the problem (I) | Post text (LD-JSON), last two sentences; card in J8 |
| `bachmann2024pitfalls` (Use 2) | The compounding critique conflates two phases (App. B) | PMLR abstract; card in J1 |
| `wang2023self` | PaLM-540B GSM8K from 56.5% to 74.4% (VIII) | Table 2, p. 5 |
| `yao2023tree` | Best of 100 is 49%; most-frequent voting suits small answer spaces (VII-C) | Sec. 2; Sec. 4.1, Table 2 |
| `fu2026c2c` (2nd use) | Self-paired fuser gives 70–90% of the gain over a fine-tuned receiver (VI-C; Table IV) | Sec. 4.4, Table 6, p. 9 |
| `hanna2026planning` | Planning in the 14B model, nascent at 4B–8B (VI-B) | Abstract; Sec. 4.2; Sec. 4.3, p. 6 |
| `li2025unraveling` | Final-layer embeddings; preset number of strata (VI-B) | Sec. 4, p. 4; Sec. 5, p. 7 |
| `tang2024quest` | Quest retains the whole cache and reads a query-dependent subset (VIII) | Sec. 2 |
| `costello2025think` | Coverage stays roughly flat (VIII) | arXiv v1, pp. 1 and 7 |

## External pre-submission review (2026-10-12)

An outside reviewer read the full PDF, reproduced the numerical examples and Table VI, and spot-checked key references. Their points, and how each was resolved:

| Point | Resolution in `main.tex` |
|---|---|
| The target should be the uniform, independent per-token argument, not exponential decay as such | Intro ¶3 and Conclusion ¶1 now say that rejecting the argument's assumptions does not rule out exponential decay; it means the argument cannot establish it as a general law. |
| Slow decay also needs bounded non-key risk | Condition added to the abstract, VII-B ("as long as the residual risk at non-key positions stays summable") and the Conclusion. Table I "length is free" became "added length costs only non-key risk". Table V gains two rows: sublinear decision count (not yet measured) and summable non-key rates (assumption). |
| Importance evidence does not estimate k or the failure hazard | IV-C, V-C, VII-A ("bound loosely" removed) and IX now say this. IX calls the long–short count a proxy, pairs it with an error-based count and a residual-risk measurement, and no longer says a fitted exponent "decides between the regimes". |
| Jury-theorem premise misstated | App. A-D and B-D now state the symmetric tendency-to-competence condition (SEP Sec. 2.5, quoted in audit Part 2), the mixture limit, and the reviewer's counterexample: individual accuracy 0.69, three-vote majority 0.68205, recomputed. |
| Agreement among wrong answers is not dependence | Sentence added in App. A-D. VI-D now distinguishes bias shared by every sample from accuracy that varies across tasks. |
| "Voting helps only if" overstated | VI-D and VIII now carry "with many independent samples" or "with many samples"; B-D now says "voting over independent samples". |
| Odd m in Eq. (5) | "Sample an odd number m of answers, so that a two-way vote cannot tie." |
| Error-free traces vs final answers; chain-of-thought example | Scope sentence added in III-A. The intro's chain-of-thought example is no longer called a counterexample; it now says the study is no controlled test of length. |
| Dziri et al. stated too narrowly | Intro now covers both propositions. Verified from the NeurIPS PDF, Sec. 4, p. 8: Prop. 4.1 (independent steps, collision floor) and Prop. 4.2 (iterated application, recovery probability at most c); in both, success falls exponentially toward a small floor. |
| Lin et al. details | Text and Table III now give 100 incorrect traces each from the GSM8K and MATH training sets, with a critical token found in all but one (200 traces; card B). V-C adds that most critical tokens did not coincide with conventional error tokens: 65% mismatch on GSM8K and 87% on MATH500, card B, p. 3. |
| Table V geometry row, grading basis, search scope | Strength column changed to "Hypothesis; indirect support". The grading basis is stated in II-C, and II-B says the search was narrative rather than systematic. |
| Commercial-bridge footnote (optional deletion) | Kept. The authors asked for the industry example, and the footnote already states that no results are relied on. |
| VOLUME 11, 2023 footer | Generated by `ieeeaccess.cls` (`\thevol`, `\theyear`). The publisher replaces it, so it is left as the template supplies it. |

No citation key was added or removed.

## Known residual items

- **`hoeffding1963probability`**: not opened (paywalled). It is cited for the standard inequality, which is stated and applied correctly.
- **`lam1997application`**: abstract only. The citing sentence claims no more than the abstract does.
- **`eckhardt1985theoretical`**: read in its NASA TM 86369 precursor; IEEE Xplore was bot-protected.
- **`knight1986experimental`**: read in the authors' manuscript.
- **`hsieh2024ruler`**: eight authors, following arXiv v3 (the COLM camera-ready). The COLM accepted-papers page lists seven, which matches the pre-camera-ready list.
