# Humanization log 2: `main_humanized2.tex`

- **Source:** `main.tex`, not modified. Its md5 is `69833612143d821108e41997f0ed9ca1`, unchanged throughout the pass. **Output:** `main_humanized2.tex`. **Date:** 2026-10-03.
- **Procedure:** this is the final texture pass after the citation audit. The `telegrapher-style-profile` final-pass checklist governs, with its style guide; the generic `humanization` skill applies where neither speaks.
  - Every edit is a literal OLD→NEW replacement. Each OLD string occurs exactly once in `main.tex`, and the output is `main.tex` with exactly the 74 replacements below.
  - Before finalizing, I read the three audit reports in `audits/` against every edited sentence. Two candidate edits would have undone wording the auditor chose, so I dropped them (see "Dropped after reading the audit").
- **Weighting:**
  - Heaviest: Appendix B, with 42 of the 74 edits.
  - Next: the sentences the audit lengthened.
  - Light elsewhere. Paragraphs that already read well were left alone: the Introduction, II-A/B, III-C/D, IV-B, IV-C, V-C, VI-A ¶3, VI-B ¶3, VII-A and VII-D, most of VIII and IX, the Conclusion, and most of Appendix A.
- **Frozen and untouched:**
  - everything from the preamble through `\maketitle`, including the title, authors, abstract, and keywords;
  - all equations, tables, captions, and the figure;
  - the three itemized lists and every heading;
  - the footnote, the Acknowledgment, and the biographies.

## Summary

| | Before | After |
|---|---|---|
| Words, raw whitespace tokens (whole file) | 13,568 | 13,535 (−33, −0.24%) |
| Words, detexed (whole file) | 13,300 | 13,267 (−0.25%) |
| Words, prose outside frozen blocks | 11,211 | 11,178 (−0.29%) |
| Body sentences | 412 | 475 |
| Mean sentence length (words) | 27.7 | 24.0 |
| Sentences over 45 words (body / Appendix B) | 62 / 27 | 15 / 4 |
| Semicolons | 114 | 80 (none added) |
| Em-dash tokens `---` | 3 (two uses) | 3 (none added) |
| Sentence-initial But / Yet / So / And / Nor | 1 / 0 / 0 / 2 / 1 | 2 / 1 / 1 / 2 / 1 |

**Edits by primary rule (74):** T1 50 · Pass 2a 11 · C3 4 · C4 4 · C2 2 · T8 2 · T5 1.

**Secondary tags:** C2 22, mostly a semicolon or colon removed by a split. Also T1 8 and C3 6, plus one each of T3, T5, C4, and Pass 2a.

**By area:** Appendix B has 42 edits (−19 words). The main text and Appendix A have 32 (−14 words).

**Length.** The aim was 1–3% shorter. The pass reached about 0.25–0.3%.
- Most of the work was splitting sentences, which does not change length.
- Almost every other cut I looked for would have touched something protected:
  - a hedge-list word, including inside a longer word ("different" contains "if", "linearly" contains "nearly", "cannot" and "candidate" contain "can");
  - a number, a name, or a setting phrase;
  - or a clause whose wording the audit fixed.
- The filler that was cut:
  - "which is", "Now", "while it is being generated";
  - "the argument of this review", "the question of this review", "the setting of this review";
  - "how many of the steps", a doubled "from", a relative "that";
  - conjunctions dropped at splits.

## (a) Invariant checks

The checks are scripted (`check.py`, in the session scratchpad, not in the project folder) and compare `main.tex` with `main_humanized2.tex`. **All pass.**

| # | Check | Result |
|---|---|---|
| 1 | `\cite` commands (options and keys) identical and in order | PASS: 228 = 228 commands, 243 = 243 keys |
| 1 | Words immediately before each `\cite` (attachment review) | Changed for 6 of 228. Five are the deliberate author-as-subject moves (E42, E48, E52, E60, E72). The sixth is E61, a fronted setting phrase; the four words before its citation ("and rejected it decisively") are unchanged. No citation left its clause. |
| 2 | Multiset of digit numbers | PASS: 654 = 654 tokens |
| 2 | Multiset of number words (one, two, ... first, single, half, both, once, ...) | PASS: 319 = 319 |
| 3 | Sequences of `\ref`, `\eqref`, and `\label` | PASS: 77 / 17 / 25 in the same order. The combined `\ref` + `\eqref` order is also identical (94). |
| 3 | `\footnote` content | PASS (1) |
| 3 | Frozen blocks byte-identical: the preamble through `\maketitle`, the abstract and keywords, every `table`, `table*`, `tabular`, `figure`, `equation`, and `itemize`, the 7 captions, the 44 headings, and everything from the Acknowledgment to the end | PASS |
| 3 | `\emph` sequence; multiset of inline math | PASS: 38; 151 |
| 4 | Hedge and scope words: 31 phrases, case-insensitive, counted as whole words and as substrings | PASS: all 31 identical (table below) |
| 5 | Proper names kept; multiset of model and dataset tokens (those with digits or internal capitals); named setting phrases | PASS: no name lost; token multiset identical; all 10 setting phrases checked are present ("on PG-19 books", "for a gpt-4o function-calling agent", "On the retail domain of $\tau$-bench", "Gemini 1.5 Flash", "Llama-3.3-70B", "In a controlled study", "in a stylized model", "in its reported run", "in the authors' single-run comparison", "in work its authors call preliminary") |
| 6 | No new British spellings | PASS |
| 7 | Total words did not grow | PASS: −33 raw (−0.24%) |
| 8 | Em-dashes and semicolons not increased; no "Moreover", "Furthermore", "Notably", "Importantly", or enthusiasm adverbs added | PASS: em-dashes 3 → 3; semicolons 114 → 80; none added |

Hedge counts:

| Phrase | Whole-word (before → after) | Substring (before → after) |
|---|---|---|
| about | 49 → 49 | 49 → 49 |
| roughly | 6 → 6 | 6 → 6 |
| nearly | 1 → 1 | 5 → 5 |
| most | 31 → 31 | 45 → 45 |
| mostly | 10 → 10 | 10 → 10 |
| often | 25 → 25 | 25 → 25 |
| usually | 8 → 8 | 8 → 8 |
| some | 19 → 19 | 23 → 23 |
| one model | 12 → 12 | 12 → 12 |
| in one | 4 → 4 | 9 → 9 |
| on our reading | 10 → 10 | 10 → 10 |
| on our calculation | 1 → 1 | 1 → 1 |
| we found no | 5 → 5 | 5 → 5 |
| we are not aware | 1 → 1 | 1 → 1 |
| suggests | 3 → 3 | 3 → 3 |
| may | 1 → 1 | 1 → 1 |
| can | 44 → 44 | 60 → 60 |
| could | 7 → 7 | 7 → 7 |
| although | 18 → 18 | 18 → 18 |
| only | 41 → 41 | 41 → 41 |
| at least | 7 → 7 | 7 → 7 |
| in the authors' | 1 → 1 | 1 → 1 |
| preprint | 6 → 6 | 6 → 6 |
| preliminary | 1 → 1 | 1 → 1 |
| in a diagnostic study | 1 → 1 | 1 → 1 |
| in an idealized setting | 1 → 1 | 1 → 1 |
| if | 23 → 23 | 155 → 155 |
| when | 48 → 48 | 51 → 51 |
| unless | 1 → 1 | 1 → 1 |
| at a two-way decision | 3 → 3 | 3 → 3 |
| consistent with | 1 → 1 | 1 → 1 |

