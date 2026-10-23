# Ledger part F — pillar 3C (cross-model shared structure; correlated errors)

Checked 2026-10-03. Every paper below was opened in full text (arXiv HTML and PDF; venue PDF where one exists). Venue metadata comes from PMLR, the NeurIPS proceedings, OpenReview (search API), or the ICLR virtual site. DBLP and OpenReview forum pages served bot-verification pages, which were not bypassed. Retraction checks used the Crossref query API (`query.bibliographic`, rows=3) plus the arXiv record. Quotes are kept under 15 words, one per source. Other details are paraphrased, with their locations given.

Required framing for 3C: the evidence supports shared local and relative structure, not a single universal global manifold. Each entry says whether the evidence comes from differently trained models or from one model or family.

---

### moschella2023relative
- Source of record: ICLR 2023. OpenReview forum https://openreview.net/forum?id=SrC-nwieGJ (from the DBLP record via the OpenReview API). https://iclr.cc/virtual/2023/oral/12532 lists it as an in-person oral (top 5%). Access: full text (https://arxiv.org/html/2209.15430 and https://arxiv.org/pdf/2209.15430v2, v2 of 7 Mar 2023, after acceptance). The OpenReview PDF itself was not opened because of the bot check.
- Retraction: none found. Crossref has no record for this title and no retraction notice; arXiv v2 is not withdrawn.
- Use 1 — intended claim: "angles/similarities between encodings are stable across independently trained models, enabling zero-shot stitching. Check modalities/models used."
  - Source passage: "the angles between the encodings within distinct latent spaces do not change" — Abstract. The same sentence restricts this to models trained on the same data with the same modeling choices. Sec. 3 states it as the method's core assumption: the change between trainings preserves angles.
  - Scope: small and medium encoders, not LLMs.
    - Retrainings with different seeds of AEs and VAEs on MNIST, Fashion-MNIST, and CIFAR-10/100 (Sec. 5.1, Table 3).
    - GCNs on Cora, CiteSeer, and PubMed (Secs. 4.2–4.3).
    - Two pretrained word-embedding models trained on different corpora, FastText and Word2Vec (Sec. 4.1, Table 1). After the relative transform, neighbourhood Jaccard is 0.34/0.39, MRR 0.94/0.98, and cosine 0.86, against about 0 for absolute coordinates.
    - Cross-lingual stitching between language-specific RoBERTa models (Table 4).
    - Cross-architecture text stitching between BERT-cased, BERT-uncased, ELECTRA, and RoBERTa (Table 5).
    - ViT variants and RexNet on images (Table 6).

    How it works: each sample is re-expressed as its cosine similarities to a shared set of anchor samples. When the domains differ, these are parallel anchors with a known correspondence. Zero-shot stitching needs a decoder trained on this relative representation.

    Stitching loses accuracy. TREC drops from 88.1 to 75.9 F1 and DBpedia from 97.4 to 80.5 ± 21.1 across architectures (Table 5). An English decoder with a Japanese encoder scores 65.7, against 90.1 without stitching (Table 4).
  - Verdict: NARROW → safe wording: "Moschella et al. observed that the angles between latent encodings are approximately preserved when networks are retrained on the same data with different seeds, and stay similar across architectures and across pretrained word-embedding models. Representing each sample by its cosine similarities to a shared set of anchor samples let them stitch encoders to decoders trained on that relative representation, with no further training, on image, text, and graph tasks, at some cost in accuracy [moschella2023relative]."
- Other findings a reviewer would expect:
  - The invariance is an empirical assumption, not a theorem. Deformations that are not isometries are not handled; App. A.3 and Fig. 7 sketch a quantization fix.
  - The choice and number of anchors matter. Relative representations trained end-to-end can collapse (App. A.2, Fig. 6).
  - Sec. 4.2, Fig. 3: on Cora, how similar a model's relative space is to a strong reference model tracks its accuracy (mean Pearson 0.955 over about 2,000 models, after filtering). This is useful if 3C links geometry to quality.
  - The method works because only relative (angular) structure is shared, not absolute coordinates. That matches the local/relative framing.
- Bib: Eleventh ICLR (2023). Author order follows arXiv and the ICLR page. There is no DOI; `url` points to the OpenReview forum.

### maiorca2023translation
- Source of record: NeurIPS 2023 proceedings, https://proceedings.neurips.cc/paper_files/paper/2023/hash/ad5fa03c906ca15905144ca3fbf2a768-Abstract-Conference.html (vol. 36, pp. 55394–55414, DOI 10.52202/075280-2418; OpenReview pBa70rGHlr, NeurIPS 2023 poster). Access: full text (proceedings PDF; https://arxiv.org/html/2311.00664 v2).
- Retraction: none found. The Crossref record 10.52202/075280-2418 has no update-to or relation entries.
- Use 1 — intended claim: "latent spaces of different pretrained models can be translated with simple (e.g., orthogonal/linear) transforms estimated from a few anchors."
  - Source passage: "the transformation relating to these pre-trained encoders is indeed mostly orthogonal" — Sec. 4.1 (Cross-Architecture), result analysis of Table 1. The same sentence appears in the NeurIPS PDF.
  - Scope:
    - Models: frozen pretrained encoders of base size (Table 7). Text: BERT cased and uncased, ELECTRA, RoBERTa, ALBERT, XLM-R, and the CLIP text encoder. Vision: RexNet, CSPDarkNet, four ViTs, and the CLIP image encoder. Sec. 4.3 adds pairs of CNN autoencoders that differ only in seed.
    - Fit: the map is fitted in closed form (least squares; SVD or Procrustes for orthogonal) on parallel anchors, meaning paired samples known to correspond.
    - Anchor count: comparable to the latent dimension (Sec. 4, Stitching Procedure). That is 1,000 anchors for 500-d spaces (Table 3), 2,000 for the cross-modal runs (Fig. 5), and 500 for the AE runs (Table 8). This is not "a few".
    - Decoders: SVM or MLP heads trained on the original absolute spaces.
    - Cross-modal: text↔image on N24News (Sec. 4.2).
    - Accuracy cost: with the ortho map, DBpedia drops from 0.78 to 0.66 and TREC from 0.87 to 0.79 (Table 1).
    - No LLM hidden states are studied.
  - Verdict: NARROW → safe wording: "Maiorca et al. showed that the latent spaces of different pretrained text and image encoders can be mapped onto one another by closed-form, largely orthogonal (Procrustes) transformations. The maps are fitted on a few hundred to a few thousand paired anchor samples, which is enough to reuse a classifier trained on one encoder's space with another encoder, without retraining [maiorca2023translation]." Avoid "a few anchors".
