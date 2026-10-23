# Humanization log: `main_humanized.tex`

- **Source:** `main.tex` (not modified). **Output:** `main_humanized.tex`. **Date:** 2026-10-03.
- **Procedure:** the `telegrapher-style-profile` (style guide + final-pass checklist) ran on top of the generic `humanization` skill, and the profile won wherever the two conflicted. Pass 2a (de-densify) ran first, then the texture interventions T1–T8 and C1–C4, scaled to a 13-page review. The detector step was skipped. No section or subsection was restructured and no heading was moved. Spelling stays American.
- **Edits:** 28 in all: Pass 2a: 3 · T1 clause architecture: 12 · T2 results parallelism: 1 · T3 hedge position: 1 · T4 transitions: 1 · C1/T5 register: 1 · T8 register across paragraphs: 2 · C2 punctuation: 1 · C3 sentence openings: 6. Edit IDs (E01–E28) follow paper order. The tables below group them by primary rule; any secondary rule is named in the last column.
- **Untouched:** preamble, title, authors, abstract, keywords, all tables, the figure, the equations, the itemized lists, the acknowledgment, the bibliography commands, and the biographies.

## Pass 2a: De-densify (3)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E05 · II-D Relation to Existing Reviews, ¶1 (last sentence) | `The intervention side of the question, how the recurring failures at key decisions can be cataloged and targeted inside a deployment domain, is developed in a companion paper~\cite{arbuzov2026architecture}.` | `A companion paper~\cite{arbuzov2026architecture} develops the intervention side of the question: how the recurring failures at key decisions can be cataloged and targeted inside a deployment domain.` | Pass 2a. A passive sentence with a 17-word appositive between subject and verb becomes active, with the verb as the fourth word, and the appositive becomes a clause after a colon. The \cite stays attached to "companion paper". |
| E13 · VI-A Dependence Within One Answer, ¶3 | `In an audit that swapped relayed key--value caches between examples, receiving agents, copies of the same model as the sender, followed the content of a mismatched cache in about 64\% of cases, against about 22\% under a matched control~\cite{cheng2026audit}.` | `In an audit that swapped relayed key--value caches between examples, receiving agents (copies of the same model as the sender) followed the content of a mismatched cache in about 64\% of cases, against about 22\% under a matched control~\cite{cheng2026audit}.` | Pass 2a, with C2. Parentheses around the mid-sentence appositive, so "examples, receiving agents, copies…" no longer reads as a list. |
| E25 · IX Open Problems, "local or global?" ¶ | `Whether different models also fail at the same local decision points would connect this geometry directly to error correlation.` | `Determining whether different models also fail at the same local decision points would connect this geometry directly to error correlation.` | Pass 2a. Gives the *whether*-clause a governing verb, since a question cannot itself "connect" anything. The claim is unchanged. |