## (b) Build check

I copied the folder to `scratchpad/h2build/` and built `main.tex` and `main_humanized2.tex` side by side, each with pdflatex → bibtex → pdflatex → pdflatex (MiKTeX). Nothing was built in the project folder.

| | `main.tex` | `main_humanized2.tex` |
|---|---|---|
| Exit code, every step | 0 | 0 |
| Pages | 21 | 21 |
| `!` errors | 0 | 0 |
| Undefined citations or references | 0 | 0 |
| bibtex warnings / bibitems | 0 / 156 | 0 / 156 |
| Overfull / underfull boxes | 45 / 29 | 45 / 30 |
| Other warnings | 20× the template's font-shape warning `T1/formata/m/sl` | the same 20, plus one "Label(s) may have changed" after the prescribed sequence; a fourth pdflatex pass clears it (0 LaTeX warnings) |

## (c) Edits

For each edit:
- **Header line:** the edit ID, the section, the paragraph's opening words as they read in `main.tex`, the rule, and the change in word count.
- **Before / After:** the exact strings that were replaced.

**E01** · II-C How the Evidence Was Checked · ¶ "Every cited result was read in the full text…" · **C3** · ±0 words

- Before: `For each citing sentence, a ledger records the supporting passage, its location in the source, and the setting in which the result holds: the models, data, and task.`
- After: `The ledger records, for each citing sentence, the supporting passage, its location in the source, and the setting in which the result holds: the models, data, and task.`
- Why: Breaks the double "For a few works, ... / For each citing sentence, ..." opening, and uses "The ledger", since the paragraph's first sentence has already introduced it.

**E02** · II-D Relation to Existing Reviews · ¶ "Recent reviews each cover one of the mechanisms…" · **Pass 2a** · -2 words

- Before: `compose into the probability that a long output is correct, which is the question this review is organized around.`
- After: `compose into the probability that a long output is correct, the question this review is organized around.`
- Why: Cuts "which is" and leaves an appositive. -2 words.

**E03** · III-A The Uniform Model · ¶ "Independence is the subtler of the two…" · **C2** · ±0 words

- Before: `that rate overstates the risk at a position whose prefix is still correct, and, when the rate is the same at every position,`
- After: `that rate overstates the risk at a position whose prefix is still correct, and when the rate is the same at every position,`
- Why: Removes the stumble ", and, when" by dropping one comma. The logic and the "when" condition are unchanged.

**E04** · III-B The Two-Rate Model · ¶ "Now suppose instead that a small set of k positions…" · **Pass 2a** · -1 word

- Before: `Now suppose instead that a small set of $k$ positions`
- After: `Suppose instead that a small set of $k$ positions`
- Why: "Now" duplicates the subsection break and "instead". -1 word.

**E05** · IV-A Evidence · ¶ "The most direct evidence asks which predictions need distant context…" · **T1 (+C2)** · ±0 words

- Before: `gained essentially nothing in overall perplexity from context more than 2K tokens back; the gains, mainly in the Routing Transformer,`
- After: `gained essentially nothing in overall perplexity from context more than 2K tokens back. The gains, mainly in the Routing Transformer,`
- Why: Splits a 61-word sentence at its semicolon. The second sentence opens on the anaphor "The gains", and sun2021longrange still closes the two-sentence description of the same study.

**E06** · IV-A Evidence · ¶ "The most direct evidence asks which predictions need distant context…" · **T1** · ±0 words

- Before: `ask the converse question for positions a model already predicts correctly and confidently: for 75--80\% of them,`
- After: `ask the converse question for positions a model already predicts correctly and confidently. For 75--80\% of them,`
- Why: Splits a 49-word sentence at its colon. The citation stays on "Vakilian et al." (author as subject), so it covers both sentences.

**E07** · IV-A Evidence · ¶ "A second line of work measures attention…" · **T1** · ±0 words

- Before: `approaches full attention once $k$ is in the low hundreds, which lets 8B-parameter models serve`
- After: `approaches full attention once $k$ is in the low hundreds. This lets 8B-parameter models serve`
- Why: Splits a 54-word sentence. The "which lets" clause becomes "This lets ...", and liu2024retrieval stays at the end of the unit.

**E08** · IV-A Evidence · ¶ "A second line of work measures attention…" · **T1 (+C2)** · ±0 words

- Before: `in the authors' single-run comparison~\cite{yuan2025nsa}; it reads only a minority of positions in full but removes none.`
- After: `in the authors' single-run comparison~\cite{yuan2025nsa}. It reads only a minority of positions in full but removes none.`
- Why: The citation stays on its clause. The review's gloss ("reads only a minority ... removes none") becomes a short closing sentence.

**E09** · IV-A Evidence · ¶ "The third line removes tokens outright…" · **T1** · -1 word

- Before: `by dropping predictable tokens~\cite{jiang2023llmlingua}, and a model continually pre-trained`
- After: `by dropping predictable tokens~\cite{jiang2023llmlingua}. A model continually pre-trained`
- Why: Splits two studies that were joined by ", and" (47 words). Each keeps its own citation.

**E10** · IV-A Evidence · ¶ "The third line removes tokens outright…" · **Pass 2a** · -5 words

- Before: `Closest to the setting of this review, R-KV compresses a reasoning model's own chain of thought while it is being generated and matches`
- After: `Closest to this review's setting, R-KV compresses a reasoning model's own chain of thought during generation and matches`
- Why: "the setting of this review" becomes "this review's setting", and "while it is being generated" becomes "during generation". -5 words. The clause before cai2025rkv is unchanged.

**E11** · V-A Evidence · ¶ "The cleanest evidence comes from re-sampling…" · **T1 (+C2)** · ±0 words

- Before: `at which the outcome shifts abruptly; such shifts appeared in up to 63\% of examples`
- After: `at which the outcome shifts abruptly. Such shifts appeared in up to 63\% of examples`
- Why: Splits a 48-word sentence. The citation sits on "Bigelow et al." (author as subject), so it covers the second sentence too. The Lin et al. sentence that follows keeps its semicolon, so the two reports do not mirror each other.

**E12** · V-A Evidence · ¶ "Generation-time entropy is sharply skewed…" · **T1 (+C2)** · ±0 words

