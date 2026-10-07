# Revision log, Phase B, Writer C (Appendices F, G, H)

Writer C, 2026-10-07. Files edited in place: `submission/sections/S5_families.md` (Appendix F), `S6_audit.md` (Appendix G), `S7_extended_related_work.md` (Appendix H). Snapshot for comparison: `submission/sections_before/`. Nothing was built or run. The only checks were read-only grep/diff/wc/awk pipelines. `CLAIMS_AUDIT.md` is untouched.

## Mechanical checks

- **Citation keys.** The key set across the three files is unchanged. S5 and S7 have identical key multisets before and after. S6 had no keys before; it now carries 11 occurrences of keys already cited in S7.3, moved into the new rubric-reward table (gunjal2025rubrics, jia2025writingzero, shi2026references, jin2026rlaes, plesner2026cheapverifier, yu2025rlpr, xu2026rubricarm, ding2026evorubrics, zhu2026score, li2026rubricem, chen2026rubricsurvey). S7.3 keeps all of them. No key was added to the document or dropped from it.
- **Numbers.** Distinct digit strings, before against after. S5: identical. S7: identical, apart from the new pointer "S6.6". S6: three strings left, all by directive: "127" (now 126), and the line references "190" and "231" (now the claims they point to). Three strings arrived as copies of S7.3 values in the new table: 79.1%, 0.803, 0.805. Every other count kept its digits. "7" stays a digit in S6.7 ("The 7 second-pass systems …"), and "14", "3", "256", "130", "126", "204", and "52" all survive in S6.7 prose. Spelled-out numbers were checked by eye. One stale word count changed: see S5.7.
- **Banned vocabulary.** Zero hits in the three files for the checker's appendix list (sweep, refresh, looking for, we checked, rescored, IEEE version/text, Removed from the, `Say "`, Restate, `See NNN`, 127, PP, single-loop boundary, Appendix XII-D). Also zero hits for the brief's list ("in our survey", "current survey corpus", "has arrived", "now exists", "May corpus", "May 2026", "October-2026"). The only date left is "the October 2026 cutoff" in S7.5, which is an allowed scope statement.
- **Tables.** S5: 11 table lines before and after (Table S5.2), with two cells reworded (see S5.2). S6: all 46 rows of the four three-column tables kept, plus the 5 lines of the four-column predictions table. The new rubric-reward table adds 5 lines (header, separator, three rows). Every row has the right pipe count. The "Line" column stays removed. Headers "| Claim | Verdict | Evidence |" and "| Claim | Statement | Verdict | Evidence |" are unchanged, so the generator's WIDTHS entries still match. The new rubric table has its own header, with dash widths 14/10/36/26.
- **Heading scheme.** "# S5.", "# S6.", "# S7." plus "## S<n>.<m>" are kept. S6 now runs S6.1–S6.7. Nothing outside S6 pointed at an S6 subsection number; the body and the other appendices point only to "Supplementary Material S6".
- **Pointer forms.** Main text: "Section N", "Table N-k", "Appendix XIII". Supplementary: "Section S<n>.<m>". The four occurrences of "Appendix XII-D of the main text" in S5 became "the correspondence note of the formal appendix", the phrase `v4/assemble_arxiv.py` already maps. "Section II's table" became "Table II-1", because the stage table now sits in III-D.

## Appendix F (`S5_families.md`)

### Header and intro
- Two paragraphs became one. Cut: the subsection roadmap, which had five pointers as sentence subjects, and "the October 2026 additions … described in Section VIII … scored in Section S1".
- New scope sentence, per the directive: "The walkthroughs were written before the second pass; the members it adds to each family appear in Table VIII-1 and in the score table of Section S1." This replaces "This section carries the May–September 2026 walkthroughs".
- Words: 91 → 60.

### S5.1 The convergent landscape (light pass)
- "the cleanest current instance of artifact-layer descent in our survey" → "the clearest instance of artifact-layer descent we found". The wording follows the audit's sharpened verdict and the body's "clearest single instance".
- "in 2025–2026" kept as a date range. "The convergence is striking because" → "They converge from different starting points" (dry register).
- Cut: "The landscape table of Section VIII indexes the families … the subsections below walk each family in detail", a pointer used as a sentence subject.
- RBAC is spelled out at its first use in F.
- Words: 240 → 209.

