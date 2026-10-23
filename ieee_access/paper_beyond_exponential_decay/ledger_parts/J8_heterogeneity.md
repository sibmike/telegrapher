# Ledger part J8 — Heterogeneity, voting at scale, information density, and the opening argument

Checked 2026-10-03. This part covers seven new works and one new use of an already-cited post. I read the full text of six of the seven works and of the LeCun post. Lam and Suen (1997) could not be opened, so its card rests on the publisher's abstract and is narrowed to match. Sources of record and full texts:
- Schaeffer et al.: the PMLR v267 page, its BibTeX and the PMLR PDF, compared with arXiv v1 at the cited passages. The ICML 2025 oral is confirmed on icml.cc.
- Proschan: the scanned 1963 article (with an OCR text layer) in the Technometrics back-issue archive hosted by Carnegie Mellon University's Department of Statistics. Metadata are from Crossref.
- Li et al.: the TMLR listing and BibTeX on jmlr.org, the OpenReview search API, and the arXiv v2 PDF and HTML, whose header marks it as the TMLR version.
- Kleinberg and Raghavan: the PubMed Central full-text HTML of the PNAS article.
- Levy and Jaeger: the NeurIPS proceedings page, its BibTeX, metadata file and PDF, plus the MIT Press DOI record in Crossref.
- Meister et al.: the ACL Anthology page, its .bib and the PDF.
- LeCun: the LinkedIn post's embedded LD-JSON (`SocialMediaPosting.articleBody`).
- Lam and Suen: Crossref; the Internet Archive capture (12 Apr 2024) of the IEEE Xplore abstract page; and two open secondary sources that describe the paper. These are Louisa Lam's own later expository paper (hosted on a University of Palermo site) and Kuncheva, Whitaker, Shipp and Duin (2003, authors' copy).

Blocked and not bypassed:
- Taylor & Francis (Proschan) and pnas.org (Kleinberg and Raghavan) showed a Cloudflare challenge.
- The PMC PDF route showed a proof-of-work check, so the PMC HTML full text was used instead.
- The OpenReview PDF (Li et al.) showed a challenge page, so the arXiv v2 camera-ready was used instead.
- IEEE Xplore (Lam and Suen) returned an empty bot-protection response. dblp showed a bot check. CiteSeerX now redirects to the Internet Archive, and no record was found there. A copy of Lam and Suen on a third-party personal website exists; I did not use it.
- DTIC was down for maintenance. It was not needed.

Retraction checks: a Crossref `query.bibliographic` search (rows=3) for every title, repeated with `filter=update-type:retraction`; `filter=updates:<DOI>` for each DOI; and the arXiv abs pages for withdrawal notices. Nothing was found for any work.

Quote policy: one verbatim quote per source, under 15 words. Everything else is paraphrased with a location. Page numbers are the printed journal or proceedings pages where the PDF prints them (Technometrics, NIPS 19, EMNLP 2021) and physical PDF pages otherwise (PMLR PDF, arXiv v2 PDF). The PNAS article is located by section heading. "Our arithmetic" marks numbers that are not printed in the source. `J8_heterogeneity.bib` (7 entries) passed a test run of bibtex with the paper's IEEEtran.bst: 7 bibitems, 0 warnings. lecun2023why gets no new entry.

---