- Other findings a reviewer would expect:
  - For image autoencoders, the latent spaces are related by a class of maps larger than orthogonal (Sec. 4.3). Which simple map works depends on the setting.
  - Text encoders carry information in the embedding norm: L2 normalization hurts them (Table 2 vs Table 1).
  - On N24News, translated text embeddings can beat the image encoder on the image classifier (Sec. 4.2).
  - The authors leave open the right number of anchors and what makes two spaces compatible, such as intrinsic dimension (Sec. 5).
- Bib: from the NeurIPS proceedings BibTeX (NEURIPS2023_ad5fa03c). Editors are omitted.

### jha2025vec2vec
- Source of record: NeurIPS 2025 proceedings, https://proceedings.neurips.cc/paper_files/paper/2025/hash/4175dee33d6145cb8f0323703d138a53-Abstract-Conference.html (vol. 38, pp. 45963–45987, DOI 10.52202/085713-1530; OpenReview jiCLUPq5xv, NeurIPS 2025 poster). Access: full text (proceedings PDF; https://arxiv.org/html/2505.12540 v4, 26 Jan 2026). The key passages are the same in both.
- Retraction: none found. The Crossref record 10.52202/085713-1530 is clean.
- Use 1 — intended claim: "unsupervised translation between text-embedding spaces of different models without paired data. Note what kind of models (sentence encoders vs LLM hidden states)."
  - Source passage: "translating text embeddings from one vector space to another without any paired data" — Abstract.
  - Scope: sentence and text embedding models, not LLM hidden states.
    - Models (Table 1): GTR (T5), E5, GTE, and Stella (BERT); Granite (RoBERTa, multilingual); the CLIP text encoder. One extra pair uses a 4B Qwen3-based embedding model (App. C: cosine 0.50 for gte→qwen, 0.84 for qwen→gte).
    - Method (Sec. 3): MLP adapters with a shared backbone, trained with adversarial, cycle-consistency, and vector-space-preservation losses.
    - Data: about 1M unpaired embeddings per side, from disjoint Natural Questions texts (Sec. 4.1). 50K embeddings give nearly the same quality; 10K is weak (Table 7).
    - Results: in distribution, top-1 matching among 8,192 candidates reaches 1.00 and cosine reaches 0.92 (Table 2). Pairs with different backbones beat the naive and oracle-OT baselines by a wide margin; for gte→gtr, cosine is 0.75, top-1 0.91, and mean rank 2.64. Out of distribution it still works on tweets and medical records (Table 3). Translation to and from CLIP is weaker (Table 4).
    - Stability: the reported runs are the best of several initializations (Sec. 4.1). In a fixed budget, only 3 of 15 seeds converged for a pair with different backbones, against 14 of 15 for a same-backbone pair (App. E).
  - Verdict: NARROW → safe wording: "Jha et al. learned to translate between the embedding spaces of different text-embedding models, such as T5-based and BERT-based encoders, from unpaired samples alone. Most translated embeddings matched their true counterparts among thousands of candidates. The evidence concerns sentence-embedding models trained for similar objectives, not LLM hidden states, and training was unstable for unrelated backbones [jha2025vec2vec]."
- Other findings a reviewer would expect:
  - The authors frame the result as a stronger, constructive Platonic hypothesis: a universal latent space (Secs. 2 and 9). That is their conjecture. Cite the translation result, not the universal-manifold framing. A learned nonlinear map fits shared relational structure without needing identical global geometry.
  - Embedding models with the same backbone are already nearly compatible without translation (Table 2, naive baseline).
  - Security: translated embeddings leak document attributes and content (Sec. 6).
  - Kim et al. (ICML 2025, Sec. 2) cite this paper as a possible mechanism behind correlated LLM errors. This bridges the two halves of 3C, but nobody has tested the link.
- Bib: the proceedings list "Jha, Rishi; Morris, John"; OpenReview has the full middle names. The byline form (John X. Morris) is used.

### huh2024platonic
- Source of record: PMLR vol. 235 (ICML 2024), https://proceedings.mlr.press/v235/huh24a.html, pp. 20617–20642. OpenReview BH8TYy0r6u lists it as an ICML 2024 Oral. Access: full text (PMLR PDF; https://arxiv.org/html/2405.07987 v5).
- Retraction: none found.
- Use 1 — intended claim: "representations of different models/modalities converge as scale increases (a hypothesis with supporting evidence)."
  - Source passage: "they measure distance between datapoints in a more and more alike way" — Abstract. The subject is vision and language models as they get larger.
  - Scope: a position paper.
    - Evidence: a literature survey (Secs. 2.1–2.4) and experiments.
    - Vision experiment: 78 vision models on Places-365; models that do better on VTAB are more aligned with each other (Fig. 2).
    - Cross-modal experiment: language models vs vision models on WIT image–caption pairs; alignment rises with the language model's 1 − bits-per-byte score (Fig. 3).
    - The alignment metric is mutual k-nearest-neighbour overlap, which is a local metric (Sec. 2; App. A–B).
    - Cross-modal alignment peaks near 0.16 out of a maximum of 1 (Sec. 6, last paragraph).
    - The hypothesis (Sec. 1) and its selective pressures (Sec. 3) are argued, not proven. Sec. 6 lists counterexamples: modality-specific information, observations that are not bijective, and special-purpose systems.
  - Verdict: ACCURATE. Keep the word "hypothesis". Suggested wording: "Huh et al. hypothesize that, as models scale, their representations converge toward a shared statistical model of reality. Their evidence is that more capable vision and language models induce increasingly similar nearest-neighbour structure over paired data [huh2024platonic]."
