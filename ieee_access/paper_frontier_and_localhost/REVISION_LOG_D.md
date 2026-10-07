# Revision log D: light final-pass clarity edits

Scope: clause-level only. No claim, number, citation key, REF token, heading, heading id, table, tag line, figure block, or equation changed. No REF or supplementary pointer added, removed, or moved between paragraphs. No restricted vocabulary introduced. "patch", "tenant", the [Auto × Human] notation, C1–C4, S1–S6, and (a)–(d) all still first appear where they did before.

Checklist keys: **2a** = Pass 2a de-densify (split a read-twice sentence, unpack a noun-stack, verb over nominalization); **FH** = freshest handle / clear antecedent; **T1** = vary clause architecture; **C3** = sentence-opening variation; **T3** = hedge the untested only.

## Edits (48)

### abstract.md (2; word count unchanged at 250: one "and" removed, "That" became "The signal's")
1. "After a failure, teams edit ... far faster than any weight update, and two earlier results ...": split into two sentences at "update." (2a)
2. "That class fixes what the gate can be ...": "That class" became "The signal's class"; "class" had no antecedent (FH)

### sections/I_III.md (11)
3. I, P2, "Read together, they are one adaptation surface ...": split before "The question this survey asks" (2a)
4. I, P3, "What separates them is the signal the gate receives, and its class fixes ...": split; "its class" became "The class of that signal" (2a, FH)
5. II-B, "*Beyond Exponential Decay* ... finds that long LLM outputs ...": dangling "under a tenth of tokens" became "which make up under a tenth of tokens" (2a)
6. II-B, "This article asks where the fixes live ...": "modes are addressed cheaply, inspected, and reversed" became "a fix for a recurring, deployment-specific mode is cheap to make, inspect, and reverse" (modes were being "reversed"; the fix is what is reversed) (2a, FH)
7. II-C, "The prompt-optimization lineage a reader will expect here, OPRO, ...": five-name appositive moved out of the subject–verb span ("A reader will expect the prompt-optimization lineage here: ... . That lineage optimizes ...") (2a)
8. II-C, "What changes here is that the edited artifact persists ...": "must earn, under a second gate, any scope beyond it" became "must clear a second gate before it earns any scope beyond that deployment"; supplementary pointer still ends the sentence (2a, FH)
9. III-A, "For such a mode it locates the scaffold coordinate responsible ...": split after the five-item list; "It then synthesizes one candidate edit ..." (2a)
10. III-A, "The loop measures whether the edit lowers the failure rate on that patch's recurring tasks, the **patch loss**, ...": definition stated directly: "The failure rate on that patch's recurring tasks is the **patch loss**; the loop measures whether the edit lowers it, ..." (the appositive read as attached to "tasks") (2a)
11. III-B, "Loop 1 sets how much one accepted edit changes the local scaffold, the analogue of a step size.": became "In optimizer terms, Loop 1 sets the analogue of a step size: how much ..."; this fixes the misattached appositive and breaks a run of four "Loop N ..." openings (2a, T1)
12. III-C, "It yields a candidate edit $z_t$, proposed by reflection over ... in order of how often ...": became "proposed by reflecting over the accumulated failure history, with modes taken in order of how often and how badly each fails" (2a)
13. III-C, "where $\Omega \ge 0$ penalizes the complexity ... and the breadth of its promotion and $\tau_t$ ...": comma added before "and $\tau_t$" (prose line under the equation; equation untouched) (2a)

### sections/IV_feedback_signal_classes.md (7)
14. IV, P2, "The gate accepts an edit when its estimate ... clears a margin, and condition 1 asks ...": split at "margin." (2a)
15. C2, "Devin's merged pull requests [...], SAGE's ..., SkillRL's ..., and PACE's ... are gates of this class.": predicate moved to the front: "Gates of this class include ..." (four cited items no longer precede the verb) (2a)
16. C3, "The third change defines the class: the rubric that defines the loss ...": second "defines" became "sets" (2a)
17. C3, "A pitch-review system that keeps overrating decks claiming a large market without numbers traces ...": stacked subject split: "Suppose a pitch-review system keeps overrating decks that claim ... . It traces ..." (2a; also varies example introduction)
18. C4, "Research programs, product strategy, and open-ended discovery are of this kind, and automated research pipelines such as the AI Scientist, which ..., are its clearest instance": split; "The clearest instances are automated research pipelines such as the AI Scientist, which ..." (2a)
19. C4, "The dominant failure is drift: ..., and an optimizer in this class cannot be told from random search ..., the indistinguishability Ong et al. report ...": split after the drift clause; trailing appositive became "; Ong et al. [...] report the same indistinguishability for harness optimizers" (2a)
20. "What the class predicts", "... and three predictions follow that Section REF(sec:design) tests.": garden path ("follow that ...") fixed with "follow, which Section REF(sec:design) tests" (2a)

