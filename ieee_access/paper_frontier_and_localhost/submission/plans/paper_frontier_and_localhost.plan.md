# Plan: Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights
Status: REVIEWED (P1-P4 passed 2026-10-22 with the changes in section 6); open author decisions listed in section 5
Source: `ieee_access/paper_frontier_and_localhost/submission/abstract.md` and `submission/sections/` (body: `I_II_intro_loop.md` to `X_open_problems_conclusion.md`; appendices `appA_formal.md`, `appB_gates.md`)
Last checked against text: commit 5038169 (2026-10-12); revised text checked 2026-10-22 (REVISION_LOG_R.md)
House style: `style/telegrapher_paper_style_guide.md` and `style/telegrapher_final_pass_checklist.md` (no `docs/STYLE_GUIDE.md` exists in this repository). The house style wins on conflicts: no em-dashes, American spelling with "catalogue" and "analogue", mechanism over capability, one claim per paragraph, relationships over raw values in prose.
Companion: `plans/paper_frontier_and_localhost.ledger.md` (S4 diagnostic ledger, R-2 reverse outline, R-4 gap table).

## 1. Frame card

Two frames, side by side. The fresh frame is built from the readers and the problem (R-1); the recovered frame is what the text currently says (S1-R). Every difference is a finding (section 1c).

### 1a. Fresh frame (R-1)

| Field | Content | Status |
|---|---|---|
| Topic | How deployed AI systems turn experience into persistent changes outside the model weights, and what evidence supports keeping those changes and sharing them. | PROPOSED |
| Why it matters | Much of the adaptation a deployed system undergoes now happens in its instructions, skills, memories, tools, and orchestration, so the reliability of deployed AI depends on how those changes are tested before they are kept and before they spread. | PROPOSED |
| Readers | (R1) researchers who build or evaluate self-improving, memory, skill, and harness-optimization systems: they know the methods, and will use the framework to position their work and choose open problems. (R2) engineers and architects who run production agents: they know their platform, and will decide what to automate in their own maintenance and what evidence to require before sharing a fix. (R3) IEEE Access reviewers: they check that every conclusion is supported. | DECIDED (prior rounds; the venue and the practitioner audience are the reason the opening keeps its coding-agent example) |
| Problem type | Mixed, bridged: a practical cost (teams keep changes whose value is unknown, and copy fixes that can harm their recipients) leads to a knowledge gap (no account of which parts of the keep-and-share process the field has built, or of what each kind of feedback can establish), then to the findings, then to the action they enable (what can be automated now and where new evidence or a human decision is still needed). | PROPOSED |
| Shared context | Deployed systems adapt mostly by editing persistent artifacts around a fixed model, and the field calls many such systems self-improving. | FOUND (I ¶1–2; III ¶3 for the label) |
| Condition (one) | Primary, the knowledge gap: no one has mapped which systems test a change before keeping it, which test it again before sharing it, and what their feedback lets those tests establish. Its source in the world: a change that persists is not thereby shown to improve the deployment that made it, nor shown for another deployment. | REVIEWED (P4: make the gap primary; the text states the world condition in I ¶3 and the two questions in I ¶4, never what is unknown) |
| Cost, per reader | R2: rules that conflict or merely lengthen the prompt, outdated memories still retrieved, fixes that help one repository and hurt the next. R1: a researcher cannot say whether a system described as self-improving improved anything, cannot compare two such systems, and may build on a loop that has no gate or no failure record. | R2 FOUND (I ¶3); R1 MISSING in the text, added in I ¶3 from material already in III (the label test) |
| Point | The surveyed systems have built the acceptance test nearly everywhere a local loop exists, but not the failure record and attribution that should feed it, nor governed promotion across organizations; the feedback a deployment receives explains much of this pattern, and in every class an accepted edit is evidence only for the measure and tasks on which it was tested. | FOUND, distributed across I ¶5–7 |
| Themes (2–4) | the acceptance gate (local and promotion); failure record and attribution (credit assignment); promotion and receiving-side evaluation; the feedback class and its measure. | PROPOSED |
| Motive / conflicts | The two prior analyses cited in IX-A are the authors' own (Parts 1 and 2 of a series); they are cited in the third person, stated as a hypothesis the survey does not test, and kept load-bearing as the reason the layer is the right architecture (standing author decision). One author is employed by Palo Alto Networks; the funding and conflict statement is still a placeholder (author item). The survey praises or criticises no vendor beyond what its sources document. | FOUND / OPEN (author paperwork) |

