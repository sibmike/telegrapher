# ACL Rolling Review version: brief (paper-compression, n_pages = 8)

Target: ACL Rolling Review long paper, primary venue NAACL 2027 (COLING 2027 as alternative). Eight pages of body in the ACL two-column template; the abstract (at most 200 words), references, the mandatory unnumbered **Limitations** section, an optional Ethics Statement, and appendices do not count. Anonymized for double-blind review. Standalone: a reader who never sees the IEEE article must get the whole argument from these eight pages.

Source of truth for every fact: the IEEE package after round P, `ieee_access/paper_frontier_and_localhost/submission/sections/` (`I_II_intro_loop.md`, `III_method.md`, `IV_local_findings.md`, `V_feedback_signal_classes.md`, `VI_promotion.md`, `VII_failure_surface.md`, `VIII_missing_architecture.md`, `IX_families.md`, `X_open_problems_conclusion.md`, `appA_formal.md`, `appB_gates.md`), which was fact-screened against the released table on 2026-10-09. Nothing enters this version that is not in those files. No new numbers, systems, claims, or citations.

## 1. Story spine (the body must deliver these nine sentences, in order)

1. Systems built on large language models increasingly adapt by editing the persistent text and code around a frozen model (instructions, skills, memories, tools, and routing), and the literature calls almost any system that does so self-improving.
2. That label conflates three different things: an artifact that persists, an edit shown to improve the deployment that made it, and an improvement justified somewhere else.
3. We separate them as two decisions, a local loop that keeps an edit only when a check shows the deployment's failure rate falls, and a promotion loop that decides how far a kept edit may travel, and we read 256 public systems by who or what makes each decision.
4. The local acceptance check is the most developed piece: nearly every failure-driven system decides it by program, while the steps that should feed it, a log of failures and the trace from a failure to the artifact that caused it, are the least built.
5. Promotion exists only in parts and only inside one operator; no surveyed system promotes across organizations under an automatic gate with lineage, access control, and rollback.
6. The feedback a deployment receives (an exact check, an observed outcome, a judgment, or a reward that arrives months later) explains much of this pattern, because it fixes what an acceptance gate can know, and in every class an accepted edit is evidence only for the measure and the tasks it was tested on.
7. The same reading exposes four confusions that the self-improvement label hides: detection mistaken for testing, history mistaken for correction, local success mistaken for transfer, and an evaluator that becomes part of what it evaluates.
8. The survey runs no experiments; its classifications are one rater's reading of public evidence, released row by row so that each can be checked.
9. The work this points to is attribution across artifact types, evaluation at the receiving deployment, calibration of a judge whose rubric is being edited, evaluation under delayed reward, and, only after those, governed sharing across organizations.

The reviewer-facing emphasis (from the venue assessment): the contribution is the analytic distinction in sentences 2, 3, 6, and 7 and what it reveals about language agents that retain experience, test changes, and transfer learned artifacts. Governed cross-organization promotion is a consequence of the findings (sentence 9), not the reason the survey exists; it gets one paragraph in the body and its full audit in an appendix. Reviewers will probe originality against neighboring surveys and the single-rater classifications: the related-work section answers the first in the body, and the Limitations section answers the second honestly.

## 2. Body outline and page budget (about 8.0 pages, two columns, 11 pt)

| § | Title (working) | Label | Pages | Paragraphs | Spine | What it carries |
|---|---|---|---|---|---|---|
| 1 | Introduction | sec:intro | 1.0 | 5 | 1, 2, 3, 4-6 preview, 8 | The naming-rule example; the three things the label conflates; the two decisions; the findings stated once; the central contribution first, the supporting ones after it, no numbered contribution list |
| 2 | Two decisions about an edit | sec:loop | 1.2 | 6 + Fig. 1 | 3 | The local loop in plain words (failure log, trace, candidate, gate, versioned keep); patch and patch loss; the five conditions named in one compact list; the gate kinds Auto, Human, None by who decides; the promotion loop, the scopes in one sentence, receiving-side evaluation and evidence radius introduced by the second-repository example; the measure bound |
| 3 | Corpus and reading | sec:method | 0.5 | 3 | 3, 8 | 256 systems, inclusion rule, core/contrast filter, two-loop audit and its 11 + 3 passers, what is read for each system, single rater and released table; everything else to Appendix A |
| 4 | What the local loop closes | sec:local | 1.3 | 6 | 4, 7 | Detection is not testing (SkillForge, SkillRL); the gate is the best-built step (89 of 105 recent core systems); failure logs and attribution are weak; evidence batching (agreement vs averaging, one sentence); history is not correction (revoked facts still returned); rollback and contaminated descendants; SkillOpt as the one system with all five conditions |
| 5 | What feedback lets a gate know | sec:signal | 1.3 | 5 + Table 1 | 6 | The four-assistants example; the four classes with one developed example each; calibration of judges; the three predictions and how the corpus bears them out |
| 6 | When an improvement is shared | sec:promotion | 1.2 | 5 + Fig. 2 | 5, 7 | Local success is not transfer; receiving-side checks that exist (ShareMem, XRepoSkill, Evo2Team) and their limits; who lets an edit climb (program, person, nothing); formats and registries that move artifacts without evidence; the gate grid read in one paragraph |
| 7 | When the evaluator changes | sec:evaluator | 0.5 | 3 | 7 | The rubric example; the reflexive gate; proxy overoptimization and drifting criteria; the weight-side analogue in one sentence |
| 8 | Related work | sec:related | 0.5 | 3 | (originality) | What the neighboring surveys organize by and the question none classifies; the prompt-optimization lineage and why it is not a deployed loop; five research lines each built one part (one paragraph, table in Appendix G) |
| 9 | Discussion and open problems | sec:discussion | 0.6 | 4 | 6, 9 | Why specialization lives outside the weights, with the error-structure hypothesis of the two prior analyses, stated as hypothesis and load-bearing (third person); governed cross-organization promotion as a consequence: the four properties in one sentence, none holds all four, pointer to Appendix F; the five open problems in one paragraph; closing three sentences |
| — | Limitations (unnumbered, not counted) | sec:limits | ~0.4 | 4 | 8 | Single rater, no inter-rater agreement; public evidence only, vendor claims tiered; corpus cutoff and selection; no experiments, the error-structure hypothesis untested here; two-pass gate columns cover only the 126 most recent systems |