### S5.2 SkillOpt: full correspondence (light pass)
- Lead sentence: "extends the Section VIII compact correspondence" → "maps each component of SkillOpt to its quantity in Section III …". Section VIII no longer has a correspondence table.
- Two table cells changed, all rows kept:
  - The $\eta_t$ row: "the Section III *learning rate* in textual form" → "the step size of Section III in textual form". Section III calls it a step size.
  - The slow/meta row: "the Section III 'step-level edits cannot overwrite the protected slow-update field' decomposition" → "step-level edits cannot overwrite the protected slow-update field". The quoted phrase is not in Section III, so the pointer was wrong.
- After the table: "the cleanest published instance we are aware of" → "the clearest instance we found".

### S5.3 What SkillOpt does that prior textual-optimization systems do not (tightened)
- **Words: 731 → 495 (−32%).**
- Cut: the framing sentence restating the paper's thesis ("the scaffold/evolution layer needs a disciplined gradient-like update mechanism"), each bullet's "In Section III terms:" preamble, and the labels (i)–(iv) on the four controls. Those labels collided with the old assumption labels that Phase A removed.
- Merged into the TextGrad bullet: "This matches our Section S4.1 classification … SkillOpt closes precisely that gap" became "which is why Section S4.1 places it outside the core corpus".
- Kept, every one: the six baselines and what each lacks at mechanism level; +5.9 to +34.0, seven scales, GPT-5.5; +5.0 to +19.0; +14.0 and +3.2 on the five-benchmark average; 145–516 tokens; 379–1,995 tokens; ABSTRAL and EvoTest as out of scope; the four controls; SkillOpt-Lite's three kept principles, four dropped controls, and LiveMath +8.8 and +25.4.
- **Audit verdict applied:** "SkillOpt is the first published system in our survey that instantiates all four simultaneously" → "SkillOpt is the first system we found that has all four". The SkillOpt-Lite paragraph that follows supplies the second half of the sharpened verdict (two of the four are stabilizers).

### S5.4 GEPA and Tiwari et al., and S5.5 RCL (light pass)
- "**@tiwari2026fastandslow** supply" → "**Tiwari et al.** [@tiwari2026fastandslow] supply", the bracketed form the brief asks for.
- The repeated "from the optimization side" was removed.
- S5.5: wording unchanged apart from punctuation (dashes turned into commas).

### S5.6 The harness-optimization cluster (tightened)
- **Words: 897 → 586 (−35%).**
- Cut, as restatements of the body or of the paragraph's own point:
  - Meta-Harness: "is Section I's scaffold-versus-weights decomposition restated". The decomposition is now stated inside the sentence, without the wrong Section I pointer.
  - AHE: "The implicit claim is that …", condensed to one sentence.
  - MOSS: "the gap is not merely inconvenient but structurally incomplete", reduced to the plain consequence.
  - CANTANTE: the duplicated Appendix XII-D sentence. The two pointers became one ("the correspondence note of the formal appendix").
  - Ong et al.: "provides independent empirical evidence for a failure mode this paper flags in Section X" and "the credit-assignment problem is not merely theoretical".
- Kept at mechanism level, every one:
  - Meta-Harness: filesystem proposer, $H_t$ / $Q_t$, Loop 1 over S5.
  - AHE: the three obstacles mapped to operations 2, 1, and 2; the three observability pillars.
  - MOSS: the code-resident failure class and the S2+S5 evolution.
  - CANTANTE: contrastive decomposition into per-agent signals.
  - Ong et al.: the Stage 2 / Stage 3 line, now pointing to Table II-1.
  - HARNESSEVO: four slots, leave-one-in +0.119, the 64-rollout budget, 0.642 to 0.761, ALFWorld, 7B, WebShop absent.
- Short quotations from the cited papers are kept where they carry the diagnosis.

