<!-- Ledger part C: pillar 1, token importance (KV-cache sparsity, prompt compression, attention sinks). Audited 2026-10-03.
Method notes:
- Full text read for all 15 papers: latest arXiv PDF for every paper, plus the venue camera-ready PDF for 13 of them (NeurIPS proceedings, proceedings.iclr.cc, PMLR, ACL Anthology). Every quoted phrase was string-matched in both versions. Page numbers are physical PDF pages ("arXiv p." / "venue p."); one number means it is the same in both.
- Two camera-ready versions could not be opened because OpenReview serves a browser-verification page, which was not bypassed: PyramidKV (COLM 2025) and the KV-cache survey (TMLR). For both, the arXiv full text was used.
- Venues were confirmed on official pages: NeurIPS and ICLR proceedings listings and their BibTeX exports, PMLR v235/v306, ACL Anthology event pages and .bib exports, the TMLR accepted-papers list at jmlr.org/tmlr, and COLM's 2025 accepted-papers page. The DBLP API was unreachable (dblp.org resets the connection and the mirror sits behind a bot check), so DBLP was not used.
- Retraction check: Crossref query.bibliographic=<title>&rows=3, plus a second query for "Retraction: <title>". I looked for update-to or retraction relations and checked each arXiv abs page for a withdrawal notice. Nothing was found for any paper.
- Quote policy: verbatim quotation is limited to one short phrase (under 15 words) per paper. All other evidence is paraphrased and given its section, table or figure and page so it can be checked in the PDF. Typographic quotes are normalised to ASCII. "[...]" marks an omission.
-->