### sections/V_method.md (4; all in V-B)
21. V-B, "The corpus holds systems that either wrap a foundation model ... found in arXiv, ...": split; window now its own sentence, "They were found in arXiv, vendor documentation, and public repositories between January 2023 and the October 2026 cutoff." (2a)
22. V-B, "The patch-local discriminator admits a system ...; systems that carry the labels but fail it ...": split at the semicolon (2a)
23. V-B, "Ten further systems that the text treats at mechanism level, SkillOpt, GEPA, ...": ten-name appositive moved after a colon; one long sentence became three (2a)
24. V-B, "Two kinds of system are excluded: those whose only update mechanism ...": semicolon before "and those with no public evidence" so the second item cannot be read as part of the first item's relative clause (2a)

### sections/VI_findings.md (8)
25. VI-A, "Skills are the most active research substrate: SAGE and COSPLAY ..., Loop 1 ..., SkillChain's ..., a two-stage local gate ..., eleven skill systems ..., and ...": five-item list with an embedded appositive split into three sentences; SkillChain appositive now follows a colon (2a)
26. VI-A, "On orchestration, automated workflow search came first, ...; topologies evolve under evaluation ...": split at the semicolon (2a)
27. VI-A, "MCP registries split into catalogs, such as the official registry, with ... and control planes with ...; none has ...": count announced ("split into two kinds:"), items separated by a semicolon, "None has evaluation-gated promotion." as its own sentence (2a, noun-stack rule)
28. VI-A, "The gradient is not a quirk of the corpus": "The gradient" became "This pattern" ("gradient" was never introduced here, and VI-C uses it for a different axis) (FH)
29. VI-B, "The one field report of anti-recurrence stores written from dead-ends ...": noun-stack unpacked to "stores written from dead-ends to prevent recurrence" (2a)
30. VI-B, "ShareMem gives evaluation tasks to a different user, ... [@qi2026vace]; even Evo2Team's confirmation ...": split at the semicolon (2a)
31. VI-C, "EvolveNet, Evo2Team, and XRepoSkill extend the loop from a single deployment to a federation of them.": "of them" became "of deployments" (singular antecedent) (FH)
32. VI-C, "SkillForge is the clearest case: ...": became "SkillForge illustrates it most plainly: ..."; the previous paragraph opens its example with the same "X is the clearest case:" frame (T1)

### sections/VII_design_space.md (4)
33. "They would enter only if any of versioning, lineage, or rollback counted ..., and then all would land ...": "enter" gets its object ("enter the matrix"); split before "All would then land ..." (FH, 2a)
34. "[Human × Auto] is empty: ... because manual authorship offers automated promotion little leverage.": nominalization became "because automating the promotion of hand-written candidates buys little." (2a, verbs over nominalizations)
35. "[Human × Human] holds MCP registries and a community hub ...; the field study of five public skill repositories ...": split at the semicolon (2a)
36. "Evidence is batched before acceptance, where earlier systems ...": "where" became "whereas" (contrast, not location) (2a)

### sections/VIII_families.md (4)
37. P1, "Five research families ... which we read as evidence ...; the vendors' convergence ...": split at the semicolon (2a)
38. P2, "Across six benchmarks, ... it is best or tied on every cell its authors evaluate, and it reports transfer ... that reads as ...": split; "It also reports transfer ..., which reads as ..." (2a)
39. P3, "Reflective context learning, the most direct independent formalization, started from the observation ..., and its generalization penalty ...": split before "Its generalization penalty ..."; this also breaks a run of five "X started from ..." sentences (2a, T1)
40. Conclusion 2, "AHE, CANTANTE, ... all identify attributing a system-level failure to one scaffold coordinate as what separates descent ...": gerund object moved after a colon: "all name the same step as what separates descent from trial-and-error: attributing ... . That step remains unsolved ..." (2a)

### sections/IX_missing_architecture.md (3)
41. "Read row by row, the partition is plain:": became "Row by row, the partition is plain:" (third "Read X," opener in VII–IX) (C3)
42. "Rollback appears inside single deployments, as edit-level reversal [...] and as an admission test ... [...], and inside one federated round; no system rolls back ...": clauses reordered so "as ..." attaches to "single deployments"; split at the semicolon; supplementary pointer still ends its sentence (2a)
43. "Where the signal is exact, automatically gated cross-tenant promotion of a test-validated skill is low-risk": "is low-risk" became "would be low-risk". The configuration has never been built, so this is a hedge on an untested claim. **Editor: revert if you want the flat normative voice kept.** (T3)

### sections/X_failure_surface.md (1)
44. "Ratchet reports LLM-authored skills at no gain over a no-skill baseline against a double-digit gain for human-curated ones, and attributes ..., which in the vocabulary of Section REF(sec:loop) means ... [@zhang2026ratchet].": became "Ratchet reports that LLM-authored skills gain nothing over a no-skill baseline while human-curated ones show a double-digit gain, and it attributes the gap to lifecycle management [@zhang2026ratchet]. In the vocabulary of Section REF(sec:loop), that means ...". The citation now closes the sentence that carries Ratchet's claim, and the gloss in our own vocabulary stands as its own sentence. Same key, same REF, same paragraph. (2a)