## T1: Clause architecture (12)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E01 · I Introduction, ¶1 | `The argument is short, and it has been used to predict a ceiling on what autoregressive systems can do.` | `The argument is short. It has been used to predict a ceiling on what autoregressive systems can do.` | T1. A bare declarative after the long Dziri sentence. It also removes one of the paragraph's two ", and" closers. |
| E03 · II-B How the Literature Was Assembled | `A preprint is included when it reports a measurement that no peer-reviewed work provides, and it is cited as a preprint.` | `When a preprint reports a measurement that no peer-reviewed work provides, it is included and cited as a preprint.` | T1. The condition moves to the front (periodic sentence), and the ", and it is" closer goes. |
| E07 · IV-B Limits, "High attention…" ¶ | `On long chains of thought, selection by attention alone fell well short of selection that also removes redundancy~\cite{cai2025rkv}, and eviction policies applied to instructions could not tell which entries were safe to drop~\cite{chen2026pitfalls}.` | `On long chains of thought, selection by attention alone fell well short of selection that also removes redundancy~\cite{cai2025rkv}. Eviction policies applied to instructions could not tell which entries were safe to drop~\cite{chen2026pitfalls}.` | T1. Splits two studies that were joined by ", and". Each keeps its own citation. |
| E15 · VI-B Structure of Internal Representations, ¶1 (last sentence) | `Static embeddings of models up to 1.5B parameters cluster into strata with different intrinsic dimensions, aligned with the source of the data~\cite{li2025unraveling}; a statistical test on the input-embedding spaces of four open LLMs rejects local smoothness around some tokens, evidence against a single smooth manifold and compatible with a stratified space~\cite{robinson2025token}; and across prompts of fixed length, those whose token representations occupy lower-dimensional point clouds have lower average surprisal~\cite{viswanathan2024geometry}.` | `Static embeddings of models up to 1.5B parameters cluster into strata with different intrinsic dimensions, aligned with the source of the data~\cite{li2025unraveling}; a statistical test on the input-embedding spaces of four open LLMs rejects local smoothness around some tokens, evidence against a single smooth manifold and compatible with a stratified space~\cite{robinson2025token}. Across prompts of fixed length, those whose token representations occupy lower-dimensional point clouds have lower average surprisal~\cite{viswanathan2024geometry}.` | T1, with C2. Breaks the three-item semicolon chain. The third result is a different kind of finding (dimension against surprisal), so it gets its own sentence. The two strata results stay joined. The paper has one semicolon fewer. |
| E16 · VI-B, ¶2 | `A probe can locate the needed information in the hidden states of a long-context model even when the generated answer is wrong~\cite{gao2024insights}.` | `When a long-context model's generated answer is wrong, a probe can still locate the needed information in its hidden states~\cite{gao2024insights}.` | T1. The condition moves to the front, which ends the back-to-back sentence endings "…probe … can … even when … wrong". "Even" becomes "still" with the same concessive sense; no scope hedge is touched. |
| E19 · VI-C Shared Structure Across Models, ¶1 (opening) | `A further question is whether this structure belongs to one model's training or to the data.` | `Whether this structure belongs to one model's training or to the data is a further question.` | T1. Periodic sentence, with the main clause last. "Further" now follows the em-dash pivot that closes VI-B (E18). |
| E20 · VI-C, ¶1 | `Representations of independently trained networks can be mapped onto one another, and Table~\ref{tab:crossmodel} summarizes the evidence.` | `Representations of independently trained networks can be mapped onto one another. Table~\ref{tab:crossmodel} summarizes the evidence.` | T1. Splits off the ", and Table … summarizes" closer, which repeated the ", and Table … lists" closer in IV-A. Only one of the two is changed, which is enough to break the echo. |
| E21 · VI-C, ¶2 | `Splicing an activation from one LLM into another's forward pass outperformed text-based debate on several tasks, mostly between two models of one family~\cite{ramesh2025activations}, and a fuser trained separately for each pair can project one model's key--value cache into another's across families, improving accuracy over text hand-off by about three to five points~\cite{fu2026c2c}.` | `Splicing an activation from one LLM into another's forward pass outperformed text-based debate on several tasks, mostly between two models of one family~\cite{ramesh2025activations}. A fuser trained separately for each pair can project one model's key--value cache into another's across families, improving accuracy over text hand-off by about three to five points~\cite{fu2026c2c}.` | T1, with T2. Splits two studies that were joined by ", and". Each keeps its citation. |
| E22 · VII-B Token-Level and Step-Level Decay | `Success on software and research tasks falls off smoothly with the time a human expert needs for the task~\cite{kwa2025measuring}, and a constant failure rate per minute of human task time, which implies exponential decay in task length, fits those data about as well as the original analysis, although its author calls the evidence suggestive~\cite{ord2025halflife}.` | `Success on software and research tasks falls off smoothly with the time a human expert needs for the task~\cite{kwa2025measuring}. A constant failure rate per minute of human task time, which implies exponential decay in task length, fits those data about as well as the original analysis, although its author calls the evidence suggestive~\cite{ord2025halflife}.` | T1. Splits two studies that were joined by ", and". Each keeps its citation, and the "suggestive" hedge is kept. |
| E23 · VIII Implications, last ¶ | `Passing internal states instead of text can carry wrong content as well as right content~\cite{cheng2026audit,fu2026c2c}, and it is harder to inspect than text.` | `Passing internal states instead of text can carry wrong content as well as right content~\cite{cheng2026audit,fu2026c2c}. It is also harder to inspect than text.` | T1. The closer becomes a short second sentence. That clause was uncited before and still is. |
| E26 · X Conclusion, ¶1 | `Risk concentrates: at each step a minority of positions carries the long-range information, and a minority of decisions determines whether an answer goes wrong.` | `Risk concentrates. At each step a minority of positions carries the long-range information, and a minority of decisions determines whether an answer goes wrong.` | T1, with C2. The colon becomes a period, giving a two-word sentence that breaks the colon parallel with the next sentence ("Errors depend on one another: …"). |
| E28 · Appendix A, Majority Voting | `If samples are positively correlated, the effective number of independent votes falls below $m$, and in the limit of perfectly correlated samples voting gains nothing.` | `If samples are positively correlated, the effective number of independent votes falls below $m$. In the limit of perfectly correlated samples, voting gains nothing.` | T1. Splits the compound sentence, so a short declarative ends the step. |

