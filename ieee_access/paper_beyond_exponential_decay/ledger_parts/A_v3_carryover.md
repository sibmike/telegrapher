# Citation ledger, part A: v3 carry-over references (14 keys)

Verified 2026-10-03 against `arxiv/beyond exponential decay/body.tex` (line numbers below refer to that file) and `references.bib`.

**Method.** For every key, I read the full text, preferring the venue version (NeurIPS / ICLR / TACL / ACL Anthology / TMLR-matching arXiv v2), and checked every `body.tex` sentence that cites it. Metadata comes from the venue's own BibTeX or metadata where it was reachable. I cross-checked against Crossref, and every DOI was checked with `filter=updates:<DOI>` for retraction or correction notices. OpenReview and dblp.org were behind bot checks or refused connections from this machine. I did not bypass them; I used iclr.cc, jmlr.org/tmlr and proceedings sites instead.

**Quote policy.** Copyright policy limits verbatim fragments to under 15 words, so each claim is anchored by a short fragment plus an exact location (section, page, table or figure). The surrounding content is paraphrased. A reviewer can check the full passage from the location given.

**Verdict counts (52 uses):** 18 ACCURATE, 32 NARROW, 2 DROP. Most NARROWs are scope or attribution fixes. The substantive ones are flagged **[substantive]**.

| key | uses | ACC / NAR / DROP | bib changed? |
|---|---|---|---|
| dziri2023faith | 1 | 0/1/0 | yes (pages, DOI, author order) |
| lecun2023why | 2 | 2/0/0 | yes (title, date, url) |
| fang2024what | 8 | 3/5/0 | yes (pages, url) |
| li2025unraveling | 5 | 4/1/0 | minor (title case, DOI) |
| wang2023self | 6 | 3/3/0 | minor (author initial, url) |
| bengio2015scheduled | 1 | 0/1/0 | yes (pages) |
| liu2023lost | 1 | 1/0/0 | minor (DOI) |
| liu2024retrieval | 6 | 2/4/0 | **yes: now NeurIPS 2025** |
| pang2024anchor | 5 | 1/4/0 | minor (DOI) |
| robinson2025token | 3 | 1/2/0 | **yes: now NeurIPS 2025** |
| viswanathan2024geometry | 2 | 0/2/0 | minor (ISSN, url) |
| gao2024insights | 3 | 0/3/0 | minor (booktitle, DOI) |
| yao2023tree | 3 | 1/2/0 | yes (pages, DOI) |
| costello2025think | 6 | 0/4/2 | note added (IEEE ICLAD version exists) |

**Cross-cutting findings**
1. **RetrievalAttention version drift.** The 89% / top-1000-of-100,000 / 4.9x figures exist only in arXiv v1–v3. The NeurIPS 2025 camera-ready (the source of record) replaces them with a different analysis and different speedups (7.93x / 2.80x). See liu2024retrieval.
2. **LongPPL window.** Fang et al. never state the short-context window K behind the "<10% of tokens" figure. Section 2.2 introduces K with "e.g., 64", and K = 4096 is stated only for the later LongPPL/LongCE experiments. Five `body.tex` sentences attach "4,096 tokens" to the <10% figure.
3. **Predicted versus measured.** Robinson et al. derive output instability from a theorem and leave the experiment to future work. Viswanathan et al. measure a cross-prompt correlation, not a within-sequence dynamic. `body.tex` states both as observed behaviour.
4. **A cited paper cuts against our dichotomy.** ToT's own Table 2 shows majority voting (CoT-SC, k=100) lifting GPT-4 on Game of 24 only from 4.0% to 9.0%. That is a reasoning task, where our "ensembles help on reasoning, not on knowledge" story predicts a large gain. Expect a reviewer to raise it. The systematic-versus-idiosyncratic claim itself (l. 35, l. 112, l. 128) is not stated or tested in Wang et al. or Yao et al. It is our conjecture, and should be marked as such (l. 138 already concedes it is post hoc).

---

### dziri2023faith
- Source of record: NeurIPS 2023 proceedings, https://proceedings.neurips.cc/paper_files/paper/2023/hash/deb3c28192f979302c157cb653c15e90-Abstract-Conference.html (DOI 10.52202/075280-3081). Access: full text (venue PDF https://proceedings.neurips.cc/paper_files/paper/2023/file/deb3c28192f979302c157cb653c15e90-Paper-Conference.pdf; also arXiv v3).
- Retraction: none found. The Crossref record exists and has 0 update notices.
- Use 1, our sentence (l. 8): "If each token has even a $1\%$ error rate then a $100$-token chain is correct only $(0.99)^{100} \approx 37\%$ of the time, and longer chains decay exponentially toward zero \citep{lecun2023why,dziri2023faith}."
  - Source passage: Prop. 4.1 (informal) considers n independent applications of a sub-function g, each wrong with probability epsilon and with independent errors, plus a collision-rate bound c_n. It gives P(f_n ≠ f̂_n) > 1 − c_n − (1−epsilon)^n (1−c_n). §4 "Error Propagations: The Theoretical Limits", PDF p. 8. §5 then generalizes: "these proofs apply to autoregressive LMs in general" (p. 9).
  - Scope: theoretical. The error unit is a reasoning step (one function application) in compositional tasks: multiplication, Einstein puzzle, dynamic programming. The success probability tends to at most c (the collision term), not to zero. Prop. 4.2 adds an explicit recovery probability c.
  - Verdict: NARROW. The 1% / 100 / 37% arithmetic is ours, which is fine under "the argument goes". Dziri et al. do present their result as general. But their unit is a step, not a token, and their bounds contain recovery/collision terms. Pairing them with LeCun's per-token form blurs that. Suggested wording: "…and longer chains decay exponentially toward zero \citep{lecun2023why}; \citet{dziri2023faith} prove the step-level analogue for compositional tasks, where independent per-step errors drive the probability of a correct final answer down exponentially in the number of steps."
- Bib changes vs current:
  - Added pages 70293–70332, DOI, publisher and url.
  - **Author order** now follows the printed title page: Welleck moves from 7th to 12th. The NeurIPS venue PDF and arXiv v3 agree on this order. The NeurIPS site metadata, its BibTeX export and Crossref list Welleck 7th, as the old bib did. So the venue's metadata disagrees with its own PDF. IEEE style prints "N. Dziri et al.", so the difference is invisible in print. Revert this one change if you prefer the metadata order.

### lecun2023why
- Source of record: LinkedIn post, https://www.linkedin.com/posts/yann-lecun_i-have-claimed-that-auto-regressive-llms-activity-7045908925660950528-hJGk. Access: full text of the post, read from the page's metadata on 2026-10-03. The post was published 2023-03-27 00:06 UTC; the LD-JSON `datePublished` and the activity-ID timestamp agree. The post describes itself as the opening statement for an NYU debate held on Friday 24 March.
- Retraction: n/a (social-media post, still live on 2026-10-03).
- Use 1, our sentence (l. 8): same sentence as dziri2023faith Use 1.
  - Source passage: e is defined as "the probability that any generated token exits the tree of 'correct' answers". The post then states "the probability that an answer of length n is correct is (1-e)^n".
  - Scope: an informal argument with no numbers. Independence and no-recovery are implicit: there is a constant per-token exit probability and an absorbing "wrong" state.
  - Verdict: ACCURATE. The 1% / 37% illustration is ours and is framed as "the argument goes".