### 1b. Recovered frame (S1-R, from the text as it stands)

| Field | What the text says | Where |
|---|---|---|
| Prelude | A coding agent's naming rule: an engineer adds a line to its instructions; the model has not changed, the deployed system has. | I ¶1 |
| Shared context | The scaffold layer; it changes on a faster schedule than the weights. | I ¶1 last sentence, I ¶2 |
| Condition | "The ease of making a change also makes it easy to accumulate changes whose value is unknown." | I ¶3 |
| Cost | Examples for practitioners only: conflicting rules, outdated memory retrieved, a useful change harmful elsewhere. | I ¶3 |
| Questions | "What evidence justifies keeping a local change? What additional evidence justifies sharing it?" | I ¶4 |
| Point | Split across three paragraphs: uneven development of the loops (¶5), sharing unassembled across organizations (¶6), feedback explains and bounds the evidence (¶7). | I ¶5–7 |
| Last sentence of the introduction | The roadmap paragraph's closing: "Its scores and classifications are released for inspection." | I ¶8 |
| Conclusion | Five open problems, the central observation restated, a three-sentence coda. | X |

### 1c. Differences (findings)

1. **The cost for researchers is missing.** The introduction states the cost in a practitioner's currency only (I ¶3). A researcher reading it is not told what they lose by not knowing which parts of the loop exist. → I ¶3 gains one sentence; no new fact is needed, since the text already states (III ¶3) that the survey tests whether systems publicly described as self-improving correspond to persistent adaptation.
2. **The condition is stated as a world condition and as two questions, never as what is unknown.** The two questions map to the two loops, so they are one condition seen twice, not two conditions. → no structural change; I ¶4's opening can make the unknown explicit.
3. **The point is distributed across three paragraphs and the introduction ends on housekeeping.** Housekeeping after the argument is allowed, but the argument's last sentence (I ¶7) states the feedback finding alone, so the point sentence does not name the gate, attribution, and promotion themes. → I ¶7 ends on one point sentence that names all four themes; the roadmap (I ¶8) stays as housekeeping after it.
4. **The prelude is kept for a stated reason.** A research paper's default is no prelude. I ¶1 is one paragraph, maps every element to the problem's themes, carries no caveat, and hands off directly to the shared context in its own last sentence. Readers R2 and the external reviewer's comment ("the opening example makes that understandable immediately") are the stated reason (decision D1).

## 2. Point outline

Document point and themes: as in 1a. Order of the whole: logical (definition of the loop → evidence base → the local loop in the corpus → why feedback shapes it → the promotion loop in the corpus → how adaptation undermines its own evidence → what governed sharing would require → why the field developed this way → open problems). Decided in round P (D2).

