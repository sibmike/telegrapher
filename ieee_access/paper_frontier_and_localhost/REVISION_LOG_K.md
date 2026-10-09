# Revision log K: corrections from the corpus enrichment review (2026-10-08, night)

The `research_gpu` enrichment pipeline (gpt-oss-120b and Qwen3-Next-80B on Bedrock) was run over the whole corpus (237 of 256 systems produced an output; `skill-federation-mvp/research_gpu/v7_corpus/`), each output was reviewed against its source and against this paper (237 machine-assisted reviews, 60 contradictions found), and the 22 highest-ranked contradictions were verified by two independent readers each, one starting from the source text and one from the paper, with block-level quotes (`v7_corpus/verification.md`). The author's instruction: "do what is honest to the papers and the research; if we have to change we change." Fifteen items were confirmed and applied; the rest were judged a difference of emphasis or left to the authors.

## Recodes that move counts (both readers agreed, confidence 4 to 5)

- **RASO** (arXiv 2609.38024) optimizes one skill for one task; the public corpus is an inbound source and nothing leaves the deployment. Section VII already said so; the supplementary listed it as a promoter in six places and the released row coded Loop 2 as Auto. Now [Auto × None], governance (a); "seven second-pass systems promote without lineage" is six everywhere (S2, S4, S6, VII, Fig. 3); "the first six enter only if" is five.
- **SkillForge** (arXiv 2604.08618v2): the judge that agrees with people more than nine times in ten classifies customer replies and forwards bad cases; the optimizer commits each skill rewrite without an acceptance test; humans review replies, not skill versions; no skill version is promoted beyond the scenario deployment. Now [Auto × None], out of the composite-audit passers; removed as the [Auto × Human] exemplar in Sections III, IV, VII and from the grid figure; Table IX-1 row recoded ((b) none); S4/S6 cells and lists updated.
- **SkillRL** (skillrl2026): the 0.4 success-rate check triggers teacher proposals and the bank update is an unconditional union, which is the paper's own definition of an unchecked step. Loop 1 None; out of [Auto × Auto] and the passers; Section IV names it as a trigger, not a gate; Appendix B's "RL threshold" row no longer lists it.
- **AutoAgent** (arXiv 2603.09716): an uncalibrated consistency judgment on text revisions to one agent's own tool and peer descriptions; per-agent store; no promotion. Now [Auto × None]; named as such in Section VII.

Net: composite-audit research passers 14 to 11 (table rows 13 to 10, plus SkillOpt); [Auto × Auto] research systems 12 to 10; [Auto × Human] 4 to 3 (CASCADE, Sierra Agent OS 2.0, Cognition Devin); ungoverned second-pass promoters 7 to 6; the S2 relaxation counts follow. The three industry exemplars, the 204/52 corpus split, every substrate score and mean, and the headline claims (no governed cross-organization promotion; the field varies on the promotion gate) are unchanged. Fig. 3 (corpus flow) regenerated with 11 and 6; Fig. 4 (gate grid) relabeled.

## Wording and evidence corrections (both readers agreed)

- **VACE** gates a harness revision against the same run's freshly trained checkpoint: a Loop 1 gate on no rung. Removed from VII's crossings and from the receiving-side evaluation list (VII, S6).
- **DGM** admits every child that compiles and still edits code; the score weights parent selection. Section IV's "accepts only after it passes" and S4's "[Auto × Human] mode" overstated the gate; both rewritten. S4 now also records SkillRL's placement in the same sentence.
- **Instruction files.** Two controlled studies exist and disagree on cost: Gloaguen et al. find instruction files raise inference cost by about a fifth and buy nothing in task success; Lulla et al. (arXiv 2601.20404, the S1 row's own source, now cited as `lulla2026empirical`) find a root AGENTS.md cuts median wall-clock time by about 29% and median output tokens by about 17% in a paired run on 124 pull requests, leaves total tokens flat, and measures no correctness. Section VI says so; S6's two rows that said "the one controlled study" were left for the authors (flagged in the plan's unresolved list).
- **OptiMAS** has no accept-or-reject step; the validation score informs the edit. Section VI's gated-orchestration sentence names AgentGrad and HarnessForge, with OptiMAS described as evaluation-informed, and the lead clause reads "evaluation-gated or evaluation-informed".
- **EDDOps** gates registry promotion on numeric thresholds before a human sign-off; VII's "none with evaluation-gated promotion" became "EDDOps gating promotion on evaluation thresholds before a human sign-off; none generates the candidate from a failure". S7's RBAC sentence reads "does not implement".
- **VerMem**'s verifiers act only at training time and it has version retention, not rollback; Section VI's ledger sentence and S6's rollback list corrected; the released row's gate and governance wording corrected.
- **VALVE** never reverts an accepted edit; S6's "held-out gates with rollback" sentence now credits rollback to SkillSmith and SkillAudit only.
- **Co-Harness** has a held-in and held-out exact-answer gate, a versioned diff registry, and demonstrated rollback: released row recoded (class C1,C2; (c) partial, (d) within one run); added to S6's (d)-holder enumeration.
- **GRACE**'s evidence line now reports the v2 value (pass^3 0.661; v1 reported 0.673).
- **Mem0**'s May evidence line replaced with figures the cited paper (2504.19413) supports.
- **Appendix B, Table B-1**: EvolveR moved from "RL threshold" to "Semantic merge" (cosine pre-filter plus LLM equivalence judgment); SkillRL removed from "RL threshold"; "LLM judge with calibration" now lists SkillChain's judge stage; CASCADE's user-click-gated write moved to "Reviewer judgment". A raw Greek kappa pasted by one edit was converted to math; the SkillChain kappa range in S6 was flagged by the review (Table 8 of the source reads 0.32 to 0.91, mean 0.62) and is left for the authors to check.
- **AutoManual** removed from S6's "First" row estimator list (its Builder writes rules by judgment; its Consolidator prunes).

## Records

Dated notes for every item are appended to `CLAIMS_AUDIT.md`. The released rows changed are in `supplementary/p3_refresh_2026-10.csv` (RASO, VerMem, Co-Harness, GRACE) and `supplementary/p3_master_scores.csv` (SkillRL, AutoAgent, SkillForge evidence lines; Mem0); the arXiv package mirrors them at build. `check_revision.py` ALLOWED_NEW gained `lulla2026empirical`. The release table `v7_corpus/corpus_enrichment.csv` was rebuilt so its paper-coding columns carry the corrected rows.

## Gates

`check_revision.py` PASS, (c) 0 hits; `recount.py` reproduces the refresh-row cells ([Auto × Auto] now 5 of the refresh rows: Evo2Team, EvolveNet, Future AGI, ShareMem, XRepoSkill); `verify_ieee.py` PASS (22 pages, 10 tables, 150 references); `check_cites.py` 150 = 150; arXiv v4 82 pages, 180 references, 0 undefined; every changed page rendered and inspected.

## Left for the authors (from the plan's unresolved lists)

S6 rows 45 and 57 still say "a controlled study" for instruction files; VerMem's released class (C2/C3 is the training reward, the run-time gate is a validity check); Mem0's May row venue is a bare "arXiv"; whether OptiMAS's Loop 1 should stay Auto under the strict "who decides" reading; whether to add a "threshold trigger with unconditional merge" family to Table B-1; the SkillChain kappa range.
