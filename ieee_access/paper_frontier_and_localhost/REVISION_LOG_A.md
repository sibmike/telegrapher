# Revision log, Phase A (abstract, Sections I–XI, wording fixes in Appendices A and B)

Writer A, 2026-10-07. Source of truth edited in place: `submission/abstract.md`, `submission/sections/{I_III, IV_feedback_signal_classes, V_method, VI_findings, VII_design_space, VIII_families, IX_missing_architecture, X_failure_surface, XI_open_problems_conclusion, appA_formal, appB_gates}.md`. Snapshot for comparison: `submission/sections_before/`. Nothing was built or run beyond read-only grep/diff/wc checks.

## Summary of mechanical checks (run by hand with grep/diff, mirroring `scripts/check_revision.py`)

- **Citation keys.** Key set before = after: 168 keys, none added, none dropped (abstract + body + appA + appB + S7). Occurrence counts change for three keys, each forced by the plan: `@gloaguen2026agentsmd` 2 → 1 and `@shen2026revoked` 2 → 1 (duplicate material given one home, per the duplicates table); `@wang2026assay` 1 → 2 (inconsistency 4: the same four citations now back "eleven" in VI and VIII). Note for the editor: check (a) of `check_revision.py` subtracts Counters, so it compares multisets and will print these three as REMOVED/ADDED although the key set is unchanged. Its own message ("same key set") suggests a set comparison was intended.
- **Banned vocabulary.** Zero hits outside V-B, using the checker's own regex list plus "has become" and "the corner". The only hit in the body files is the window sentence in V-B ("October 2026 cutoff"), which is allowed. Appendix A keeps its own (A1)–(A5).
- **Removed labels.** Absent from abstract and body: "Claim IV-", "(A2)", "single-loop boundary", "Loop 1 = None", "$n = 1$", "PP", "assumption (i)…(vi)", "Condition (iii)/(iv)/(v)", "the corner". Absent from appA: "assumption (iv) of Section".
- **Definition before first use** (same patterns as check (d)). `[L1 × L2]` defined and first used on the same line in III-C ("Loop 1 first"); C1–C4 first used in Table IV-1; properties (a)–(d) first used at their definition in IX; `tenant` first used at its definition in III-B (II-A no longer uses the word); `patch` first used at its definition in III-A (I ¶2 and II-B no longer use the word); evidence radius and receiving-side evaluation defined in III-A before any use; S1–S6 used only after Table V-1 (the "S3" in V-A's opening sentence became "the memory substrate"); core/contrast corpus, discriminator, and composite audit first appear in V-B; the three industry exemplars are named once, in V-B.
- **Supplementary pointers.** All eight are in the form "(Supplementary Material S<n>)" at the end of a sentence; none is the subject of a sentence.
- **Pointers per paragraph.** At most one in every prose paragraph except the single roadmap sentence of Section I (seven REF tokens), which the plan asks for. See "Judgment calls" below.
- **Numbers.** Every digit string that left the prose is accounted for (list per subsection below; summary: 92, 102, 126, 31 → Table VI-1 caption; 130, 269 → Fig. 3 and Appendix C; 7 → Fig. 3 and Appendix C (and "Seven" in VII prose); 435 → Table II-2; 0.72, 0.91 → Appendix G, row IV-3; 254 stays in VII). Numbers that newly appear in prose are relocations only ("2.0" from "Sierra Agent OS 2.0", now named in V-B and VII; one more "256" in the new Introduction paragraph).
- **Tables.** Row diff against the snapshot: II-2, V-1, VIII-1, A-1 unchanged; II-1 moved unchanged except the stage-3 "Dominant failure" cell; IV-1 changed only in the two headers the plan names; VI-1 two cells reworded (see VI-A); VI-2 "in 2026" removed and one cell reworded (plan); X-1 one pointer changed (plan, inconsistency 9); B-1 one cell changed (plan). All caption tag lines kept; Table IX-1 is new, with its tag line "Table IX-1. …" directly after it and cited as "Table REF(tab:IX-1)". All `{#sec:…}` ids, all REF targets, all four figure blocks, and both equations kept. Every REF target resolves to an existing label.
- **Length.** Prose words (abstract + body, tables, captions, headings and figure blocks excluded): 8,780 → 7,951 (−9.4%). All text in those files including tables: 10,894 → 10,289 (−5.6%). Below the 15% target; see "Could not do" below.

## Abstract

- Reordered as the plan specifies: phenomenon → the loop → signal class fixes the gate → finding (local loop routine; governed promotion absent) → failure surface and open problems. Opens with the plan's sentence.
- The prior-papers sentence became a clause ("two earlier results of this series explain why that layer is the right place: errors concentrate in a few key decisions that fail in a small, recurring catalogue of modes").
- "cross-organizational promotion" kept as "promotion across organizations"; no "tenant".
- **Cut:** the survey window "from January 2023 to October 2026" (the brief bans "October 2026" outside V-B; the window now lives only in V-B). Process wording removed. 249 words, one paragraph (the arXiv assembler embeds it as a single YAML line).

## I. Introduction

- ¶1 and ¶2 kept. Two word changes: the list in ¶1 lost its repeated "in" (no content change); in ¶2 "memory access specific to one patch of work" → "specific to one workflow", because "patch" is now defined in III-A and must not appear first in an undefined sense.
- **Added** ¶3 (result in plain words): the local loop is routine (wording from XI: "closes under an automatic gate in most research systems and a growing number of production ones"); the governed second loop appears in none of the 256 systems; the signal class fixes which loop a deployment can close (exact or observed outcome can gate automatically; a judgment only once calibrated against people; a delayed reward not edit by edit). Every clause restates a claim already in IV, VI, IX, or XI.
- Contributions: five one-line items without "It … (Section …)". "cross-tenant" → "cross-organization" in item 5. One roadmap sentence follows.
- Last paragraph replaced by the plan's two sentences. **Cut:** "an audit of every absolute claim against the October-2026 literature (Supplementary Material)" (process narration).

## II. Why adaptation lives outside the weights

### II-A Breadth in the weights, depth in the scaffold
- Kept, tightened. Last sentence now states the scaffold's properties plainly ("Adaptation lands in the scaffold, the one substrate that is cheap, inspectable, reversible, scoped to one customer, and updatable daily"); "In the surveyed corpus they appear rarely" → "in practice they are rare".
- "tenant" replaced by "customer"/"deployment" throughout II-A ("contradictory preferences between customers", "one customer's idiosyncrasies", "fine-tuning per customer", "per-customer adapters", "scoped to one customer"), so that "tenant" is first used where III-B defines it.

### II-B Why the scaffold is the right architecture: the two earlier results
- Retitled per plan. Two short paragraphs; one sentence per prior paper, both citations kept, the "under a tenth of tokens" figure kept.
- "not a patch on an inadequate model" → "not a workaround for an inadequate model" (avoids the undefined "patch"; matches the subsection title).
- **Deviation:** the subsection does not *end* on "This article asks where the fixes live." That sentence opens the second paragraph's argument ("This article asks where the fixes live, and the corpus answers: in persistent artifacts outside the weights …"), and the subsection ends on the architecture claim. Ending on the question after its answer would read as a bridge sentence; the house style asks sections to end on their finding. Easy to revert if you prefer the literal ending.

### II-C (old II-C) Three stages
- **Moved** to the end of Section III as III-D. See there.

### II-C (old II-D) Relation to existing surveys
- Opens with two plain sentences naming the four axes in words (loop closes at all; gate is a program or a person; what the gate can observe; promotion governed) and pointing to Table II-2. Table II-2 unchanged.
- Three short paragraphs: (1) what existing surveys classify by, ending with Ding et al.'s verdict **moved here from X** ("concentrated on accumulating and retrieving state rather than on governing, recovering, or relinquishing it", `@ding2026alwayson`); (2) prompt-optimization lineage "optimizes a prompt or program once against a development set and is not a deployed loop" (replaces "sits in the contrast corpus"); ACE now "persists its artifact but keeps it inside one context and never promotes it" (replaces "single-loop boundary"; wording from S4.1.2 and S7.2); (3) three nearest precedents and the one condition that changes, ending "(Supplementary Material S7)".
- 435 left the prose here (it was in X's prose); it remains in the Table II-2 row.

## III. The loop: artifact-layer descent

### III-A The loop in plain language
- First sentence: "We call this loop artifact-layer descent: the disciplined version of scaffold maintenance, run again and again over the life of a deployment." (The colon supplies the antecedent the bare plan sentence lacked.)
- Split into two paragraphs: local loop / promotion.
- Four definitions set in passing, in bold: **patch** ("the slice of users, tasks, and conventions it handles"), **patch loss**, **evidence radius**, **receiving-side evaluation** ("a check run where the edit arrives, not where it was made").
- Fig. 1 block unchanged.

### III-B Two loops, two knobs
- Example paragraph kept; "a cross-tenant skill registry" → "a skill registry shared across companies" (tenant not yet defined at that point).
- Scope paragraph adds the gloss of all five scopes, with **tenant** defined as "one organization or customer". The glosses (USER = one person's account or fork; PROJECT = one repository, workflow, or product workspace; STACK = a curated bundle of projects under one team; CORE = shared by every tenant) are the series' own definitions, taken from the earlier Frontier-and-Localhost manuscripts (`arxiv/frontier_and_localhost/paper_frontier_and_localhost.md`, scope paragraph). Fig. 2 block unchanged.

### III-C When the loop is an optimizer
- The five conditions are now the only numbered list of requirements. Both equations kept verbatim.
- Former III-D *Assumptions* folded in: (i), (ii), (vi) became one sentence on the setting ("The conditions presuppose frozen frontier weights, edits that persist as inspectable artifacts …, and promotion that widens an artifact's scope under a gate rather than averaging …"); (iii)–(v) deleted as duplicates of conditions 1, 3, 5. The Appendix A pointer now says "Under further assumptions on the gate's bias and the proposal process, the update satisfies a one-step descent inequality and converges, informally, to a gate-stable scaffold … (Appendix A)".
- After Auto/Human/None: "We write a system's two gates as a pair, Loop 1 first: [Auto × Human] means an algorithmic local gate and a human promotion gate."
- Closes with the hinge, renumbered: "Condition 1 says the loss must be measurable. It does not say what measures it, and that turns out to be the question that sorts the corpus."

### III-D Three stages of scaffold maintenance (moved from II-C)
- One paragraph plus Table II-1 (tag line kept as "Table II-1." so `REF(tab:II-1)` still resolves; the printed number is automatic).
- **Inconsistency 1 settled.** "In the surveyed corpus, production deployments sit at Stage 1 or 2" → "Production deployments reach Stage 3 on the local loop only behind a human promotion gate, as Spotify, SkillChain, and SkillForge do." Evidence: Appendix G (S6.4), first row, verdict "sharpened": Spotify runs automated prompt and planning optimization behind human launch and A/B metrics, SkillChain runs judge-monotone edits behind a human reflection gate. Citations for Spotify and SkillChain moved with the names (`@palumbo2026spotify`, `@hu2026skillchain`); SkillForge is cited at its first mechanism description in IV.
- Stage-3 "Dominant failure" cell filled: "(the discipline this article describes)" → "Evaluation fragility".

## IV. Where the signal comes from

- Opening paragraph kept. Second paragraph cut from four pointers to one; "the paragraphs that follow give one example per class" dropped.
- Table IV-1: only the two headers changed: "Reachable cells (Sec. VII)" → "Gates the class permits (Loop 1 × Loop 2)"; "Dominant failure (Sec. X)" → "Failure that dominates (Sec. REF(sec:failure))" (kept as a REF so the arXiv build renumbers it).
- C1: "$n = 1$, Section VII" → "accepting on a single evaluation".
- C2: pointer to Section X dropped (one pointer per paragraph; the table column carries it).
- C3: split into two paragraphs (the two measurement problems / the reflexive gate). "(A2) of Appendix A" → "the bounded-bias assumption of Appendix A". The pitch-review case is now inline in two sentences; the pointer to the Appendix A worked case and to the eval-fragility row of X were dropped.
- C4: unchanged in substance.
- Weight side: five sentences whose point is the reflexive gate; all twelve citations kept in bracketed groups. **Counts moved:** "Of fourteen such papers we checked, thirteen are methods and one is a survey; … eight hold … fixed …, five co-evolve …, five report agreement …, none of the co-evolving ones does" → only the meaningful clause stays ("none of the co-evolving methods reports agreement with human judgment (Supplementary Material S6)"). The tally lives in Appendix G (S6.5, row IV-3: 14, 8, 5, 5) and Appendix H (S7.3: fourteen, eight, five, five). "three systems report judge calibration" stays.
- "What the class does to the design space" → "What the class predicts": three plain predictions, no "Claim IV-n", no audit sentence, one pointer to VII, where they are confirmed.
- **Deleted** the last paragraph (should the gap be filled, by class). Its content lives in IX (by-class paragraph), and its one claim not already there ("safety-critical domains … are C3 or C4 domains with high stakes; the class, not the domain, carries the argument") was moved into IX.
- **Inconsistency 10 settled** by this deletion: its two wrong pointers ("Section IX names safety-critical domains", "the receiving-side evaluation that Section VI finds absent") are gone; VI-B says "rare".

## V. Substrates, corpus, and scoring

### V-A Six substrates
- Table V-1 unchanged. "The three kinds of memory on S3" → "on the memory substrate" (S-labels now appear only after the table).
- Rubric paragraph split in two: the rubric itself; then the single home of "why governance substrates can score 5 without an inner loop", now also carrying the sentence moved from VI-A ("which is why MCP and the prompts-as-code platforms score 5 there and still sit outside the two-loop cells").
- Partition paragraph keeps the invariance argument and gains the finding moved from VI-A ("every integrated system in the corpus has a recognizable instance of each substrate, under different names").

### V-B How the corpus was assembled (the only place process is narrated)
- Inclusion rule and window in one sentence; scoring-from-source sentence kept; two filters with Fig. 3; one sentence of totals (256; 204 core / 52 contrast; 14 research systems and 3 industry exemplars, the exemplars named once: Sierra Agent OS 2.0, Cognition Devin, Letta's Context Repositories); exclusions in one sentence.
- **Moved out:** the two-pass history and the query families (to Appendix C, Phase B); the seven-promoters sentence (to VII); the vendor-documentation flag (to V-C).
- **Counts:** 130 (first pass) and 126 (second pass) → Fig. 3 ("130 by May 2026, +126") and Appendix C (S2, "Corpus size"); 269 substrate rows → Appendix C (S2); 7 → Fig. 3 and Appendix C (S2, relaxation (a)); 204, 52, 14, 3, 256 stay.
- **Settled an inconsistency not on the list:** the old sentence said the first pass "kept those that wrap a foundation model with at least one persistent artifact" (and), while the contrast corpus contains systems with no persistent artifact (Self-Refine, ReAct, S4.1.1) and Appendix C states the inclusion rule as "(a) … or (b) …". V-B now reads "either wrap a foundation model with at least one persistent artifact updated from deployment signal or are described in public as self-improving, scaffolded, or agentic", matching Appendix C. Please confirm.
- **For Writer B (Appendix C), the removed text that needs a home there:** "The corpus was built in two passes with one rubric. The first pass (January 2023 to May 2026) searched arXiv, vendor documentation, and public repositories … The second pass (June to October 2026) ran query families for self-evolving skills and skill lifecycle, harness and context optimization, agent memory governance, prompt-as-code and evaluation-gated promotion, federated or multi-tenant skill sharing, and multi-agent topology evolution, and it followed the citations of the systems the first pass had identified as closest to the gap of Section IX." (The current S2 "Survey window and dating" names three strands, not these six query families.)

### V-C Evidence and scoring discipline
- The one home for method caveats: uneven evidence and one rater (topic sentence), tiers in words with "(T1 to T5 in the released table)", single-rater scoring, half-scores and rounding down, vendor-documented systems flagged (moved from V-B), released table (S1), and the two relaxations defined in a clause without (a)/(b) letters (S2).
- **Deviation:** written as two short paragraphs instead of one, because the caveats need two supplementary pointers (S1 for the table, S2 for the sensitivity analysis) and the brief allows one pointer per paragraph. Merge them and drop one pointer if you prefer.

## VI. What the corpus shows (retitled from "Findings: substrate maturity and four clusters")

### VI-A Maturity is uneven (retitled; "and the 2026 additions did not change the ceiling" dropped)
- Opens with the headline, then the ratio in words once: "Nine in ten of the most recently added core systems close the local loop under an automatic gate, and none of them reaches the top mark on any substrate."
- **Deviation in wording:** the plan's topic sentence is "The local loop has become routine; the governed second loop has not moved." `check_revision.py` bans "has become routine", so the sentence is "The local loop is routine; the governed second loop has not been built." (the thesis wording).
- Table VI-1: the column explanations moved from prose into the caption. **Counts moved to the caption:** 126, 102, 92 (plan), and 31 (the number of skill systems among the most recently added 126; it had no other home with that meaning). The phrase "the most recently added 126 systems" appears once, in the caption. "(May 2026 corpus plus October 2026 sweep)" and "No system added in 2026" removed.
- **Two Table VI-1 cells reworded** (not in the plan, needed to clear the banned list): S3 "Lineage now shipped in products" → "Lineage shipped in products"; S6 "2026 registries add lineage and rollback" → "registries add lineage and rollback". Rows, values, and the rest of the text unchanged.
- The 330-word paragraph became three themed paragraphs with all their citations: content substrates (topic: only two systems reach the top mark there, both inside one research environment); memory ("no system both gates writes and corrects from failures"); tools and governance (one pointer back to V-A for the score-5 point). Then "No system matures all six substrates at once …", ending on "it tracks which constraints each kind of system was built to satisfy."
- "Loop 1 = None" → "none of them has an inner loop".
- **Cut or moved:** "the result we were not looking for", "2026 sweep", "May corpus"; the "First … score of 5 on S4 or S6" point (→ V-A); "the six substrates recur" (→ V-A); "one deprecation in 254 edits" (→ VII only; 254 stays there); the revoked-facts figure (→ VI-B only, `@shen2026revoked` once); the duplicated "context files raise cost" claim stays here and leaves VI-C (`@gloaguen2026agentsmd` once).
- **Inconsistency 4 settled (VI side):** "eleven skill systems treat retirement as a gated operation" now carries the same four citations as VIII (`@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay`). Evidence for "eleven": Appendix G (S6.4), pruning/expiry row.

### VI-B Five absences, read by signal class
- Bullets, point first, two sentences each, exceptions by name. "Versioned memory has arrived; enforced correction has not" → "Memory is versioned, but correction is not enforced" (banned "has arrived").
- Receiving-side bullet: "It now exists in …" → findings voice; the four systems named with their mechanism; Evo2Team's misses as a fraction ("nearly a fifth of its transfers fail on new graphs"); the exact 4 of 22 lives in Appendix G (S6.4, "Held-out evals at Loop-2 promotion" row). The inference sentence ("the missing piece that would catch a scaffold over-fitting one deployment before it propagates") moved to IX, its single home.
- The pointer to Section IV was dropped (IV is the preceding section; one pointer budget used elsewhere).

### VI-C Four clusters
- Table VI-2: "in 2026" removed from four cells; the production-hybrid cell "the 2026 entries add online A/B gating and reported judge agreement" → "Spotify and SkillChain add online A/B gating and reported judge agreement". All systems, citations, and other cell text unchanged.
- Each paragraph: what the cluster shows → one system at mechanism level → what all members lack. Research full-auto: all seven member citations carried in one bracketed group; AlphaEvolve (with FunSearch) at mechanism level; NanoResearch, AutoAgent, SkillOpt, DGM, ADAS, Voyager mechanism clauses cut (NanoResearch and DGM mechanisms are in IV, SkillOpt's in VIII). Production hybrid: SkillForge at mechanism level; SkillChain's kappa range 0.72–0.91 left the prose → Appendix G (S6.5, row IV-3, "κ 0.72–0.91"). Governance-first: unchanged in substance. Open standards: vendor convergence in one sentence pointing to VIII; the duplicated Gloaguen sentence removed; "What the cluster lacks is adaptation …" ends the section.

## VII. The two-loop design space

- Opening: one sentence; the subject-position pointer "Supplementary Material S4 lists the named membership" became "(Supplementary Material S4)" at the end of the cell paragraph.
- Figure caption (inside the kept figure block) now states the convention: "Rows give the Loop 1 gate and columns the Loop 2 gate, so a cell [Loop 1 × Loop 2] such as [Auto × Human] pairs an algorithmic local gate with a human promotion gate." ($\times$ used inside the raw LaTeX.) Rest of the caption unchanged.
- Occupancy: one sentence per occupied cell, no arithmetic. **Counts:** "twelve from the May corpus" → Appendix E (S4.2.1, "[Auto × Auto] is most populated (twelve systems)"); "Those twelve plus two are the fourteen" deleted (14 stays in V-B).
- **Inconsistency 2 settled.** Rows used: `supplementary/p3_refresh_2026-10.csv`, row "Letta MemFS + Context Repositories + Dreaming (2026 refresh)" (master_alias "MemGPT / Letta"): loop1 = "Auto (dreaming); optional Auto agent-review gate", loop2 = "Auto (shared-memory git push across agents; versioned, no eval gate)", key_evidence "shared memory across cloud agents auto-pushed". → Letta's Context Repositories placed in **[Auto × Auto]**, "which push shared memory across agents automatically, with git lineage and no evaluation gate". `supplementary/p3_master_scores.csv`, rows "INTEGRATED, Sierra Agent OS 2.0" (key_evidence "… hybrid AI+human gate") and "INTEGRATED, Cognition Devin" (key_evidence "… 67% PR merge rate; human gate"); neither has a refresh row; both → **[Auto × Human]**, consistent with S4.2.1. Named in the sentence. (The loop1/loop2 columns exist only in the refresh CSV; the master CSV has no such columns, so for Sierra and Devin key_evidence was the evidence.)
- Seven cross-context promoters: one paragraph about systems; ends "(Supplementary Material S2)". **Settled a small contradiction** in the old text ("Its seven cross-context promoters land in [Auto × Auto] …; its one production loop lands in [Auto × Human]", although Spotify is one of the seven): refresh CSV rows give loop2 = Auto or Auto-partial for EvolveNet, Evo2Team, XRepoSkill, ShareMem, RASO, Future AGI and "Human (launch / A-B)" for "Spotify conversational-recommendation loop". New text: "all would land in [Auto × Auto] except Spotify's production loop, which lands in [Auto × Human]; none opens a new cell."
- "Other cells" paragraph kept (now the single home of "one deprecation in 254 edits"); "remains empty" → "is empty".
- **Added** the confirmation of IV's three predictions in plain prose, from the evidence the old IV audit sentence summarized ("the first two hold without exception and the third is sharpened by the three scaffold-side calibration figures"); details match Appendix G (S6.5, rows IV-1 to IV-3).
- Cross-cutting findings: findings first; batching stated as a finding with the trend as a clause ("where earlier systems accepted an edit on one evaluation …"); the $p^k$ versus $1/k$ sentence shortened to "Requiring agreement among independent proposals and averaging over them are different operations, and they reduce error at different rates (Appendix B)"; the rates themselves stay in Table B-1. "AlphaEvolve is still the only" → "is the only"; "the 2026 systems that keep archives" → "the other systems that keep archives".

## VIII. Convergent research families

- Opening kept; the pointer to III dropped and the vendor-convergence evidence **moved in** from VI-C, with one pointer back to VI ("the vendors' convergence on one artifact format and tool attachment (Section VI) is independent evidence of the same kind").
- SkillOpt paragraph kept verbatim.
- Families paragraph: one sentence per family (where it started, what it arrived at), every citation kept in bracketed groups attached to its own claim; names stay in Table VIII-1 (unchanged). "by October 2026 it is the largest family" → "it is the largest family"; "roughly two hundred papers … a dozen scored here" kept. The Ratchet no-gain result is no longer restated here (single home: Table X-1 and X prose); `@zhang2026ratchet` stays as the source of "hygiene is a precondition". The transfer sentence no longer repeats FederatedSkill's decision log and EvolveNet's merge gate and rollback (they are in Table IX-1).
- **Inconsistency 4 settled (VIII side):** "eleven 2026 systems" → "eleven systems", same four citations as VI.
- Conclusions: "Read against the loop and against the four properties of Section IX" → "Read against the loop" (no forward pointer). #1 "the 2026 harness papers" → "the harness-optimization papers". #3 points to Table X-1; "the 2026 retirement mechanisms" → "gated retirement". #4 in words with the pointer to IX ("neither meets the four that Section IX sets out").

## IX. The missing architecture

- Property list kept verbatim (labels (a)–(d) defined here, first use).
- **New Table IX-1** replaces the letter-coded inventory: FederatedSkill, EvolveNet, SkillForge, the governance-first registries, the MCP control planes × (a)–(d), each cell "full / partial / none / not documented / not reported" with a one-phrase reason. Sources for every cell: the old IX paragraph; for cells it was silent on, Appendix E (S4.2.2: FederatedSkill "no (d)"; SkillForge "(d) is undocumented in the public report") and Appendix G (S6.1: EvolveNet (b) "partial", MCP control planes "RBAC without versioned promotion"). The MCP control planes' (d) is marked "not reported" because nothing in the paper states it. All citations of the old paragraph are in the table's first column.
- **Inconsistency 3 settled:** SkillForge (b) is "partial: cross-team within one enterprise", per the plan and S4.2.2.
- One sentence of interpretation ("Read row by row …") and one on rollback; "Rollback, which was almost absent in the May corpus, now appears" → "Rollback appears"; ends "(Supplementary Material S4)".
- Five-part target paragraph kept.
- By-class paragraph kept as the single home; "the corner should be filled only with …" → "promotion should be automated only behind receiving-side evaluation"; the receiving-side inference moved in from VI-B ("the check that would catch a scaffold over-fitted to one deployment before it propagates to another"); Evo2Team's "four failed transfers out of twenty-two" → "some of Evo2Team's transfers still fail …" (the fraction is in VI-B, the exact count in Appendix G); the safety-critical sentence moved in from IV's deleted paragraph. Ends on the two "Naming …" sentences, joined.
- **Note on EvolveNet (b):** the old IX prose implied no (b) ("clients that are benchmark partitions rather than organizations"); Appendix G S6.1 rates EvolveNet's (b) "partial". The table follows Appendix G and states the reason in the cell. Flagging in case you want "none".

## X. The failure surface

- First paragraph tightened: "This section surveys the documented attacks and degradations; it proposes no new threat model" → "The entries are documented attacks and degradations, not a new threat model."
- Table X-1 unchanged except the patch-overfitting pointer.
- **Inconsistency 9 settled:** "(Appendix REF(app:formal))" → "(Supplementary Material S3)" (Appendix D, S3.3 "Overfitting in scaffold adaptation", holds the argument; Appendix A has only a table row).
- The two-row commentary kept, split into two paragraphs (bloat; evaluation fragility). "Two rows deserve a sentence beyond the table" dropped.
- "quantified by 2024 to 2026 work" → "quantified in the cited measurements"; Ding et al.'s verdict moved to II-C.

## XI. Open problems and conclusion

- Problems keep their headings; each states what is open and why, without tallies. #2: "Four systems now evaluate at the receiving side and one of them still misses nearly a fifth" → "even where a promoted edit is checked on arrival, some transfers still fail (Section VI)" (fraction in VI-B, count in Appendix G). #3: "Of thirteen weight-side rubric-reward methods, five co-evolve …, none of those five …; three systems report judge calibration" → the two findings without counts, pointing to IV (counts in Appendix G S6.5 and Appendix H S7.3). #5: "The governed cross-tenant corner" → "The governed cross-organization loop".
- Conclusion in two paragraphs. The prior-papers result in one sentence (plus one sentence on what follows from it); "not a patch on an inadequate model" → "not a workaround". Closing paragraph kept; two change-narration phrases reworded ("retirement and expiry have become first-class" → "are first-class operations"; "lineage has reached production memory" → "production memory carries lineage").

## Appendix A (wording only)

- "assumption (iv) of Section III" → "which is the credit-assignment condition of Section III". (A1)–(A5) unchanged.

## Appendix B (wording only)

- Multi-sample-agreement row, last cell: "Under-explored; SkillOpt-Lite's consensus attribute mining is the nearest instance" → "VaG (three heterogeneous critics must all pass); SkillOpt-Lite (consensus filter across rollouts)". Other cells of the row unchanged. No citations added to the table (the other rows carry none; VaG is cited in VII and VIII, SkillOpt-Lite in VIII).
- **Inconsistency 5** (plan assigns it to Phase B) is therefore already resolved in the body-side file; nothing else in Appendix B needed a pointer change.

## Inconsistencies: status

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | II-C/III-D stage sentence | settled | Appendix G S6.4 row 1 (Spotify, SkillChain) |
| 2 | Industry exemplars in VII | settled | refresh CSV, Letta row (loop1/loop2); master CSV, Sierra Agent OS 2.0 and Cognition Devin rows (key_evidence) |
| 3 | SkillForge (b) | settled: partial | plan; S4.2.2 |
| 4 | "eleven" citations VI vs VIII | settled: same four in both | Appendix G S6.4 pruning row |
| 9 | X overfitting pointer | settled: S3 | S3.3 |
| 10 | IV's two wrong pointers | settled by deleting IV's last paragraph; VI-B says "rare" | — |
| 5 | Appendix B agreement row | settled here (body-side file) | VII batching paragraph; VIII SkillOpt-Lite |
| — | V-B inclusion rule (and/or) | settled, please confirm | Appendix C inclusion criteria; S4.1.1 contrast rows |
| — | VII seven promoters' cells | settled | refresh CSV loop2 for the seven |

## Judgment calls and deviations from the plan (all small; each reversible)

1. **Roadmap sentence** carries seven REF pointers. The plan asks for one roadmap sentence, and the brief allows one pointer per paragraph. I kept the roadmap as the single exception.
2. **VI-A topic sentence** worded "is routine … has not been built" because the checker bans "has become routine".
3. **II-B ending** (see II-B).
4. **V-C** is two paragraphs (see V-C).
5. **Table VI-1 cells** reworded in two places to clear banned vocabulary (see VI-A).
6. **Abstract** no longer states the survey window (banned outside V-B).

## Could not do, or not fully

- **Length.** Prose is 9.4% shorter, not about 15%. The plan adds material the old text did not have (the result paragraph in I, the four definitions and five scope glosses in III, the convention sentence, the predictions confirmation in VII, the interpretation and rollback sentences around Table IX-1, the moved safety-critical sentence), roughly 350 words. Reaching 15% would mean cutting paragraphs the plan says to keep (Introduction ¶1–¶2, the SkillOpt paragraph, the two-row commentary in X, the closing paragraph of XI) or the worked examples (IV's four-scaffold opening, III-B's engineer example). Your page render will show whether the body lands in 16–18 pages; Table IX-1 adds a float.
- **Fig. 3 image text** (`figures/fig4_corpus_flow_ieee.*`) still reads "130 by May 2026, +126 in the Oct 2026 sweep". It is an image, outside my files; it may need regenerating if the banned list applies to figure text.
- **Phase B dependencies** created by this pass: Appendix C must receive the query families and the two-pass history from V-B (text above); Appendix G's S6.5 row labels "IV-1/IV-2/IV-3" refer to the deleted "Claim IV-n" names; S7.2 still says "sit in the contrast corpus or at the single-loop boundary (Section S4)" and S7.5 still says "the limitations in Section V (… two-pass corpus with an October-2026 cutoff …)", both already listed under the plan's Appendix H directive; S4's header still says "(May 2026 corpus)".

## Corrections (editor's Phase A review)

Editor confirmed: EvolveNet (b) stays "partial"; the either/or inclusion rule in V-B stands; Fig. 3 is regenerated by the editor; the checker now compares key sets. Four edits, nothing else changed:

1. **III-A, first sentence.** "We call this loop artifact-layer descent: the disciplined version of scaffold maintenance, run again and again over the life of a deployment." → "The disciplined version of scaffold maintenance is one loop, which we call artifact-layer descent, run again and again over the life of a deployment." (supplies the antecedent). Rest of the paragraph unchanged.
2. **V-B, first paragraph.** Added after the first sentence: "The corpus was assembled in two passes, the second adding 126 systems up to the cutoff (Supplementary Material S2)." This gives the Table VI-1 caption's "most recently added 126 systems" a referent. "up to the cutoff" instead of "through the October 2026 cutoff" because the preceding sentence already names the October 2026 cutoff. It is the paragraph's only pointer; the query families and the first-pass count stay out (Appendix C).
3. **XI, problem 5.** The fragment became a sentence: "The architecture of Section IX, properties (a) through (d), remains unbuilt; the receiving-side gate of problem 2 is the piece that would make cross-organization promotion safe in the two classes where it should be automatic."
4. **Abstract.** "scored on six substrates with released scores" → "scored on six substrates, with the scores released". Word count 250.

Second round (from the appendix review):

5. **V-B, totals paragraph.** One sentence added at its end: "Ten further systems that the text treats at mechanism level, SkillOpt, GEPA, Meta-Harness, CORAL, PACE, MOSS, RCL, FederatedSkill, SkillClaw, and ChronoMem, were classified from their papers after the first pass closed and are not rows of the released table, so the corpus counts above exclude them; SkillOpt, the one of them placed in the design matrix, is counted among the 14 that pass the composite audit." Two departures from the suggested wording. (i) It says "the corpus counts" and names SkillOpt as counted in the 14, because the editor notes that SkillOpt is one of the 14, so "the counts above exclude them" would contradict the 14. (ii) It drops "are placed in the matrix and the families", because Appendix E (S4.2.1 note) says GEPA, Meta-Harness, CORAL, PACE, MOSS, and RCL are not placed in the matrix; only SkillOpt is. The paragraph's pointer count is unchanged (one, the Fig. 3 reference). **V-C:** "every classification can be re-derived" → "every scored classification can be re-derived".
6. **SkillChain is not a production hybrid** (released CSV: Loop 1 "Auto->Human", Loop 2 "None"). (a) III-D: "as Spotify [@palumbo2026spotify], SkillChain [@hu2026skillchain], and SkillForge do" → "as Spotify [@palumbo2026spotify] and SkillForge do". (b) Table VI-2, production-hybrid row: SkillChain and its citation removed from the systems cell; last cell "Spotify and SkillChain add online A/B gating and reported judge agreement" → "Spotify adds online A/B gating". (c) VI-C production-hybrid paragraph: the SkillChain clause dropped ("…Devin's merged pull requests are its promotion step, and Spotify launches …"). (d) VI-A skills sentence gains ", SkillChain's judge-monotone edits pass a human reflection gate before they enter its skill bank, a two-stage local gate rather than a promotion loop [@hu2026skillchain],". `@hu2026skillchain` is now cited in IV (judge calibration) and VI-A. No other body sentence calls SkillChain a hybrid or gives it a Loop 2; VII's prediction-two sentence names no system.
7. **RLPR.** IV weight-side paragraph: "Fixed versus co-evolved is exactly the reflexive-gate question, and none of the co-evolving methods reports agreement with human judgment (Supplementary Material S6)." → "Fixed versus co-evolved is exactly the reflexive-gate question. Of the co-evolving methods, only RLPR, whose reward is a probability rather than a rubric, reports agreement with human labels; none that co-evolves a rubric or judge does (Supplementary Material S6)." XI problem 3: "No co-evolved rubric on the weight side reports agreement with human judgment" → "No method that co-evolves a rubric or judge reports agreement with human judgment". VII unchanged (scaffold systems only). Phase B note: Appendix G row IV-3 and Appendix H S7.3 still say "none of the co-evolving ones does"; they need the same scoping.

## Corrections 3 (cold read of the appendices and style pass)

The passages were re-read after the style editor's clause-level edits; each edit was made on the current text.

1. **VII, batching paragraph.** "a merge is accepted only when the held-out items it fixes outnumber those it breaks [@nie2026evolvenet]" → "a merge is accepted only when it fixes at least as many held-out items as it breaks [@nie2026evolvenet]" (evidence card: fixed ≥ broken).
2. **VII, occupancy paragraph, Letta.** Added after the Letta clause: "That push is unconditional, an algorithmic promotion with no evaluation threshold, so it sits in the Auto column of Loop 2; the composite audit admits it on lineage, not on a gate."
3. **VII, seven promoters.** Now: "Six of them would enter the matrix if any of versioning, lineage, or rollback counted as Loop-2 governance, landing in [Auto × Auto] except Spotify's production loop, which lands in [Auto × Human]. The seventh, Future AGI's prompt lifecycle, rests on a vendor blog alone (tier T5), which the tier rule does not count, and is not admitted under any rule. None opens a new cell (Supplementary Material S2)." Pointer kept; still one per paragraph.
4. **III-B scope paragraph and Fig. 2 caption.** '"Cross-tenant promotion" means reaching the TENANT or CORE level.' → "Promotion that reaches CORE crosses tenants, and we call it cross-tenant promotion; reaching TENANT applies an edit across one tenant's deployments." (The suggested appositive "the scope every tenant shares" was left out because the preceding gloss defines CORE in exactly those words.) Fig. 2 caption text only: "cross-tenant promotion means reaching TENANT or CORE" → "cross-tenant promotion means reaching CORE".
5. **V-B totals.** "14 research systems and 3 industry exemplars" → "14 research systems (13 of them rows of the released table, and SkillOpt) and 3 industry exemplars". The following SkillOpt sentence shortened to "SkillOpt is the only one of them in the design matrix." "13" is new in prose; it is 14 minus SkillOpt, as the editor specified.
6. **XI, problem 1.** "a general method is the bottleneck named by every harness-optimization paper" → "a general method is the bottleneck the harness-optimization family names".
7. **Small fixes.** IV, C2: "a channel an attacker controls" → "a channel an attacker can control". VI-B lead: "each sits in a particular feedback-signal class" → "…class, or in all of them". VI-A: "catalogs" → "catalogues".

Checks after this round: abstract 250 words (untouched); at most one pointer per paragraph (except the roadmap sentence, as before); the first lowercase use of "tenant" is still at its III-B definition.

## Corrections 4 (first-time reader of the body)

Each passage was re-read in its current form before editing.

1. **III-C, gate labels.** Each label now records who decides: "Each loop has a gate, and we name three kinds by who decides. A gate is **Auto** when a program makes the decision, whether by an evaluation score, a verifier, a reinforcement-learning threshold, a language-model judge [@zheng2023judge] with a quantified agreement rate, or, at the degenerate end, an unconditional rule that accepts every candidate. It is **Human** when a person decides. It is **None** when the loop is absent." This covers Letta's push, CORAL's heartbeat, and archive selection.
2. **VII, other-cells paragraph.** Added at its end: "The Loop 1 label in these cells, as in [None × Auto], records who supplies each candidate: a person who registers an artifact for a specific use (Human) or an engineer who authors a version at a desk for no particular failure (None); the distinction is one of convention, and the supplementary matrix records it (Supplementary Material S4)." It is the paragraph's only pointer. "as in [None × Auto]" was added so the reader sees the prompts-as-code cell the convention is contrasted with, which sits in the preceding paragraph.
3. **V-B.** "only systems that pass both enter the design space" → "only systems that pass both are counted as occupying the design space, and systems that fail it appear in the matrix as contrast entries, marked as such."
4. **Fig. 3 caption** (caption text only): "Every system is scored on the six substrates" → "Every system is scored on the substrates it adapts, with an integrated row for systems that adapt several, giving 269 substrate-level rows for 256 systems". The rest of the caption is unchanged.
5. **VI-A, memory paragraph.** "…and no system both gates writes and corrects from failures." → "… [@yu2026recuris; @wang2026memguard; @sun2026vermem]. Among the memory systems that gate writes or correct from failures, only Cuadros et al. does both, which is why it alone reaches the top mark." All citations kept; consistent with Table VI-1 (S3 Score-5: Cuadros et al.) and Appendix G S6.3 (Cuadros row, "holds").
6. **III-D, stage sentence.** → "Production deployments that reach Stage 3 on the local loop promote either behind a human gate, as Spotify [@palumbo2026spotify] and SkillForge do, or, in one case, by an automatic push that carries lineage but no evaluation, as Letta's Context Repositories do."
7. **VII, confirmation paragraph.** The opening now reads "bears out the first two predictions of Section IV", and the third item is: "The third is the scaffold-side finding that section already records, that three systems report judge calibration and none calibrates a judge under edit, and no system in the matrix changes it." The suggested wording named "Section IV" in words. I used "that section" instead, because a literal "Section IV" breaks the arXiv renumbering and a REF would be the paragraph's second pointer. **X:** "follows from those four properties: held-out, scoped, mode-weighted, re-read, and checked against attribution …" → "follows from those four facts: held-out and scoped, mode-weighted, re-read, and checked against attribution rather than only against score."
8. **Glosses at first use.** II-A: "a two-timescale system, one that learns slowly in the weights and fast outside them, needs …"; "some of the residual, the failures that remain after training, but in practice …". II-B: "the two papers that precede this one in the series". Abstract untouched (250 words).

Left for the editor: IV's predictions paragraph still says the three predictions follow "which Section VII tests". After item 7, VII tests the first two and records that nothing in the matrix changes the third. A one-word change ("which Section VII checks") would align them; it was outside this list, so I left it.