### schaeffer2025monkeys
- Source of record: https://proceedings.mlr.press/v267/schaeffer25a.html (ICML 2025: Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, pp. 53132–53176; listed as an oral at https://icml.cc/virtual/2025/oral/47224). The arXiv id is 2502.17578, with only v1 (24 Feb 2025). Access: full text (PMLR PDF https://raw.githubusercontent.com/mlresearch/v267/main/assets/schaeffer25a/schaeffer25a.pdf, 45 pp.: main text and Apps. A, B and E.1; arXiv v1 PDF https://arxiv.org/pdf/2502.17578v1 compared at the cited passages, which match: theorems, Fig. 3 caption, App. A).
- Retraction: none found. arXiv shows one version and no withdrawal. PMLR registers no DOI, and the Crossref title query returned only unrelated works.
- Card:
  - Setting: a re-analysis of existing repeated-sampling data, with theory and synthetic backtests. The LLM data are re-used from two earlier papers.
    - Pythia models (70M to 12B) on 128 MATH problems, with 10,000 independent attempts per problem. These are the data of Brown et al. 2024 (Sec. 2, p. 3; App. A, p. 24).
    - Best-of-N jailbreaking of seven models on 159 HarmBench prompts: Claude 3.5 Sonnet and Opus, Gemini 1.5 Flash and Pro, GPT-4o and GPT-4o Mini, and Llama 3 8B Instruct. These are the data of Hughes et al. 2024 (p. 3).
    - A problem counts as solved if any of k attempts succeeds (pass@k, or attack success rate ASR@k). Rates are estimated with the unbiased estimator of Chen et al. 2021 (Eq. 1, p. 1; App. B).
  - What it establishes:
    - With independent attempts, a problem's failure probability is (1 − pass_i@1)^k, so −log pass_i@k falls exponentially in k (Eqs. 5–9, p. 2). The data confirm this problem by problem in both settings, including for Llama 3 8B Instruct (Fig. 3, p. 4).
    - The aggregate law −log pass_D@k ≈ a·k^(−b) comes from how single-attempt success rates are distributed over problems. Theorem 3.1 (sufficiency) and Theorem 3.2 (necessity, under mild regularity assumptions) show that the aggregate follows a power law with exponent b exactly when that density behaves like p^(b−1) near p = 0 (Sec. 3, pp. 3–4; proofs in Apps. E.8–E.9). The empirical distributions have power-law-like left tails (Fig. 4, p. 5).
    - Llama 3 8B Instruct was jailbroken on every prompt within the sampling budget. It therefore has no heavy left tail, and its aggregate falls faster than any power law (Sec. 4, p. 6). In synthetic backtests, a distributional estimator of b has about an order of magnitude lower relative error than least-squares fitting (Sec. 5, Fig. 7, pp. 6–8).
  - Headline numbers (with location): for simple single-attempt distributions, Uniform(0,1) gives k^(−1), Beta(α, β) gives k^(−α), and Kumaraswamy(α, β) gives k^(−α) (Sec. 3, p. 3). The distributional estimator needs 2–4 orders of magnitude less inference compute for the same accuracy (Abstract, p. 1; Sec. 5, p. 8).
  - Authors' own stated limitations or scope:
    - "Independent attempts" is not fully correct for the jailbreaking data, where attempts were drawn until the first success or a cap of 10,000, in minibatches of 60. The authors say that no theorem and no main-text figure changes (App. A, p. 24).
    - They conjecture that the heavy tails come from benchmark design (problems chosen to spread in difficulty) and from selection bias toward striking power laws (Sec. 7, p. 8).
    - The theorems are asymptotic in k.
  - Relation to the review: a precedent for heterogeneity changing the shape of decay. Each item decays exponentially, but a spread of per-item rates with mass near zero turns the aggregate into a power law. App. E.1 (p. 28) cites the known result that power laws can arise from weighted sums of exponentials, which is the same mixture mechanism as Proschan's pooled decreasing failure rate. It bears on the review's reading of agent "half-life" results averaged over tasks, and it complements brown2024monkeys (ledger part J3), whose data it re-analyzes.
  - The hinge: the decaying quantity is failure across k independent whole-answer attempts, judged by an oracle that accepts any success, and the heterogeneity is across problems in a benchmark. The review's question concerns answer length and positions within a single answer, and voting without an oracle.
- Use 1 — intended claim: "With repeated sampling, each problem's failure rate falls exponentially in the number of attempts, yet the aggregate across problems follows a power law, because single-attempt success rates have a heavy tail near zero."
  - Source passage: "per-problem exponential scaling can be made consistent with aggregate polynomial scaling" (Abstract, p. 1). Theorems 3.1–3.2 (pp. 3–4) give the if-and-only-if link to a power-law left tail. Per-problem exponential decay is shown in Fig. 3 (p. 4), the tails in Fig. 4 (p. 5), and the counterexample without a tail in Sec. 4 (p. 6).
  - Scope:
    - The aggregate in the paper is the negative log of the success rate averaged over problems, −log pass_D@k ≈ a·k^(−b). For large k this approximates the average failure rate 1 − pass_D@k (our arithmetic).
    - The power law holds asymptotically in k and only where the tail exists. It is absent for Llama 3 8B Instruct under jailbreaking.
    - "Because" is supported as a mathematical equivalence (with regularity conditions) plus an empirical fit. The paper does not claim that every repeated-sampling setting yields a power law.
  - Verdict: NARROW → safe wording: "Schaeffer et al. show that with independent repeated attempts, each problem's failure probability falls exponentially in the number of attempts k, while the negative log of the success rate averaged over problems can fall only as a power law in k. This happens when, and under mild regularity conditions only when, single-attempt success rates across problems have a power-law tail near zero, as they do for Pythia models on MATH and for the jailbroken frontier models other than Llama 3 8B Instruct [schaeffer2025monkeys]."
- Bib notes: authors, title, booktitle, volume 267, pages 53132–53176, month (13–19 Jul) and publisher are from the PMLR page's BibTeX. The arXiv id is from the abs page. PMLR protects the L in "(Laws)". I left it unprotected, so IEEEtran prints sentence case "(laws)". There is no DOI. The oral status is from the icml.cc virtual page and is not needed in the bib.