### S5.7 Multi-objective and lifecycle constraints (tightened)
- **Words: 629 → 431 (−31%).**
- Opening "Two papers expose constraints … both relevant to the Section IX missing-architecture discussion" → "Descent on a single loss misses two kinds of constraint: the platform limits … and the hygiene of the artifact pool …". The old count "Two papers" introduced three walkthroughs (MOCHA, Ratchet, SkillsVote), so it was stale. The new "two" counts kinds of constraint, not papers. No claim changed.
- MOCHA: "MOCHA's empirical contribution is to show …" was merged into the preceding sentences.
- Ratchet: the second paragraph lost its restated lead-in. The mechanism mapping (retirement, active cap, canonicalization to operations 1 and 2) and the Stage 1 / 2 / 3 contrast are kept.
- SkillsVote: kept whole, with light compression.
- +0.0 pp and +16.2 pp kept. The Ratchet no-gain result keeps its body home in Table X-1; F keeps it as mechanism-level detail.

### S5.8 Cross-task transfer and evidence radius (tightened)
- **Words: 854 → 572 (−33%).**
- ICT: the paper title in bold became "In-context Training [ICT; …]"; the content is kept.
- Combee: the two quotations were compressed to one sentence of mechanism. "but it is a step toward it" was cut.
- CORAL: "its open-ended discovery framing makes the evidence-radius question concrete" was cut.
- PACE: one sentence of restatement was cut.
- FederatedSkill:
  - The motivation sentence was compressed.
  - Cut, because Table IX-1 now carries them: "(clients are backbone-plus-harness profiles, not organizations)", "reports neither RBAC nor rollback", and "Section IX's properties (b), (c), and (d) are each partially or wholly open".
  - Kept: the semantic skill diff; the capability matrix (covered, absorbing, broken, gap); the decision log; 20 task families, +44.4% and −37.5%; both "first" claims (verdict: holds); acceptance on the source client's reward, not at the receiving client.
- **Audit verdicts applied:**
  - CORAL: "it provides the only fully asynchronous multi-agent Loop-2 promotion mechanism in the current survey corpus" → "CORAL is the only fully asynchronous multi-agent Loop-2 promotion mechanism in the first pass; in the full corpus, Evo2Team and ShareMem add cross-team and cross-user promotion without versioning (Section S6.3)".
  - SkillClaw and FederatedSkill: "are the two systems in the corpus whose Loop 2 crosses users" → "are the two systems of these walkthroughs whose Loop 2 crosses users rather than tasks or agents; in the full corpus, EvolveNet, ShareMem, XRepoSkill, and RASO also promote across users, clients, or repositories, each inside one operator (Section VI)". The four names are the ones in VI-B and in G's "Cross-customer skill promotion" row.

### S5.9 Synthesis (revised per the audit)
- The lead sentence "The four claims stated in Section VIII are supported as follows" now reads as findings.
- Conclusion 2: "@ong2026harnesseval" (an in-text citation) → "the harness-optimizer evaluation of Ong et al. [@ong2026harnesseval]". "Appendix XII-D of the main text" → "the correspondence note of the formal appendix".
- Conclusion 4: "narrowed on property (b) by FederatedSkill and closed on none" → "narrowed on (b) and (d) by different systems and closed on none". A clause on EvolveNet was added ("adds a held-out merge gate and round rollback without lineage or RBAC"). This follows G, S6.1 rows 3 and 4. EvolveNet already sits in Table VIII-1.
- Words: 314 → 332.

### S5.10 and S5.11 (light pass)
- "SkillOpt is the strongest current Loop-1 proof" → "the strongest Loop-1 proof".
- "they tell us that" was cut.
- S5.11 is unchanged. Its "first published cost-per-point figure" has the verdict holds.

## Appendix G (`S6_audit.md`)

### Title and intro
- Retitled "# S6. Audit of the first-pass draft's absolute claims against the full corpus".
- The intro is now three sentences:
  1. What the audit is: absolute claims of the first-pass draft (130 systems) set against the full corpus (256).
  2. The four verdicts, defined for the reader: holds, sharpened, revised, dropped.
  3. How to read the Evidence column. The arXiv-identifier convention is stated plainly.
- The old line "arXiv ids are in the reference list" was false: 2608.29381 and 2608.15939 are not in references.bib, and dai2026hearsay and lam2026ssgm are in the bib but uncited. It now reads "parenthetical numbers such as 2608.04968 are arXiv identifiers".
- **Moved to S6.7:** the "Corpus after the sweep" paragraph and the "Corrections to the May data" paragraph, which hold the numbers 256, 130, 126, 204, 52, 5, 14, 3, 7, T5, 2605.04264, 2603.11768, 2, 4, 2.68, and 2.58. The sweep description ("three parallel sweeps: skills; …") and "(not carried into the IEEE version)" were cut.