- Use 2, our sentence (l. 26): "\citet{lecun2023why} extended the worry to autoregressive LLMs in the now-familiar form---if each token has error probability $e$, sequence-level correctness decays as $(1-e)^n$."
  - Source passage: as above. The post adds "Errors accumulate." and says training can make e smaller but cannot eliminate the problem.
  - Scope: same as Use 1.
  - Verdict: ACCURATE. Two minor points:
    - "Extended" is our narrative link from exposure bias; LeCun does not mention it. "Restated the worry for" is safer if a reviewer pushes.
    - LeCun's e is a probability of exiting the set of correct continuations (absorbing failure). That is slightly stronger than a generic "error probability" and consistent with our no-recovery framing.
- Bib changes vs current:
  - Title is now the post's opening sentence instead of the bracketed descriptive title.
  - `howpublished = {LinkedIn post}` and `month = mar`.
  - The URL moved into the `url` field; a note gives the exact posting date (UTC) and the access date.

### fang2024what
- Source of record: ICLR 2025 proceedings, https://proceedings.iclr.cc/paper_files/paper/2025/hash/ebd6641c32ed633c2a3addc689d39896-Abstract-Conference.html. Access: full text (camera-ready PDF https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf). arXiv v5 is identical on every passage below, and v1–v3 were also checked for the K question.
- Retraction: none found (no Crossref DOI for ICLR; arXiv v5 active).
- Shared scope:
  - Evaluator models: Qwen2-72B-Instruct is the key-token discriminator. Llama-3.1-8B and Mistral Large 2 serve as alternatives.
  - Data: 50 GovReport documents of up to 32k tokens. LongPPL is correlated across 9 long-context models (Fig. 1b, Table 1).
  - The LongEval answer-token analysis uses Yi-6B-200K and CLEX-7B-64K.
- **K issue [substantive]:**
  - §2.2 (p. 4) defines the short context with "where K is a short length, e.g., 64".
  - K = 4096 is stated only for the LongPPL setup: "α = 2, β = −2, K = 4096" (§4.1, p. 7) and for LongCE (§4.2).
  - The "<10%" statement rests on Fig. 4(a), the LSD distribution on GovReport (§2.2, p. 5). Neither the K nor the model behind that figure is stated in any version (v1–v5, camera-ready).
- Use 1, our sentence (l. 10): "fewer than $10\%$ of tokens in natural text gain meaningfully from context beyond the preceding four thousand tokens \citep{fang2024what}."
  - Source passage: "only less than 10% tokens are highly influenced by long context (with LSD> 2)" (§2.2, p. 5, Fig. 4(a)).
  - Scope: one corpus (GovReport); window not stated.
  - Verdict: NARROW. "Natural text" generalizes from one corpus, and "four thousand tokens" attaches a window the paper does not state for this figure. Suggested: "fewer than $10\%$ of tokens in a natural-text corpus (GovReport) gain substantially (LSD $>2$, i.e. more than 2 nats) from the full context over a truncated short context \citep{fang2024what}."
- Use 2, our sentence (l. 12): "\citet{fang2024what} on which tokens actually need long context".
  - Source passage: the paper's thesis (abstract; §2.1 title "Not all tokens matter for long-context performance").
  - Verdict: ACCURATE.
- Use 3, our sentence (l. 29): "…whose long-short difference (LSD) metric finds fewer than $10\%$ of tokens in a natural corpus (GovReport) scoring LSD$>2$---that is, predicted materially better with the full context than with only the preceding $4{,}096$ tokens."
  - Source passage: as in Use 1, together with the K statements above.
  - Verdict: NARROW. Suggested: "…scoring LSD$>2$---that is, predicted materially better with the full context than with a truncated short context (their LongPPL experiments truncate to the preceding $4{,}096$ tokens; the window behind this particular figure is not stated)."
- Use 4, our sentence (l. 49): "The one direct estimate of $k/n$ for natural text is the LongPPL measurement of \citet{fang2024what}: fewer than $10\%$ of GovReport tokens are predicted materially better with the full context than with only the preceding $4{,}096$ tokens."
  - Verdict: NARROW, for three reasons:
    1. The <10% comes from the §2.2 LSD-distribution analysis, not from the LongPPL measurement (§4.1).
    2. The window K is not stated for that figure.
    3. "The one direct estimate" is a claim about the literature that we cannot source.
  - Suggested: "A direct estimate of $k/n$ for natural text comes from the long-short-difference analysis of \citet{fang2024what}: fewer than $10\%$ of GovReport tokens gain more than 2 nats of log-probability from the full context relative to a truncated short context."
- Use 5, our sentences (l. 98): "A token counts as key if the full context improves its log-likelihood by more than $2$ nats over a $4{,}096$-token window and the token remains predictable under the full context; on the GovReport corpus, fewer than $10\%$ of tokens qualify. Perplexity restricted to those tokens (LongPPL) correlates with LongBench performance at Pearson $-0.96$ …, where ordinary perplexity over all tokens correlates at $-0.18$; and on a retrieval task where the answer tokens are known in advance, perplexity on the non-answer tokens carries almost no signal at all."
  - Source passages:
    - Key-token rule: Eq. (4), LSD > α and LCL > β, with α = 2, β = −2, K = 4096 (§4.1, p. 7).
    - Units are nats: Eq. (7) sets exp(LSD) equal to the probability ratio P(x|l)/P(x|s) (p. 6).
    - Correlations: Table 1 (p. 8) gives LongBench PPL −0.18 and LongPPL −0.96. LongEval and RULER give −0.90 / −0.90, with PPL at +0.24 / +0.27.
    - Non-answer tokens: the paper says their perplexity "shows almost no correlation with LongEval accuracy" (§2.1, p. 4).
  - Verdict: NARROW, first sentence only. The key-token definition matches the LongPPL rule at K = 4096, but "fewer than 10% qualify" is the Fig. 4(a) LSD>2 count, whose K is not stated. The rest is ACCURATE. Suggested first sentence: "A token counts as key if the full context improves its log-likelihood by more than $2$ nats over a truncated window ($4{,}096$ tokens in their LongPPL experiments) and the token remains predictable under the full context; on GovReport, fewer than $10\%$ of tokens clear even the first criterion."
- Use 6, our sentence (l. 131): "…LongPPL restricts perplexity to key tokens and lifts the correlation with downstream performance to $r = -0.96$ from a near-zero baseline."
  - Source passage: Fig. 1 caption (p. 2): "While PPL shows no correlation w.r.t. Longbench score". Table 1 gives −0.18.
  - Verdict: ACCURATE. Optionally write "from $-0.18$".