### zhang2023h2o
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html (NeurIPS 2023: Advances in NeurIPS 36, pp. 34661-34710, DOI 10.52202/075280-1506). Access: full text (arXiv v3 https://arxiv.org/pdf/2306.14048v3 and the NeurIPS camera-ready PDF; the cited passages are identical in both).
- Retraction: none found. Crossref record 10.52202/075280-1506 has no update or retraction relation, and the arXiv abs page shows no withdrawal.
- Use 1. Intended claim: "a small portion of tokens ('heavy hitters') contributes most of the attention value"
  - Source passage: "a small portion of tokens contributes most of the value when computing attention scores" (Abstract, p.1). Supporting evidence is in Sec. 3.1-3.2 and Fig. 2 (p.4-5).
  - Scope: The observation was made on OPT, zero-shot, on the WikiText-103 validation set. Attention matrices are over 95% sparse in almost all layers if every entry below 1% of its row maximum counts as zero (Sec. 3.1, p.4). The authors describe accumulated attention per token as power-law distributed and correlated with how often tokens co-occur (Sec. 3.2, Fig. 2b). Masking the heavy hitters makes accuracy collapse (Fig. 2c).
  - Verdict: ACCURATE. This is the authors' own framing. If we mention the distribution, write that the authors describe it as power-law rather than asserting it ourselves.
- Use 2. Intended claim: "keeping ~20% heavy hitters preserves quality with large throughput gains"
  - Source passage (paraphrase): The abstract labels the throughput setting a 20% heavy-hitter configuration. It reports throughput up to 29x higher than DeepSpeed Zero-Inference, 29x higher than HF Accelerate and 3x higher than FlexGen on OPT-6.7B and OPT-30B (p.1). The body describes the cache differently. Sec. 5.1 Baselines (p.7) says H2O splits its cache budget evenly between heavy hitters and the most recent tokens. Sec. 5.1 Main Results (p.8) reports accuracy comparable to the full cache at a total KV budget under 20%, which is more than a 5x memory reduction. The opening line of Sec. 5.1 (p.7) puts it as 5-10x memory reduction with comparable accuracy on most, not all, tasks.
  - Scope: Models are OPT 6.7B-175B, LLaMA and GPT-NeoX-20B. Most tasks are 5-shot lm-eval-harness or HELM tasks (COPA, MathQA, OpenBookQA, PiQA, RTE, Winogrande), plus XSUM and CNN/DailyMail. Throughput was measured in a FlexGen-based system on a T4 with 16 GB and CPU offloading, and on an A100, using synthetic padded prompts and XSUM. Much of the speedup comes from avoiding offloading and running larger batches (Sec. 5.2, p.8-9). The authors call XSUM and CNN/DailyMail their long-generation tasks, but these outputs are news summaries and the rest are short answers. None of this tests long-output reliability.
  - Verdict: NARROW. Safe wording: "H2O keeps a KV-cache budget of 20% of the sequence, split evenly between heavy-hitter and recent tokens. On most of the evaluated OPT, LLaMA and GPT-NeoX tasks this matched full-cache accuracy. In a FlexGen-based system it raised generation throughput up to 29-fold over DeepSpeed Zero-Inference and Hugging Face Accelerate, and 3-fold over FlexGen [zhang2023h2o]."
- Other findings a reviewer would expect:
  - (i) Heavy hitters alone are not enough. Keeping only heavy hitters, or only recent tokens, loses 2.85-22.75% (Sec. 5.3 Q4, p.10). The sparse set that works is heavy hitters plus recent tokens.
  - (ii) Eviction cannot be undone. The authors warn that evicting important KVs can wreck generation because of its sequential dependency (Sec. 3.2, p.5). They show the recency-only "Local" policy collapsing on XSUM and CNN/DM at budgets where H2O still matches the full cache (Sec. 5.1, p.8). This bears directly on sequence-level reliability.
  - (iii) App. B.2 (arXiv p.21-22; venue p.22-23) reports two biases. Accumulated scores favour older tokens, and many heavy hitters sit at sentence beginnings, which overlaps with attention sinks (see gu2025sink).
  - (iv) The 4-million-token "infinite input" result (Sec. 5.3 Q1, Fig. 5, p.9) is perplexity on a single PG-19 sample, not task accuracy.
- Bib/venue notes: The NeurIPS export spells the author "Zhangyang \"Atlas\" Wang"; the bib uses the arXiv byline, "Wang, Zhangyang". The export title is plain "H2O"; the printed title uses a subscript 2.

### xiao2024streamingllm
- Source of record: https://proceedings.iclr.cc/paper_files/paper/2024/hash/5e5fd18f863cbe6d8ae392a93fd271c9-Abstract-Conference.html (ICLR 2024, pp. 21875-21895 in the proceedings.iclr.cc volume). Access: full text (arXiv v4 https://arxiv.org/pdf/2309.17453v4 and the ICLR camera-ready PDF; the cited passages are identical in both).
- Retraction: none found. There is no Crossref record because ICLR does not deposit DOIs, and the arXiv abs page shows no withdrawal.
- Use 1. Intended claim: "keeping the initial 'sink' tokens plus a recent window recovers window-attention performance"
  - Source passage: "keeping the KV of initial tokens will largely recover the performance of window attention" (Abstract, p.1). Details are in Sec. 3.1-3.2 and Fig. 3 (p.4-5). The Table 2 ablation shows that 4 initial tokens are enough.
  - Scope: "Performance" here means language-modelling perplexity. Window attention collapses as soon as the first tokens are evicted. Adding back 4 initial tokens brings perplexity down to the level of the sliding-window-with-recomputation oracle (Fig. 3: 20K-token texts; Llama-2, MPT, Falcon, Pythia).
  - Verdict: ACCURATE. Add "perplexity" if space allows.
- Use 2. Intended claim: "stable to millions of tokens"
  - Source passage (paraphrase): The abstract (p.1) and Fig. 5 (Sec. 4.1, p.7) report stable, efficient language modelling on streams of up to 4 million tokens, using the concatenated PG19 test set of 100 books.
  - Scope: This is perplexity stability with a fixed cache: 2048 tokens for Llama-2 and 1024 for the other models, including the 4 sink tokens (Sec. 4.1). The paper's own limitations rule out more than that:
    - App. A (p.15): StreamingLLM neither extends the context window nor adds long-term memory, and it is unsuitable for long-document QA or summarisation.
    - App. C (Table 7, p.16): StreamEval accuracy falls to zero once the distance between query and answer exceeds the cache.
    - App. D (Table 8, p.17): on LongBench, a cache of 4 sinks plus 3496 recent tokens underperforms simple truncation.
  - Verdict: NARROW. Safe wording: "With a fixed cache of a few initial 'sink' tokens plus a recent window, StreamingLLM keeps language-modelling perplexity stable over streams of up to 4 million tokens. Anything outside that cache is lost, so this shows stable local prediction, not preserved long-range dependency [xiao2024streamingllm]."
- Other findings a reviewer would expect:
  - Sink tokens collect large attention scores even though they carry little meaning (Sec. 1, p.2). The authors trace this to softmax normalisation; gu2025sink refines that account.
  - In 160M-parameter pre-training runs, a dedicated learnable sink token removes the need to keep several initial tokens (Sec. 3.3, 4.2).
  - A larger cache does not consistently lower perplexity (Sec. 4.4, Table 6, p.9), which suggests the models do not fully use the extra context.
- Bib/venue notes: The proceedings.iclr.cc export has booktitle "International Conference on Learning Representations" and a volume field of "2024". The volume field is dropped and the booktitle is written in the OpenReview style used in the other ledger parts.

### li2024snapkv
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html (NeurIPS 2024: vol. 37, pp. 22947-22970, DOI 10.52202/079017-0722). Access: full text (arXiv v2, still labelled "Preprint. Under review.", and the NeurIPS camera-ready PDF; the cited passages are identical, with small wording changes in the camera-ready introduction).
- Retraction: none found (Crossref record 10.52202/079017-0722 has no update or retraction relation).
- Use 1. Intended claim: "each head attends to a stable set of positions identifiable before generation"
  - Source passage: "each attention head [...] consistently focuses on specific prompt attention features during generation" (Abstract, p.1). The abstract adds that the pattern can be read from an observation window at the end of the prompt. The evidence is in Sec. 3, Figs. 2-3 (p.3-4).
  - Scope:
    - The positions are prompt (prefix) positions only.
    - The observations use UltraChat dialogues with prompts over 3K tokens and responses over 512 tokens (Sec. 3, p.3).
    - "During generation" was measured over four 128-token windows, i.e. the first 512 generated tokens (Sec. 3, p.4).
    - The observation window is the end of the prompt, which contains the user's question or instruction.
    - Sec. 4.2.1 (arXiv p.5; venue p.6) shows that different instructions on the same document pick out different positions, so the pattern depends on the query.
  - Verdict: NARROW. Safe wording: "SnapKV finds that, for each head, the prompt positions that will receive high attention during generation can be predicted from a short observation window at the end of the prompt, which contains the query. This selection stays largely consistent over the next roughly 512 generated tokens, but which positions matter changes with the instruction [li2024snapkv]."
- Use 2. Intended claim: "large memory/speed gains with comparable quality"
  - Source passage (paraphrase): At 16K-token inputs, generation is 3.6x faster and memory efficiency 8.2x better than the baseline, and performance is comparable to the baseline across 16 long-sequence datasets. Needle-in-a-Haystack runs to 380K tokens on one A100-80GB with a negligible accuracy drop (Abstract, p.1; Sec. 5.1-5.3).
  - Scope:
    - Speed and memory were measured on LWM-Text-Chat-1M against the HuggingFace implementation.
    - Quality was measured on LongBench with LWM-Text-Chat-1M, LongChat-7B-32k, Mistral-7B-Instruct-v0.2 and Mixtral-8x7B-Instruct.
    - The prompt KV cache was compressed to 1024-4096 entries. On roughly 13K-token inputs, 1024 entries is about 92% compression (Sec. 5.3, arXiv p.9; venue p.10).
    - Outputs are short answers and summaries.
  - Verdict: ACCURATE. When citing, say "prompt KV cache" and "on LongBench".
- Other findings a reviewer would expect:
  - Only the prompt KV is compressed. Generated tokens are kept in full, so the paper does not test memory over long outputs.
  - Keeping only the highest-weight positions is not enough. Neighbouring tokens must be pooled in, or the model retrieves partial details and invents the rest (Sec. 4.3, p.6). Importance comes in clusters, not single tokens.
  - The authors state that SnapKV cannot extend a model's long-context ability (Sec. 6, arXiv p.12; venue p.10).
- Bib/venue notes: none. The export matches the byline.

### tang2024quest
- Source of record: https://proceedings.mlr.press/v235/tang24l.html (ICML 2024, PMLR 235:47901-47911). Access: full text (arXiv v2 https://arxiv.org/pdf/2406.10774v2 and the PMLR PDF; the cited passages are identical).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "a small portion of critical tokens dominates attention"
  - Source passage (paraphrase): The abstract (p.1) presents this as a finding of previous work (H2O, FastGen; Sec. 1 and 3.2), not as Quest's own result. Quest's own measurement is Fig. 3 (p.3), on LongChat-7B-v1.5-32k and PG19. With oracle top-k selection and less than 0.01 perplexity increase, sparsity is under 10% in the first two layers and over 90% in every later layer.
  - Scope: Attention at decode time. Quest leaves the first two layers dense.
  - Verdict: NARROW, on attribution and scope. Safe wording: "Decode-time attention is highly sparse beyond the first layers. In LongChat-7B, more than 90% of cached tokens can be skipped in every layer after the first two with negligible change in perplexity [tang2024quest], extending observations in [zhang2023h2o]."
- Use 2. Intended claim: "which tokens are critical depends on the query"
  - Source passage: "we observe the criticality of a token highly depends on the query" (Abstract, p.1). Evidence is in Sec. 3.3, Figs. 2 and 4 (p.2-3), and the Table 1 caption (p.5).
  - Scope: Fig. 2 is a Llama-2-7B toy example, and Fig. 4 measures top-10 recall in passkey retrieval. The passkey runs use 10K tokens (LongChat-7B) and 100K tokens (Yarn-Llama-2-7B-128k). Query-agnostic eviction (H2O, TOVA, StreamingLLM) drops the passkey before the question arrives and scores about 0-10%. Quest scores 65-100% at budgets of 32-4096 tokens.
  - Verdict: ACCURATE.
- Other findings a reviewer would expect:
  - Quest keeps the entire KV cache in memory and loads only the top pages for each query (Sec. 2.2, p.2; Sec. 3.5). This shows that each step can read sparsely. It does not show that a small fixed subset can be kept.
  - Sec. 4.2.2 (p.5) notes that PG19 perplexity only involves local dependencies, which is why passkey and LongBench tests are needed for long-range dependence.
  - On LongBench, a 1K budget performs comparably to the full cache (Sec. 4.2.3, p.6).
  - The PMLR web abstract swaps the speedups (2.23x / 7.03x) relative to the PDF. The PDF gives 7.03x for self-attention and 2.23x end-to-end; cite the PDF numbers.
- Bib/venue notes: PMLR and its PDF title the paper "QUEST: ..." (arXiv: "Quest: ..."), and the bib follows PMLR.

### cai2024pyramidkv
- Source of record: https://colmweb.org/2025/AcceptedPapers.html, the official COLM 2025 accepted-papers list, where it is marked Spotlight and linked to OpenReview https://openreview.net/forum?id=ayi7qezU87. Access: full text of arXiv v4 (15 May 2025, https://arxiv.org/pdf/2406.02069v4, still labelled "Preprint. Under review."). The COLM camera-ready could not be opened (OpenReview verification page), so all quotes and pages refer to arXiv v4.
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "matches full-KV performance retaining ~12% of the KV cache"
  - Source passage (paraphrase): On LongBench, PyramidKV matches full-cache performance while keeping 12% of the KV cache (Abstract, p.1). Sec. 1 (p.2) specifies this as a KV-cache size of 2048. LongBench inputs average 1,235-18,409 tokens (Sec. 5.1.2, p.6).
  - Scope: LLaMA-3-8B-Instruct, Mistral-7B-Instruct and LLaMA-3-70B-Instruct, with greedy decoding. Compression applies to the prompt KV cache. Outputs are short (QA, summaries, code completion). Scores are averaged over 16-17 datasets.
  - Verdict: NARROW. Safe wording: "On LongBench (prompts of about 1-18K tokens, short answers), a prompt KV cache averaging 2048 entries per layer, about 12% of the input, matched full-cache scores for LLaMA-3-8B/70B-Instruct and Mistral-7B-Instruct [cai2024pyramidkv]."
- Use 2. Intended claim: "attention funnels toward few tokens in higher layers"
  - Source passage: "(a.k.a massive activation or attention sink)" (Abstract, p.1). This is the authors' own gloss on the "critical tokens" that upper layers attend to. The abstract describes attention spreading widely in lower layers, consolidating within documents in middle layers, and focusing on a few such tokens in upper layers. Supporting evidence is in Sec. 3, Fig. 2 (p.3-4) and App. D (Figs. 5-6).
  - Scope: Qualitative, head-averaged attention maps of one multi-document QA example per model (LLaMA in the main text; Mistral-7B and Mixtral-8x7B in App. D). No quantitative measure of concentration is given.
  - Verdict: NARROW. Safe wording: "PyramidKV's attention maps show attention spread broadly in lower layers and concentrated on a few tokens in upper layers ('pyramidal information funneling'). The authors identify those tokens with massive activations and attention sinks, so this is evidence that attention concentrates, not that those tokens carry the needed content [cai2024pyramidkv]."
- Other findings a reviewer would expect:
  - At an extreme budget of 0.7% of the KV cache, PyramidKV beats the other compressors (up to +20.5 points on TREC), but no method recovers full-cache scores (Abstract; Table 1).
  - The statement in App. A that no decoding collapse was observed (p.13) is self-reported, not a systematic test.
  - Needle-in-a-Haystack with 128 entries was tested only up to 8K context (Sec. 5.3.1).
- Bib/venue notes: The venue is confirmed by COLM's official accepted-papers page. COLM's 2025 call for papers names it the 2nd Conference on Language Modeling, so the booktitle follows the OpenReview pattern used in the other ledger parts ("Second Conference on Language Modeling (COLM)"). The OpenReview BibTeX itself could not be fetched. The key says 2024 but the paper was published in 2025; the key is kept as instructed and year = 2025.

### jiang2023llmlingua
- Source of record: https://aclanthology.org/2023.emnlp-main.825/ (EMNLP 2023 main conference: pp. 13358-13376, DOI 10.18653/v1/2023.emnlp-main.825). Access: full text (arXiv v2 https://arxiv.org/pdf/2310.05736v2 and the Anthology PDF; the passages are identical).
- Retraction: none found (Crossref DOI record, no update relation).
- Use 1. Intended claim: "up to 20x prompt compression with little performance loss"
  - Source passage: "allows for up to 20x compression with little performance loss" (Abstract, p.1). The numbers are in Sec. 5.2 and Table 2 (p.6) and the Limitations section (p.9-10).
  - Scope:
    - The 20x figure is the GSM8K quarter-shot setting with GPT-3.5-Turbo-0301 as the target model: exact match 77.33 against 78.85 for the full few-shot prompt, a 1.52-point loss. At 14x the loss is 1.44 points.
    - On BBH, 5x compression costs 8.5 exact-match points and 7x costs 13.2.
    - In Table 1, ShareGPT reaches 3.3x and Arxiv-March23 reaches 9x, judged by BERTScore.
    - The Limitations section reports a notable drop at 25-30x on GSM8K.
    - What gets compressed is mostly redundant few-shot chain-of-thought demonstrations. Tokens are scored by a small LM's perplexity (Alpaca-7B or GPT2-Alpaca).
  - Verdict: NARROW. Safe wording: "LLMLingua compressed few-shot chain-of-thought prompts by up to 20x on GSM8K with about a 1.5-point exact-match loss for GPT-3.5-Turbo. Losses were larger on BBH (8.5-13.2 points at 5-7x), and accuracy drops notably beyond about 25x [jiang2023llmlingua]."
- Other findings a reviewer would expect:
  - Importance here is information-theoretic: low-perplexity tokens are dropped. It is not attention-based.
  - Both demonstration-level selection and iterative token-level pruning matter (Table 3 ablation).
  - Compressed prompts make the target model's outputs shorter (Sec. 5.5, Fig. 2, p.8), so prompt compression changes output length.
- Bib/venue notes: The Anthology export is used. Title braces are normalised to {LLMLingua}.

### cai2025rkv
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html (NeurIPS 2025: vol. 38, pp. 60980-61005, DOI 10.52202/085713-2038). Access: full text (arXiv v4 of 22 Jan 2026 and the NeurIPS camera-ready PDF; the cited passages are identical).
- Retraction: none found (Crossref record, no update relation).
- Use 1. Intended claim: "for reasoning models, ~10% of the KV cache retains nearly full performance on chain-of-thought"
  - Source passage: "preserves nearly 100% of the full KV cache performance using only 10%" (Abstract, p.1). Sec. 4.2 "Ratio Budget" (p.7) gives the budget needed to match the full cache:

    | Model | MATH-500 | AIME-24 | Budget giving 105% of full-cache accuracy |
    |---|---|---|---|
    | R1-Llama-8B | 34% | 10% | 16% (AIME-24, per Sec. 1) |
    | R1-Qwen-14B | 54% | 25% | 33% (dataset not stated) |

  - Scope:
    - R-KV compresses the model's own long chain-of-thought at decode time, every 128 generated tokens.
    - Models are DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-Distill-Qwen-14B, on MATH-500 and AIME-24 (pass@1 over 64 samples, temperature 0.6).
    - Budget ratios are relative to the average generated length: about 2.8-3.0K tokens on MATH-500 and 12.4-15.5K on AIME-24 (Sec. 4.2, p.7).
    - The only baseline is SnapKV, adapted to decoding.
  - Verdict: NARROW. Safe wording: "R-KV, a redundancy-aware compressor applied while decoding, matched full-cache accuracy with budgets of 10-34% of the generated length for DeepSeek-R1-Distill-Llama-8B and 25-54% for R1-Distill-Qwen-14B on MATH-500 and AIME-24. The 10% figure is the best case (AIME-24, 8B model), and attention-only selection (SnapKV) fell well short [cai2025rkv]."
- Other findings a reviewer would expect. This paper is the closest to our setting, since it compresses long outputs rather than prompts.
  - Attention-based importance alone fails on long chain-of-thought. Repeated self-reflection attracts high attention to itself (Sec. 2.2, Fig. 3, p.3).
  - Scoring by attention alone, or by redundancy alone, performs worst (Sec. 5.1, p.7). Removing redundancy, not only exploiting sparse long-range dependency, is what makes small budgets work.
  - The attention-importance scores are themselves sparse and dominated by a few outliers (Sec. 5.1, p.7).
  - The authors' analysis claims over half of R1's reasoning tokens contribute little (Sec. 1, p.2).
  - Efficiency: a 90% memory saving and 6.6x throughput at a 10% budget (Abstract; App. C.2).
  - Scope limits: mathematics only, two distilled models.
  - Small internal inconsistencies: the abstract says two datasets; Sec. 4.1 says three benchmarks but lists two, and the evaluation setup also mentions AIME 2025.
- Bib/venue notes: The export lists "cheng Luo", corrected to "Luo, Cheng", and "Animashree Anandkumar" (byline: "Anima Anandkumar"); the export form is kept. The export volume field "38, Main Conference" is set to 38.

### yuan2025nsa
- Source of record: https://aclanthology.org/2025.acl-long.1126/ (ACL 2025, Volume 1 Long Papers: pp. 23078-23097, DOI 10.18653/v1/2025.acl-long.1126; the Anthology event listing shows a Best Paper award badge). Access: full text (arXiv v2 https://arxiv.org/pdf/2502.11089v2 and the ACL PDF). The ACL version moves "Rethinking Sparse Attention Methods" to App. B and renumbers the sections; the numbers are unchanged.
- Retraction: none found. The Crossref DOI record has no update relation. A National Science Review item with a similar title (10.1093/nsr/nwag212) is a separate publication, not a correction notice.
- Use 1. Intended claim: "models trained with natively sparse attention match or exceed full attention, suggesting sparsity is structure rather than approximation"
  - Source passage: "maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning" (Abstract, p.1). The results are in ACL Sec. 3 / arXiv Sec. 4:
    - Table 1, general benchmarks: NSA is better on 7 of 9 metrics.
    - Table 2, LongBench: average 0.469 for NSA against 0.437 for full attention.
    - Table 3: AIME after supervised fine-tuning.
  - Scope:
    - One model: 27B total parameters, 3B active, GQA plus MoE.
    - Pretrained on 260B tokens (introduction) or 270B tokens (ACL Sec. 3.1; arXiv Sec. 4.1) at 8K context, then adapted to 32K.
    - NSA combines three branches: compressed coarse tokens over the whole context, 16 selected 64-token blocks, and a 512-token sliding window.
    - One run per arm.
    - Margins on general benchmarks are small (average 0.456 against 0.443).
    - AIME scores are low in absolute terms: 0.121 against 0.046 at 8K, and 0.146 against 0.092 at 16K.
  - Verdict: NARROW. Safe wording: "In the authors' single-run comparison, NSA, a natively trained sparse attention (compressed coarse tokens, selected blocks and a 512-token window), matched or exceeded a full-attention twin of the same 27B-parameter MoE model on general, LongBench and AIME evaluations [yuan2025nsa]." Reading this as "sparsity is structure rather than approximation" must be presented as our interpretation, not as the authors' finding.
- Other findings a reviewer would expect:
  - The authors' own motivation argues against treating post-hoc sparsity as free. Citing MagicPIG, they note that in dense-trained models the top 20% of attention entries cover only about 70% of attention mass, which leaves structures such as retrieval heads exposed to inference-time pruning (arXiv Sec. 2.2, p.4; ACL App. B.2, p.12).
  - The compression branch gives every token coarse access, so NSA is not "a sparse subset only".
  - Needle-in-a-Haystack is perfect at 64K.
  - Speedups at 64K: up to 9.0x forward, 6.0x backward, and up to 11.6x expected decode speedup.
- Bib/venue notes: The Anthology export lists "Yuxing Wei", while the PDF byline prints "Y. X. Wei"; the export form is kept.

### vakilian2025short
- Source of record: https://arxiv.org/abs/2512.08082 (arXiv v2, 10 Feb 2026). No venue was found: the paper is absent from the ICLR 2026 proceedings, ICML 2026 (PMLR 306) and the ACL 2026 Anthology. A search result points to an OpenReview forum (wL3LrVW0by), but it could not be opened. Access: full text (https://arxiv.org/pdf/2512.08082v2).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "75–80% of sequences (1–7k-token documents) need only the last ≤96 tokens"
  - Source passage: "75–80% require only the last 96 tokens at most" (Abstract, p.1; the abstract's context is sequences of 1-7k tokens from long-context documents). Also Sec. 3.3 (p.4) and App. D, Table 4 (p.25).
  - Scope:
    - A "sequence" is a sampled prefix plus its true next token, not a whole document. Prefixes are 32-1K tokens for short documents and 6-7K tokens for long ones.
    - Only positions that the oracle model already predicts correctly, with a top-1 margin of at least 0.2, are kept (Sec. 3.2, p.4). The oracles are LLaMA-3-8B, Mistral-7B-Instruct-v0.2 and Qwen2-7B.
    - MCL is the shortest suffix, starting from 32 tokens, that reproduces that confident top-1 prediction.
    - Table 4 (LLaMA-3) shows how much the result depends on the criterion:

      | Dataset (window) | Top-1 criterion (MCL) | Whole-distribution criterion (DaMCL, JSD) |
      |---|---|---|
      | GovReport (≤96) | 75.19% | 36.36% |
      | News (≤64) | 80.52% | 45.43% |
      | Wikipedia (≤64) | 78.15% | 31.65% |

    - The Sec. 3.3 body gives about 80-90% needing 32-96 tokens or fewer; the abstract says 75-80%.
  - Verdict: NARROW. Safe wording: "Using 7-8B LLMs as oracles, Vakilian et al. look only at next-token positions the model already predicts correctly and confidently. For 75-80% of these positions, in sequences of up to about 7k tokens, the last 64-96 tokens reproduce the full-context prediction. When the whole next-token distribution must match (DaMCL), the share falls to roughly 32-45% [vakilian2025short]."
- Other findings a reviewer would expect:
  - The authors treat short-context dominance as a source of bias. Next-token training and perplexity are dominated by short-range positions, which can hide long-context weaknesses (Sec. 3.3, p.4-5, linking to Sun et al. 2021).
  - They build a detector for positions that need long context (DaMCL thresholding, Sec. 5) and a decoding correction, TaBoo, that improves long-context QA (Sec. 6).
  - The MCL histogram is heavy-tailed. It is fitted as a power law in log-log space in Sec. 3.3 (p.4), yet a Fig. 18 caption (p.25) calls the pattern exponentially decaying. Do not attribute a functional form to this paper.
  - Everything is teacher-forced next-token prediction on natural text, not free-running long generation.
- Bib/venue notes: arXiv @misc entry. The title follows the arXiv abs page.

### gu2025sink
- Source of record: https://proceedings.iclr.cc/paper_files/paper/2025/hash/f1b04face60081b689ba740d39ea8f37-Abstract-Conference.html (ICLR 2025, pp. 97114-97144 in the proceedings.iclr.cc volume; Spotlight per the arXiv comment). Access: full text (arXiv v2 https://arxiv.org/pdf/2410.10781v2 and the ICLR PDF; the passages are identical).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1 (caveat). Intended claim: "attention sinks are an optimization/softmax artifact, so high attention ≠ carrying meaning"
  - Source passage: "which could be non-informative and not contribute to the value computation" (Abstract, p.1). The sentence says the sink acts like a key bias that stores extra attention. The same abstract says sinks emerge after effective optimisation on sufficient data and stem at least partly from softmax normalisation. Sec. 7.4 (p.10) shows that sigmoid attention without normalisation removes sinks in LMs up to 1B parameters.
  - Scope: The paper studies the first-token sink only (Sec. 8, p.10). The controlled experiments use about 60M-parameter LLaMA-style models trained on 5B Pile tokens (Sec. 4, p.5), plus runs at 1B. The observational part analyses open LLaMA-2/3, Mistral, GPT-2, Pythia and OPT models.
  - Verdict: NARROW. Safe wording: "Gu et al. show that the first-token attention sink emerges during pre-training once optimisation is effective and data sufficient. It acts like a key bias that absorbs attention without contributing to the value computation, and it arises at least partly from softmax normalisation; removing the normalisation removes it in models up to 1B parameters. A high attention score therefore does not by itself show that a token carries content [gu2025sink]." Avoid the word "artifact". The authors call sink tokens functionally important (App. A.4, p.15), and removing learned sink parameters lowers performance (Sec. 7.3).
- Other findings a reviewer would expect:
  - The authors leave open whether sinks help downstream performance (Sec. 8).
  - The sink position can shift with the data distribution or loss (for example, prefix language modelling).
  - Weight decay encourages sinks, and small learning rates weaken them (Sec. 4-6).
- Bib/venue notes: none (export matches byline). Booktitle follows the OpenReview style used in the other parts.

### chen2026pitfalls
- Source of record: https://aclanthology.org/2026.acl-long.1926/ (ACL 2026, Volume 1 Long Papers: pp. 41530-41553, DOI 10.18653/v1/2026.acl-long.1926). The venue question "(ACL 2026?)" is confirmed: main conference, long paper. Access: full text (arXiv v2 https://arxiv.org/pdf/2510.00231v2 and the ACL PDF; the passages are identical).
- Retraction: none found (Crossref DOI record, no update relation).
- Use 1. Intended claim: "some instructions degrade much faster under compression and get ignored"
  - Source passage: "certain instructions degrade much more rapidly with compression" (Abstract, p.1). The abstract continues that these instructions end up completely ignored. See also Pitfall 1 (Sec. 3, p.3) and Pitfall 5 (Sec. 5, p.6).
  - Scope: Only the prompt is compressed, offline (Sec. 2.3, p.3). Models are Llama3 8B and Qwen2.5 14B. Five eviction policies are run through KVPress (StreamingLLM, H2O, K-Norm, SnapKV, TOVA) on IFEval single- and multi-instruction prompts. The compression ratio is the fraction of entries evicted, from 0.3 to 0.9.
  - Verdict: ACCURATE. When citing, add "under prompt (offline) compression".
- Use 2. Intended claim: "system prompts can leak"
  - Source passage (paraphrase): The abstract and Pitfall 3 (Sec. 4, p.5) show that under compression the defence instruction in a system prompt gets evicted and the model reveals the system prompt. How much leaks depends on the method, the order of instructions (Pitfall 4) and eviction bias.
  - Scope: Same setting as Use 1. Leakage is scored with ROUGE-L and cross-checked with an LLM judge (App. L).
  - Verdict: ACCURATE.
- Other findings a reviewer would expect:
  - The authors conclude that eviction policies cannot tell which entries can be dropped without losing meaning (Pitfall 6, Sec. 5, p.6; Sec. 7, p.9). This is direct counter-evidence to using attention scores as an importance proxy.
  - Effects depend strongly on the policy and the model (Pitfall 2).
  - Simple "fair eviction" and whitelisting reduce the damage (Sec. 5-6).
  - Online (decode-time) compression is not tested (Sec. 8).
- Bib/venue notes: The Anthology export gives "Van Den Broeck, Guy" and "Israel, Daniel Mingyi". The PDF byline reads "Guy Van den Broeck, Daniel Israel". The bib uses "{Van den Broeck}, Guy" and keeps "Israel, Daniel Mingyi". The Anthology web abstract says "Llama3.1 8B" where the PDF says "Llama3 8B"; follow the PDF.

### liu2026semantic
- Source of record: https://proceedings.mlr.press/v306/liu26dz.html (ICML 2026, PMLR 306:78537-78565). The venue question "(ICML 2026?)" is confirmed. Access: full text (arXiv v4 https://arxiv.org/pdf/2502.01941v4 and the PMLR PDF; the passages are identical).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "retrieval tasks are robust to KV compression but reasoning tasks degrade severely"
  - Source passage: "while retrieval tasks remain robust, reasoning tasks exhibit severe Task-Dependent Degradation under aggressive compression" (Abstract, p.1). See also Observation 1 (Sec. 4.3, p.5) and the matched comparison in App. D.2 (p.22).
  - Scope:
    - Prefill compression of few-shot chain-of-thought prompts, plus LongGenBench for long generation.
    - Models: LLaMA-3.1-8B (base and instruct), Mistral-7B-Instruct and DeepSeek-R1-Distill-Llama-8B.
    - Methods: StreamingLLM, H2O, SnapKV, PyramidKV, PyramidInfer and ChunkKV.
    - "Aggressive" means keeping less than about 20-40% of the cache. With 40% or more retained, every task is stable (Obs. 1, p.5). GSM8K accuracy falls from about 0.75 to below 0.5 once less than 20% is retained.
    - In App. D.2 the same methods and ratios (10%, 30%) are applied to both kinds of task. LongBench stays comparatively stable, while 50-shot GSM8K (about a 4K-token prompt) degrades sharply at 10%.
  - Verdict: NARROW. Safe wording: "Under aggressive KV compression (keeping about 20-30% of the cache or less), retrieval-oriented long-context tasks stay comparatively robust, while multi-step arithmetic reasoning, code and safety tasks degrade sharply. With at least 40% retained, all task types were stable [liu2026semantic]."
- Other findings a reviewer would expect:
  - The authors' explanation speaks directly to our pillar. In high-density reasoning almost every prompt token matters, whereas in retrieval only a small "needle" subset does (Sec. 1, p.2). Token sparsity is therefore task-dependent.
  - Decode-time compression of roughly 4K-token generations loses more than 20% of performance below a 30% ratio (Obs. 6, p.7). This is direct evidence about long outputs.
  - The R1-distilled reasoning model is more robust: at 10% retention it loses 15.8%, against 35.3% for the instruct model (Obs. 2; the percentages are in App. D.1, Tables 6 and 8).
  - Shorter prompts are more vulnerable (Obs. 3).
  - Keeping whole semantic units (shots or chunks) beats token-level selection (ShotKV, Sec. 5).
- Bib/venue notes: none (PMLR export matches byline).

### li2025scbench
- Source of record: https://proceedings.iclr.cc/paper_files/paper/2025/hash/a540b17fb2295c736d5afd6c507acf66-Abstract-Conference.html (ICLR 2025, pp. 66063-66093 in the proceedings.iclr.cc volume). Access: full text (arXiv v2 https://arxiv.org/pdf/2412.10319v2 and the ICLR PDF; the passages are identical).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "sub-O(n) memory methods suffer in multi-turn/shared-context use"
  - Source passage: "sub-O(n) memory methods suffer in multi-turn scenarios" (Abstract, p.1). See also findings 1-4 in Sec. 1 (p.4) and Fig. 3.
  - Scope:
    - 12 tasks in two shared-context modes, multi-turn and multi-request.
    - 13 long-context methods, including StreamingLLM, SnapKV, PyramidKV, Quest, RetrievalAttention, LLMLingua-2, KIVI, MInference and Tri-shape.
    - Models: Llama-3.1-8B/70B, Qwen2.5-32B/72B, Llama-3-8B-262K and GLM-4-9B-1M, plus Codestral-Mamba and Jamba-1.5-Mini.
  - Verdict: ACCURATE.
- Other findings a reviewer would expect:
  - Sparse-decoding methods do well on the first query and then lose accuracy on follow-up queries. Compression conditioned on the current query discards what later queries need (Sec. 1, p.4).
  - Methods with sub-O(n) memory drop sharply at a 1/4 compression rate.
  - Exact-match retrieval needs O(n) memory, while global-information tasks tolerate sparsity. This contrasts with liu2026semantic's finding that retrieval is robust, which was measured with single requests.
  - Long generation shifts the distribution of KV importance, which hurts even O(n)-memory methods (Sec. 1, p.4). This is direct evidence that importance is not stationary over long outputs.
  - App. F (p.27): using the model's own answers as context for later turns lowers accuracy. The authors attribute this to errors propagating from earlier turns.
- Bib/venue notes: The export gives "Amir Abdi"; the bib uses the byline form "Abdi, Amir H.".

### li2025kvsurvey
- Source of record: https://openreview.net/forum?id=z3JZzu9EA3 (Transactions on Machine Learning Research, May 2025). It is listed at https://jmlr.org/tmlr/papers/ with BibTeX at https://jmlr.org/tmlr/papers/bib/z3JZzu9EA3.bib. Access: full text of arXiv v3 (30 Jul 2025, https://arxiv.org/pdf/2412.19442v3; its comment says "Accepted to TMLR 2025" and that it was revised with more papers). The TMLR PDF could not be opened (OpenReview returned 403 / verification page).
- Retraction: none found (no Crossref record; no withdrawal on arXiv).
- Use 1. Intended claim: "prior review; covers efficiency taxonomy but does not connect token sparsity to sequence-level reliability"
  - Source passage: "may degrade model performance if key information is lost" (Sec. 2.3, Challenges, p.4). This is the survey's general statement of the accuracy cost, made in its list of KV-cache management challenges. Supporting locations:
    - Abstract (p.1): taxonomy of token-, model- and system-level methods, plus text and multimodal benchmarks.
    - Sec. 4.1 (p.6): notes that the attention matrix is sparse.
    - Sec. 8 (p.31), future directions: cross-category integration, real-world case studies, domain-specific optimisation, privacy and security, and implementation complexity.
  - Scope: A full-text search of arXiv v3 found nothing on output or generation length, chain-of-thought or reasoning models, or error accumulation over long outputs.
  - Verdict: ACCURATE. Recommended wording: "Li et al. survey KV-cache management as an efficiency problem, covering token-, model- and system-level methods and benchmarks. They note that attention is sparse and that compression can lose key information, but they do not analyse what token-level sparsity means for the reliability of long generated outputs [li2025kvsurvey]." The absence was checked on arXiv v3, not on the TMLR PDF.
- Other findings a reviewer would expect: none that cut against our use.
- Bib/venue notes: The TMLR export gives "Haoyang LI", "Nicole HU" and "Li Qing"; the byline is "Haoyang Li, ..., Nicole Hu, ..., Qing Li", and the bib uses the byline. TMLR has no volume or pages.

### li2024promptsurvey
- Source of record: https://aclanthology.org/2025.naacl-long.368/ (NAACL 2025, Volume 1 Long Papers: pp. 7182-7195, DOI 10.18653/v1/2025.naacl-long.368). The task listed only arXiv, but there is a published venue. Access: full text (arXiv v2 https://arxiv.org/pdf/2410.12388v2 and the Anthology PDF; the passages are identical).
- Retraction: none found (Crossref DOI record, no update relation).
- Use 1. Intended claim: "prior review of hard/soft prompt compression; check whether it discusses reliability over long outputs"
  - Source passage: "For tasks with short outputs, these improvements may not be substantial." (Sec. 6.1, Limited efficiency improvements; arXiv p.7, venue p.8). Output length comes up only in efficiency terms: this sentence, plus related remarks that soft-prompt gains arise only while new tokens are generated (Sec. 6.1-6.2). The abstract (p.1) sets out the hard-prompt versus soft-prompt taxonomy. Sec. 6.1 lists the challenges as information loss, reduced model capability and marginal efficiency gains.
  - Scope: A survey of hard-prompt methods (SelectiveContext, the LLMLingua family, Nano-Capsulator) and soft-prompt methods (ICAE, 500xCompressor, xRAG, UniICL and others). It runs no evaluation of its own.
  - Verdict: ACCURATE as a prior review. The answer to the check is no: it does not discuss reliability over long outputs. It frames compression losses as information loss and reduced capability on the input side.
- Other findings a reviewer would expect: It calls for comparing prompt compression against attention-side methods such as sliding-window and sparse attention, noting this has not been done (Sec. 6.1). Our review can point to that gap.
- Bib/venue notes: The key says 2024 but the paper was published in 2025; the key is kept as instructed and year = 2025.