### S6.1 (retitled "The four properties of Section IX"; "the corner" is a removed label)
- Row 1: "Three sweeps, 126 systems:" → "Across the 126 second-pass systems:". RBAC and ACM are spelled out at first use.
- Row 2: "is now the nearest … cite both" became a statement of EvolveNet's mechanism and the sharpened claim: "neither it nor FederatedSkill meets the FedAvg limit".
- Row 3: the claim label "(iv) …" → "Fourth conclusion on the research families". "Say …" became the statement "The gap is narrowed on (b) and (d) by different systems and closed on none (Table IX-1)".
- Row 4: "New sentence: …" became the statement itself, which matches IX's rollback sentence.

### S6.2 Matrix cells
- Row 1:
  - "now occupy" → "occupy".
  - "Restate as: three cells hold every system that passes the composite audit; …" → "Two cells hold every system that passes the composite audit, a third holds the governance-first platforms, and the human-authored cells are occupied only by registries and curation workflows with no session-signal loop (Section VII)".
  - **Settled a small inconsistency.** The audit's suggested wording ("three cells hold every system that passes") contradicts the body's Section VII figure caption and occupancy paragraph ("Two cells hold every system that passes the composite audit; a third holds the governance-first platforms"), and S4 asterisks the governance-first platforms as failing the composite audit. G now follows the body.
- Row 2: "was found" → "No system in the full corpus pairs …".
- Row 3: "see above" → "(first row of this table)". A restated claim matching VII was added.
- Row 4: "Restate: …" became a statement.
- Row 5: "fires at n = 1" is kept as the quoted first-pass claim, with a gloss: "(accepts an edit on a single evaluation)". "now common … Say 'common since mid-2026' and cite SAGE-gate and VaG" → "is common, and has been since mid-2026: … Evidence is batched before acceptance, with SAGE-gate and VaG as instances (Section VII)". The plan states this trend as a clause.
- Row 6: "Keep the p^k-vs-1/k distinction, drop 'no surveyed system'" → "agreement-based acceptance exists. The distinction between agreement and averaging stands: under agreement the false-accept rate decays as $p^k$, under averaging the variance decays as $1/k$ (Appendix XIII)". The wording is Table B-1's.
- Row 7: "Say 'AlphaEvolve remains the only …'" → "AlphaEvolve is the only system that combines the two".

### S6.3 "Only" and "first"
- CORAL row: "Say 'CORAL was the only one in the May corpus; …'" → "CORAL is the only such mechanism in the first pass; in the full corpus Evo2Team and ShareMem add … (Section S5.8)".
- Strassen row: "Third-party; attribute to the AlphaEvolve report in the same sentence." → a statement of the attribution. The body no longer mentions Strassen, so the cell does not say where the article states it.
- CASCADE row (dropped): "Not re-checked across 127 new systems … Removed from the IEEE text." → "Not established for the 126 second-pass systems, and ablation gains measured on different benchmarks are not comparable. The article does not make the claim." **127 → 126.**
- ChronoMem row: "Say 'among the first' and cite the counter-evidence" → "ChronoMem and rollback repair are among the first instances, and the checkpoint-rollback studies are the counter-evidence".
- Cuadros row: "Memory governance additions" → "The memory-governance systems of the second pass".
- SkillOpt row: "Say 'the first system we found …'" became the statement, with a pointer to S5.3, where F now carries it.
- FederatedSkill row: "Aug 2026" → "August 2026".
- Cost-per-point row: "No earlier figure found." → "The full corpus contains no earlier figure."