- Use 7, our sentence (l. 142): "The long-context estimate is under $10\%$ against a $4{,}096$-token window \citep{fang2024what}".
  - Verdict: NARROW. Suggested: "The long-context estimate is under $10\%$ \citep{fang2024what} (key tokens defined against a truncated window---$4{,}096$ tokens in their LongPPL setup; the window behind the $<10\%$ figure itself is not reported)." The proposed $k(n)$ experiment, which fixes K explicitly, is the right remedy.
- Use 8 (l. 196, Table): "LongPPL \citep{fang2024what}" listed as a key-token-restricted metric.
  - Verdict: ACCURATE.
- Uncited echoes: the abstract (l. 2) says "the one direct measurement of long-range dependence" and the conclusion (l. 147) says "under a tenth of tokens". Both have the same single-corpus scope, and "the one direct measurement" is our wording.
- Bib changes vs current: added pages 94541–94563 and the proceedings URL (from the ICLR 2025 BibTeX). Authors, title and year were verified and are unchanged.

### li2025unraveling
- Source of record: arXiv, https://arxiv.org/abs/2502.13577 (v1 only). No venue found: Crossref has no match, and Semantic Scholar and DBLP list CoRR only. Access: full text (https://arxiv.org/pdf/2502.13577v1).
- Retraction: none found.
- Shared scope:
  - Method: a dictionary-learning MoE (7 experts, sparsity 8–32) applied to last-hidden-layer embeddings.
  - Models: BERT, RoBERTa, Llama-3.2-1B and DeepSeek-R1-Distill-Qwen-1.5B. Results are shown for the last three.
  - Data: six sources with 500 samples each.
  - The number of strata is fixed at 5 by design: "we also set the number of strata as 5" (§5, p. 7).
  - Intrinsic dimension (ID) is the number of PCA components needed for 75% of the variance (Table 1, p. 8).
  - Limitations (§7, p. 8) concede the mathematics of the structure has not yet been investigated.
- Use 1, our sentence (l. 12): "\citet{li2025unraveling} on the stratified-manifold organization of embeddings".
  - Source passage: the abstract's hypothesis and its claim to validate it.
  - Verdict: ACCURATE.
- Use 2, our sentence (l. 32): "…probed LLM embedding spaces with sparse mixture-of-experts and found a stratified-manifold structure: a union of low-dimensional submanifolds aligned with semantic domain."
  - Source passage: the abstract says the model "learns specialized sub-manifolds for an ensemble of input data sources". §5.2 (p. 7) reports that embeddings from similar datasets cluster and share a stratum.
  - Verdict: ACCURATE as a report of the authors' claim. Caveat: the strata count is imposed and the evidence comes from models of at most 1.5B parameters.
- Use 3, our sentence (l. 71): "The embedding space's stratified structure \citep{li2025unraveling} introduces correlation, and we can read the dynamics off it directly."
  - Source passage: none. The paper analyses static embeddings of whole inputs. It says nothing about errors, correlation or generation trajectories.
  - Verdict: NARROW, because the claim is ours. Suggested: "If the embedding space is stratified, as \citet{li2025unraveling} report for static input embeddings, we expect that structure to introduce correlation between errors; we model the dynamics as follows."
- Use 4, our sentence (l. 104): "…sparse-MoE probe of frozen LLM embeddings finds a union of low-dimensional manifolds aligned with data source (movie and product reviews, tweets, news), with measurably different intrinsic dimension across regions."
  - Source passage: the sources are IMDB, Rotten Tomatoes, Amazon Polarity, SST-2, TweetEval and AG News (§5, pp. 4/7). The paper reports "varying intrinsic dimensions" across strata (§5.2, p. 8), with per-stratum IDs of 2–16 in Table 1.
  - Verdict: ACCURATE. Optionally add "(models up to 1.5B parameters)".
- Use 5, our sentence (l. 138), the manifold account "leans on" this paper, which is recent and needs larger-scale replication.
  - Verdict: ACCURATE.
- Bib changes vs current: title recased to the arXiv title, and the arXiv DOI 10.48550/arXiv.2502.13577 added (it resolves). The entry remains an unrefereed preprint.

### wang2023self
- Source of record: ICLR 2023 poster, https://iclr.cc/virtual/2023/poster/11718, linking to OpenReview https://openreview.net/forum?id=1PL1NIMMrw (OpenReview showed a bot-check page, which I did not bypass). Access: full text of the camera-ready, which is arXiv v4 (https://arxiv.org/abs/2203.11171v4, marked "Published as a conference paper at ICLR 2023").
- Retraction: none found.
- Use 1, our sentence (l. 12): "\citet{wang2023self} on the convergence of correct reasoning paths under sampling".
  - Source passage: "correct reasoning processes, even if they are diverse, tend to have greater agreement" (§1, p. 2).
  - Verdict: ACCURATE. Note that the convergence is in the final answer; the paths themselves are diverse.
- Use 2, our sentence (l. 35): "…sample multiple reasoning paths, take the majority answer. The gain was $+17.9$ points on GSM8K, with no retraining."
  - Source passages: Table 2 (p. 5) shows GSM8K rising 56.5→74.4 with PaLM-540B and 60.1→78.0 with code-davinci-002, both +17.9. The method "avoids any additional training, auxiliary models or fine-tuning" (§2, p. 2).
  - Verdict: ACCURATE.
  - **Adjacent uncited claim [substantive]:** the same paragraph says reasoning errors are idiosyncratic, knowledge-gap errors are systematic, and that this is why ensembles help in one case and not the other. Neither Wang et al. nor Yao et al. state or test this. The closest result in Wang et al. is that answer consistency "is highly correlated with accuracy" (§3.5, Fig. 5, p. 8). Mark it as our conjecture or source it elsewhere. ToT's Table 2 is a counterexample a reviewer could raise (see yao2023tree).
- Use 3, our sentence (l. 87): "Wang et al.'s self-consistency results \citep{wang2023self} sit closer to the $\rho = 0$ regime than to $\rho = 1$, which is why … lift GSM8K accuracy by $17.9$ points: the gain is structural, not a property of the sampling temperature."
  - Source passages: the +17.9 figure is in Table 2. Robustness: "robust to sampling strategies and parameters" (§3.5, p. 8; Fig. 4 left varies temperature, top-k and nucleus p on PaLM-540B).
  - Verdict: NARROW. Wang et al. never estimate error correlation, so placing them near ρ = 0 is our inference and should be marked as such. Suggested: "On our reading, Wang et al.'s results \citep{wang2023self} sit closer to the $\rho = 0$ regime than to $\rho = 1$ (they do not measure error correlation): a method that adds no parameters and no training data lifts GSM8K accuracy by $17.9$ points, and the gain is robust to temperature, top-$k$ and nucleus settings."
