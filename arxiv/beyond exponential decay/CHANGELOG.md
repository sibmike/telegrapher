# Changelog — Beyond Exponential Decay (arXiv:2505.24187)

## v3 (prepared 2026-09-20, not yet uploaded)

Built from `main.tex` + `body.tex` in this folder (`bash build.sh`). The same `body.tex` is copied verbatim into the NeurIPS-format package.

### Corrected statistics and attributions (each checked against the cited source)

| Location | v2 text | v3 text | Source |
|---|---|---|---|
| §1, §2, §4.1, App. B | "in Llama-3" (attention-recovery figure) | "in Llama-3-8B" | RetrievalAttention §2.3, Fig. 2 (arXiv:2409.10516) |
| §1, §2, §3.1, §4.1, §6 | "~9% of tokens ... depend on distant context" | "fewer than 10% of tokens ... gain from context beyond the preceding 4,096 tokens (GovReport)" | LongPPL §2.2 & Fig. 4a: key token = LSD > 2 against a 4096-token window and LCL > −2 (arXiv:2410.23771; PKU-ML/LongPPL code) |
| §4.1 | "perplexity on the other 91% ... essentially zero correlation" | LongPPL vs LongBench r = −0.96; plain PPL r = −0.18; non-answer-token PPL uninformative on LongEval | LongPPL Fig. 1b, Fig. 2 |
| §4.1 | TextFooler "flips decisions by perturbing 5–10% of tokens; random perturbation of much larger fractions does nothing" | "3.5%–22% of words depending on task/model (4–6% IMDB, 14–18% NLI); ablation: random word choice raises after-attack accuracy by >45 points" | TextFooler Tables 3–4 and Ablation (arXiv:1907.11932) |
| Abstract, §2, §3.1, §4.1 | Anchor-LLM "99% context reduction with <1.5% accuracy loss" | "up to 99% keys/values-cache reduction at an average accuracy cost of about 1.5%" | AnLLM abstract and Table 1 (arXiv:2402.07616) |
| §3.1 | Anchor result "requires k to be effectively bounded" | "consistent with a bounded number of load-bearing positions per span" | hedged; the paper does not measure k |
| §5, App. B | AIMO-2 tool integration "fires Python execution at high-entropy spans" | model emits code blocks itself, budget of 1–8 executions per solution; GenSelect numbers added (76.3% majority@64 vs 90.0% GenSelect, 14B, Comp-Math-24-25) | OpenMathReasoning paper §TIR, §GenSelect (arXiv:2504.16891) |
| App. A | TPT lets small models "match models 30× larger" | "roughly an order of magnitude larger" | TPT abstract: Gemma2-9B (82%) matches LLaMA-3.1-70B (arXiv:2504.18116) |

### Citation-audit fixes (three-audit pass, 2026-09-20; 29 entries, none hallucinated)

| Item | v2/draft | v3 | Source |
|---|---|---|---|
| `viswanathan2024geometry` | cited as ICLR 2025 under the arXiv v1 title | TMLR (2026), "The Intrinsic Dimension of Prompts in Internal Representations of LLMs"; old title kept in `note` | arXiv:2501.10573 comments; OpenReview 23adDIOrjB |
| §4.2 Li & Sarwate | domains "(scientific text, dialogue, code)" | "(movie and product reviews, tweets, news)" — their actual datasets | arXiv:2502.13577, datasets section |
| App. A | "Trace-Prune-Train" | "Think-Prune-Train (TPT)" | arXiv:2504.18116 title |
| §2 lost-in-the-middle | "models disproportionately attend to ..." | "models perform best when the relevant material sits near the beginning or end" (the paper measures accuracy, not attention) | arXiv:2307.03172 |
| §2 Gwern | "evidence curated in" | "self-correction examples collected in" (a bibliography is not a finding) | — |
| §1 Snell | "on equivalent reasoning tasks" | "on reasoning problems where the smaller model already has a non-trivial success rate" | arXiv:2408.03314 abstract |
| §2 ToT, §4.2 Robinson | mechanism glosses stated as the sources' claims | glosses marked as our reading / restated in the sources' terms | — |
| §6, §7 | "4% to 22%", "5%–10% of tokens" | "3.5% to 22%", "under a tenth of tokens" | consistency with §4.1 and Fang et al. |
| bib metadata | — | full 26-author list for Kwa et al.; pages for Liu 2024 (TACL), Pang 2024, Morris 2020, Zhu 2024 (+DOI); Snell → ICLR 2025; Wu → EMNLP 2025; "Eric J. Bigelow" | ACL Anthology, AAAI OJS, OpenReview, arXiv |

### Math fixes

- §3.1: stated the summability condition on non-key error rates (Σ e_non(i) < ∞) without which the non-key factor is itself exponential; wrote out the regime-1 algebra; saturating regime needs both k → k_max and summability.
- §3.2: rewrote the union-bound paragraph. v2 compared k·e_key with 1−(1−e)^n (different rates) and said correlation "cuts" the union bound. v3: the bound holds regardless of correlation; compare with n·e (ratio k/n); correlation is a separate effect that lowers P(≥1 failure) below the independent value 1−(1−e_key)^k.
- §3.3: v2 gave f → e_key^(m−1) at ρ = 0 as the majority-vote gain. That is Pass@m with an oracle verifier. v3 gives both: oracle e_key^(m−1); majority vote = binomial tail ≤ exp(−2m(1/2 − e_key)^2) for e_key < 1/2 (Hoeffding), and notes that the e_key < 1/2 condition is why voting fails on knowledge-gap errors.

### New material

- Fig. 1 (`figures/fig1_decay_regimes.pdf`): uniform vs three two-rate regimes, illustrative parameters stated in caption. Source: `figures/fig1_decay_regimes.tex` (pgfplots) + `figures/make_fig1_data.py`.
- §2 new paragraph "Decision-point tokens in reasoning": Bigelow et al. 2025 (ICLR), Lin et al. 2024, Wang et al. 2025 (NeurIPS).
- §2 and §6: engagement with the step-level counter-evidence — Kwa et al. 2025 (METR time horizons), Ord 2025 (constant hazard rate), Sinha et al. 2026 (self-conditioning). §6 reconciles: k ∝ n_steps in agentic tasks gives exponential decay in task length; the two-rate model rules out exponential decay in tokens at fixed decision count.
- §6: k/n is criterion-dependent (<10% long-context, ~20% entropy, 4–22% perturbation); a concrete k(n) measurement protocol (LSD-key count at n ∈ {1,2,4,8,16}K for window K, fit k ∝ n^b) and what a null result (b ≈ 1) would mean.
- §7: forward pointer to Part 2 (arXiv:2605.30628).
- Abstract: one sentence marking where the argument stops (long-horizon agentic tasks).

### Source layout

- `template.tex` (the v1 body, 3-author block) moved to `legacy_v1/`. It did not correspond to the published v2.
- `body.tex` is now shared with `neurips/paper_beyond_exponential_decay/submission/` (verbatim copy).

## v2 (2026-05-06)

Tightened rewrite of the v1 text in NeurIPS preprint format; five-author block. Posted before the 15–17 May 2026 bibliography audit, so it still contained the "96% of attention", "1B beats 405B [Venture Research]" and "Gao >80%" statements that the repo had already corrected.

## v1 (2025-05-30)

Original preprint.