### S6.4 Absences
- Stage row: "say …" became the statement "(Section III)". This is the wording of III-D.
- S1 row: "S1 n=15, max 4; adoption studies cut the other way" → "On S1, n=15 and the maximum score is 4. Adoption studies point the same way: …". Numbers 15, 4, and 20% kept.
- Memory row: "Say 'versioned lineage has arrived …'" → "Production memory is versioned, but correction is not enforced (Section VI)", the wording of VI-B.
- S5 topology row: "Gated topology evolution now exists … Say …" → statements. "in either corpus" → "in either pass". Pointer to S6.7 for the correction.
- "no system matures all six" row: "No October addition" → "None of the 126 second-pass systems".
- **"See 190"** (memory-versioning row) → "The evidence is the same as for the claim that production memory lacks versioned lineage (fourth row of this table): …", then the restated claim "Memory versioning is common, not confined to Cuadros et al. and ChronoMem".
- Receiving-side row: "now exists" → "exists". Restated: "Receiving-side evaluation at promotion is rare, not absent (Section VI)". 4 of 22 kept.
- Research full-auto row: "No October" → "No second-pass".
- Governance-first row: "all have Loop 1 = None" (a removed label) → "all lack an inner loop".
- AGENTS.md row: "Newer counts: … Replace the single count with these studies and the cost finding (Gloaguen)" → "Adoption is measured directly rather than by one repository count: …". 2,853, 128,018, 22–29%, and 36,710 kept.
- Pruning row: "Say 'pruning and expiry became first-class in 2026; …'" → "Pruning and expiry are first-class operations; what remains rare is …". The eleven names, n ≥ 100, −0.10, and 50 kept.
- **"See 231"** (multi-sample-agreement row) → "The evidence is the same as for the two acceptance-rule claims of Section S6.2, single-evaluation acceptance and k-of-n agreement: SAGE-gate, VaG, and SkillSpec. Agreement-based acceptance is instantiated, not under-explored (Appendix XIII)." In CLAIMS_AUDIT.md, line 231 carries three claims; the two that bear on agreement are named.
- The remaining rows are unchanged in substance, with small grammatical completions.

### S6.5 (retitled "The three predictions of Section IV"; "rescored" removed)
- A one-sentence lead was added.
- Claim labels "IV-1 / IV-2 / IV-3" → "First / Second / Third". The Statement cells now hold the three predictions as Section IV states them, including "should".
- Third row: the statement was "Rubric-as-reward builds C3 gates on the weight side; scaffold-side judge calibration under the reflexive condition is rare". It is now the body's third prediction, "No scaffold system should yet calibrate a judged gate under the reflexive condition".
- The weight-side tally moved out of this row into S6.6 (14, 8, 5, and 5, plus the five co-evolving names). The row keeps the scaffold-side evidence (>90%, κ 0.72–0.91, 82→96%) and one sentence pointing to S6.6. "now report calibration" → "report calibration". "May" / "October" → "First pass" / "Second pass".

### S6.6 The rubric-reward comparison (new subsection, built from existing material only)
- Prose: the tally, verbatim in substance: fourteen papers; thirteen methods and one survey; eight fixed and five co-evolved; five report human agreement, none of them co-evolving.
- Table: Held fixed (8 methods), Co-evolved (5 methods), Survey (1). Every cited member and its one-phrase mechanism comes from S7.3 and from body IV. Human-agreement values (79.1%, QWK 0.803 against 0.805) were copied from S7.3, and the cheap-verifier caveat from S7.3.
- The three fixed-gate methods that the document does not cite appear as "three further methods" (see open question 2).
- Closing sentence: "None of the methods that let the gate move reports agreement with people: the reflexive-gate problem of Section IV, seen from the weight side."

### S6.7 Recount of the full corpus (was S6.6)
- Receives the two moved intro paragraphs, rewritten as findings:
  - "Corpus after the sweep" → "The full corpus holds …".
  - "relaxation (a)" → "the relaxation that counts any of versioning, lineage, or rollback as Loop-2 governance", which is V-C's wording, without a letter.
  - "applied before the recount" → "Two first-pass rows are corrected before the recount".
- One sentence was added to say what the block shows and how to read its last line.
- Code block: unchanged except its last, hand-written line: "May corpus alone (after corrections)" → "First pass alone (after corrections)". `scripts/recount.py` does not print that line (checked by grep); the numbers 130 / 99 / 31 and 2.58 are unchanged. Revert if you want the block byte-identical to `CLAIMS_AUDIT.md`.
- Words: G as a whole went from 2,354 to 3,099 (prose and tables, headings excluded). The growth comes from the new S6.6 subsection (+319) and from the restated claim that every sharpened or revised row now carries. G is the one appendix the plan grows.

## Appendix H (`S7_extended_related_work.md`)