- Use 4, our sentences (l. 112): "\citet{wang2023self} showed that self-consistency lifts GSM8K by $17.9$ points and SVAMP by $11.0$, with no model change. The mechanism, on our reading, is that correct paths concentrate near a low-dimensional attractor while incorrect ones disperse---so majority voting picks out the attractor's mode."
  - Source passages: the abstract gives GSM8K +17.9% and SVAMP +11.0%. In Table 2, the +11.0 on SVAMP is code-davinci-002 (PaLM-540B gets +7.6); the +17.9 on GSM8K holds for both models.
  - Verdict: NARROW.
    - The numbers are ACCURATE; both are code-davinci-002 figures.
    - The mechanism sentence is flagged as our reading, but it conflicts with the paper's premise that correct paths are diverse; the agreement Wang et al. rely on is in answer space.
  - Suggested: "…and SVAMP by $11.0$ (GPT-3 code-davinci-002), with no model change. The mechanism, on our reading, is that correct paths---diverse as they are---converge on one final answer while incorrect ones scatter across many, so majority voting picks out the mode."
- Use 5, our sentence (l. 128): self-consistency exploits the convergence-of-correct-paths structure.
  - Verdict: ACCURATE for self-consistency, since answer agreement is its premise. The ToT part of this sentence is handled under yao2023tree.
- Use 6 (l. 194, Table): row "Error reduction", two-rate cell "Branching at uncertain junctions", exemplar "Self-consistency \citep{wang2023self}".
  - Verdict: NARROW. Self-consistency samples complete paths independently and votes on the final answers; it does not branch at junctions. Suggested two-rate cell: "Aggregation over diverse sampled paths (errors idiosyncratic at key decisions)".
- Bib changes vs current:
  - "Chi, Ed" becomes "Chi, Ed H.", matching the camera-ready title page and the ICLR site.
  - OpenReview URL added.
  - "Le, Quoc" is kept as printed on the paper; the ICLR site lists "Quoc V Le".

### bengio2015scheduled
- Source of record: NIPS 2015 proceedings, https://proceedings.neurips.cc/paper_files/paper/2015/hash/e995f98d56967d946471af29d7bf99f1-Abstract.html. Access: full text (venue PDF …-Paper.pdf).
- Retraction: none found (no DOI; the proceedings page is live).
- Use 1, our sentence (l. 26): "The exposure-bias problem is old. \citet{bengio2015scheduled} formalized it: models trained with teacher forcing must, at inference time, condition on their own potentially noisy output, so small errors can compound through state updates."
  - Source passages:
    - Abstract (p. 1): the train/inference discrepancy can yield "errors that can accumulate quickly along the generated sequence".
    - §2.3 (p. 3): after a wrong decision the model can land in an unfamiliar part of state space and "can easily lead to cumulative bad decisions".
  - Scope: RNN sequence prediction, with results on image captioning, constituency parsing and speech recognition. The proposed remedy is a curriculum (scheduled sampling).
  - Verdict: NARROW. The mechanism is described correctly, but three wording problems remain:
    - The paper describes the mechanism; it does not formalize it.
    - The term "exposure bias" does not appear in the paper; it was coined later.
    - Neither does "teacher forcing", though using it as a modern gloss is fine.
  - Suggested: "The exposure-bias problem is old. \citet{bengio2015scheduled} identified its mechanism: a model trained to predict each token from the true previous token must, at inference time, condition on its own generated tokens, so errors can accumulate along the generated sequence."
