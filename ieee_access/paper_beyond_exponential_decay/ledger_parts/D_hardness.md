<!-- Ledger part D: pillar 2, token hardness (pivotal and decision tokens, entropy-gated decoding, early commitment, confident errors). Audited 2026-10-03.
Method notes:
- Full text read for all 14 papers; none is abstract-only. For the 8 papers with a venue version I read the venue text (NeurIPS proceedings PDF, PMLR PDF, five ACL Anthology PDFs, and the ACM camera-ready as posted on arXiv) and compared it with the latest arXiv full text. Cited passages and numbers agree between versions unless a note says otherwise. The other 6 papers are arXiv-only and were read in their latest version.
- Page numbers are physical PDF pages of the version named under "Access".
- Venues were confirmed on official pages: the NeurIPS 2024 proceedings page and its BibTeX export, PMLR v235, ACL Anthology volume pages and .bib exports (ACL 2025, EMNLP 2025, Findings of EMNLP 2025, EACL 2026, Findings of ACL 2026), and the FSE 2026 research-track programme on conf.researchr.org together with the Crossref record for DOI 10.1145/3808142. Rejected or workshop-only status comes from the OpenReview search API (venue and venueid fields).
- Not used: DBLP (dblp.org resets the connection and the mirror serves a bot check) and the ACM Digital Library (Cloudflare check). Neither check was bypassed. Semantic Scholar rate-limited most queries; where it answered, it listed arXiv only.
- Retraction check: Crossref works?query.bibliographic=<title>&rows=3, repeated with filter=update-type:retraction. I looked for update-to and relation fields and checked each arXiv abs page for a withdrawal notice. Nothing was found for any paper.
- Quote policy (same as ledger part C): one short verbatim phrase (under 15 words) per paper. All other evidence is paraphrased and located by section, table or figure, and page. Typographic quotes and dashes are normalised to ASCII.
- Keys are unchanged as instructed. Two keys carry a year that differs from the publication year: li2025egb (EACL 2026) and he2025adadec (Proc. ACM Softw. Eng. 3(FSE), 2026).
-->