- Other findings a reviewer would expect:
  - The title of record starts with "Position:".
  - The appendix figure on the CKNNA metric (PMLR Fig. 7; arXiv Fig. 10) shows cross-modal alignment getting stronger as k shrinks, so convergence is mostly local. This supports the 3C framing.
  - Sec. 5 speculates that scale may reduce hallucination. That is untested; do not cite it as evidence.
  - Gröger et al. (2026) show that the trends in global metrics vanish after null calibration, while the mutual-kNN trends survive.
  - Goel et al. (2025) build their correlated-mistakes study on this paper.
- Bib: PMLR BibTeX (pmlr-v235-huh24a), with the "Position:" prefix (the arXiv title lacks it). {Platonic} is brace-protected against IEEEtran sentence-casing. Editors and month are omitted.

### groger2026aristotelian
- Source of record: ICML 2026. OpenReview uz0gAAYydl lists it as "ICML 2026 regular" (venueid ICML.cc/2026/Conference); arXiv v2 (25 Jun 2026) is marked as the camera-ready. The PMLR volume for ICML 2026 is not on proceedings.mlr.press as of 2026-10-03 (the newest volume listed is v341), so there are no page numbers yet. Access: full text (https://arxiv.org/html/2602.14486 v2 and PDF).
- Retraction: none found.
- Use 1 — intended claim: "(refinement): after calibrating similarity metrics, global convergence largely disappears while local neighborhood agreement remains."
  - Source passage: "the apparent convergence reported by global spectral measures largely disappears after calibration" — Abstract. The same sentence adds that local neighbourhood similarity keeps significant agreement across modalities, but local distances do not.
  - Scope: a re-analysis using Huh et al.'s protocol (Sec. 6.3).
    - Data and models: 1,024 WIT image–text pairs. Language models from three families (BLOOM, OpenLLaMA, LLaMA); vision models from five (ImageNet-21K, MAE, DINOv2, CLIP, fine-tuned CLIP). That gives 204 pairs.
    - Settings: maximum over layers, k = 10, Benjamini–Hochberg FDR correction. The analysis is extended to video–language pairs (VideoMAE).
    - Calibration: a permutation-based null that corrects for width (dimension relative to sample count) and for depth (taking the maximum over layer pairs).
    - Result: correlation with language-model capability falls after calibration from 0.86 to 0.45 for linear CKA and from 0.89 to 0.39 for Procrustes. It stays near 0.85 for mKNN and 0.87 for CKNNA.
  - Verdict: ACCURATE. Suggested wording: "After correcting similarity scores for width and depth confounds, Gröger et al. find that apparent global convergence largely disappears. What persists across modalities is agreement on which inputs are each other's nearest neighbours [groger2026aristotelian]."
- Other findings a reviewer would expect:
  - The paper refines the Platonic hypothesis rather than refuting it (Sec. 7).
  - Its stated caveats: similarity has no ground-truth scale, and the permutation test assumes exchangeability.
  - Pairwise distances do not converge (CKA-RBF with a small bandwidth; Sec. 6.3, App. E.10). Only who-is-near-whom does.
  - This is the best single citation for "local/relative, not global".
- Bib: from the OpenReview BibTeX (booktitle "Forty-third International Conference on Machine Learning"). The surname is spelled Brbić, as on arXiv (OpenReview has "Brbic"). Add the PMLR volume and pages once they are published.

### ramesh2025activations
- Source of record: PMLR vol. 267 (ICML 2025), https://proceedings.mlr.press/v267/ramesh25a.html, pp. 51094–51116 (OpenReview W6RPXUUFic, ICML 2025 poster). Access: full text (PMLR PDF; https://arxiv.org/html/2501.14082 v2).
- Retraction: none found.
- Use 1 — intended claim: "exchanging activations instead of text improves multi-agent performance (up to ~27%) at lower compute. Check whether models are same-family."
  - Source passage: "up to 27.0% improvement over natural language communication across datasets with <1/4 the compute" — Abstract (PMLR PDF and arXiv v2).
  - Scope:
    - Method (Sec. 3.1): one model's last-token activation at layer j = 26 is replaced by the sender's activation at layer k. There is no training. An optional linear map W can be fitted on 3,072 sentences from C4.
    - Main experiments: LLaMA-3.2-3B sends to LLaMA-3.1-8B. These are different models from the same family. Seven benchmarks are used, each on a 100-question subset (Table 3).
    - The 27.0% is relative, not in points: MMLU Formal Logic goes from 37.0 (natural-language debate) to 47.0. On GSM8K, debate beats activation communication, 75.0 vs 64.0.
    - The coordination games use two copies of the same model (Table 2).
    - Cross-family test (Table 4): pairs from Qwen-2.5, Gemma-2, and LLaMA-3, on Biographies and GSM8K only, without W. Activation communication matches or beats debate there, but one cross-family pair falls below its stronger member alone on Biographies (73.0 vs 83.0).
  - Verdict: NARROW → safe wording: "Ramesh and Li splice an intermediate activation from one LLM into another's forward pass. They report gains over natural-language debate of up to 27% (relative) at under a quarter of the compute. Most experiments pair two LLaMA-3 models; a smaller cross-family test covers two tasks [ramesh2025activations]."
- Other findings a reviewer would expect:
  - App. B.4: across the six model pairs, the gain grows with a matrix similarity between the two models' activation spaces. The benefit of latent communication tracks how well the representations align.
  - Without the learned map, the method assumes the two embedding spaces are aligned, and it needs white-box access (Sec. 5).
  - Version difference: arXiv v2 offers the Platonic hypothesis as an alternative explanation for the cross-family results. The PMLR version of record drops that remark. Do not cite this paper as evidence for the Platonic hypothesis.
  - Liu (2026) files this method in its no-alignment, same-model group, which does not match the paper.
- Bib: PMLR BibTeX (pmlr-v267-ramesh25a). Editors are omitted.

### fu2026c2c
- Source of record: ICLR 2026. OpenReview LeatkxrBCi lists it as "ICLR 2026 Poster"; the arXiv v2 comment reads "Published in ICLR'26". Access: full text (https://arxiv.org/html/2510.03215 v2 of 2 Mar 2026). The ICLR abstract, fetched through the OpenReview API, matches v2.
- Retraction: none found.
- Use 1 — intended claim: "a learned projector fuses KV caches across heterogeneous models; +3–5% accuracy vs text communication and ~2x faster."
  - Source passage: "outperforms the text communication paradigm by approximately 3.1-5.4%" — Abstract of v2 and the ICLR version. The same sentence reports an average 2.5× latency speedup.
  - Scope:
    - Method: a trained fuser (projection, dynamic weighting, and a learnable gate per layer) merges the sender's KV cache into the receiver's. Both LLMs stay frozen.
    - Training: a new fuser for each model pair, on 500k OpenHermes-2.5 samples (Sec. 4.1).
    - Models: from Qwen2.5, Qwen3, Llama3.2, and Gemma3, from 0.5B to 14B parameters. The main table (Table 4) fixes Qwen3-0.6B as receiver, with Qwen2.5-0.5B, Llama3.2-1B, and Qwen3-4B-Base as senders. Table 7 adds Gemma3-1B, Qwen2.5-Math-1.5B, and Qwen2.5-Coder-0.5B as senders.
    - Benchmarks: OpenBookQA, MMLU-Redux, ARC-C, and C-Eval.
    - Size of gains: in accuracy points, averaging 5.36, 4.15, and 3.06 over text hand-off for the three senders.
    - Speedups: they vary by sender, at 3.46×, 1.51×, and 14.41× (Table 4).
    - Versions: the v1 abstract (Oct 2025) said 3.0–5.0% and 2.0×. v2 and the ICLR version say 3.1–5.4% and 2.5×.
  - Verdict: NARROW → safe wording: "Fu et al. train a small fuser that projects one LLM's KV cache into another's, across model families (Qwen, Llama, Gemma) and sizes. They report roughly 3–5 points higher accuracy than text hand-off, with a 2.5× average reduction in latency [fu2026c2c]." Update "~2x" to 2.5×. The fuser is trained for each pair; it is not zero-shot.
- Other findings a reviewer would expect:
  - Ablation (Table 6): fusing the receiver with a copy of itself already gives most of the gain. On OpenBookQA: 45.8 with fine-tuning alone, 50.6 with a copy of the same model, 52.6 with a different model. The content from the other model adds only about 1–2 points.
  - Replacing the receiver's cache with the projected sender cache alone drops average accuracy to 20.7 (Table 8). The transformed cache covers only part of the target model's space (Sec. 3.2.2). Translation is partial, not a global equivalence.
  - Errors propagate through the channel. The sender's reading can mislead the receiver into a wrong answer (Sec. 4.5, App. A.4.6). A much weaker sender can degrade a stronger receiver (Sec. 5, Limitations). This is directly relevant to error accumulation.
  - An independent audit [cheng2026audit] (arXiv:2608.04893, Aug 2026, not peer reviewed; full entry at the end of this file) found no example-specific content transfer through the released C2C projector (Qwen2.5-7B-Instruct to Qwen3-8B). The test used synthetic tasks where the receiver needs the sender's private information, and it is detection-level (three seeds). The audited pair is not one of C2C's tabulated configurations, and the authors say the result does not show that C2C's reported benchmark gains are artifacts.
- Bib: OpenReview BibTeX (fourteenth ICLR). {Cache-to-Cache} is brace-protected.

### zou2026latentmas
- Source of record: ICML 2026. OpenReview syG9I9ofd8 lists it as "ICML 2026 spotlight"; the arXiv v4 (3 Aug 2026) comment says ICML2026 Spotlight. Not yet in PMLR. Access: full text (https://arxiv.org/html/2511.20639 v4 and PDF; App. G was read in the PDF).
- Retraction: none found.
- Use 1 — intended claim: "agents collaborating in latent space improve accuracy and cut tokens/latency. Check whether agents share one base model (important: same-model vs cross-model)."
  - Source passage: "we assume that all agents in LatentMAS share the same shape of transformer layers" — App. G (Extension to Heterogeneous Agents), PDF p. 27.
  - Scope: one model, not cross-model.
    - Agents: in each run, every agent is the same backbone (Qwen3-4B, 8B, or 14B, or Llama-3 3B or 8B). They differ only by role prompt: planner, critic, refiner, and solver; or domain experts plus a summarizer.
    - Mechanism: each agent generates "latent thoughts" from its last-layer hidden states. These are mapped back to the input space by a closed-form matrix computed within the model (W_a, Sec. 3.1). Agents communicate by prepending the previous agent's KV cache, which requires identical architecture (Sec. 3.2). No training is involved.
    - Results (Sec. 4.1, 9 benchmarks): vs a single model, average gains of +14.6 (sequential) and +13.3 (hierarchical). Vs text-based multi-agent systems, +2.8 and +4.6, with 70.8% and 83.7% fewer output tokens and about 4× and 4.3× faster inference. The abstract's "up to 14.6%" is the gain over a single model, not over text-based agents.
  - Verdict: NARROW → safe wording: "When every agent is a copy of one backbone, passing hidden states and KV caches instead of text improved accuracy over text-based multi-agent baselines by 2.8–4.6 points on average, while cutting output tokens by 70.8–83.7% and latency about fourfold [zou2026latentmas]." Do NOT cite this as evidence that differently trained models share structure. App. G says heterogeneous agents would need a trainable adapter. In 3C it can only serve as the same-model contrast case.
- Other findings a reviewer would expect:
  - Lossless transfer (Thm. 3.3) holds by construction. The receiver reads a cache produced by the same weights on the same inputs (proof in App. B.2).
  - The expressiveness result (Thm. 3.1) assumes the Linear Representation Hypothesis.
  - Latent channels are harder to audit. The authors add a debug mode to track errors in intermediate steps (Sec. 5; App. F and I), which is relevant to error accumulation.
  - The independent audit [cheng2026audit] (arXiv:2608.04893, not peer reviewed; full entry at the end of this file) tested GSM8K, ARC-C, and MedQA, where the receiver can solve the task alone.
    - On Qwen3-4B/8B/14B, relaying the matched cache instead of another example's cache made no difference beyond ±2.8 points (TOST equivalence), apart from one small +1.5-point advantage.
    - On Mistral-Nemo-12B it found no advantage, but equivalence was not established.
    - So LatentMAS's benchmark gains need not reflect example-specific transmitted content.
    - When the receiver needs the sender's private information, the native LatentMAS relay transfers it at ceiling.
- Bib: OpenReview ICML 2026 BibTeX. Author order follows the ICML record and arXiv v4; v1 and the DBLP CoRR record put Xiyuan Yang second.

### kim2025correlated
- Source of record: PMLR vol. 267 (ICML 2025), https://proceedings.mlr.press/v267/kim25e.html, pp. 30038–30066 (OpenReview kzYq2hfyHB, ICML 2025 poster). Access: full text (PMLR PDF; https://arxiv.org/html/2506.07962 v1).
- Retraction: none found.
- Use 1 — intended claim: "models agree on ~60% of their errors when both are wrong, across providers/architectures."
  - Source passage: "agree on average about 60% of the time when both models are incorrect" — Sec. 1, point (1); the subject is pairs of models on HELM. Sec. 3.2 gives 0.6 on HELM and 0.423 on Hugging Face.
  - Scope:
    - What is measured: when both models of a pair are wrong, how often they pick the same wrong option. This is not the overlap in which questions each model misses.
    - HELM: 71 LLMs, many of them proprietary, on 14,042 four-option MMLU questions, so chance is 1/3.
    - Hugging Face Open LLM Leaderboard: 349 LLMs on 12,032 questions, mostly ten-option; mean 0.423 against a chance level of 0.127.
    - Of all pairs, 97.5% (HELM) and 100% (Hugging Face) agree more often than chance.
    - Regression (Table 1): a shared company, a shared base architecture, and similar size all raise agreement. Higher accuracy of both models raises it even after controlling for those factors (R² 0.34–0.61).
    - A separate resume-screening task uses 20 LLMs.
  - Verdict: NARROW → safe wording: "On the HELM leaderboard (71 LLMs, MMLU questions), when two models both get a question wrong, they pick the same wrong option about 60% of the time on average, against 33% expected by chance. Agreement is higher within a provider or architecture, yet more accurate models have highly correlated errors even across providers and architectures [kim2025correlated]." Avoid "agree on 60% of their errors": the statistic is conditional on both models being wrong, and it comes from one leaderboard.
- Other findings a reviewer would expect:
  - LLM judges inflate the accuracy of less accurate models, especially models from the same provider (Sec. 4). A hiring simulation shows monoculture effects (Sec. 5).
  - In Sec. 2 the authors suggest a mechanism: embeddings can be translated across models (Jha et al.) and activations are consistent at similar depths. This explicitly bridges 3C's two claims, but they do not test it.
  - The metric ignores output probabilities, unlike Goel et al.'s CAPA.
- Bib: PMLR BibTeX (pmlr-v267-kim25e). The first author is listed as Elliot Myunghoon Kim (arXiv: Elliot Kim).

### goel2025think
- Source of record: PMLR vol. 267 (ICML 2025), https://proceedings.mlr.press/v267/goel25b.html, pp. 19621–19678 (OpenReview 3Z827FtMNe). Access: full text (PMLR PDF; https://arxiv.org/html/2502.04313 v2).
- Retraction: none found.
- Use 1 — intended claim: "a similarity metric (CAPA) shows model mistakes become more similar as capability rises."
  - Source passage: "model mistakes are becoming more similar with increasing capabilities" — Abstract; Sec. 5, Fig. 6.
  - Scope:
    - Metric: CAPA (κp) adjusts agreement for chance, uses output probabilities, and counts two different wrong answers as a disagreement (Sec. 2).
    - Trend study: 130 open models from Open LLM Leaderboard 2, on MMLU-Pro (11,828 questions after filtering) and BBH (23 multiple-choice tasks). Models are split into five bins by accuracy percentile. Similarity is computed only between models from different developers and families (Sec. 5.1, App. D.1).
    - Limits: the result is a correlation, it covers multiple-choice questions only, and it uses open models.
    - The trend is steeper for instruction-tuned models (App. D.2.1). Question difficulty is not a major confounder (App. D.2.2).
  - Verdict: ACCURATE. Suggested wording: "Using CAPA, a chance-adjusted measure of how much two models' mistakes overlap, Goel et al. find that among 130 open models compared across developers, more capable models make more similar mistakes [goel2025think]."
- Other findings a reviewer would expect:
  - LLM judges favour models similar to themselves (Sec. 3).
  - Weak-to-strong training gains more when the supervisor and the student differ (Sec. 4).
  - Sec. 5 starts from Huh et al. and asks whether converging representations also mean similar mistakes. This is a published bridge between 3C's two claims.
  - The authors say causation is not established (Sec. 7).
- Bib: PMLR BibTeX (pmlr-v267-goel25b), with Strüber's umlaut (arXiv metadata has "Struber") and {AI} brace-protected.

### liu2026latentsurvey
- Source of record: arXiv:2606.05711, v3 of 15 Jul 2026, https://arxiv.org/abs/2606.05711. No venue was found: the OpenReview search has no match and there is no journal-ref. Access: full text (https://arxiv.org/html/2606.05711 v3 and PDF).
- Retraction: none found.
- Use 1 — intended claim: "prior review/taxonomy of latent communication methods; check whether it connects to error accumulation (for our novelty claim)."
  - Source passage: "error propagation across multiple communication rounds would make claims of superiority more precise" — Sec. 7.4 (Theoretical Understanding). This is the survey's only mention of error propagation.
  - Scope: a single-author scoped review.
    - Search: arXiv, ACL Anthology, and OpenReview, with a cut-off of 15 Jul 2026 (Sec. 2).
    - Taxonomy: 18 representative methods along three axes (Sec. 5). WHAT is sent: embeddings, hidden states, or KV caches. WHICH alignment is used: latent-space and layer alignment. HOW the message is fused into the receiver.
    - It covers Ramesh and Li, C2C, and LatentMAS, among others.
  - Verdict: ACCURATE as a prior taxonomy. On the novelty question, the survey does not analyze error accumulation. It raises nearby concerns only as open problems or failure modes: auditability, state contamination that affects later turns without a readable trace (Sec. 6.3), security and robustness (Sec. 7.2), and error propagation across rounds (Sec. 7.4). Safe novelty wording: "Existing reviews of latent communication organize methods by what is transmitted and how it is aligned and fused [liu2026latentsurvey]. They flag error propagation across communication rounds as an open question, but do not analyze how errors accumulate through latent channels." Avoid "first".
- Other findings a reviewer would expect:
  - The survey is not peer reviewed.
  - It has metadata errors. Its reference list names Jiaming Liu as first author of C2C (actually Tianyu Fu) and Zhenyu Wang as first author of LatentMAS (actually Jiaru Zou). Its alignment table puts Ramesh and Li in the same-model, no-alignment group and C2C among learned projections for homogeneous backbones; both conflict with the primary papers. Cite it only for its taxonomy, never for details of a method.
  - The arXiv abstract on the abs page is the older v1-era text; the v3 PDF has a revised abstract, and the PDF title uses different capitalization. Neither change is substantive.
  - Work a reviewer might raise against a novelty claim:
    - Chen et al., "The Five Ws of Multi-Agent Communication" (TMLR 2026; arXiv:2602.11583), another communication survey. I saw only the citation, not the paper.
    - Cheng, Das, and Ramnath, arXiv:2608.04893, a causal audit of relayed KV caches. Now reviewed in full and entered as cheng2026audit; see the entry at the end of this file. Its own concurrent-work note also cites Zhang and Emu, arXiv:2607.26773, a similar audit of LatentMAS that I have not read.
    - arXiv:2605.28214, on latent attacks in latent-based multi-agent systems. Seen as a title only.
    - An anonymous ICLR 2027 submission titled "Safety of Latent Communication in Multi-Agent Systems". Seen as a title only; it is under review.
- Bib: @misc with the exact title from the arXiv abs page; {LLM} is brace-protected.

### mostik2026bridge (MOSTIK; industry note, proposed key)
- Source: https://mostik.ai/ and https://mostik.ai/read-more, fetched 2026-10-03. Neither page shows a date. The read-more page says the company is coming out of stealth. The site's HTML metadata gives a publish time of Sep 11, 2026, 22:17 UTC. The page links to a WIRED article by Will Knight (AI Lab newsletter, dated 2026-09-02) as the first outside account.
- Retraction: not applicable.
- What is claimed. Only the first item is quoted; the rest are paraphrased from read-more:
  - Method: "One model hands its hidden states to another through a small trained bridge" — section What we built. Both models stay frozen and only the bridge is trained. No text passes between them. The company name is Russian for little bridge.
  - Models: the sender is GLM-5.2 (753B) and the receiver is Qwen-3.5 (4B) (section The first result).
  - Numbers as claimed, with no benchmark named:
    - With the bridge, the small model closes 50% of the score gap to the large model. The page calls this a 25% lift in the small model's own accuracy.
    - On harder subsets the uplift reaches 2×.
    - The bridged pair is said to cost 2.5× less compute than a mid-sized model scoring the same.
    - Latent hand-off beats text hand-off at every level of large-model compute tested, by up to 10 percentage points, most when the hand-off comes before the large model writes anything.
    - The page also claims a Pareto improvement over other ways of combining models, without saying which.
  - Not stated anywhere on the pages: benchmarks or datasets, number of runs, variance, the identity of the baselines, or the bridge's architecture, size, or training data.
  - Geometry claims:
    - Alignment between models does not grow on its own as models get more capable, so a bridge has to be built.
    - Some alignment exists and varies in predictable ways.
    - Freezing both models is presented as a strict test, so the bridge must exploit structure the two models already shared despite different teams and training data.
    - This fits the partial, local framing of 3C, but none of it can be verified.
  - Other claims: a team of 15 (12 PhDs and a Fields Medalist), founded four months before the announcement, backed by General Catalyst, Foundation Capital, and others. The homepage lists former employers: Google X, NVIDIA, Perplexity, FAR.AI. Uses for observability, distillation, and specialization are described as early.
- Press (WIRED, 2026-09-02, paraphrased):
  - People: CEO Sasha Malysheva, credited with developing the approach; chief scientist Stanislav Smirnov (University of Geneva; 2010 Fields Medal).
  - The same GLM-5.2→Qwen-3.5 bridge is reported as performing halfway between the two models at about one-twentieth of the full GLM model's cost.
  - It mentions an undisclosed entry in the ARC-AGI-3 competition.
  - It quotes two people described as familiar with the team; this is not an independent evaluation.
  - WIRED's description of the mechanism (values in the models' weights) conflicts with the company's own (hidden states, with frozen weights).
- Public paper or code, checked 2026-10-03:
  - Nothing is linked from mostik.ai.
  - arXiv API author searches: au:Malysheva (35 records) and au:Smirnov_Stanislav (29 records; the latest is from 2023, in mathematics). None is about latent communication between models. An arXiv query for "mostik" returns 0.
  - Google Scholar returns nothing for Mostik + latent, for the GLM-5.2/Qwen-3.5 bridge, or for author:"Stanislav Smirnov" + "language models" since 2025.
  - GitHub has an organization named mostik-ai, created 2026-04-20. It is not linked from mostik.ai, so ownership is unverified. Its only public repository is a fork of an RL post-training framework (radixark/miles); it has no bridge code.
- Verdict: NARROW → footnote only. This is not evidence; do not use or repeat its numbers.
  - Proposed footnote: "An industry effort, mostik.ai, describes a trained bridge that passes a large model's hidden states to a smaller, frozen model in place of text [mostik2026bridge]. As of 3 October 2026 it has released no paper, evaluation protocol, or code, so we do not rely on its reported results."
- Bib: @misc mostik2026bridge in F_crossmodel.bib (howpublished = URL; note = company technical note, accessed 2026-10-03, no peer-reviewed results).

---

## Batch notes for 3C (how the citations fit the required framing)

- Evidence that differently trained models share structure:
  - moschella2023relative: different seeds and architectures; FastText vs Word2Vec.
  - maiorca2023translation: different pretrained encoders, and text↔image.
  - jha2025vec2vec: different text-embedding models, with no paired data.
  - ramesh2025activations: a cross-family subset only.
  - fu2026c2c: across families, but only through a fuser trained for each pair.
  - huh2024platonic and groger2026aristotelian: alignment measured between LLMs and vision models.

  Most of the mapping evidence comes from encoders and embedding models (BERT-family, ViT, CLIP, sentence encoders), not LLM hidden states. If the text says "LLM representations", lean on Huh/Gröger for measurement and on Ramesh/C2C for LLM-to-LLM transfer.
- Same-model only: zou2026latentmas, and the coordination games in Ramesh and Li. Use LatentMAS as the contrast case, not as support.
- Local and relative, not global:
  - groger2026aristotelian: global trends vanish after calibration; neighbourhoods persist.
  - huh2024platonic: a local mutual-kNN metric; alignment grows as k shrinks; peak score 0.16.
  - moschella2023relative: only angles relative to anchors are shared.
  - fu2026c2c: projection alone fails, and the mapped cache covers only part of the target space.
  - jha2025vec2vec: a learned nonlinear map, unstable for unrelated backbones.
  - Together these support "shared local and relative structure, recoverable by learned or anchored maps". They do not support one universal manifold. Do not adopt vec2vec's or Huh's universality language as a finding.
- Correlated errors: kim2025correlated and goel2025think. Both papers themselves point to representational convergence (Kim cites Jha et al.; Goel starts from Huh et al.). Neither tests that link causally, so write "consistent with", not "caused by".
- Errors through latent channels, useful for an error-accumulation review:
  - C2C: a sender can mislead the receiver, and a weak sender degrades a strong receiver.
  - LatentMAS: a debug mode for tracking intermediate errors.
  - Liu: state contamination and auditability.
  - cheng2026audit (not peer reviewed): LatentMAS's benchmark gains need not reflect example-specific content. Its receivers followed a mismatched sender's content when content mattered, which is error transmission through a latent channel. It detected no example-specific transfer through C2C's released projector, but it did not test C2C's benchmark gains.

---

## Addendum (2026-10-03): audit preprint added at coordinator request

### cheng2026audit
- Source of record: arXiv:2608.04893, https://arxiv.org/abs/2608.04893.
  - The abs page confirms the title, When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs, and the authors Jiaming Cheng, Subhransu Das, and Rajiv Ramnath.
  - v1 is from 5 Aug 2026. v2 (27 Aug 2026) is a metadata-only fix to the abstract formatting.
  - Subjects: cs.CR (primary), cs.AI, cs.LG. No journal-ref.
  - Affiliations (PDF p. 1): Cheng is an independent researcher; Das and Ramnath are at The Ohio State University. None appears on the LatentMAS or C2C author lists, so the audit is third-party.
  - Access: full text (https://arxiv.org/pdf/2608.04893v2, 26 pp.; body and Apps. A–H read; HTML also fetched).
- Peer review: none. It is an arXiv preprint: every page is headed A PREPRINT, and there is no venue or journal-ref. The authors' term pre-registered means dated internal design documents shipped with their release, not an entry in a third-party registry (App. G.2).
- Retraction: none found. Crossref has no record for the title (arXiv DOIs are registered with DataCite) and no retraction notice; the arXiv record is not withdrawn.
- Use 1 — intended claim: "An independent audit of C2C and LatentMAS finds that their benchmark gains need not reflect example-specific content passed between models; for C2C's released projector it detected no example-specific transfer."
  - Source passage: "not a claim that C2C’s reported benchmark gains are artifactual" — Sec. 5.1, last sentence.
  - The abstract states the two supporting findings (paraphrased). First, under one information-asymmetry test the delivered channels range from ceiling (LatentMAS's native relay) through partial (KVComm) to no detected example-specific transfer (C2C's released projector). Second, benchmark deltas alone do not establish that latent thoughts are transmitted. See also Fig. 3 and Apps. C.4–C.5.
  - Audit method (Sec. 3, Fig. 1; Apps. E–F):
    - Where it intervenes: at the relay boundary, on the cache only. Every arm sends the same receiver, under the same prompt, a cache of identical geometry: layer count, sequence length, dtype, position offsets, and attention mask.
    - The arms:
      - True: the example's own cache.
      - Deranged: the cache of a different example from the same batch, chosen by a fixed-point-free permutation. This keeps the overall set of caches exactly the same and changes only which query each one reaches.
      - Zero: all entries zeroed.
      - Random: Gaussian noise matched to the true cache's moments, per example, layer, and K/V tensor.
      - Intact-no-private: the sender processes a version with the private facts swapped for answer-irrelevant ones. Calibrated regime only.
      - Direct-text: the private facts are placed in the receiver's prompt. This is a validity check, explicitly not a text-channel baseline.
    - Primary estimand: the pairing effect, the true arm's accuracy minus the deranged arm's (Eq. 1).
    - Two regimes:
      - Calibrated: the receiver cannot answer without the relay. Only the sender sees a freshly generated registry of four entity–value bindings; the receiver sees a four-option query. A version written as prose paragraphs tests whether the result depends on surface form.
      - Natural: standard benchmarks the receiver can solve alone.
    - Statistics:
      - n = 500 per arm per seed, in 25 batches of 20.
      - The receiver decodes at the audited system's settings (temperature 0.6, top-p 0.95).
      - Seeds: three per cell, or five in the natural cells. The seed, not the example, is the unit of inference (App. A).
      - Natural cells: two one-sided tests (TOST) for equivalence within ±2.8 points. The margin equals LatentMAS's own reported aggregate gain over its text-based baseline. Holm correction is applied within pre-set families.
  - Systems, models, and benchmarks audited:
    - LatentMAS, the native KV prepend; the only system audited in both regimes. In LatentMAS the agents are instances of one checkpoint.
      - Calibrated regime: five checkpoints from three families: Qwen3-4B, Qwen3-8B, and Qwen3-14B; Mistral-Nemo-12B; phi-4. The prose version ran on Qwen3-8B.
      - Natural regime: GSM8K and ARC-Challenge (fixed training-split items) on Qwen3-4B, 8B, 14B and on Mistral-Nemo-12B; MedQA (test split) on Qwen3-8B. A descriptive replication used the official GSM8K test split (App. A).
    - C2C: the released Qwen2.5-7B-Instruct → Qwen3-8B projector, in the calibrated registry cell plus a prose replication; three seeds each.
    - KVComm: a Qwen3-8B port that relays 11 of 36 layers; calibrated cell only.
    - Llama-3.2-3B: the LatentMAS relay could not be consumed under either delivered realignment setting, so the authors call it a portability boundary, not an audit result (App. E.6).
    - A bolt-on latent-prefix control: Qwen3-8B drafts fed to a Qwen3-4B critic (App. E.4).
  - Results:
    - LatentMAS, calibrated, Qwen3-8B: the true arm scores 500/500 in every seed; the intact arm scores 117–126/500. The true-minus-intact gap is about +75 points, and it replicates in every family tested (Sec. 4.1, Table 1).
    - LatentMAS, natural: all seven Qwen3 cells are equivalent to zero pairing effect within ±2.8 points (Sec. 4.2, Table 2).
      - One cell shows a small detected advantage (+1.52 points, Qwen3-4B GSM8K).
      - On Mistral-Nemo-12B there is no detected advantage, but equivalence is not established.
      - On MedQA, true minus zero is +14.7 points, while true minus deranged is only +0.4 (90% CI −1.34 to +2.14). A large effect from receiving a cache need not come from which example's cache it is.
    - C2C, calibrated (Sec. 5.1): true 114–117/500, deranged 104–126, intact 99–113, zero 26–35, direct-text 498–500.
      - True minus deranged is +2.0, +0.6, and −1.8 points across seeds: mixed in sign, so no example-specific transfer is detected.
      - The prose replication gives −0.2, −0.2, and +2.6 points (Holm p = .91; App. C.4, Table 7).
    - KVComm, calibrated: transfer is detected but far below ceiling (true minus deranged +7.2 to +10.8 points; Sec. 5.2).
  - Scope and caveats stated by the authors:
    - Sec. 6, Scope: the audit bounds only the value of which example's cache is relayed. It gives no verdict on latent versus text. The calibrated cells rule out the reading that relayed caches carry nothing.
    - Sec. 6, Limitations:
      - Each external system is audited in one released configuration only.
      - The calibrated regime uses one registry construction; the prose cell partly addresses this.
      - Absolute accuracies in some cells cannot be interpreted directly; within-cell contrasts remain valid.
    - App. C.5:
      - C2C's paper shows the audited pair only as one untabulated point in a model-size scaling figure, so the cell makes no contact with any tabulated C2C gain.
      - The ceiling / partial / none-detected reading is not a capacity ranking of the three architectures.
      - The C2C and KVComm cells claim detection only, never equivalence.
    - App. F.2: only three of LatentMAS's nine benchmarks could support n = 500. AIME, GPQA-Diamond, HumanEval+, and MBPP+ remain unmeasured for the pairing term.
    - App. E.2: the estimand is the pairing value of the whole relayed cache. The authors deliberately do not call it latent-thought transfer.
    - Sec. 4.2: the natural GSM8K and ARC items come from training splits. The authors argue that memorization would push toward the null they report, and the official-test replication matches it.
  - Verdict: NARROW.
    - The C2C half is accurate as scoped: no example-specific transfer was detected for the released Qwen2.5-7B-Instruct→Qwen3-8B projector, on synthetic information-asymmetry tasks, at detection level.
    - The benchmark-gain half holds for LatentMAS only. This paper never tests C2C on standard benchmarks, and explicitly says its result is not a claim about C2C's reported gains.
    - In LatentMAS the content passes between agents that are copies of one checkpoint, not between different models.
    - Safe wording: "A preprint audit that swaps relayed KV caches between examples found that LatentMAS's gains on GSM8K, ARC-Challenge, and MedQA did not depend on which example's cache was relayed (equivalent to zero within ±2.8 points on Qwen3 models). The same relay carries private information at ceiling when the receiver needs it. For C2C's released Qwen2.5-7B→Qwen3-8B projector, the audit detected no example-specific transfer on a synthetic information-asymmetry task; it did not test C2C's reported benchmark gains [cheng2026audit]."
- Other findings a reviewer would expect:
  - Receivers follow mismatched content (Sec. 4.1; App. C.2). Under deranged relays in the calibrated cells, 64.2–64.8% of answers match the donor example's label, against 20.8–23.4% under the matched control. The receiver acts on relayed content even when it is wrong. This is direct evidence that errors propagate through a latent channel, and it suits the error-accumulation framing of the review.
  - The effect of receiving any cache varies sharply by receiver (App. D.1). On the natural tasks, true minus zero ranges from −7.5 to +78.1 points while the pairing term stays near zero. At Qwen3-4B, the relayed setup scores below the receiver working alone.
  - Bolt-on control (App. E.4): prepending latent vectors damages the critic whatever their content. Net corrections are −36 (hidden payload), −46 (shuffled), and −46 (random tokens), against +1 with no injection.
  - Concurrent work: Zhang and Emu (arXiv:2607.26773) audit LatentMAS's relay with similar message replacements and reach the same motivating conclusion. Cited in this paper; not read here.
  - Released artifacts: the audit harness, the generator for the calibration tasks, and per-example raw ledgers (App. G.3).
- Bib: @misc cheng2026audit in F_crossmodel.bib. Title and authors are taken from the arXiv abs page. {A}, {KV}, and {LLMs} are brace-protected against IEEEtran sentence-casing.