1. **S7.2.** "which is why they sit in the contrast corpus or at the single-loop boundary (Section S4)" → "That is why OPRO and TextGrad score below the core-corpus threshold and DSPy, which persists only optimizer state, closes no second loop; Section S4.1 lists all three."
   - Evidence: `p3_master_scores.csv` scores OPRO 2, TextGrad 2, and "DSPy compile" 3 (all on S6). S4.1.1 lists OPRO and TextGrad in the contrast corpus. S4.1.2 lists DSPy among core systems failing the composite criterion, and the matrix places it in [Auto × None].
2. **S7.3.** "Of the fourteen papers in this line that were checked, eight hold … five co-evolve …; five report … none of the co-evolving ones does; one calibrates …; and a survey …" → "The groups part on human calibration: no method that moves the gate with the policy reports agreement with human judgment (Section S6.6 gives the tally). One study calibrates its verifier against language-model golden judges rather than people [@plesner2026cheapverifier], and a survey of rubric evaluation names the dynamic regime as the trend [@chen2026rubricsurvey]."
   - The counts fourteen, eight, five, and five left S7 prose and live in S6.6, in prose and table. The brief's directive (2) asks for this. Both citations stay.
3. **S7.5.** "and the limitations in Section V (single-rater scoring, two-pass corpus with an October-2026 cutoff, no new experiments) bound them" → "Three limits bound them: scoring is single-rater over public evidence of uneven strength (Section V), the corpus closes at the October 2026 cutoff, and the evidence is the published behavior of the 256 systems rather than new experiments (Section I)."
   - The no-experiments statement is the last paragraph of Section I, and the single-rater and tier caveats are V-C. "two-pass" was dropped as process; the cutoff stays as a scope statement.
- No other changes to H.

## Inconsistencies settled

| # | Item | Status | Evidence |
|---|---|---|---|
| 7 | Appendix F claims revised by the audit | Settled. SkillOpt is "the first system we found" (S5.3; also S5.1 and S5.2 "clearest instance we found"). CORAL is "the only … in the first pass", with Evo2Team and ShareMem named. SkillClaw and FederatedSkill are scoped to "these walkthroughs", with EvolveNet, ShareMem, XRepoSkill, and RASO named. "written before the second pass" is the scope statement. The S5.9 conclusion-4 gap now reads "narrowed on (b) and (d) by different systems". | CLAIMS_AUDIT.md rows for SkillOpt "first", CORAL "only", FederatedSkill "first" (holds, kept), the "(iv) … narrowed on one property" row, and "Cross-customer skill promotion" (the four names); body VI-B; Table IX-1 |
| 8 | Appendix G: "127", "See 190/231" | Settled. 127 → 126 (the second-pass count in V-B, Table VI-1 caption, S2). "See 190" → the production-memory lineage claim (fourth row of S6.4). "See 231" → the two acceptance-rule claims of S6.2. In CLAIMS_AUDIT.md, the Line-column values 190 and 231 (line numbers of the first-pass draft) identify the rows "correctable, versioned memory is rare …" and "Nearly every auto-gated system fires at n = 1" / "no surveyed system has formalized agreement as a k-of-n acceptance rule" |
| — | G's restated "three cells hold every composite-passing system" against the body's "two cells … a third holds governance-first" | Settled toward the body | Section VII figure caption and occupancy paragraph; S4 asterisks |
| — | S5.2 table cell quoting Section III for text that Section III does not contain | Settled (the misattribution was removed) | Section III; Appendix A setup |

## Flagged, not changed

1. **RLPR and "none of the co-evolving ones reports human agreement".** The authors' own rubric cards (`m1_memory_surveys_rubrics.md`, the file `related_work_cards.md` cites; found at `C:\Users\mikea\AppData\Local\Temp\claude\C--Users-mikea-SCRIPTS-telegrapher-ai\065ecc48-9014-4dec-9e70-17f3c11d4c6b\scratchpad\`, PART 3, table row at line 428, and summary lines 441 and 584) record that RLPR, which they count as co-evolving "by construction", reports reward quality against human annotations (ROC-AUC ≈0.95 math / ≈0.82 general).
   - Line 584 lists RLPR among "the 5 that report any human-agreement number" and in the same sentence says "no co-evolving method does". Line 441 lists six candidates (RaR plot-only, RLPR, References, Query-specific, RLAES, Open Rubric) for "only 5".
   - So either the five include RLPR, and "none of the co-evolving ones" is false, or RaR's plot-read accuracy is the fifth, and RLPR's AUC is judged not to be agreement with human judgment.
   - The claim appears in body IV ("none of the co-evolving methods reports agreement"), XI problem 3 ("No co-evolved rubric on the weight side reports agreement with human judgment"), S6.5, S6.6, and S7.3. The tally is kept verbatim as the brief requires. The authors should decide, and if RLPR's AUC counts, reword in every place.