## T2: Results-reporting parallelism (1)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E10 · V-A Evidence, ¶3 | `Branching only where entropy is high, in a verifier-guided beam search, raises accuracy over single-path decoding by 18\% (relative) on average across six models and five benchmarks while running 31--75\% faster than uniform beam search, although most of the gain over single-path decoding comes from the verifier-guided search itself~\cite{li2025egb}.` | `In a verifier-guided beam search, branching only where entropy is high raises accuracy over single-path decoding by 18\% (relative) on average across six models and five benchmarks while running 31--75\% faster than uniform beam search, although most of the gain over single-path decoding comes from the verifier-guided search itself~\cite{li2025egb}.` | T2, with C3. Breaks a run of three gerund subjects in a row (Pausing / Branching / Allocating) in a results paragraph. |

## T3: Asymmetric hedging, position only (1)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E09 · V-A Evidence, ¶2 | `In chain-of-thought generation by Qwen3-8B, over half of all tokens have entropy below 0.01; restricting policy-gradient updates to the 20\% of tokens with the highest entropy, a cutoff the authors chose, matched full-gradient reinforcement learning at 8B and exceeded it at 14B and 32B~\cite{wang2025beyond8020}.` | `Over half of all tokens in chain-of-thought generation by Qwen3-8B have entropy below 0.01; restricting policy-gradient updates to the 20\% of tokens with the highest entropy---a cutoff the authors chose---matched full-gradient reinforcement learning at 8B and exceeded it at 14B and 32B~\cite{wang2025beyond8020}.` | T3, with C2 and C3. The existing hedge ("a cutoff the authors chose") is set off with em-dashes, so it is embedded mid-sentence and marks where the subject ends. The new opening also removes the second consecutive "In [setting] by/from [model]," frame. No hedge was added or removed. |

## T4: Transitions (1)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E14 · VI-B Structure of Internal Representations, ¶1 (opening) | `If errors propagate, it is natural to ask what they propagate through.` | `[deleted]` | T4. A bridge sentence is dropped, following the profile's "drop bridge sentences" rule. The subsection now opens on its first claim ("Several lines of work find…"), and the RQ3 claim plus the heading already carry the link. This is the pass's only deletion; to revert, restore the sentence. |

## C1/T5: Vocabulary and register (1)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E06 · III-A The Uniform Model, ¶1 (opening) | `The pessimistic argument is short.` | `The pessimistic argument fits in a few lines.` | C1/T5. Plainer phrasing that avoids repeating the Introduction's "The argument is short." word for word. |

## T8: Register across adjacent paragraphs (2)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E12 · V-C What This Means for the Model, ¶1 | `The evidence supports the second premise of \eqref{eq:tworate}: the outcome turns on a minority of decisions, and targeting them is effective. It qualifies it in two ways.` | `The second premise of \eqref{eq:tworate} is also supported: the outcome turns on a minority of decisions, and targeting them is effective. The evidence qualifies it in two ways.` | T8, with C3. Breaks the template it shared with IV-C ("The evidence supports the [first/second] premise of (2): …") and fixes the clumsy "It qualifies it". |
| E24 · IX Open Problems, "How far do importance and hardness coincide?" ¶ | `Importance (Section~\ref{sec:importance}) and hardness (Section~\ref{sec:hardness}) are measured by different methods on different data, and we are not aware of a study that computes both on the same outputs and reports their overlap.` | `Importance (Section~\ref{sec:importance}) and hardness (Section~\ref{sec:hardness}) are measured by different methods on different data. We are not aware of a study that computes both on the same outputs and reports their overlap.` | T8. The authors' statement that they know of no such study becomes its own sentence, so the authors are briefly visible. The hedge wording is unchanged. |