### sections/XI_open_problems_conclusion.md (4)
45. "The two earlier papers of this series showed why ...: errors concentrate in a few key decisions that fail, inside a bounded deployment, in a small ...": the interrupting phrase was removed. The three findings are now separated by semicolons: "errors concentrate in a few key decisions; inside a bounded deployment, those decisions fail in ...; and such a catalogue ..." (2a)
46. "The survey shows how far practice has come toward that loop": "that loop" became "that optimizer"; no loop is named in the preceding paragraph, and its first sentence names the optimizer (FH)
47. "No surveyed system promotes a validated edit across an organization boundary ..., and the signal-class analysis says ...": split (2a)
48. "Reliability comes from governing that specialization, and the instruments that judge each edit ..., so ...": split; the closing sentence is now periodic ("Because the instruments that judge each edit are themselves part of the moving scaffold, the same ... must extend to the gates that judge it.") so the close does not end on four consecutive "The ..." openings (2a, C3)

## Left alone (with reason)

- **I, P2, "A skill file is a procedure ... A repository rule is ... A retrieval connector is ... A tool registry provisions ... A pull-request review ... is a promotion gate"**: five sentences in a row open the same way. I left them: the parallel construction is the argument (each artifact re-read as one optimizer part), and varying one would blur that mapping. Editor's call.
- **I, roadmap paragraph ("Section REF(sec:why) argues ...")**: four REF tokens, above the one-per-paragraph rule. This was there before me, and cross-references are off-limits.
- **I, contribution 4, "read structurally"**: vague, but rewording it would change what is claimed.
- **II-A, "Reinforcement learning from human feedback reduces output diversity ..., and instruction-tuning data rewards ..., so the frontier model is trained to disfavor ..."**: long, but a split would make the "so" follow only from instruction-tuning and narrow the claim.
- **IV, C2, "its signal arrives through a channel an attacker controls"**: possibly needs a hedge ("can control"). I left it: the documented attacks in Table X-1 arguably demonstrate it, and the hedge would weaken a claim. Editor's call.
- **IV, weight-side paragraph, "One group holds the gate fixed while the policy learns, as an instance-specific checklist, ..."**: "as" attaches loosely. Rewording risks re-characterizing four cited methods.
- **V-B, the corpus-count sentence vs. the SkillOpt sentence**: "Of the 256 systems, ... 14 research systems and 3 industry exemplars ... pass the composite audit" reads as if the 14 are among the 256. Two sentences later, SkillOpt (outside the 256) "is counted among the 14". Per S2, the 14 are 13 first-pass systems plus SkillOpt. This is a content inconsistency, not a style one. Not touched.
- **V-C, "The counts of the findings move under two natural relaxations"**: slightly opaque ("move" = change); left as within tolerance.
- **VI-A, "Nine in ten of the most recently added core systems" and the Table VI-1 caption "most recently added 126 systems"**: close in spirit to the restricted "added in 2026" family but not on the list. The caption is off-limits. Not touched.
- **VI-B lead, "each sits in a particular feedback-signal class"**: the second bullet is tagged "(all classes)". This is a mild inconsistency, but fixing it would change a claim or a label.
- **VIII, P1, "have arrived independently at parts of it"**: not the restricted string "has arrived", but a mechanical check on "arrived" will hit it. Pre-existing.
- **VIII, P2, "The gate and a consensus form of credit assignment are load-bearing; the rest are stabilizers."**: a flat inference from one follow-up comparison. It is demonstrated by SkillOpt-Lite, so no hedge added.
- **XI, problem 1, "the bottleneck named by every harness-optimization paper"**: an absolute claim ("every"). It needs an evidence row; flagged only.
- **XI, problem 4, "is the open method"**: slightly opaque, but rewording would alter what is claimed to be open.
- **Pre-existing gate-sense "pass"/"passes" outside V-B**: IV ("pass or fail" twice, "after it passes in a sandbox", Table IV-1 "pass/fail"); VI-A ("pass a human reflection gate"); VI-C ("passes each skill diff"); VII ("they pass only the Loop-2 half", "must all pass"); Table X-1 ("pass the same promotion gate"); Fig. 3 caption. All are the verb sense, not corpus-process narration. I introduced none.
- **"catalogue" (abstract, II-B, II-C as a verb, X, XI) vs. "catalogs" (VI-A)**: mixed US/UK spelling. Left: "catalogue of modes" echoes *The Architecture of Errors* and the supplementary files, and changing the abstract's term is an editor decision.
- **Table tag order**: "Table II-1." (three stages) sits in Section III-D, after "Table II-2." in II-C. Tag lines are off-limits; flagged for the editor.