- Before: `locates the earliest erroneous step; most first errors fall in the opening steps,`
- After: `locates the earliest erroneous step. Most first errors fall in the opening steps,`
- Why: Splits a 49-word, three-clause sentence (the audit's caveat and the 30% set-aside). The first sentence describes the annotation, and zheng2025processbench closes the findings sentence. Every condition is kept.

**E13** · V-A Evidence · ¶ "Acting on these points helps…" · **T1 (+T3)** · ±0 words

- Before: `while running faster than uniform beam search~\cite{li2025egb}; on our reading of the paper's own results table, though,`
- After: `while running faster than uniform beam search~\cite{li2025egb}. On our reading of the paper's own results table, though,`
- Why: Splits a 49-word sentence. The citation stays on its clause, and the "On our reading ... though" gloss becomes its own sentence. The hedge stands at the front of its sentence.

**E14** · V-B Limits · ¶ "Uncertainty does not find every hard decision…" · **T1 (+C3)** · -1 word

- Before: `go wrong on later tokens~\cite{yeom2026commit}; and in 500 one-sentence answers from one model,`
- After: `go wrong on later tokens~\cite{yeom2026commit}. Across 500 one-sentence answers from one model,`
- Why: Splits a 73-word sentence at "; and". Both halves keep their own yeom2026commit citation. "in" becomes "Across", so the paragraph does not open three sentences in a row with "In ..." (the audit's "In one worked example" opening stays as written). -1 word.

**E15** · V-B Limits · ¶ "Some failures are spread out…" · **T1** · +1 word

- Before: `although in most of these the advantage lay within statistical uncertainty, while in 9 the predictive signal kept growing to the end~\cite{thoria2026fail}.`
- After: `although in most of these the advantage lay within statistical uncertainty. In the remaining 9, the predictive signal kept growing to the end~\cite{thoria2026fail}.`
- Why: The audit's hedge left an "although ..., while in 9 ..." chain. The hedge now ends the first sentence, and "In the remaining 9" (14 + 9 = 23) opens the second, which keeps thoria2026fail. +1 word.

**E16** · V-B Limits · ¶ "Some failures are spread out…" · **T1 (+C2)** · ±0 words

- Before: `that such a heuristic can find~\cite{candussio2026demyst}; the study concerns where task information sits,`
- After: `that such a heuristic can find~\cite{candussio2026demyst}. That study concerns where task information sits,`
- Why: The citation stays on its clause. The review's scope note becomes its own sentence. "That study" avoids two consecutive "The ... study" openings.

**E17** · VI-A Dependence Within One Answer · ¶ "The worry that errors compound is older…" · **T1 (+C2)** · ±0 words

- Before: `usually support it with false claims; yet when each false claim is put to the same model in a fresh session,`
- After: `usually support it with false claims. Yet when each false claim is put to the same model in a fresh session,`
- Why: Splits a 64-word sentence at "; yet". The second sentence opens on the anaphor "each false claim", and zhang2024snowball still closes the unit.

**E18** · VI-A Dependence Within One Answer · ¶ "For models without trained reasoning…" · **T1 (+C3)** · -1 word

- Before: `from $-11.2$ to $+4.4$ points~\cite{kumar2025score}, and reinforcement learning with rewards that checked only final answers produced reasoning`
- After: `from $-11.2$ to $+4.4$ points~\cite{kumar2025score}. With rewards that checked only final answers, reinforcement learning produced reasoning`
- Why: Splits two studies joined by ", and" (48 words), and fronts the reward condition so the next sentence does not also open with "...reinforcement learning". Each citation stays with its clause. -1 word.

**E19** · VI-A Dependence Within One Answer · ¶ "For models without trained reasoning…" · **T1** · ±0 words

- Before: `Finding the error is the harder half: language models located the first logical mistake`
- After: `Finding the error is the harder half. Language models located the first logical mistake`
- Why: The review's framing becomes a seven-word sentence. The 41-word evidence sentence that follows keeps tyen2024llms whole.

**E20** · VI-B Structure of Internal Representations · ¶ "Several lines of work find that models organize information…" · **T1 (+C2)** · ±0 words

- Before: `align with the source of the data~\cite{li2025unraveling}; a statistical test on the input-embedding spaces`
- After: `align with the source of the data~\cite{li2025unraveling}. A statistical test on the input-embedding spaces`
- Why: Splits a 75-word sentence at its semicolon. The two studies keep their own citations.

**E21** · VI-B Structure of Internal Representations · ¶ "Internal states also carry information about errors…" · **T1** · -1 word

- Before: `predicts whether that chunk's intermediate answer is correct, and used as an early-exit test on one model it cut generated tokens`
- After: `predicts whether that chunk's intermediate answer is correct. Used as an early-exit test on one model, it cut generated tokens`
- Why: The run-on "..., and used as an early-exit test on one model it cut ..." becomes two sentences. The second opens on the participle and refers back with "it", and zhang2025reasoningprobe still closes the unit. "one model" is kept. -1 word.

**E22** · VI-B Structure of Internal Representations · ¶ "Internal states also carry information about errors…" · **Pass 2a (+T1)** · +1 word

- Before: `In the Qwen-3 family, the 14B model, and in nascent form the 4B and 8B models, have internal features that represent a word before it is generated and shape the token that precedes it, while the smallest models seldom have such features; even at 14B, planning more than a token ahead is rare~\cite{hanna2026planning}.`
- After: `In the Qwen-3 family, the 14B model has internal features that represent a word before it is generated and shape the token that precedes it, as do the 4B and 8B models in nascent form. The smallest models seldom have such features, and even at 14B, planning more than a token ahead is rare~\cite{hanna2026planning}.`
- Why: The audit-lengthened subject ("the 14B model, and in nascent form the 4B and 8B models, have") broke the verb away from its subject. Now: the 14B model has the features, as do the 4B and 8B models in nascent form. Then a separate sentence on the smallest models and the 14B planning caveat, which keeps the citation. Every scope phrase is kept. +1 word.

**E23** · VI-C Shared Structure Across Models · ¶ "Whether this structure belongs to one model's training…" · **T1 (+C3)** · -1 word

- Before: `paired samples~\cite{maiorca2023translation}, and the embedding spaces of different text-embedding models can be translated without any paired data, although training`
- After: `paired samples~\cite{maiorca2023translation}. Without any paired data, the embedding spaces of different text-embedding models can be translated, although training`
- Why: Splits two studies joined by ", and" (49 words). The second fronts its condition ("Without any paired data"), so the paragraph does not open two sentences in a row with "The ... spaces". The clause before jha2025vec2vec is unchanged. -1 word.

**E24** · VI-C Shared Structure Across Models · ¶ "Most of this mapping evidence concerns encoders…" · **T1** · ±0 words

- Before: `over paired data~\cite{huh2024platonic}, but once similarity scores are corrected for model width and depth, apparent global convergence`
- After: `over paired data~\cite{huh2024platonic}. Once similarity scores are corrected for model width and depth, however, apparent global convergence`
- Why: Splits two studies joined by ", but" (48 words). The contrast moves to a mid-sentence "however", which saves the paper's second "But" opening for the split in Section VIII. Each study keeps its citation.

**E25** · VI-C Shared Structure Across Models · ¶ "Most of this mapping evidence concerns encoders…" · **T1 (+C2)** · -1 word

- Before: `These results come with cautions: in the fuser's own ablation, pairing the receiver with a copy of itself already gave 70--90\% of the improvement that a different model gave over a fine-tuned receiver alone, although the authors read the remaining margin as the other model's contribution~\cite{fu2026c2c}; latent collaboration between agents that are all copies of one model~\cite{zou2026latentmas} says nothing about different models; and the audit cited above detected no example-specific transfer through one released cross-model projector on a synthetic task, a detection-level result that does not test that system's reported gains~\cite{cheng2026audit}.`
- After: `These results come with cautions. In the fuser's own ablation, pairing the receiver with a copy of itself already gave 70--90\% of the improvement that a different model gave over a fine-tuned receiver alone, although the authors read the remaining margin as the other model's contribution~\cite{fu2026c2c}. Latent collaboration between agents that are all copies of one model~\cite{zou2026latentmas} says nothing about different models. The audit cited above detected no example-specific transfer through one released cross-model projector on a synthetic task, a detection-level result that does not test that system's reported gains~\cite{cheng2026audit}.`
- Why: The paper's longest sentence (91 words; a colon and two semicolons) becomes a topic sentence plus three cautions, one sentence each, each with its own citation. The "although" hedge and the detection-level caveat are kept. -1 word.

**E26** · VI-C Shared Structure Across Models · ¶ "Models also fail together…" · **T1** · -1 word

- Before: `whenever inputs differ in how hard they are~\cite{eckhardt1985theoretical}, and an experiment with 27 independently written versions`
- After: `whenever inputs differ in how hard they are~\cite{eckhardt1985theoretical}. An experiment with 27 independently written versions`
- Why: Splits a model and an experiment that were joined by ", and" (53 words). Each keeps its citation. -1 word.

**E27** · VI-D Limits and What This Means for the Model · ¶ "Within these limits, dependence cuts both ways…" · **T1** · -1 word

- Before: `correlated wrong answers limit what voting can recover: a vote helps only at decisions where the correct answer is the model's most likely single answer, which at a two-way decision means being right more often than not, and wrong answers that agree with each other defeat it`
- After: `correlated wrong answers limit what voting can recover. A vote helps only at decisions where the correct answer is the model's most likely single answer, which at a two-way decision means being right more often than not. Wrong answers that agree with each other defeat it`
- Why: A 53-word sentence becomes three: the claim, the condition (with "at a two-way decision" intact), and a short close. It no longer mirrors the matching sentence in Section VIII ("But voting recovers accuracy only where ..."). -1 word.

**E28** · VII-B Token-Level and Step-Level Decay · ¶ "Agent evaluations seem to contradict…" · **Pass 2a** · -2 words

- Before: `Agent evaluations seem to contradict the argument of this review.`
- After: `Agent evaluations seem to contradict this review's argument.`
- Why: "the argument of this review" becomes "this review's argument". "seem" is kept. -2 words.

**E29** · VIII Implications for System Design · ¶ "Diversify ensembles, and verify rather than vote…" · **T1 (+C3)** · ±0 words

- Before: `without retraining~\cite{wang2023self}, but voting recovers accuracy only where`
- After: `without retraining~\cite{wang2023self}. But voting recovers accuracy only where`
- Why: Splits a 60-word sentence. The PaLM result keeps wang2023self, and the review's condition starts a new sentence with "But". The paper now has two "But" openings.

**E30** · VIII Implications for System Design · ¶ "Diversify ensembles, and verify rather than vote…" · **T1** · +2 words

- Before: `Selecting among candidates with a trained selector~\cite{moshkov2025aimo}, a verifier trained on feedback about each step, which on MATH outperformed both majority voting and a verifier trained on final answers alone~\cite{lightman2024lets}, or, in a diagnostic study, a probe on the model's own activations~\cite{orgad2025know} can recover answers that a majority would miss.`
- After: `Answers that a majority would miss can be recovered by selecting among candidates with a trained selector~\cite{moshkov2025aimo}, a verifier trained on feedback about each step, which on MATH outperformed both majority voting and a verifier trained on final answers alone~\cite{lightman2024lets}, or, in a diagnostic study, a probe on the model's own activations~\cite{orgad2025know}.`
- Why: The main verb came after 45 words. Now the main clause comes first (a loose sentence) and the three selectors follow, each still attached to its own citation in the original order. "can" and "in a diagnostic study" are kept. +2 words.

**E31** · IX Open Problems · ¶ "How far do importance and hardness coincide?…" · **T8** · ±0 words

- Before: `greatest counterfactual influence on the answer~\cite{bogdan2025anchors}; we are not aware of a study`
- After: `greatest counterfactual influence on the answer~\cite{bogdan2025anchors}. We are not aware of a study`
- Why: Splits a 51-word sentence. The citation stays on its clause, and "We are not aware ..." becomes its own sentence, where the authors are visible. The hedge wording is unchanged.

**E32** · Appendix A-D Majority Voting · ¶ "where the bound is Hoeffding's inequality…" · **T1 (+C2)** · ±0 words

- Before: `but levels off below one~\cite{dietrich2023jury}; in the limit of perfectly correlated samples, voting gains nothing.`
- After: `but levels off below one~\cite{dietrich2023jury}. In the limit of perfectly correlated samples, voting gains nothing.`
- Why: Splits a 51-word sentence. dietrich2023jury stays on its clause, and the limit case becomes a short declarative, as in the earlier pass, before the audit inserted the sentence.

**E33** · Appendix B (opening) · ¶ "Five choices shape this review…" · **Pass 2a** · -1 word

- Before: `and each meets a line of work that the main text does not survey in full.`
- After: `and each meets a line of work the main text does not survey in full.`
- Why: Drops the relative "that". -1 word.

**E34** · Appendix B (opening) · ¶ "Five choices shape this review…" · **T1 (+C2)** · -1 word

- Before: `The review judges reliability on the whole answer and counts as errors only wrong commitments; it treats the failure of an answer as a composition of risks at single positions; it uses importance and hardness as two handles on those positions; it asks what dependence across samples and models does to voting; and it treats the structure of internal representations as a candidate explanation for that dependence.`
- After: `The review judges reliability on the whole answer and counts as errors only wrong commitments. It treats the failure of an answer as a composition of risks at single positions, and uses importance and hardness as two handles on those positions. It asks what dependence across samples and models does to voting, and treats the structure of internal representations as a candidate explanation for that dependence.`
- Why: A 67-word chain of four semicolons ("...; it treats ...; it uses ...; it asks ...; and it treats ...") becomes three sentences. The pairs that belong together (positions and their handles; dependence and its explanation) share a sentence. All five choices are kept, in order. -1 word.

**E35** · Appendix B (opening) · ¶ "Five choices shape this review…" · **Pass 2a** · -2 words

- Before: `and where the question of this review differs.`
- After: `and where this review's question differs.`
- Why: "the question of this review" becomes "this review's question". -2 words.

**E36** · B-A Compounding Error and Recovery · ¶ "The compounding argument is older than language models…" · **T1 (+C2)** · ±0 words

- Before: `because one mistake can take it to states the expert never visited; Ross and Bagnell show`
- After: `because one mistake can take it to states the expert never visited. Ross and Bagnell show`
- Why: Splits a 60-word sentence. The bound is stated, then attributed in a short sentence with the authors as subject and the citation ("Ross and Bagnell show that this bound is tight").

**E37** · B-A Compounding Error and Recovery · ¶ "The compounding argument is older than language models…" · **T1 (+C2)** · ±0 words

- Before: `is the most a single wrong action can raise the cost; the bound is linear in $T$ when $u$ stays bounded,`
- After: `is the most a single wrong action can raise the cost. The bound is linear in $T$ when $u$ stays bounded,`
- Why: Splits a 66-word sentence at its semicolon. "The bound" refers back, and ross2011dagger still closes the description. The "when ... as when" conditions are kept.

**E38** · B-A Compounding Error and Recovery · ¶ "The compounding argument is older than language models…" · **T1 (+Pass 2a)** · ±0 words

- Before: `quadratic growth is not inevitable either: when the expert lies in the policy class, the range of the total reward does not grow with the horizon (as when only the final outcome is scored), and neither does the complexity of the class, the sample complexity of behavior cloning can be independent of $T$; for stochastic experts`
- After: `quadratic growth is not inevitable either. The sample complexity of behavior cloning can be independent of $T$ when the expert lies in the policy class, the range of the total reward does not grow with the horizon (as when only the final outcome is scored), and neither does the complexity of the class; for stochastic experts`
- Why: In the 81-word sentence, three conditions came before the result, and the end of the conditions ("..., and neither does the complexity of the class, the sample complexity ...") read as an apposition. Now the framing claim is its own sentence and the result comes before its conditions. All three conditions, the parenthesis, "can", and the semicolon-joined worst-case result with foster2024behavior are kept.

**E39** · B-A Compounding Error and Recovery · ¶ "The compounding argument is older than language models…" · **Pass 2a** · -1 word

- Before: `comes from the absence of recovery rather than from uniform risk.`
- After: `comes from the absence of recovery rather than uniform risk.`
- Why: Drops the repeated "from". "On our reading" is kept. -1 word.

**E40** · B-A Compounding Error and Recovery · ¶ "The compounding argument is older than language models…" · **T1 (+C2)** · ±0 words

- Before: `and one mistake there decides the episode~\cite{ross2010efficient}; in K\"a\"ari\"ainen's`
- After: `and one mistake there decides the episode~\cite{ross2010efficient}. In K\"a\"ari\"ainen's`
- Why: Splits two examples, each with its own citation. The parallel "In the example ... / In Kaariainen's example ..." is deliberate, since "Both lock in" closes it.

**E41** · B-A Compounding Error and Recovery · ¶ "Language generation inherited the argument as exposure bias…" · **T1 (+C2)** · ±0 words

- Before: `which the authors read as self-recovery; prefixes written by the model itself`
- After: `which the authors read as self-recovery. Prefixes written by the model itself`
- Why: Splits a 52-word sentence. The first sentence names He et al., and the second refers back with "their proxy metrics" and keeps the citation.

**E42** · B-A Compounding Error and Recovery · ¶ "Language generation inherited the argument as exposure bias…" · **C4 (+T1)** · ±0 words

- Before: `Repetition under greedy decoding shows the opposite tendency: in a 750M-parameter model, the more often a sentence already appears in the context, the more probable its next repetition becomes, a self-reinforcing effect that traps greedy decoding in loops; Xu et al.\ attribute the contrast with He et al.\ to the difference in decoding~\cite{xu2022loop}.`
- After: `Xu et al.~\cite{xu2022loop} found the opposite tendency under greedy decoding: in a 750M-parameter model, the more often a sentence already appears in the context, the more probable its next repetition becomes, a self-reinforcing effect that traps greedy decoding in loops. They attribute the contrast with He et al.\ to the difference in decoding.`
- Why: Author as subject, with the citation moved onto the authors at the head of their own sentence. The 53-word sentence then splits, and the second sentence ("They attribute ...") stays under the same citation. Same key, same claim. "Xu et al." and "He et al." are both kept.

**E43** · B-A Compounding Error and Recovery · ¶ "Language generation inherited the argument as exposure bias…" · **T1** · ±0 words

- Before: `conflates two phases of next-token prediction: it assumes that teacher-forced training`
- After: `conflates two phases of next-token prediction. It assumes that teacher-forced training`
- Why: Splits a 52-word sentence. The authors' thesis comes first and short, then the explanation, which keeps the citation. "can" is kept.

**E44** · B-A Compounding Error and Recovery · ¶ "Recovery is the other half of the argument…" · **T1 (+C2)** · ±0 words

- Before: `after large-scale fine-tuning~\cite{kamoi2024selfcorrect}; the trained self-correction`
- After: `after large-scale fine-tuning~\cite{kamoi2024selfcorrect}. The trained self-correction`
- Why: The citation stays on its clause. The review's chronology note becomes its own sentence.

**E45** · B-A Compounding Error and Recovery · ¶ "Recovery is the other half of the argument…" · **T1** · +1 word

- Before: `just after the model had committed to them, and pretraining on solutions with inserted errors`
- After: `just after the model had committed to them. Pretraining such models on solutions with inserted errors`
- Why: Splits a 56-word sentence. "such models" ties the second finding to the same controlled study, whose setting phrase stays intact. +1 word.

**E46** · B-A Compounding Error and Recovery (closing paragraph) · ¶ "These lines established that errors can compound…" · **C3 (+T5)** · -1 word

- Before: `These lines established that errors can compound, that compounding is not inevitable, and that recovery can be learned.`
- After: `Errors can compound, compounding is not inevitable, and recovery can be learned: these lines established that much.`
- Why: All five subsection closers opened "These lines established/measured/built ...". This one leads with the three findings and attributes them after a colon ("...: these lines established that much"), a small register shift. The claim and both "can"s are unchanged, and "They charge ..." still follows naturally. -1 word.

**E47** · B-A Compounding Error and Recovery (closing paragraph) · ¶ "These lines established that errors can compound…" · **Pass 2a** · -2 words

- Before: `The review asks instead how many of the steps are decisions,`
- After: `The review asks instead how many steps are decisions,`
- Why: "how many of the steps" becomes "how many steps". -2 words.

**E48** · B-B Finding the Positions That Matter · ¶ "Attention weights were an early candidate for importance…" · **C4 (+T1)** · ±0 words

- Before: `Wiegreffe and Pinter replied that whether attention explains a prediction depends on what counts as explanation, and that a fair counterfactual test must train an adversarial model rather than alter attention instance by instance; such trained adversaries still found very different attention at unchanged accuracy, but less easily than the per-instance search had suggested, and their weights guided a simple model poorly where the original weights guided it well~\cite{wiegreffe2019attention}.`
- After: `Wiegreffe and Pinter~\cite{wiegreffe2019attention} replied that whether attention explains a prediction depends on what counts as explanation, and that a fair counterfactual test must train an adversarial model rather than alter attention instance by instance. Such trained adversaries still found very different attention at unchanged accuracy, but less easily than the per-instance search had suggested, and their weights guided a simple model poorly where the original weights guided it well.`
- Why: Author as subject: the citation moves onto "Wiegreffe and Pinter", so it covers both halves of a 69-word sentence, which then splits at its semicolon. Same key, same claim.

**E49** · B-B Finding the Positions That Matter · ¶ "Research on uncertainty reached the hardness side…" · **T1 (+C3)** · ±0 words

- Before: `so that variation in wording is not counted as uncertainty; on free-form question answering it predicted whether an answer was correct better than entropy over the sampled sequences, with the clearest gains for the larger models~\cite{kuhn2023semantic}, and it detected confabulations across datasets and models, although`
- After: `so that variation in wording is not counted as uncertainty. On free-form question answering, it predicted whether an answer was correct better than entropy over the sampled sequences, with the clearest gains for the larger models~\cite{kuhn2023semantic}. Across datasets and models, it also detected confabulations, although`
- Why: A 75-word sentence with two citations becomes three sentences: the definition, the kuhn2023semantic result ("it" refers back), and the farquhar2024detecting result with its condition fronted ("Across datasets and models, it also ..."). Fronting the condition avoids two adjacent "It"-openings before "Its unit". The "although by its authors' account" caveat is kept.

**E50** · B-B Finding the Positions That Matter · ¶ "Research on uncertainty reached the hardness side…" · **T1 (+C2)** · ±0 words

- Before: `while hallucinations diverge~\cite{manakul2023selfcheckgpt}; on our reading, an error`
- After: `while hallucinations diverge~\cite{manakul2023selfcheckgpt}. On our reading, an error`
- Why: The citation stays on its clause. "On our reading ..." becomes its own sentence, with the hedge at the front.

**E51** · B-B Finding the Positions That Matter · ¶ "Research on uncertainty reached the hardness side…" · **T1** · -2 words

- Before: `yet account for most of its summed uncertainty, and that weighting uncertainty by relevance`
- After: `yet account for most of its summed uncertainty. Weighting uncertainty by relevance`
- Why: Splits a 60-word "found that ..., and that ..." sentence. The first sentence names Duan et al., and the second carries the "in most settings tested" and "although" qualifiers and keeps the citation. -2 words.

**E52** · B-B Finding the Positions That Matter · ¶ "Research on uncertainty reached the hardness side…" · **T1 (+C4)** · -2 words

- Before: `at both the token and the sequence level~\cite{malinin2021uncertainty}, and Kadavath et al.\ showed that large models can be well calibrated on suitably formatted multiple-choice and true/false questions, can estimate with few-shot prompting whether their own sampled answers are right, and can be trained to predict whether they know an answer, a prediction that generalized only partly to new tasks and was poorly calibrated there~\cite{kadavath2022language}.`
- After: `at both the token and the sequence level~\cite{malinin2021uncertainty}. Kadavath et al.~\cite{kadavath2022language} showed that large models can be well calibrated on suitably formatted multiple-choice and true/false questions, can estimate with few-shot prompting whether their own sampled answers are right, and can be trained to predict whether they know an answer. That prediction generalized only partly to new tasks and was poorly calibrated there.`
- Why: A 76-word sentence held two studies. Malinin and Gales keep their citation. Kadavath et al. get author-as-subject integration, with the citation moved onto the names, and the closing caveat becomes its own sentence ("That prediction generalized only partly ..."), so "only" and "poorly calibrated there" stay. -2 words.

**E53** · B-B Finding the Positions That Matter (closing paragraph) · ¶ "These lines measured importance and hardness separately…" · **T5 (+C3, T1)** · -1 word

- Before: `These lines measured importance and hardness separately and for their own ends: explanation, compression, the detection of hallucination, the selection of answers. The review treats both as handles on one quantity, the number of positions that decide an answer, and their overlap at the level of tokens is the measurement still missing`
- After: `So importance and hardness were measured separately and for their own ends: explanation, compression, the detection of hallucination, the selection of answers. The review treats both as handles on one quantity, the number of positions that decide an answer. Their overlap at the level of tokens is the measurement still missing`
- Why: A summarizing "So ..." with a passive verb replaces the "These lines measured ..." template. It is the second of the pass's two register shifts; the first is in the B-A closer. The closing ", and their overlap ..." also becomes its own sentence. The claims are unchanged. -1 word.

**E54** · B-C Uneven Cost Across Tokens · ¶ "Several lines of work assume, and exploit…" · **T1 (+C2)** · ±0 words

- Before: `which preserves the target's output distribution exactly; with drafts about a hundred times smaller,`
- After: `which preserves the target's output distribution exactly. With drafts about a hundred times smaller,`
- Why: Splits a 60-word sentence. The mechanism comes first, then the measured result, which keeps leviathan2023fast.

**E55** · B-C Uneven Cost Across Tokens · ¶ "Several lines of work assume, and exploit…" · **T1 (+C2)** · ±0 words

- Before: `with fewer operations per forward pass~\cite{raposo2024mixture}; early exit, discussed in`
- After: `with fewer operations per forward pass~\cite{raposo2024mixture}. Early exit, discussed in`
- Why: The citation stays on its clause. The early-exit cross-reference becomes its own sentence.

**E56** · B-C Uneven Cost Across Tokens · ¶ "Psycholinguistics frames the question in terms of information…" · **T1 (+C2)** · ±0 words

- Before: `spread information evenly across an utterance; Levy and Jaeger supported it`
- After: `spread information evenly across an utterance. Levy and Jaeger supported it`
- Why: The hypothesis is stated in its own sentence, and "Levy and Jaeger supported it ..." follows with the citation.

**E57** · B-C Uneven Cost Across Tokens · ¶ "Psycholinguistics frames the question in terms of information…" · **T1 (+C2)** · ±0 words

- Before: `rather than where information sits; the entropy profiles of Section~\ref{sec:hardness},`
- After: `rather than where information sits. The entropy profiles of Section~\ref{sec:hardness},`
- Why: Splits a 53-word sentence. The "On our reading" clause keeps its hedge. The factual note on entropy profiles (model outputs, not human speech) becomes its own sentence.

**E58** · B-C Uneven Cost Across Tokens · ¶ "Long inputs carry their own costs…" · **T1** · -1 word

- Before: `before reaching their claimed context length~\cite{hsieh2024ruler}, and adding irrelevant sentences`
- After: `before reaching their claimed context length~\cite{hsieh2024ruler}. Adding irrelevant sentences`
- Why: Splits two studies joined by ", and" (47 words). Each keeps its citation, and the "a precursor of ..." appositive stays with shi2023distracted. -1 word.

**E59** · B-C Uneven Cost Across Tokens (closing paragraph) · ¶ "These lines measure or exploit uneven cost…" · **C3 (+T1)** · ±0 words

- Before: `These lines measure or exploit uneven cost for efficiency, for the study of language, or for robustness, and treat the cost of a token as something to predict or to save.`
- After: `For efficiency, for the study of language, or for robustness, these lines measure or exploit uneven cost and treat the cost of a token as something to predict or to save.`
- Why: Fronts the three purposes, which breaks the "These lines ..." closer template. Same words.

**E60** · B-D Voting With Correlated Voters · ¶ "Software engineering modeled the dependence and then measured it…" · **C4 (+T1)** · ±0 words

- Before: `Eckhardt and Lee modeled independently developed versions of a program as random draws from a population of developers and showed that the versions fail independently only if every input is equally likely to defeat them; when that likelihood varies across inputs, versions fail together more often than independence predicts~\cite{eckhardt1985theoretical}.`
- After: `Eckhardt and Lee~\cite{eckhardt1985theoretical} modeled independently developed versions of a program as random draws from a population of developers and showed that the versions fail independently only if every input is equally likely to defeat them. When that likelihood varies across inputs, versions fail together more often than independence predicts.`
- Why: Author as subject, with the citation moved onto "Eckhardt and Lee". The 49-word sentence then splits, and the "When that likelihood varies ..." consequence stays under the same citation. "only if" is kept.

**E61** · B-D Voting With Correlated Voters · ¶ "Software engineering modeled the dependence and then measured it…" · **C3 (+T1)** · ±0 words

- Before: `Knight and Leveson tested the assumption with 27 versions of one program written independently and a million test cases, and rejected it decisively~\cite{knight1986experimental}.`
- After: `With 27 versions of one program written independently and a million test cases, Knight and Leveson tested the assumption and rejected it decisively~\cite{knight1986experimental}.`
- Why: Fronts the setting, so the paragraph no longer runs "Eckhardt and Lee modeled ... / Knight and Leveson tested ...". Same words, and the citation is still at the end of its clause.

**E62** · B-D Voting With Correlated Voters · ¶ "Software engineering modeled the dependence and then measured it…" · **T1** · ±0 words

- Before: `Sharing can cost even when it helps each user alone: in a stylized model`
- After: `Sharing can cost even when it helps each user alone. In a stylized model`
- Why: The framing claim becomes a short sentence. The stylized model (setting phrase intact) follows with its citation.

**E63** · B-D Voting With Correlated Voters · ¶ "Repeated sampling of language models shows the same limits…" · **T1** · ±0 words

- Before: `stopped improving after about a hundred: for one 8B model on MATH,`
- After: `stopped improving after about a hundred. For one 8B model on MATH,`
- Why: Splits a 66-word sentence. The general finding comes first, then the one-model numbers, which keep brown2024monkeys.

**E64** · B-D Voting With Correlated Voters · ¶ "Repeated sampling of language models shows the same limits…" · **T1 (+C2)** · ±0 words

- Before: `could first rise and then fall as calls were added; the authors' analysis attributes this`
- After: `could first rise and then fall as calls were added. The authors' analysis attributes this`
- Why: Splits a 69-word sentence. "The authors' analysis attributes this ..." refers back and keeps the citation.

**E65** · B-D Voting With Correlated Voters · ¶ "Repeated sampling of language models shows the same limits…" · **T1 (+C2)** · ±0 words

- Before: `for a gpt-4o function-calling agent~\cite{yao2025taubench}; had every task the same success rate,`
- After: `for a gpt-4o function-calling agent~\cite{yao2025taubench}. Had every task the same success rate,`
- Why: The citation stays with the measured result. The review's own calculation ("on our calculation") becomes its own sentence.

**E66** · B-D Voting With Correlated Voters · ¶ "Repeated sampling of language models shows the same limits…" · **Pass 2a** · ±0 words

- Before: `Decomposition pushes voting furthest: splitting a 20-disk Towers of Hanoi task into its roughly one million single-move subtasks, with the solution strategy given in every prompt, voting on each move until one answer led by three votes, and discarding overlong or misformatted outputs to reduce correlated errors, one system completed every move without error in its reported run~\cite{meyerson2025maker}.`
- After: `Decomposition pushes voting furthest: one system split a 20-disk Towers of Hanoi task into its roughly one million single-move subtasks, with the solution strategy given in every prompt, voted on each move until one answer led by three votes, discarded overlong or misformatted outputs to reduce correlated errors, and completed every move without error in its reported run~\cite{meyerson2025maker}.`
- Why: The subject came only after 45 words of participles ("splitting ..., voting ..., and discarding ..., one system completed"). Now "one system" comes first with four finite verbs. Every step, "roughly", and "in its reported run" are kept. Same word count.

**E67** · B-D Voting With Correlated Voters · ¶ "Heterogeneity changes the shape of decay…" · **C2** · ±0 words

- Before: `are fixed multiples, their frailties, of a common age schedule,`
- After: `are fixed multiples (their frailties) of a common age schedule,`
- Why: Parentheses for the nested appositive ("fixed multiples, their frailties, of ..."), which read as a list.

**E68** · B-D Voting With Correlated Voters · ¶ "Heterogeneity changes the shape of decay…" · **T1** · -1 word

- Before: `gives the pool a decreasing failure rate~\cite{proschan1963theoretical}, and with repeated sampling,`
- After: `gives the pool a decreasing failure rate~\cite{proschan1963theoretical}. With repeated sampling,`
- Why: Splits two studies joined by ", and" (54 words). Each keeps its citation, and the "when ... heavy tail" condition stays. -1 word.

**E69** · B-D Voting With Correlated Voters · ¶ "Heterogeneity changes the shape of decay…" · **T1** · -1 word

- Before: `if the spread of per-step difficulty is similar at every task length, and a mixture of exponential decays`
- After: `if the spread of per-step difficulty is similar at every task length. A mixture of exponential decays`
- Why: Splits a 56-word sentence. The hedged reading ("On our reading ... if ...") keeps its condition, and the mathematical fact about mixtures closes the paragraph on its own. -1 word.

**E70** · B-D Voting With Correlated Voters (closing paragraph) · ¶ "These lines established that a vote helps only when…" · **Pass 2a (+T1)** · -2 words

- Before: `The review applies the same condition at single decisions, where, at a two-way decision, voting helps only if $e_{\text{key}}<\tfrac12$, and it takes shared difficulty`
- After: `The review applies the same condition at single decisions: at a two-way decision, voting helps only if $e_{\text{key}}<\tfrac12$. It takes shared difficulty`
- Why: Removes the comma pile ", where, at a two-way decision, ..." with a colon, and splits off the shared-difficulty sentence. "at a two-way decision" and "only if" are kept. -2 words.

**E71** · B-E Comparing Representations Across Networks · ¶ "The mappings between models cited in Section VI rest on older tools…" · **T1** · ±0 words

- Before: `far more than with humans~\cite{geirhos2020beyond}, an ancestor of the measures of shared mistakes in Table~\ref{tab:crossmodel}.`
- After: `far more than with humans~\cite{geirhos2020beyond}. The measures of shared mistakes in Table~\ref{tab:crossmodel} descend from it.`
- Why: Two sentences in a row ended "~\cite{}, a precursor of ..." / "~\cite{}, an ancestor of ...". The second appositive becomes a short declarative of the same relation. The Table reference keeps its position after the citation. +1 word.

**E72** · B-E Comparing Representations Across Networks · ¶ "Probes for truth found signals about errors inside single models…" · **C4** · ±0 words

- Before: `Contrast-consistent search found, without labels, a direction along which a statement and its negation receive consistent probabilities, and in one model it held its accuracy when a misleading prompt lowered the accuracy of the model's own answers~\cite{burns2023discovering}.`
- After: `Contrast-consistent search~\cite{burns2023discovering} found, without labels, a direction along which a statement and its negation receive consistent probabilities, and in one model it held its accuracy when a misleading prompt lowered the accuracy of the model's own answers.`
- Why: The method named as subject carries its citation, which breaks a run of five "result~\cite{}." sentences. Same key, same claim. "in one model" is kept.

**E73** · B-E Comparing Representations Across Networks · ¶ "Probes for truth found signals about errors inside single models…" · **T1** · -1 word

- Before: `conjunction, and translation~\cite{burger2024truth}, and in one chat model, features`
- After: `conjunction, and translation~\cite{burger2024truth}. In one chat model, features`
- Why: Splits two studies joined by ", and in one chat model, ...". That phrasing could be read as part of the first study. Each keeps its citation, and "In one chat model" is kept. -1 word.

**E74** · B-E Comparing Representations Across Networks (closing paragraph) · ¶ "These lines built the tools for comparing representations…" · **T8** · -1 word

- Before: `needs both tools at once, and we found no study that asks it in that form.`
- After: `needs both tools at once. We found no study that asks it in that form.`
- Why: "We found no study ..." becomes a short closing sentence where the authors are visible. The hedge wording is unchanged. -1 word.


## Splits for the author to confirm: the citation closes a two-sentence unit

In each of these splits, no citation moved. It stays on the clause it already ended.
- **What changed:** the new first sentence states part of the same cited result without a citation of its own.
- **What links them:** the second sentence opens on an explicit link back. The links are "The gains", "This lets", "Most first errors", "In the remaining 9", "Yet when each false claim", "Used as ... it", "The smallest models seldom have such features", "this bound", "The bound", "such models", "it predicted", "With drafts", "supported it", "For one 8B model", and "The authors' analysis attributes this".

The splits, by edit and key:
- E05 `sun2021longrange`
- E07 `liu2024retrieval`
- E12 `zheng2025processbench`
- E15 `thoria2026fail`
- E17 `zhang2024snowball`
- E21 `zhang2025reasoningprobe`
- E22 `hanna2026planning`
- E36 `ross2010efficient`
- E37 `ross2011dagger`
- E38 `foster2024behavior` (the split-off sentence is the framing claim)
- E45 `ye2025physics22`
- E49 `kuhn2023semantic` (the split-off sentence is the definition)
- E54 `leviathan2023fast`
- E56 `levy2007speakers` (the split-off sentence states the hypothesis)
- E63 `brown2024monkeys`
- E64 `chen2024more`

If the house rule is that every sentence stating a third-party result carries its own citation, revert any of these. Its before-string is above.

In five other splits, the first sentence names the authors:
- E06 Vakilian (citation on the names)
- E11 Bigelow (citation on the names)
- E41 He
- E43 Bachmann and Nagarajan
- E51 Duan

In the remaining splits, either each half keeps its own citation, or the split-off part is the review's own gloss or framing ("On our reading ...", "That study concerns ...", "Finding the error is the harder half.", "Sharing can cost ...").

## Author-as-subject moves (C4)

Five citations moved onto the author or method name at the head of their own sentence, where each covers that sentence and the one after it:
- E42 `xu2022loop`
- E48 `wiegreffe2019attention`
- E52 `kadavath2022language`
- E60 `eckhardt1985theoretical`
- E72 `burns2023discovering`

In each, the key, its position in the citation sequence, and the claim are unchanged. In E52, the Kadavath caveat ("That prediction generalized only partly ...") still refers to the clause about being trained to predict whether the model knows an answer, which is what audit fix M5 requires.

## Dropped after reading the audit

I checked every edited sentence against the auditor's proposed fixes in `audits/`, and dropped these two candidates:

1. **IV-B: "Under prompt compression, some instructions came to be ignored entirely"** (`chen2026pitfalls`). I wanted "were ignored entirely" (−2 words). Not changed: the audit chose "came to be ignored" to carry the source's "degrade until completely ignored".
2. **V-B: "In one worked example, the Phi-4 report shows ..."** (`abdin2024phi4`). I wanted to move the scope phrase to mid-sentence (C3). Not changed: this is the audit's exact fix, and it puts the scope first. E14's "Across" still prevents three consecutive "In ..." openings.

In the edited sentences, every other audit fix survives word for word; only the sentence boundaries listed in each edit changed. Examples:
- M1: the three Foster conditions.
- M3: the Wiegreffe concession.
- M4: Duan's "in most settings tested ... although".
- M5: the attachment of the Kadavath caveat.
- M8: chen's "could" and "the authors' analysis attributes".
- H1: the τ-bench domain, the agent, and "on our calculation".
- The hanna three tiers (14B full, 4B–8B nascent, the smallest models seldom).
- thoria's "within statistical uncertainty".
- zheng's caveat about short solutions.

## Wanted to change, did not (would touch an invariant)

1. **II-D ¶2, "Appendix~\ref{app:adjacent} places the review against ..." (62 words).** An inline list of five items. Splitting it cleanly needs a count word ("five"), which changes the number multiset. It is also intentional structure.
2. **IV-C, "The evidence supports the first premise ... far fewer than $n$" (46 words).** Splitting at the colon leaves the next sentence's "It does not support ..." without a clear antecedent. Fixing that adds words.
3. **V-A, "The very first token can be such a position: branching over the ten most likely first tokens and then decoding greedily, the most confident path contained ..." (47 words).** The participle dangles, since the path is not what branches. A clean fix needs "when" or "if" (both on the hedge list) or new wording around `wang2024chain`.
4. **VI-A, "Across the turns of a conversation, ... although the authors attribute most of the resulting drop ..." (46 words).** A split would turn "although" into "however" or "though", which removes a hedge-list word.
5. **VI-B, "On our reading, this structure is what separates the two kinds of error ...: a slip ... while a wrong key decision ..." (50 words).** Splitting at the colon would take the mechanism outside the "On our reading" scope.
6. **VI-D Limits, "Truth representations lose separability ...~\cite{haller2025brittle}; probes that detect truthfulness also generalize ...~\cite{orgad2025know}" (49 words).** The semicolon groups two studies as one finding. If split, "Three findings limit the reading above" would read as four.
7. **VIII, "Several methods treat a minority of positions differently: ..." (46 words), and IX, "A direct test would reuse ...: fix ..., count ..., and record ..." (46 words).** Both are deliberate colon lists: VIII has a citation per item, IX a protocol per step.
8. **B-A, the Foster result sentence after E38 (about 58 words).** Two results share one citation across a semicolon. Splitting would leave the horizon-independence result without its citation. The alternative, "Foster et al.~\cite{foster2024behavior} show that ...", adds 5 words and moves the citation away from the worst-case clause.
9. **B-D ¶1, "When votes are independent only given such shared facts, ... converges to a limit below one: the probability that ..." (55 words).** Splitting at the colon needs "That limit is" (+3 words) and leaves the theorem itself without a citation. The sentence is also audit fix M7.
10. **B-D ¶3, "...~\cite{chen2024more}, the many-answer counterpart of the two sides of Table~\ref{tab:majority}."** The appositive comes after the citation. Making it a sentence adds words, and audit fix M8 placed it there.
11. **B-D ¶3, "Decomposition pushes voting furthest: one system split ..." (about 58 words even after E66).** Four steps sit under one citation. E66 moves the subject to the front. A further split would separate the method from its citation.
12. **VI-B, the repeated "even when" in "...even when the model usually generates a wrong one~\cite{orgad2025know}. A probe can locate ... even when the generated answer is wrong~\cite{gao2024insights}."** Left as is. Fronting the second condition would put "Even when" straight after "...a wrong one." The earlier pass's fronted version ("When ..., a probe can still locate ...") is also not in the current `main.tex`.
13. **II-D ¶1, "Surveys of ... / A review of ... / A review of ..."**: a templated triple that the previous pass flagged. Breaking it either reorders `zhang2026activeuq` and `liu2026latentsurvey` or adds words.
14. **B-E ¶1, lenc/bansal (45 words), and B-B ¶3, lightman/wang2024mathshepherd (45 words).** Left joined.
    - lenc/bansal: splitting gives two parallel sentences ("could be swapped ..." / "could be joined ..."), and since "could" is a hedge-list word, neither half can be reworded to break the parallel.
    - lightman/wang2024mathshepherd: splitting gives a run of three sentences that each end on a result and its citation.

## Other observations for the author (nothing changed)

- **II-C against the Acknowledgment.**
  - II-C names the two exceptions to full-text reading as "a classical inequality cited as a standard result, and one paywalled paper for which only the abstract was available".
  - The frozen Acknowledgment says "two paywalled sources were checked against their bibliographic records only".
  - These agree only if the inequality's source is the second paywalled item. "Only the abstract" also differs from "bibliographic records only". Worth one look.
- **Paragraph density.** B-B ¶2 (about 340 words) and B-D ¶3 (about 310 words) are the paper's two walls of text. Natural paragraph breaks fall before "Closest to the two-rate picture, Duan et al." and before "Reliability over repeated trials can be measured directly." I did not add them, because paragraph breaks were not among the allowed moves.
- **Repeated condition.** The voting condition ("which at a two-way decision means being right more often than not ... wrong answers that agree ... defeat it") appears in both VI-D and VIII. It stays, because "at a two-way decision" is a counted hedge phrase. E27 and E29 now give the two copies different sentence shapes.
- **Register and punctuation.**
  - Register shifts: two, E46 ("...: these lines established that much") and E53 ("So importance and hardness were measured ...").
  - Semicolons and em-dashes: none added.
  - Sentence-initial "But" now appears twice (II-D and VIII); "Yet" and "So" appear once each.
