# Response to the external review of 2026-10-07

Review of `submission/main.pdf` at commit `063e1b6` (the story-first build). Each point below gives our verdict on the objection, what changed in the manuscript, and where. The authors can adapt the "Response" paragraphs into the cover letter or a formal response.

## 1. The classification needs consistent definitions

**Verdict: correct.** Section III defined a gate by who decides; Section VII re-labelled the human-authored cells by who supplied the candidate, and treated Letta's unconditional push as an "Auto" gate. Those are two variables under one label, and under the second reading the emptiness of [Human × Auto] was uninterpretable.

**Change.** Both axes now record who decides, and nothing else: Auto when a program applies a check, Human when a person decides, None when the step is absent or runs unchecked. The "degenerate unconditional rule" clause is gone from the definition of Auto. Candidate source (agent, engineer, registrant) is recorded as a separate variable in a new occupant table in Supplementary Material S4.2.1, which lists candidate source, Loop 1 gate, promotion mechanism, and Loop 2 gate for every matrix occupant, the three variables the reviewer asked us to separate. Eight rows of the released table were re-coded under the strict definition (recorded in S6.7 and in `CLAIMS_AUDIT.md`); no score changed. Consequences: Letta's Context Repositories move to [Auto × None] and the text says plainly that a push which carries every edit is not a gate; the registries and the community hub move to [None × Human], because a person registering an artifact supplies a candidate and does not gate a failure-driven loop; [Human × Auto] and [Human × Human] are both empty, which now means one interpretable thing, that no surveyed system puts a person on the local gate of a failure-driven loop and then promotes the result. Section III-C, Section VII, Figure 4 and its caption, Table VI-2, S2, S4.2.1, S6.2.

**Response.** We agree, and we thank the reviewer for catching it. The central finding is unchanged in substance and is now stated under one definition: two gated cells hold every audit passer whose promotion has a gate, one half-cell holds the governance-first platforms, one passer promotes with no gate at all, and no populated cell adds governed cross-tenant promotion.

## 2. The feedback-class conclusions are too categorical

**Verdict: mostly correct.** (a) A deterministic check is exact for the artifact and the test it runs; it does not make the gate's estimate of the patch loss exact, because the suite samples the patch's task mix and the agent that runs under the edited scaffold is stochastic. (b) Delay, subjectivity, and observability overlap, and the text never said how a class is assigned. (c) The AlphaEvolve spot-check is correct: the paper's own description (arXiv 2506.13131, Sections 2.4 and 2.5) says every candidate "is automatically evaluated" and that the evolutionary database aims "to continuously improve the best programs while maintaining diversity". Our wording "keeps candidates for their diversity, not their score", and the placement of the archive under the delayed class, were wrong.

**Change.** Section IV now states the assignment rule (a partition by the property that binds the gate first: delay, then absence of ground truth, then exactness). The C1 paragraph and its table row say that one run settles the checked case while the margin absorbs sampling error over the patch, and the claim about automatic promotion without a receiving-side person is conditioned on the receiving side running the same check. AlphaEvolve's database is described as a search strategy inside the exact class, removed from the C4 examples, and relabelled in Appendix B (archive selection inherits the class of the evaluator that scored the archive). Appendix A's sentence on the estimator bias per class is narrowed in the same way.

**Response.** We agree on all three and have narrowed the claims as described. The classes remain a partition for the purpose the paper uses them for, which is to say what gate a deployment can build; the assignment rule is now explicit, and the "one run suffices" claim is scoped to the check rather than to the loss estimate.

## 3. The convergence appendix is inconsistent

**Verdict: correct, and a real error.** Assumption (A5) required infinite cumulative expected descent while the loss stayed non-negative and bounded; summing the one-step inequality drives the expected loss to minus infinity, so the assumptions could not hold together on an indefinitely running process.

**Change.** (A5) is now summable estimator bias alone. The one-step inequality is then of the Robbins–Siegmund form, so the loss converges almost surely and the cumulative expected descent is finite almost surely, as a conclusion rather than an assumption. With proposal coverage strengthened to include a positive acceptance probability for an improving edit, the finite sum implies that the process visits non-gate-stable scaffolds only finitely often, and with effective compactness the limit set is gate-stable. The proposition's conclusion is unchanged; its assumptions are now consistent, and the one reference needed (Robbins and Siegmund, 1971) is added. The body sentence in III-C that pointed to the result is reworded to match (a statement about the gate, not about optimality).

**Response.** We agree. We kept the proposition, repaired rather than removed, because the survey uses gate stability as the vocabulary for what the gated loop converges to; nothing in the corpus findings depends on it, as the reviewer notes.

## 4. The corpus must support the strength of the absence claim

**Verdict: partly correct.** "No surveyed system publicly documents all four properties" is what the coding supports; "has not been built" went beyond it. The denominator sentence about the 14 research systems and SkillOpt was confusing. Independent re-rating is a fair request; it needs a second rater, and we have not done it.

**Change.** "Has not been built" and "remains unbuilt" are replaced throughout (abstract, Sections I, VI, XI) by what the evidence supports: no surveyed system documents the governed second loop. Section V-B now states the denominator in one place: the audit was applied to the 204 core systems and to ten mechanism-level systems that are not rows of the released table; it admits 14 research systems (13 table rows and SkillOpt) and 3 industry exemplars. Section V-C discloses that the scores have not been independently re-rated and names that check as future work. The cover letter states that Supplementary Material S1 to S7, which the reviewer did not receive, is uploaded with the submission.

**Response.** We agree on the wording and the denominator and have changed both. On re-rating: the single-rater design is disclosed, every row carries a one-line justification and is released, and the sensitivity analysis in S2 shows the qualitative findings survive the natural relaxations of the audit; an independent second rating of the audit passers and a sample of the corpus is the right next step and is stated as such in V-C.

## 5. Let the paper stand on its own evidence

**Verdict: a judgment call, and we have met it halfway.** The two earlier papers are the series' explanation of why adaptation belongs in the scaffold, and we keep that argument as its own subsection. The reviewer is right that the survey should not inherit their open assumptions as premises.

**Change.** Section II-B now presents the two earlier results as the hypothesis that explains the pattern the corpus shows, states the scope each rests on in its own terms (one natural-text measurement and reasoning benchmarks for the first; bounded patches of recurring tasks, with a negative result for unbounded domains, for the second), draws the architecture conclusion conditionally on that hypothesis, and ends by saying that the survey's findings in Sections VI to IX stand without it. The abstract says the earlier results "suggest" rather than "explain" why; the conclusion says the corpus is consistent with the hypothesis.

**Response.** The survey's motivation in Section II-A (cost, cadence, and scope of weight updates versus scaffold edits) and its findings do not depend on the earlier papers; those papers say why the pattern should exist, and the corpus is consistent with them. We have made that relationship explicit rather than removing the argument, because the series' claim that the scaffold is the right architecture, not a workaround, is the reason the gap this survey identifies matters.

## Not changed

The literature was not expanded, per the reviewer's advice that the classification, the feedback claims, and the convergence paragraph matter more than another batch of systems.