## C2: Punctuation (1)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E18 · VI-B, ¶3 (last sentence) | `They establish that structure exists and that errors are visible in it, not that the structure governs how errors spread.` | `They establish that structure exists and that errors are visible in it---not that the structure governs how errors spread.` | C2, with T8. An em-dash makes a hard pivot here instead of the paper's frequent ", not that …" construction. This is the second of two em-dash uses in the paper (the other is E09). |

## C3: Sentence openings (6)

| Section | Original sentence | Revised sentence | Rule applied |
|---|---|---|---|
| E02 · I Introduction, ¶3 | `Errors are not independent: an early wrong commitment is carried forward, and wrong answers agree across samples and across models.` | `Nor are errors independent: an early wrong commitment is carried forward, and wrong answers agree across samples and across models.` | C3. "Nor" breaks the parallel openings "Risk is not …:" and "Errors are not …:". |
| E04 · II-D Relation to Existing Reviews, ¶1 | `The uncertainty review notes that early mistakes can derail a chain of thought and surveys methods that propagate uncertainty across agent steps, but none of these reviews models how the findings compose into the probability that a long output is correct, which is the question this review is organized around.` | `The uncertainty review notes that early mistakes can derail a chain of thought and surveys methods that propagate uncertainty across agent steps. But none of these reviews models how the findings compose into the probability that a long output is correct, which is the question this review is organized around.` | C3. A "But" opening at the review's positioning point; it is the only sentence in the paper that opens with "But". It also splits a 50-word sentence. |
| E08 · V-A Evidence, ¶1 | `In incorrect reasoning traces of Llama-3-8B on GSM8K and MATH, Lin et al.~\cite{lin2024critical} located a \emph{critical token} in each trace; forcing a different token at that one position recovered the correct answer in about 30\% of single re-samples and in over 90\% of cases within 64.` | `Lin et al.~\cite{lin2024critical} located a \emph{critical token} in each incorrect reasoning trace of Llama-3-8B on GSM8K and MATH; forcing a different token at that one position recovered the correct answer in about 30\% of single re-samples and in over 90\% of cases within 64.` | C3. Putting the authors first breaks a run of three front-loaded openers (Re-sampling …, / In incorrect …, / At the level …,). The \cite stays attached to "Lin et al.". |
| E11 · V-B Limits, "Some failures are spread out" ¶ | `Across 23 model and benchmark settings, an early prefix of a reasoning trace predicted failure better than the full trace in 14, while in 9 the predictive signal kept growing to the end~\cite{thoria2026fail}.` | `An early prefix of a reasoning trace predicted failure better than the full trace in 14 of 23 model and benchmark settings, while in 9 the predictive signal kept growing to the end~\cite{thoria2026fail}.` | C3. Subject first, which removes two front-loaded openers in a row (Across …, / For compressing …,). The numbers 14, 23 and 9 are unchanged; only their order in the sentence differs. |
| E17 · VI-B, ¶2 (last sentence) | `In Qwen-3 models up to 14B parameters, internal features represent a word before it is generated and shape the token that precedes it, although planning more than a token ahead is rare~\cite{hanna2026planning}.` | `Qwen-3 models up to 14B parameters have internal features that represent a word before it is generated and shape the token that precedes it, although planning more than a token ahead is rare~\cite{hanna2026planning}.` | C3. Subject first, which removes two consecutive "In [models]," openers. The scope ("up to 14B parameters") and the hedge ("rare") are kept. |
| E27 · X Conclusion, ¶2 | `When every step of a task brings new decisions, reliability decays exponentially again, in decisions rather than tokens, which is what evaluations of long agentic tasks report.` | `If instead every step of a task brings new decisions, reliability decays exponentially again, in decisions rather than tokens, which is what evaluations of long agentic tasks report.` | C3. Breaks two consecutive "When …" openers. |

## Not applied, and why