### proschan1963theoretical
- Source of record: Technometrics 5(3):375–383, August 1963, DOI 10.1080/00401706.1963.10490105 (Crossref record). Taylor & Francis showed a Cloudflare challenge, which I did not bypass. Access: full text (scanned article with an OCR text layer, Technometrics back-issue archive hosted by Carnegie Mellon University's Department of Statistics, https://www.stat.cmu.edu/technometrics/59-69/VOL-05-03/v0503375.pdf, 9 pp.). The OCR garbles some formulas and table cells, so the numbers below were read in their sentence context. The paper was reprinted in Technometrics 42(1):7–11, Feb 2000 (DOI 10.1080/00401706.2000.10485974; not opened).
- Retraction: none found. Neither the 1963 record nor the 2000 reprint record in Crossref carries an update or retraction relation, and `filter=updates:` returns 0 notices.
- Card:
  - Setting: field data on the intervals between successive failures of the air-conditioning system in a fleet of 13 Boeing 720 jets (Table 1, p. 376). Counting the intervals after a major overhaul as separate series gives 17 series. Pooled, there are 213 intervals with mean 93.14 hours (Sec. 2, p. 377). The theory is that mixtures of decreasing-failure-rate (DFR) distributions are DFR (Theorem 2, which the paper cites from Barlow, Marshall and Proschan 1963).
  - What it establishes:
    - Theorem 2 (p. 382): a mixture of distributions that each have a decreasing failure rate itself has a decreasing failure rate. The exponential has a constant, hence non-increasing, failure rate, so a mixture of exponentials is DFR. When the rates differ, the mixture is not exponential, so its failure rate is non-constant and decreasing (p. 382).
    - Plane by plane, successive intervals show no significant trend (Mann's test combined by Fisher's method; Sec. 3, pp. 378–380). Nor is there conclusive evidence against a constant failure rate (the Proschan–Pyke test; Sec. 4, p. 381). The author therefore accepts an exponential distribution for each plane, with plane-specific rates.
    - Pooled across planes, a test against the DFR alternative rejects a constant failure rate (Sec. 5, p. 383). A Kolmogorov–Smirnov test had not rejected an exponential fit to the same pooled data, although the empirical survival curve crossed the exponential once from below (Sec. 2, p. 377).
  - Headline numbers (with location): 213 pooled intervals, mean 93.14 h, Kolmogorov–Smirnov band ±0.0931 (p. 377). The combined trend statistic is 27.239, about 0.42 two-tailed (p. 380). The pooled DFR test gives a standardized value of −2.46, with probability 0.007 (p. 383).
  - Authors' own stated limitations or scope:
    - Pooling corresponds only approximately to a convex combination, because the number of intervals each plane contributes is random. It is about 2000·λ_i before overhaul, by the renewal theorem (pp. 382–383).
    - Section 6 (p. 383) proposes the same explanation for semiconductors (lot-to-lot variation) and for components pooled across types of equipment, as plausible cases. They are not tested.
  - Relation to the review: the classical precedent for the mixture argument. Units that each have a constant hazard, pooled, show a decreasing hazard. This supports the claim that heterogeneity in per-unit rates makes aggregate survival decay more slowly than a single exponential, and it is the reliability counterpart of schaeffer2025monkeys. It also carries a caution: a pooled decreasing hazard says nothing about any single unit, whose hazard here is constant. Note also that the generic goodness-of-fit test missed the mixture (p. 377).
  - The hinge: the heterogeneity is across independent units (planes), each with a constant hazard in continuous operating time, and the DFR is a property of the pooled population. In the review's two-rate model, positions within one answer combine as a product (a series system). A mixture arises only when answers or tasks with different rates are pooled.
- Use 1 — intended claim: "Pooling components whose lifetimes are each exponential, with different rates, yields a decreasing failure rate for the pool."
  - Source passage: "convex combinations of exponentials have decreasing failure rate" (Sec. 5, p. 382). The pooled air-conditioning intervals are treated as such a mixture and test as DFR (p. 383).
  - Scope: "decreasing" means non-increasing throughout (p. 375). A strictly decreasing rate needs the rates to differ. Pooling observed intervals is approximately a mixture, weighted by how many intervals each unit contributes (p. 382). The theorem itself is cited from Barlow, Marshall and Proschan (1963). Proschan's paper applies it and tests it on data.
  - Verdict: ACCURATE. If the sentence names Proschan as its source, a precise version is: "Proschan showed that pooling failure data from units whose lifetimes are each exponential, with different rates, yields a decreasing failure rate for the pool: air-conditioning failures in a fleet of Boeing 720 jets were consistent with an exponential distribution plane by plane, while the pooled intervals had a decreasing failure rate [proschan1963theoretical]."
- Bib notes: author, title, journal, volume 5, number 3, pages 375–383, August 1963 and the DOI are from the Crossref record and match the printed running heads ("TECHNOMETRICS, VOL. 5, NO. 3; AUGUST 1963", pp. 375–383). The author is Frank Proschan, Boeing Scientific Research Laboratories, per the title page. The entry cites the original rather than the 2000 reprint.

### li2024more
- Source of record: Transactions on Machine Learning Research, October 2024. OpenReview forum https://openreview.net/forum?id=bgzUSZ8aeg; the OpenReview search API gives venue "Accepted by TMLR", venueid TMLR, publication date 2024-10-23. The TMLR list at https://jmlr.org/tmlr/papers/ shows "October 2024", and the BibTeX is at https://jmlr.org/tmlr/papers/bib/bgzUSZ8aeg.bib. arXiv:2402.05120: v1 of 3 Feb 2024; v2 of 11 Oct 2024, with the comment "Published at Transactions on Machine Learning Research (TMLR)". Access: full text of arXiv v2 (PDF https://arxiv.org/pdf/2402.05120v2 and HTML https://arxiv.org/html/2402.05120v2, used to read the tables). Its header reads "Published in Transactions on Machine Learning Research (10/2024)" and links the OpenReview review. The OpenReview PDF sits behind a challenge page and was not opened.
- Retraction: none found. arXiv shows two versions and no withdrawal. TMLR registers no DOIs, and the Crossref title query returned unrelated works.
- Card:
  - Setting: "Agent Forest" samples N outputs from the same LLM, or from the same prompting or multi-agent method, and returns the output with the highest summed similarity to the others (Sec. 3, Alg. 1, p. 4). Similarity is answer frequency for closed-ended tasks, which amounts to a plurality vote, and BLEU for code.
    - Models: Llama2-13B-Chat, Llama2-70B-Chat and GPT-3.5-Turbo. GPT-4 is queried once, as a reference only.
    - Tasks: GSM8K, MATH, MMLU, chess state tracking and HumanEval.
    - Ensembles grow to 40 samples, and results are averaged over 10 runs (Sec. 4, pp. 5–6).
    - The difficulty analysis uses a synthetic arithmetic task with GPT-3.5-Turbo (Sec. 6, pp. 9–11).
  - What it establishes:
    - Accuracy generally rises with ensemble size for all three models on all five tasks (Fig. 3, Table 2, Sec. 5.1, p. 6). A one-way ANOVA across sizes 1, 10, 20, 30 and 40 gives p < 0.05 in every cell (App. B.2, Table 7, pp. 17–18).
    - Adding voting to CoT, zero-shot CoT, SPP, Debate or Reflection usually adds further gains (Table 3, Sec. 5.2, p. 7). The exception is Debate with either Llama2 model on HumanEval, which scores 0 both alone and with voting. The authors attribute this to noise from other agents' answers disrupting the code logic.
    - Relative gains are larger for weaker models and on the harder dataset (Table 6, p. 9). In the synthetic task, gains first rise and then fall as inherent difficulty grows (Property 1), rise with the number of reasoning steps (Property 2.1), and absolute accuracy rises with the prior probability of the correct answer (Property 3) (Secs. 6.2–6.4, pp. 10–11).
  - Headline numbers (with location), single query → ensemble of 40 (Table 2, p. 6):
    - GSM8K: Llama2-13B 0.35 → 0.59, Llama2-70B 0.54 → 0.74, GPT-3.5-Turbo 0.73 → 0.85.
    - MATH: 0.03 → 0.09, 0.05 → 0.11 and 0.29 → 0.39, in the same model order.
    - Absolute gains are 12–24 points on GSM8K, 6–10 on MATH, 1–4 on Chess, 5–11 on MMLU and 4–9 on HumanEval (Sec. 5.1, p. 6).
    - Relative gains (Table 6, p. 9) are 69%, 37% and 16% on GSM8K and 200%, 120% and 34% on MATH, for Llama2-13B, Llama2-70B and GPT-3.5-Turbo respectively.
  - Authors' own stated limitations or scope:
    - Gains taper off at the highest inherent difficulty tested (I = 400). The authors suggest that excessive complexity exceeds the model's reasoning ability, so the method gives diminishing returns under extreme difficulty (Sec. 6.2, p. 10). This is their own statement of when the gains shrink.
    - On Chess the method is not the best standalone method for either Llama2 model (Sec. 5.3, p. 7).
    - Cost grows in proportion to the number of samples (Sec. 5.5, p. 8; Sec. 7, p. 12).
    - Internal inconsistencies to avoid quoting: Sec. 6 (p. 8) gives Llama2-13B relative gains of "28%-200%" and GPT-3.5 gains of "8%-16%", while Table 6 gives 69–200% and 16–34%. Table 3 lists the Llama2-13B ensemble on HumanEval at 0.25, while Table 2 lists 0.18.
  - Relation to the review: RQ3/C4, voting at scale. Plurality voting raised MATH accuracy even where single-query accuracy was far below one half (Llama2-13B, 0.03 → 0.09). This fits the review's remark that a plurality can be right when e_key > 1/2 if wrong answers are spread over many alternatives (our reading; the paper does not report how wrong answers are distributed). The rise-then-fall with inherent difficulty is consistent with voting failing once the correct answer is no longer the most common one. The paper itself gives the capability explanation above.
  - The hinge: a whole-answer plurality vote over samples from the same model, at temperature 1 by default (Fig. 4 caption, p. 7). Neither per-problem correctness rates nor the correlation between samples is reported. The review's analysis is per key decision and turns on that correlation.
- Use 1 — intended claim: "Under simple sampling and voting, performance on several tasks rose with the number of sampled agents, with larger gains on harder tasks."
  - Source passage: "Gains increase then decrease by rising the inherent difficulty" (Property 1, Sec. 6.2, p. 10). In paraphrase: the abstract says the size of the improvement correlates with task difficulty (p. 1), and the introduction says gains are larger for difficult tasks and for weaker models (p. 2). The evidence for "harder" is the relative gain in Table 6 (p. 9).
  - Scope:
    - "Larger gains on harder tasks" holds for relative gains, (P_m − P_s)/P_s. In absolute points, the MATH gains (6–10) are smaller than the GSM8K gains (12–24) (Table 2; Sec. 5.1).
    - In the controlled task, gains rise and then fall with difficulty.
    - Three models, ensembles of at most 40 samples.
  - Verdict: NARROW → safe wording: "Li et al. found that accuracy rose as up to 40 samples from the same LLM were combined by plurality vote, for three models on five benchmarks. Relative gains were largest for weaker models and on the harder benchmark, MATH, though absolute gains there were smaller than on GSM8K; in a controlled arithmetic task, gains first rose and then fell as problems became harder, which the authors attribute to problems exceeding the model's ability [li2024more]."
- Bib notes:
  - Authors and title are from the printed TMLR version (Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, Deheng Ye; all Tencent). The OpenReview/TMLR BibTeX has profile-case names ("junyou li", "QIANG FU"); these were normalised.
  - Journal, ISSN 2835-8856, year 2024 and the OpenReview URL follow the TMLR BibTeX. The month (October) comes from the TMLR list and the PDF header.
  - There is no DOI, and the arXiv id is given in a note.

### kleinberg2021algorithmic
- Source of record: https://doi.org/10.1073/pnas.2018340118 (PNAS 118(22):e2018340118). It was published online 25 May 2021, with issue date 1 June 2021. It was edited by Matthew O. Jackson, received 31 Aug 2020 and approved 3 Feb 2021. Access: full text (PubMed Central HTML of the published article, https://pmc.ncbi.nlm.nih.gov/articles/PMC8179131/). The pnas.org page showed a Cloudflare challenge and the PMC PDF a proof-of-work check, and neither was bypassed. The SI Appendix (proofs of Theorems 2 and 3, the RUM counterexamples) was not read. arXiv:2101.05853 v2 (1 June 2021) notes that a version appears in PNAS.
- Retraction: none found. The Crossref record has no update relation, and `filter=updates:` returns 0 notices.
- Card:
  - Setting: a stylized game-theoretic model with no data (sections "Modeling Ranking" and "Modeling Selection").
    - Two firms each hire one of n candidates, whose values are x_1 > … > x_n.
    - Each firm ranks the candidates either with its own independent "human evaluator" ranking (accuracy θ_H) or with a common algorithmic ranking (accuracy θ_A). The algorithmic ranking is identical for every firm that uses it.
    - The firms move in random order, and each hires its top remaining candidate.
    - Rankings come from a "noisy permutation family" (Definition 1), such as random utility models (RUMs) and the Mallows model.
  - What it establishes:
    - Theorem 1 ("Stating the Main Result") requires two conditions on the ranking model: a "preference for the first position" (Def. 2) and a "preference for weaker competition" (Def. 3). If both hold, then for any θ_H there is a θ_A > θ_H at which using the algorithm is a strictly dominant strategy for both firms, yet social welfare, and each firm's utility, would be higher if both used human evaluators. The theorem is a Braess-paradox-type result.
    - Mechanism ("A Preference for Independence"): Def. 2 is equivalent to the firm that hires second preferring a ranking independent of its competitor's to the competitor's own ranking, at equal accuracy (Eqs. 2–3).
    - The conditions hold for the Mallows model under any candidate distribution (Theorem 3), and for Gaussian or Laplacian RUMs with three candidates (Theorem 2). They can fail with more candidates: Def. 2 fails for Laplacian noise with 15 candidates (Fig. 2). They never hold under Plackett–Luce, where monoculture has no effect (section "RUMs").
  - Headline numbers (with location): in one example (three candidates with values drawn uniformly around zero, Gaussian noise), equilibrium welfare with both firms using the algorithm is about 4% lower than with human evaluators. Other instances turn optimal positive welfare into negative welfare (section "RUMs", paragraph on magnitude).
  - Authors' own stated limitations or scope:
    - The model is stylized: two firms, one hire each, though the authors say it readily generalizes.
    - The authors ask readers to treat the Mallows result with caution, because that model ignores candidate values and so allows arbitrarily large effects ("The Mallows Model").
    - Monoculture does not always lead to adverse outcomes. The paper gives conditions under which it can (Conclusion). Quantitative bounds are left to future work.
  - Relation to the review: RQ3/C4. A precedent for the value of independent errors across decision makers: one shared source of judgments, more accurate than each alternative, can lower the collective outcome because every user inherits the same errors. It supports the review's point that shared errors across samples or models reduce what multiplicity buys.
  - The hinge: the decision makers compete for the same scarce candidates, and the loss arises in sequential selection with a shared ranking. Nothing is aggregated by vote. The review's question concerns samples combined into one answer by majority vote.
- Use 1 — intended claim: "When several decision makers adopt the same algorithm, its errors become correlated across them, and overall welfare can fall even when the shared algorithm is more accurate for each one taken alone."
  - Source passage: "even when the algorithm is more accurate for any one agent in isolation" (Abstract). The algorithmic ranking is identical for all firms that use it ("Modeling Selection"), and the welfare result is Theorem 1.
  - Scope:
    - The formal results cover two firms and require Defs. 2–3. Those conditions hold always under Mallows, in some RUM cases, and never under Plackett–Luce.
    - The paper stresses that its welfare loss needs no assumption of shocks or correlated failures (Significance). It does not depend on the algorithm failing for everyone at once. What is shared is the identical noisy ranking.
    - "Can fall" is right. The paper shows existence, not prevalence.
  - Verdict: NARROW → safe wording: "Kleinberg and Raghavan show, in a stylized model of two firms hiring from the same pool, that when both rank candidates with the same algorithm, and so share its ranking errors, the total quality of their hires can be lower than if each had used its own independent but less accurate ranking, even though the algorithm is more accurate for each firm alone and adopting it is each firm's dominant strategy [kleinberg2021algorithmic]."
- Bib notes:
  - Authors, title, journal, volume 118, issue 22, article number e2018340118 and the DOI are from Crossref and the PMC citation metadata.
  - The month is the issue date (June 2021); online publication was 25 May 2021.
  - The title keeps PNAS's sentence case.

### lam1997application
- Source of record: IEEE Transactions on Systems, Man, and Cybernetics, Part A: Systems and Humans 27(5):553–568, September 1997, DOI 10.1109/3468.618255 (IEEE Xplore document 618255).
- Access: not opened (paywalled on IEEE Xplore; the live Xplore page returned an empty bot-protection response; no author-hosted or institutional copy was found; CiteSeerX is offline); metadata verified.
  - Metadata come from Crossref and from the Internet Archive capture (12 Apr 2024) of https://ieeexplore.ieee.org/abstract/document/618255/, which gives the abstract, volume, issue, pages, date and affiliations.
  - What the paper analyzes was cross-checked against two open secondary sources. The first is Louisa Lam's own later expository paper, "Theory and application of majority vote — from Condorcet jury theorem to pattern recognition" (https://sites.unipa.it/grim/Jlamlouisa.PDF; undated, PDF created 2002), which summarizes the 1997 results and cites them as its reference [4]. The second is Kuncheva, Whitaker, Shipp and Duin, "Limits on the majority vote accuracy in classifier fusion", Pattern Analysis and Applications 6:22–31 (2003), authors' copy at https://www.lucykuncheva.co.uk/papers/lkpaa.pdf (Sec. 1).
- Retraction: none found. The Crossref record has no update relation, and `filter=updates:` returns 0 notices.
- Card:
  - Setting: majority voting among classifiers in pattern recognition (abstract). According to the secondary sources, the domain is handwritten numeral recognition, and a strict majority is required: with no majority the sample is rejected, so the outcomes are correct, error and rejection. The theory takes independent classifiers, first equally accurate with odd and even ensemble sizes, then with unequal accuracies when classifiers are added.
  - What it establishes (abstract): a ground-up analysis of how and why majority voting works. It focuses on how the correct and error rates change when classifiers are added, derives conditions under which adding or eliminating classifiers serves a given objective, and compares the theory with experiments that reflect the predicted trends.
  - From the secondary sources (not seen in the 1997 text):
    - Lam's summary reports these results of the paper. An even ensemble can tie, so the correct rate is not monotone in ensemble size. Specific orderings of the majority-correct probability hold for p < 0.1208 and for p ≥ 0.8090. Adding two classifiers raises the correct rate if the product of their odds ratios exceeds the odds ratio of every existing classifier, a sufficient but not necessary condition. Adding two classifiers to an even ensemble helps the correct rate more, and adding them to an odd ensemble lowers the error rate more.
    - Kuncheva et al. describe the paper as treating equally accurate independent classifiers with odd and even ensemble sizes, finding that the majority beats a single classifier when individual accuracy exceeds 0.5.
  - Headline numbers: the thresholds 0.1208 and 0.8090 above, as reported in Lam's later summary. They were not verified in the 1997 text.
  - Authors' own stated limitations or scope: the abstract claims only that the experiments reflect the predicted trends. Lam's summary adds that independence cannot be assumed in the experiments.
  - Relation to the review: the classical pattern-recognition analysis behind the review's majority-vote calculation (Appendix A, "Majority Voting"), including the role of ensemble parity (ties). It is a precedent, not new evidence.
  - The hinge: the voters are different classifiers deciding among ten digit classes, with a reject option when no strict majority exists. The review analyzes a two-way majority at one key decision among samples of one model, where a correlation between samples is expected.
- Use 1 — intended claim: "Lam and Suen analyzed majority voting among independent classifiers: how its accuracy changes with the number of classifiers and their individual accuracies, including the effect of adding classifiers in odd and even numbers."
  - Source passage: "changes in the correct and error rates when classifiers are added" (Abstract, IEEE Xplore page). The independence assumption and the odd/even analysis are supported only by the secondary sources above.
  - Scope: "accuracy" is two rates here, correct and error, plus rejection, because a strict majority is required. The full text was not read.
  - Verdict: NARROW → safe wording, supported by the abstract alone: "Lam and Suen analyzed how the correct and error rates of majority voting among classifiers change as classifiers are added, and derived conditions under which adding or removing classifiers serves a given objective [lam1997application]." Adding "independent" and "in odd and even numbers" is consistent with the first author's own later summary and with Kuncheva et al. (2003). Confirm both in the full text before printing them.
- Bib notes:
  - Journal, volume 27, issue 5, pages 553–568, September 1997, DOI and ISSN 1083-4427 are from Crossref and the archived IEEE Xplore page.
  - Author names: Crossref and IEEE Xplore give "L. Lam" and "S.Y. Suen". The second author is Ching Y. Suen of Concordia University's Centre for Pattern Recognition and Machine Intelligence, the affiliation Xplore lists; Lam's own later paper and Kuncheva et al. cite him as C. Y. Suen, and Semantic Scholar lists "Ching Y. Suen". The bib uses "Suen, Ching Y.". "Louisa" comes from Lam's later paper (Hong Kong Institute of Education, the affiliation Xplore lists). The printed byline was not seen.
  - The title keeps IEEE's sentence case.

### levy2007speakers
- Source of record: https://papers.nips.cc/paper_files/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html (Advances in Neural Information Processing Systems 19, NIPS 2006, pp. 849–856). The MIT Press volume carries Crossref DOI 10.7551/mitpress/7503.003.0111, issued 7 Sep 2007. Access: full text (proceedings PDF https://papers.nips.cc/paper_files/paper/2006/file/c6a01432c8138d46ba39957a8250e027-Paper.pdf, 8 pp.).
- Retraction: none found. The Crossref record has no update relation, and `filter=updates:` returns 0 notices.
- Card:
  - Setting: 3,452 English relative clauses (RCs) in which the relativizer "that" is optional, from the Switchboard corpus of spontaneous American English speech (Sec. 3, p. 851). They come from about 350 speakers (fn. 10, p. 855). Only finite, restrictive, non-pied-piped, non-extraposed, non-subject-extracted RCs are included (fn. 2, p. 851).
    - Predictability is estimated in two ways: a trigram model trained on Switchboard with the optional relativizers deleted (Sec. 4, p. 852), and an incremental tree-generation model with log-linear features (Secs. 5.1–5.2, pp. 853–854).
    - The predictability estimates enter a logistic regression of relativizer omission with control factors, bootstrapped over speakers (Sec. 5.3, p. 855).
  - What it establishes:
    - Speakers omit "that" more often when the first word of the RC would be predictable without it, and keep it when that word would be surprising (Sec. 4, Fig. 1, p. 852; the text refers to the figure as "Figure 4").
    - Phrasal predictability of the RC remains a significant predictor of omission after the controls (Sec. 5.3, p. 855).
    - Both surface n-gram cues and structural cues contribute to predictability (Sec. 5.4, p. 855).
  - Headline numbers (with location): phrasal predictability gives χ²(1) = 54.3, p < 0.0001 (Sec. 5.3, p. 855). In the two-predictor model, structural predictability gives χ²(1) = 23.55, p < 0.0001, and n-gram predictability χ²(1) = 5.28, p < 0.025. The two measures correlate at r² = 0.70 (Sec. 5.4, p. 855).
  - Authors' own stated limitations or scope:
    - The Sec. 4 correlation alone does not show that speakers are directly sensitive to information density (Sec. 5, p. 852). The regression with controls is the stricter test.
    - The construction was chosen because omitting one word barely changes meaning (Sec. 6, p. 855).
    - Whether the choices ease production or serve the listener is left open (Sec. 6, p. 856).
    - Later work notes that the paper tests a surprisal-versus-length trade-off implied by UID rather than its formal operationalization (Meister et al. 2021, Sec. 2.2, p. 965).
  - Relation to the review: adjacent evidence from psycholinguistics that positions in human language differ in information, and that speakers act to smooth peaks. It is background for RQ1. Under the review's definitions (C1), surprisal is not an error and not importance, so UID bears on how information is spread in text, not on which tokens decide correctness.
  - The hinge: human speakers' choice of an optional function word, measured by surprisal in spontaneous speech. The review's question concerns which generated tokens decide whether an LLM answer is correct.
- Use 1 — intended claim: "The uniform information density hypothesis holds that speakers spread information evenly across an utterance; Levy and Jaeger supported it with optional syntactic reduction, which is more likely where the following material is predictable."
  - Source passage: "speakers are more likely to reduce less information-dense phrases" (Abstract, p. 849). The paper defines UID as avoiding peaks and troughs in information density (Sec. 1, p. 849), with each unit's information as uniform and as close to an ideal value as possible (Sec. 2, p. 850). The supporting regression is in Sec. 5.3 (p. 855).
  - Scope: one construction (the optional relativizer in English RCs), one corpus (Switchboard).
  - Verdict: ACCURATE. A more specific version, if wanted: "...Levy and Jaeger supported it with a syntactic choice: in spontaneous English speech, speakers more often omit the optional relativizer 'that' when the relative clause it would introduce is predictable [levy2007speakers]."
- Bib notes:
  - Pages 849–856, the MIT Press publisher and the DOI are from Crossref and the NeurIPS metadata file. The title is as printed.
  - Author order follows the printed byline and Crossref: Roger Levy (UC San Diego), then T. Florian Jaeger (Stanford and UC San Diego). The NeurIPS proceedings page and its BibTeX list "Jaeger, T. and Levy, Roger", which contradicts the PDF.
  - Year 2007 is the volume's publication year, matching the key. The NeurIPS BibTeX gives 2006, the conference year.
  - Editors are omitted, because the NeurIPS BibTeX misspells one (it gives "T. Hoffman") and Crossref lists none.

### meister2021revisiting
- Source of record: https://aclanthology.org/2021.emnlp-main.74/ (Proceedings of EMNLP 2021, pp. 963–980, Online and Punta Cana, November 2021; DOI 10.18653/v1/2021.emnlp-main.74). Access: full text (ACL Anthology PDF https://aclanthology.org/2021.emnlp-main.74.pdf, main text pp. 963–971 and appendices).
- Retraction: none found. The Crossref record has no update relation, and `filter=updates:` returns 0 notices.
- Card:
  - Setting:
    - Data (Sec. 4, p. 967): English reading times from two self-paced reading corpora (Natural Stories, Brown) and two eye-tracking corpora (Provo, Dundee); acceptability judgments from CoLA and the BNC dataset of Lau et al. (2017); and Dutch eye-tracking (GECO) in App. C.
    - Surprisal comes from GPT-2, TransformerXL, BERT (pseudo-surprisal) and a 5-gram model.
    - Predictors are sentence-level: a sum of surprisal^k and several UID operationalizations, namely variance around a sentence or language mean, local variance, maximum surprisal and Rényi entropy (Sec. 3, pp. 965–967).
    - Fit is measured as ΔLogLik on held-out data with 10-fold cross-validation. Reading times use linear mixed-effects models and acceptability uses logistic regression (Sec. 4.2, p. 968).
  - What it establishes:
    - Acceptability: the best fits have k > 1, a super-linear cost of surprisal. The null hypothesis that k = 1 predicts at least as well is rejected at α = 0.001 (Bonferroni-corrected) for every language model except the n-gram (Sec. 4.3, Fig. 3, p. 969).
    - Reading times: the best fit often has k slightly above 1, but k = 1 stays within a standard error and the null is never rejected. A linear effect of surprisal is not ruled out (Sec. 4.3, p. 969).
    - Super-linear sums and a language-level variance explain the data best. Language-level mean regression beats sentence-level and local versions (Table 1, p. 970; Fig. 4), which the authors read as suggesting that the pressure toward uniformity is global (Abstract, p. 963; Sec. 6, p. 971).
  - Headline numbers (with location): the acceptability tests are significant at α = 0.001 for all models but the n-gram, and the reading-time tests are never significant (p. 969). BERT pseudo-surprisal predicts acceptability well but reading times poorly (p. 969).
  - Authors' own stated limitations or scope: the analysis covers English, with Dutch in the appendix, and written-language data only; spoken data should be analyzed. It cannot fully test whether the pressure acts at the level of the whole language, or whether there is a cross-linguistic channel capacity. The link between language-model quality and psychometric predictive power has itself been questioned (Sec. 5, p. 971).
  - Relation to the review: adjacent evidence on whether information is spread evenly in human text. Comprehension-side support for UID is clear for acceptability and weak for reading times. It is background for RQ1: uniformity of surprisal is a graded tendency, not a law.
  - The hinge: human judgments and reading times on human-written sentences, with surprisal estimated by language models. The review's question concerns which positions in LLM-generated answers decide correctness.
- Use 1 — intended claim: "Reading times and acceptability judgments show a preference for evenly distributed surprisal."
  - Source passage: "non-uniformity in information density is predictive of lower acceptability" (Abstract, p. 963). For reading times, the abstract says only that the results are also consistent with a weakly super-linear effect, and Sec. 4.3 (p. 969) never rejects the linear hypothesis.
  - Scope: English written data. The evidence is clear for acceptability and only compatible for reading times.
  - Verdict: NARROW → safe wording: "Meister et al. found that English sentences whose surprisal is distributed less evenly are judged less acceptable; sentence-level reading times are consistent with the weakly super-linear cost of surprisal that uniform information density implies, but do not rule out a linear cost [meister2021revisiting]."
- Bib notes: everything follows the ACL Anthology .bib export: authors including J{\"a}ger, title with protected {U}niform {I}nformation {D}ensity, booktitle, pages 963–980, address, publisher, November 2021, DOI and URL. Editors are omitted, as in the other ACL entries.

### lecun2023why (additional use)
- Source of record: LinkedIn post, https://www.linkedin.com/posts/yann-lecun_i-have-claimed-that-auto-regressive-llms-activity-7045908925660950528-hJGk. Access: full text of the post, re-read on 2026-10-03 from the page's LD-JSON (`SocialMediaPosting`, `articleBody`). `datePublished` is 2023-03-27T00:06:34.510Z, and the author is Yann LeCun. The page served the post publicly (HTTP 200); the "captcha" string in the page is a configuration attribute, not a challenge. The post links its full slide deck through https://lnkd.in/eueY5EAq, which resolves to a Google Drive file. The deck was not opened and is not the cited source.
- Retraction: n/a (a social-media post, still live on 2026-10-03).
- Card (for this use only; ledger part A holds the post's two earlier uses, which it also numbers Use 1 and Use 2):
  - Setting: an informal argument with no data. The post calls itself LeCun's introductory position statement for the NYU debate "Do large language models need sensory grounding for meaning and understanding?"
  - What it establishes: claims, not evidence. It defines e as the probability that any generated token exits the tree of correct answers and concludes (1−e)^n. It states that errors accumulate and that correctness decreases exponentially. Training can make e smaller but cannot eliminate the problem, and a solution would need non-autoregressive LLMs that keep their fluency.
  - Headline numbers: none.
  - Authors' own stated limitations or scope: none stated.
  - Relation to the review: this is the argument the review examines. The new use records the conclusion LeCun draws from it.
  - The hinge: a constant per-token exit probability e and an absorbing failure state, both implicit. Positions are not distinguished and recovery is ruled out.
- Use 2 — intended claim: "The argument has been used to predict a ceiling on what autoregressive systems can do."
  - Source passage: "A solution would require to make LLMs non auto-regressive while preserving their fluency" (post body, last paragraph of the argument). The sentence just before it says the problem can be mitigated by making e smaller through training, but cannot be eliminated entirely.
  - Scope:
    - The post claims an inherent limitation of autoregressive generation: correctness falls exponentially with answer length, and training can reduce the problem but not eliminate it. It does not use the word "ceiling", and it makes no claim about capabilities in general.
    - "Has been used" is passive. The one cited source is LeCun's own post, so the sentence should name him.
  - Verdict: NARROW → safe wording: "LeCun used the argument to conclude that the problem is intrinsic to autoregressive generation: training can make e smaller but cannot eliminate it, and a solution would require models that are not autoregressive [lecun2023why]." If "ceiling" is kept, make it "an inherent limit on the reliability of long autoregressive outputs" and attribute it to LeCun.
- Bib notes: no new entry. The key is in A_v3_carryover.bib, and I re-checked it today. The title is the post's opening sentence, the month (March 2023) matches the LD-JSON `datePublished`, and the URL serves the post. It is correct as it stands.