| § | Heading (themed) | Point sentence | Themes | Protagonists | Order |
|---|---|---|---|---|---|
| I | Introduction | The surveyed systems have built the acceptance test nearly everywhere a local loop exists, but not the failure record and attribution that feed it, nor governed promotion across organizations, and the feedback a deployment receives explains much of this. | gate; failure record and attribution; promotion; feedback | the deployed system; the team; the survey | logical |
| II | From a local fix to a measured improvement | Maintenance becomes optimization only when a failure record, credit assignment, a candidate edit, and a gate on a measurable patch loss are all present, and sharing the result is a second decision that needs its own evidence. | local loop; promotion loop; five conditions; gate kinds | the loop; the gate; the team | logical |
| III | Corpus and method | The corpus is read by behavior (artifact, feedback, deciding gate, scope), scored on six substrates, and audited for both loops, and every count states its population. | substrates; two-loop audit; populations | the corpus; the audit; the rater | coordinate |
| IV | What local adaptation actually closes | Detecting a failure is not testing a fix: among recent systems with a local loop the gate is a program in 89 of 96, while the failure record and attribution that should supply it remain incomplete. | gate; failure record; attribution; maintenance | systems (SkillForge, SkillRL, SkillOpt) and their gates | logical (the loop's own order) |
| V | What the feedback allows a gate to know | The class of feedback (exact check, observed outcome, judgment, delayed outcome) fixes what a gate can establish, and so predicts where automatic acceptance and automatic promotion occur. | feedback class; what a gate can establish; predictions | the four classes | coordinate |
| VI | When a local improvement is shared | Local success is not evidence for a recipient: transfers are checked inside one operator, promoted by program in research and by a person in production, and no system joins the learning of the top grid row to the governance of the bottom. | promotion; receiving-side evaluation; gate grid | systems and their promotion gates | logical |
| VII | How adaptation can undermine its own evidence | An improvement loop changes the context of its next decision: accumulated and contaminated artifacts, an evaluator that is itself edited, and structural drift each erode the evidence a gate relies on, and each is answered by a piece of the loop. | accumulation; contamination; reflexive gate; drift | the loop; the evaluator | coordinate |
| VIII | What governed sharing would require | The capabilities exist in different systems but no surveyed system connects them; four properties and receiving-side evaluation define the missing combination, with automation scaled to the feedback. | four properties; receiving-side evaluation | the architecture | logical |
| IX | How the research lines fit together | Each research line built the part of the loop nearest its starting problem, which is why evaluation is more developed than failure capture; the layer sits outside the weights for practical reasons and, on the authors' prior hypothesis, structural ones. | research lines; why outside the weights; neighboring surveys | the research lines | coordinate |
| X | Open problems and conclusion | Five problems remain, one per decision of the loop; the central observation (the local gate is built, governed promotion across organizations is not, and feedback explains much of the pattern) closes the paper. The coda's unconditioned "Reliability comes from governing that specialization" is AUTHOR FLAG X-1 (IX-A states the idea only as a hypothesis). | attribution; recipient evidence; calibration; delayed outcomes; governed sharing | the open problems | coordinate |

Introduction, paragraph by paragraph (target):

| ¶ | role | point | protagonist | themes |
|---|---|---|---|---|
| 1 | prelude + shared context | A deployed system changes without its model changing, and much of its useful experience now lives in persistent artifacts. | the coding agent / the deployed system | persistent artifacts |
| 2 | shared context | The scaffold is the inspectable, revisable layer around the model, and it changes faster than the weights. | the scaffold | scaffold |
| 3 | problem: condition + cost | Easy changes accumulate with unknown value; the cost falls on the team (conflict, stale memory, harmful copies) and on researchers (no way to tell demonstrated improvement from persistence). | changes / the team / researchers | value unknown |
| 4 | problem → questions → the two loops | Two decisions follow, keeping and sharing, which define the local loop and the promotion loop that frame the survey of 256 systems. | the survey; the two loops | local loop; promotion loop |
| 5 | point (part 1) | The local loop is built unevenly: the gate nearly everywhere a loop exists, the failure record and attribution weakly, release machinery without proposals. | the systems | gate; failure record; attribution |
| 6 | point (part 2) | Sharing is less assembled: portable artifacts, checks inside one operator, no governed promotion across organizations. | a change / the systems | promotion |
| 7 | point (part 3) + closing point sentence | Feedback explains the pattern and bounds what any accepted edit shows; closing sentence names all four themes. | the feedback | feedback; measure; (all themes in the closing sentence) |
| 8 | housekeeping | Roadmap and evidence base. | the survey | — |

## 3. Theme registry

| Concept | Locked term | Never use (drift found or likely) |
|---|---|---|
| layer around the model | the scaffold | "harness" for the whole layer (harness is a substrate-specific term in the cited work) |
| decision to keep an edit | the local gate (the gate; "acceptance test" is its plain gloss, defined in II-A as the same thing) | "acceptance check" |
| first loop | the local loop | "local improvement loop" except at the definition in the abstract and Fig. 1 caption; "Loop 1" |
| second loop | the promotion loop; its gate is the promotion gate | "sharing loop", "Loop 2" |
| editable target | coordinate (scaffold coordinate) | "slot" except when quoting harness work |
| tracing a failure to its cause | credit assignment (attribution in prose about methods) | — |
| failure history | failure record / failure log (condition 2 is named "a failure log") | — |
| deployment's workload | the patch; patch loss | "task distribution" for the defined term |
| scope of supporting evidence | evidence radius | — |
| check at the recipient | receiving-side evaluation | "target-side check" |
| feedback classes | C1 exact check · C2 observed outcome · C3 judgment · C4 delayed outcome | "observable outcome" (Table IV-1 cell, VII), "delayed reward" (abstract), "delayed and sparse outcomes" (V-D heading) |
| a judge whose rubric is edited | the reflexive gate | — |
| scopes | USER, PROJECT, STACK, TENANT, CORE | — |
| who decides | Auto, Human, None; a pair written [local × promotion] | — |
| the organizing boundary | across organizations (cross-tenant is a defined synonym in VIII) | "cross-org" |

## 4. Claims ledger

| Claim (where stated) | Supported where | Strength stated vs warranted | Qualifier required | Status |
|---|---|---|---|---|
| Automatic local acceptance in 89 of 96 recent core systems with a local loop (abstract, I ¶5, III, IV ¶3) | released table, refresh rows; Table V-2 caption | "nearly every" = 92.7% of a stated population | the population (recently added, with a local loop) must travel with the number | OK after round Q |
| Failure capture and attribution are weak (abstract, I ¶5, IV-A) | one field report; arrival-order use; harness-optimization papers naming attribution as the bottleneck | "weaker", "often incomplete" | no corpus-wide count | OK |
| No surveyed system connects an automatic local gate to promotion across organizations with lineage, access control, and rollback (abstract, I ¶6, III, VI, VIII, X) | two-loop audit; Table IX-1; S4 | absolute, auditable | "in the public systems examined" (X ¶6) | OK; stated in seven places (redundancy, see ledger 2.5) |
| Feedback class explains much of the pattern (abstract, I ¶7, V-E, VI-D) | grid placements; Table VII-1 | "helps explain" | expectations, not restrictions (V-E ¶2) | OK |
| Three judges report calibration; only SkillCoach audits an edited rubric, offline (V-C, VII-B, X) | cited papers; S6 | narrowed in round Q | judge-assisted audit | OK |
| Receiving-side evaluation is necessary, not sufficient (VI-A) | Evo2Team: nearly a fifth of confirmed transfers fail | stated | — | OK |
| Prior analyses: sparse key decisions; a slowly growing catalogue of failure modes (IX-A) | arbuzov2025beyond; arbuzov2026architecture | hypothesis, not tested here | each limit stated | OK; load-bearing by decision D4 |
| Appendix XI convergence | conditional under (A3)–(A5) | narrowed in round Q | not used elsewhere | OK |

## 5. Decisions log

| # | Question | Options | Decision | By / date |
|---|---|---|---|---|
| D1 | Keep the coding-agent opening as a prelude in a research paper? | keep / cut | keep: practitioner readers; one paragraph; hands off to the shared context | author, round P (2026-10-09), reaffirmed by the external reviewer's note; logged 2026-10-22 |
| D2 | Section order | — | the round-P order (I intro … X open) | author, round P |
| D3 | Loop names | — | the local loop and the promotion loop | author, round O |
| D4 | The two prior analyses | trim / keep load-bearing | keep load-bearing, third person, as a hypothesis the survey does not test | standing author instruction |
| D5 | Score-5 marks on tools and governance | — | MCP, Harvey, Hippocratic AI, AGENTS.md rescored to 3 | author, 2026-10-12 |
| D6 | Headings | relabel to carry themes / keep | keep the round-P headings; they already carry themes except "Corpus and method", which is conventional for a method section | this pass (no author input needed: no claim changes) |
| D7 | Restatements of the cross-organization absence | trim / keep | trim restatements that add nothing to their paragraph's point; keep each instance that carries its own evidence | this pass, under the house rule "honest accounting once"; the external reviewer suggested the same |
| D8 | P4 proposed reordering (V before IV, VII after IV, IX folded into V) | adopt / log as proposal | log as a proposal only; D2 stands (author's round-P order; the external reviewer asked to preserve the structure) | this pass; open to the author |
| D9 | One home per repeated caveat | — | (a) evidence is bound to the measure and tasks tested: stated in II (closing of II-A/II-B), pointed to elsewhere; (b) local success is not evidence for a recipient: defined in II-C, developed in VI-A; (c) a delayed outcome cannot credit one edit: V-D. Other occurrences shrink to a clause or a pointer, keeping every citation and number in the same file | this pass (D7 generalized) |
| D10 | Section openings | — | IV, V, VI, VII open by stating their finding at the end of the opening segment (VI's finding, now in its last sentence, is forecast in VI's opening); V's opening links back to IV (why the gate differs by feedback); VII's opening links back to VI (evidence degrades after promotion) | this pass |
| D11 | IX-A and IX-B sit under "How the research lines fit together" | move / retitle / keep | keep (moving touches cross-references; D6 keeps headings); proposal to the author | open to the author |
| D12 | Unconditioned coda in X ("Reliability comes from governing that specialization") | restore "on that hypothesis" / keep | keep the claim strength; AUTHOR FLAG X-1 | open to the author |
| D13 | Section IV has five subsections (house limit four) | merge / keep | keep (D6); a paragraph may move across a subsection boundary where its role belongs to the neighbor | this pass |

## 6. Review record

- **P1 frame complete** (fresh frame vs recovered frame, every difference recorded in 1c): pass after the P4 changes above (condition stated as a knowledge gap; R1 cost added).
- **P2 point outline**: the section point sentences, read in order, make the argument; each serves the document point. Pass, with the Section X sentence corrected so it does not assert the flagged coda.
- **P3 theme registry**: locked terms set in section 3; the S4 ledger found drift in "change/edit/revision", "local improvement/adaptation loop", "artifact-layer optimization/descent", "attribution/credit assignment", and "observable outcome"; all fixed to the locked term in this pass except definitions.
- **P4 cold plan review** (Sonnet subagent, plan only, 2026-10-22). Findings and dispositions: (1) reordering proposals: D8, not adopted. (2) Condition packs two claims plus an unknown: adopted (1a). (3) R1 cost vague: adopted (1a). (4) Intro point spread over ¶5–7: adopted as one closing point sentence at the end of ¶7 (1c item 3). (5) Make the IV→V and VI→VII links visible: D10. (6) Claim-level objections: absence claims are already scoped to public evidence ("documents", "in the public systems examined"); "explains" is already "helps explain" in the text; the plan's "most of the adaptation" was corrected to "much"; single rater is stated in III; the X coda is AUTHOR FLAG X-1 (D12).
- **Restructure verdicts** (R-4 gap table, see the ledger file): re-draft 42 paragraphs (A: I_II:1, 6, 7, 14, 21, 29; B: III:10, 12, IV:2, 5, 6, 9, 14; C: V:5, 6, 13, 15, 18, VI:3, 6, 10, 12, 15, 16, 17; D: VII:2, 4, 7, 9, 12, 13, IX:7, 14, 15; E: X:2, 3, 4, 5, 8, appA:4, 5, appB:2); polish all others. Prelude I_II:1 is re-drafted inside the prelude gate, not cut (D1).
- **S6 cold read** (Sonnet, revised text only, 2026-10-22). Problem and point recovered as in 1a. Section points found in the opening for I, IV, V, VI, VII, VIII, appendices; later for II (its subsections carry it, by design: II opens on the example), III (method), IX (fixed: IX now opens on why the loop is uneven), X (conclusion, acceptable). Prose fixes applied: VI's grid described before its rows are named; I ¶7 closing sentence split. Claim-level objections (single rater not in the abstract; post hoc class assignment vs "predicts"; convergence of research lines read through the five conditions; unconditioned coda; absence claims) are author flags in REVISION_LOG_R.md, not argued away in prose.
- **S7**: invariant diff PASS (citation-key multiset, numbers, REF tokens, headings, tables, captions, raw LaTeX, display math, bold terms; per file). Builds and gates PASS (see REVISION_LOG_R.md).