- **T5 register shifts that add phrases** (for example "This is where things get interesting" or "Frankly, we expected…"): these would add flourish or new content, which the hard constraints forbid. Only one rewording-based shift was made (E06).
- **T6 (how examples are introduced):** the paper has one running example, so there is nothing to vary.
- **T7 (uneven paragraph density):** no paragraphs were split or merged, per instruction 3. The paper already mixes dense single paragraphs (VI-D Limits) with short ones (VI-A ¶3, VIII last ¶).
- **C4 (varying citation integration):** blocked by frozen citation placement. No \cite left the noun phrase it marks. E05 and E08 move a noun phrase ("companion paper", "Lin et al.") together with its \cite.
- **C1 beyond one instance:** the register already has "doomed", "load-bearing", "pays for", "sink", and "snowballing". More would read as inconsistency.
- **B1–B3 (table-prose mirroring):** handled as flags below; the numbers stay.
- **Semicolons:** none added, since the paper already has 75. One was removed (E15).
- **Em-dashes:** two uses (E09, E18), three "---" tokens. That is sparing, and each does a different job: an embedded hedge and a hard pivot.

## Flagged for author: relationships over values (numbers left in place)

The profile's rule is that tables hold the numbers and prose holds the relationship, with one headline number per system. The sentences below repeat table cells or carry several values per study. **No number was removed.** Note that the paper's own design ("comparison tables that report each result with the setting it holds in") partly justifies repeating figures, so this is the author's call.