### lin2024rho1
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2024/hash/3322a9a72a1707de14badd5e552ff466-Abstract-Conference.html (NeurIPS 2024, oral per OpenReview: Advances in NeurIPS 37, pp. 29029-29063, DOI 10.52202/079017-0914). Access: full text (NeurIPS camera-ready https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf and arXiv v4 https://arxiv.org/html/2404.07965v4; the cited passages are identical).
- Retraction: none found. Crossref record 10.52202/079017-0914 has no update or retraction relation, and the arXiv abs page shows no withdrawal.
- Use 1 — intended claim: "training only on selected useful tokens matches or beats uniform loss"
  - Source passage (paraphrase): Selective Language Modeling (SLM) applies the loss only to the top k% of tokens, ranked by excess loss: the training model's loss minus that of a reference model trained on curated data (Sec. 2.2, p.4). On the same OpenWebMath tokens, it beats ordinary continual pretraining by 16.5 points of average few-shot accuracy over 9 math tasks at 1B and by 10.4 points at 7B (Table 1, p.5; Sec. 3.2, p.6-7). On 80B general tokens with TinyLlama-1.1B, the average gain over 15 benchmarks is 6.8% (Sec. 3.3, p.7).
  - Scope: Continual pretraining only, of TinyLlama-1.1B and Mistral-7B; nothing is trained from scratch. The selection keeps 60% of tokens at 1B and 70% at 7B (Sec. 3.1, p.6), a majority rather than a few. The reference model needs 0.5B curated math tokens, partly GPT-generated (Sec. 3.1, p.5-6).
  - Verdict: ACCURATE. For our pillar, do not suggest that the kept tokens are few or that they are the "hard" ones (see Other findings ii).
- Use 2 — intended claim: "e.g., matching DeepSeekMath with 3% of pretraining tokens"
  - Source passage: "matching DeepSeekMath with only 3% of the pretraining tokens" (Abstract, p.1).
  - Scope: The match is on MATH after fine-tuning on the 69k-example ToRA tool-integrated corpus: Rho-1-7B scores 51.8% against DeepSeekMath-7B's 52.0% (Table 2, p.6; Sec. 3.2, p.7). The 3% compares math continual-pretraining tokens: 15B OpenWebMath tokens (10.5B of them selected) against DeepSeekMath's 500B, on different base models. Before fine-tuning, few-shot Rho-1-7B is described as comparable but scores lower: average 66.2 vs 68.4, MATH 31.0 vs 34.2 (Table 1, p.5).
  - Verdict: NARROW → safe wording: "Rho-1 continues pretraining Mistral-7B on 15B math tokens, applying the loss only to the 70% of tokens with the highest excess loss over a reference model. After tool-integrated fine-tuning it reaches 51.8% on MATH, on par with DeepSeekMath-7B (52.0%), which used about 33 times as many math pretraining tokens [lin2024rho1]."
- Other findings a reviewer would expect:
  - (i) Token-level training dynamics (Sec. 2.1, p.3): during continual pretraining of TinyLlama-1B on OpenWebMath, only 26% of tokens show a marked loss reduction and 51% are already learned. Another 11% stay at high loss throughout, which the authors attribute to high aleatoric uncertainty. This is heterogeneous token difficulty, but at training time.
  - (ii) The useful tokens are not the hard ones. The score is excess loss over the reference model, so tokens that stay hard for both models score low and tend to be dropped; the authors present SLM as filtering out noisy and irrelevant tokens. Citing Rho-1 for "hard tokens matter most" would reverse its meaning.
  - (iii) In the self-reference variant (Sec. 3.4, Table 3), scoring by the reference model's loss or by its next-token entropy both help. Intersecting the two gives +3.3% with 40% fewer training tokens, so an entropy score also works for training-data selection.
  - (iv) The arXiv title is "Rho-1: Not All Tokens Are What You Need"; the NeurIPS title adds "for Pretraining". The bib uses the NeurIPS title.

### abdin2024phi4
- Source of record: https://arxiv.org/abs/2412.08905. This is a Microsoft technical report: arXiv only, single version v1 (12 Dec 2024), not peer reviewed. Access: full text (https://arxiv.org/html/2412.08905v1 and the v1 PDF).
- Retraction: none found. There is no Crossref record for the title and no withdrawal notice on arXiv.
- Use 1 — intended claim: "correctness depends on generating a small number of pivotal tokens"
  - Source passage: "highly dependent on a successful generation of a small number of key tokens" (Sec. 4.3 Pivotal Token Search, p.14). The sentence is hedged: the authors say this is often the case, not always. They call these tokens pivotal because sampling them sharply changes the probability that the solution ends correct (Sec. 4.3, p.14).
  - Scope: This is a qualitative observation illustrated with one example: GPT-4o at temperature 1 on a single MATH problem, with success probability estimated from 529 independent completions after each prefix (Fig. 3 caption, p.13). The report does not count how many pivotal tokens a typical solution contains.
  - Verdict: NARROW → safe wording: "The Phi-4 report observes that correctness often hinges on a few pivotal tokens, those whose sampling sharply changes the estimated probability that the solution ends correct [abdin2024phi4]."
- Use 2 — intended claim: "Pivotal Token Search builds DPO pairs at those tokens only"
  - Source passage (paraphrase): PTS samples completions after each prefix and checks them with an oracle to estimate the probability of success. It splits the solution recursively until it isolates single tokens that change that probability sharply. Each one becomes a preference pair: the query is the prefix, and the accepted and rejected completions are single tokens, so the DPO update acts on one token (Sec. 4.3, p.14; pseudocode in Fig. 4).
  - Scope: Applied to math, several kinds of QA, and coding, where answers can be checked. Questions are limited to success probabilities between 0.2 and 0.8, because pivotal tokens are rare on very easy or very hard tasks (p.14). PTS supplies the first of two DPO rounds; the second is judge-guided DPO on full responses (Sec. 4.2, p.12).
  - Verdict: ACCURATE.
- Other findings a reviewer would expect:
  - (i) Pivotal tokens are not the low-probability tokens. Fig. 3 (p.13) underlines tokens with probability at most 0.1 precisely to show the two sets differ, and the main pivotal token in the example had probability 0.31. Detectors based on entropy or probability will not necessarily find pivotal tokens.
  - (ii) Pivotal tokens are often not mistakes. They are choices that steer the model onto a less favourable path (p.14).
  - (iii) Ablation (Sec. 4.5, Table 9, p.16-17): relative to SFT, pivotal-token DPO alone raises MATH from 77.1 to 80.5 and GPQA from 47.3 to 53.6. The authors find it most useful on reasoning-heavy tasks and complementary to judge-guided DPO.
- Venue/bib notes: There is no venue; the bib cites the arXiv report with all 27 authors as listed there.

### bogdan2025anchors
- Source of record: https://arxiv.org/abs/2506.19143 (v4, 27 Oct 2025). Venue claim: the paper was not accepted at ICLR 2026. OpenReview lists it as a rejected ICLR 2026 submission (https://openreview.net/forum?id=6NUtPO9PdV). It was a spotlight at the non-archival Mechanistic Interpretability Workshop at NeurIPS 2025 (https://openreview.net/forum?id=VnSlfeRCaU). Cite arXiv. Access: full text (https://arxiv.org/html/2506.19143v4 and the v4 PDF).
- Retraction: none found.
- Use 1 — intended claim: "a few sentences (mostly planning/uncertainty-management) have outsized counterfactual influence on reasoning outcomes, measured by resampling"
  - Source passage: "certain sentences can have an outsized impact on the trajectory of the reasoning trace" (Abstract, p.1). The abstract adds that these "thought anchors" are generally planning or uncertainty-management sentences. Sec. 3.3 (p.5) reports that plan-generation and uncertainty-management sentences have consistently higher mean counterfactual importance than fact-retrieval or active-computation sentences.
  - Scope: The main model is DeepSeek-R1-Distill-Qwen-14B at temperature 0.6, on 20 MATH problems it solves 25-75% of the time, with one correct and one incorrect trace per problem (Sec. 2.1, p.3). Each sentence gets 100 rollouts. Importance is the KL divergence between final-answer distributions with and without the sentence, conditioned on semantically different resamples (Sec. 3.2). The category pattern was replicated on R1-Distill-Llama-8B (App. B, p.14). The paper never counts how many sentences are anchors; the category result compares means. The authors call the work preliminary (Sec. 8, p.10).
  - Verdict: NARROW → safe wording: "Resampling each sentence of reasoning traces 100 times, Bogdan et al. find that certain sentences, mostly plan-generation and uncertainty-management steps, have outsized counterfactual influence on the final answer of distilled R1 models on MATH problems [bogdan2025anchors]."
- Other findings a reviewer would expect:
  - (i) The unit is the sentence, not the token. In the case study, resampling at the token level over the first 1,000 tokens gives the same picture as resampling sentences, at much higher cost (Sec. 2.4 and Fig. 2, p.3).
  - (ii) The answer depends on how importance is measured. Forced-answer importance instead singles out active computation (Sec. 3.3, Fig. 3A).
  - (iii) Planning and uncertainty-management sentences also produce semantically different resamples more often (App. I), and the counterfactual measure conditions on exactly those resamples. The authors note it becomes noisy when few divergent resamples exist.
  - (iv) The attention-based (receiver-head) analyses are confounded by sentence position (Sec. 8, p.10).

### li2025egb
- Source of record: https://aclanthology.org/2026.eacl-long.235/ (EACL 2026, Volume 1: Long Papers, pp. 5054-5069, Rabat, DOI 10.18653/v1/2026.eacl-long.235). arXiv:2503.21961 v4 (27 Jan 2026) matches the EACL text, including Tables 1-4. Access: full text (EACL PDF https://aclanthology.org/2026.eacl-long.235.pdf and arXiv v4 HTML).
- Retraction: none found. Crossref 10.18653/v1/2026.eacl-long.235 has no update relation.
- Use 1 — intended claim: "branching only at high-uncertainty steps improves accuracy (+22.6%)"
  - Source passage: "EGB improves accuracy by 22.6% over standard inference" (Abstract, p.1).
  - Scope:
    - Baseline: The 22.6% is a relative gain over standard single-path decoding (greedy in Table 4), not over beam search.
    - Number: The figure appears only in the abstract. The results text gives an average gain of 18.4% across all models and benchmarks, with absolute gains of 3-8 points in most settings (Sec. 5, p.5). Recomputing from Table 1 (p.6), 18.4% is the ratio of mean accuracies over the 30 model-benchmark cells. I could not reproduce 22.6% from Table 1. The 22.6% first appeared in the arXiv v2 abstract, which also claimed a 37% speed-up over beam search. It is unchanged in the v3, v4 and EACL abstracts, while the current results text gives 18.4%.
    - Method: EGB is beam search guided by a process reward model (beam size 4, width 4, Qwen2.5-Math-PRM-7B). It branches only where next-token entropy exceeds a threshold, tuned separately for each model family (Sec. 3-4).
    - Models and benchmarks: Qwen3 1.7B/4B/8B in non-thinking mode, Llama-3.2-1B/3B and Llama-3.1-8B, on CFA Level I/II mock exams, AIME 2022-24, MATH-500 and GSM8K. Correctness was judged by Gemini 2.5 Flash (App. A, p.12).
  - Verdict: NARROW → safe wording: "Entropy-gated branching, a reward-model-guided beam search that branches only where next-token entropy exceeds a threshold, raises accuracy over single-path decoding by 18.4% (relative) on average across six 1-8B models and five math and finance benchmarks [li2025egb]." Do not use 22.6%, and do not attribute the gain over standard decoding to the gating alone, since most of it comes from verifier-guided search.
- Use 2 — intended claim: "and is faster than beam search"
  - Source passage (paraphrase): Compared with uniform reward-model-guided beam search at the same budget, EGB runs 31-75% faster across the evaluated benchmarks (Sec. 5.2 and Fig. 3 right, p.8). Its accuracy is comparable or better in 67% of settings (Sec. 5.1, p.7).
  - Scope: Same models, benchmarks and verifier as Use 1. In the entropy-threshold sweep, a threshold of 0 reduces to beam search and an infinite threshold to self-consistency. Broad intermediate ranges beat both endpoints (App. A.2, Table 3, p.14-15).
  - Verdict: ACCURATE for speed. If accuracy against beam search is mentioned, write "matched or exceeded it in two-thirds of settings".
- Other findings a reviewer would expect:
  - (i) The motivating observation (Sec. 1, p.2): in the authors' analysis, 39 of 50 high-entropy spikes coincided with a flawed reasoning step. The abstract also states that a small subset of uncertain steps has a disproportionate effect on accuracy. How the 50 spikes were sampled is not described.
  - (ii) Beam search beats EGB in several cells, especially for the small Llama models (Table 1, p.6). EGB's advantage over beam search grows with model size (Sec. 5.1).
  - (iii) Results depend on the verifier. Swapping the reward model changes absolute accuracy. EGB's gain over beam search holds for Qwen3-1.7B under both reward models, but for Llama-1B under the default one it is -0.49 points (App. A.2, Table 2, p.14).
  - (iv) In thinking mode, the smallest Qwen3 model gains nothing over beam search (Table 4, p.15).

### he2025adadec
- Source of record: https://doi.org/10.1145/3808142. This is Proc. ACM Softw. Eng. 3(FSE), Article FSE135, pp. 3047-3069, July 2026, listed in the FSE 2026 Research Papers track at https://conf.researchr.org/track/fse-2026/fse-2026-research-papers. Metadata comes from Crossref, because the ACM Digital Library page sits behind a browser check that was not bypassed. Access: full text (arXiv v5 https://arxiv.org/abs/2506.08980v5). That version is the authors' camera-ready, carrying ACM's reference format, the article number, the DOI and a CC BY 4.0 notice.
- Retraction: none found. Crossref 10.1145/3808142 has no update relation.
- Use 1 — intended claim: "many code-generation errors occur at high-uncertainty steps where the correct token is present but not top-ranked"
  - Source passage: "where the correct token is present but not top-ranked" (Abstract, p.1). The phrase completes the authors' summary that many generation errors stem from token-ranking mistakes at high-uncertainty steps.
  - Scope:
    - Data: The empirical study (Sec. 2.2, p.4-5) uses one model, DeepSeek-Coder-6.7B-Instruct with greedy decoding on HumanEval. Failed solutions were compared with the reference solution through AST diffs plus human annotation. This gave 46 "logic drift" points, one in each of 46 problems, against 2,889 other decoding steps from the same generations.
    - Entropy: At drift points the median entropy is 1.26, against 0.03 at other steps; 87% of drift points fall at the start of a line.
    - Rank evidence: That the correct token usually sits second or third comes from the authors' first manual inspection (Sec. 2.2.1, p.4) and is not tabulated.
    - Other models: Across nine models, entropy correlates moderately with the rank of the ground-truth token (Spearman 0.46-0.52; Sec. 2.3, Table 1).
  - Verdict: NARROW → safe wording: "In DeepSeek-Coder-6.7B's failed HumanEval solutions, the steps where program logic first goes wrong carry far higher entropy than other steps (median 1.26 vs 0.03), and the correct token there is typically ranked just below the top rather than absent [he2025adadec]."
- Use 2 — intended claim: "uncertainty-gated lookahead raises Pass@1 by up to 20.9%"
  - Source passage (paraphrase): AdaDec pauses only when entropy exceeds a learned, model-specific threshold, then reranks the top candidates by a short lookahead. Over greedy decoding, this raises Pass@1 on all three benchmarks, by +3.59 points on average on HumanEval+, +7.61 on MBPP+ and +4.53 on DevEval. The 20.9 is the single largest cell: Qwen3-0.6B on MBPP+, +20.90 points (Sec. 4.2, p.12-13).
  - Scope: Nine open models of 0.6-8B. Beam search with the same width (3) gains less; on DevEval, for example, it gains +1.45 against AdaDec's +4.53. AdaDec pauses at 0.85-12.17% of decoding steps, about 6.75% on average (Sec. 4.3, p.13).
  - Verdict: NARROW → safe wording: "Pausing for lookahead reranking only at high-entropy steps (about 7% of steps) raises Pass@1 over greedy decoding by 3.6-7.6 points on average per benchmark, up to 20.9 points for one model, and beats beam search of the same width [he2025adadec]." Write "points" (absolute), not "%".
- Other findings a reviewer would expect:
  - (i) Gains are largest on MBPP+ and smallest on HumanEval+. For some models AdaDec is even faster than greedy decoding, because it avoids degenerate, overlong outputs (Sec. 4.3).
  - (ii) The trigger is Shannon entropy alone, which the authors call a coarse signal (Sec. 5.2). They recommend re-learning the threshold after fine-tuning or alignment (Sec. 5.1).
  - (iii) The benchmarks are small; HumanEval+ has 164 problems, which the authors list as a threat to validity (Sec. 6).
- Venue/bib notes: FSE 2026 is confirmed. The publication is the PACMSE journal issue, so the bib is @article. Crossref dates it 2026-06-30, while ACM's reference format in the camera-ready says July 2026; the bib follows ACM.

### xia2025tokenskip
- Source of record: https://aclanthology.org/2025.emnlp-main.165/ (EMNLP 2025 main conference, pp. 3351-3363, Suzhou, DOI 10.18653/v1/2025.emnlp-main.165). Access: full text (ACL Anthology PDF and arXiv v3 camera-ready https://arxiv.org/html/2502.12067v3; the cited passages are identical).
- Retraction: none found.
- Use 1 — intended claim: "CoT tokens can be cut ~40% on GSM8K with <0.4% accuracy drop"
  - Source passage: "reduces reasoning tokens by 40% (from 313 to 181) on GSM8K" (Abstract, p.1). The abstract states this for Qwen2.5-14B-Instruct, with a drop it gives as under 0.4%.
  - Scope:
    - Training: The result requires fine-tuning. The model is LoRA-tuned on its own correct chains of thought, pruned to random target ratios by LLMLingua-2, an external BERT-sized token-importance classifier (Sec. 3 and Sec. 4.1, p.5).
    - The figure: It covers one model on one benchmark. App. B.2, Table 2 (p.12) gives accuracy 93.1 to 92.7, a drop of 0.4 points, at ratio 0.6 (313 to 181 tokens, actual ratio 0.57).
    - Other settings: Smaller models lose more at the same ratio (Qwen2.5-7B -3.5 points, 3B -6.4). LLaMA-3.1-8B on MATH-500 saves about 30% of tokens for a drop under 4% (Sec. 4.2, p.6).
  - Verdict: NARROW → safe wording: "After fine-tuning on chains of thought pruned of low-importance tokens, Qwen2.5-14B-Instruct produces about 40% fewer reasoning tokens on GSM8K (313 to 181) at a cost of 0.4 accuracy points; smaller models and harder problems lose more [xia2025tokenskip]."
- Other findings a reviewer would expect:
  - (i) The skipped tokens are low-importance filler such as connectives; numbers and equations are kept, and the number of reasoning steps does not fall (Sec. 4.3 Case Study, p.7). This is evidence of redundancy, not of a few decision tokens.
  - (ii) Naive truncation to the same length collapses accuracy: -79 points on GSM8K at ratio 0.5 for LLaMA-3.1-8B (Table 1, p.6). Which tokens are removed matters.
  - (iii) Below a ratio of 0.5 the model no longer hits its target ratio (Sec. 4.3).

### zheng2025processbench
- Source of record: https://aclanthology.org/2025.acl-long.50/ (ACL 2025, Volume 1: Long Papers, pp. 1009-1024, Vienna, DOI 10.18653/v1/2025.acl-long.50). Access: full text (ACL Anthology PDF and arXiv v4 https://arxiv.org/html/2412.06559v4).
- Retraction: none found.
- Use 1 — intended claim: "the earliest erroneous step in math reasoning is a well-defined, annotatable location"
  - Source passage: "the earliest step that contains an error, or conclude that all steps are correct" (Abstract, p.1). This is the task models must solve.
  - Scope:
    - What it shows: ProcessBench defines this target and gets experts to agree on it, with effort, for 3,400 solutions to GSM8K, MATH, OlympiadBench and Omni-MATH problems from 12 Qwen and LLaMA models.
    - Step boundaries: Qwen2.5-72B-Instruct re-segmented the steps to standardise their granularity (Sec. 3.2, p.4).
    - Annotation: Each solution went to three annotators with doctoral-level mathematical expertise, and to more if they disagreed. It was discarded if three of up to five could not agree, which removed about 30% of solutions (Sec. 3.2, p.5). Even among the erroneous samples that were kept, only 48-67% reached agreement among the first three annotators (Table 2, p.5).
    - Why the earliest error: The authors focus on it because later steps built on an error have ambiguous correctness (Sec. 3.1, p.3). They acknowledge that wrong labels may remain on Olympiad-level problems (Limitations, p.9).
  - Verdict: NARROW → safe wording: "ProcessBench operationalises a reasoning error as the earliest erroneous step and obtains expert-consensus labels for it on 3,400 competition-math solutions, although about 30% of candidate solutions were dropped for lack of consensus [zheng2025processbench]."
- Other findings a reviewer would expect:
  - (i) Errors concentrate early. Most first errors fall in steps 0-3 on GSM8K and MATH and in steps 1-5 on OlympiadBench and Omni-MATH (Sec. 3.3 and Fig. 3, p.5). This supports early-commitment arguments.
  - (ii) Correct final answers often hide process errors. The share of correct-answer solutions containing an erroneous step is 3.5% on GSM8K, 18.8% on MATH, 32.2% on OlympiadBench and 51.8% on Omni-MATH (Sec. 3.3, p.5-6). Outcome-level reliability overstates process-level reliability.
  - (iii) Existing process reward models generalise poorly to harder problems; prompted critic models (QwQ-32B-Preview, GPT-4o, o1-mini) do better (Sec. 4).

### zhang2024snowball
- Source of record: https://proceedings.mlr.press/v235/zhang24ay.html (ICML 2024 poster, PMLR 235:59670-59684). Access: full text (PMLR PDF https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ay/zhang24ay.pdf). arXiv v1 (May 2023) is an earlier, shorter version: it covers ChatGPT and GPT-4 only, has no LLaMA-2 results and a different section structure. Cite and quote the ICML version.
- Retraction: none found. PMLR does not register DOIs, so there is no Crossref record; arXiv shows no withdrawal.
- Use 1 — intended claim: "models commit to an early wrong answer and then justify it"
  - Source passage (paraphrase): The authors build three yes/no question sets that a model cannot answer correctly in a single step: primality testing, senator search and graph connectivity, with 500 questions each. GPT-3.5 and GPT-4 commit to Yes or No in the very first token over 95% of the time (98.40% and 95.67%; Sec. 2, p.2), and LLaMA-2-70B-chat within the first few tokens (Sec. 1, p.1). A wrong commitment is then justified with an incorrect claim, such as a wrong factorisation or a nonexistent flight (Sec. 3, p.2-5).
  - Scope: Zero-shot prompting that asks for the answer first, with greedy decoding, on synthetic tasks whose correct label is fixed.
  - Verdict: NARROW → safe wording: "Asked to answer first, GPT-3.5, GPT-4 and LLaMA-2-70B-chat commit to yes or no within the first token or first few tokens and, when that answer is wrong, justify it with false claims [zhang2024snowball]."
- Use 2 — intended claim: "they can recognize 67% (ChatGPT) and 87% (GPT-4) of their own mistakes when asked separately"
  - Source passage: "can identify 67%, 87%, and 94% of these incorrect claims" (Abstract, p.1). These figures are for GPT-3.5, GPT-4 and LLaMA2-70B-chat; the exact rates are 67.37%, 87.03% and 93.67% (Sec. 3.4, p.5).
  - Scope: The percentages are of the incorrect claims inside the justifications, checked in a separate session. They are not percentages of all mistakes, nor of the initial wrong answers. The ICML version calls the first model GPT-3.5 (gpt-3.5-turbo), not ChatGPT.
  - Verdict: NARROW → safe wording: "Yet when each false justification is put to the same model in a fresh session, it rejects 67% (GPT-3.5), 87% (GPT-4) and 94% (LLaMA-2-70B-chat) of them [zhang2024snowball]."
- Other findings a reviewer would expect:
  - (i) Neither a higher sampling temperature nor beam search removes the snowballing (Abstract; Sec. 5, p.6).
  - (ii) Zero-shot chain of thought fixes most errors on these simple tasks for GPT-3.5 and GPT-4. It breaks down on composite questions that require solving several sub-problems (Sec. 4 and Sec. 5, p.6). The effect is tied to answer-first formats.

### obeso2025entities
- Source of record: https://arxiv.org/abs/2509.03531 (v2, 5 Feb 2026; v1, 26 Aug 2025). Venue check: OpenReview lists it as a rejected ICLR 2026 submission (https://openreview.net/forum?id=YxJEMTflww), and no other venue was found. Cite arXiv. Access: full text (https://arxiv.org/html/2509.03531v2 and the v2 PDF).
- Retraction: none found.
- Use 1 — intended claim: "token-level probes localize hallucinated entities (AUC ~0.90 vs 0.71 for semantic entropy) in long outputs"
  - Source passage: "AUC 0.90 vs 0.71 for Llama-3.3-70B" (Abstract, p.1). Table 1 (p.8) gives, for Llama-3.3-70B on the LongFact test set: LoRA probe 0.905, linear probe 0.867, semantic entropy 0.714, token entropy 0.712 and perplexity 0.706.
  - Scope:
    - Which probe: The 0.90 is the LoRA probe, with adapters trained into the model. A plain linear probe reaches 0.87 (Sec. 1, p.3).
    - Supervision: The probes are trained on about 25,000 generations. Their entity spans were labelled by Claude 4 Sonnet using web search (Sec. 3.1 and Sec. 4.1).
    - Evaluation: Scoring is per entity, using the maximum token score over the span. The semantic-entropy baseline is a long-form adaptation: 10 continuations are sampled from the prefix before each entity and clustered by GPT-4.1 (App. F.2).
    - Limits: Even the best probe recovers only about 70% of hallucinated entities at a 10% false-positive rate (Sec. 4.2; Sec. 6, p.13).
  - Verdict: NARROW → safe wording: "Supervised probes on hidden states flag hallucinated entities in long-form text much better than uncertainty baselines: on Llama-3.3-70B, AUC is 0.87 for a linear probe and 0.90 with LoRA, against about 0.71 for both semantic entropy and token entropy [obeso2025entities]."
- Other findings a reviewer would expect:
  - (i) Output-distribution uncertainty localises poorly in long-form text: token entropy and perplexity reach only 0.71-0.76 AUC on LongFact for both Llama models (Table 1). This qualifies any claim that entropy alone finds the hard tokens.
  - (ii) The authors use a span-max loss because the hallucination signal concentrates on specific high-information tokens (Sec. 3.2, p.6). This is consistent with sparse hardness.
  - (iii) The labels are noisy. The annotation pipeline caught 80.6% of injected errors with a 15.8% false-positive rate, and a human annotator agreed with 84% of 50 sampled labels (Sec. 3.1, p.5).
  - (iv) Framing errors at the entity level misses relational errors between real entities (Sec. 6, p.12). Even so, probes trained on entities also detect wrong answers on MATH (Table 1).
- Venue/bib notes: OpenReview gives the first author as "Oscar Balcells Obeso"; the bib follows the arXiv byline, "Oscar Obeso".

### thoria2026fail
- Source of record: https://arxiv.org/abs/2606.06635 (v1, 4 Jun 2026). No venue was found on OpenReview or Semantic Scholar. Access: full text (https://arxiv.org/html/2606.06635v1 and the v1 PDF).
- Retraction: none found.
- Use 1 — intended claim: "two failure modes — 'committed' failures lock in at an early commitment point; 'persistent' failures accumulate uncertainty across the trace (qualifies the sparse-hardness claim)"
  - Source passage: "locks onto an incorrect reasoning path early in its trace" (Abstract, p.1), which defines committed failure. The abstract describes persistent uncertainty as uncertainty that builds up throughout the trace, so that the full trace is needed to tell failures from successes.
  - Scope:
    - Unit: The modes are assigned to model-dataset configurations, not to individual traces.
    - Method: For each configuration, a logistic classifier predicts failure from ten log-probability features (entropy, top-2 margin and others) of one zero-shot chain-of-thought completion. The features are computed over the first T tokens, and PR-AUC is compared across T = 128, 256, 400, 512, 1024 and 2048 (Sec. 3-4).
    - Definitions: A configuration is "committed" if some early prefix predicts better than the full trace. Its commitment point is that best window, so it is a window size, not a token position (Sec. 7, p.9).
    - Data: 23 configurations of open and closed models (Qwen3.5, Llama-3.1, GPT-OSS, Gemma-4, GPT-4o, Gemini 2.5 Pro) on GSM8K, MATH-500, GPQA Diamond and LiveCodeBench. Of these, 14 are committed, most with confidence intervals that span zero, and 9 are persistent (Table 1 and Sec. 5, p.6).
    - Effect size: The pooled advantage of the best early window over the full trace is small, +0.013 PR-AUC (Table 2, p.8). Configurations with failure rates outside 15-60% and AUROC below 0.55 were excluded (Sec. 4.1, p.5).
  - Verdict: NARROW → safe wording: "Thoria et al. find two signatures across 23 model-benchmark settings. In 14, uncertainty features from an early prefix of a single trace predict failure better than the full trace (committed failure); in 9, predictive power keeps rising to the end (persistent uncertainty), so not every failure is decided early [thoria2026fail]."
- Other findings a reviewer would expect:
  - (i) Effect sizes are small, and many committed cases are weak, with intervals spanning zero.
  - (ii) Uncertainty from a single completion is much weaker than self-consistency agreement: PR-AUC about 0.42 against about 0.78 on GPQA. Combined with agreement, it adds a small but consistent lift (Sec. 5.4, p.8).
  - (iii) GPT-4o and Gemini 2.5 Pro expose only their top-20 log-probabilities, which weakens the mean-based features for those models (Sec. 5.2 and Sec. 7).

### simhi2025choke
- Source of record: https://aclanthology.org/2025.findings-emnlp.792/ (Findings of EMNLP 2025, pp. 14665-14688, Suzhou, DOI 10.18653/v1/2025.findings-emnlp.792). Access: full text (ACL Anthology PDF and arXiv v2 https://arxiv.org/html/2502.12964v2; the cited passages are identical).
- Retraction: none found.
- Use 1 — intended claim (counter): "models hallucinate with high certainty despite knowing the answer, so entropy cannot flag every error"
  - Source passage: "A non-negligible amount of hallucinations despite knowledge (16-43%) occur with high certainty" (Sec. 4.1, p.5).
  - Scope:
    - Task and "knowing": closed-book short-answer QA (TriviaQA, Natural Questions). A model counts as knowing an answer if it answers correctly with a few-shot prompt in five sampled decodings and one greedy one. Hallucinations are then elicited with natural rephrasings of the prompt (Sec. 3.1, p.3).
    - Certainty measures: first-answer-token probability, the margin between the top two tokens, or semantic entropy, each with the threshold that best separates right from wrong answers (Sec. 3.2-3.3, p.4).
    - Models: Llama-3.1-8B, Mistral-7B-v0.3 and Gemma-2-9B, in base and instruct versions, plus Gemma-2-27B.
    - Mitigation: Certainty-based mitigation methods that do well overall score much lower on these cases (Sec. 5.2, p.9).
  - Verdict: ACCURATE. For precision: "In closed-book QA, 16-43% of the hallucinations a model produces despite demonstrably knowing the answer carry high certainty under token-probability, probability-margin or semantic-entropy measures, so certainty-based detectors miss them [simhi2025choke]."
- Other findings a reviewer would expect:
  - (i) Prevalence: these certain hallucinations are only 0.3-2.1% of all hallucinations, because hallucinations despite knowledge are themselves only 2-8% of all hallucinations (Sec. 4.1, p.5). Do not suggest that most errors are confident ones.
  - (ii) They recur consistently across prompts, unlike randomly sampled hallucinations (Table 2), and instruction-tuned models are less calibrated (Sec. 4.2).
  - (iii) The authors do not explain the cause (Limitations, p.9). Their probe-based mitigation helps but does not solve the problem.

### yeom2026commit
- Source of record: https://arxiv.org/abs/2605.22007 (v1, 21 May 2026). Venue check: a poster at the non-archival Mechanistic Interpretability Workshop at ICML 2026 (https://openreview.net/forum?id=pTdBfvJLto); no archival venue was found. Cite arXiv. Access: full text (https://arxiv.org/html/2605.22007v1 and the v1 PDF).
- Retraction: none found.
- Use 1 — intended claim (counter): "a substantial share (16–47%) of hallucinations occur when the correct answer already has substantial probability"
  - Source passage: "16-47% of Instruct hallucinations occur with substantial probability mass already on the correct concept" (Abstract, p.1).
  - Scope:
    - Setting: short-form QA (TriviaQA and NQ-Open, 3,000 questions per model), greedy decoding, answers of 1-3 tokens.
    - Definition: "Substantial" means at least 0.2 total probability, at the answer step, on the first tokens of any alias of the gold answer (Sec. 4.2, p.6). The measure needs the gold aliases, so it is an analysis tool, not a detector (Sec. 5, p.9).
    - Composition: About 80% of these cases are multi-token divergences, where the first token already matches an alias and the continuation goes wrong. Only about 20% are cases where a wrong first token wins (Sec. 4.2 and Table 1, p.6).
    - Caveat: The authors note that for multi-token divergences, first-token mass may reflect a shared prefix rather than belief in the correct answer (Sec. 5).
  - Verdict: NARROW → safe wording: "In short-form QA with instruction-tuned Qwen and Llama models, 16-47% of wrong answers place at least 0.2 probability on the correct answer's first token(s) at the moment of answering; most of these begin correctly and diverge on later tokens [yeom2026commit]."
- Use 2 — intended claim: "rate rises with scale"
  - Source passage (paraphrase): Among Instruct models, the commitment-failure share rises monotonically with size, in both families (Sec. 4.2 and Table 1, p.6). For Qwen3.5 0.8B, 2B, 4B and 9B and Qwen2.5-72B it is 16, 17, 26, 32 and 41%. For Llama 1B, 3B, 8B and 70B it is 16, 28, 33 and 47%.
  - Scope: The trend is reported for Instruct models only. The authors attribute it to instruction tuning rather than size: when a wrong first token wins, its probability grows with size in Instruct models but stays flat near 0.3 in Base models (Sec. 1, p.3; Sec. 4.3).
  - Verdict: NARROW → safe wording: "... a share that grows with model size among instruction-tuned models, which the authors trace to instruction tuning sharpening the answer distribution [yeom2026commit]."
- Other findings a reviewer would expect:
  - (i) Support for sparse hardness: in one example, entropy is near zero at most steps and spikes at a few commitment steps (Fig. 1, p.2).
  - (ii) A limit on entropy as a localiser: in 500 long-form answers from Qwen3.5-9B Instruct, the highest-entropy step coincides with the commitment step in only 20% of cases (32% within one step). Entropy at that step barely separates right from wrong answers (Wilcoxon p=0.055) (Sec. 4.1, p.5).
  - (iii) Small and mid-sized models were run with 4-bit NF4 quantisation (Sec. 3).

### candussio2026demyst
- Source of record: https://arxiv.org/abs/2607.28707 (v3, 9 Sep 2026; v1, 30 Jul 2026). No venue was found. Access: full text (https://arxiv.org/html/2607.28707v3 and the v3 PDF).
- Retraction: none found.
- Use 1 — intended claim (counter): "sentence-level entropy pruning is no better than random"
  - Source passage: "entropy offers no advantage over random pruning in any evaluated setting" (Abstract, p.1). The phrase refers to keeping low-entropy or high-entropy sentences of a chain of thought.
  - Scope:
    - Task: chain-of-thought compression. Sentences of a finished reasoning trace are kept under a selection rule up to a token budget, and the model must then answer from the compressed trace (Sec. 3).
    - Models and benchmarks: six open reasoning models (gpt-oss-20b and 120b, Gemma-4 E4B and 26B-A4B, Qwen3-4B and 14B) on AIME 2024-26, a MATH-500 subset, ZebraLogic and GPQA-Diamond. Entropy is computed from the top-20 log-probabilities, renormalised (Sec. 4, p.4).
    - Key numbers: For gpt-oss-20b on AIME25, at moderate to high compression, random selection keeps 78-90% of full-trace accuracy, against 40-79% for low-entropy and 60-89% for high-entropy selection (Sec. 5, p.4). No entropy selector significantly beats random in any setting (Table 1; Sec. 6, p.6).
  - Verdict: ACCURATE, provided it is framed as chain-of-thought compression (which sentences can be dropped), not as error detection.
- Use 2 — intended claim (counter): "task information is distributed across the chain"
  - Source passage (paraphrase): From activation-patching experiments, the abstract concludes that task information is not concentrated in a small set of CoT tokens identifiable by heuristics but is spread across the whole chain (p.1).
  - Scope: The same experiments show that keeping only the number tokens, with their original activations patched in, recovers near-full accuracy on math from 10-20% of the tokens (Sec. 5-6). Because the patched activations carry context from the whole trace, the result concerns where information is stored. It rules out entropy as the way to find that information; it does not rule out sparse decision points.
  - Verdict: NARROW → safe wording: "... and conclude that the task-relevant content of a reasoning trace is not concentrated in a small set of tokens that a heuristic such as entropy can pick out [candussio2026demyst]."
- Other findings a reviewer would expect:
  - (i) At the token level, keeping low-entropy tokens helps only on math, and only because numeric tokens have low entropy. Without them, low-entropy selection falls below random (Sec. 5, p.5).
  - (ii) The non-AIME evaluation sets are small (50-100 questions), and traces were capped at 16k tokens (Limitations).
  - (iii) The paper tests entropy as a relevance signal for compression. It does not test whether errors originate at high-entropy tokens, so it does not directly contradict entropy-as-risk evidence such as AdaDec or EGB.

### zhang2026activeuq
- Source of record: https://aclanthology.org/2026.findings-acl.2064/ (Findings of ACL 2026, pp. 41525-41544, San Diego, DOI 10.18653/v1/2026.findings-acl.2064). Venue correction: the arXiv comment says "accepted by ACL 2026", but the paper appears in Findings of ACL 2026, not the main conference proceedings. Access: full text (ACL Anthology PDF and arXiv v2 https://arxiv.org/html/2601.15690v2).
- Retraction: none found.
- Use 1 — intended claim: "prior review framing uncertainty as a control signal for compute"
  - Source passage: "from a passive diagnostic metric to an active control signal" (Abstract, p.1).
  - Scope: A survey with no experiments of its own (Limitations, p.9). It covers three areas. In reasoning (Sec. 3) it treats choosing among paths, steering within a path and allocating compute; Sec. 3.3 (p.5) treats uncertainty as an economic signal for when to think harder. In agents (Sec. 4) it covers abstention, tool use and uncertainty propagation. Sec. 5 covers RL and reward modelling.
  - Verdict: ACCURATE. Compute allocation is one of its themes, so say "control signal, e.g., for allocating test-time compute".
- Use 2 — novelty check: does it connect token uncertainty to sequence-level reliability?
  - Finding:
    - There is no formal link.
    - It states only qualitatively that early mistakes can derail an entire chain of thought (Sec. 2, p.2) and that small errors accumulate across multi-step agent workflows (Sec. 4.3, p.6).
    - It surveys step-level propagation methods for agents (SAUP, UProp), trajectory-level aggregation (MUR, Sec. 3.3), and the finding that RL gains come mainly from high-entropy minority tokens (Sec. 5.3, p.8).
    - It has no model of how per-token hardness composes into sequence-level success, or of how reliability scales with output length.
  - Verdict: NARROW, for the novelty claim → safe wording: "Zhang et al. survey uncertainty as an active control signal in reasoning, agents and RL and note that errors compound across steps, but they do not model how token-level uncertainty determines sequence-level reliability [zhang2026activeuq]." Do not claim that no prior work aggregates uncertainty across steps: SAUP and UProp do so for agents.
- Other findings a reviewer would expect:
  - (i) It is a Findings paper, not main-conference ACL.
  - (ii) It cites Wang et al. (2025), "Beyond the 80/20 rule: high-entropy minority tokens drive effective reinforcement learning", which reviewers will also expect under pillar 2. Check that it is in another ledger part.
