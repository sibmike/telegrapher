# "Missing XYZ" sweep — candidates and decisions

Two simulated memory-based reviewers were run on 2026-10-03, following Phase 2 of the `extended-related-work` skill. Both answered from memory, with no web access.

- **Sweep A** saw the full manuscript and the bibliography.
- **Sweep B** saw only the abstract and the introduction.

Names they produced are *candidates*. A candidate enters the paper only after a full-text card in `ledger_parts/J*.md`.

## Sweep B (abstract and introduction only): verdict and objections

**Verdict, as the simulated reviewer gave it.** The review is novel as a synthesis, not in its findings. The decay prediction is textbook survival and reliability mathematics: a mixture of hazards decays more slowly than an exponential. The voting calculation is the Condorcet jury theorem with correlated voters. The revision of the authors' own preprint needs an explicit list of changes.

**Objections, and how the manuscript answers them**

| # | Objection | Answer / action |
|---|---|---|
| B1 | "Independence is the wrong assumption to attack." By the chain rule, P(all correct) = ∏(1 − h_t) holds with no independence, where h_t is the error probability given a clean prefix. The exponential form needs only a constant h_t. Snowballing acts after the first error. | **Main-text fix (Section III-A).** State the chain-rule identity. Independence is what licenses using a per-token error rate measured over whole outputs as h_t. When an earlier error makes later ones more likely, that measured rate overstates the risk at an error-free prefix, so (1) is pessimistic. Appendix A-C gains the one-line ordered version (h_t ≤ P(F_t)) beside the Esary association result. |
| B1' | Snowballing after the first error does not change P(no error) unless recovery is possible. | **Main-text fix (Section VII-B).** Remove "self-conditioning is the mechanism that links the two levels". Restate it as mattering where a task allows a mistake to be repaired. |
| B2 | "Key position" has no definition independent of the outcome. Importance and hardness are different things: a copied entity name versus a forking token. | Already distinguished (Section III-E, Section V-C, Section IX). **Add** the concrete contrast as an example in Section III-E, and add the re-sampling (hardness) variant of the k(n) protocol to Section IX. |
| B3 | No search protocol is visible from the introduction; the review is built around the authors' own model; strawman risk (a talk slide); counter-evidence needs equal weight. | Section II gives the method. The formal versions are already cited (Dziri et al.). **Add** the imitation-learning bound (Ross and Bagnell) and counter-evidence (collapse on controllable puzzles; inverse scaling in test-time compute) to Appendix B, with one pointer from Section VII-C. |
| B4 | Revision of the authors' own preprint: list what changed. | Cover letter and `SUBMISSION_NOTES.md` (prior-publication disclosure): add a short list of changes from the preprint. |

**Candidates from Sweep B** (✓ = sent to verification; – = not pursued, with reason)

| Candidate | Status |
|---|---|
| Bachmann and Nagarajan 2024 (pitfalls) | already cited; new use (framing against the snowballing critique) → J1 |
| Ross and Bagnell 2010; Ross, Gordon and Bagnell 2011 (DAgger) | ✓ J1 |
| Bengio et al. 2015; Ranzato et al. 2016 (exposure bias) | Bengio already cited; Ranzato ✓ J1 |
| Ord 2025; Sinha 2025; Bigelow 2025; Kim 2025; Wang 2025; Lin 2024; Abdin 2024; Bogdan 2025; Goel 2025 | already cited |
| Eckhardt and Lee 1985; Knight and Leveson 1986 (coincident failures in multiversion software) | ✓ J3 |
| Vaupel et al. 1979 (frailty) | ✓ J3 |
| He et al. 2021 (self-recovery) | ✓ J1 |
| Arora et al. 2022 | already cited |
| Foster et al. 2024 (horizon in behavior cloning) | ✓ J1 |
| Ladha 1992; Kuncheva and Whitaker 2003 | ✓ J3, with the SEP entry on jury theorems and Krogh and Vedelsby 1995 |
| Chen et al. 2024 (more LLM calls) | ✓ J3 |
| Meyerson et al. 2025 (million-step task) | ✓ J2 |
| Lanham et al. 2023 (CoT faithfulness) | pending Sweep A |
| Lightman et al. 2024 (step-level verification) | pending Sweep A (planned for batch J4) |
| Ye et al. 2025 (learning from mistakes) | ✓ J2 |
| Kamoi et al. 2024 (self-correction survey) | ✓ J2 |
| Shojaee et al. 2025 (collapse on puzzles) | ✓ J2. The rebuttal comment (Lawsen 2025) is not pursued: a commentary, not a study |
| Gema et al. 2025 (inverse scaling in test-time compute) | ✓ J2 |
| Duan et al. 2024 (relevance-weighted uncertainty) | pending Sweep A (planned for batch J4) |
| Xu et al. 2022 (repetition self-reinforcement) | ✓ J1 |
| Sun et al. 2021 (do long-range LMs use long-range context?) | not cited yet; direct RQ1 evidence; planned for J4 and possibly the main text (Section IV-A) |