| Flag | Location | Values in prose | Why flagged |
|---|---|---|---|
| F01 | IV-A ¶2 (Fang et al.) | "fewer than one token in ten … more than 2 nats" | Repeats Table I. It is a candidate anchor (the section's "most direct evidence"), so keep it if only one number stays. |
| F02 | IV-A ¶2 (Vakilian et al.) | "75--80\% … the last 64--96 tokens" | Repeats Table I. The same sentence already states the distribution case in words ("between a third and a half"). |
| F03 | IV-A ¶3 (Quest) | "more than 90\% of cached tokens" | Repeats Table I. |
| F04 | IV-A ¶4 (anchor tokens) | "up to 99\% … about 1.5\%" | Two values for one system. They are not in any table. |
| F05 | IV-A ¶4 (R-KV) | "10--54\% of the generated length" | Repeats Table I. |
| F06 | V-A ¶1 (Bigelow; Lin) | "up to 63\%"; "about 30\% … over 90\% … within 64" | Repeats Table II. |
| F07 | V-A ¶2 (Wang; He) | "below 0.01 … the 20\%"; "(median 1.26 against 0.03)" | Wang repeats Table II. He's medians appear only in prose, and "far higher" already gives the relationship. |
| F08 | V-A ¶3 (He; Li) | "about 7\% … 3.6 to 7.6 points"; "18\% (relative) … 31--75\%" | Repeats Table II, with two values per system. |
| F09 | V-B ¶1 (Yeom; Obeso) | "16--47\%", "about a fifth"; "0.87--0.90 against about 0.71" | The prose already states the relationship ("much better than token entropy"). |
| F10 | VI-A ¶1 (Zhang et al.) | "67\%, 87\%, and 94\% … respectively" | Three per-model values. A relationship form (for example "between two-thirds and nearly all of them") would carry the point. This is the author's call. |
| F11 | VI-C ¶3 (Kim et al.) | "about 60\% … against 33\% expected by chance" | Repeats Table III, but it is the comparison against chance. Recommend keeping it. |
| F12 | VI-A ¶3 (audit) | "about 64\% … against about 22\%" | Comparison against a control, which separates the interpretations. Recommend keeping it. |

Not flagged: the running-example values in III, and "17.9 points" and "$-0.18$ to $-0.96$" in VIII. These are values the reader computes from, or anchors.

## Flagged for author: wanted to change, did not

These were held back because the change would alter a claim, a citation's placement, or a cross-reference.

1. **II-D: the three sentences "Surveys of… / Reviews of… / A review of…"** are a templated parallel. Breaking it would mean moving `\cite{liu2026latentsurvey}` off its noun phrase.
2. **III-D: "as with any rate that falls faster than $1/i$"** is mathematically too broad. $1/(i\ln i)$ falls faster than $1/i$, but its sum diverges. A precise version would be "any rate bounded by $c\,i^{-p}$ with $p>1$". Not changed because it is a math claim.
3. **III-E: "Section~\ref{sec:reconcile} asks how far the two coincide."** The overlap question is actually posed in IX ("How far do importance and hardness coincide?", `sec:open`), and V-C already points there. This may be a stale cross-reference. Not changed.
4. **IV-A ¶4: moving "in the authors' single-run comparison" to the front** (T3, hedge position) would make "the authors" read as R-KV's authors. The hedge stays at the end.
5. **V Claim: splitting "…, and spending extra computation at those points pays off."** The next sentence's "this way" would lose its antecedent.
6. **V-A ¶2: splitting "Token difficulty is uneven at training time as well: …~\cite{lin2024rho1}" at the colon** would leave the general claim without its adjacent citation.
7. **VII-C: changing "where the two-rate picture does not hold" to "two-rate model"** (to reuse the term already on the page). "Picture" covers the whole argument, including sparsity, detection based on uncertainty, and voting, so "model" would narrow the claim.
8. **VI-D: changing "less surface-invariant than the clean results suggest" to "more brittle"** (C1) would broaden the claim beyond surface form.
9. **VI-E: "Within one answer, failures that co-occur concentrate in fewer answers"** reads as self-contradictory ("within one answer … fewer answers"). The intended meaning is probably that positive dependence among an answer's key positions concentrates failures into fewer answers, but rewording it touches the dependence claim.
10. **VIII ¶1: splitting "Dense attention pays for a sparse signal, and caches …~\cite{tang2024quest,cai2024pyramidkv}"** would leave the first claim uncited.
11. **X ¶3: "Why errors cluster, and whether …, has been suggested by the evidence but not tested."** A *why*-clause cannot itself be "suggested". The fix ("An explanation of why errors cluster …") would rewrite a sentence that carries a hedge.
12. **VI-C ¶2: "For LLMs, more capable language and vision models induce…"** "For LLMs" sits oddly with "vision models", but rewording it would change the claim's scope.

## Reviewer-facing checks from the profile (for the author; nothing changed)

- **Absolute claims that need a row in the ledger:** IX ¶1 says "No study has measured the number of key positions as a function of output length on a fixed corpus." V-C says "…has not been measured". Compare IX ¶2, which hedges: "We are not aware of a study…". Either confirm the ledger has rows for both, or align the hedging.
- **Third-party numbers:** every numeric sentence carries its \cite in the same sentence.
- **Self-citations:** `arbuzov2025beyond` (provenance) and `arbuzov2026architecture` (a pointer) carry no body claim on their own.

## Verification

A scripted check compared `main.tex` with `main_humanized.tex`:

- **Edit list:** each original string occurs exactly once in `main.tex`. The written file is byte-identical to applying exactly these 28 edits mechanically, with LF line endings as in the source.
- **Frozen regions are identical:**
  - everything from `\documentclass` through `\maketitle`, including the abstract and keywords;
  - every table (2), table* (4), figure (1), equation (5) and itemize (3) environment;
  - everything from `\section*{Acknowledgment}` through `\end{document}`;
  - all 41 headings.
- **Ordered sequences are identical:** 141 `\cite` (same keys, options and order), 67 `\ref`/`\eqref`, 24 `\label`, 106 inline-math segments, 35 `\emph`, 1 footnote.
- **Numbers:** the 272 numeric tokens form the same multiset. The only change of order is E11's "14 of 23".
- **Names:** model, dataset and venue names form the same multiset.
- **Hedge words:** counts are unchanged except "even" going to "still" in E16, which is concessive wording rather than a scope hedge. "On our reading", "suggests", "about", "untested", "preprint", "seem", "largely", "not aware" and "illustrative" are all intact.
- **Punctuation:**
  - semicolons 75 → 74;
  - colons 162 → 162;
  - em-dash tokens 0 → 3 (two uses);
  - ", and " 79 → 70.

  Braces are balanced, the `\begin`/`\end` counts are unchanged, and no British spellings were introduced.
- **Compile check:** both files were built in a scratch copy (pdflatex, bibtex, pdflatex twice). Both give 13 pages with no errors and no undefined citations or references, and the same overfull/underfull counts (36/18). The only remaining warning is the template's font-shape warning, which appears in both.
- **Rhythm:**
  - body sentences 252 → 261;
  - mean length 23.8 → 22.8 words;
  - pairs of adjacent sentences sharing an opening word 17 → 12.

  The pairs that remain are intentional or harmless: the "The criterion/unit/task differs" taxonomy, the appendix enumeration "If $k = $…", and pairs that span a heading.