2. **Three of the eight fixed-gate rubric methods are not cited anywhere in the document**: `bhattarai2026rubricgrounded`, `jia2026openrubric`, and `lv2026queryrubrics`. They are in references.bib but uncited, so the IEEE build drops them.
   - The tally (8 fixed; 5 reporting human agreement, of which Open Rubric and the query-specific rubrics are two) cannot be checked by a reader without them.
   - S6.6 says "three further methods" because adding keys is outside the brief. Citing the three in the S6.6 table would close the gap; the cells are ready to take them.
3. **SkillChain's cell.** G (S6.2, row 1) places SkillChain in [Auto+Human × None], which matches the second-pass CSV (loop1 "Auto->Human", loop2 "None"). The body's VI-C Table VI-2 lists SkillChain in the production-hybrid cluster (Auto / Human), and III-D cites it as reaching Stage 3 "behind a human promotion gate". This is a body-against-data question for Phase A; G keeps the CSV's reading as evidence.
4. **Column width of the predictions table.** The generator's WIDTHS entry (5, 23, 10, 42) was sized for "IV-1" labels. "First", "Second", and "Third" should fit, but check the render; widening the first column to 7 may help.
5. **Revised claims that no longer appear in the article.** The Strassen, ChronoMem "first", and CASCADE claims appear nowhere in the current body. G states what the corpus shows and does not claim the article repeats them. Only the CASCADE row says "The article does not make the claim", because that row's verdict is "dropped".
6. **Generator front matter** (`scripts/generate_supplementary.py`, not my file) still describes S6 as "the audit of every absolute claim of the earlier preprint against the October-2026 literature". Consider aligning it with the new S6 title.

## Corrections (editor's Phase B review)

The editor resolved flagged items 1–3 and 6; item 4 is the editor's render check. Five corrections, applied in place; nothing else changed.

1. **Rubric-reward tally scoped to the card (G S6.5 and S6.6, H S7.3).** Every number is kept (fourteen; thirteen and one; eight and five; five).
   - S6.6 prose now reads: "Five report a human-agreement figure; among the co-evolving five only RLPR does, for its probability reward against human labels, and no method that co-evolves a rubric or judge reports one."
   - S6.6 table, co-evolved row, agreement cell: "None reported" → "RLPR only, for its probability reward against human labels; no method that co-evolves a rubric or judge reports a figure".
   - S6.6 closing: "No method that co-evolves a rubric or judge reports agreement with people; the one co-evolving method that does, RLPR, scores by probability rather than by a rubric."
   - S6.5, third prediction, Evidence cell: "the rubric-reward methods that co-evolve the judge report no agreement" → "no method that co-evolves a rubric or judge reports agreement with people".
   - S7.3: "among the methods that move the gate with the policy, only RLPR, whose reward is a probability rather than a rubric, reports agreement with human labels, and no method that co-evolves a rubric or judge does (Section S6.6 gives the tally)."
   - RLPR's ROC-AUC values were not added; they appear nowhere in the document.
2. **Three fixed-gate methods cited (G S6.6).** "three further methods" → "Rubric-Grounded RL, the Open Rubric System, and query-specific rubrics learned from human preferences [@bhattarai2026rubricgrounded; @jia2026openrubric; @lv2026queryrubrics]".
   - The names come from the three titles in references.bib.
   - Document-wide key set: these three keys are the only additions (checked by diff over all section files and the abstract against the snapshot).
3. **SkillChain (G S6.4, Stage row).** The row now names Spotify and SkillForge: "SkillForge passes each skill diff through a judge that agrees with engineers more than nine times in ten, and support engineers decide whether it ships", the wording of body IV and VI-C. SkillChain left that row.
   - SkillChain's other mentions stand. S6.2 row 1 places it in [Auto+Human × None], a two-stage local gate with no promotion loop. S6.5 row 3 cites its κ 0.72–0.91 judge calibration.
   - Neither F nor H mentions SkillChain.