## Sweep A (full manuscript): claims at risk and actions

| # | Claim at risk (as the simulated reviewer put it) | Action taken in `main.tex` |
|---|---|---|
| A1 | III-A: independence is not needed; LeCun's e is a hazard with an absorbing wrong state (the ledger for `lecun2023why` agrees) | Chain-rule paragraph added. Error redefined as a wrong commitment, so that several errors can co-occur. The finality premise is stated, and the review "largely accepts" it (Section VI evidence; reasoning models partly repair) |
| A2 | VI-D/VII-B: with "an error changes the outcome" plus no repair, an answer holds at most one error, so association is incoherent; self-conditioning acts after the first error | The definition fix makes multiple errors well defined. The ordered-hazard argument is added to App. A-C (an earlier error raising later risk gives h ≤ P(F)). VII-B rewritten: self-conditioning does not by itself produce the decay; it matters where repair is possible |
| A3 | IV-C conflates context positions that are read with output positions that can fail | Narrowed to "on the side of information … earlier positions … at any step"; the existing sentence separating importance from hardness kept |
| A4 | III-B running example is circular as evidence | Already labelled "illustrative, not measured". No change |
| A5 | e_non shrinking is supported only by counter-evidence | J4 verifies the evidence on per-position loss (Kaplan; Olsson) and branching factor (Yang and Holtzman). To be placed with explicit caveats (loss ≠ error) |
| A6 | The k(n) protocol measures importance, not the k of (2) | IX now says so, adds the hardness (re-sampling) variant, and links the two to the overlap question |
| A7 | "Recovering … is hard" rests on 2023-era models | Narrowed to "models without trained reasoning". SCoRe / R1 / Tyen (J2, J6) to be added |
| A8 | II-D "none of these reviews" | Already limited to the four reviews cited. No change. Malinin and Gales (J5) go to App. B |
| A9 | "ensembles help less than their number suggests" has no direct measurement | VI-D and VIII rewritten as consequences of the voting analysis plus measured agreement |
| A10 | The central argument rests on a LinkedIn post; "used to predict a ceiling" is uncited | J8 re-reads the post for the ceiling claim. Bachmann and Nagarajan (peer reviewed) framing checked in J1. The Mostik footnote stays (it is labelled as relying on no results) |

**Novelty objections → actions**

- Voting equals Condorcet. Contribution 3 now says "worked calculations, using classical tools". App. A-D will cite the jury theorem (J3).
- Table I forms can also arise from heterogeneity across problems (Proschan; Schaeffer). One sentence will go in App. B (J8).
- Section VI-C: shared item difficulty (Eckhardt and Lee) explains co-failure without geometry. VI-C and Table V will name it as the simpler alternative (J3).
- Changes from the preprint will be listed against arXiv v3 in the cover letter.

**Candidates from Sweep A sent to verification:**
- J4 (context use and length): Khandelwal 2018; Sun 2021; Kaplan 2020; Olsson 2022; Yang and Holtzman 2025; RULER; Levy et al. 2024; GSM-Symbolic; GSM-IC; Wei et al. 2022.
- J5 (uncertainty and attention): Kuhn 2023; Farquhar 2024; Kadavath 2022; SelfCheckGPT; Duan 2024; Malinin and Gales 2021; Jain and Wallace; Wiegreffe and Pinter; Kobayashi 2020; Kalai and Vempala 2024.
- J6 (steps and repair): Lightman 2024; Cobbe 2021; Math-Shepherd; Tyen 2024; Wang and Zhou 2024; DeepSeek-R1; Leviathan 2023; Mixture-of-Depths; Laban 2025; Lanham 2023.
- J7 (representations): SVCCA; CKA; Lenc and Vedaldi; Bansal 2021; Conneau 2018; Azaria and Mitchell; CCS; ITI; Bürger 2024; Ferrando 2025; Geirhos 2020; Meng 2022.
- J8 (heterogeneity): Schaeffer 2025; Proschan 1963; More Agents (Li 2024); Kleinberg and Raghavan 2021; Lam and Suen 1997; Levy and Jaeger 2007; Meister 2021; LeCun post (additional use).

**Not pursued:**

| Candidate | Reason |
|---|---|
| Gloeckle 2024 | Multi-token prediction is not about errors |
| Ilyas 2019 | Transferability of adversarial examples; Geirhos covers error overlap more directly |
| LongBench, LongWriter | Benchmarks; RULER covers effective context |
| Pass@k (Chen 2021) | Brown 2024 covers coverage |
| Wu 2025 (CoT length) | Lower priority; Gema 2025 covers longer reasoning lowering accuracy |
| Boland 1989 | SEP and Ladha cover correlated jurors |
| Graves 2016 (ACT); Elbayad 2020 | Mixture-of-Depths and CALM cover adaptive computation |
| Kalai et al. 2025 | Kalai and Vempala 2024 (peer reviewed) covers the statistical floor |