Density caps in the body (skill Step 5): at most one equation block per paragraph (the body keeps only the gate inequality, introduced by a sentence that says what it does, or drops it to Appendix B; writer's choice, with a one-sentence plain statement in the body either way); two or three numbers per paragraph; two to four citations per paragraph; no citation harvests.

## 3. Detail ledger

| Item (source) | Type | Body treatment | Appendix destination |
|---|---|---|---|
| Abstract (abstract.md, 229 words) | framing | rewritten to at most 200 words from the spine | — |
| Naming-rule example, scaffold definition (I) | framing | kept, shortened | — |
| Five conditions list, update rule, gate inequality, gate stability (II) | formal | conditions as one compact list; inequality one block or plain sentence; stability one sentence | B (Formal statement, from appA_formal.md, unchanged mathematics) |
| Gate kinds Auto / Human / None, cell notation (II) | definition | kept, one short paragraph | — |
| Scopes USER to CORE, Fig. scope (VI-A) | definition | one sentence naming the scopes | A (with the scope figure) |
| Corpus selection, filters, Fig. corpus, 269 rows, passers list (III) | protocol | 256 / 204 core / 52 contrast; 11 research + 3 industry passers named in one sentence | A (selection, figure, passers, paper-only systems, relaxations) |
| Substrates table, ruler 0 to 5, score-5 rules (III, Table V-1) | protocol | one sentence on six substrates and a 0 to 5 ruler | A (Table: substrates; ruler) |
| Substrate maturity table (Table V-2), second-pass counts 105/32/89 | results | the 89-of-105 figure only, scoped to the 126 most recent systems | A (Table: maturity) |
| Evidence tiers, single rater, rounding rules (III-C) | protocol | Limitations section | A |
| SkillForge, SkillRL (IV opening) | key finding | developed example | — |
| Failure log rarity, arrival-order use, Task-CoEvolve, AutoSaddler (IV-A) | evidence | one sentence each for the finding, 1 to 2 citations | — (body only; full rows in the released table) |
| Attribution bottleneck, harness-optimization citations (IV-A) | evidence | finding + 2 to 3 representative keys | G (research lines table carries the rest) |
| Instruction files: adoption and two controlled studies (IV-B) | evidence | one sentence: widespread, no measured success gain, studies disagree on cost | A (or body, if space; numbers 124, 29%, 17% go to the appendix) |
| Orchestration progression, OptiMAS (IV-B) | evidence | one sentence | D (gate grid discussion) |
| SAGE-gate, VaG, AutoSaddler; agreement vs averaging (IV-C) | mechanism | one sentence; the p^k vs 1/k contrast in words | C (Gate families table) |
| Ratchet, eleven retirement systems (IV-D) | evidence | one sentence | E (failure surface) |
| Letta, Mem0, Zep lineage; revoked facts; Cuadros et al. (IV-D) | key finding | developed: history is not correction | — |
| SkillSmith, SkillAudit, EvoUndo; VaG descendants (IV-D) | key finding | one or two sentences: rollback leaves descendants | E |
| SkillOpt and SkillOpt-Lite (IV-E) | example | three or four sentences | B (correspondence) |
| Feedback classes table (V, Table IV-1) | analytic table | Table 1 in the body (full width) | — |
| Class paragraphs C1 to C4 (V-A..D) | analysis | one developed example per class, compressed | C (gate families by class) |
| Calibration: three systems report it (V-C) | key finding | one sentence | — |
| Three predictions (V-E) | analysis | one paragraph, with the qualification | D |
| Receiving-side checks, federated placement, Evo2Team limit (VI-A) | key finding | developed | F |
| Automatic / human / unchecked promotion; production-viable pairing (VI-B) | analysis | one paragraph | D |
| Formats, registries, prompt platforms (VI-C) | evidence | one paragraph: portable but not evidenced | D |
| Gate grid figure and table (VI-D, Table VII-1) | analytic figure | Fig. 2 (column width) + one paragraph | D (Table: grid cells, boundary cases, six ungoverned promoters) |
| Failure surface table and paragraphs (VII, Table X-1) | analysis | the reflexive-gate subsection only, plus one sentence pointing to the full table | E (Table: failures; poisoning, injection, coordination, drift paragraphs) |
| Reflexive gate, RLVR comparison (VII-B) | key finding | developed, the weight-side comparison in one sentence | E |
| Governed sharing: four properties, closest approaches table, architecture, FL comparison, by-class automation (VIII) | consequence | one paragraph in the discussion | F (full section and Table: closest approaches) |
| Research lines table and paragraphs (IX opening, Table VIII-1) | context | one paragraph in related work | G (Table: research lines) |
| Why outside the weights; RLHF diversity; adapters; error-structure hypothesis (IX-A) | motivation | one paragraph in the discussion, hypothesis load-bearing, third person | — |
| Neighboring surveys table and paragraph; prompt-optimization lineage (IX-B) | positioning | one paragraph + one on the lineage | H (Table: neighboring surveys) |
| Open problems 1 to 5, conclusion (X) | implication | one paragraph of problems, three closing sentences | — |
| Gate families table (appB) | reference | pointer | C (unchanged) |
| Formal appendix (appA) | proof | pointer | B (unchanged mathematics) |
| Supplementary material S1 to S7, released CSVs | data | pointer to the anonymized supplementary material | submitted separately as supplementary material |

## 4. Rules for writers

- **Labels.** Body: sec:intro, sec:loop, sec:method, sec:local, sec:signal, sec:promotion, sec:evaluator, sec:related, sec:discussion, fig:loop, fig:grid, tab:classes. Appendix (one `##` per letter, in this order): app:corpus (A), app:formal (B), app:gates (C), app:grid (D), app:failure (E), app:governed (F), app:lines (G), app:surveys (H). Figures in the appendix: fig:scope, fig:corpus. Tables in the appendix: tab:substrates, tab:maturity, tab:optim (from appA), tab:gatefamilies, tab:gridcells, tab:failures, tab:closest, tab:lines, tab:surveys. Cross-reference as `Section REF(sec:x)`, `Appendix REF(app:x)`, `Table REF(tab:x)`, `Fig. REF(fig:x)`.
- **Citations** (pandoc, rendered as ACL author-year by natbib): parenthetical `[@key]` or `[@a; @b]`; author as subject `@key` (renders "Sculley et al. (2015)"). Never write "Sculley et al. [@key]". Use only keys present in the source sections.
- **Anonymity.** No author names, no "our previous work", no "this series", no "Part 1/2/3". The two prior analyses are cited in the third person: "@arbuzov2025beyond argue that ...", "@arbuzov2026architecture argue that ...". No acknowledgments. The supplementary is "the supplementary material".
- **Loop names.** The local loop and the promotion loop; the local gate and the promotion gate. Never "Loop 1/Loop 2" in prose. Conditions by name, never "(condition N)".
- **Settled facts that must not drift** (all fact-screened): nearly every failure-driven system closes the local loop by program (89 of the 105 core systems among the 126 most recently added; not a count over all 256); SkillForge's calibrated judge picks the replies to rewrite and nothing tests the rewrite; SkillRL adds skills unconditionally on a success-rate trigger; both sit in [None × None]; OptiMAS has no keep-if-better gate; DGM keeps edits that pass a compile-and-edit validity check, the benchmark score weights parent selection; NanoResearch, AutoManual, and ShareMem decide by program but none estimates a loss change; three systems report judge calibration (SkillForge, SkillChain, SkillCoach) and no other surveyed judge does; no system calibrates a judge whose rubric is being edited; RLPR is the only co-evolving reward method reporting human agreement, and its reward is a probability, not a rubric; receiving-side evaluation is necessary, not sufficient (nearly a fifth of Evo2Team's confirmed transfers still fail on new graphs); federated clients are partitions under one operator; Letta pushes with lineage and no gate; production promotion keeps a person at the promotion gate and that pairing is the production-viable one, not a compromise; no system has both the learning of the top row and the governance of the bottom; no system rolls back a promotion across organizations because none makes one; the literature, not the corpus, measured the failures; SkillChain's person decides which refined skills are deployed; skill-repository edits are committed under named human accounts and human-merged, most with an AI co-author trailer.
- **Style.** The project style guide `C:\Users\mikea\SCRIPTS\ICLR_normalize\skills\telegrapher-style-profile\telegrapher_paper_style_guide.md` and the paper-compression anti-patterns. Each section opens on its evidence or its complication, not on an announcement; explain a compact phrase in literal words before using it; one claim per paragraph; no em-dashes; American spelling ("catalogue" and "analogue" stay); no bridges; dry register.