4. **Relaxation naming (G S6.7).** "the relaxation that counts any of versioning, lineage, or rollback as Loop-2 governance" → "the governance relaxation of Section S2, which counts any of versioning, lineage, or rollback as Loop-2 governance". G never named the optimizer-state relaxation, so no other change was needed.
5. **Recount block.** "First pass alone" kept, as instructed.

Post-correction checks: S6 tables intact (46 three-column lines, 10 four-column lines); S6 digit strings unchanged from the first submission (only 127, 190, and 231 gone; 79.1%, 0.803, and 0.805 added); no banned-vocabulary hits.

## Corrections 2 (first-time reader of the appendices)

Nine fixes, applied in place; each uses evidence already in the document.

1. **CORAL is not a first-pass system.** S2 lists it among the ten systems classified from their papers after the first pass closed.
   - S5.8 and S6.3: "the only … in the first pass" → "the only … among the systems classified before the second pass".
   - S6.5, first prediction, Evidence cell: the label "First pass:" → "Before the second pass:", because the list includes SkillOpt and CORAL. All names kept.
2. **S5 intro scope sentence.** The walkthroughs mention SkillOpt-Lite, HARNESSEVO, and EvolveNet, so the sentence now reads: "The walkthroughs were written before the second pass and updated where the audit of Section S6 revised a claim; the members the second pass adds to each family appear in Table VIII-1 and in Section S1."
3. **EvolveNet's merge rule (S7.4).** "merges only when the held-out items a merge fixes outnumber those it breaks" → "merges only when a merge fixes at least as many held-out items as it breaks". This matches the evidence card's "≥" and G (S6.1, S6.2).
4. **S6.4, "Held-out evals at Loop-2 promotion" row.** "EvolveNet explicitly has none" → "EvolveNet gates the merge on a server-side held-out slice but runs no check at the receiving client".
5. **S6.1, first row.** "(b) is unclaimed by any evidenced system (…)" → "no system demonstrates promotion across organizations, and EvolveNet and RASO have a partial (b) inside one operator (EvolveNet's clients are benchmark partitions, 'organizations' only in motivation; RASO draws on a public corpus as its source); MemClaw is single-tenant in its evaluation, and Buildrix is an open community hub with no gate". The rest of the cell is unchanged. The row now agrees with its own fourth row and with Table IX-1.
6. **S6.3, SkillOpt row.** "matches SkillOpt" → "matches or beats SkillOpt", as in S5.3 and the body.
7. **S6.3, Strassen row.** The claim is now stated in words: "AlphaEvolve's reported improvement on Strassen's algorithm for 4×4 matrix multiplication", "taken from the AlphaEvolve report and … not independently measured". No numbers were added beyond the matrix size the coordinator specified.
8. **S6.6, RLPR sentences restructured into three.** "Five report a human-agreement figure. Four of them hold the gate fixed, and the fifth, RLPR, co-evolves a probability reward rather than a rubric, checked against human labels. No method that co-evolves a rubric or judge reports one."
   - The closing paragraph has the same shape: "The only co-evolving method with a human-agreement figure, RLPR, co-evolves a probability reward, not a rubric. No method that co-evolves a rubric or judge reports agreement with people. That is the reflexive-gate problem …"
   - "Four of them hold the gate fixed" follows from five reporters minus RLPR. It is the coordinator's wording.
9. **S6.7, Future AGI.** The seven systems are now listed first. Then: "The first six enter only under the governance relaxation of Section S2 …; Future AGI's evidence is T5 only, so it enters not at all."
   - Possible knock-on in the body: Section VII says that under the relaxation "all would land in [Auto × Auto] except Spotify's production loop", which counts Future AGI among the systems that enter. If Future AGI enters not at all, VII's "Seven systems … would enter" may need the same qualification.

Checks: S6 tables intact (46 three-column lines, 10 four-column lines). The key set across the three files differs from the snapshot only by the three keys approved in item 2 of "Corrections". No occurrence remains of "outnumber", "explicitly has none", "unclaimed", or "in the first pass".