- Bib changes vs current: added pages 1171–1179 (from the official NeurIPS metadata JSON; the site's BibTeX leaves pages empty), publisher and url. Title recased to match the proceedings.

### liu2023lost
- Source of record: TACL vol. 12 (2024), https://aclanthology.org/2024.tacl-1.9/ (DOI 10.1162/tacl_a_00638). Access: full text (https://aclanthology.org/2024.tacl-1.9.pdf).
- Retraction: none found (Crossref: 0 update notices).
- Use 1, our sentence (l. 29): "\citet{liu2023lost} documented the lost-in-the-middle effect---models perform best when the relevant material sits near the beginning or end of the prompt and worst when it sits in the middle."
  - Source passages: the abstract (p. 157) says performance "is often highest when relevant information occurs at the beginning or end". §1 (p. 158) describes a "distinctive U-shaped performance curve".
  - Scope: multi-document QA and synthetic key-value retrieval, with greedy decoding. Models include GPT-3.5-Turbo, Claude-1.3, MPT-30B-Instruct, LongChat-13B and Flan-T5/UL2. Caveat: some models, such as Claude-1.3, are perfect on key-value retrieval (figure caption, p. 163).
  - Verdict: ACCURATE. Optionally add "often", as the abstract does.
- Bib changes vs current: added DOI and publisher (MIT Press). All other fields match the ACL Anthology BibTeX.

### liu2024retrieval
- Source of record: NeurIPS 2025 (Advances in NIPS 38), https://proceedings.neurips.cc/paper_files/paper/2025/hash/4e36d4049fb0fea195a8267c8dcd0824-Abstract-Conference.html (DOI 10.52202/085713-1816). Access: full text (camera-ready PDF …/4e36d4049fb0fea195a8267c8dcd0824-Paper-Conference.pdf, and arXiv v3 https://arxiv.org/abs/2409.10516v3).
- Retraction: none found (Crossref: 0 update notices).
- **Version drift [substantive].** `body.tex` uses figures that appear only in arXiv v1–v3:
  - an oracle top-1000 out of 100,000 tokens recovering 89% on average, and over 90% for most heads;
  - a 4.9x speedup over exact KNN;
  - 0.188 s per token.

  The NeurIPS camera-ready drops the recovery-ratio analysis. Instead it measures the error (MSE) of attention restricted to the top-k tokens: "The MSE drops sharply when k is even smaller than 200 tokens" (§2.2, p. 3, 128K context). It reports "7.93× and 2.80× decoding latency reduction" against exact KNN and IVF (§1, p. 3), and 0.107 s per token (abstract).

  Recommended: cite the NeurIPS paper and switch to the camera-ready numbers, using the wording below. The alternative is to cite arXiv v3 explicitly for the 89% and 4.9x figures, which exposes the discrepancy to any reviewer who opens the published version.
- Use 1, our sentence (l. 10): "selecting just the top $\sim 1\%$ of tokens by attention mass recovers $\sim 89\%$ of full-attention scores on average across heads and layers in Llama-3-8B \citep{liu2024retrieval}".
  - Source passage (arXiv v3 only): §2.3 (p. 3) reports "an average of 89% across all heads and layers". The Fig. 2 caption (p. 4) says this was measured in a "KV retrieval test of 100,000 tokens", over 20 decoding steps, with an oracle top-k chosen per query. Static selection drops the figure to 71%.
  - Scope: a synthetic key-value retrieval prompt, oracle selection, Llama-3-8B.
  - Verdict: NARROW [substantive]. The number is absent from the source of record, and it comes from a synthetic retrieval prompt. Suggested (camera-ready): "attention output restricted to the top-$k$ critical tokens approaches full attention once $k$ reaches a couple of hundred out of a $128$K-token context \citep{liu2024retrieval}". If you keep 89%, add "on a 100K-token key-value retrieval prompt (preprint version)".
- Use 2, our sentence (l. 29): "…showed that scanning only $1{,}000$ critical tokens out of $100{,}000$ in Llama-3-8B recovers $\sim 89\%$ … (over $90\%$ for most heads), and used the observation to enable $128$K-token contexts on consumer GPUs."
  - Source passage: as in Use 1. For the second clause, the camera-ready abstract says the method lets 8B models "handle 128K tokens on a single NVIDIA RTX4090 (24GB)".
  - Verdict: NARROW. Same drift. "Scanning" is also the wrong word: the 1,000 tokens are oracle-selected by full attention, and "scanning" describes the 1–3% of keys the index traverses. The second clause is ACCURATE. Suggested: "\citet{liu2024retrieval} show that in a $128$K-token context the attention output computed from only the top-$k$ critical tokens approaches full attention once $k$ is in the low hundreds, and exploit this to serve $128$K-token contexts for 8B-parameter models on a single 24\,GB consumer GPU."
- Use 3, our sentence (l. 100): "…reach $128$K-token effective context on consumer GPUs by computing attention only over the top $\sim 1{,}000$ tokens by attention mass, recovering $89\%$ of full-attention scores on average and over $90\%$ for most heads."
  - Source passage: by default the system retrieves "the top-100 nearest key vectors and use 640 tokens" (128 initial plus 512 local-window tokens) as a static pattern (camera-ready §4.1, p. 7; same in the arXiv Table 2 caption).
  - Verdict: NARROW [substantive]. The mechanism is misdescribed: the system attends to 100 retrieved keys plus 640 static tokens, not to the top ~1,000 by attention mass. The 89% belongs to the separate oracle analysis, which the camera-ready drops. Suggested: "\citet{liu2024retrieval} serve $128$K-token contexts for 8B models on a single consumer GPU by attending, at each decoding step, only to the $100$ keys retrieved by an attention-aware nearest-neighbour index plus $640$ fixed initial and recent tokens, with accuracy close to full attention."
- Use 4, our sentence (l. 122): "\citet{liu2024retrieval}'s top-$k$ attention are the existing demonstrations".
  - Verdict: ACCURATE (dynamic sparse attention over retrieved top-k keys).
- Use 5, heading and sentences (l. 176–177): heading "Attention concentration in production models", then "In Llama-3-8B, retrieving just $1{,}000$ critical tokens out of $100{,}000$ recovers about $89\%$ … RetrievalAttention exploits this directly: at generation time, only the top critical tokens enter attention, with the rest treated as a nearest-neighbor lookup over $1$--$3\%$ of key vectors. The result is $128$K effective context on a single RTX 4090 with a $4.9\times$ decoding-latency reduction over exact KNN."
  - Source passages:
    - Camera-ready §1 (p. 3): the index needs "traversal of only a small subset of key vectors (1–3%)" to identify the critical tokens.
    - Speedups: "7.93× and 2.80×" (p. 3).
    - §2.2 (p. 4): the top-100 critical tokens across three decoding steps share "only 30% overlap".
  - Verdict: NARROW [substantive], for three reasons:
    1. The 89% and 4.9x figures are drift (see above).
    2. The 1–3% is the share of keys the index traverses in order to find the critical tokens. "The rest treated as a nearest-neighbor lookup" inverts this.
    3. "Production models" overstates. The models are open long-context variants: Llama-3-8B-Instruct-262k and Yi-6B/9B-200K.
  - Suggested: "In a $128$K-token context, attention restricted to the top-$k$ critical tokens approaches full attention once $k$ is below about $200$, and the critical set shifts from step to step (only $30\%$ overlap of the top-$100$ across three decoding steps). RetrievalAttention exploits this directly: for each query, an attention-aware nearest-neighbour index that traverses only $1$--$3\%$ of the key vectors retrieves the top-$100$ critical tokens, which are attended together with $640$ fixed initial and recent tokens. The result is $128$K-token inference for 8B models on a single RTX 4090, with a $7.93\times$ decoding-latency reduction over exact-KNN retrieval." Heading: "Attention concentration in open long-context models".
- Use 6 (l. 190, Table): "RetrievalAttention \citep{liu2024retrieval}" as an example of sparse retrieval focused on key tokens.
  - Verdict: ACCURATE.
- Uncited echo: the abstract's "$128$K-token retrieval on consumer GPUs" is ACCURATE.
- Bib changes vs current:
  - Entry type changed from `@article` (arXiv) to `@inproceedings`: NeurIPS 2025, vol. 38, pp. 54358–54385, DOI 10.52202/085713-1816.
  - Year changed from 2024 to 2025; the key is unchanged.
  - Pages come from the neurips.cc BibTeX. Crossref lists pp. 60539–60566 for the same DOI (Curran's print pagination). The length is the same, so this is a different pagination scheme rather than an error.

### pang2024anchor
- Source of record: Findings of ACL 2024, https://aclanthology.org/2024.findings-acl.295/ (DOI 10.18653/v1/2024.findings-acl.295). Access: full text (https://aclanthology.org/2024.findings-acl.295.pdf).
- Retraction: none found (Crossref: 0 update notices).
- **Shared scope [substantive]:**
  - The base model is Llama2-7B, continually pre-trained on about 1B tokens of RedPajama-Data-1T-Sample with anchor-based attention masks (§1, p. 4959; §4, p. 4962). This is not a training-free method.
  - Anchors are punctuation marks (AnLLM-EP) or an appended <AC> token per sequence or demonstration (AnLLM-AC).
  - Cache reduction is measured on cached five-shot demonstrations across 8 QA benchmarks (OBQA, WinoGrande, ARC-e/c, PIQA, HellaSwag, SCIQ, BoolQ). Demonstrations are 89–804 tokens long, 334 on average (Table 1(b), p. 4964).
  - This is not a long-context evaluation.
- Use 1, our sentence (l. 29): "Anchor compression \citep{pang2024anchor} cuts the keys/values cache by up to $99\%$ at an average accuracy cost of about $1.5\%$."
  - Source passages:
    - Abstract (p. 4958): "up to 99% keys/values cache reduction".
    - §1 (p. 4959): "minor decrease in accuracy (within 1.5%)".
    - §5 (p. 4963): "the average accuracy reduction is minimal, approximately 1.5%".
    - p. 4964: "an impressive 99% for AnLLM-AC".
  - Verdict: NARROW. The numbers are right, but the scope is missing, and the sentence sits in the "Long-context utilization" paragraph. Suggested: "Anchor compression \citep{pang2024anchor}---Llama2-7B continually pre-trained to fold each sequence into an anchor token---cuts the keys/values cache of cached five-shot demonstrations by up to $99\%$ on short question-answering benchmarks, at an average accuracy cost of about $1.5\%$."
- Use 2, our sentences (l. 67): "…compress each processed span into a single anchor token, discarding up to $99\%$ of the keys/values cache at an average accuracy cost of about $1.5\%$. That is consistent with a bounded number of load-bearing positions per span, and hard to express under exponential decay, where every discarded token should have cost something."
  - Verdict: NARROW. Add the scope. The inference should also acknowledge that the model was trained to move each span's information into its anchor. The evidence therefore shows how little state suffices; it does not show that an unmodified model's tokens are dispensable.
  - Suggested: "\citet{pang2024anchor} continually pre-train Llama2-7B to compress each sequence into a single anchor token; on five-shot question-answering benchmarks this discards up to $99\%$ of the demonstrations' keys/values cache at an average accuracy cost of about $1.5\%$. On our reading, a model that can be trained to carry each span forward in one position is consistent with a bounded number of load-bearing positions per span, and hard to square with a view in which every token carries equal weight."
- Use 3, our sentence (l. 100): "Anchor-LLM \citep{pang2024anchor} compresses each span into a single anchor token, cutting the keys/values cache by up to $99\%$ at an average accuracy cost of about $1.5\%$."
  - Verdict: NARROW, with the same fix as Use 1: after continual pre-training; for cached demonstrations; on short QA benchmarks.
- Use 4, our sentence (l. 122): anchor compression as one of "the existing demonstrations".
  - Verdict: ACCURATE.
- Use 5 (l. 190, Table): two-rate cell "Sparse retrieval focused on key tokens", exemplar "Anchor LLMs \citep{pang2024anchor}".
  - Verdict: NARROW. AnLLM is learned compression, not retrieval. Suggested cell: "Compression or sparse retrieval focused on key tokens".
- Uncited echo: the abstract's "anchor compression at $99\%$ KV-cache reduction" needs the same scope if the abstract keeps it.
- Bib changes vs current: added DOI, publisher and address. "Wong, Derek F." is kept: the printed paper says "Derek Fai Wong", while the ACL metadata says "Derek Wong".

### robinson2025token
- Source of record: NeurIPS 2025, https://proceedings.neurips.cc/paper_files/paper/2025/hash/d8892ad16f16c11dd592f2e90066c951-Abstract-Conference.html (DOI 10.52202/085713-4929). Access: full text (camera-ready PDF; also arXiv v3).
- Retraction: none found (Crossref: 0 update notices).
- Shared scope:
  - The tests run on the static input token-embedding matrices of GPT2, Llemma7B, Mistral7B and Pythia6.9B (§1, p. 2).
  - The flagged tokens are mostly word-initial tokens, word fragments, and whitespace or non-printing tokens (§5.2, p. 8; §6, p. 10).
  - About 0.1% of tokens are singular (appendix, p. 16).
- Use 1, our sentence (l. 32): "…whose fiber-bundle hypothesis test flags tokens whose embedding neighborhoods violate the local-smoothness assumption; semantically equivalent prompts containing such irregular tokens produce less stable continuations than those containing only regular-neighborhood tokens."
  - Source passages:
    - Abstract (p. 1): the response "will likely exhibit less stability than the other". This is derived from Theorem 2 (§3.2, p. 5) together with the test results.
    - §6 (p. 10): "future experiments can be run to explore the impact of irregular tokens" on response variability.
  - Verdict: NARROW [substantive]. The first half is ACCURATE. The stability claim is a theoretical implication that the authors explicitly leave to future experiments, and they make no comparison with prompts containing "only regular-neighborhood tokens". Suggested: "…; they argue, via a theorem on how such singularities propagate to the output, that of two semantically equivalent prompts, the one containing a flagged token will likely receive the less stable response---an implication they leave to future experiments."
- Use 2, our sentences (l. 104): "…fiber-bundle analysis distinguishes regular-neighborhood tokens (perturbation has minimal effect) from irregular-neighborhood tokens (prompts containing them yield less stable continuations). On our reading the irregular tokens sit at manifold junctions, and the mapping to our key/non-key partition is direct: irregular-neighborhood tokens are exactly the points where a small input change can move the trajectory between manifolds."
  - Source passages:
    - Abstract (p. 1): "Failing to reject the null is uninformative".
    - §7 Limitations (p. 10): the test "does not afford us any evidence as to the type of singularity".
    - Partial support for "junctions": §6 (p. 10) hypothesizes that manifolds for different languages would be joined at tokens such as "*".
  - Verdict: NARROW [substantive, must-fix]:
    - "(perturbation has minimal effect)" is contradicted by the paper, which says non-rejection is uninformative.
    - "Yield less stable continuations" is predicted, not measured.
    - "The mapping … is direct" and "exactly the points" overclaim. These are input-embedding singularities, mostly word fragments, about 0.1% of the vocabulary, and no link to long-range key tokens is tested.
  - Suggested: "\citet{robinson2025token}'s fiber-bundle test identifies irregular-neighborhood tokens in the input-embedding spaces of four open LLMs and argues that prompts containing them will likely yield less stable responses (failing to reject regularity at a token is, in their words, uninformative). On our reading, irregular tokens are candidate manifold junctions---points where a small input change could move the trajectory between regions, as the authors themselves illustrate with tokens such as `*' that join distinct usages; whether they coincide with the key tokens of our partition is untested, and most flagged tokens are word-initial pieces and word fragments."
- Use 3, our sentence (l. 138): the manifold account leans on this paper; it is recent and larger-scale replication would help.
  - Verdict: ACCURATE. Optionally add that the paper's evidence is against a single smooth manifold. That is compatible with a stratified (singular) space, which is how we use it, but a reader skimming the title may see a contradiction.
- Bib changes vs current:
  - Entry type changed from `@article` (arXiv) to `@inproceedings`: NeurIPS 2025, vol. 38, pp. 147340–147376, DOI 10.52202/085713-4929.
  - Crossref lists pp. 163602–163638 for the same DOI (Curran's pagination, same length).
  - Title now in proceedings Title Case.

### viswanathan2024geometry
- Source of record: TMLR 2026. Listed on https://jmlr.org/tmlr/papers/ (August 2026) with the official BibTeX at https://jmlr.org/tmlr/papers/bib/rBEgNAslpY.bib; OpenReview forum rBEgNAslpY (bot-check page, not bypassed). Access: full text via arXiv v2 (https://arxiv.org/abs/2501.10573v2), whose comment says it "matches published version" in TMLR.
- Retraction: none found.
- Shared scope:
  - Models: four 7–8B pretrained models (Llama 3 8B, Mistral 7B, Pythia 6.9B-dedup, OPT 6.7B).
  - Data: 2,244 Pile-10K prompts truncated to the first 1,024 tokens "to eliminate the length-induced bias" (§3, p. 5).
  - Measure: the intrinsic dimension of each prompt's token point cloud, per layer.
  - Analysis: a Pearson correlation of log ID against average surprisal, computed across prompts (§5, Fig. 2, p. 7).
- Use 1, our sentence (l. 32): "\citet{viswanathan2024geometry} link intrinsic dimensionality to prediction loss; high-confidence contexts collapse to lower-dimensional representations."
  - Source passages: the abstract says ID is "strongly correlated with average surprisal". §5 (p. 7) reports a "positive correlation between intrinsic dimension and surprisal across all models".
  - Verdict: NARROW. The first clause is ACCURATE. "Collapse" implies a process the paper does not measure; the finding is a correlation across prompts. Suggested: "…link intrinsic dimensionality to prediction loss: across prompts, those whose token representations occupy lower-dimensional point clouds have lower average surprisal."
- Use 2, our sentences (l. 106): "…link this to confidence: prompts that elicit low-intrinsic-dimensional representations correlate with lower prediction loss. The model's state contracts as confidence rises---which is why the per-token error rate $e_{\text{non}}$ should fall, not stay constant, as context accumulates."
  - Verdict: NARROW [substantive]. The first sentence is ACCURATE. The second presents a within-sequence dynamic, and its consequence for e_non, as established. The paper holds prompt length fixed and measures neither errors nor context growth. Suggested second sentence: "On our reading, if confident prediction goes with a lower-dimensional state, context that progressively constrains the state should push $e_{\text{non}}$ down rather than leave it constant---a within-sequence prediction the paper does not test."
- Bib changes vs current: added ISSN 2835-8856 and url, following the official TMLR BibTeX. Title, authors, journal and year 2026 are confirmed. The note about the earlier title was confirmed on arXiv v1 (17 Jan 2025, "The Geometry of Tokens in Internal Representations of Large Language Models").

### gao2024insights
- Source of record: Findings of EMNLP 2024, https://aclanthology.org/2024.findings-emnlp.447/ (DOI 10.18653/v1/2024.findings-emnlp.447). Access: full text (https://aclanthology.org/2024.findings-emnlp.447.pdf).
- Retraction: none found (Crossref: 0 update notices).
- Shared scope:
  - Tasks: Liu et al.'s key-value retrieval (100 pairs of UUIDs) and multi-document QA (30 documents).
  - Models: LLaMa3-8B-Instruct and Mistral-7B-Instruct-v0.3, plus Gemma in the appendix.
  - Probe: a linear probe on the last-token representation at each layer predicts the gold pair or document index, i.e. the position of the target information (§3, pp. 7612–7613).
- Use 1, our sentence (l. 32): "…find near-perfect classifier accuracy at locating target information in the model's hidden states even when the surface generation gives the wrong answer."
  - Source passages (§4.1, p. 7614):
    - For key-value pairs: "there is always a layer where its probe can almost perfectly identify the location", and "This holds true even when the LLM provides an incorrect answer".
    - For multi-document QA: "peak probing accuracy is consistently higher than the direct answer accuracy".
  - Verdict: NARROW (minor). "Near-perfect" holds for key-value retrieval only. Suggested: "…find that a probe can almost perfectly locate the target key-value pair from the model's hidden states even when the generated answer is wrong (on multi-document QA, probing accuracy is consistently above generation accuracy)."
- Use 2, our sentence (l. 78): "The manifold structure also explains the compartmentalization \citet{gao2024insights} document: intermediate layers preserve correct internal representations even when the surface output strays, because the hidden-state trajectory remains on the correct manifold even when token sampling does not."
  - Source passage: §5 (p. 7615). The authors attribute the failures to positional bias: "delayed extraction of this information leads to a noticeable drop in accuracy".
  - Verdict: NARROW [substantive]:
    - What the probe recovers is the position of the target information, not "correct internal representations" in general.
    - Token sampling plays no role in their setup, which is answer generation from a long prompt.
    - "Explains" asserts our mechanism over the authors' positional-bias account.
  - Suggested: "The manifold structure also offers a reading of the gap \citet{gao2024insights} document: intermediate layers encode where the needed information sits even when the generated answer is wrong. On our reading, the hidden-state trajectory can remain on the correct manifold while the output does not; the authors attribute the gap to positional bias and late extraction."
- Use 3, our sentences (l. 108): "…probes that achieve near-perfect accuracy at locating target information in intermediate representations, even when the LLM's surface generation gives the wrong answer---a ``know but don't tell'' gap between probing accuracy and generation accuracy that holds across positions and across models. The information was preserved internally; only the surface form failed. This is the manifold-stays-correct behavior our framework predicts."
  - Source passages: as in Use 1. The Fig. 2 caption (p. 7613) says probes "surpass the model's generated answers across all gold positions", and §3 (p. 7613) reports consistency across the three models.
  - Verdict: NARROW:
    - Sentence 1 is ACCURATE apart from the scope of "near-perfect".
    - "Only the surface form failed" overstates: the answers were wrong in content, and the probe recovers a location, not the answer.
    - Sentence 3 should be marked as our reading.
  - Suggested replacement for sentences 2–3: "The location of the needed information was encoded internally; the failure was in using it. On our reading this is the manifold-stays-correct behavior our framework predicts; the authors explain it by positional bias, noting that the later a layer locates the information, the lower the generation accuracy."
- Bib changes vs current:
  - Booktitle now ends "…: EMNLP 2024"; DOI, publisher and address added.
  - Author order (Gao first) is confirmed by the venue PDF and the ACL Anthology. arXiv v2 lists Taiming Lu first; do not "fix" the bib toward arXiv.
  - "Lu, TaiMing" follows the ACL metadata; the paper prints "Taiming".

### yao2023tree
- Source of record: NeurIPS 2023, https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html (DOI 10.52202/075280-0517). Access: full text (venue PDF …/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf).
- Retraction: none found (Crossref: 0 update notices).
- Shared scope: GPT-4 (May 2023) on Game of 24, using 100 hard games indexed 901–1,000. ToT runs breadth-first search with breadth b = 5 over 3 thought steps, using the LM's own value prompts (§4.1, Table 2).
- Use 1, our sentence (l. 35): "Tree-of-Thoughts \citep{yao2023tree} extends the idea with structured tree search over intermediate thoughts, each branch self-evaluated before expansion, and pulls GPT-4 on Game-of-24 from $4\%$ to $74\%$."
  - Source passages:
    - Abstract: CoT "only solved 4% of tasks"; ToT reaches 74%.
    - §4.1: "at each step we keep the best b = 5 candidates", after the LM rates each candidate as sure, maybe or impossible.
    - §3: CoT-SC is a special case of ToT.
  - Verdict: ACCURATE.
- Use 2, our sentence (l. 112): "\citet{yao2023tree}'s Tree-of-Thoughts moves GPT-4 on Game-of-24 from $4\%$ to $74\%$ by branching at high-uncertainty points specifically."
  - Source passage: §4.1. The search expands and evaluates at every step; uncertainty-targeted branching appears nowhere in the paper.
  - Verdict: NARROW [substantive]. The mechanism clause is wrong. Suggested: "…from $4\%$ to $74\%$ by breadth-first search over intermediate steps, keeping at each step the five partial solutions the model itself rates most promising; their error analysis finds that about $60\%$ of chain-of-thought samples have already failed after the first step." The paper's error analysis (§4.1) says "around 60% of CoT samples already failed the task after generating the first step". That supports a decision-point reading honestly.
- Use 3, our sentence (l. 128): "…\citet{yao2023tree}'s tree search, and \citet{moshkov2025aimo}'s GenSelect all exploit the convergence-of-correct-paths structure."
  - Source passages: ToT's mechanism is lookahead and backtracking with self-evaluation. The paper says the most-frequent-answer heuristic "only applies when the output space is limited" (§2, p. 3), and Table 2 shows CoT-SC (k=100) at only 9.0%.
  - Verdict: NARROW. Suggested: "\citet{wang2023self}'s self-consistency and \citet{moshkov2025aimo}'s GenSelect exploit the convergence of correct paths on a shared answer; \citet{yao2023tree}'s tree search exploits the model's ability to evaluate partial solutions at intermediate decision points."
- **Caveat [substantive]:** Table 2 shows majority voting (CoT-SC) barely helping on Game of 24 (4.0% to 9.0%). That is a reasoning task, so it cuts against the claim at l. 35 and l. 112 that ensembles help on reasoning and fail on knowledge.
- Bib changes vs current: added pages 11809–11822, DOI and publisher. "Griffiths, Thomas L." is kept as printed; the proceedings metadata says "Tom Griffiths".

### costello2025think
- Source of record: arXiv, https://arxiv.org/abs/2504.18116 (v1). Access: full text (arXiv v1).
- A peer-reviewed version exists: "Think, Prune, Train: Can Small Models Teach Themselves to Reason?", 2025 IEEE International Conference on LLM-Aided Design (ICLAD), pp. 195–203, DOI 10.1109/ICLAD65226.2025.00012.
  - It has the same four authors, and its abstract is verbatim identical to arXiv v1, per the IEEE Xplore REST metadata.
  - It is listed at https://iclad.ai/lad25-accepted-papers.
  - Its full text is paywalled, so I could read only its abstract.
- Retraction: none found (the IEEE record in Crossref has no update notices; arXiv v1 is active).
- Shared scope: GSM8K and CodeContests; Gemma2-2B, Gemma2-9B and LLaMA-3.1-70B-Instruct; supervised fine-tuning on self-generated, correctness-pruned traces over up to 4 rounds.
- Use 1, our sentences (l. 89): "…observe that iterative self-training raises Pass@1 while Pass@$k$ remains relatively stable. On our reading, this is the marginal gain from majority voting falling as correct reasoning paths cluster on a narrow manifold while incorrect ones fan out: ensemble methods only help when the model's spread of guesses straddles the right region."
  - Source passages:
    - §1 (p. 1): "Pass@50 and Pass@20 remain relatively stable"; the authors read this as the model maintaining diversity.
    - §4.2 (p. 7): Pass@20 is "mostly plateauing after the first iteration".
    - §4.5 (p. 9) re-reads the pattern as possible mode collapse: the model "converges on a narrower set of high-probability outputs".
  - Verdict: NARROW [substantive]. The first sentence is ACCURATE. But Pass@k is oracle coverage (any of k samples correct), not majority voting, and the paper reports no majority-vote results. "Incorrect ones fan out" is not in the paper either. Suggested second sentence: "On our reading, the headroom from sampling more (Pass@$k$ minus Pass@1, the most an oracle selector could gain) shrinks as probability mass concentrates on correct paths---the authors themselves describe the model as converging `on a narrower set of high-probability outputs'---so ensembles help only while the model's spread of guesses still straddles the right region."
- Use 2, our sentence (l. 131): "\citet{costello2025think}'s self-improvement curves---Pass@1 rising round by round while Pass@$k$ holds---are, on our reading, the staircase pattern our model predicts at finer resolution, not the smooth exponential decay of the alternative."
  - Verdict: DROP. These curves plot accuracy against self-training round, not reliability against output length. Neither the two-rate model nor the independent-error model predicts anything about training rounds, and the paper reports no length dependence. If you want something in its place, this is defensible: "\citet{costello2025think}'s self-improvement curves---Pass@1 rising round by round while Pass@$k$ holds---show that single-sample accuracy and coverage can move independently, so evaluations should report both."
- Use 3, our sentence (l. 133): "building on the alignment-not-scale results of \citet{costello2025think}".
  - Verdict: NARROW. TPT is supervised self-training on the model's own correctness-filtered traces; the paper does not frame it as alignment. Suggested: "building on the self-training-over-scale results of \citet{costello2025think}".
- Use 4, our sentence (l. 161): "…shows that smaller models ($2$--$9$B parameters) iteratively fine-tuned on their own pruned reasoning traces can match models roughly an order of magnitude larger on GSM8K---improving Gemma2-2B from $41.9\%$ to $57.6\%$ Pass@1, Gemma2-9B to $82\%$ (matching LLaMA-3.1-70B), and LLaMA-3.1-70B to $91\%$ (above GPT-4o's $82\%$)."
  - Source passages: the abstract; §1 (p. 2), where Gemma2-9B's 82% is compared with LLaMA-3.1-70B-Instruct's 78%; and the Fig. 3 caption (p. 8) and Conclusion: "surpassing GPT-4o (82%)".
  - Verdict: NARROW (minor). All the numbers are ACCURATE. Only the 9B model is shown to match a model about 8x larger, so "smaller models (2–9B) … can match" overgeneralizes. Suggested: "…shows that models iteratively fine-tuned on their own correctness-pruned reasoning traces can close much of the gap to far larger ones on GSM8K---Gemma2-2B from $41.9\%$ to $57.6\%$ Pass@1, Gemma2-9B to $82\%$ (above LLaMA-3.1-70B-Instruct's $78\%$, a model about $8\times$ larger), and LLaMA-3.1-70B itself to $91\%$ (above GPT-4o's $82\%$)."
- Use 5 (l. 196, Table): row "Key-token-restricted metrics", exemplar "success-plateau curves \citep{costello2025think}".
  - Verdict: DROP this exemplar. TPT proposes no key-token-restricted metric.
- Use 6 (l. 198, Table): row "Alignment over scale", exemplar "TPT".
  - Verdict: NARROW. Change the cell to "Self-training over scale".
- Bib changes vs current: added the arXiv DOI and a note recording the ICLAD 2025 version.
  - **Decision for the author:** switch to the IEEE entry only if you are willing to rest the non-abstract claims (Pass@k stability, GPT-4o's 82%) on the arXiv full text, because I could not check them in the paywalled IEEE version. The alternative entry is below, kept out of the .bib to avoid a duplicate key:

```bibtex
@inproceedings{costello2025think,
  title     = {Think, Prune, Train: Can Small Models Teach Themselves to Reason?},
  author    = {Costello, Caia and Guo, Simon and Goldie, Anna and Mirhoseini, Azalia},
  booktitle = {2025 IEEE International Conference on LLM-Aided Design (ICLAD)},
  pages     = {195--203},
  address   = {Stanford, CA, USA},
  publisher = {IEEE},
  year      = {2025},
  doi       = {10.1109/ICLAD65226.2025.00012}
}
```

---

**Bib file check.** `A_v3_carryover.bib` was compiled with BibTeX 0.99e under both `plainnat` and `IEEEtran`. Each run produced 14/14 bibitems with 0 warnings.
