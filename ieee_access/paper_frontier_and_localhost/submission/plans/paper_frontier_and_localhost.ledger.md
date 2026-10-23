# Diagnostic ledger, reverse outline, and gap table: Frontier and Localhost

Clarity-and-grace, Full size, Revise mode, 2026-10-22. S4 diagnostic ledger and R-2 reverse outline written by five Opus readers (one per section group) on the text at commit 5038169; R-4 gap table assembled from their re-draft verdicts against the plan (`paper_frontier_and_localhost.plan.md`). Paragraph ids are `<file>:<n>` in the order of the pre-revision text.

## R-4 gap table

| Group | Re-draft (role-level fail or >=3 passage fails) | Document/section-level change (plan decision) |
|---|---|---|
| A | I_II:1 (prelude, inside the gate per D1), 6, 7, 14, 21, 29 | Intro: "but" turn and R1 cost at ¶3; one closing point sentence naming the four themes at the end of ¶7; roadmap ¶8 not ending on a caveat; abstract ends on the finding |
| B | III:10, III:12, IV:2, IV:5, IV:6, IV:9, IV:14 | IV opens on its finding; "proposing is not accepting" made once (D9); "credit assignment" kept as the locked term |
| C | V:5, 6, 13, 15, 18; VI:3, 6, 10, 12, 15, 16, 17 | V opening links from IV and forecasts the predictions; VI opening forecasts the grid finding (D10); caveats to one home (D9) |
| D | VII:2, 4, 7, 9, 12, 13; IX:7, 14, 15 | VII opening links from VI and states its point; IX-A/IX-B placement is a proposal (D11) |
| E | X:2, 3, 4, 5, 8; appA:4, appA:5; appB:2 | X opening states its point; coda strength is AUTHOR FLAG X-1 (D12); appendix paragraphs split by job, math verbatim |

## Group A (abstract, I, II): S4 diagnostic ledger

# S4 diagnostic ledger, group A: abstract, Section I (Introduction), Section II (the loop)

Sources diagnosed (read-only): `cg_pre/abstract.md` (1 paragraph, 237 words); `cg_pre/I_II_intro_loop.md` (29 paragraphs incl. 8 list items; Intro 647 words, Section II about 937 words).
Numbering: `abstract:1`; `I_II:1`–`I_II:8` = Introduction; `I_II:9`–`I_II:29` = Section II. List items count as paragraphs: `I_II:16`–`I_II:20` are the five conditions; `I_II:25`–`I_II:27` are Auto / Human / None. `I_II:22` is the single Markdown paragraph that wraps both display equations (lines 58–62); the equations themselves are n/a. Sentences are numbered S1, S2, … within each paragraph.
House-style checks run throughout: no em-dashes found in either file (0); American spelling consistent ("behavior", "revise"); no "catalog"/"analog" occurrences.

## Document-level row (Introduction, I_II:1–I_II:8)

| unit | 1.1 six-step intro test | 1.2 prelude gate (I_II:1) | 1.3 proportion |
|---|---|---|---|
| Introduction | FLAG (partial). Classify: survey article. Line drawn after I_II:4 S1 ("These situations raise two questions") / I_II:5 S1. Division: [prelude] I_II:1 S1–S4 · context I_II:1 S5 + I_II:2 · problem I_II:3 (+ questions I_II:4 S1–S3) · method/solution exposition I_II:4 S4–S6 · point I_II:5 S1 ("The systems surveyed have developed these loops unevenly") extended by I_II:6 and I_II:7 · roadmap and scope I_II:8. Check for *but*: FLAG, the turn from context to problem is unmarked; I_II:3 S1 opens "The ease of making a change also makes it easy…" with no *but/however*, so a reader can miss the turn. Condition vs cost: condition = "changes whose value is unknown" (I_II:3 S1); cost = conflicting rules, stale retrieval, harm on transfer (I_II:3 S2–S4): present and in the reader's terms, pass. Underline the point: FLAG, the point is spread over three paragraphs (local-loop unevenness in I_II:5, missing governed cross-organization promotion in I_II:6 S6, feedback class as explanation in I_II:7 S1) with no single sentence that states all three; I_II:5 S1 states only "unevenly". The point is not last (roadmap I_II:8 follows), which is allowed, but I_II:8 ends on a scope caveat ("Its scores and classifications are released for inspection"). | FLAG. Genre: research survey, where preludes are rare (default none); the vignette I_II:1 S1–S4 ("A coding agent repeatedly uses the wrong naming convention in a repository…") is a present-tense anecdote before the shared context. Length: one paragraph, pass. Function: maps to the condition (change outside the weights) and is reused as the running example in I_II:9 and I_II:13, pass. Contents: FLAG, S5 carries an unsupported thesis-level claim inside the prelude ("Much of the experience that makes an AI system useful in one setting now accumulates in these persistent artifacts outside the model's weights"). Hand-off: I_II:2 ("We call this layer the scaffold") follows directly, pass. Hook: the problem arrives two paragraphs later (I_II:3), close call; the prelude is short (80 words). Net: fails on genre and contents; defensible as a running example if recast as illustration inside the shared context. | pass. Intro 647 words vs a body of about 21 IEEE pages: substantially shorter. Prelude (80 words) < context I_II:2 (87) + problem I_II:3 (73) + point sentence I_II:5 S1 (9). Solution exposition between problem and point = one paragraph (I_II:4 S4–S6), at the limit (close call). |

## (a) Mandatory ledger

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| abstract:1 | point (abstract) | pass (S1–S2 open on "change… weights" and "the system is improving") | pass (within abstract; its S10 is the canonical statement repeated later, see I_II:6, I_II:29) | FLAG: subjects hop across nine topics: "Deployed AI systems" → "These changes" → "This survey" → "We" → "these decisions" → "automatic acceptance tests" → "Promotion" → "The feedback" → "Exact checks…" → "an accepted edit" → "We" → "The resulting framework" | FLAG: S6 opens on new information "Among recently added systems with a local adaptation loop"; S9 opens on four new terms "Exact checks, observed outcomes, judgments, and delayed rewards" | pass (close call: S1 stress is "model weights are updated", the contrast term; S2 completes the two-sentence opening on "the system is improving") | pass (close call: S8 "this pattern" points to S6–S7, which were never called a pattern) | pass | FLAG: S6 verb arrives after 12 words ("Among recently added systems with a local adaptation loop, automatic acceptance tests are present"); S9 subject is a four-item abstract list | FLAG: S7 "none documents their integration into governed promotion across organizations" (of-chain of nominalizations); S6 "are present in"; S4 "whether there is enough evidence" | pass (S7 37 words but point-first: "Promotion is more fragmented:") | FLAG: S10 ends "on which it was evaluated" (preposition/relative tail); S4 ends "share it more widely" (qualifier) | pass (close call: S12 "can already automate" / "is still required" kept because they carry the current-state contrast) | pass (S6 measured "89 of 96" stated flat; S8 "helps explain" calibrated) | pass | FLAG: equal-weight contribution list in S11 ("five conditions…, a classification…, and four properties…"); synonym cycling "local improvement loop" (S5) → "local adaptation loop" (S6); "changes" (S1–S3) → "edit" (S4); "attribution" (S6) where the paper's term is "credit assignment"; abstract ends on framework, not on the finding |
| I_II:1 | prelude + context | FLAG: S1 ends "in a repository" (scene-setting); theme words ("persistent artifacts outside the model's weights") first appear in S5 | pass (S3 and S5 both say the change is outside the weights, but S5 generalizes the case, close call) | FLAG: subjects hop "A coding agent" → "An engineer" / "the next session" → "The model" / "the deployed system" → "Similar changes" / "an assistant" → "Much of the experience"; protagonist (the deployed system or its artifacts) is subject once | pass (close call: S2 opens on the new character "An engineer", acceptable in narrative) | FLAG: opening sentence stress "naming convention in a repository" names the scene, not the concept the story shows | FLAG: S2 "its instructions" can resolve to "a repository" (the nearest noun; repositories carry instruction files) or to "A coding agent"; S5 "these persistent artifacts" presents as old a category never named (the line, the preference, the skill were not called artifacts) | pass | FLAG: S5 subject "Much of the experience that makes an AI system useful in one setting" runs 13 words before "accumulates" | pass | FLAG: S5 relative clause "that makes an AI system useful in one setting" interrupts subject and verb | pass | pass | FLAG: S5 flat thesis claim tucked into a prelude, "now accumulates in these persistent artifacts", with no citation or forward pointer | pass | FLAG: cinematic present-tense cold open in a research paper; tidy antithesis S3 "The model has not changed, but the deployed system has." (1 of the section's cap of 1) |
| I_II:2 | context | pass ("scaffold") | pass | pass (close call: "We" → "It" → "it" → "The distinction" → "A team" / "a new model"; scaffold holds S2–S3) | pass | pass (S1 ends on the new term "scaffold") | FLAG: S3 "it is the part … without retraining it": first "it" = scaffold, final "it" = the model; S4 "The distinction" was never stated as a distinction (close) | pass | pass | pass (close call: S5 "a separate training, evaluation, and release process" kept as process terms) | pass | FLAG: S2 ends "control their use" (pronoun); S3 ends "retraining it" (pronoun) | pass | pass | pass | pass (note: the five-item artifact list repeats the abstract's S1 list) |
| I_II:3 | problem | pass ("changes whose value is unknown") | pass (S4 anticipates I_II:6; see I_II:6) | pass (close call: subjects are instances of change, "A rule…", "A corrected memory…", "a demonstrably useful change", a coordinate set) | pass | pass (S1 ends "changes whose value is unknown") | FLAG: S3 "A corrected memory may remain in the history while the system continues to retrieve the outdated entry": "A corrected memory" and "the outdated entry" name the same memory in two states; a reader must re-parse which one remains and which is retrieved | pass | FLAG: S1 abstract subject "The ease of making a change" | FLAG: S1 "The ease of making a change also makes it easy" (nominalization subject + empty verb; ease/easy echo) | pass | pass | pass | pass ("may", "can" mark possibilities, right weight) | pass | pass (note: turn word missing, see flags-only 5.3b) |
| I_II:4 | problem → method | pass ("two questions") | pass | FLAG: S4 "This survey" breaks the string "These situations" → [questions] → "The first" → "The second" | pass | pass | FLAG: S5 "The first" follows S4 "256 public production and research systems", so "The first" can briefly read as the first system rather than the first question | pass | pass | pass | pass (S6 30 words, colon-led list, point first) | pass (close call: S3 ends on pronoun "sharing it", acceptable in a short question) | pass | pass | pass | pass |
| I_II:5 | point (finding 1) | pass ("unevenly") | pass (S2 repeats abstract S6 by design) | FLAG: "The systems surveyed" → "Automatic tests" → "The steps" → "failures" / "a failed output" → "production platforms" | FLAG: S4 opens on new information "Meanwhile, production platforms" | pass (S1 ends "unevenly") | pass | pass (close call: S2–S3 tell the loop backward, gate first then capture and attribution; deliberate strong-to-weak order) | FLAG: S2 abstract subject "Automatic tests for accepting a local edit" + "are present"; S3 subject "The steps that should supply those tests with well-founded candidates" runs 11 words before "are weaker" | FLAG: S2 "are present in" (presence frame) | pass | FLAG: S3 ends "caused it" (pronoun) | FLAG: S4 "substantial" (unmeasured adjective); "Meanwhile" (temporal connective, relation is contrast) | pass (S3 "often", "rarely" unquantified but survey-level; close call) | pass | FLAG: intensifier "substantial"; synonym cycling "change" (I_II:3–4) → "edit" (S2); bluffing connective "Meanwhile" |
| I_II:6 | point (finding 2) | FLAG: S1 "Sharing adds a further limitation" frames vaguely; the paragraph's claim (no system documents governed cross-organization promotion) arrives in S6 | FLAG: S2–S3 ("A change that improves one deployment has been evaluated against that deployment's tasks and measure of success. Another deployment may need different behavior.") restate I_II:3 S4 ("Even a demonstrably useful change can become harmful when copied into a deployment with different tasks or conventions") | FLAG: "Sharing" → "A change" → "Another deployment" → "Shared formats and registries" → "Some surveyed systems" → "None" | pass | FLAG: opening stress "a further limitation" is generic; the themes (receiving-side evidence, governed cross-organization promotion) appear only in S4–S6 | pass | pass | pass | pass (close call: S6 "promotion across organizations" kept as a theme term) | pass (see flags-only 4.13 for S6 attachment) | pass | pass | pass | pass | FLAG: synonym cycling "local improvement loop" (S6) vs "local loop" (I_II:4); point-last paragraph |
| I_II:7 | point (finding 3) | pass ("The feedback available to each system") | FLAG: S6 "none establishes an improvement beyond what it actually measures" restates I_II:6 S2 and abstract S10 | FLAG: after S1 the subjects are four different example types, "A compiler or test suite" → "A booked appointment" → "A writing task" → "A research decision" → "These signals"; feedback itself is subject only in S1 and S6 | pass (close call: S3–S5 open on new examples, read as a list) | FLAG: S1 stress is the pointer "these differences"; the theme (kinds of feedback) sits at the start and never reaches a stress position | pass (close call: S6 "These signals" summarizes the four examples, though S1 called them "feedback") | pass | pass | pass | pass | FLAG: S1 ends on the pointer "these differences" | FLAG: S6 "actually" (tic) | pass ("helps explain", "can drift", "may take" are calibrated) | pass | FLAG: synonym cycling "feedback" (S1) → "signals" (S6); tic "actually" |
| I_II:8 | housekeeping (roadmap, 100 words, not exempt) | pass (close call: "a framework for reading this evidence") | pass | pass (close call: "The survey" / "We" / "The later sections" / "The evidence" / "Its scores", one actor in two names) | pass | pass (close call) | FLAG: S1 "this evidence" (feedback? the survey's evidence? never named); S4 "these checks" (no checks named in I_II:7–8); S4 "its components" (its = "the unassembled architecture", separated by "the findings" and "the research lines") | pass | pass | FLAG: S2 "the conditions under which artifact maintenance constitutes optimization" (two nominalizations + empty verb) | FLAG: S4 three coordinated predicates, two carrying relative clauses, one nested ("failures that arise when these checks are missing", "research lines that produced its components") | FLAG: S6 ends "released for inspection" (scope caveat in the paragraph's and section's stress) | pass | pass | pass | FLAG: caveat in the stress position closing the Introduction; synonym cycling "governed sharing" (S4) vs "governed promotion" (abstract S7) |
| I_II:9 | section opening (II) | pass | pass | FLAG (mild): subjects alternate "Adding a naming rule" → "the team" → "the change" / "it" → "the team" → "Repeating this process" | pass | FLAG: S1 ends "a reasonable response"; the section theme ("a procedure for improving the deployment") arrives only in S5 | pass (close call: S2 "the team" is presented as old; I_II:1 had "An engineer", I_II:2 "A team") | pass (add rule → rerun → compare → keep or reverse → repeat, in order) | pass (close call: S1 gerund subject, verb at word 8) | pass | pass | FLAG: S4 ends "reverse it" (pronoun) | pass | pass | pass | pass |
| I_II:10 | body | pass ("a record of failures") | pass | FLAG: "The procedure" → "Repeated failures" → "the system" → "A stale memory entry"; actor shifts from "the team" (I_II:9) to "the system" (S3) without comment | pass (close call: S4 opens on the example "A stale memory entry") | pass | pass | pass (record → group → prioritize → identify) | pass | pass (close call: S4 "calls for a different intervention") | pass | pass | pass | pass ("tries to identify" right weight) | pass | pass |
| I_II:11 | body (definitions) | pass ("credit assignment") | pass | FLAG (mild): "We" → "It" → "The system" → "The acceptance test" → "An accepted edit" / "subsequent evidence of regression" → "Fig." | pass | pass | pass | pass | pass | FLAG: S5 "subsequent evidence of regression can trigger rollback" (nominalization subject with of-chain) | pass | pass | pass | pass | pass | pass (note: three new terms in one paragraph, see flags-only 4.15 / house style) |
| I_II:12 | body (definitions) | pass (close call: S1 stress "actual workload"; the new term "patch" follows in S2) | pass | FLAG (mild): "The evaluation" → "A deployment" → "Its patch loss" → "this" → "A gate" | pass | pass (close call) | pass | pass | pass | FLAG: S5 "can establish an improvement" (empty verb + nominalization) | pass | FLAG: S5 ends on pointer "this loss" | FLAG: S1 "actual"; S2 "particular" (tic words) | pass | pass | pass |
| I_II:13 | body (running example) | pass | pass (close call: S4 restates I_II:6 S3 through the running example; kept as illustration) | FLAG: "the naming rule" → "The team" → "That decision" → "Other repositories" / "the local evaluation" | pass | FLAG: S1 ends "the original repository" (scene); the theme ("changes the population") arrives in S3 | pass | pass | pass | pass | pass | FLAG: S4 ends "about them" (pronoun) | pass | pass | pass | pass |
| I_II:14 | body (definitions) | pass ("evidence at the receiving scope") | FLAG: S4 "A local success does not automatically enlarge that radius" restates I_II:13 S4 ("the local evaluation says little about them") and I_II:6 S2–S3 | FLAG: "The promotion loop" → "We" → "The evidence radius" → "A local success" → "Section REF(sec:design)" | FLAG: S3 opens on a new term, "The **evidence radius** is the scope…" | pass | pass | pass | pass | pass (close call: S2 "a check conducted on the tasks of the deployment" of-chain) | pass | FLAG: S5 ends "between them" (pronoun) | FLAG: S5 "already" (inferable) | pass | pass | FLAG: synonym cycling "the edit" (S2) → "the change" (S3) in adjacent sentences |
| I_II:15 | body (list lead-in, 19 words; carries the definition, not exempt) | pass | pass | pass | pass | pass (ends "through five conditions:") | pass | pass | pass | pass | pass (see flags-only 4.13) | pass | FLAG: "the form of maintenance" (redundant category) | pass | pass | FLAG: term drift, heading "Five conditions for artifact-layer optimization" vs defined term "artifact-layer descent" |
| I_II:16 | list item 1 | pass (bold label frames) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| I_II:17 | list item 2 | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass (close call: ends "later changes", where the list's term is "edit") | pass | pass | pass | pass |
| I_II:18 | list item 3 | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass (short interruption "at least sometimes" acceptable) | pass | pass | FLAG: stacked hedge "can, at least sometimes, be traced" (load-bearing, see AUTHOR FLAGS) | pass | pass |
| I_II:19 | list item 4 | pass | pass | pass | pass | pass | FLAG: "the process proposes" presents "the process" as old; the "proposal process" is introduced only later (I_II:22 S2, "A proposal process") | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: label "A candidate edit" vs body "a change" |
| I_II:20 | list item 5 | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: "only after a check of whether it lowers the relevant loss" (nominalization + of-whether) | pass | pass | pass | pass | pass | pass |
| I_II:21 | body (taxonomy of maintenance) | pass (two-sentence opening ends "three recurring forms of maintenance") | pass (close call: S1 "The model weights remain fixed" repeats I_II:1 S3 and I_II:2 S3) | FLAG: "The model weights" / "the edits" → "These conditions" → "an engineer" → "a system" → "Artifact-layer descent" → "the optimization interpretation" | FLAG: S1 opens on "The model weights", not on anything the list just ended on ("the relevant loss") | pass (close call; S1 is a separate claim, see flags-only 1.5) | FLAG: S1 "this process" (the five conditions are not a process); S2 "These conditions" (the five, or the two S1 just added?); S5 "that trace" points to an action S4 negated ("without tracing failures to their causes") | pass | FLAG: S6 abstract subject "the optimization interpretation" | FLAG: S6 "the optimization interpretation is correspondingly limited"; S5 "before acceptance" | pass | FLAG: S6 ends "correspondingly limited" (qualifier) | FLAG: S6 "correspondingly" (inferable) | FLAG: S6 vague hedge "is correspondingly limited" does not say how the interpretation weakens | pass | FLAG: caveat in the stress position closing the paragraph; term drift "optimization" vs "descent"; "change" (S5) vs "edit" (S1) |
| I_II:22 | body (formalization; display math n/a) | pass ("write the patch loss as") | pass (close call: S7 anticipates the Human gate of I_II:24–26) | FLAG: two protagonists: the loss and proposal (S1–S3: "[we] write", "A proposal process", "There is no analytic gradient") and the gate (S4–S7: "the gate", "Ω", "An evaluation", "A reviewer or governance process") | pass | pass | pass | pass | pass (close call: S6 subject "An evaluation that blocks a regressing merge" is 7 words with a relative clause) | FLAG: S6 "is a practical instance of this rule" (empty verb + nominalization) | pass (display equations between clauses are math convention) | FLAG: S6 ends on pointer "this rule" | pass (close call: "practical", "required" kept) | pass | pass | pass |
| I_II:23 | body (formal result) | pass | pass | pass (close call: "Appendix" → "improving edits" → "This" → "A limited proposal process", short paragraph) | FLAG: S2 opens on new information "With additional coverage, compactness, and summable-bias assumptions" | pass | pass | pass | pass (close call: subject after 7 words in S2) | pass | pass | pass | pass | pass | pass | pass (close call: antithesis S3 "not a claim of global optimality", within cap) |
| I_II:24 | body (subsection opening) | pass ("author" vs "authority") | pass | pass (close call: parallel pairs in S2) | pass | pass (close call: S1 stress "are separate", themes are the subject) | pass | pass | FLAG: S1 subject "The author of an edit and the authority that accepts it" runs 11 words with a relative clause | FLAG: S3 "who makes the acceptance decision" (empty verb + nominalization) | pass | pass | pass | pass | pass | FLAG: synonym cycling "edit" (S1) → "revision" (S2, twice) |
| I_II:25 | list item (Auto) | pass | pass | pass | pass | pass | pass ("that judge" = language-model judge) | pass | FLAG: S2 subject "Whether that judge has been calibrated against people" runs 9 words | pass | pass | FLAG: S2 ends "takes up" (phrasal-verb tail on a cross-reference) | pass | pass | pass | pass (note: a forward caveat inside a list item; see flags-only 5.2, 4.12) |
| I_II:26 | list item (Human) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | FLAG (mild): "the change" where the subsection says "edit" |
| I_II:27 | list item (None) | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: "no acceptance decision is made" (nominalization + empty passive verb) | pass | pass | pass | pass | pass | pass |
| I_II:28 | body (notation) | pass | pass | pass ("A pair" → "These labels" → "They") | pass | pass (ends "human promotion gate") | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| I_II:29 | section close | pass ("two limits") | FLAG: S2 "an accepted edit is evidence of improvement only on the measure and tasks evaluated" is the sixth statement of this proposition (abstract S10; I_II:6 S2–S3; I_II:7 S6; I_II:13 S4; I_II:14 S4) | FLAG: "The loss definition" → "an accepted edit" → "Promotion" → "the loop" → "It" → "Revising the evaluator" | pass | FLAG: S1 stress "on every such loop"; the theme "two limits" sits mid-sentence | FLAG: S1 "every such loop" (which loops? the gate-classified ones, or both local and promotion loops?); S3 "that meaning" (no meaning was stated; the referent is the scope of S2's evidence) | pass | pass | pass | pass | FLAG: S1 ends "every such loop" (pointer); S6, the section's last words, end on a forward cross-reference "a complication we return to in Section REF(sec:reflexive)" | pass | pass | pass | FLAG: section ends on a forward pointer rather than arrival (house rule 10) |

FLAG cell count (table a): 95 (columns 2.1 through AI-sweep; the kind column is not counted).

## (b) Flags only (other paragraph-level tests)

| ¶ | test | finding (quote the words) |
|---|---|---|
| abstract:1 | 2.2 point position | The findings sit in S6–S9, but the abstract ends on contributions (S11 "five conditions…, a classification…, and four properties…") and a framework claim (S12), not on the finding (house rule: the abstract is a result announcement, not a table of contents). |
| abstract:1 | 2.3 theme recurrence | Drift: "changes" (S1–S3) → "edit" (S4, S10); "local improvement loop" (S5) → "local adaptation loop" (S6); "failure capture and attribution" (S6) vs the paper's "failure log" / "credit assignment". |
| abstract:1 | 3.5 connective audit | S11 "We use this observation to develop five conditions…, a classification…, and four properties…": the relation claimed (the conditions derive from S10's observation) is stronger than the text shows; the conditions are defined independently in Section II. |
| abstract:1 | 4.12 coordination | S4 "whether an edit improves the deployment that produced it, and whether there is enough evidence to share it more widely": the two decisions are not parallel in logic (a fact vs the sufficiency of evidence). |
| abstract:1 | 4.15 new terms | Unglossed for an abstract reader: "recently added systems" (added to what?), "lineage", "governed promotion", "artifact-layer optimization", "gate types". |
| abstract:1 | 6.3 claim calibration | S12 "identifies what existing systems can already automate" is stronger than a documentation-based survey shows (close call; see AUTHOR FLAGS). |
| I_II:1 | 1.6 illustration | pass with note: the case shows the mechanism (a line in the instructions) but its outcome rests on one session ("the next session follows the convention"); I_II:9 picks this up deliberately ("To learn whether it works, however, the team must run the agent again"), so it works as a setup. |
| I_II:1 | 4.2 who does what | S4 "when an assistant corrects a stored preference": the corrector is ambiguous (the user corrects it, or the assistant does?). |
| I_II:1 | 6.3 claim calibration | S5 "Much of the experience … now accumulates in these persistent artifacts" is a field-level claim with no citation or pointer to the evidence. |
| I_II:2 | 4.13 modifiers | S3 "the part surrounding the model that a deployment can inspect and revise": "that…" can attach to "the model". |
| I_II:2 | 4.2 who does what | S3 "that a deployment can inspect and revise": a deployment is cast as the actor; the operators or the team inspect and revise. |
| I_II:3 | 5.3b missing metadiscourse | The turn from context (I_II:2) to problem (I_II:3 S1) is unmarked; a *but* would show it. |
| I_II:4 | 1.5 relevance/placement | S4 (method: "This survey uses those questions to examine 256 public production and research systems") sits between the questions (S2–S3) and the loops they define (S5–S6). |
| I_II:5 | 2.4 framing / house rule "one claim per paragraph" | S4 ("production platforms have built substantial versioning and release machinery without any process that proposes changes from deployment experience") is a separate finding about production platforms inside the local-loop paragraph. |
| I_II:5 | 3.5 connective audit | S4 "Meanwhile" claims simultaneity; the real relation is contrast (strong release machinery, no proposal process). |
| I_II:5 | 4.15 new terms | S2 "recently added system" is not glossed (the corpus and its additions are described only in Section III). |
| I_II:6 | 2.2 point position | The paragraph's claim ("None documents an automatic local improvement loop connected to promotion across organizations with versioned lineage, access control, and rollback") is its last sentence; S1–S4 build to it. |
| I_II:6 | 4.13 modifiers | S6 "connected to promotion across organizations with versioned lineage, access control, and rollback": "with…" can attach to "organizations" or to "promotion". |
| I_II:6 | 4.15 new terms | S5 "within one operator" ("operator" is new; "organization" is the term used elsewhere). |
| I_II:7 | 4.12 coordination | S2–S5 list non-parallel things: a checker ("A compiler or test suite"), an outcome ("A booked appointment"), a task ("A writing task"), a decision ("A research decision"). |
| I_II:7 | 4.2 who does what | S3 "A booked appointment provides a later, noisier outcome": the appointment is the outcome, not its provider. |
| I_II:8 | 2.3 theme recurrence | "governed sharing" (S4) vs "governed promotion" elsewhere; "local adaptation" (S3) vs "local loop". |
| I_II:8 | 1.7 order / roadmap coverage | The roadmap names Sections II–IX by content but not the open-problems/conclusion section (X); note only. |
| I_II:8 | 4.11 tacked-on chain | S4 "failures that arise when these checks are missing" (relative clause containing a *when* clause) plus "research lines that produced its components". |
| I_II:9 | 2.2 point position | Section opening's point ("Repeating this process turns a growing collection of fixes into a procedure for improving the deployment") is the paragraph's last sentence; acceptable for an opening paragraph, noted. |
| I_II:10 | 1.8 headings | "The local loop" is a label heading, not a theme. |
| I_II:10 | 4.2 / 4.5 who does what, voice | S2 "Repeated failures are grouped into modes and prioritized": agent hidden; I_II:9 used "the team", S3 switches to "the system". Who acts matters to the paper's Auto/Human classification. |
| I_II:11 | house rule "one concept per paragraph" / 4.15 | Three new terms in six sentences ("credit assignment", "coordinate", "gate"), plus versioning and rollback. |
| I_II:11 | 4.13 modifiers | S2 "an editable part of the scaffold, or **coordinate**": "or" can read as an alternative rather than a gloss. |
| I_II:12 | 4.15 new terms | Two new terms ("patch", "patch loss") are introduced in stress positions, which is good; "operational measure" is not glossed (close call). |
| I_II:13 | 4.12 coordination | S4 "Other repositories may follow a different convention, and the local evaluation says little about them": *and* hides *so* (they may differ, so the local evaluation says little). |
| I_II:13 | 4.2 who does what | S1 "the naming rule improves the original repository": the rule improves the agent's work in the repository, not the repository. |
| I_II:14 | 4.15 new terms | Three new terms in five sentences: "receiving scope" (S1, unglossed), "receiving-side evaluation" (S2), "evidence radius" (S3, at the sentence start). |
| I_II:15 | 4.13 modifiers | "the form of maintenance that connects recurring failures to measured improvements through five conditions": "through five conditions" attaches to "connects", which makes the conditions the means of connection rather than the criteria. |
| I_II:15 | 2.3 theme recurrence / 1.8 headings | Heading "Five conditions for artifact-layer optimization" vs defined term "artifact-layer descent"; I_II:21 S6 adds "the optimization interpretation". |
| I_II:16–20 | 4.12 coordination | Item clauses are grammatically parallel but switch subject and voice: "the deployment has" / "relevant failures are retained" / "failures can… be traced" / "the process proposes" / "an edit is retained or promoted". Close call. |
| I_II:20 | 2.3 theme recurrence | "retained or promoted": a promotion term inside the local-loop conditions (intended? see AUTHOR FLAGS). |
| I_II:21 | 1.5 relevance/placement | S1 ("The model weights remain fixed during this process, and the edits persist beyond the current interaction") adds two scope conditions after the five-item list; it belongs with the list's lead-in or with I_II:22's θ_M definition, not as the opening of the taxonomy paragraph. |
| I_II:21 | 4.12 coordination | S3–S4 use "In *patchwork*, …" / "In *random artifact search*, …", but the third member switches to "Artifact-layer descent uses that trace…". |
| I_II:22 | 4.15 new terms / symbols | Symbols used without definition: π in "ℓ(π(θ_M,θ_s,x))", x, and λ in "+λΩ(z_t)". The superscript t on θ_s^t is inferable. (See AUTHOR FLAGS.) |
| I_II:22 | house rule "one claim per paragraph" | One Markdown paragraph carries the loss definition, the proposal process, the absence of a gradient, the gate rule, its parameters and two practical instances (117 words + two display equations). |
| I_II:23 | 6.2 plain paraphrase | S2 "improving edits eventually stop clearing the gate" reads in plain terms as "good edits start being rejected"; the intended reading (eventually no available edit clears the gate) is hidden. (See AUTHOR FLAGS.) |
| I_II:24 | 4.8 whole-subject length | S1 subject has 11 words with a relative clause ("the authority that accepts it"). |
| I_II:25 | 5.2 metadiscourse | S2 "is a separate question, which Section REF(sec:signal) takes up": about half the sentence is about the paper. |
| I_II:25–27 | 4.12 coordination | Unequal items: Auto has two sentences with a forward caveat; Human one clause; None switches to a passive nominal ("no acceptance decision is made") where the others have an actor ("a program applies", "a person decides"). |
| I_II:29 | house rule "honest accounting in one place" | The scope caveat recurs in six places across the abstract, Introduction and Section II (see 2.5). |

## (c) Suggested moves (one line per FLAG, keyed by ¶ and test)

- **Doc 1.1 (turn):** mark the context→problem turn at I_II:3 S1 with *but*.
- **Doc 1.1 (point):** add one point sentence (I_II:5 S1 is the natural slot) that names all three findings before I_II:5–7 develop them; end I_II:8 on the framework, not the release caveat.
- **Doc 1.2:** either recast I_II:1 as shared context (open on the general claim, then the coding-agent case as its illustration) or keep the vignette but move S5's claim to I_II:2 and give it a pointer to the evidence; the running example must survive (I_II:9, I_II:13 use it).
- abstract:1 3.1: make the deployment/its edits the running subject for S4–S10 where the grammar allows; keep "We" only for what the authors do.
- abstract:1 3.2: open S6 on the known loop ("Local loops almost always…") and S9 on "These classes of feedback" after naming the class once.
- abstract:1 4.1: put the subject first in S6 and S9.
- abstract:1 4.3: verbalize S7's "integration into governed promotion" ("none documents how they combine to govern promotion…").
- abstract:1 4.14: end S10 on "evaluated on" content (move "only" scope to the stress), S4 on the evidence term.
- abstract:1 AI-sweep: fix the term registry (change vs edit; one name for the local loop; credit assignment); end on the finding, compress S11's contribution list.
- I_II:1 2.1/3.6: end the opening sentence on the concept the story shows (a persistent change outside the model), not on "a repository".
- I_II:1 3.1: keep the deployed system or its instruction file as the subject of most clauses.
- I_II:1 3.7: replace "its instructions" with "the agent's instructions"; name the category before "these persistent artifacts".
- I_II:1 4.1/4.9: shorten S5's subject; move the relative clause after the verb.
- I_II:1 5.3: move S5's thesis claim out of the vignette or give it a forward pointer to the corpus evidence.
- I_II:1 AI-sweep: keep at most one antithesis in Section I; see 1.2 for the cold open.
- I_II:2 3.7: name the model in S3's final clause; name "the distinction" (scaffold vs weights) in S4.
- I_II:2 4.14: end S2 and S3 on nouns, not "their use" / "it".
- I_II:3 3.7: say which entry remains and which is retrieved (the correction vs the outdated entry).
- I_II:3 4.1/4.3: make the team or the change the subject of S1 ("Because a change is easy to make, changes of unknown value accumulate").
- I_II:4 3.1/3.7: move S4 (the corpus sentence) after S6 so "The first" follows the questions.
- I_II:5 3.1/3.2: keep "the surveyed systems" or "the local loop" as the running subject; open S4 on the contrast, not "Meanwhile".
- I_II:5 4.1/4.3: make the systems the subject of S2 and the missing steps the object in S3.
- I_II:5 4.14: end S3 on the artifact list, not "caused it".
- I_II:5 5.1/AI-sweep: drop "substantial" or replace with the measured relationship; replace "Meanwhile" with the real contrast; use "edit" consistently.
- I_II:6 2.1/3.6: open on the finding about cross-organization promotion so the opening stress names it.
- I_II:6 2.5: cut or compress S2–S3, pointing back to I_II:3 S4.
- I_II:6 3.1: keep "sharing"/"promotion" or "the surveyed systems" as subject.
- I_II:6 AI-sweep: use "local loop" (the defined term).
- I_II:7 2.5: cut S6's second clause or merge it into the one canonical statement of the scope limit.
- I_II:7 3.1: make the feedback the subject of S2–S5 ("Feedback from a compiler…", "Feedback from a booked appointment…") or name each signal type.
- I_II:7 3.6/4.14: end S1 on the theme (the kind of feedback a system receives).
- I_II:7 5.1/AI-sweep: drop "actually"; pick "feedback" or "signal" and keep it.
- I_II:8 3.7: name the evidence (published methods and documentation), the checks (the gates) and the architecture's components.
- I_II:8 4.3: verbalize S2 ("when maintaining artifacts counts as optimization").
- I_II:8 4.9–4.11: split S4 into two sentences.
- I_II:8 4.14/AI-sweep: move the release and no-new-experiments scope notes before the roadmap's final item, or close on the framework's purpose.
- I_II:9 3.1: keep the team (or the rule) as the running subject.
- I_II:9 3.6: let S1 end on the theme of measurement (the response is reasonable but untested).
- I_II:9 4.14: end S4 on "reverse the change" or a noun.
- I_II:10 3.1: name one actor for grouping and attribution (the team or the system) and keep it.
- I_II:11 3.1: keep the loop step or the edit as the running subject.
- I_II:11 4.3: verbalize S5 ("if the edit later causes regressions, it can be rolled back").
- I_II:12 3.1: keep the evaluation (or the gate) as subject from S1 to S5.
- I_II:12 4.3/4.14: verbalize "establish an improvement"; end S5 on "patch loss".
- I_II:12 5.1: cut "actual" and "particular".
- I_II:13 3.1: keep the team (or the rule) as the running subject.
- I_II:13 3.6: end S1 on the decision to share or the template.
- I_II:13 4.14: end S4 on "other repositories".
- I_II:14 2.5: keep one statement of the radius limit (here) and cut the earlier restatements, or vice versa.
- I_II:14 3.1/3.2: open S3 on the old item ("The scope that this evaluation supports is the change's evidence radius"), new term last.
- I_II:14 4.14/5.1: end S5 on the scopes; cut "already".
- I_II:14 AI-sweep: use "edit" in S2 and S3.
- I_II:15 5.1: cut "the form of".
- I_II:15 AI-sweep: align the heading with "artifact-layer descent" (heading wording is the author's call).
- I_II:18 5.3: flag only; the hedge is part of the condition (see AUTHOR FLAGS).
- I_II:19 3.7: say "a proposal process" here, or define it in the lead-in.
- I_II:19 AI-sweep: use "edit" in the item body.
- I_II:20 4.3: "only if a check shows it lowers the relevant loss".
- I_II:21 3.1/3.2/1.5: move S1 to the list's lead-in or to I_II:22; open on "These conditions distinguish three recurring forms of maintenance".
- I_II:21 3.7: repeat the noun ("the five conditions"; "the trace from failure to cause").
- I_II:21 4.1/4.3/4.14/5.1/5.3: say concretely what a partly met condition costs the optimization reading, ending on that cost (flag if this needs new claim wording).
- I_II:21 AI-sweep: one term for the method ("descent"); "edit" throughout.
- I_II:22 3.1: split into a loss paragraph (S1–S3) and a gate paragraph (S4–S7).
- I_II:22 4.3/4.14: "A merge check that blocks regressions applies this rule" (verb, ends on the instance).
- I_II:23 3.2: open S2 on the result and move the assumptions to the end, or on "Under three further assumptions (…)".
- I_II:24 4.1: shorten S1's subject ("Who writes an edit and who accepts it are separate questions").
- I_II:24 4.3: "We classify the gate by who accepts the edit".
- I_II:24 AI-sweep: use "edit" for "revision".
- I_II:25 4.1/4.14: move the calibration caveat to its own short clause ending on the concept, or to Section V's pointer.
- I_II:26 AI-sweep: "the edit".
- I_II:27 4.3: give None an actor parallel to the others ("nothing decides: either…").
- I_II:29 2.5: keep this closing statement as the canonical one and shorten the earlier ones, or point back from here.
- I_II:29 3.1: keep "the loop" as the running subject.
- I_II:29 3.6/4.14: end S1 on "two limits"; end the section on the limit itself, moving the forward pointer before it.
- I_II:29 3.7: name the loops ("every local and promotion loop") and the meaning ("the scope of that evidence").
- I_II:29 AI-sweep: end Section II on arrival, not a pointer.

## (d) Role-level verdicts

| ¶ | role-level test failed / passage-test fail count (2.5, 3.1, 3.2, 3.6, 3.7, 3.8) | verdict |
|---|---|---|
| abstract:1 | none role-level; passage fails 2 (3.1, 3.2) | keep-and-polish |
| I_II:1 | **prelude 1.2 (genre, contents)**; passage fails 3 (3.1, 3.6, 3.7) | re-draft |
| I_II:2 | none; 1 (3.7) | keep-and-polish |
| I_II:3 | none; 1 (3.7) | keep-and-polish |
| I_II:4 | placement 1.5 (S4) fixable by moving one sentence; 2 (3.1, 3.7) | keep-and-polish |
| I_II:5 | none; 2 (3.1, 3.2) | keep-and-polish |
| I_II:6 | none role-level; 3 (2.5, 3.1, 3.6) | re-draft |
| I_II:7 | none role-level; 3 (2.5, 3.1, 3.6) | re-draft |
| I_II:8 | none; 1 (3.7) | keep-and-polish |
| I_II:9 | none; 2 (3.1, 3.6) | keep-and-polish |
| I_II:10 | none; 1 (3.1) | keep-and-polish |
| I_II:11 | none; 1 (3.1) | keep-and-polish |
| I_II:12 | none; 1 (3.1) | keep-and-polish |
| I_II:13 | none; 2 (3.1, 3.6) | keep-and-polish |
| I_II:14 | none role-level; 3 (2.5, 3.1, 3.2) | re-draft |
| I_II:15 | none; 0 | keep-and-polish |
| I_II:16 | none; 0 | keep-and-polish |
| I_II:17 | none; 0 | keep-and-polish |
| I_II:18 | none; 0 | keep-and-polish |
| I_II:19 | none; 1 (3.7) | keep-and-polish |
| I_II:20 | none; 0 | keep-and-polish |
| I_II:21 | **placement 1.5 (S1 belongs with the list)**; 3 (3.1, 3.2, 3.7) | re-draft |
| I_II:22 | none role-level; 1 (3.1); split into two paragraphs advised | keep-and-polish |
| I_II:23 | none; 1 (3.2) | keep-and-polish |
| I_II:24 | none; 0 | keep-and-polish |
| I_II:25 | none; 0 | keep-and-polish |
| I_II:26 | none; 0 | keep-and-polish |
| I_II:27 | none; 0 | keep-and-polish |
| I_II:28 | none; 0 | keep-and-polish |
| I_II:29 | none role-level; 4 (2.5, 3.1, 3.6, 3.7) | re-draft |

## AUTHOR FLAGS (fixes that would touch a claim, number, citation, symbol or cross-reference)

1. **I_II:22, undefined symbols.** π (in ℓ(π(θ_M,θ_s,x))), x and λ (in +λΩ(z_t)) are never defined in the text. Defining them adds formal content; the author should supply the glosses (presumably π = the deployed policy/system, x = an input drawn from D, λ = the weight on the complexity/breadth penalty), checked against Appendix REF(app:formal).
2. **I_II:23 S2, statement of the stability result.** "improving edits eventually stop clearing the gate" can be read as "good edits get rejected". Rewording the result is a claim change; the author should confirm the intended statement against the appendix theorem (e.g., whether it means that eventually no proposed edit clears the gate).
3. **I_II:18, stacked hedge in condition 3.** "failures can, at least sometimes, be traced" is part of the condition's definition; removing either hedge changes the condition. Keep unless the author decides.
4. **I_II:20, "retained or promoted".** Condition 5 mentions promotion inside the local-loop conditions; confirm whether the five conditions are meant to cover promotion gates too (the gate rule's Ω also penalizes "promotion breadth", I_II:22 S5).
5. **abstract:1 S11, "We use this observation to develop five conditions…".** The derivation claimed (conditions developed from the observation in S10) is a claim about the paper's logic; rephrase only with the author's agreement.
6. **abstract:1 S12, "identifies what existing systems can already automate".** Calibration for a documentation-based survey (6.3); weakening it changes the claim.
7. **I_II:1 S5, "Much of the experience … now accumulates in these persistent artifacts".** A field-level claim with no citation or pointer in the Introduction; the author may want a pointer to the corpus section or a citation.
8. **I_II:2 S3, attribution to [@zaharia2024compound].** "In the language of compound AI systems [@zaharia2024compound], it is the part surrounding the model that a deployment can inspect and revise without retraining it": whether the cited source frames the non-model components in these terms was not verified in this pass; a reviser must read the source before rewording this sentence.
9. **Term registry decisions (headings and defined terms).** "artifact-layer optimization" (abstract S11; heading of the five-conditions subsection) vs "artifact-layer descent" (the defined term); "local improvement loop" / "local adaptation loop" / "local loop"; "governed promotion" / "governed sharing". Changing headings or a defined term affects cross-references and other sections; the author should fix the registry once.
10. **I_II:8, roadmap coverage.** The roadmap does not mention the final open-problems/conclusion section; adding it means naming a section, which the author should confirm.

## Group A (abstract, I, II): R-2 reverse outline

# Reverse outline, group A: abstract, Section I (Introduction), Section II (the loop)

Numbering matches `ledger_A.md`. Word counts from a script over the source files (list items counted separately; display equations included in I_II:22's count).

## Paragraphs

| ¶ | role | its point in one sentence | protagonist | themes | evidence | words | tests failed |
|---|---|---|---|---|---|---|---|
| abstract:1 | point (abstract) | Systems change outside the weights, and of the two decisions (keep locally, share more widely) the surveyed systems automate local acceptance widely but leave failure capture, attribution and governed cross-organization promotion weak, a pattern the feedback class helps explain. | shifts (systems, changes, survey/we, tests, promotion, feedback, edit, framework) | change outside the weights; local loop vs promotion loop; acceptance tests; feedback classes | 256 systems; 89 of 96 | 237 | 3.1, 3.2, 4.1, 4.3, 4.14, AI-sweep; flags-only 2.2, 2.3, 3.5, 4.12, 4.15, 6.3 |
| I_II:1 | prelude + context | A coding agent's fix shows that a deployed system can change while its model does not, and much useful experience now accumulates in such persistent artifacts. | shifts (agent, engineer, model, assistant, experience) | change outside the weights; persistent artifacts | none (vignette) | 80 | 1.2, 2.1, 3.1, 3.6, 3.7, 4.1, 4.9–4.11, 5.3, AI-sweep; flags-only 4.2, 6.3 |
| I_II:2 | shared context | The scaffold (instructions, skills, memory, tools, orchestration, evaluation and governance rules) is the editable part around the model, and it changes faster than the model. | the scaffold | scaffold; different schedules of change | [@zaharia2024compound] | 87 | 3.7, 4.14; flags-only 4.13, 4.2 |
| I_II:3 | problem | Because changes are easy to make, changes of unknown value accumulate: rules conflict, stale memories persist, and useful changes harm other deployments. | change (instances: rule, memory, useful change) | unknown value; harm on transfer | none (examples) | 73 | 3.7, 4.1, 4.3; flags-only 5.3b |
| I_II:4 | problem → method | Two questions (what evidence justifies keeping a change, and what justifies sharing it) define the local and promotion loops through which the survey reads 256 systems. | the two questions / loops | evidence to keep; evidence to share; local loop; promotion loop | 256 systems | 81 | 3.1, 3.7; flags-only 1.5 |
| I_II:5 | point (finding 1) | The local loop is uneven: acceptance tests are nearly universal (89 of 96) while failure capture and attribution are weak, and production platforms build release machinery without proposing changes. | shifts (systems, tests, steps, platforms) | uneven development; acceptance tests; failure capture; attribution | 89 of 96 | 86 | 3.1, 3.2, 4.1, 4.3, 4.14, 5.1, AI-sweep; flags-only 2.4, 3.5, 4.15 |
| I_II:6 | point (finding 2) | Portability does not establish benefit to a recipient, and no surveyed system documents an automatic local loop connected to governed cross-organization promotion. | shifts (sharing, change, deployment, formats, systems) | sharing; recipient evidence; governed cross-organization promotion | survey coding (none cited) | 75 | 2.1, 2.5, 3.1, 3.6, AI-sweep; flags-only 2.2, 4.13, 4.15 |
| I_II:7 | point (finding 3) | The kind of feedback a system receives (immediate check, delayed outcome, drifting judge, months-long reward) explains much of the unevenness, and no signal establishes improvement beyond what it measures. | shifts (compiler, appointment, task, decision, signals) | feedback classes; automation; measured scope | none (examples) | 65 | 2.5, 3.1, 3.6, 4.14, 5.1, AI-sweep; flags-only 4.12, 4.2 |
| I_II:8 | housekeeping (roadmap + scope) | The survey's framework runs from the two loops through corpus, local adaptation, feedback, promotion, failures, architecture and research lines, using public documentation only, with scores released. | the survey / we | framework; section order; evidence base | none | 100 | 3.7, 4.3, 4.9–4.11, 4.14, AI-sweep; flags-only 2.3, 1.7, 4.11 |
| I_II:9 | section opening (II) | A fix becomes a procedure for improving the deployment only when it is tested on relevant tasks, kept if it helps and reversed if it regresses. | the team / the fix | measured improvement; keep or reverse | none (running example) | 68 | 3.1, 3.6, 4.14; flags-only 2.2 |
| I_II:10 | explanation | The local loop starts from a failure record, groups and ranks failure modes, and looks for the artifact responsible for each. | shifts (procedure, failures, system, memory entry) | failure record; modes; responsible artifact | none | 62 | 3.1; flags-only 1.8, 4.2/4.5 |
| I_II:11 | explanation (definitions) | Linking a failure to its coordinate is credit assignment; the system then proposes an edit, and the gate decides whether it is kept, versioned and later rolled back if needed. | shifts (step, system, test, edit) | credit assignment; coordinate; gate; rollback | Fig. REF(fig:descent) | 63 | 3.1, 4.3; flags-only house rule, 4.13 |
| I_II:12 | explanation (definitions) | The gate's evaluation must estimate the patch loss, the failure rate on the deployment's own distribution of users, tasks and conventions. | shifts (evaluation, deployment, loss, gate) | patch; patch loss; gate evaluation | none | 68 | 3.1, 4.3, 4.14, 5.1; flags-only 4.15 |
| I_II:13 | explanation (running example) | Sharing the naming rule changes the population it acts on, and the local evaluation says little about that population. | shifts (rule, team, decision, repositories) | sharing; population; local evaluation's reach | none (running example) | 45 | 3.1, 3.6, 4.14; flags-only 4.12, 4.2 |
| I_II:14 | explanation (definitions) | Promotion needs receiving-side evaluation, because a local success does not enlarge an edit's evidence radius. | shifts (promotion loop, we, radius, success) | receiving-side evaluation; evidence radius; scopes | Section REF(sec:design) | 67 | 2.5, 3.1, 3.2, 4.14, 5.1, AI-sweep; flags-only 4.15 |
| I_II:15 | point (subsection lead-in) | Artifact-layer descent is maintenance that meets five conditions. | we / artifact-layer descent | artifact-layer descent; five conditions | none | 19 | 5.1, AI-sweep; flags-only 4.13, 2.3/1.8 |
| I_II:16 | explanation (list item 1) | The deployment has a defined measure of success or failure. | the deployment | patch loss | none | 15 | none |
| I_II:17 | explanation (list item 2) | Relevant failures are retained as evidence. | failures | failure log | none | 13 | none |
| I_II:18 | explanation (list item 3) | Failures can, at least sometimes, be traced to responsible coordinates. | failures | credit assignment | none | 15 | 5.3 (author flag) |
| I_II:19 | explanation (list item 4) | A process proposes a change to those coordinates. | the process | candidate edit | none | 12 | 3.7, AI-sweep |
| I_II:20 | explanation (list item 5) | An edit is kept or promoted only after a check that it lowers the relevant loss. | an edit | acceptance gate | none | 21 | 4.3; flags-only 2.3 |
| I_II:21 | explanation (taxonomy) | The five conditions, with fixed weights and persistent edits, separate patchwork, random artifact search and artifact-layer descent, and partial compliance limits the optimization reading. | shifts (weights, conditions, engineer, system, descent, interpretation) | patchwork; random artifact search; artifact-layer descent | none | 85 | 3.1, 3.2, 3.7, 4.1, 4.3, 4.14, 5.1, 5.3, AI-sweep; flags-only 1.5, 4.12 |
| I_II:22 | explanation (formalization) | The patch loss is an expectation over the deployment, and because no gradient exists the gate accepts an edit when its estimated loss change plus a complexity/breadth penalty clears a margin, as merge checks and reviewers do. | the loss, then the gate | patch loss; gate rule; margin; penalty | none (equations) | 117 | 3.1, 4.3, 4.14; flags-only 4.15, house rule |
| I_II:23 | explanation (formal result) | Under stated assumptions the appendix proves a one-step descent inequality and gate stability, which is not global optimality. | the formal result | descent inequality; gate stability; limits | Appendix REF(app:formal) | 56 | 3.2; flags-only 6.2 |
| I_II:24 | point (subsection opening) | Who writes an edit and who accepts it are separate, so the gate is classified by who accepts. | author / authority | proposer vs decider; gate classification | none | 44 | 4.1, 4.3, AI-sweep; flags-only 4.8 |
| I_II:25 | explanation (list item Auto) | An Auto gate is a program's check (verifier, threshold or LLM judge), whose calibration Section V examines. | a program | automatic gate; judge calibration | [@zheng2023judge]; Section REF(sec:signal) | 33 | 4.1, 4.14; flags-only 5.2, 4.12 |
| I_II:26 | explanation (list item Human) | A Human gate is a person's decision. | a person | human gate | none | 10 | AI-sweep (mild) |
| I_II:27 | explanation (list item None) | A None gate means no acceptance decision: no loop, or every edit kept. | (no acceptance decision) | no gate | none | 20 | 4.3; flags-only 4.12 |
| I_II:28 | explanation (notation) | A pair like [Auto × Human] names the local and promotion gates, and the labels say nothing about how well supported a decision is. | the labels | gate pairs; decision mechanism vs support | none | 36 | none |
| I_II:29 | point (section close) | Every loop has two limits: an accepted edit is evidence only on the measure and tasks evaluated, and the loop optimizes a fixed objective that revising the evaluator would change. | shifts (loss definition, edit, promotion, loop, evaluator) | two limits; measured scope; fixed objective | Section REF(sec:reflexive) | 68 | 2.5, 3.1, 3.6, 3.7, 4.14, AI-sweep; flags-only house rule |

## Sections and subsections

| section | its opening's point sentence, quoted | themes named | order | does the heading carry a theme? |
|---|---|---|---|---|
| Abstract | "These changes accumulate experience, but their persistence alone does not establish that the system is improving." (S2; the findings follow in S6–S9) | change outside the weights; persistence vs improvement; local vs promotion loop; feedback | logical (context → turn → method → findings → contributions) | n/a |
| I. Introduction | "The systems surveyed have developed these loops unevenly." (I_II:5 S1, the nearest single point sentence; the problem is "The ease of making a change also makes it easy to accumulate changes whose value is unknown." I_II:3 S1) | scaffold; changes of unknown value; local loop; promotion loop; uneven development; feedback | logical (vignette → context → problem → questions → three findings → roadmap) | no ("Introduction", label mandated by venue) |
| II. From a local fix to a measured improvement | "Repeating this process turns a growing collection of fixes into a procedure for improving the deployment." (I_II:9 S5) | measured improvement; keep or reverse; procedure | logical (local loop → sharing → formal conditions → who decides → limits) | yes (fix → measured improvement) |
| II.A The local loop | "The procedure starts with a record of failures: rejected answers, user corrections, failed tool calls, evaluation regressions, or unsuccessful tasks." (I_II:10 S1) | failure record; credit assignment; coordinate; gate; patch loss | chronological (steps of the loop in order) | no (label) |
| II.B The second decision: whether to share the fix | "That decision changes the population on which the rule will act." (I_II:13 S3) | sharing; population; receiving-side evaluation; evidence radius | logical (example → consequence → definitions) | yes |
| II.C Five conditions for artifact-layer optimization | "We use **artifact-layer descent** for the form of maintenance that connects recurring failures to measured improvements through five conditions:" (I_II:15) | artifact-layer descent; five conditions; patchwork vs random search; patch loss; gate rule; gate stability | coordinate (five conditions) then logical (taxonomy → formalization → formal result) | partly (names the five conditions, but says "optimization" where the defined term is "descent") |
| II.D Who proposes and who decides | "We classify the gate by who makes the acceptance decision:" (I_II:24 S3) | proposer vs decider; Auto / Human / None; gate pairs; two limits | coordinate (three gate classes) then logical (limits) | yes |

## Group B (III, IV): S4 diagnostic ledger

# S4 diagnostic ledger B: III_method.md, IV_local_findings.md

Scope: Section III "Corpus and method" (15 prose paragraphs) and Section IV "What local adaptation actually closes" (21 prose paragraphs). Sentences are numbered S1, S2, ... within each paragraph. Tables, the LaTeX figure block and headings are not paragraphs; their caption problems appear in the flags-only table. There are no display equations in these files. No paragraph qualifies for the aside exemption: III:8 (37 words), III:11 (~47) and IV:16 (44) are short, but each carries a definition or a finding that the argument needs. House-style checks: no em-dashes in either file; the spelling is American throughout.

## (a) Mandatory ledger

### III_method

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| III_method:1 | point (section opening) | pass (circled: artifact, feedback, decision, scope) | pass | pass | pass | pass (close call: S1 lands the four-part frame but ends on the weak passive "the result is used") | FLAG: S1 "it" names two things, the system in "the persistent artifact it changes" and the change in "the decision that accepts it"; S2 bare "This allows" (the reading procedure) | pass | FLAG: S2 subject is the bare demonstrative "This" plus the capability verb "allows" | pass | pass (S1, 37 words, point first, list after the colon) | FLAG: S1 ends "in which the result is used" (stress on a weak passive verb, not on "scope") | pass | pass | pass | FLAG: capability voice, S2 "This allows systems ... to be compared by their behavior" |
| III_method:2 | body (method) | pass | FLAG: S3 "Sources include research papers, public repositories, product documentation, and supported production reports" is restated in III:13 S1 "The evidence ranges from peer-reviewed studies and open-source artifacts to vendor claims" | pass (close call: corpus → search pass → sources, a related set) | pass (close call: S2 "The first search pass" is new, but a corpus implies a search) | FLAG: S1 ends on scene-setting, "the October 2026 cutoff"; the paragraph is about how the corpus was assembled (two passes, sources, recorded rules) | pass | pass | pass | pass | pass (note: S3's semicolon joins two different claims; see 4.12) | FLAG: S3's stress falls on housekeeping, "are recorded with the released data (Supplementary Material S2)" | FLAG: S3 "supported production reports": "supported" adds a word whose meaning is unclear (supported by what?) | pass | pass | pass |
| III_method:3 | body (inclusion rule) | pass | pass | pass (note: S2 hops to the gerund subject "Including the latter group") | pass | pass | pass | pass | FLAG: S2 gerund subject "Including the latter group provides"; S3 subject "Systems whose only update mechanism is weight-level training" (9 words, relative clause) before "are excluded" | FLAG: S2 empty verb + noun, "provides a contrast set" | FLAG: S3's long subject with an embedded relative clause delays the verb | pass | pass | pass | pass | pass |
| III_method:4 | body (first filter) | pass | pass (note: S4 "the 256 systems occupy 269 scored rows" recurs in the Fig. corpus caption, acceptable for a caption) | pass | FLAG: S4 opens on a new topic, "A system may have one integrated row or several substrate-specific rows"; rows have nothing to do with the filters this paragraph introduces | pass | pass (note: S2 "the rubric below" is announced as forward, not presented as old) | pass | pass | pass | pass | FLAG: S2 ends on a pointer, "under the rubric below" | pass | pass | pass | pass |
| III_method:5 | body (second filter) | pass | pass | pass | pass | pass | FLAG: S3 "the eight systems without an audit" is presented as known, but nothing earlier states eight (204 − 202 = 2) [AUTHOR FLAG 1] | pass | FLAG: S3 opens with a ~25-word participial phrase, "Applied to 202 of the 204 core systems and to 4 research systems classified from their papers alone (SkillOpt, FederatedSkill, SkillClaw, and ChronoMem)," before the subject "it" | pass | FLAG: S3 (~50 words) has a long fronted modifier, then a semicolon tacks on an unrelated clause about the unaudited systems | pass (note: S3 ends on "(Supplementary Material S4)") | pass (note: S2 "subsequently" can be inferred from "promoted beyond") | pass | pass | pass (note: semicolon chain in S3) |
| III_method:6 | evidence (list of passers) | pass | FLAG: S3 "SkillOpt is classified from its paper" repeats III:5 S3 "4 research systems classified from their papers alone (SkillOpt, ...)" | pass | pass | pass (close call: S1's stress is an 11-name list; the theme "passing the audit" sits in the subject) | pass | pass | pass | pass | FLAG: S4 gapped coordination, "and the audit's boundary cases [are identified] in the contrast set", forces a re-parse | pass | pass | pass | pass | pass |
| III_method:7 | point (qualification) | pass | FLAG: S3 "Letta passes on the lineage of its shared-memory updates even though those updates have no acceptance gate" is restated in III:15 S2 "Letta alone passes with an ungated promotion" | pass | pass | pass | FLAG: S4 "reported separately" points to no stated location | pass | pass (note: S1 gerund subject "Passing this audit") | FLAG: S4 nominalization subject + passive, "their treatment under relaxed audit rules is reported" | pass | FLAG: S4 ends "reported separately" | pass | pass | pass | pass |
| III_method:8 | context (definition) | pass | pass (note: deliberately repeats the Introduction's scaffold list as a definition) | pass | pass | pass | pass | n/a: no events | pass | pass | pass | FLAG: S3's stressed content is an attribution, "follow Sumers et al. [@sumers2023coala]" | pass | pass | pass | pass |
| III_method:9 | body (scale definition) | pass | pass | pass (note: S5's subject switches to "a program"; old→new justifies it) | pass | pass | pass | pass | pass | pass | pass | FLAG: S6 ends on an attribution, "as specified in the table" | pass | pass | pass | pass (note: the "At 0 ... At 4" run is intentional parallel scaffolding) |
| III_method:10 | explanation | FLAG: S1's circled words, "important ... interpreting the scores", name no theme; the theme (a score of 5 certifies different things on different substrates) arrives in S6 | FLAG: S2–S3 restate Table V-1's score-5 column (S3 nearly repeats the S5 row "Topology updated from deployment feedback by a loop outside the agent's own run"); S5 restates Table V-2's integrated row "Breadth and depth of adaptation, not the loop" | FLAG: the subjects tour the substrates ("Instructions and skills" → "Orchestration" → "Memory, tools, and governance" → "Integrated rows" → "The scale"); the paragraph's character, the score of 5, is a subject only in S6 | pass | FLAG: S1 ends on "when interpreting the scores" | FLAG: S1 "This last distinction"; III:9 S6 states a dependence ("depends on the substrate"), not a distinction | pass | FLAG: S1 abstract subject + "is important" | FLAG: S5 "closure of either loop"; S6 "a universal certificate of complete optimization" | pass | FLAG: S1 ends "interpreting the scores" | FLAG: S1 "is important" (empty); S6 "universal ... complete" (doubled intensifiers) | pass | pass | FLAG: "This last distinction is important" (an importance announcement, cap 0); two antitheses in one paragraph (S5 "not closure of either loop"; S6 "is not a universal certificate") |
| III_method:11 | evidence (table summary) | FLAG: S1's circled words, "the corpus distribution", announce the table, not the finding | pass (note: prose states Table V-2's score-5 column as a relationship, which is acceptable) | pass | pass | FLAG: S1 ends on "the corpus distribution"; the themes (research systems top skills and memory, production tops governance, no system tops instructions, tools or orchestration) arrive in S2–S3 | pass | n/a: no events | FLAG: S1 metadiscourse subject, "Table REF(tab:V-2) gives" | pass | pass | pass | pass | pass | pass | FLAG: topic-announcement opener |
| III_method:12 | housekeeping (scope note) | pass (note: a line can be drawn at "explicit columns of the released table") | FLAG: S2 "96 of their 105 core systems have a local loop, and 89 of those close it under a program" repeats the Table V-2 caption and IV:3 S1 (and Introduction ¶5); S3 "This is not a gate count over all 256 systems" restates S1 "counts based on those columns apply to those systems" | FLAG: subjects run "gate types, feedback classes, and governance properties" → "counts" → "96 of their 105" → "This"; the character (the 126-system subset) is never a subject | pass | FLAG: S1 ends "apply to those systems" | FLAG: S3 bare "This" could be S2's example count or S1's scope rule | pass | FLAG: S1's verb "are recorded" arrives at about word 16, after a 7-word fronted phrase and a 9-word list subject | pass | pass (close call: S1 is a 33-word passive) | FLAG: S1 ends on "those systems", repeating "systems" from the same sentence | pass | pass | pass | pass |
| III_method:13 | body (evidence weighting) | pass (close call: S1 names the range of evidence, not the weighting rule the paragraph is about) | FLAG: S1 restates III:2 S3's list of sources | pass (note: S2 hops to "Every row of the released table") | FLAG: S2 "Every row of the released table carries its source" breaks the weighting thread; S3 "Peer-reviewed papers" picks up S1, not S2 | pass | pass | pass | pass | pass | pass | FLAG: S4 ends on a pronoun, "corroborates it"; S5 ends on "identified as such" | pass | pass | pass | pass |
| III_method:14 | other view (limitation) | pass | pass | pass (close call: author → cases/half-scores → re-rating → classifications, in four short sentences) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S4 "an auditable interpretation of public evidence, not a complete inventory" is the section's third not-X antithesis (after III:10 S5 and S6) |
| III_method:15 | evidence (sensitivity) | pass | FLAG: S2 "Letta alone passes with an ungated promotion" restates III:7 S3 | pass | pass | pass | FLAG: S2 presents "Membership" (of what? the passing set) and "the human-local cells" (no grid of cells is introduced in this section or in Section II) as known | pass | pass | pass | pass (close call: S2 runs ~45 words, but its main clause is short and early) | pass (note: S3 ends on a cross-reference) | FLAG: S3 "the full score table with the released table" is circular; S2 "principal structural findings" (two stacked adjectives) | pass | pass | pass |

### IV_local_findings

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IV_local_findings:1 | point + illustration (section opening) | pass | pass | FLAG: subjects hop "A system" → "SkillForge" → "Its judge" → "Those replies"/"the updated skill" → "The calibration" → "It"; the protagonist leaves subject position after S2 | FLAG: S2 opens on the new name, "SkillForge illustrates this distinction" | pass | pass (note: S5 "The calibration" relies on Section II's "calibrated against people"; S2 "this distinction" names a contrast S1 only implies) | pass | FLAG: S5 abstract subject, "The calibration concerns" | FLAG: S6 of-chain "the effect of the resulting skill changes"; S4 "drive updates to the skill" | pass | pass (note: S2 ends on the pointer "this distinction") | pass (note: S1 "ever") | pass | pass | pass |
| IV_local_findings:2 | illustration + method rationale | FLAG: S1's circled words, "the same separation through a different mechanism", name no mechanism; the theme (unconditional acceptance) arrives in S2 | FLAG: S4 "the survey records who accepts an edit separately from who generates it" restates Section II ("The author of an edit and the authority that accepts it are separate ... We classify the gate by who makes the acceptance decision"); S3 restates S2 and IV:1 S4 | FLAG: "SkillRL" → "A success-rate threshold"/"the skill bank" → "Both systems" → "This" | FLAG: S2 opens on the new "A success-rate threshold" | FLAG: S1 ends on "a different mechanism" | pass (note: S1 "the same separation" = IV:1 "this distinction", a synonym drift, see 2.3; S4 bare "This is why") | pass | pass | FLAG: S2 "triggers proposals for new skills" hides who proposes | pass | FLAG: S3 ends on the cross-reference "defined in Section REF(sec:loop)"; S4 ends on the pronoun "triggers it" | pass | pass | pass | FLAG: vague opener "exposes the same separation through a different mechanism"; S4 is method-justification metadiscourse |
| IV_local_findings:3 | point (section finding) | pass | pass (note: the section's deliberate anchor for the 96/89 counts; the duplicate to cut is III:12 S2) | FLAG: "96"/"automatic acceptance" → "Looking inside those loops" → "Evaluation"/"the failure record and the link" | pass | pass (close call: S1 ends "retain or reject changes"; the section's themes, failure record and attribution, arrive as the point in S3) | pass | pass | FLAG: S1 fronts 12 words, "Among the 105 core systems most recently added to the corpus,", before the subject "96"; S2 gerund subject "Looking inside those loops reveals" | pass | FLAG: S1 (35 words) puts its point ("automatic acceptance is ... the dominant pattern") in the second coordinate clause, after the count | FLAG: S2 ends on the vague "a less even picture" | FLAG: S1 "nevertheless" (no contrast with the preceding clause); "Among ... among them" repeats | pass | pass | FLAG: S2 cliché "reveals a less even picture" |
| IV_local_findings:4 | body (failure log) | pass | pass | pass (close call: failure history → production memory → field report → persistent store, a related set) | pass | pass | pass (note: S4 "The persistent store" = S2 "Production memory") | pass | pass | pass | pass | pass | FLAG: S2 "more often" has no comparator (more often than failures?); S4 "particular" is a tic word | pass | pass | pass |
| IV_local_findings:5 | body (prioritization) | pass | FLAG: S1 "nearly every system uses them in arrival order", S2 "Few explicitly choose which recurring modes deserve attention" and S5 "this remains uncommon in the surveyed implementations" state one proposition three times | pass (note: S3's subject shifts to mechanisms) | FLAG: S3 opens on the new names "Task-CoEvolve's variance-weighted task sampling and AutoSaddler's mini-batch failure signals" and ends on the old frame "are exceptions" | pass | FLAG: S4 "They ... rather than letting the most recent session determine it": "they" = the two mechanisms or the two systems; "it" = "the experience" or "the next update" | pass | FLAG: S3 has a 10-word subject before "are" | pass | pass | FLAG: S4 ends on the pronoun "determine it" | pass (note: S5 "described earlier" can be inferred) | FLAG: S1 "nearly every system" is a corpus-wide quantifier with no count or pointer to the data [AUTHOR FLAG 9] | pass | pass |
| IV_local_findings:6 | body (attribution) | FLAG: S1 "The next step is harder." leaves nothing to circle; the theme (credit assignment) is never named in the paragraph | pass | FLAG: "The next step" → "A failed output" → "Harness-optimization papers" → "An evaluation of harness optimizers"; the character (credit assignment) is never a subject | FLAG: S3 and S4 open on new sources, "Harness-optimization papers" and "An evaluation of harness optimizers" | FLAG: S1 ends "harder" | pass ("The next step" resolves to Section II's sequence) | pass | pass | pass | pass | pass | pass | pass | pass | pass (note: S1 is a deliberate terse beat, which the house style allows, but it carries no theme word) |
| IV_local_findings:7 | body (partial solutions) | pass | pass (note: S6 restates S1 as a frame-close) | pass (a coordinate list of methods) | pass | pass | pass | pass | pass | FLAG: S5 "give the proposal process more useful evidence" (empty verb; the actor is a nominalization) | pass | pass | pass | pass | pass | pass |
| IV_local_findings:8 | body (candidate generation) | pass (close call) | pass | FLAG: "Research systems" → "an engineer"/"session feedback"/"public skill repositories" → "A field study"/"every substantive edit" → "the evaluation machinery"/"the improvement process" | pass | FLAG: S1 ends "reflecting on trajectories" (the research mechanism); the paragraph's point (proposal that waits on people keeps improvement intermittent) arrives only in S4 | pass | pass | FLAG: S4 fronts an 11-word clause, "Where proposal generation depends on a person noticing a problem,", before the subject | FLAG: S4 "proposal generation", "the improvement process itself" | FLAG: S2 packs three clauses about two populations (prompt platforms; public skill repositories) joined by "and ... while" | pass | FLAG: S4 "itself" (intensifier), "machinery" (vague) | pass | pass | pass |
| IV_local_findings:9 | evidence (skills by gate) | pass | FLAG: S3 "SkillRL and SkillForge, described above, leave the proposed changes unchecked" repeats IV:1–IV:2; S4 repeats IV:2 S4's rationale; S2 (SkillChain's human reflection decision) is repeated in IV:12 S2 | pass (close call: a coordinate tour, SAGE/COSPLAY → SkillChain → SkillRL/SkillForge) | pass | FLAG: S1 ends on "inside a research environment"; the theme (skill systems differ in where acceptance sits) appears only in S4 | FLAG: S4 "all three"; S1–S3 name five systems (or three groups), so the count does not resolve | pass | FLAG: S4 "These differences would be obscured by classifying" (abstract subject, agentless passive) | FLAG: S2 "adds a human reflection decision after the judge" (a person decides) | FLAG: S2's tacked-on relative "after the judge, on which refined skills are deployed": "which" can attach to "judge" or to "decision" | pass | FLAG: S4 "simply" | pass | pass | pass |
| IV_local_findings:10 | evidence (orchestration) | FLAG: S1 "a similar progression" leaves nothing to circle; no progression was described for skills | pass (note: S5 restates Table V-2's orchestration row) | pass | pass | FLAG: S1 ends "a similar progression" | FLAG: S1 "similar" to what? IV:9 compares skill systems; it narrates no progression | pass (chronological) | pass | pass | pass (S4, 33 words, point first) | pass | pass | pass | pass | pass |
| IV_local_findings:11 | evidence (instruction files) | FLAG: S1's circled words, "a useful counterpoint", name neither the artifact nor what it contrasts with | pass (note: S3's frame and S7's close restate one claim deliberately) | pass (note: two halves, instruction files then studies) | pass | FLAG: S1 ends on "a useful counterpoint"; "instruction files" first appears in S2 | FLAG: S1 presents "The most widely deployed artifact" as known before S2 names it; what it counters is unstated | pass | pass | pass | FLAG: S5 (~42 words) stacks two measured results, the absolute phrase "with total tokens approximately unchanged", and a semicolon clause | pass | FLAG: S1 "useful" | pass | pass | pass |
| IV_local_findings:12 | body (human gates) | pass | FLAG: S2 "in SkillChain a person decides, at a reflection gate, which refined skills are deployed" repeats IV:9 S2 | pass (close call) | pass | pass | FLAG: S4 "which belongs to promotion": "which" = "release or admission", or the checks | pass | FLAG: S3 has a 10-word subject, "Prompt platforms and registries without a failure-driven proposal process", before "have" | pass | pass (note: S2's interruption "at a reflection gate") | FLAG: S3 ends on the metadiscourse "in this classification" | pass | pass | pass | pass |
| IV_local_findings:13 | body (noisy gates) | pass | FLAG: S5's AutoSaddler "mini-batch failure signals" already appear in IV:5 S3, in a different role (prioritization) | pass | pass | pass | pass (note: S2 bare "this") | pass | pass | pass | pass (note: S3's appositive interruption is needed to separate SAGE-gate from SAGE) | pass | FLAG: S2 "directly" | pass | pass | pass |
| IV_local_findings:14 | explanation | FLAG: S1 "These mechanisms should not be conflated": the only word to circle is "conflated"; the two mechanisms (averaging, agreement) go unnamed | pass | FLAG: "These mechanisms" → "Averaging" → "Requiring agreement" → "The independence assumptions"/"actual critics" → "Appendix" → "The shared development" | FLAG: S6 opens on a new frame, "The shared development", after S5's appendix pointer | FLAG: S1 ends "conflated" | FLAG: S1 "These mechanisms" = the three IV:13 systems, but S2–S3 discuss two operations (averaging, agreement) without saying which system does which; in S3 "the idealized probability $p^k$" leaves the event (all k checks falsely accept) implicit | pass | FLAG: S3's verb "gives" arrives at about word 11, after a gerund subject and the interruption "each with false-acceptance probability $p$" | FLAG: S6 "The shared development is that acceptance increasingly depends on" (nominalization subject + is-that) | FLAG: S3's interruption sits between subject and verb | pass (note: S5 ends on the weak "their roles") | pass | pass (note: S6 "increasingly" extrapolates a trend from three systems; the hedge is acceptable) | pass | FLAG: S6 "rather than one favorable observation" is the fourth "rather than" antithesis in Section IV (IV:5 S4, IV:10 S4, IV:14 S6, IV:20 S3) |
| IV_local_findings:15 | body (removal) | pass | pass | pass (close call) | pass (note: S3 opens on the new name "Ratchet") | pass | pass | pass | FLAG: S1 nominalization subject, "The evaluation of a new edit also depends" | FLAG: S1 of-chain "The evaluation of a new edit"; S3 agentless "until lifecycle hygiene is applied" | pass | pass (note: S4 ends on four citations plus "(Supplementary Material S6)") | pass | pass | pass (note: stacked parentheticals) | pass |
| IV_local_findings:16 | body (memory history) | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S1 "have made substantial progress on" (empty verb + nominalization) | pass | pass | FLAG: S1 "substantial" | FLAG: S1 "substantial progress" is an intensifier with no measure | pass | FLAG: intensifier inflation, "substantial progress" |
| IV_local_findings:17 | body (correction) | pass | pass (note: S5 restates Table V-2's memory row) | FLAG: "History" → "A study"/"all five" → "The record"/"retrieval" → "Research systems" → "Cuadros et al.'s governed collaborative memory"; the paragraph moves from a production failure (S1–S3) to a research taxonomy (S4–S5) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| IV_local_findings:18 | body (reversal) | pass | pass | pass (note: systems → VaG → consequences, a related set) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass (S4 "may therefore" hedges an extrapolation from one result: just right) | pass | FLAG: S2 capability verb, "support edit-level rollback" (the house style asks for mechanism over capability) |
| IV_local_findings:19 | illustration (worked case) | pass | pass | pass (note: an intentional walk through the five conditions) | pass | pass | pass | FLAG: S2–S5 walk the conditions as state → failure log → attribution → proposal → loss + gate, while Section II numbers the loss first; the reader must re-sort S2–S5 to map them onto conditions 1–5 | pass | FLAG: S1 "provides a concrete instance of" | pass | pass | pass | pass | pass | pass |
| IV_local_findings:20 | evidence (results + ablation) | pass | FLAG: S2 (SkillOpt-Lite keeps the consensus filter) restates IV:7 S4 "its ablation finds this consensus mechanism load-bearing" | pass | pass | FLAG: S1's stress falls on the attribution "reported by its authors" | pass | pass | FLAG: S1 fronts 11 words, "Across six benchmarks, seven target models, and three harnesses,", before the subject | FLAG: S3 "supports the importance of the gate" | FLAG: S3's trailing participle "while identifying the removed controls as stabilizers" (its implied doer is "This comparison"); S2 also trails "while retaining" | FLAG: S1 ends "by its authors" | pass | pass | pass | FLAG: S3 "rather than necessities" repeats the antithesis pattern (see IV:14) |
| IV_local_findings:21 | point (section close) | pass | pass | pass | pass | FLAG: S1 ends on the list "models, harnesses, and benchmarks"; the point (transfer is not acceptance) lands in S3 | FLAG: S3 presents "the shared skill bank" as known, but IV:19 S2 calls SkillOpt's state "one markdown skill document" [AUTHOR FLAG 8] | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S4 is a section-ending bridge sentence, "This distinction becomes central once the same local procedure is used in settings where correctness is harder to measure" (house-style rules 7 and 10) |

FLAG cell count: III_method 51; IV_local_findings 86; total 137.

## (b) Flags only (other paragraph-level tests)

| ¶ | test | finding (quote the words) |
|---|---|---|
| III_method:1 | 4.2 / 4.5 | S2 "to be compared": the passive hides the comparer (we). |
| III_method:2 | 4.12 | S3's semicolon joins two claims: what the sources are, and "the search families, evidence tiers, and inclusion rules are recorded with the released data". |
| III_method:2 | 4.15 | "search families" and "evidence tiers" are used before they are defined (tiers are explained only in III:13); "supported production reports" is unclear. |
| III_method:3 | 2.3 | "contrast set" (III:3 S2, III:5 S3, III:6 S4) vs "contrast corpus" (III:4 S3): two names, and possibly two definitions [AUTHOR FLAG 2]. |
| III_method:3 | 4.8 | S3's whole subject, "Systems whose only update mechanism is weight-level training", runs 9 words and holds a relative clause. |
| III_method:4 | 4.15 | "scaffold substrate" (S2) and "integrated row" (S4) are used before III:8–III:10 define them. |
| III_method:4 | 1.5 (sentence placement) | S4 (rows and the 269 count) belongs with "Substrates and scoring", not with the filters. |
| III_method:5 | 4.13 | S2 "beyond the deployment that produced it, with versioning or lineage": the phrase can attach to "promoted" or to "deployment". |
| III_method:5 | 4.15 | "industry exemplars" is a new term; III:13 S5 later calls them "vendor-based exemplars". |
| III_method:6 | 4.12 | S4's gapped coordination, "and the audit's boundary cases in the contrast set", is not parallel. |
| III_method:7 | 4.12 | S2 "within one operator, into a shared bank or archive that later runs draw from, or across the agents and sessions of one deployment": the three items are not parallel (the middle one carries a relative clause). |
| III_method:7 | 4.15 | "operator" is unglossed. |
| III_method:8 | 4.12 | S3's semicolon joins unrelated clauses (a table pointer; the source of the memory taxonomy). |
| Table V-1 caption | 4.15 | "what a system must do on it to score 5" appears before the 0–5 scale is introduced in III:9. |
| Table V-1 S5 row vs III_method:10 S3 | 2.3 | "outside the agent's own run" vs "outside the agent's own execution". |
| Table V-1 / V-2 captions | label | Literal "Table V-1." and "Table V-2." captions sit in Section III [AUTHOR FLAG 11]. |
| III_method:9 | 4.15 | "common scoring scale" ("common" = shared across substrates?); "persists with tool attachment" is unexplained; "spans scopes" assumes the scopes are defined. |
| III_method:10 | 2.2 | The point (S6 "The scale therefore supports substrate-specific comparisons") arrives last. |
| III_method:10 | 2.4 | The framing sentence comes last, as a summary, with no earlier frame. |
| III_method:10 | 5.2 | S1 "This last distinction is important when interpreting the scores" is metadiscourse about how to read. |
| III_method:11 | 5.2 | S1 "Table REF(tab:V-2) gives the corpus distribution" is a topic announcement. |
| Table V-2 caption | 2.5 | The caption (~75 words) repeats "96 of those core systems have a local loop and 89 close it under a program", also in III:12 S2 and IV:3 S1, and carries a finding found nowhere in the prose ("none of the 126 scores 5 on any substrate") [AUTHOR FLAG 4]. |
| III_method:12 | 1.5 | This scope note duplicates the Table V-2 caption, and it qualifies counts that are used only in Section IV. |
| III_method:13 | 4.6 | The writer's own methodological decisions sit in agentless passives: "receive the greatest weight", "is counted only when", "are not pooled", "are identified as such". |
| III_method:13 | 2.3 | "industry exemplars" (III:5–6) vs "vendor-based exemplars" (S5); "production claim" (S4) vs "vendor claims" (S1). |
| III_method:15 | 4.15 | "human-local cells" and "loops that persist only optimizer state" are unglossed; "[Auto × Auto]" relies on Section II. |
| III_method:15 | 4.12 | S3's gapped coordination, "and the full score table with the released table", is circular [AUTHOR FLAG 13]. |
| III (section) | 1.8 | The headings are labels ("Corpus and method", "Scope and selection", "Substrates and scoring", "Evidence and limitations"). |
| III (section) | 4.16 | pass: sentence lengths vary from about 5 to 50 words. |
| IV_local_findings:1 | 4.2 | S4 "the updated skill is committed": who commits (the system) is hidden. |
| IV_local_findings:2 | 2.3 | "distinction" (IV:1 S2) → "separation" (IV:2 S1) for one concept. |
| IV_local_findings:2 | 5.2 | S4 "This is why the survey records ..." is method metadiscourse. |
| IV_local_findings:3 | 3.4 | S1 has 12 words before the subject. |
| IV_local_findings:3 | 3.5 | S1 "nevertheless" claims a contrast that does not exist (a bluff). |
| IV_local_findings:4 | 6.4 | S2 "Production memory more often records preferences, successes, or conversation history" is an uncited corpus-level claim [AUTHOR FLAG 10]. |
| IV_local_findings:5 | 4.8 | S3's subject runs 10 words. |
| IV_local_findings:5 | 6.3 / 6.4 | S1 "nearly every system uses them in arrival order" has no count or source [AUTHOR FLAG 9]. |
| IV_local_findings:6 | 2.3 | Section II's term "credit assignment" (condition 3) appears in IV only as "this attribution problem" (IV:6 S3), "the general attribution problem" (IV:7 S6), "attribute recurring errors" (IV:19 S4) and once as "this form of credit assignment" (IV:20 S3); the reader must re-map it. |
| IV_local_findings:6 | 3.5 | S4 "reaches the same conclusion": the cited claim (by downstream score alone a harness optimizer "cannot be told from trial and error") is related to, but not the same as, "attribution ... is the bottleneck" [AUTHOR FLAG 7]. |
| IV_local_findings:7 | 5.6 | S3's verb "attributes outcomes" vs S4's noun "the attributes that recur" (a word clash). |
| IV_local_findings:7 | 1.6 (note) | S2's Meta-Harness example shows record-keeping ("the record of which edits helped") more than attribution to a substrate coordinate; it weakly illustrates the paragraph's claim. |
| IV_local_findings:8 | 3.5 | S2 "while": no real contrast; both populations depend on people. |
| IV_local_findings:8 | 4.15 | "AI co-author trailer" (a git commit trailer) is unglossed for non-developer readers. |
| IV_local_findings:8 | 1.5 (subsection) | The paragraph is about generating candidates but sits under the heading "Testing the candidate". |
| IV_local_findings:9 | 4.5 | S4's passive, "would be obscured by classifying", hides who classifies. |
| IV_local_findings:9 | 4.7 | "human reflection decision" is an invented noun string. |
| IV_local_findings:10 | 4.15 | "structural invariant" is unglossed. |
| IV_local_findings:11 | 4.12 | S2's list mixes products ("Claude Code, Cursor, ... Windsurf, and Continue.dev") with a file convention ("AGENTS.md"). |
| IV_local_findings:11 | 4.15 | "root AGENTS.md", "paired runs" and "wall-clock" are unglossed for non-developer readers (minor). |
| IV_local_findings:12 | 4.8 | S3's subject runs 10 words. |
| IV_local_findings:12 | consistency | S3 "Prompt platforms and registries ... have no local gate in this classification" vs III:15 S2 "the human-local cells hold only curation and registries" [AUTHOR FLAG 3]. |
| IV_local_findings:13 | 4.15 | "three heterogeneous critics" is unglossed. |
| IV_local_findings:14 | 2.4 / house "one claim per paragraph" | S1–S5 distinguish averaging from agreement; S6 asserts a shared trend ("acceptance increasingly depends on a body of evidence"): two claims. |
| IV_local_findings:14 | 4.2 | S3 "gives the idealized probability $p^k$": the event (all k checks falsely accept) is missing. |
| IV_local_findings:14 | 6.3 | S2 "reduces the variance of their mean by a factor of $1/k$" [AUTHOR FLAG 5]. |
| IV_local_findings:15 | 4.15 | "lifecycle hygiene" is unglossed. |
| IV_local_findings:17 | 3.5 | S4 "likewise": research systems dividing between two designs is not like production backends returning revoked facts (a bluff). |
| IV_local_findings:17 | 2.4 / house "one claim per paragraph" | S1–S3 cover a production failure (history is not correction); S4–S5 cover a research taxonomy and the top memory score. |
| IV_local_findings:19 | 5.3b | Signposts are missing that map S2–S5 onto the numbered conditions 1–5. |
| IV_local_findings:20 | 4.13 | S3 "while identifying the removed controls": the implied doer is "This comparison" (a loose dangler). |
| IV_local_findings:21 | house style rules 7 and 10 | S4 is a bridge to the next section; the section should end on its own conclusion (S3). |
| IV (section) | house style formatting | Five subsections; the house cap is 4 per top-level section. |
| IV (section) | 1.8 | "What local adaptation actually closes" ("actually" is a tic; the heading names no finding). "Testing the candidate" covers proposal (¶8), per-substrate gating (¶9–10), instruction-file effectiveness (¶11) and human gates (¶12). |
| IV (section) | AI caps | Four "rather than" antitheses (IV:5 S4, IV:10 S4, IV:14 S6, IV:20 S3) plus three "does not / not X" correctives (IV:1 S6, IV:11 S3, IV:17 S1); the cap is about 1 per section. |
| IV (section) | 4.16 | pass: sentence lengths vary from 4 ("Reversal has its own limits.") to about 42 words. |

## (c) Suggested moves (one per FLAG)

III_method
- III:1 3.7: Use "it" for one referent only (name "the change" in the third item); replace the bare "This" with a noun.
- III:1 4.1: Make "we" the subject: "so we can compare systems ... by what they do".
- III:1 4.14: End S1 on "scope", e.g. "... and how far the result travels (its scope)".
- III:1 AI: Replace "allows ... to be compared" with an active verb that has a named doer.
- III:2 2.5: Keep the list of source types in one place (here or III:13) and point to it from the other.
- III:2 3.6: End S1 on what the paragraph develops (how the corpus was assembled); move the dates to the front.
- III:2 4.14: Split S3; end the second sentence on the content (inclusion rules) and move the supplement pointer forward or into a parenthesis mid-sentence.
- III:2 5.1: Clarify or drop "supported" (author decides; see AUTHOR FLAG 14).
- III:3 4.1: Open S2 with "These self-described systems form a contrast set"; open S3 with "We exclude ...".
- III:3 4.3: Replace "provides a contrast set" with a verb.
- III:3 4.9–4.11: Use "We exclude systems that update only their weights ..." to shorten the subject.
- III:4 3.2: Move S4 (rows) to III:8–III:9, or open it on old information ("These 256 systems occupy 269 rows because ...").
- III:4 4.14: End S2 on the threshold; move "under the rubric below" to the front ("Under the rubric in III-B, ...").
- III:5 3.7: State where the unaudited systems come from before calling them "the eight" (AUTHOR FLAG 1).
- III:5 4.1: Make "The audit" the subject at the start of S3, and move the list of applied-to systems after the verb.
- III:5 4.9–4.11: Split S3 at the semicolon; give the unaudited systems their own sentence.
- III:6 2.5: Cut S3's restatement or merge it into III:5's mention of SkillOpt.
- III:6 4.9–4.11: Restore the verb in the second half of S4, or split it into two sentences.
- III:7 2.5: Keep the Letta point in one place (here) and refer to it in III:15.
- III:7 3.7: Name where the relaxed-rule treatment appears (needs a cross-reference: AUTHOR FLAG 12).
- III:7 4.3: Rewrite S4 with "we" as subject: "we report how relaxed rules treat them in ...".
- III:7 4.14: End S4 on its content, not on "separately".
- III:8 4.14: Split S3; end the memory clause on the categories, with the attribution up front ("Following Sumers et al., memory is ...").
- III:9 4.14: Trim "as specified in the table", or move the pointer forward ("Table V-1 gives the score-5 requirement for each substrate").
- III:10 2.1: Re-draft with a point-first opening that names the theme (what a 5 certifies differs by substrate).
- III:10 2.5: Cut the restatements of the table rows; keep only the interpretive consequence.
- III:10 3.1: Make "a score of 5" (or "the scale") the running subject.
- III:10 3.6: End the opening sentence on the theme words.
- III:10 3.7: Replace "This last distinction" with an explicit noun phrase, or delete it with the re-draft.
- III:10 4.1: Drop "is important"; open on the substantive claim.
- III:10 4.3: Use verbs: "whether either loop closes"; "does not certify that the system is fully optimized".
- III:10 4.14: Covered by the opening re-draft.
- III:10 5.1: Cut "important"; keep at most one of "universal"/"complete".
- III:10 AI: Keep one antithesis at most; state the other plainly.
- III:11 2.1: Open on the finding, with the table pointer in parentheses.
- III:11 3.6: End S1 on the themes (which corpus segments hold the top marks).
- III:11 4.1: Make the systems the subject; demote "Table REF(tab:V-2)" to a parenthesis.
- III:11 AI: Remove the announcement frame.
- III:12 2.5: Cut S2's example counts (they live in the caption and IV:3) and S3's restatement; keep one sentence of scope.
- III:12 3.1: Make "the 126 most recently added systems" (or "these counts") the subject.
- III:12 3.6: End the opening on the scope limit ("... cover only these 126 systems").
- III:12 3.7: Replace the bare "This" with a noun, or drop S3.
- III:12 4.1: Open on a short subject ("We record ...") and move the list after the verb.
- III:12 4.14: Avoid ending on "those systems"; end on "126 systems" or on the scope word.
- III:13 2.5: Keep the source list in one place; III:13 should state only the weighting.
- III:13 3.2: Move S2 (per-row documentation) after S5, or to III:2, so that S1 → S3 → S4 → S5 flows.
- III:13 4.14: End S4 on "stronger evidence"; end S5 on "vendor-based".
- III:14 AI: Drop the "not X" frame or keep it only if it is the section's single antithesis.
- III:15 2.5: Refer back to III:7 for Letta rather than restating it, or keep it as a one-word item in the list.
- III:15 3.7: Name the set ("Which systems pass changes ...") and gloss "human-local cells" (or point to the gate grid).
- III:15 5.1: Fix the circular "full score table with the released table" (AUTHOR FLAG 13); trim "principal structural".

IV_local_findings
- IV:1 3.1: Keep SkillForge (or "the system") as the subject across S3–S6.
- IV:1 3.2: Put old information first: "This distinction shows in SkillForge."
- IV:1 4.1: Make SkillForge's judge the subject: "Its judge's agreement with people says which replies ...".
- IV:1 4.3: Use verbs: "how the resulting skill edits change outcomes"; "SkillForge updates the skill from those replies".
- IV:2 2.1: Re-draft; merge with IV:1 and open on the shared point (proposing without accepting).
- IV:2 2.5: Cut S4's restated rationale (point back to Section II); fold S3 into the merged opening.
- IV:2 3.1: Keep SkillRL as the subject: "SkillRL proposes a skill when ...; its bank accepts every proposal".
- IV:2 3.2: Start S2 on SkillRL (old), not on "A success-rate threshold".
- IV:2 3.6: End S1 on the mechanism (unconditional acceptance).
- IV:2 4.3: Name who proposes (the agent or the optimizer).
- IV:2 4.14: Move the cross-reference forward; end S4 on a noun, not "it".
- IV:2 AI: Replace the vague opener with the concrete mechanism.
- IV:3 3.1: Keep "these loops" as the topic across S1–S3.
- IV:3 4.1: Shorten the fronted phrase ("Of the 105 recently added core systems, ..."); give S2 a concrete subject.
- IV:3 4.9–4.11: Lead S1 with the point (automatic acceptance dominates) and put the counts after it.
- IV:3 4.14: End S2 on the specific contrast that S3 states, or merge S2 into S3.
- IV:3 5.1: Delete "nevertheless"; delete the second "among them".
- IV:3 AI: Replace "reveals a less even picture" with the claim itself.
- IV:4 5.1: Add the comparator ("than failures") or drop "more often"; delete "particular".
- IV:5 2.5: Keep one statement of "few prioritize" (S1 or S2) and turn S5 into the specific gap (recurrence and severity).
- IV:5 3.2: Put old first: "Two systems are exceptions: Task-CoEvolve ... and AutoSaddler ...".
- IV:5 3.7: Name the subject of S4 and the referent of "it".
- IV:5 4.1: Covered by the 3.2 move.
- IV:5 4.14: End S4 on a noun ("... than the most recent session").
- IV:5 5.3: Give a count or a pointer to the coded data, or soften (AUTHOR FLAG 9).
- IV:6 2.1: Re-draft the opening so it names the theme ("credit assignment") in its stress; the terse beat can stay if it carries the term.
- IV:6 3.1: Make credit assignment (or "the failed output") the running subject.
- IV:6 3.2: Open S3 and S4 on the old topic ("This attribution problem is what harness-optimization papers ...").
- IV:6 3.6: Same as 2.1.
- IV:7 4.3: Use a verb: "these methods tell the proposer which edits helped".
- IV:8 3.1: Keep "the candidate" or "who proposes" as the topic across clauses.
- IV:8 3.6: Open on the point (who proposes the candidate differs by setting), with research reflection as the first case.
- IV:8 4.1: Shorten or move the "Where ..." clause after the main clause.
- IV:8 4.3: "When a person must notice a problem before anyone proposes a fix, ...".
- IV:8 4.9–4.11: Split S2 into prompt platforms and skill repositories.
- IV:8 5.1: Delete "itself"; replace "machinery" with "evaluation" or "gate".
- IV:9 2.5: Cut S3–S4 (already said in IV:1–2) and keep SkillChain in one place (here or IV:12).
- IV:9 3.6: Open on the theme (skill systems differ in where acceptance sits) and end the sentence on it.
- IV:9 3.7: Replace "all three" with an explicit noun, or cut it with S4.
- IV:9 4.1: Give S4 an agent, or cut it.
- IV:9 4.3: "a person decides, after the judge, which refined skills to deploy".
- IV:9 4.9–4.11: Remove the dangling "on which" relative clause by recasting with a verb.
- IV:9 5.1: Delete "simply".
- IV:10 2.1: Name the progression in the opening ("Orchestration moved from score-guided search to gated edits").
- IV:10 3.6: End S1 on that theme.
- IV:10 3.7: Drop "similar" or name the comparison.
- IV:11 2.1: Open on instruction files and the contrast (common, but untested by any gate).
- IV:11 3.6: Put "instruction files" in the stress of S1.
- IV:11 3.7: Name the artifact before referring to it.
- IV:11 4.9–4.11: Split S5: one sentence for the measured results, one for "it does not measure correctness".
- IV:11 5.1: Delete "useful".
- IV:12 2.5: Keep SkillChain in one place; refer to it here by name only.
- IV:12 3.7: Recast S4 so "which" has one antecedent ("Those checks act at release or at admission to a shared pool, and both belong to promotion").
- IV:12 4.1: Shorten S3's subject ("Prompt platforms and registries have no local gate here, because no failure drives their proposals").
- IV:12 4.14: End S3 on "no local gate", with the classification qualifier moved forward.
- IV:13 2.5: Distinguish AutoSaddler's two roles explicitly, or keep it in one subsection only.
- IV:13 5.1: Delete "directly".
- IV:14 2.1: Re-draft the opening to name both operations ("Averaging scores and requiring agreement reduce different errors").
- IV:14 3.1: Keep "the gate" (or the two operations) as the subject throughout.
- IV:14 3.2: Move S6 (the shared trend) to IV:13's opening, or into a separate short closing that picks up the old term.
- IV:14 3.6: Same as 2.1.
- IV:14 3.7: Map each system to its operation; name the event whose probability is $p^k$.
- IV:14 4.1: Move "each with false-acceptance probability $p$" so the verb follows the subject.
- IV:14 4.3: "Acceptance increasingly rests on several observations, not one."
- IV:14 4.9–4.11: Same as 4.1.
- IV:14 AI: Drop one "rather than" frame; state the relation plainly.
- IV:15 4.1: Make the candidate edit or the existing artifacts the subject ("Artifacts already in place also affect how a new edit scores").
- IV:15 4.3: Same as 4.1; name who applies hygiene.
- IV:16 4.3: Use a verb: "Memory products now record each entry's history".
- IV:16 5.1: Delete "substantial".
- IV:16 5.3: Replace the intensifier with the observed relationship (three products record history).
- IV:16 AI: Same as 5.1.
- IV:17 3.1: Split S4–S5 into their own paragraph or bridge them with old information; keep "correction" as the topic.
- IV:18 AI: Name the mechanism ("SkillSmith and SkillAudit can roll back a single edit").
- IV:19 3.8: Order S2–S5 to match conditions 1–5 or signpost each condition's number.
- IV:19 4.3: "SkillOpt meets all five conditions".
- IV:20 2.5: Point back to IV:7 for the consensus result and keep only the new information (removing the buffer and schedule).
- IV:20 3.6: End S1 on the result ("best or tied in every reported cell"), with the attribution moved forward ("Its authors report ...").
- IV:20 4.1: Same as 3.6.
- IV:20 4.3: "shows that the gate and this credit assignment matter in that setting".
- IV:20 4.9–4.11: Split S3, or make the second clause finite ("the removed controls look like stabilizers, not necessities").
- IV:20 4.14: Same as 3.6.
- IV:20 AI: Keep at most one antithesis across the section.
- IV:21 3.6: Open on the distinction (transfer measures usefulness elsewhere; acceptance admits an edit).
- IV:21 3.7: Use the term that IV:19 established for SkillOpt's state (AUTHOR FLAG 8).
- IV:21 AI: End the section on S3's point; cut or shorten S4 (the bridge).

## (d) Role-level verdicts

Passage tests counted: 2.5, 3.1, 3.2, 3.6, 3.7, 3.8. No paragraph failed the prelude (1.2) or illustration (1.6) test. One paragraph (IV:8) sits under a mismatched subsection heading; that is recorded at section level and not counted against the paragraph.

| ¶ | role-level test failed / passage-test failures | verdict |
|---|---|---|
| III_method:1 | 1 (3.7) | keep-and-polish |
| III_method:2 | 2 (2.5, 3.6) | keep-and-polish |
| III_method:3 | 0 | keep-and-polish |
| III_method:4 | 1 (3.2) | keep-and-polish |
| III_method:5 | 1 (3.7) | keep-and-polish |
| III_method:6 | 1 (2.5) | keep-and-polish |
| III_method:7 | 2 (2.5, 3.7) | keep-and-polish |
| III_method:8 | 0 | keep-and-polish |
| III_method:9 | 0 | keep-and-polish |
| III_method:10 | 4 (2.5, 3.1, 3.6, 3.7); also 2.2/2.4 point last | re-draft |
| III_method:11 | 1 (3.6) | keep-and-polish |
| III_method:12 | 4 (2.5, 3.1, 3.6, 3.7); also 1.5 placement (duplicates the caption) | re-draft |
| III_method:13 | 2 (2.5, 3.2) | keep-and-polish |
| III_method:14 | 0 | keep-and-polish |
| III_method:15 | 2 (2.5, 3.7) | keep-and-polish |
| IV_local_findings:1 | 2 (3.1, 3.2) | keep-and-polish |
| IV_local_findings:2 | 4 (2.5, 3.1, 3.2, 3.6) | re-draft (merge with IV:1) |
| IV_local_findings:3 | 1 (3.1) | keep-and-polish |
| IV_local_findings:4 | 0 | keep-and-polish |
| IV_local_findings:5 | 3 (2.5, 3.2, 3.7) | re-draft |
| IV_local_findings:6 | 3 (3.1, 3.2, 3.6) | re-draft |
| IV_local_findings:7 | 0 | keep-and-polish |
| IV_local_findings:8 | 2 (3.1, 3.6); subsection heading mismatch noted at section level | keep-and-polish |
| IV_local_findings:9 | 3 (2.5, 3.6, 3.7) | re-draft |
| IV_local_findings:10 | 2 (3.6, 3.7) | keep-and-polish |
| IV_local_findings:11 | 2 (3.6, 3.7) | keep-and-polish |
| IV_local_findings:12 | 2 (2.5, 3.7) | keep-and-polish |
| IV_local_findings:13 | 1 (2.5) | keep-and-polish |
| IV_local_findings:14 | 4 (3.1, 3.2, 3.6, 3.7); also two claims in one paragraph | re-draft |
| IV_local_findings:15 | 0 | keep-and-polish |
| IV_local_findings:16 | 0 | keep-and-polish |
| IV_local_findings:17 | 1 (3.1) | keep-and-polish |
| IV_local_findings:18 | 0 | keep-and-polish |
| IV_local_findings:19 | 1 (3.8) | keep-and-polish |
| IV_local_findings:20 | 2 (2.5, 3.6) | keep-and-polish |
| IV_local_findings:21 | 2 (3.6, 3.7) | keep-and-polish |

## AUTHOR FLAGS (a fix would touch a claim, number, citation, definition or cross-reference)

1. III:5 S3 "the eight systems without an audit are listed with the contrast set": S3 says the audit covers 202 of the 204 core systems, which leaves 2 core systems unaudited. Where do the other six come from (contrast-set systems? paper-only classifications?)? The count, or its source, needs stating.
2. III:3 vs III:4, contrast set: III:3 S2 defines the contrast set as the systems admitted because they are "publicly described as self-improving, scaffolded, or agentic"; III:4 S3 defines the 52-system "contrast corpus" as the systems that fail the score-≥3 filter. Are these the same set? Reconciling them changes a definition.
3. III:15 S2 vs IV:12 S3: "the human-local cells hold only curation and registries" (under relaxations) vs "Prompt platforms and registries ... have no local gate in this classification". Check whether registries enter a human-local cell only under the relaxed boundaries, and say so if they do.
4. Table V-2 caption, "none of the 126 scores 5 on any substrate": verify that none of the score-5 systems in the table (SAGE, COSPLAY, Cuadros et al., Braintrust, Vellum, LangSmith Hub, NanoResearch, AutoAgent, SkillRL) is among the 126 most recently added; several carry 2026 citation keys.
5. IV:14 S2, "reduces the variance of their mean by a factor of $1/k$": the variance of the mean scales by $1/k$ (that is, it falls by a factor of $k$). The wording can be read either way; this is a math claim for the author to phrase.
6. IV:14 S1–S3: which of SAGE-gate (paired per-item comparisons), VaG (three critics must pass) and AutoSaddler (mini-batch failure signals) is "averaging" and which is "agreement"? SAGE-gate's paired test is neither plain averaging nor agreement. The mapping should be confirmed against the sources.
7. IV:6 S4, "An evaluation of harness optimizers reaches the same conclusion" [@ong2026harnesseval]: confirm that the source concludes attribution is the bottleneck, not only that score alone cannot distinguish an optimizer from trial and error.
8. IV:21 S3, "the acceptance decision that admits an edit to the shared skill bank" vs IV:19 S2, "one markdown skill document used by a frozen agent": which does SkillOpt's gate admit edits into? The answer also bears on SkillOpt's two-loop pass in III:6.
9. IV:5 S1, "nearly every system uses them in arrival order": needs a count, or a pointer to the coded column in the released table.
10. IV:4 S2, "Production memory more often records preferences, successes, or conversation history": uncited; needs a citation or a pointer to the data.
11. The literal captions "Table V-1." and "Table V-2." sit in Section III after the restructure (REVISION_LOG P section order). Check that the rendered table numbers and the labels tab:V-1/tab:V-2 are what the author wants.
12. III:7 S4, "their treatment under relaxed audit rules is reported separately": no location is given, and III:15 does not mention these six systems. A cross-reference (or a sentence in III:15) is needed.
13. III:15 S3, "the full score table with the released table (Supplementary Material S1)": this reads as circular. Is the full score table S1 itself? Clarifying it touches a supplement cross-reference.
14. III:2 S3, "supported production reports": "supported" may encode an inclusion criterion (corroborated by stronger evidence, as in III:13 S4). The author should say what it means rather than have the reviser guess.
15. Duplicate counts: "96 of 105 ... 89" appears in the Introduction ¶5, the Table V-2 caption, III:12 S2 and IV:3 S1. The suggested cut (III:12 S2) removes a number from one place without changing it; the author should confirm which statements stay.

## Group B (III, IV): R-2 reverse outline

# Reverse outline B: III_method.md, IV_local_findings.md

Word counts exclude citation keys. "Tests failed" lists the FLAG cells from ledger_B.md (a) only.

## Paragraphs

| ¶ | role | its point in one sentence | protagonist | themes | evidence | words | tests failed |
|---|---|---|---|---|---|---|---|
| III_method:1 | point | Each system is read for four things (the artifact it changes, the feedback that prompts the change, the decision that accepts it, and the scope of use), so that systems can be compared by behavior rather than name. | we (the survey) | artifact, feedback, decision, scope | none | 51 | 3.7, 4.1, 4.14, AI |
| III_method:2 | evidence | The corpus is 256 systems (Jan 2023 to Oct 2026) from two search passes (130 + 126), drawn from papers, repositories, documentation and production reports. | the corpus | corpus size, search passes, sources | Supp. S2 | 57 | 2.5, 3.6, 4.14, 5.1 |
| III_method:3 | explanation | Systems enter if they adapt through a persistent artifact or are described as self-improving, scaffolded or agentic (the contrast group); weight-only and undeployed systems are excluded. | a system | inclusion, contrast set, exclusion | none | 69 | 4.1, 4.3, 4.9–4.11 |
| III_method:4 | explanation | The first filter (a score ≥3 on any substrate) splits the corpus into 204 core and 52 contrast systems, which occupy 269 scored rows. | the filter / systems | core corpus, contrast corpus, scored rows | none | 62 | 3.2, 4.14 |
| III_method:5 | explanation | The second filter, the two-loop audit (does session feedback change a persistent artifact, and is that artifact promoted with lineage?), admits 11 research systems and 3 industry exemplars. | the audit | two-loop audit, promotion, lineage | Supp. S4; Fig. corpus | 85 | 3.7, 4.1, 4.9–4.11 |
| III_method:6 | evidence | The passing systems are named, and SkillOpt is identified as a paper-only classification. | passing systems | passers, industry exemplars, paper-based classification | Supp. S2, S4 | 74 | 2.5, 4.9–4.11 |
| III_method:7 | point | Passing the audit does not mean governed cross-organization sharing: all passers promote within one operator or deployment, Letta passes without a gate, and six systems promote without lineage. | passing systems | governed sharing, operator scope, lineage, gate | none | 75 | 2.5, 3.7, 4.3, 4.14 |
| III_method:8 | shared context | The scaffold has six substrates (instructions, skills, memory, tools, orchestration, governance), and these are the targets of an edit. | the scaffold / substrates | six substrates, edit targets | Table V-1; Sumers et al. | 37 | 4.14 |
| III_method:9 | explanation | The common 0–5 scale runs from ephemeral (0) to program-updated from feedback (4); what a 5 requires depends on the substrate. | the artifact | scoring scale, persistence, feedback, gate | Table V-1 | 67 | 4.14 |
| III_method:10 | explanation | A 5 certifies different things on different substrates (both loops for instructions and skills, governance capability for memory, tools and governance, breadth for integrated rows), so the scale supports only within-substrate comparison. | the substrates (should be: the score) | score-5 meaning, loops, governance, integrated rows | Tables V-1, V-2 | 85 | 2.1, 2.5, 3.1, 3.6, 3.7, 4.1, 4.3, 4.14, 5.1, AI |
| III_method:11 | evidence | Research systems hold the top scores on skills, memory and integrated rows and production platforms on governance; no system tops instructions, tools or orchestration, and none tops all six. | systems | top scores, research vs production, empty substrates | Table V-2 | ~47 | 2.1, 3.6, 4.1, AI |
| III_method:12 | housekeeping | The gate, feedback and governance counts come from explicit columns recorded only for the 126 newest systems (e.g., 96 of 105 have a local loop, 89 under a program), not from all 256. | the recorded columns / counts | count scope, 126 subset, gate counts | released table | 64 | 2.5, 3.1, 3.6, 3.7, 4.1, 4.14 |
| III_method:13 | explanation | Evidence is weighted by tier: peer review and open source count most, production claims need a named target, blogs need corroboration, and vendor evidence is never pooled with peer-reviewed evidence. | evidence types | evidence tiers, weighting, vendor claims | released table | 89 | 2.5, 3.2, 4.14 |
| III_method:14 | other view | A single author scored conservatively, without re-rating, so the scores are an auditable interpretation of public evidence, not an inventory of private behavior. | the author / scores | single rater, rounding down, auditability | none | 50 | AI |
| III_method:15 | evidence | Relaxing the audit boundaries changes membership but not the structural findings: [Auto × Auto] stays populated, human-local cells hold only curation and registries, Letta alone passes ungated, and no relaxation adds governed cross-organization promotion. | the audit / findings | sensitivity, relaxations, structural findings | Section gap; Supp. S1, S2 | 92 | 2.5, 3.7, 5.1 |
| IV_local_findings:1 | point + illustration | A system can detect, explain and correct a failure without testing the correction; SkillForge's calibrated judge picks replies to rewrite, but the skill updates are committed untested. | SkillForge (drifts to judge / replies / calibration) | detection vs acceptance, calibration, acceptance test | skillforge2026 | 78 | 3.1, 3.2, 4.1, 4.3 |
| IV_local_findings:2 | illustration + rationale | SkillRL proposes skills from a success-rate trigger and accepts every proposal unconditionally, which is why the survey records the acceptor separately from the proposer. | SkillRL / both systems | unconditional acceptance, proposer vs acceptor | skillrl2026; Section loop | 62 | 2.1, 2.5, 3.1, 3.2, 3.6, 4.3, 4.14, AI |
| IV_local_findings:3 | point | Of the 105 newest core systems, 96 have a local loop and 89 accept automatically; evaluation is mature, while the failure record and failure-to-artifact attribution are weak. | local loops | automatic acceptance, failure record, attribution | released table counts | 65 | 3.1, 4.1, 4.9–4.11, 4.14, 5.1, AI |
| IV_local_findings:4 | evidence | Production memory rarely keeps a comparable record of failures; only one self-reported field report describes a dead-end store. | the failure history / memory store | failure history, production memory, dead ends | helwig2026memory | 71 | 5.1 |
| IV_local_findings:5 | evidence | Systems use retained failures in arrival order; only Task-CoEvolve and AutoSaddler weight experience, and none prioritizes by recurrence and severity. | systems | prioritization, arrival order, recurrence/severity | miyai2026taskcoevolve; park2026autosaddler | 69 | 2.5, 3.2, 3.7, 4.1, 4.14, 5.3 |
| IV_local_findings:6 | problem | A failed output does not reveal which artifact caused it, and the harness-optimization literature names this attribution step as the bottleneck. | (none; should be credit assignment) | attribution / credit assignment, bottleneck | lin2026ahe; zehle2026cantante; lee2026metaharness; nguyen2026harnessevo; liu2026skillsvote; ong2026harnesseval | 65 | 2.1, 3.1, 3.2, 3.6 |
| IV_local_findings:7 | evidence | Existing attribution methods (Meta-Harness, SkillsVote, SkillOpt-Lite) work within one substrate; none solves attribution across all six. | attribution methods | within-substrate attribution, consensus, proposal evidence | lee2026metaharness; liu2026skillsvote; shen2026skilloptlite | 71 | 4.3 |
| IV_local_findings:8 | evidence | Candidates come from trajectory reflection in research, but from people in production platforms and skill repositories, so improvement there is intermittent even when evaluation is automatic. | who proposes (hops) | candidate generation, human proposal, intermittency | shen2026whomaintains | 85 | 3.1, 3.6, 4.1, 4.3, 4.9–4.11, 5.1 |
| IV_local_findings:9 | evidence | Skill systems differ in where acceptance sits: SAGE and COSPLAY close both loops, SkillChain adds a human decision, SkillRL and SkillForge leave edits unchecked. | skill systems | gate placement on skills, both loops, human decision | wang2025sage; wu2026cosplay; hu2026skillchain | 58 | 2.5, 3.6, 3.7, 4.1, 4.3, 4.9–4.11, 5.1 |
| IV_local_findings:10 | evidence | Orchestration moved from score-guided topology search to gating topology edits before keeping them (OptiMAS excepted); none closes both loops with lineage. | orchestration systems | topology search, evaluation gate, lineage | zhuge2024gptswarm; zhang2024aflow; chu2026agentgrad; chen2026harnessforge; zhao2026tocomas; cheng2026optimas | 75 | 2.1, 3.6, 3.7 |
| IV_local_findings:11 | evidence | Instruction files are widespread (in a fifth to a quarter of coding-agent projects), but two studies disagree on cost and neither shows a task-success benefit. | instruction files, then studies | prevalence vs effectiveness, cost, task success | agentsmd2025; robbes2026agenticmuch; galster2026harnessconfig; gloaguen2026agentsmd; lulla2026empirical | 113 | 2.1, 3.6, 3.7, 4.9–4.11, 5.1 |
| IV_local_findings:12 | explanation | Human local gates exist only as curation (VerificAgent, SkillChain); platform and registry checks act at release or admission, so they count as promotion. | human gates | human local gate, curation, release vs local | nguyen2025verificagent | 59 | 2.5, 3.7, 4.1, 4.14 |
| IV_local_findings:13 | evidence | Because one run is too noisy, newer gates gather more evidence: paired per-item tests (SAGE-gate), multiple critics (VaG), mini-batch signals (AutoSaddler). | acceptance test / systems | noisy acceptance, multi-observation gates | wang2026sagegate; shang2026vag; park2026autosaddler | 55 | 2.5, 5.1 |
| IV_local_findings:14 | explanation | Averaging reduces variance while agreement multiplies false-acceptance probabilities (under independence), and acceptance increasingly rests on several observations. | (hops: mechanisms, averaging, agreement) | averaging vs agreement, independence, body of evidence | Appendix gates | 76 | 2.1, 3.1, 3.2, 3.6, 3.7, 4.1, 4.3, 4.9–4.11, AI |
| IV_local_findings:15 | point | Existing artifacts confound the evaluation of a new edit, so skill systems now gate removal as they gate admission. | existing artifacts / skills | stale artifacts, lifecycle hygiene, gated removal | zhang2026ratchet; zhang2026librarydrift; wei2026skillsmith; pu2026skillops; wang2026assay; Supp. S6 | 75 | 4.1, 4.3 |
| IV_local_findings:16 | evidence | Memory products record each entry's history (git, per-memory history, bitemporal facts). | memory products | entry history, provenance | letta2026memfs; mem02026history; zep2026facts | 44 | 4.3, 5.1, 5.3, AI |
| IV_local_findings:17 | evidence | Recorded history does not enforce correction: all five production backends return revoked facts; research systems split between provenance controls and verifier-gated correction, and only Cuadros et al. combine them. | history / memory systems | correction, revoked facts, provenance | shen2026revoked; wang2026toki; xu2026ppmf; margalit2026governed; sun2026vermem; yu2026recuris; wang2026memguard; cuadros2026governed | 65 | 3.1 |
| IV_local_findings:18 | evidence | Rollback exists (SkillSmith, SkillAudit, EvoUndo), but an edit's consequences outlast it once other skills derive from it. | reversal | rollback, derived artifacts, lasting consequences | wei2026skillsmith; gao2026skillaudit; sah2026evoundo; shang2026vag; Section failure | 62 | AI |
| IV_local_findings:19 | illustration | SkillOpt meets all five conditions: a skill document, rollout failure evidence, a consensus filter, bounded edit operators, and a strict held-out gate. | SkillOpt | five conditions, gate, consensus | yang2026skillopt | 65 | 3.8, 4.3 |
| IV_local_findings:20 | evidence | SkillOpt is best or tied everywhere reported, and SkillOpt-Lite matches it without the buffer and schedule, so the gate and consensus credit assignment carry the gain. | SkillOpt / SkillOpt-Lite | results, ablation, gate, credit assignment | shen2026skilloptlite | 74 | 2.5, 3.6, 4.1, 4.3, 4.9–4.11, 4.14, AI |
| IV_local_findings:21 | point | SkillOpt's transfer experiments measure portability and are distinct from the acceptance decision, and this distinction matters more where correctness is hard to measure. | SkillOpt's experiments | transfer vs acceptance | none | 54 | 3.6, 3.7, AI |

## Sections and subsections

| section | its opening's point sentence, quoted | themes named | order | does the heading carry a theme? |
|---|---|---|---|---|
| III Corpus and method | "We read each system's public method or documentation for four things: the persistent artifact it changes, the feedback that prompts the change, the decision that accepts it, and the scope in which the result is used." | artifact, feedback, decision, scope | logical (selection → scoring → evidence) | no: a label |
| III-A Scope and selection | "The corpus contains 256 unique systems from January 2023 through the October 2026 cutoff." (The section's real point, "Passing this audit does not establish governed sharing across organizations.", comes in III:7.) | corpus, filters, two-loop audit, governed sharing | chronological/procedural (inclusion → filter 1 → filter 2 → passers → qualification) | no: a label |
| III-B Substrates and scoring | "The scaffold has six substrates: instructions, skills, memory, tools, orchestration, and governance." | substrates, 0–5 scale, score-5 meaning, distribution | logical (define → scale → interpret → distribution → count scope) | no: a label |
| III-C Evidence and limitations | "The evidence ranges from peer-reviewed studies and open-source artifacts to vendor claims." | evidence tiers, single rater, sensitivity | coordinate | partly: names the topic, not a finding |
| IV What local adaptation actually closes | "Evaluation is comparatively mature, while the failure record and the link from a failure to the responsible artifact are often incomplete." (end of the three-paragraph opening, IV:3) | automatic acceptance, failure record, attribution | logical (follows the loop: failure log → attribution → candidate → gate → evidence → maintenance → worked example) | partly: names the question, not the finding; "actually" is a tic |
| IV-A Finding the right thing to change | "A useful failure history must retain what went wrong in a form that supports later comparison." | failure history, prioritization, attribution/credit assignment | logical (log → prioritize → attribute → partial solutions) | partly: an action, not the finding (failure records and attribution are weak) |
| IV-B Testing the candidate | "Research systems commonly generate candidates by reflecting on trajectories." | candidate generation, gate placement per substrate, instruction files, human gates | coordinate (by substrate and by gate type), mixed with proposal | no: ¶8 is about proposing, not testing; the subsection covers four distinct topics |
| IV-C Gathering enough evidence to accept | "An acceptance test can itself be too noisy to support a decision from one run." | noisy gates, averaging vs agreement | logical | yes |
| IV-D Maintaining the artifacts that survive | "The evaluation of a new edit also depends on the artifacts already present." | removal, history, correction, reversal | coordinate (removal → history → correction → reversal) | partly |
| IV-E A complete local example | "SkillOpt provides a concrete instance of all five conditions [@yang2026skillopt]." | five conditions, gate, credit assignment, transfer vs acceptance | logical (mapping → results → transfer) | no: a label |

## Group C (V, VI): S4 diagnostic ledger

# Diagnostic ledger C: Sections V (feedback classes) and VI (promotion)

Stage S4 (Diagnose), review only. Files diagnosed:
- `cg_pre/V_feedback_signal_classes.md` (¶ V:1 to V:18)
- `cg_pre/VI_promotion.md` (¶ VI:1 to VI:17)

Paragraphs are numbered per file; sentences are numbered S1, S2, ... within each paragraph. House style (telegrapher_paper_style_guide.md) is applied on conflicts: one claim per paragraph, mechanism over capability, no feature-list voice, honest accounting in one place, end sections clean, one name per concept. No em-dashes were found in either file; spelling is American throughout.

Short-aside exemption used once: VI:14 (3 sentences, 47 words, figure/table pointers plus one set-up sentence) skips 2.1 to 2.4 and 3.6.

## (a) Mandatory ledger

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V:1 | prelude (section vignette) | FLAG: S1–S4 name no theme word; "evidence"/"signal" first appear in V:2 (mild for a prelude) | FLAG: repeats the Introduction's four cases almost one to one ("A compiler or test suite can check a candidate immediately. A booked appointment provides a later, noisier outcome. A writing task may depend on a judge... A research decision may take months") | pass (note: four parallel assistants as subjects; the parallel set is the point) | pass (note: each sentence opens on a new assistant, but the repeated frame makes it predictable) | pass (close: S1 stress "within seconds" names only timing) | pass (note: S4 "the direction" stands in for "its strategy"; readable) | pass | pass | pass | pass | FLAG: S2 ends "an appointment was made" and S4 "was productive", so the class-defining delay ("later", "months") sits mid-sentence, while S1 ("within seconds") and S3 ("a reviewer's preference") end on it | pass | pass | pass | FLAG: uniform rhythm, four sentences on one frame "A ___ changes its ___ and ___"; present-tense cold open (one paragraph, within cap) |
| V:2 | point (section opening) | pass (S1–S2 end "the evidence available for accepting it") | pass | FLAG: subjects hop "All four systems" → "What differs" → "The signal's timing, exactness, and dependence on judgment" → "We"; the feedback signal is subject once | FLAG: S3 opens on "The signal's timing", but S2 ended on "evidence"; "signal" is new here | pass (close: the two-sentence opening ends on the pronoun "it") | pass | pass | FLAG: S3 abstract 7-word subject "The signal's timing, exactness, and dependence on judgment"; verb "determine" at word 8 | FLAG: S3 "dependence on judgment" | pass | FLAG: S2 ends on pronoun "accepting it"; S4 ends on housekeeping "summarized in Table REF(tab:IV-1)" | pass | pass | pass | FLAG: synonym cycling "evidence" (S2) / "signal" (S3) / "feedback classes" (S4) for one concept |
| V:3 | body (assignment rule) | pass (S1 ends "the constraint that binds first") | pass | pass (close: subjects are the constraints in decision order: "A long delay", "the absence of an independent ground truth", "repeatable exact checks") | pass | pass | pass (note: S5 "supports it" resolves to "decision") | pass (rule told in decision order: delay, ground truth, exactness) | FLAG: S1 passive hides the doer "The classes are assigned by the constraint" (we assign); S3 abstract subject "the absence of an independent ground truth" | FLAG: S3 "the absence of an independent ground truth makes the signal C3" | pass | FLAG: S5 ends on pronoun "the signal that supports it" | pass | pass | pass | pass |
| V:4 | body (evidence) | pass (S1 ends "immediately and repeatably") | pass (note: S1 restates the table's C1 cell "at once and repeatably"; deliberate theme) | FLAG: subjects tour "AlphaEvolve" → "SkillOpt" → "DGM" → "The broader benchmark score"; the exact check (S1–S2) leaves subject position | pass (note: S3 opens on a system name, anticipated as an instance of S2) | pass | FLAG: S5 "The broader benchmark score" is presented as old, but no broader benchmark was stated (S4 names only "ten benchmark tasks"); S2 "This" points at a whole clause (close) | pass | pass | FLAG: S4 "makes a narrower acceptance decision"; S3 "uses held-out exact-match evaluation" | pass | FLAG: S2 ends "straightforward to implement", putting stress on "implement" rather than on the automatic gate | pass | pass | pass | pass |
| V:5 | body (limit) | pass (S1 ends "the deployment as a whole") | FLAG: S4 "Passing the suite also establishes only the properties the suite tests" restates S1 and the Section II limit "an accepted edit is evidence of improvement only on the measure and tasks evaluated" (also table C1 "an improvement in what the check measures on the cases it ran"; V:18 S4) | FLAG: subjects "Exactness" → "Repeating a deterministic check" → "an agent" → "a finite suite" → "Estimating the change in patch loss" → "Passing the suite"; gerunds hide the actor | FLAG: S3 opens on new "Estimating the change in patch loss" and ends on old "that variation" | pass | FLAG: S3 "that variation" points to two things in S2: stochastic outputs and partial sampling of the task distribution (sampling coverage is not variation) | pass | FLAG: S1 abstract subject "Exactness"; S3 gerund subject, verb "requires" at word 7 | FLAG: S3 "requires accounting for that variation" | pass (note: S2 has three clauses, "but ... and", carrying two different reasons) | FLAG: S1 ends on qualifier "as a whole"; S4 ends on a repeat "the suite tests" after "Passing the suite" | FLAG: S1 "as a whole" (inferable); S4 "also" | pass | pass | FLAG: antithesis "applies to the check, not to the deployment" (1 of 4 in V; over cap) |
| V:6 | body (problem) | FLAG: S1 "Two problems remain even with a reliable checker" names no problem; the themes arrive in S2–S3 | pass (note: S2 repeats table C1 "the check names the failed output, not the coordinate that caused it"; S4 is the point, not a restatement) | FLAG: subjects "Two problems" → "A failed test" → "repeated optimization" → "Cheap acceptance" → "Exact feedback"; exact feedback is subject only in S4 | FLAG: S3 opens on new "Cheap acceptance" | FLAG: S1 stress "a reliable checker" is old; attribution, overfitting and pool growth are absent from the opening | pass (note: S2 "can overfit it": "it" is the suite grammatically, but the scaffold is what overfits) | pass | FLAG: S3 abstract subject "Cheap acceptance"; S2 second clause "repeated optimization" | FLAG: S4 "makes evaluation easier" and "does not supply attribution or lifecycle management" | pass | FLAG: S1 "a reliable checker" (old); S2 ends on pronoun "overfit it" | FLAG: S3 "also"; "sufficient" in "without sufficient pruning" | pass | pass | FLAG: S3 capability voice "can also allow the artifact pool to grow"; S4 antithesis "makes evaluation easier; it does not supply"; the count "Two problems" against three listed (AUTHOR FLAG 1) |
| V:7 | context | pass (two-sentence opening ends "noisy or confounded") | FLAG: S1 repeats the table's C2 cell nearly verbatim ("a booked slot, a merged pull request, a closed ticket; noisy and confounded"); the booked appointment is in its fourth appearance (Intro, V:1, Table, V:7) | pass (note: one hop to "A user" in S3) | pass | pass | pass | pass | FLAG: S1 subject is a 12-word list; verb "provides" at word 13 | FLAG (mild): S1 "provides an observable result" | pass | pass | FLAG: S2 "meaningful" (vague) | pass | pass | pass |
| V:8 | body (evidence) | FLAG: S1 ends "as feedback" plus a citation; the paragraph's claim "The same kind of outcome can therefore support different operations" is S4 | pass | FLAG: tour "Devin" → "SAGE" → "PACE" → "SkillRL" → "The same kind of outcome" | pass (note: S1 picks up V:7's "merged pull request") | FLAG: opening stress "as feedback" does not name the theme (one outcome, different operations) | pass | pass | pass | pass | pass | FLAG: S4 ends on a repeat "different operations in different systems" | pass | pass | pass | FLAG: point-last summary (evidence, evidence, then a "therefore" generalization) |
| V:9 | body (explanation) | pass (close: S1 "sampled repeatedly" frames S1–S2 only; S3–S4 turn to observed outcomes in general) | FLAG: S4 "reveals that the task failed more readily than why it failed" restates the table's C2 cell "The outcome says *that* the episode failed, not *why*" | FLAG (mild): subjects "Simulated outcomes" → "They" → "an automatic gate" → "the result" | pass | pass | pass | pass | FLAG: S1 verb "remove" at word 14 | pass | FLAG: S1 interruption between subject and verb "such as those in Voyager's game world or SAGE's AppWorld" | pass (note: S4 repeats "failed" deliberately for the that/why contrast) | FLAG: S2 "distinguishable" (vague); S3 "more generally" | FLAG: S4 stacked qualifiers "usually reveals ... more readily than" (flag only; the hedge is part of the claim) | pass | pass |
| V:10 | body (problem) | pass (theme "Promotion is harder" at the start; S1 ends "acceptance behavior") | FLAG: S2 "A sender's successful outcome is not an evaluation of the recipient" restates the receiving-side caveat in Section II ("the local evaluation says little about them"), V:18 S4, VI:1 S2–S3 and VI:3 | FLAG: subjects "Promotion" → "A sender's successful outcome" → "This class"; S3 changes topic | pass | pass | pass (close: S3 "This class" reaches back to V:9 S2 "within C2" across a promotion sentence) | pass | pass | FLAG: S2 "is not an evaluation of"; S3 "connecting the reliability of feedback to the integrity of its source" | FLAG: S3 relative clause "channels that can carry poisoned memories or injected tool instructions" plus a tacked-on participle "connecting ..." | pass | FLAG: S3 "also" | pass | pass | FLAG: trailing participle "..., connecting the reliability of feedback to the integrity of its source"; two claims in one paragraph (promotion; poisoned channels) |
| V:11 | context + evidence | pass (S1 ends "or model judge") | pass (note: S2 "There is no independent exact answer" repeats V:3 S3 "the absence of an independent ground truth" and the table's "no ground truth"; could go) | FLAG: subjects "a gate" → "There" → "CASCADE" → "a reviewer" → "SkillForge" | pass (note: S3 opens on a system name, anticipated as an instance) | pass | FLAG: S4 "earlier in the process": the process, and the later point it is compared with, are unstated | pass | pass (note: 8 words of meaningful circumstance before "a gate") | pass | pass | FLAG: S2 ends on a passive participle "being measured" | pass | pass | pass | pass |
| V:12 | point | pass (close: S1 stress "evidence of that preference"; the theme word "calibrated" sits mid-sentence) | pass | FLAG: subjects "A program" → "its score" → "the score" → "The gate labels" → "an uncalibrated model judge" → "the meaning of its acceptances" → "SkillForge, SkillChain, and SkillCoach" | pass | pass (close: see 2.1) | FLAG: S2 "this distinction" is presented as old, but S1 states a requirement (calibrate before treating the score as evidence), not a distinction | pass | pass | FLAG: S2 "the meaning of its acceptances is less established" | FLAG: S1 (33 words) tacks two subordinate clauses after the main clause: "it is intended to represent" and "before the score is treated as evidence of that preference" | FLAG: S2 ends on qualifier "less established" | pass | pass | pass | pass |
| V:13 | problem | FLAG: S1 "Optimization introduces another risk" ends on a placeholder; the theme (the judge is a target that can be gamed and that moves) arrives in S2 | pass (note: S2 repeats table C3 "the proxy gets optimized past the point where it tracks quality") | FLAG: subjects "Optimization" → "A scaffold" → "Reward-model research" → "Human evaluation" → "Shankar et al." → "evaluators' criteria" → "the system" → "This reflexive gate" | FLAG: S3 opens on new "Reward-model research" and ends on old "this form of proxy overoptimization" | FLAG: S1 stress "another risk" | FLAG: S1 "another risk" presumes an earlier risk; V:11–V:12 name none (calibration is a requirement) | pass | FLAG: S1 abstract subject "Optimization" plus empty verb "introduces" | FLAG: S1 "introduces another risk" | pass | FLAG: S1 "another risk"; S6 ends on a cross-reference "is developed in Section REF(sec:reflexive)" | pass | pass | pass | pass |
| V:14 | context/problem | pass (S1 ends "many intervening edits") | pass (note: S3 is the table's C4 "Credit across many edits", first stated in prose here) | pass (close: "Research programs and open-ended discovery" → "The AI Scientist" → "The eventual outcome"; short) | pass (note: S2 opens on a named system as illustration) | pass | pass | pass (S2: ideas, experiments, paper, in order) | pass (close: S1 verb "may produce" at word 7) | pass | pass | pass | FLAG: S1 "meaningful" (vague; second use after V:7); S2 "broad" | pass | pass | pass (note: drift "edits" S1 → "scaffold change" S3) |
| V:15 | body (evidence) + boundary note | pass (S1 ends "intermediate decisions") | FLAG: S4 "they do not estimate each edit's contribution to the eventual loss" restates V:14 S3 ("cannot usually be assigned to each preceding scaffold change"); the same point recurs in V:16 S2 and V:17 S3 and S5 | FLAG: subjects "Systems in this class" → "NanoResearch" → "CORAL" → "These operations" → "AlphaEvolve's archive diversity" → "its candidates" → "archive selection" | FLAG: S5 opens on new "AlphaEvolve's archive diversity", a C1 system in the C4 paragraph | pass | pass | pass | FLAG: S5 abstract subject "AlphaEvolve's archive diversity" with negative verb "does not make it" | FLAG (mild): S1 "use intermediate decisions" | pass | FLAG: S3 ends on peripheral "on a heartbeat"; S5 ends "within C1", which takes the paragraph's last stress away from C4 | pass | pass | pass | FLAG: caveat in the stress position (the S5 boundary note closes the paragraph) |
| V:16 | body (limits) | pass (S1 ends "at the longer horizon") | FLAG: S2 "Temporal credit assignment remains unresolved" restates V:14 S3 and V:15 S4; S3 restates table C4 "the loop cannot be told from random search" | FLAG: subjects "the descent interpretation" → "Temporal credit assignment" → "the environment" → "Outcome gains alone" | pass (note: S3 "Outcome gains alone" is loosely old) | pass | pass (close: S1 "the longer horizon" relies on V:14's "weeks or months") | pass | pass | FLAG: S3 "to distinguish directed improvement from a successful search", "the evaluation of harness optimizers" | pass (S3 summative modifier is legitimate) | FLAG: S3 ends on an attribution "a limitation emphasized in the evaluation of harness optimizers [@ong2026harnesseval]" | FLAG: S3 "also" | pass | pass | pass (note: "harness" against the paper's "scaffold"; see flags-only) |
| V:17 | point (section consequences) | pass (S1 ends "checked against the corpus") | FLAG: S5 "Delayed feedback supports no immediate per-edit gate on either half" restates S3 "delayed feedback cannot evaluate edits individually until the outcome arrives" (and V:14–V:16); S6 restates Table IV-1's "What stays hard" column | pass (close: subjects alternate gate types and signal types: "local automatic acceptance", "Judged acceptance", "delayed feedback", "automatic promotion", "human promotion", "the main failure risks") | pass | pass | FLAG: S5 "either half" is presented as old; the section says "the two loops", not "halves" | pass | FLAG: S2 abstract subject plus passive "local automatic acceptance is most directly supported by"; S4 subject with relative clause "automatic promotion that estimates a loss change" | pass | FLAG: S4 (40 words) joins two main clauses with "and"; "in exact and re-runnable simulated settings" attaches ambiguously (to "applied at the recipient" or to "occur") | FLAG: S5 ends "on either half" | pass | pass | pass | pass (note: First/Second/Third predictions are a legitimate enumeration) |
| V:18 | other view + closing caveat | pass (S1 ends "execute a decision") | FLAG: S4 "sharing remains an additional empirical question: even the same exact checker must be applied to the recipient's relevant cases" restates V:10 S2 and Section II; VI:1 repeats it on the next page | FLAG: subjects "These" → "A program" → "Section REF(sec:design)" → "sharing" | FLAG: S4 opens on a new topic "In every class, sharing" | pass | pass | pass | pass | FLAG: S4 "before broader performance is established" | pass | FLAG: S4 ends on passive "is established" | FLAG: S4 "relevant" (vague) | pass | pass | FLAG: S1 antithesis "expectations ..., not restrictions" (fourth in V, about 1,350 words); the section ends on a caveat instead of its result (house rule: end sections clean) |
| VI:1 | context → point (section opening) | pass (S1 ends "in the next") | FLAG: restates Section II's "The second decision" paragraph ("Other repositories may follow a different convention, and the local evaluation says little about them") and V:18 S4 just before | pass (close: "A rule" → "Copying the file" → "The recipient" → "This") | pass (note: S2 "the file" for S1's "rule") | pass | FLAG: S4 "This is the additional decision": "This" has no single antecedent (S3 is an obligation with two options), and "the additional decision" is presented as old | pass | pass | pass | pass | FLAG: S2 ends on pronoun "justified it" | FLAG: S3 "relevant" | pass | pass | pass (note: S2 antithesis "the instruction, but not the evidence", 1 of 5 in VI) |
| VI:2 | context (definitions) | pass (S1 ends "five nested scopes") | FLAG: S7 "Promotion changes which population the edit is intended to improve" restates Section II ("That decision changes the population on which the rule will act") and the Fig. 2 caption ("Wider adoption changes the population on which an edit acts") | pass (definitions; the scopes are subjects) | pass | pass | pass | pass | pass | pass | pass | FLAG: S7 ends on a figure pointer "as shown in Fig. REF(fig:scope)" | pass | pass | pass | pass |
| VI:3 | point | FLAG: S1 "The nesting makes an important limit visible" names no limit; the theme (an average hides harm to one recipient) arrives in S2 | pass | FLAG: subjects "The nesting" → "A lower average loss" → "The proposed architecture" → "Versioning and access control" → "receiving-side evaluation" | FLAG: S3 opens on new "The proposed architecture in Section REF(sec:gap)"; S4 on new "Versioning and access control" | FLAG: S1 stress "visible" | pass | pass | FLAG: S1 abstract subject "The nesting" | FLAG: S1 empty verb "makes ... visible" | pass | FLAG: S1 ends "visible"; S4 ends on the pointer "there" | FLAG: S1 "important" | pass | pass | FLAG: intensifier "important" |
| VI:4 | body (evidence) | pass (S1 ends "within one operator") | FLAG: S5 "These are concrete instances of evidence being gathered beyond the source deployment" restates S1 | pass (note: systems as related subjects after the general claim) | pass | pass | pass | pass | pass | FLAG: S5 "concrete instances of evidence being gathered beyond" | pass | pass | FLAG: S5 "concrete" | pass | pass | FLAG: point-last summary closer (S5) |
| VI:5 | body (other view) | pass (close: S1 ends "elsewhere") | pass (note: S5 draws S4's consequence; VI:6 S2 repeats this paragraph) | pass (close: federated systems and their parts) | pass | FLAG: S1 stress "elsewhere" is relative and vague; the theme (the check sits at the aggregator or server, not the recipient) arrives in S2 | FLAG: S5 "They" follows S4's subject "Their clients" but means EvolveNet and FederatedSkill | pass | pass | pass | pass | FLAG: S1 ends "elsewhere" | pass | pass | pass | pass (note: S4 antithesis "..., not independently governed customer organizations") |
| VI:6 | point | pass (close: S1 names both themes, "location" and "coverage") | FLAG: S2 restates VI:4–VI:5 system by system; S4 "finite evaluation does not guarantee performance on all future tasks" restates V:5 S4 and the Section II limit | FLAG: subjects "The location of the evaluation" → "its coverage" → "ShareMem, XRepoSkill, and Evo2Team" → "EvolveNet" → "FederatedSkill" → "nearly a fifth of confirmed transfers" → "A receiving-side check" → "finite evaluation" | pass | FLAG: S1 ends on a repeat "correctly located" (after "The location"); "coverage" sits mid-sentence | FLAG: S3 "graphs" has no antecedent; Evo2Team was described as promoting "routing skills between teams" | pass | FLAG: S1 abstract subject "The location of the evaluation" | FLAG: S1 "The location of the evaluation"; S3 "not covered by confirmation"; S4 "provides necessary evidence for adoption" | pass | FLAG: S1 "correctly located" (repeat); S3 "by confirmation" | pass | pass | pass | FLAG: semicolon chain in S2 (three clauses) |
| VI:7 | body (evidence) → point | pass (S1 ends "that later runs reuse") | pass (note: S4 "within one operator" echoes VI:4–VI:5) | pass (close: research systems as subjects until S5 "That pool") | FLAG: S5 opens on "That pool", a noun not used before | pass | FLAG: S5 "That pool" is presented as old; S2 "this shared environment" also renames "bank or archive" | pass | pass | FLAG: S2 "apply programmatic decisions"; S3 "before archive admission" | pass | FLAG: S1 ends "that later runs reuse", an object relative that invites reading "runs" as the verb | pass | pass (note: S4 "AlphaEvolve has produced gains used within Google" has no citation in its own sentence) | pass | FLAG: synonym cycling "bank or archive" / "shared environment" / "archive" / "pool" |
| VI:8 | point | pass (S1 ends "evidentiary meaning") | FLAG: S3 "an automatic promotion decision can exist where a per-edit improvement estimate does not" restates V:18 S1–S2 ("A program can merge two judged artifacts or prune a delayed proposal without estimating a loss change"); NanoResearch's merge was already discussed in V:15 | FLAG: S2 subject is three nominalized operations; S3 subject "The distinction"; no character acts | pass | pass | pass (close: S3 "The distinction anticipated by the feedback classes" reaches back to V:18 across a section break) | pass | FLAG: S2 verb "are" at word 16 after the list subject; S1 abstract negative opener "Not every automatic admission" | FLAG: S2 nominalized subject plus "are programmatic decisions"; "a candidate's reduction in patch loss"; S3 "an automatic promotion decision can exist where a per-edit improvement estimate does not" | pass | pass (note: S3 ends on an elliptical "does not", deliberate) | FLAG: S3 "essential" | FLAG: S3 "is therefore essential" is an intensifier without evidence | pass | FLAG: intensifier "essential"; noun piles "per-edit improvement estimate", "automatic promotion decision" |
| VI:9 | body (evidence) → interpretive point | pass (S1 ends "promotion decision") | FLAG (mild): S3 Devin's merge repeats V:8 S1; S5 CASCADE repeats V:11 S3 and Table VII-1 ("and CASCADE") | FLAG: tour "Sierra" → "the same pull-request merge" → "Spotify's optimized prompts and plans" → "CASCADE" → "the person at the promotion gate"; the person is subject only in S6 | pass (note: system names as instances of S1) | pass | pass | pass | pass | pass | FLAG: S6 (41 words) puts its main claim in a tacked-on "which" clause, and the 13-word object "a program on the local gate with a person on the promotion gate" interrupts "makes ... the production-viable pairing" | FLAG: S6 ends on the rejected alternative "rather than a compromise" | pass | FLAG: S6 "the production-viable pairing rather than a compromise" is an unhedged evaluative claim (AUTHOR FLAG 4) | pass | FLAG: overbalance "rather than a compromise"; "which" refers to a whole clause |
| VI:10 | body (evidence) | FLAG: S1 "take a different path" names no theme; the claim that unifies the paragraph (None at promotion, for two reasons) arrives in S7 | FLAG: S4 "The record explains what was shared, while leaving whether it should have been shared unresolved" restates S3 "pushed with git lineage but without an acceptance check" | FLAG: subjects "Letta's Context Repositories" → "background reflection" → "the only check on a local edit" → "the system" → "Shared-memory changes" → "The record" → "promotion" → "AutoAgent" → "Both cases" | pass | FLAG: S1 stress "a different path" | FLAG: S2 "its Auto local gate": "its" follows the subject "background reflection" but means Letta; S4 "it should have been shared" has no singular antecedent (S3 "Shared-memory changes") | FLAG: S2 tells the merge ("merges them back automatically") before the review that precedes it ("before the edit is applied") | pass | pass | FLAG: S2 (61 words) chains a semicolon, a relative clause "which is the basis for its Auto local gate" and a coordinated counterfactual "and with that option off the system would sit in [None × None]"; S4 object "whether it should have been shared" interrupts "leaving ... unresolved" | FLAG: S1 ends "a different path" | FLAG: S2 "in the released evidence" (vague) | pass | pass (note: no hard-rule error, but S2's punctuation has to carry three clauses) | FLAG: tacked-on chain (S2); tidy antithesis S7 "one shares without checking; the other does not share" (deliberate, but counts toward the cap) |
| VI:11 | body (evidence) | pass (S1 ends "independently of these learning loops") | FLAG: S5 "The portable file does not necessarily carry the history that produced it" restates S4 and VI:1 S2 ("Copying the file transfers the instruction, but not the evidence") | FLAG: subjects "Much of the infrastructure" → seven-product list → "This convergence" → "A study" → "the runtime state of the adaptation process" → "The portable file" | pass | pass | pass (note: S3 "This convergence" summarizes S2; S1 "these learning loops" reaches across a subsection) | pass | FLAG: S2 verb "use" at word 14 after the seven-product list | FLAG (mild): S4 "the runtime state of the adaptation process" | pass | FLAG: S5 ends on pronoun "produced it" | pass | pass | pass | pass |
| VI:12 | body (evidence) | FLAG: S1 ends "human admission", which frames S1–S2 only; S3–S5 turn to MCP registries, control planes and governance registries, and the claim that ties them is S5's last clause | pass | FLAG: subjects "Public repositories" → "every substantive change" → "only one of 254 edits" → "MCP registries" → "control planes" → "Governance registries" → "EDDOps" → "none of these registries" | FLAG: S3 opens on new "MCP registries" | pass (close: see 2.1) | FLAG: S5 "none of these registries": EDDOps is not one of the registries named, and it is unclear whether public repositories are included | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: feature-list voice "provide ... provide ... add ... add" (house style: kill the feature-list voice) |
| VI:13 | body (evidence) → point | pass (S1 ends on "rollback") | FLAG: S4 "These platforms supply much of the machinery for controlled change without closing the failure-driven local loop" restates S3, VI:12 S5 and the Introduction ("substantial versioning and release machinery without any process that proposes changes from deployment experience") | pass (close: "Braintrust, Vellum, and LangSmith Hub" → "Engineers" → "evaluations" → "session feedback" → "These platforms") | pass | pass | FLAG (mild): S2 "the candidates" is presented as old; no candidates have been named for these platforms | pass | pass | FLAG: S3 "trigger candidate generation"; S4 "the machinery for controlled change" | pass | pass | pass | pass | pass | FLAG: capability voice "provide", "supply" |
| VI:14 | transition | n/a: short transition (3 sentences, 47 words) | pass | pass (note: housekeeping subjects "Fig.", "Table", "The grid") | pass | n/a: short transition | pass | pass | pass | FLAG: S3 "while allowing their complementary capabilities to be compared" | FLAG: S3 tacked-on "-ing" clause "while allowing ..." | FLAG: S3 ends on passive "to be compared" | pass | pass | pass | FLAG: capability voice "allowing" |
| VI:15 | body → point | pass (S1 ends "exact checks or simulated outcomes") | FLAG: S2 "The judged and delayed cases use pruning, rewriting, or merging rather than that estimate" restates VI:8 and V:18 S2; S1 and S3 restate Table VII-1's "Signal found there" column | FLAG: subjects "the operative signals" → "The judged and delayed cases" → "[Auto × Human]" → "These patterns" | pass | FLAG: the opening's stress names signals, but the paragraph's theme (the grid matches the feedback expectations) first appears in S4 | pass | pass | FLAG: S1 subject comes after an 11-word phrase; main verb "are" at word 16 | FLAG: S4 "once the meaning of automatic admission is made explicit" | pass | FLAG: S2 ends on the pointer "that estimate"; S4 ends "made explicit" | pass | pass | pass | FLAG: point-last summary |
| VI:16 | body (evidence) | FLAG: S1 frames the empty human-local cells; S3–S4 move to "the bottom row" and [None × None] without a frame (three claims) | FLAG: S1 restates the Table VII-1 caption ("[Human × Auto] and [Human × Human] hold no surveyed system"); S4 restates V:8 S3 on SkillRL and the table row | FLAG: subjects "The [Human × Auto] and [Human × Human] cells" → "no system" → "Human local decisions" → "The bottom row" → "SkillRL and SkillForge" | FLAG: S3 opens on new "The bottom row"; S4 on "SkillRL and SkillForge" | pass | FLAG: S3 "The bottom row" is ambiguous: in Table VII-1 the bottom row is [None × None] (SkillRL, SkillForge), which do have failure-driven loops; in Fig. 3 it is the whole None-local row (AUTHOR FLAG 6) | pass | pass | FLAG: S2 "Human local decisions occur in curation" | FLAG: S4 appositive "new skills in SkillRL and rewrites in SkillForge" interrupts subject and verb | pass | pass | pass | pass | pass |
| VI:17 | point (section close) | FLAG: S1 ends on the pointer "this structure"; the section's point (S5 "a division of capabilities") is the paragraph's last sentence | pass (note: S4–S5 restate the Introduction and abstract finding deliberately, as the section's point) | FLAG: subjects "The audit's boundary cases" → "five" → "Spotify" → "The sixth" → "No relaxation" → "What the grid reveals" → "no system" | FLAG: S2 opens on new "Of six systems that promote without artifact lineage" | FLAG: S1 stress "this structure" | pass (note: "this structure" resolves to the grid of VI:15–VI:16; "the audit", "the tier rule" and "T5" rely on Section III, see 4.15) | pass | pass | FLAG: S4 "No relaxation yields governed promotion" | pass (note: S2 appends "Spotify is one of them" after a semicolon) | FLAG: S1 "this structure"; S2 ends on pronoun "one of them" | pass | pass | pass | FLAG: colon reveal "What the grid reveals is a division of capabilities:"; the section's main point follows a robustness note (point-last) |

## (b) Flags only: other paragraph-level tests, captions and tables

| ¶ | test | finding (quote the words) |
|---|---|---|
| V (section) | 2.2 | The section's consequence (what the classes predict for the two loops) arrives only in V:17. The opening's last sentence is housekeeping, "We divide the surveyed systems into four feedback classes, summarized in Table REF(tab:IV-1)"; the point sentence is V:2 S3. |
| V:2 | 2.3 | One concept, three names: section title "feedback", S2 "evidence", S3 "signal", S4 "feedback classes", table caption "feedback-signal classes". |
| V:3 | 4.5 | S1 passive on the writer's own method, "The classes are assigned by the constraint that binds first" (doer: we). |
| V:4 | 4.7 | Invented noun string "a sandboxed compile-and-edit functionality check". |
| V:6 | 2.4 | The framing sentence announces "Two problems", but S2 gives two (attribution, overfitting) and S3 adds a third with "also" ("Cheap acceptance can also allow the artifact pool to grow"); the real frame is S4 at the end (AUTHOR FLAG 1). |
| V:6 | 2.3 / 4.15 | "lifecycle management" (S4) is unglossed, and the same idea is called "grow without sufficient pruning" (S3) and "bloat" (V:17 S6). |
| V:6 | 3.5 | S3 "also" is additive. |
| V:8 | 2.2 | Point-last: S4 "The same kind of outcome can therefore support different operations in different systems". |
| V:8 | 3.5 | S4 "therefore" asserts a conclusion, but S4 generalizes S1–S3 rather than following from them. |
| V:8 | 1.5 (placement) | SAGE appears as a real observed-outcome example ("SAGE measures task success in AppWorld") one paragraph before V:9 says AppWorld outcomes are simulated and a distinct case. |
| V:9 | 2.4 (house: one claim) | Two claims: simulated outcomes as a subcase (S1–S2); what a gate needs under noisy outcomes, and what it still cannot learn (S3–S4). |
| V:9 | 4.6 | S2 passive on the writer's own classification, "They are treated as a distinguishable case within C2". |
| V:10 | 2.4 (house: one claim) | Two claims: promotion is harder (S1–S2); C2 channels can be poisoned (S3). |
| V:10 | 4.2 | S2 hides the sender in a possessive, "A sender's successful outcome". |
| V:10 | 4.13 | S3 "connecting the reliability of feedback ..." attaches to the whole clause; it is unclear what connects. |
| V:10 | 6.4 | S3 "channels that can carry poisoned memories or injected tool instructions" has no citation here (AUTHOR FLAG 8). |
| V:11 | 4.12 | S3 joins a system (CASCADE) and an unattributed repository practice ("a reviewer approves promotion into Anthropic's skills repository") with "and". |
| V:11 | 6.4 | S3 "a reviewer approves promotion into Anthropic's skills repository" has no citation (AUTHOR FLAG 8). |
| V:11 | 5.3b | S4 never states the consequence that SkillForge's judge triggers rewrites but does not gate acceptance; VI:16 relies on it ("rewrites in SkillForge, are kept unchecked"). |
| V:13 | 5.2 | S6 "This reflexive gate is developed in Section REF(sec:reflexive)" is a legitimate signpost, but it is the paragraph's last sentence (see 4.14). |
| V:14 | 1.6 (illustration) | "The AI Scientist illustrates the broad setting by generating ideas, conducting experiments, and writing a paper": the case shows a research workflow, not the delay of weeks or months across many scaffold edits that S1 and S3 claim. Close call; the sentence claims only "the broad setting" (AUTHOR FLAG 3). |
| V:14 | 2.3 | "edits" (S1) / "scaffold change" (S3). |
| V:15 | 1.5 / 2.4 (house: one claim) | S5, the boundary note "AlphaEvolve's archive diversity does not make it a delayed-signal example", belongs with the assignment rule (V:3) or the C1 subsection (V:4), not at the close of C4. |
| V:15 | 4.15 | "on a heartbeat" is unglossed jargon. |
| V:16 | 2.3 / 4.15 | "harness optimizers" uses "harness" for what the paper calls the scaffold (also VI:5 "a shared harness"); it may be the cited source's term (AUTHOR FLAG 13). |
| V:17 | 2.3 | "either half" (S5) against "the two loops" (heading); Table VII-1 also uses "close both halves". |
| V:17 | 4.8 | S4 whole subject with a relative clause, "automatic promotion that estimates a loss change". |
| V:17 | 4.12 / 4.13 | S4 "in exact and re-runnable simulated settings": unclear whether these are two kinds of setting or one, and what the phrase modifies. "human promotion should hold the observed outcomes and judgments": the verb "hold" leaves the relation unclear (AUTHOR FLAG 11). |
| V:18 | 2.4 (house: one claim) | Two claims: the expectations concern evidence, not executability (S1–S3); sharing stays an empirical question (S4). The section ends on a caveat (house rules: "End sections clean"; "Honest accounting goes in one place"). |
| V (section) | AI cap | Antitheses: V:5 S1, V:6 S4, V:9 S4 (that/why), V:18 S1, which is 4 in about 1,350 words (cap about 3). |
| Table IV-1 caption | cross-ref | The caption reads "Table IV-1." and the label is tab:IV-1, but the table sits in Section V (AUTHOR FLAG 2). |
| Table IV-1 caption | 2.3 | The caption's "what it cannot fix" does not match the column header "What stays hard"; the caption skips the "Corpus examples" column. |
| Table IV-1, C1 row, "What the gate can be" | 4.12 | Faulty coordination: "An automatic check, run over enough cases, and enough repeated runs of a stochastic agent, to sample the task mix" ("run over enough cases, and [over] enough repeated runs"). |
| Table IV-1, C1 row, "What stays hard" | 4.15 | "The lift" is unglossed; the prose never uses "lift". |
| Table IV-1, C2 row | 1.5 | Sierra is listed as a C2 example, but the C2 prose never mentions Sierra; VI:9 describes it only as human-routed promotion (AUTHOR FLAG 10). |
| VI (section) | 2.2 / 1.8 | The section opening (VI:1) says sharing needs a separate decision; the section's finding, "no system has both the learning of the top row and the governance of the bottom row", arrives in the last sentence of VI:17. The heading "When a local improvement is shared" names a situation, not the finding. |
| VI:2 | 4.12 | The definitions are not parallel: "USER covers", "PROJECT covers", "STACK is a team's", "A TENANT is", "CORE is the scope". |
| Fig. 2 caption | 2.5 | "Wider adoption changes the population on which an edit acts" duplicates VI:2 S7, and "Receiving-side evaluation checks whether the improvement is supported for the recipient" duplicates VI:3 S4. |
| VI:5 | 4.15 | "aggregator" is unglossed; "harness" is used for scaffold (S2). |
| VI:6 | 4.15 | "graphs" (S3) is unexplained (AUTHOR FLAG 7). |
| VI:7 | 2.2 | Point-last: S5 "That pool is as far as any of them travels, and none has access control, audited promotion, or a gate at a receiving organization". |
| VI:7 | 4.13 | S1 "a bank or archive that later runs reuse" is a garden path ("runs" read as the verb). |
| VI:7 | 6.4 | S4 "AlphaEvolve has produced gains used within Google" has no citation in its own sentence (S3 cites alphaevolve2025) (AUTHOR FLAG 12). |
| VI:8 | 4.7 | Noun strings "per-edit improvement estimate" and "automatic promotion decision". |
| VI:8 | 4.8 | S2 whole subject of 15 words of nominalizations: "NanoResearch's semantic merge, AutoManual's judged rewriting and consolidation, and ShareMem's judged consolidation". |
| VI:8 | 6.4 | AutoManual is named without a citation in either file (AUTHOR FLAG 8). |
| VI:9 | 4.2 | S2 "Sierra routes generated insights through human-authored expert answers" does not say who makes the promotion decision; the person hides in "human-authored". |
| VI:9 | 6.3 | S6 "makes a program on the local gate with a person on the promotion gate the production-viable pairing rather than a compromise": the claim is stronger than four cases support (AUTHOR FLAG 4). |
| VI:9 | 3.5 | S5 "also" is additive. |
| VI:10 | 2.4 (house: one claim) | Two systems and two claims (Letta shares without checking; AutoAgent does not share), joined only by S7. |
| VI:10 | 4.5 | S3 passive "Shared-memory changes are then pushed" (doer Letta, recoverable). |
| VI:10 | 4.13 | S2 "which is the basis for its Auto local gate" attaches either to "an optional agent review" or to the whole clause. |
| VI:10 | 6.2 / 6.4 | Plain paraphrase: Letta's Auto label rests on an optional review ("with that option off the system would sit in [None × None]"). That is a scoring note inside the prose. Letta is not cited in the paragraph (AUTHOR FLAG 5). |
| VI:11 | 4.15 / 5.6 | "MCP" is not glossed in these files (it may be defined earlier); "markdown" should be capitalized as "Markdown". |
| VI:12 | 1.5 | The relevance of S2's "only one of 254 edits deprecated a skill" to "a shared scope with human admission" is not stated. |
| VI:12 | 6.4 | "EDDOps" has no citation (AUTHOR FLAG 8). |
| VI:12 | 2.2 | Point-last: S5 "none of these registries generates candidate artifacts from failures". |
| VI:13 | 2.2 | Point-last: S4. |
| VI:14 | 5.2 | Two of three sentences are figure and table pointers ("Fig. REF(fig:design) places ...", "Table REF(tab:VII-1) summarizes ..."). |
| Table VII-1 caption | cross-ref | The caption reads "Table VII-1." and the label is tab:VII-1, but the table sits in Section VI (AUTHOR FLAG 2). |
| Table VII-1 header | 2.3 | "who lets it climb" introduces "climb" for promote; the prose uses "promote" and "travels" (VI:7 S5). |
| VI:15 | 3.4 | 11 words before the subject: "Among [Auto × Auto] systems whose promotion gate estimates a loss change,". |
| VI:15 | 2.2 | Point-last: S4 "These patterns match the feedback-based expectations". |
| VI:16 | 2.4 (house: one claim) | Three claims: the human-local cells are empty; the bottom row holds comparison systems; SkillRL and SkillForge sit in [None × None]. |
| VI:16 | 4.15 | "curation" is used as a category without a gloss. |
| VI:17 | 4.15 | "The audit", "the tier rule", "T5 evidence" and "when the audit is relaxed" are not defined in V–VI; the reader needs a pointer to Section III. |
| VI:17 | 1.5 | The section's main point (S5) is placed as the last sentence of a boundary-case paragraph. |
| VI (section) | AI cap | Antitheses: VI:1 S2, VI:5 S4, VI:9 S6, VI:10 S7, VI:17 S5, which is 5 in about 1,300 words (cap about 3). |
| V, VI | 4.16 | pass: sentence lengths range from about 6 to 61 words in both sections. |

## (c) Suggested moves, one per FLAG

**Section V**
- V:1 2.1: let the stress of the last vignette sentence, or a short following clause, carry "evidence for accepting an edit", or merge V:1 into V:2.
- V:1 2.5: keep one set of four cases. Either point back to the Introduction's cases and drop the vignette, or keep the vignette and have the Introduction name the cases more briefly (an author decision across sections).
- V:1 4.14: end each vignette sentence on its timing or judgment feature (move "later" and "months" to the stress).
- V:1 AI: vary one or two of the four sentence frames, or compress the four into two sentences.
- V:2 3.1: make the feedback signal the subject of S2–S4.
- V:2 3.2: introduce "signal" as the old term ("evidence, which reaches the gate as a feedback signal") before S3 uses it.
- V:2 4.1: open S3 on a short subject ("How soon the signal arrives, ...") or split it.
- V:2 4.3: verbalize "dependence on judgment" ("whether it depends on someone's judgment").
- V:2 4.14: end S2 on the noun ("evidence for accepting the edit") and move the table pointer into a parenthetical earlier in S4.
- V:2 AI: fix one name for the concept ("feedback signal") and use it in the title, body and caption.
- V:3 4.1: make "we" the doer in S1, and make S3 parallel with S2 ("Among timely signals, a signal with no independent ground truth is C3").
- V:3 4.3: same as 4.1 for S3.
- V:3 4.14: end S5 on "the signal that supports that decision" or on "operative signal".
- V:4 3.1: keep the exact check as the running topic, for example "Exact evaluators score AlphaEvolve's candidates ...", or accept the system tour with one framing clause.
- V:4 3.7: name the broader benchmark in S5, or say "DGM's full benchmark score".
- V:4 4.3: "DGM decides more narrowly: it keeps ..."; "SkillOpt evaluates on held-out exact-match items".
- V:4 4.14: reorder S2 so it ends on "an automatic gate".
- V:5 2.5: cut S4 or merge it into S1; state the scope limit once (Section II) and point back to it.
- V:5 3.1: make "the check" or "the suite" the subject of most clauses.
- V:5 3.2: put "that variation" first in S3 ("That variation must be accounted for when ...").
- V:5 3.7: name both sources (stochastic outputs and a finite sample of tasks) or split S2.
- V:5 4.1: replace the gerund subjects with characters (the check, the agent, the gate).
- V:5 4.3: "the gate must account for that variation when it estimates ...".
- V:5 4.14: trim "as a whole"; end S4 on something other than a repeat ("only what it tests").
- V:5 5.1: cut "as a whole" and "also".
- V:5 AI: keep at most one antithesis in this subsection.
- V:6 2.1: name the problems in S1 (subject to AUTHOR FLAG 1 on the count).
- V:6 3.1: make exact feedback, or the checker, the subject of S2–S3.
- V:6 3.2: introduce "cheap acceptance" from old material ("Because acceptance is cheap, ...").
- V:6 3.6: end S1 on the problem names.
- V:6 4.1: verbalize "Cheap acceptance" and "repeated optimization".
- V:6 4.3: "Exact feedback makes it easier to evaluate an edit, but not to attribute a failure or to prune the pool".
- V:6 4.14: end S2 on "the suite" as a noun phrase ("can overfit the scaffold to that suite").
- V:6 5.1: cut "also"; replace "sufficient" with what the pruning lacks.
- V:6 AI: replace "allow ... to grow" with the mechanism (who adds and who fails to remove); keep only one antithesis.
- V:7 2.5: point to the table row instead of listing the outcomes again, or vary the examples.
- V:7 4.1: shorten the list subject or move it after the verb ("An episode can end in an observable result: ...").
- V:7 4.3: "An episode ends in an observable result".
- V:7 5.1: replace "meaningful" with what makes the result informative (it is real) or cut it.
- V:8 2.1: open on the claim (S4) and let the systems follow as instances.
- V:8 3.1: with the claim first, make "the outcome" the running topic ("Devin reads it as feedback; SAGE ...").
- V:8 3.6: end the opening sentence on "different operations".
- V:8 4.14: end S4 on "operations", or drop the second "different".
- V:8 AI: move the generalization to the front and drop "therefore".
- V:9 2.5: cut S4 or point to the table; alternatively keep S4 and simplify the table cell.
- V:9 3.1: split the paragraph at S3 (simulated subcase / requirements of the gate).
- V:9 4.1: move "such as ... AppWorld" to the end or into its own sentence.
- V:9 4.9–4.11: same as 4.1.
- V:9 5.1: replace "distinguishable" with "a separate"; cut "more generally".
- V:9 5.3: flag for the author whether "usually" or "more readily" carries the claim; keep one.
- V:10 2.5: keep the receiving-side caveat at one home (Section II or VI:1) and point to it here.
- V:10 3.1: split S3 (poisoned channels) into its own paragraph, or move it to the failure-modes section.
- V:10 4.3: "does not evaluate the recipient"; "so feedback is only as reliable as its source".
- V:10 4.9–4.11: split S3 into two sentences.
- V:10 5.1: cut "also".
- V:10 AI: replace the trailing "connecting ..." with its own sentence.
- V:11 3.1: keep "the gate" or "the judge" as the subject (for example "CASCADE's gate combines a human and an agent ...").
- V:11 3.7: say what SkillForge's judge comes earlier than (the acceptance gate) and what that means.
- V:11 4.14: end S2 on "preference" ("no independent exact answer exists for the preference measured").
- V:12 3.1: make "the judge" the running subject.
- V:12 3.7: state the distinction (calibrated versus uncalibrated judge) before calling it "this distinction".
- V:12 4.3: "we are less sure what its acceptances mean".
- V:12 4.9–4.11: split S1 after "these decisions"; put "calibrated" at the stress.
- V:12 4.14: end S2 on the noun it qualifies.
- V:13 2.1: open on the theme ("A judge can be gamed, and it can move").
- V:13 3.1: keep "the judge" (or "the gate's instrument") as the subject across S2–S5.
- V:13 3.2: put "This proxy overoptimization" first in S3.
- V:13 3.6: same as 2.1.
- V:13 3.7: drop "another", or name the first risk.
- V:13 4.1: give S1 a concrete subject and verb ("A scaffold optimized against a judge can ...").
- V:13 4.3: same as 4.1.
- V:13 4.14: end S6 on "reflexive gate" (put the section pointer earlier or in parentheses).
- V:14 5.1: replace "meaningful" (or cut it) and "broad".
- V:15 2.5: state the per-edit credit problem once in C4 (V:14 S3 or V:16 S2) and let the others point to it.
- V:15 3.1: make "these systems" or "intermediate decisions" the running subject.
- V:15 3.2: move S5 to V:3 or V:4.
- V:15 4.1: same as 3.2; if S5 stays, open it on "AlphaEvolve's candidates".
- V:15 4.3: "decide at intermediate points".
- V:15 4.14: end S3 on "shared memory" (move "on a heartbeat" left); end the paragraph on C4.
- V:15 AI: move the boundary note out of the stress position.
- V:16 2.5: same as V:15 2.5; keep the "search versus descent" sentence, which the citation supports.
- V:16 3.1: make "the gate" or "the descent interpretation" the subject of S2–S3.
- V:16 4.3: "cannot show whether the loop improved by direction or by search".
- V:16 4.14: move the attribution left ("As the evaluation of harness optimizers emphasizes, ...").
- V:16 5.1: cut "also".
- V:17 2.5: drop S5, or fold it into S3; point to Table IV-1 for the failure risks instead of restating them.
- V:17 3.7: use "loops" or define "half" once.
- V:17 4.1: "Exact checks and observed outcomes support local automatic acceptance most directly".
- V:17 4.9–4.11: split S4 into one sentence per loop; place "in exact and re-runnable simulated settings" next to what it modifies.
- V:17 4.14: end S5 on "gate" (or cut S5).
- V:18 2.5: drop S4 here and let VI:1 carry the sharing caveat.
- V:18 3.1: keep "these expectations" or "the gate" as the subject.
- V:18 3.2: with S4 gone, the problem is gone.
- V:18 4.3: (if S4 stays) "before it can claim broader performance".
- V:18 4.14: (if S4 stays) end on "broader performance".
- V:18 5.1: replace "relevant" with the named cases or cut it.
- V:18 AI: end the section on the expectations (or on V:17's third expectation), not on a caveat.

**Section VI**
- VI:1 2.5: keep VI:1 as the section's opening but shorten it; point back to Section II's naming-rule example instead of restating it.
- VI:1 3.7: name the decision ("whether the recipient should adopt the edit") instead of "This".
- VI:1 4.14: end S2 on "evidence" ("but not the evidence that justified the instruction").
- VI:1 5.1: cut "relevant" or say which conditions.
- VI:2 2.5: keep the population claim in one place (Section II or VI:2) and trim the caption.
- VI:2 4.14: move the figure pointer to the front or into parentheses.
- VI:3 2.1: name the limit in S1.
- VI:3 3.1: make the receiving-side check (or the recipient) the running subject.
- VI:3 3.2: introduce the architecture from old material ("For that reason, the architecture proposed in Section ... includes ...").
- VI:3 3.6: same as 2.1.
- VI:3 4.1: replace "The nesting" with an actor or the averaging mechanism.
- VI:3 4.3: drop "makes ... visible".
- VI:3 4.14: end S1 on the limit; end S4 on "the receiving tenant".
- VI:3 5.1: cut "important".
- VI:3 AI: same as 5.1.
- VI:4 2.5: cut S5.
- VI:4 4.3: same as 2.5.
- VI:4 5.1: same as 2.5.
- VI:4 AI: same as 2.5.
- VI:5 3.6: end S1 on where the check sits ("at the aggregator, not the recipient").
- VI:5 3.7: repeat the noun ("Neither system instantiates ...").
- VI:5 4.14: same as 3.6.
- VI:6 2.5: drop S2's roll call; cut S4's restated limit, or point back to V:5.
- VI:6 3.1: make "the receiving-side check" the subject.
- VI:6 3.6: end S1 on "coverage".
- VI:6 3.7: say what the graphs are, or use the term already used for Evo2Team (AUTHOR FLAG 7).
- VI:6 4.1: "Where the evaluation runs matters, and so does what it covers".
- VI:6 4.3: verbalize "location", "confirmation" and "provides ... evidence".
- VI:6 4.14: end S1 on "coverage"; end S3 on the graphs left untested.
- VI:6 AI: with S2's roll call cut, the semicolon chain goes too.
- VI:7 3.2: use the S1 noun ("That archive") or name "pool" in S1.
- VI:7 3.7: same as 3.2; settle on one name for the shared store.
- VI:7 4.3: "decide programmatically"; "before admitting them to the archive".
- VI:7 4.14: "an archive that later runs reuse it", or "a bank or archive that later runs draw on".
- VI:7 AI: same as 3.2.
- VI:8 2.5: keep S1–S2 as evidence and replace S3 with a pointer to V:18, or cut V:18 S1–S2 and keep S3 here (one home).
- VI:8 3.1: make the systems the subjects ("NanoResearch merges semantically, AutoManual ... ; none estimates ...").
- VI:8 4.1: same as 3.1.
- VI:8 4.3: same as 3.1; "a program can decide to promote without estimating whether the edit improves".
- VI:8 5.1: cut "essential".
- VI:8 5.3: same as 5.1.
- VI:8 AI: same as 5.1; unpack the noun piles.
- VI:9 2.5: shorten the Devin and CASCADE sentences to clauses that point back.
- VI:9 3.1: make "a person" the subject of the instances ("In Sierra, experts author ...; in Devin, a reviewer's merge ...").
- VI:9 4.9–4.11: split S6 and put the claim in a short main clause.
- VI:9 4.14: end S6 on the positive claim.
- VI:9 5.3: the author decides how strongly to state S6 (AUTHOR FLAG 4).
- VI:9 AI: same as 4.9–4.11.
- VI:10 2.1: open on the shared claim (None at promotion, for two reasons), then Letta, then AutoAgent; or split into two paragraphs.
- VI:10 2.5: cut S4 or merge it into S3.
- VI:10 3.1: keep Letta as the subject of S1–S4.
- VI:10 3.6: same as 2.1.
- VI:10 3.7: "Letta's Auto local gate"; "whether those changes should have been shared".
- VI:10 3.8: tell the review before the merge.
- VI:10 4.9–4.11: split S2 into two or three sentences; move the counterfactual to a note or a footnote (AUTHOR FLAG 5).
- VI:10 4.14: same as 2.1.
- VI:10 5.1: say which evidence ("in the released documentation").
- VI:10 AI: same as 4.9–4.11.
- VI:11 2.5: cut S5, or fold it into S4.
- VI:11 3.1: make the artifacts or formats the running subject.
- VI:11 4.1: "Seven tools use git-tracked Markdown artifacts ...: Claude Agent Skills, ...".
- VI:11 4.3: "the runtime state of the adaptation" or "how the loop's state evolved".
- VI:11 4.14: end S5 on "history".
- VI:12 2.1: open on the shared claim (these scopes provide admission and lineage, but none generates candidates from failures).
- VI:12 3.1: make the registries or repositories the running subject.
- VI:12 3.2: introduce MCP registries from old material ("Registries add ...").
- VI:12 3.7: name the set "none of these" refers to; handle EDDOps separately.
- VI:12 AI: replace "provide/add" with what each mechanism does.
- VI:13 2.5: cut S4, or keep S4 and cut S3; one statement of the gap.
- VI:13 3.7: "Engineers author the candidate prompts".
- VI:13 4.3: "session feedback does not generate candidates or start a release".
- VI:13 AI: say what the platforms do (store versions, block releases, roll back).
- VI:14 4.3: "and lets the reader compare them" or cut the clause.
- VI:14 4.9–4.11: same as 4.3.
- VI:14 4.14: end on "capabilities".
- VI:14 AI: same as 4.3.
- VI:15 2.5: cut S2, or point back to VI:8.
- VI:15 3.1: make "the grid" or "the cells" the running subject.
- VI:15 3.6: open on the claim (the grid matches the feedback expectations), then give the two cells as evidence.
- VI:15 4.1: shorten the opening phrase ("In [Auto × Auto], where promotion estimates a loss change, ...").
- VI:15 4.3: "once we separate automatic admission from loss estimation".
- VI:15 4.14: end S2 on "estimate of loss change"; end S4 on "expectations".
- VI:15 AI: same as 3.6.
- VI:16 2.1: split into two paragraphs, empty human-local cells and the None-local row; or open with a frame naming both.
- VI:16 2.5: cut S1's restatement of the caption, or trim the caption; point back to V:8 for SkillRL.
- VI:16 3.1: make the cells or rows the running subject.
- VI:16 3.2: with a frame naming the bottom row, the new topic becomes old.
- VI:16 3.7: name the row by its label (the None-local row) instead of "bottom" (AUTHOR FLAG 6).
- VI:16 4.3: "Only curators decide locally by hand".
- VI:16 4.9–4.11: move the appositive into its own clause after the verb.
- VI:17 2.1: move S5 (the division of capabilities) to its own closing paragraph or to the section opening; open VI:17 on the boundary cases by name.
- VI:17 3.1: keep "the boundary cases" or "the six systems" as the subject of S1–S4.
- VI:17 3.2: open S2 on old material ("Six boundary systems promote without artifact lineage").
- VI:17 3.6: end S1 on "the grid's structure", or on the result.
- VI:17 4.3: "Relaxing the audit does not produce governed promotion across organizations".
- VI:17 4.14: end S1 on its result; end S2 on "Spotify" ("one of them is Spotify").
- VI:17 AI: state the division of capabilities as a plain claim without the "What X reveals is" frame.

## (d) Role-level verdict per paragraph

Passage tests counted: 2.5, 3.1, 3.2, 3.6, 3.7, 3.8. A paragraph is re-drafted if it fails a role-level test or three or more passage tests.

| ¶ | role-level test failed / passage tests failed | verdict |
|---|---|---|
| V:1 | 1.2 prelude gate: close pass (one paragraph, maps to C1–C4, hands off to V:2; but it duplicates the Introduction's cases, see 2.5); passage fails 1 (2.5) | keep-and-polish |
| V:2 | none; passage fails 2 (3.1, 3.2) | keep-and-polish |
| V:3 | none; 0 | keep-and-polish |
| V:4 | none; 2 (3.1, 3.7) | keep-and-polish |
| V:5 | none; 4 (2.5, 3.1, 3.2, 3.7) | re-draft |
| V:6 | none (but the count is wrong, AUTHOR FLAG 1); 3 (3.1, 3.2, 3.6) | re-draft |
| V:7 | none; 1 (2.5) | keep-and-polish |
| V:8 | none (1.5 SAGE placement noted); 2 (3.1, 3.6) | keep-and-polish |
| V:9 | none; 2 (2.5, 3.1) | keep-and-polish (split at S3 per house one-claim rule) |
| V:10 | none; 2 (2.5, 3.1) | keep-and-polish (move S3 out) |
| V:11 | none; 2 (3.1, 3.7) | keep-and-polish |
| V:12 | none; 2 (3.1, 3.7) | keep-and-polish |
| V:13 | none; 4 (3.1, 3.2, 3.6, 3.7) | re-draft |
| V:14 | 1.6 illustration: close call (AI Scientist shows the setting, not the delay; AUTHOR FLAG 3); 0 | keep-and-polish |
| V:15 | 1.5 placement: S5 boundary note misplaced (a sentence, not the paragraph); 3 (2.5, 3.1, 3.2) | re-draft |
| V:16 | none; 2 (2.5, 3.1) | keep-and-polish |
| V:17 | none; 2 (2.5, 3.7) | keep-and-polish |
| V:18 | none; 3 (2.5, 3.1, 3.2) | re-draft |
| VI:1 | none; 2 (2.5, 3.7) | keep-and-polish |
| VI:2 | none; 1 (2.5) | keep-and-polish |
| VI:3 | none; 3 (3.1, 3.2, 3.6) | re-draft |
| VI:4 | none; 1 (2.5) | keep-and-polish |
| VI:5 | none; 2 (3.6, 3.7) | keep-and-polish |
| VI:6 | none; 4 (2.5, 3.1, 3.6, 3.7) | re-draft |
| VI:7 | none; 2 (3.2, 3.7) | keep-and-polish |
| VI:8 | none; 2 (2.5, 3.1) | keep-and-polish |
| VI:9 | none; 2 (2.5, 3.1) | keep-and-polish |
| VI:10 | none; 5 (2.5, 3.1, 3.6, 3.7, 3.8) | re-draft |
| VI:11 | none; 2 (2.5, 3.1) | keep-and-polish |
| VI:12 | 1.5 relevance of S2's deprecation count unstated (a sentence); 3 (3.1, 3.2, 3.7) | re-draft |
| VI:13 | none; 2 (2.5, 3.7) | keep-and-polish |
| VI:14 | none; 0 | keep-and-polish |
| VI:15 | none; 3 (2.5, 3.1, 3.6) | re-draft |
| VI:16 | none; 4 (2.5, 3.1, 3.2, 3.7) | re-draft |
| VI:17 | 1.5 placement: the section's main point sits in the last sentence of a boundary-case paragraph; 3 (3.1, 3.2, 3.6) | re-draft |

Re-draft: V:5, V:6, V:13, V:15, V:18, VI:3, VI:6, VI:10, VI:12, VI:15, VI:16, VI:17 (12 of 35).

## AUTHOR FLAGS (fixes that would touch a claim, number, citation, quotation or cross-reference)

1. **V:6 S1 "Two problems remain even with a reliable checker."** S2–S3 describe three: failed tests that do not identify the cause, overfitting to the suite, and an artifact pool that grows without pruning ("Cheap acceptance can also ..."). The count is the author's to fix: either "Three problems", or treat pool growth as a separate point.
2. **Table labels.** Section V's table is captioned "Table IV-1" (label tab:IV-1), and Section VI's is captioned "Table VII-1" (label tab:VII-1). They look like leftovers from the earlier section numbering. Confirm how the IEEE build numbers and refers to them; these are cross-references, so the author changes them.
3. **V:14 S2, The AI Scientist [@lu2024aiscientist].** It is offered to illustrate "the broad setting" of delayed outcomes. It shows a research workflow, but not weeks-long delays across many scaffold edits. Choosing the example is a citation decision.
4. **VI:9 S6 "the production-viable pairing rather than a compromise".** This evaluative claim is stronger than the four cases support (Sierra's mechanism, "routes generated insights through human-authored expert answers", does not plainly show a person at a promotion gate). The author should calibrate it.
5. **VI:10 S2, Letta's classification.** The Auto local gate rests on an optional review ("with that option off the system would sit in [None × None]"). This is a scoring claim, and Letta's Context Repositories carry no citation in the paragraph.
6. **VI:16 S3 "The bottom row includes comparison systems without a failure-driven local loop" and VI:17 S5 "the learning of the top row and the governance of the bottom row".** Row orientation depends on Fig. 3. [None × None] contains SkillRL and SkillForge, whose local loops are failure-driven (VI:16 S4), so "bottom row" can be read two ways. Confirm the wording against the figure.
7. **VI:6 S3 "nearly a fifth of confirmed transfers fail on graphs not covered by confirmation".** The number and the term "graphs" come from the Evo2Team source; confirm what the graphs are before rephrasing.
8. **Citations missing in the sentence** (they may be cited elsewhere in the paper): V:10 S3 (poisoned memories, injected tool instructions); V:11 S3 (review of Anthropic's skills repository); VI:8 S2 (AutoManual); VI:10 (Letta Context Repositories); VI:12 S5 (EDDOps).
9. **V:8 S2 SAGE.** SAGE is cited as an observed-outcome example, while V:9 says its AppWorld outcomes are simulated and a distinct case. Classification placement is the author's call.
10. **Table IV-1, C2 row.** Sierra is listed as a C2 example; the prose describes Sierra only as human-routed promotion (VI:9). Confirm the classification.
11. **V:17 S4 "human promotion should hold the observed outcomes and judgments".** The verb's meaning determines the expectation being tested. The author should state the intended relation (for example, "should be where observed outcomes and judgments are promoted").
12. **VI:7 S4 "AlphaEvolve has produced gains used within Google".** Confirm that [@alphaevolve2025] in S3 supports it, or add the citation to S4.
13. **"harness" (V:16 S3, VI:5 S2).** This may be the cited sources' term (ong2026harnesseval, nie2026evolvenet). Replacing it with "scaffold" could misdescribe the source, so the author decides.

## Group C (V, VI): R-2 reverse outline

# Reverse outline C: Sections V (feedback classes) and VI (promotion)

Paragraph numbers match `ledger_C.md`. "Tests failed" lists every FLAG for the paragraph: the mandatory ledger columns plus the flags-only table.

## Paragraphs

| ¶ | role | its point in one sentence | protagonist | themes | evidence | words | tests failed |
|---|---|---|---|---|---|---|---|
| V:1 | prelude | Four assistants can each edit the scaffold, but each learns whether the edit helped at a different speed and from a different kind of signal. | four assistants (coding, scheduling, marketing, research) | feedback timing; kind of signal | none (vignette; repeats the Introduction's four cases) | 58 | 2.1, 2.5, 4.14, AI |
| V:2 | point | The timing, exactness and judgment-dependence of the feedback signal determine how well a gate can estimate an edit's change in loss, which gives four feedback classes. | the feedback signal (subject once) | evidence for acceptance; signal properties; four classes | Table IV-1 | 49 | 3.1, 3.2, 4.1, 4.3, 4.14, AI, 2.2 (section), 2.3 |
| V:3 | explanation (method) | A system's class is set by the first binding constraint, delay then ground truth then exactness, applied to the signal behind its operative acceptance decision. | the constraints | assignment rule; delay; ground truth; exactness | none | 73 | 4.1, 4.3, 4.14, 4.5 |
| V:4 | evidence | Exact checks decide a property immediately and repeatably, so automatic gates are easy to build; AlphaEvolve, SkillOpt and, more narrowly, DGM use them. | exact checkers, then systems | exact check; automatic gate; DGM's narrower retention rule | alphaevolve2025, yang2026skillopt, zhang2025darwin | 78 | 3.1, 3.7, 4.3, 4.14, 4.7 |
| V:5 | explanation (limit) | An exact check is exact about its output, not about the deployment: stochastic agents and finite suites still have to be sampled. | the check / suite (hidden in gerunds) | exactness of check vs deployment; variation; suite scope | none | 64 | 2.5, 3.1, 3.2, 3.7, 4.1, 4.3, 4.14, 5.1, AI |
| V:6 | problem | Even exact feedback does not attribute failures, guard against overfitting the suite, or prune a growing pool. | exact feedback (subject only in S4) | attribution; overfitting; pool growth / lifecycle | none | 58 | 2.1, 3.1, 3.2, 3.6, 4.1, 4.3, 4.14, 5.1, AI, 2.4, 2.3/4.15, 3.5 |
| V:7 | shared context | Observed outcomes are real results of an episode, but noisy and confounded. | the outcome | observed result; noise; confounding | none (repeats table C2 cell) | 53 | 2.5, 4.1, 4.3, 5.1 |
| V:8 | evidence | The same observed outcome supports different operations in different systems (feedback, success measure, failure signal, proposal trigger). | systems (Devin, SAGE, PACE, SkillRL) | uses of outcome feedback | cognition2025devinreview, wang2025sage, ling2026pace, skillrl2026 | 57 | 2.1, 3.1, 3.6, 4.14, AI, 2.2, 3.5, 1.5 |
| V:9 | explanation | Simulated outcomes remove the user confound; for real outcomes a gate needs a margin and enough episodes, and still learns *that* rather than *why* a task failed. | simulated outcomes, then the gate | simulation; margin and episodes; that-not-why | none | 67 | 2.5, 3.1, 4.1, 4.9–4.11, 5.1, 5.3, 2.4, 4.6 |
| V:10 | problem | Promotion under C2 is harder because a sender's outcome does not evaluate the recipient, and the outcome channel can be poisoned. | promotion, then "this class" | promotion; recipient difference; poisoned channels | none (S3 uncited) | 51 | 2.5, 3.1, 4.3, 4.9–4.11, 5.1, AI, 2.4, 4.2, 4.13, 6.4 |
| V:11 | shared context + evidence | Preference-dependent tasks are gated by people, rubrics or model judges, as in CASCADE, Anthropic's skills repository and SkillForge. | the gate, then systems | judged gate; no ground truth | huang2025cascade, skillforge2026 (repository review uncited) | 66 | 3.1, 3.7, 4.14, 4.12, 6.4, 5.3b |
| V:12 | point | A judge's score is evidence of a preference only after it is calibrated against people; the Auto label does not record calibration, and only three surveyed systems report it. | the judge / its score | calibration; Auto label; meaning of acceptance | skillforge2026, hu2026skillchain, zhu2026skillcoach | 73 | 3.1, 3.7, 4.3, 4.9–4.11, 4.14 |
| V:13 | problem | The judge is a moving and gameable target: scaffolds can overoptimize the proxy, human criteria drift, and editing the rubric creates a reflexive gate. | shifts (optimization, scaffold, research, evaluators, system) | proxy overoptimization; evaluator drift; reflexive gate | gao2023overoptimization, shankar2024validators; Section REF(sec:reflexive) | 73 | 2.1, 3.1, 3.2, 3.6, 3.7, 4.1, 4.3, 4.14 |
| V:14 | shared context / problem | In research and open-ended discovery the outcome arrives after weeks or months and many edits, so it cannot be credited to each edit. | the delayed outcome | delay; many intervening edits; credit | lu2024aiscientist | 47 | 5.1, 1.6 (close), 2.3 |
| V:15 | evidence + other view | C4 systems fall back on intermediate decisions (merging, heartbeat promotion) that prune but do not estimate each edit's contribution; AlphaEvolve's archive is C1, not C4. | C4 systems, then AlphaEvolve | intermediate decisions; no per-edit estimate; boundary of C4 | xu2026nanoresearch, qu2026coral, alphaevolve2025 | 73 | 2.5, 3.1, 3.2, 4.1, 4.3, 4.14, AI, 1.5/2.4, 4.15 |
| V:16 | explanation (limits) | Under C4, descent applies only to a proxy gate or a long-horizon evaluation; credit, drift and the search-versus-descent question remain open. | the descent interpretation | proxy gate; temporal credit; search vs descent | ong2026harnesseval | 59 | 2.5, 3.1, 4.3, 4.14, 5.1, 2.3/4.15 |
| V:17 | point | The classes predict three testable patterns: which signals support local automatic acceptance, which support automatic versus human promotion, and which failure risk dominates each class. | gate types (acceptance, promotion) | three expectations; local vs promotion; failure risks | Table IV-1 (implicitly) | 118 | 2.5, 3.7, 4.1, 4.9–4.11, 4.14, 2.3, 4.8, 4.12/4.13 |
| V:18 | other view + housekeeping | The expectations concern what a gate can establish, not what software can execute, and sharing always needs evidence at the recipient. | the expectations, then sharing | evidence vs execution; sharing as empirical question | Section REF(sec:design) | 73 | 2.5, 3.1, 3.2, 4.3, 4.14, 5.1, AI, 2.4 |
| VI:1 | shared context → point | Copying an edited file moves the instruction but not its evidence, so the recipient must share the evaluation conditions or test the edit itself. | the rule / recipient | transfer of evidence; recipient decision | none (restates Section II) | 54 | 2.5, 3.7, 4.14, 5.1, 2.2/1.8 (section) |
| VI:2 | housekeeping (definitions) | Five nested scopes run from USER to CORE; a wider scope pools the losses it contains, so promotion changes the population an edit should improve. | the scopes | scopes; aggregation; population | Fig. REF(fig:scope) | 70 | 2.5, 4.14, 4.12 |
| VI:3 | point | A lower average loss at a wide scope can hide harm to one recipient, so the proposed architecture adds a held-out check at the receiving tenant, separate from versioning and access control. | shifts (nesting, loss, architecture, controls, evaluation) | averaging hides harm; receiving-side check; delivery vs use | Section REF(sec:gap) | 59 | 2.1, 3.1, 3.2, 3.6, 4.1, 4.3, 4.14, 5.1, AI |
| VI:4 | evidence | ShareMem, XRepoSkill and Evo2Team already evaluate transfers in the receiving context within one operator. | the systems | within-operator transfer; receiving context | hu2026sharemem, guo2026xreposkill, wang2026evo2team | 59 | 2.5, 4.3, 5.1, AI |
| VI:5 | other view | Federated systems check at the aggregator or server, over clients under one operator, so they are not receiving-organization gates. | federated systems | check location; aggregator; one operator | nie2026evolvenet, yang2026federatedskill | 70 | 3.6, 3.7, 4.14, 4.15 |
| VI:6 | point | Where the check runs matters, and so does what it covers: even receiving-side confirmation in Evo2Team misses nearly a fifth of transfers on untested graphs. | shifts (location, systems, transfers, check) | location; coverage; finite evaluation | Evo2Team number (wang2026evo2team, cited in VI:4) | 69 | 2.5, 3.1, 3.6, 3.7, 4.1, 4.3, 4.14, AI, 4.15 |
| VI:7 | evidence → point | Research systems promote by admitting candidates to a shared bank or archive within one operator, and none adds access control, audited promotion or a receiving-organization gate. | research systems | archive admission; one operator; missing governance | yang2026skillopt, zhang2025darwin, hu2024adas, wang2023voyager, wang2025sage, alphaevolve2025, romeraparedes2024funsearch | 96 | 3.2, 3.7, 4.3, 4.14, AI, 2.2, 4.13, 6.4 |
| VI:8 | point | Automatic admission does not always mean a loss estimate: semantic merges and judged consolidations are programmatic but estimate no improvement. | admissions (nominalized) | evidentiary meaning of automatic admission | none in paragraph (NanoResearch, AutoManual, ShareMem named) | 58 | 2.5, 3.1, 4.1, 4.3, 5.1, 5.3, AI, 4.7, 4.8, 6.4 |
| VI:9 | evidence → interpretive point | Production systems keep a person at the promotion gate (Sierra, Devin, Spotify, CASCADE), standing in for the exact signal production lacks. | systems, then the person | person at promotion; production pairing | sierra2025os20, cognition2025devinreview, palumbo2026spotify, huang2025cascade | 112 | 2.5, 3.1, 4.9–4.11, 4.14, 5.3, AI, 4.2, 6.3, 3.5 |
| VI:10 | evidence | A None at promotion can mean sharing without a check (Letta's git-pushed shared memory) or no sharing at all (AutoAgent). | shifts (Letta, reflection, check, changes, record, AutoAgent) | ungated push; absent promotion; two meanings of None | wang2026autoagent (Letta uncited) | 138 | 2.1, 2.5, 3.1, 3.6, 3.7, 3.8, 4.9–4.11, 4.14, 5.1, AI, 2.4, 4.5, 4.13, 6.2/6.4 |
| VI:11 | evidence | Common git-tracked formats make artifacts portable between runtimes, but the history of the loop that produced them stays outside version control. | infrastructure / formats | portability; convergence; missing history | galster2026harnessconfig, barbaste2026harnessengineering, lulla2026loopengineering | 85 | 2.5, 3.1, 4.1, 4.3, 4.14, 4.15/5.6 |
| VI:12 | evidence | Public repositories, MCP registries, control planes and governance registries supply human admission, versioning, access control, lineage and rollback, but none generates candidates from failures. | repositories and registries | human admission; registry controls; no failure-driven generation | shen2026whomaintains, agenticcommunity2026mcpgateway, microsoft2026apicentermcp, truefoundry2026mcpgateway, kang2026registry, quessadavial2026acm, qin2026governed | 88 | 2.1, 3.1, 3.2, 3.7, AI, 1.5, 6.4, 2.2 |
| VI:13 | evidence → point | Prompt platforms supply versions, thresholds and rollback for engineer-authored changes, but session feedback starts neither candidate generation nor release. | the platforms | release machinery; engineer authorship; no failure-driven loop | braintrust2026docs, vellum2026docs, langsmith2026hub | 58 | 2.5, 3.7, 4.3, AI, 2.2 |
| VI:14 | housekeeping (transition) | Fig. 3 and Table VII-1 place every system on a grid of local gate by promotion gate, separating systems that generate and test edits from those that distribute human-authored artifacts. | the grid | gate grid; generation vs distribution | Fig. REF(fig:design), Table REF(tab:VII-1) | 47 | 4.3, 4.9–4.11, 4.14, AI, 5.2 |
| VI:15 | evidence → point | The occupied cells match the feedback expectations: automatic promotion with a loss estimate uses exact or simulated signals, and [Auto × Human] holds observed outcomes and judgments. | the cells / signals | signals per cell; match with V's expectations | Table VII-1 | 66 | 2.5, 3.1, 3.6, 4.1, 4.3, 4.14, AI, 3.4, 2.2 |
| VI:16 | evidence | No system pairs a human local gate with promotion; the None-local row holds comparison systems; SkillRL and SkillForge keep failure-driven updates unchecked. | the cells, then systems | empty human cells; comparison row; unchecked loops | jiang2026buildrix | 80 | 2.1, 2.5, 3.1, 3.2, 3.7, 4.3, 4.9–4.11, 2.4, 4.15 |
| VI:17 | point (section close) | The six boundary systems do not change the grid, and the grid shows a division of capabilities: no system combines failure-driven learning with cross-organization governance. | boundary cases, then the grid | audit robustness; division of capabilities | audit tier rule (Section III, by implication) | 84 | 2.1, 3.1, 3.2, 3.6, 4.3, 4.14, AI, 4.15, 1.5 |

## Sections and subsections

| section | its opening's point sentence, quoted | themes named | order | does the heading carry a theme? |
|---|---|---|---|---|
| V. What the feedback allows a gate to know | "The signal's timing, exactness, and dependence on judgment determine how well a gate can estimate the change in loss." (V:2 S3; the opening's last sentence is the housekeeping "We divide the surveyed systems into four feedback classes, summarized in Table REF(tab:IV-1).") | feedback signal; gate; estimating change in loss; four classes | coordinate (C1 to C4), then logical (consequences) | Yes, partly: "what the feedback allows a gate to know" names the theme as a question, not the claim. |
| V-A. Exact checks: C1 | "A compiler, proof checker, schema validator, or exact-match answer key can decide a specified property immediately and repeatably." | exactness; automatic gate; limits (scope, attribution, overfitting, pool growth) | logical (what it enables, then what it does not) | No: class label only. |
| V-B. Observed outcomes: C2 | "The result is meaningful but may be noisy or confounded." (V:7 S2) | noise; confounding; that-not-why; recipient difference; poisoning | logical | No: class label only. |
| V-C. Judgments: C3 | "For style, persuasion, design, or other preference-dependent tasks, a gate relies on a person, rubric, reference comparison, or model judge." | judge; calibration; proxy overoptimization; reflexive gate | logical | No: class label only. |
| V-D. Delayed and sparse outcomes: C4 | "Research programs and open-ended discovery may produce meaningful outcomes only after weeks or months and many intervening edits." | delay; per-edit credit; intermediate decisions; search vs descent | logical | No: class label only. |
| V-E. Consequences for the two loops | "The classification yields three expectations that can be checked against the corpus." | local acceptance; promotion; failure risks | coordinate (First, Second, Third), then a qualification | Partly: it names the two loops but not the expectations. |
| VI. When a local improvement is shared | "The recipient must either share the relevant evaluation conditions or test the change on its own workload." (VI:1 S3; S4 "This is the additional decision that separates local adaptation from promotion.") The section's finding, "no system has both the learning of the top row and the governance of the bottom row", is the last sentence of VI:17. | evidence transfer; receiving-side decision | logical (scopes, then who checks, who promotes, what infrastructure exists, the grid) | No: it names a situation, not the finding (division of capabilities). |
| VI-A. Scope and receiving-side evaluation | "We distinguish five nested scopes." (point at VI:3 S2: "A lower average loss at a broad scope can conceal harm to an individual recipient.") | scopes; receiving-side evaluation; location and coverage of the check | logical | Yes: both themes are named. |
| VI-B. Automatic, human, and unchecked promotion | "Research systems often promote by admitting a candidate to a bank or archive that later runs reuse." | automatic admission; evidentiary meaning; person at promotion; two meanings of None | coordinate (automatic, human, none) | Partly: it names the three categories, not the claim about evidentiary meaning. |
| VI-C. What formats, registries, and release platforms provide | "Much of the infrastructure needed for sharing already exists independently of these learning loops." | portability; admission; versioning and rollback; missing failure-driven loop | coordinate (formats, registries, platforms) | Partly: it names the infrastructure but not the gap ("without the loop"). |
| VI-D. The two decisions viewed together | "Fig. REF(fig:design) places the local and promotion gates on a common grid." (point: VI:17 S5 "What the grid reveals is a division of capabilities: no system has both the learning of the top row and the governance of the bottom row.") | gate grid; signals per cell; empty cells; division of capabilities | logical (grid, match with expectations, empty cells, robustness, finding) | No: a label; the finding (division of capabilities) is not in the heading. |

## Group D (VII, VIII, IX): S4 diagnostic ledger

# S4 diagnostic ledger, part D: Sections VII, VIII, IX

Files diagnosed (read-only): `cg_pre/VII_failure_surface.md` (14 paragraphs), `cg_pre/VIII_missing_architecture.md` (13 paragraphs, counting the lead-in and the four list items), `cg_pre/IX_families.md` (15 paragraphs). Total: 42.

Numbering: F:N, where N counts prose paragraphs and list items from 1. Tables, headings and captions are not numbered; caption problems are in table (b). S1, S2 and so on count sentences inside the paragraph ("et al." does not end a sentence).

Exemptions applied: VIII:2 (8-word list lead-in) and VIII:7 (26-word housekeeping note) skip 2.1 to 2.4. The list items VIII:3 to VIII:6 are one sentence each, so the tests that need two sentences are n/a. No display math occurs in these files.

House style used alongside the skill: `telegrapher_repo/style/telegrapher_paper_style_guide.md`. Its rules that bear on these sections: tables hold values and prose holds interpretation ("Don't duplicate the table in the text"); one claim per paragraph; honest accounting in one place; end sections clean; mechanism over capability; American spelling, with "catalogue" and "analogue". No em-dashes or British spellings were found in the three files.

## (a) Mandatory ledger

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VII_failure_surface:1 | point (section opening) | pass | pass | pass (close call: S4 "The literature" and S5 "Table REF(tab:X-1)" hand the subject to metadiscourse; failures are the subject in S2–S3) | pass (close call: S4 brings in a count, "six", that the reader has not seen) | FLAG: S1 ends on a passive verb, "in which its next decision is made"; the themes "failures" and "the control that addresses it" first appear in S3 and S5 | FLAG: S4 "six of these failures" points back to the three examples in S2 but counts table rows not yet shown; "in a measured case" has no stated referent | pass | pass | pass | pass (S4 appositive "a seventh, overfitting to one deployment," is short) | FLAG: S3 ends on an attribution, "by Sculley et al. [@sculley2015debt]"; S5 ends on a pronoun, "addresses it" | pass | pass | pass | pass |
| VII_failure_surface:2 | body | pass | pass (restates the Table X-1 row "Scaffold bloat" but adds evidence) | FLAG: subjects hop: S1 "following them" (gerund), S2 "Ratchet's finding", S3 "Conflicting or obsolete artifacts", S4 "Gated retirement, pruning, and expiry"; the protagonist (accumulated artifacts) is the subject only in S3 | FLAG: S2 opens on new information: "Ratchet's finding that model-written skills need lifecycle hygiene" | pass (close call: S1 ends "latency increases"; the other themes, "attribution" and "retirement", first appear in S3–S4) | FLAG: S2 "the consequence" has two candidate antecedents in S1, "following them becomes harder" and "latency increases" | pass | FLAG: S2's subject "Ratchet's finding that model-written skills need lifecycle hygiene before producing gains" runs 12 words before the verb "makes" | FLAG: S2 nominalization subject plus empty verb: "finding ... makes the consequence visible" | FLAG: S2 has a relative clause inside the subject ("that model-written skills need ... before producing gains") | FLAG: S2 ends on the qualifier "at the system level" | FLAG: S4 "can be meaningfully assessed": "meaningfully" fails the strip test | pass | pass | FLAG: abstract subject plus empty verb ("finding ... makes ... visible") |
| VII_failure_surface:3 | evidence | FLAG: the opening frames memory only ("Persistent memory creates another route to lasting error"); S3–S4 move to tool outputs and an MCP configuration, outside that frame | pass | FLAG: a tour of subjects: "Persistent memory", "PoisonedRAG", "AgentPoison", "memory control-flow attacks", "Tool outputs and connected servers", "a previously approved MCP configuration" | FLAG: S3 "Tool outputs and connected servers" and S4 "In CVE-2025-54136" open on new topics | pass | pass | pass | pass | pass | pass (S2's three coordinated clauses) | pass | pass | pass (check that "major agent frameworks" is the source's own word) | pass | FLAG: subject-hopping "tour" paragraph, one citation per clause |
| VII_failure_surface:4 | explanation (controls) | pass | FLAG: S1 restates the Table X-1 controls for "Poisoned memory" and "Injection via tools and MCP" ("Provenance on every entry; write gating; a rollback envelope"; "Narrow tool permissions; a privilege hierarchy over instructions"); S2 restates the table's "tool bindings pass the same promotion gate as any other coordinate" | pass (close call: S3's gerund subject "Checking only the initial registration" hides who checks) | pass | FLAG: S1 ends on the last item of a list of controls, "an instruction privilege hierarchy"; the paragraph's own point (a tool binding needs gating at every later change) arrives in S2–S3 | FLAG: S3 "the decision that authorized it": "it" can be "The tool binding" (S2) or "the initial registration" (S3) | pass | FLAG: S3 has the gerund subject "Checking only the initial registration" | pass | pass (close call: S1 attaches "together with ..." after a citation; 30+ words) | FLAG: S3 ends on a pronoun, "authorized it" | pass | pass | pass | pass |
| VII_failure_surface:5 | point | pass | FLAG: S3 restates Section IV ("VaG finds that reversing a contaminated skill recovers little once other skills have been derived from it", IV_local_findings) with the same citation; VIII:10 repeats it a third time | pass (rollback, restoring, VaG's recovery and version history form a related set) | pass (VaG is already known from Section IV) | pass | pass (S4 "this work" = the checking and tracking in S3) | pass | FLAG: S3 abstract subject "VaG's limited recovery after such rollback" | FLAG: S3 nominalization chain: "recovery ... supports checking contamination before commitment and tracking consequences" | pass | FLAG: S3 ends "after it"; S4 ends "by itself" | pass | pass | pass | FLAG: abstract subject plus "supports" around a nominalization chain (S3) |
| VII_failure_surface:6 | illustration (subsection opening) | pass (themes arrive late; see 3.6) | pass (S4 deliberately sets up Section II's "Revising the evaluator changes the objective itself") | FLAG: subjects hop: "a pitch-review assistant" (object of "Consider"), "The team", "The edit"/"it", "the same rubric"/"the improvement process"; the rubric, which undergoes the mechanism, is a subject only in S4's if-clause | pass ("The team" in S2 is inferable) | FLAG: S1 ends on scene-setting, "without supporting numbers"; the theme (the process edits its own measuring instrument) arrives only in S4 | pass | pass | pass | pass | FLAG: S1 stacks "that consistently overrates decks" and "claiming a large market without supporting numbers" after the main clause | pass | pass | pass | pass | pass |
| VII_failure_surface:7 | point (finding) | pass | FLAG: S5 "The missing result is therefore more specific than an absence of calibrated judges" and S6 "It concerns keeping calibration while the criterion keeps changing" restate S4 "No surveyed system reports calibration maintained across continuing rubric revisions and deployment drift" | FLAG: subjects hop: "This", "The survey", "SkillCoach"/"it", "trajectory-filtering consistency", "No surveyed system", "The missing result", "It" | pass | pass (close call: S1 ends "C3 feedback"; "calibration" enters in S2, inside the two-sentence opening) | FLAG: S3 "after editing it: offline, it compares its initial and evolved rubrics": the first "it" is the judge, the second is SkillCoach | pass | pass (S5 "The missing result is" has an abstract subject) | pass ("calibration" is a term of art) | FLAG: S3 (about 62 words) chains a colon clause, a coordinate clause ("and trajectory-filtering consistency rises from 82% to 96%") and a summative modifier ("an audit its authors describe as judge-assisted rather than a new human annotation study") | pass | pass | pass | pass | FLAG: S5–S6 are a tidy antithetical close ("more specific than an absence of ... It concerns ..."); S3's number load (50, 10, 82%, 96%) runs against "relationships over values" (author's call; see AUTHOR FLAGS) |
| VII_failure_surface:8 | other view | pass | pass | pass | pass | pass (close call: S1 ends "open-ended tasks"; the fixed-versus-co-evolving split that carries the paragraph enters in S2–S3) | pass ("a related problem" = the reflexive gate of VII:7) | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S5 ends the paragraph on a scope caveat in the stress position: "these weight-side methods are not included in the scaffold scores" |
| VII_failure_surface:9 | point + evidence | pass | FLAG: S2 and S5 restate Section V with the same citations ("Reward-model research measures this form of proxy overoptimization [@gao2023overoptimization]"; "Shankar et al. find that evaluators' criteria change as they grade more outputs [@shankar2024validators]") | FLAG: a tour: "a fixed evaluator", "Optimizing a proxy", "Unequal exposure to evaluation data", "Evaluations of agent trajectories"/"deployment tasks", "Human criteria", "a gate"; the evaluator (protagonist) is the subject only in S1 | FLAG: S3 opens on new "Unequal exposure to evaluation data"; S5 opens on new "Human criteria" | pass | pass | pass | FLAG: S2 gerund subject "Optimizing a proxy beyond a point"; S3 nominalization subject "Unequal exposure to evaluation data" | FLAG: S3 "Unequal exposure ... can create apparent performance gains" (nominalization subject plus empty verb) | pass | pass | pass | FLAG: "can" in four of six sentences (S1, S2, S3, S5), including cited findings that could stand flat; judge each claim and keep any hedge that carries weight | pass | FLAG: uniform hedging ("can" four times) |
| VII_failure_surface:10 | point | pass | pass | pass (close call: S1 has three subjects in three clauses: hypothesis, failures, tasks) | pass | pass | FLAG: S1 "The failure-mode hypothesis discussed in Section REF(sec:why)" is presented as old, but sec:why comes later (Section IX) and never uses the name "failure-mode hypothesis" ("a hypothesis", "these hypotheses") | pass | pass (7-word subject; the verb "adds" is word 8) | FLAG: S1 "adds a conditional implication" (empty verb plus nominalization) | pass (S3, about 40 words, puts its point first) | pass | pass | pass | pass (two colons in three sentences) | pass (two colon reveals) |
| VII_failure_surface:11 | point + evidence | pass ("structure" here, "coordination" in the heading) | pass | FLAG: "Some failures", then "A study of multi-agent systems", then "Treating routing and role assignments ..." | FLAG: S2 opens on new information, "A study of multi-agent systems" | pass | pass | pass | FLAG: S3 gerund subject of 10 words, "Treating routing and role assignments as editable scaffold coordinates", before "makes" | FLAG: S3 "makes them subject to evaluation and rollback" | pass | pass (close call: S3 ends on the already-known "instructions and skills") | pass (close call: "prominently") | pass | pass | pass |
| VII_failure_surface:12 | point | FLAG: S1 "Specialization creates a related boundary" leaves nothing concrete to circle | FLAG: restates Section II ("The promotion loop therefore asks for evidence at the receiving scope ... A local success does not automatically enlarge that radius") and the Table X-1 row "Patch overfitting"; the S4 caveat repeats the abstract's "supported only for the measure and task distribution on which it was evaluated" | FLAG: "Specialization", "A scaffold", "Receiving-side evaluation"/"the evidence radius", "This" | pass | FLAG: S1 ends on "a related boundary"; the themes (one deployment degrading another; receiving-side evaluation) appear in S2–S3 | FLAG: S1 "related" names no relatum; S4 "This" can be receiving-side evaluation, the evidence radius, or both | pass | pass | pass | pass | FLAG: S4 ends on a qualifier, "outside the evaluated cases" | pass | pass | pass | FLAG: caveat in the stress position closing the paragraph (S4) |
| VII_failure_surface:13 | point | pass | FLAG: S1 repeats the Table X-1 row "Old rules, polluted memory, and drifting tool versions crowd out adaptation" almost word for word; S3 repeats VII:2 S4's "Gated retirement, pruning, and expiry" | FLAG: "the scaffold", "Long-context degradation", "Expiry, pruning, and rollback" | FLAG: S2 opens on new information, "Long-context degradation [@liu2023lostmiddle]" | pass (close call: S1 ends "accumulate"; the theme "less adaptable" sits mid-sentence) | FLAG: S2 "one related mechanism": the sentence never says what it is related to or what it is a mechanism of | pass | FLAG: S2 abstract subject "Long-context degradation" | FLAG: S2 "provides one related mechanism" (empty verb) | pass | pass | pass | pass (the link from long-context degradation to plasticity loss is asserted loosely; see 6.3) | pass | FLAG: empty verb "provides" |
| VII_failure_surface:14 | point (section close) | pass | pass (S2 restates the table's "Dominant class" column in prose, but adds a mechanism for each class) | pass (S2's four subjects are the feedback classes; S3 moves to "Production systems") | pass (S3's "controls" are already known from the section) | FLAG: S1 ends on a negated caveat, "without making them exclusive to one class"; the section's point (no system runs the controls together) is the last clause of S3 | FLAG: S3 "the surface": "failure surface" appears only in the table caption; S1 "these risks" renames the section's "failures" | pass | pass | pass | pass (S2's four-clause semicolon series is parallel; about 38 words) | FLAG: S1 ends "to one class"; S3 ends on a pronoun, "runs them together" | pass | FLAG: S3 "stays largely unmitigated because no surveyed system runs them together": the effect is hedged, the cause is not (see AUTHOR FLAGS) | pass (the semicolon chain is a parallel taxonomy, which the house style allows) | pass (the section ends on "them together") |
| VIII_missing_architecture:1 | point (section opening) | pass | pass (restates the Introduction's sixth paragraph as this section's opening claim, deliberately) | pass (S2–S4 have parallel subjects, one per component) | pass | pass | FLAG: S5 "under equivalent controls": the text never says equivalent to what | pass | pass (S1 "The evidence so far identifies" has an abstract subject) | pass | pass | pass | pass | pass | pass | pass (the S2–S4 triplet is the section's one parallel flourish) |
| VIII_missing_architecture:2 | transition (list lead-in) | n/a: transition | pass | pass | pass | pass | pass ("that missing combination" can be inferred from VIII:1 S5, which said "process", not "combination") | pass | pass | pass | pass | pass | pass | n/a: no claim | pass | pass |
| VIII_missing_architecture:3 | list item (a) | n/a: list item | pass | pass | n/a: one sentence | pass | pass | n/a: one sentence | pass | pass ("algorithmic acceptance criterion" reads as a term) | pass | pass | pass | pass | pass | pass |
| VIII_missing_architecture:4 | list item (b) | n/a: list item | pass | pass | n/a: one sentence | pass | pass | n/a: one sentence | pass | pass | pass | FLAG: ends on the afterthought "or customers", which adds a second name for the boundary that VIII:7 then has to reconcile | pass | pass | pass | pass |
| VIII_missing_architecture:5 | list item (c) | n/a: list item | pass | pass | n/a: one sentence | pass | pass | n/a: one sentence | pass | pass | pass (one trailing "with policies controlling ...") | FLAG: ends on a pronoun, "access it" | pass | pass | pass | pass |
| VIII_missing_architecture:6 | list item (d) | n/a: list item | pass | pass | n/a: one sentence | pass | pass | n/a: one sentence | pass | pass | pass | pass | pass | pass | pass | pass |
| VIII_missing_architecture:7 | housekeeping | n/a: short housekeeping (26 words) | pass | pass | FLAG: S2 opens on a long run of new information, "Sharing among agents, users, or benchmark partitions within one operator" | FLAG: S1 ends on "here" | pass ("here" = this audit) | pass | FLAG: S2's verb "does not establish" arrives at word 11 | pass | pass | FLAG: S1 ends on "here" | FLAG: S1 "here" can be inferred | pass | pass | pass |
| VIII_missing_architecture:8 | evidence | pass (S1 is a pointer to the table; the paragraph's claim is S6) | FLAG: S2–S5 restate the Table IX-1 rows in prose (FederatedSkill's "auditable server decision log", EvolveNet's "previous shared harness", the registries, the MCP planes); house style: "Don't duplicate the table in the text" | pass (the systems are the subjects and form one related set) | pass | FLAG: S1 ends on a pointer, "the closest systems"; the finding (no system crosses the organization boundary) arrives in S4 and S6 | pass | pass | pass | pass | pass | pass (S6 ends "such a promotion", repeating "a promotion" from earlier in the sentence; the repeat is deliberate) | pass | pass | pass | pass |
| VIII_missing_architecture:9 | point | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S3 "making an unsupported decision about whether" (empty verb plus nominalization) | pass | pass | pass | pass | pass | pass |
| VIII_missing_architecture:10 | point | pass | FLAG: S3 is the third statement of VaG's finding about descendants (IV_local_findings; VII:5 S2–S3) | pass (S3 hops to "VaG's result") | pass (VaG is already known from IV and VII) | pass | FLAG: S1 "addresses both": the two antecedents are paragraphs apart (the four-property audit in VIII:2–6 and receiving-side evaluation in VIII:9); "the rollback envelope" is presented as known but appears only in Table X-1 | pass | pass | pass | pass (S1 runs about 45 words but puts its point first, before a colon list) | pass | pass | pass | pass | pass |
| VIII_missing_architecture:11 | other view | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S2 ends "have been extensively studied" plus citations; S4 ends on the qualifier "often through a language model" | FLAG: S1 "useful" and S2 "extensively" fail the strip test | pass | pass | pass ("offers a useful comparison") |
| VIII_missing_architecture:12 | point | pass | pass (S5 overlaps VIII:13 S1) | pass (S4 breaks the feedback-class subject series with "a human promotion gate") | pass | pass | FLAG: S5 "those systems" has no antecedent; the clause before it names "Delayed outcomes", not systems | pass | FLAG: S1 abstract subject "The extent of automation" | FLAG: S1 "The extent of automation"; S2 "provide the most direct setting for testing" | pass | pass | pass | pass | pass | pass |
| VIII_missing_architecture:13 | point (section close) | pass | pass (S3 restates the paper's evidence-radius thread as the section close; exempt) | pass | pass | pass | pass | pass | pass | FLAG: S2 "be interpreted as a requirement to automate"; S3 "preserve the ability to inspect and reverse its adoption" | pass (S3 has two coordinated that-clauses) | pass | FLAG: S3 "the ability to" (a phrase where "can" would do) | pass | pass | FLAG: S2 is a defensive caveat ("They should not be interpreted as a requirement to automate every decision in every domain"), against the house rule "Honest accounting goes in one place" |
| IX_families:1 | point (section opening) | pass | pass | pass | pass ("Different research communities" in S2 can be inferred from "history") | FLAG: S1 ends on "has a history"; the theme, "the part of the loop" each line built, arrives in S3 | FLAG: S1 "The uneven architecture" is presented as known (Section VIII described a missing architecture, not an uneven one); in S4, "five such lines" uses "lines" before the paragraph has named any (S2 says "communities") | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| IX_families:2 | evidence | FLAG: no framing sentence; S1 already glosses the first table row, so no line can be drawn for the paragraph as a whole | FLAG: restates Table VIII-1 rows 1–3 ("proposal by reflection over trajectory evidence; the two-timescale case"; "a generalization penalty, the $\Omega$ of the gate"; "attribution of a failure to one slot") | pass (the research lines are the subjects) | pass | FLAG: S1 ends on "a faster schedule than weights"; the paragraph's claim (each line built one condition) is never stated | pass | pass | pass | pass | FLAG: S2 trailing participle "corresponding to the complexity penalty in the acceptance rule"; S1 tacks on "together with an argument for adapting artifacts" | pass | pass | pass | pass | FLAG: trailing participle (S2) |
| IX_families:3 | evidence | FLAG: S1 frames only the lifecycle line; S3 (transfer and federation) falls outside the frame | FLAG: restates Table VIII-1 rows 4–5 ("gated retirement; hygiene as a precondition"; "receiving-side confirmation") | pass | FLAG: S3 opens on a new line, "Transfer and federation", with no join | pass | pass | pass | pass (S2 "Its contributions include") | FLAG: S2 "Its contributions include" (nominalization subject plus weak verb) | pass (S3 trails "progressing from ...") | pass | pass | pass | pass | pass |
| IX_families:4 | point (explanation) | pass | pass | FLAG: "This history", "Each research line", "Building a record of recurring failures", "Attribution", "The local loop" | FLAG: S4 opens on new information, "Attribution" | pass | pass | pass | FLAG: S3 gerund subject "Building a record of recurring failures" | FLAG: S3 "was none of their starting problems" | pass | FLAG: S4 ends on "a particular line studies" | FLAG: S4 "substantial" fails the strip test; S3 uses a negative frame, "none of their starting problems" | pass (S5's "consequently" asserts causation from the history; see 6.3) | pass | pass |
| IX_families:5 | point | pass | FLAG: S5 restates IX:1 S2–S3; S4's second clause restates Section VIII ("The surveyed systems do not connect these capabilities ...") | pass | pass | pass (close call: S1 ends "weights and editable artifacts", but S5 adds a second claim, convergent mechanisms, that S1 does not frame) | FLAG: S1 "The convergence" is presented as known; no earlier sentence in the section names a convergence (only the Table VIII-1 caption, "converging on") | pass | pass | pass ("a shared decomposition of the system into") | FLAG: S3 the appositive "SIA" splits subject from verb: "A system that updates both, SIA, still treats" | FLAG: S2 ends on a pronoun, "all use it" | pass | pass | pass | FLAG: S4 defensive caveat ("does not establish that one architecture is optimal") |
| IX_families:6 | point (subsection opening) | pass | pass (S4 restates the Introduction's scaffold definition) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S4 uses capability voice: "The scaffold provides a place to encode those requirements" |
| IX_families:7 | evidence | pass (the framing sentence is S2) | pass | FLAG: "Work on reinforcement learning from human feedback", "This", "Tiwari et al."/"in-context changes"/"in-weight adaptation" | FLAG: S3 opens on a new character, "Tiwari et al." | FLAG: S1 ends on evidence, "more homogeneous preferences"; the theme (broad model behavior versus customer-specific requirements) arrives in S2 | pass (S3 "approach it" = the distinction in S2) | pass | FLAG: S1 subject "Work on reinforcement learning from human feedback"; the verb is word 8 | FLAG: S2 "helps motivate the distinction between" | pass | pass | pass | pass | pass | pass |
| IX_families:8 | other view + point | pass | FLAG: S2 restates the Introduction's "a new model requires a separate training, evaluation, and release process" | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass (close call: "the cheaper path" is an unsourced comparative; see 6.3) | pass | pass ("offer the cheaper path") |
| IX_families:9 | evidence (series hypothesis) | pass | pass | pass | pass | FLAG: S1 ends on a hedge, "may be effective"; the theme "targeted artifact changes" sits mid-sentence | pass | pass | pass | pass | FLAG: in S3 the where-clause "where fewer than a tenth of tokens depend on distant context" sits between the two coordinated objects of "includes", so "and the accuracy recovered through majority voting" can attach to the where-clause | FLAG: S1 ends "may be effective" | pass | pass (close call: "offer a hypothesis ... may be effective" stacks two hedges; they carry weight, so the author decides) | pass | pass |
| IX_families:10 | evidence (series hypothesis) | pass | pass | pass | pass | FLAG: S1 ends on scene-setting, "evaluator expectations"; the theme (a catalogue of failure modes) arrives in S2 | pass | pass | pass | pass | pass | pass | FLAG: S4 "equally relevant" fails the strip test | pass (S2 and S3 tie growth to different variables; see AUTHOR FLAGS) | pass | pass |
| IX_families:11 | point | pass | pass | FLAG: "a deployment", "Persistent rules, memories, skills, and tool changes", "the gated and scoped artifact layer", "The survey"/"its findings" | pass | pass | FLAG: "these hypotheses" in S1 (two) becomes "On that hypothesis" in S3 (one) | pass | pass (in S3 the verb follows "On that hypothesis" at word 10) | FLAG: S2 "provide an inspectable representation for those interventions" | pass (S3, about 50 words, puts its point first) | FLAG: S4 ends "independently of them" | pass | pass (S3's flat "is ... the architecture the error structure calls for" is conditioned by "On that hypothesis"; this is the load-bearing three-paper argument, so keep it) | pass | pass (S3's "not X but Y" plus triplet is the section's one flourish; keep it) |
| IX_families:12 | other view (subsection opening) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass | FLAG: S2 ends "is subsequently used" | FLAG: S2 "subsequently" can be inferred | pass | pass | pass |
| IX_families:13 | other view | pass | FLAG: S2–S4 restate the Table II-2 rows for Ding and Lin ("governance is an axis, the gate on an edit is not"; "principal scoping and rollback are axes, feedback and promotion are not") | pass | pass | pass (S1 ends on survey names; the theme "governance precedents" is in the subject) | pass | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| IX_families:14 | other view (lineage) | FLAG: S1 frames "Prompt optimization ... lineage"; S2–S3 (ACE, agent symbolic learning, STOP, SICA) are not prompt optimization and fall outside the frame | FLAG: prompt optimization already appears in IX:1 ("improving prompts") and IX:2 ("Prompt optimization and reflective evolution developed ways to propose edits") | FLAG: a tour: "OPRO, EvoPrompt, ...", "ACE", "Agent symbolic learning", "STOP", "SICA", "These works" | FLAG: S2 "ACE" and S3 "Agent symbolic learning" open on new systems | pass | pass | pass | pass | pass | pass (S3 is a parallel semicolon chain) | pass | FLAG: S1 "important" | FLAG: S1 "another important lineage" is an intensifier without evidence | pass | FLAG: intensifier "important"; tour paragraph |
| IX_families:15 | point (section close) | pass | FLAG: S1 restates IX:12 S2's unit of analysis ("the decision that accepts a persistent change, the feedback supporting that decision, and the scope in which the change is subsequently used") | FLAG: abstract subjects throughout: "The contribution", "The 256-system corpus, two-loop classification, feedback classes, and governance audit", "An extended discussion" | pass | pass | FLAG: S1 "their joint reading": "their" reaches back to IX:14's "These works"; S2 "that comparison" has no antecedent (S1 says "joint reading") | pass | FLAG: S2 has a 9-word compound subject before "make" | FLAG: S1 "The contribution here is their joint reading" (nominalization + is + nominalization) | pass | FLAG: S3 ends on a pointer, "(Supplementary Material S7)" | FLAG: S1 "here" | pass | pass | FLAG: the section ends on a pointer to the supplement rather than on its point (house rule "End sections clean") |

## (b) Flags-only table (other paragraph-level tests)

| ¶ | test | finding (quote the words) |
|---|---|---|
| VII_failure_surface:1 | 2.2 | The section's point, that controls exist but "no surveyed system runs them together" (VII:14 S3), arrives in the section's last clause; the opening states only that "An improvement loop changes the context in which its next decision is made." |
| VII_failure_surface:1 | 4.15 | "in a measured case" is unclear: one study? a measurement per failure? |
| VII_failure_surface:1 | 4.2 | "identified for machine-learning systems by Sculley et al.": the authors sit in a by-phrase. |
| VII_failure_surface:2 | 4.8 | S2's whole subject is 12 words and contains a relative clause ("Ratchet's finding that model-written skills need lifecycle hygiene before producing gains"). |
| VII_failure_surface:3 | 4.12 | S2's three coordinated clauses are not parallel: "PoisonedRAG demonstrates", "AgentPoison plants", then a class of attack, "memory control-flow attacks operate". |
| VII_failure_surface:3 | house style (one claim per paragraph) | Memory poisoning (S1–S2) and tool/MCP injection (S3–S4) are two claims; Table X-1 gives them two rows. |
| VII_failure_surface:3 | 4.15 | "memory control-flow attacks" is not glossed. |
| VII_failure_surface:4 | 4.5 | "The tool binding itself must be subject to controlled revision": agentless, with no stated reviser or gate. |
| VII_failure_surface:6 | 2.4 | The framing sentence comes last (S4). The house style's "show before you name" allows this; it is noted, not failed. |
| VII_failure_surface:7 | 2.2 | The point (S4) comes after evidence (S2–S3) and is then restated twice (S5–S6). |
| VII_failure_surface:7 | 4.15 | "human-gold references" and "trajectory-filtering consistency" are not glossed. |
| VII_failure_surface:9 | 6.4 | S4 "Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite remains fixed" carries no citation. |
| VII_failure_surface:9 | 4.12 | In S6, "its own held-out checks, calibration where judgment is involved, and revision history" has a middle item that carries a clause. |
| VII_failure_surface:10 | 4.15 | "failure-mode hypothesis" is never defined under that name; IX:9–11 say "a hypothesis" and "these hypotheses". |
| VII_failure_surface:12 | 2.3 | "Specialization" (prose) and "Patch overfitting" (Table X-1) name the same failure. |
| VII_failure_surface:13 | 2.3 | Table X-1 says "Plasticity loss"; the prose says "less adaptable" and never names the failure. |
| VII_failure_surface:13 | 6.3 | "Long-context degradation [@liu2023lostmiddle] provides one related mechanism": the link to loss of adaptability is asserted, not shown. |
| VII_failure_surface:14 | 6.3 | "the surface stays largely unmitigated because no surveyed system runs them together" is a causal claim with no evidence in the sentence. |
| VII_failure_surface:14 | 2.3 | The section's term drifts: "failures" (section), "these risks" (S1), "the surface" (S3); "observable outcomes" here vs. "observed outcomes" in VIII:12 and the abstract. |
| VII table caption | caption | "Table X-1." carries a pre-restructure number (the section is now VII); "feedback-signal class" here vs. "feedback class" in the prose; the "Evaluation fragility" cell's "read non-independently" is unclear. |
| VIII_missing_architecture:3–6 | 4.12 | The list items are not parallel: (a) "a criterion tests" (active), (b) "artifacts can be promoted" (modal passive), (c) "a promoted artifact carries" (active), (d) "a harmful promotion can be reversed" (modal passive). |
| VIII_missing_architecture:4 | 2.3 | The boundary has three names: "organizations or customers" (b), "cross-tenant" (VIII:7), "per-tenant", "receiving tenant" (VIII:10). VIII:7 reconciles two of them, and only after (b). |
| VIII_missing_architecture:8 | 2.2 | The paragraph's point (S6, "no system rolls back a promotion that has crossed an organization boundary") comes last. |
| VIII table caption/body | caption | "Table IX-1." carries a pre-restructure number (the section is now VIII). In the SkillForge row, "(c) partial" has no explanation, unlike every other partial cell. "not documented" (SkillForge) and "not reported" (MCP) are worded differently. The prose never discusses the SkillForge row. |
| VIII_missing_architecture:9 | 4.6 | "It is kept separate from the four-property audit": a passive on the authors' own decision. |
| VIII_missing_architecture:11 | 4.5 | "have been extensively studied": agentless (the citations stand in for the agent). |
| VIII_missing_architecture:12 | 4.12 | The S2–S5 series of feedback classes breaks parallel at S4 ("Where quality is judged, a human promotion gate ..."). |
| VIII_missing_architecture:12 | 2.3 | "Observed outcomes" here vs. "observable outcomes" in VII:14. |
| VIII_missing_architecture:13 | 4.6 | "They should not be interpreted as": a passive on the authors' own claim. |
| IX_families:1 | 2.3 | S2's problem names drift from the Table VIII-1 "Started from" column: "improving prompts" vs. "Prompt optimization and continual learning"; "selecting agent workflows" vs. "Orchestration and harness engineering"; "maintaining skill libraries" vs. "Skill pools that bloat under platform limits". |
| IX table caption | caption | "Table VIII-1." carries a pre-restructure number (the section is now IX). |
| IX_families:2 | 2.4 | No framing sentence. |
| IX_families:2–3 | house style (one claim per paragraph) | IX:2 covers three research lines and IX:3 covers two; together they gloss Table VIII-1 row by row, and neither states the claim the rows support. |
| IX_families:4 | 6.3 | S5 "The local loop has consequently developed from evaluation backward": a causal reading of the history, stated flat. |
| IX_families:5 | 4.12 | S2 "GEPA, Meta-Harness, MOSS, RCL, PACE, and the harness-optimization papers": Meta-Harness and MOSS are themselves harness-optimization papers (cited as such in IX:2), so the series overlaps. |
| IX_families:5 | house style (one claim per paragraph) | S1 (a shared weights/artifacts decomposition) and S5 (convergent mechanisms from different problems) are two claims. |
| IX_families:7 | 2.3 | The character drifts: "deployment" (IX:6), "customer-specific" (IX:7), "Per-customer", "one customer" (IX:8). |
| IX_families:7 | 4.2 | "Work on reinforcement learning from human feedback reports": the researchers are hidden behind "Work". |
| IX_families:8 | 6.3 | "Persistent artifacts offer the cheaper path": a cost comparison with no citation. |
| IX_families:12 | 1.5 (placement, section level) | "Relation to neighboring surveys" is related work placed at the end of a section headed "How the research lines fit together"; the label "tab:II-2" shows it once sat in Section II. |
| IX table II-2 | caption/body | "Table II-2." carries a pre-restructure number. The Guo et al. row's "touches all four questions without classifying by any" does not say which four (IX:12 S2 names three elements; the caption names four axes). The caption's "is the only one to cover promotion across organizations" is unqualified (see AUTHOR FLAGS). |
| IX_families:15 | 5.2 | S3 "An extended discussion separates these contributions from their precedents (Supplementary Material S7)" is mostly a pointer. |
| IX section | 1.5 (placement, section level) | The subsection "Why specialization remains outside the weights" {#sec:why} is motivation, not a research line. VII:10 already relies on it ("discussed in Section REF(sec:why)") before it appears. |
| IX_families:14 | 1.5 (placement) | These prompt-optimization precedents are separated from the prompt-optimization line in IX:2 by eleven paragraphs. |

No findings for 3.3 (pointer words are early everywhere), 3.4 (no subject is preceded by more than about 7 words of throat-clearing), 3.5 (every connective names a real relation: "therefore" in VII:7 S5, "Consequently" in VII:9 S6, "Thus" in VIII:13 S1, "consequently" in IX:4 S5), 4.7 (noun strings are terms of art), 4.13, 4.16 (sentence lengths in each section run from about 6 to about 62 words), 6.1, 6.2, 6.5 or 6.6.

## (c) Suggested moves, one per FLAG

| ¶ | test | move |
|---|---|---|
| VII:1 | 3.6 | End S1 on the section's theme (the loop alters the evidence for its next acceptance), not on "is made". |
| VII:1 | 3.7 | Say "seven failures" (or name the table) before counting six of them; replace "in a measured case" with what was measured. |
| VII:1 | 4.14 | Move Sculley et al. to the front of S3 (they identified the debt); end S5 on "control" rather than "it". |
| VII:2 | 3.1 | Make the accumulated artifacts (instructions, skills) the running subject; turn Ratchet into evidence after the verb. |
| VII:2 | 3.2 | Open S2 on the old element (model-written skills, accumulation) and put Ratchet's finding after the verb. |
| VII:2 | 3.7 | Name which consequence Ratchet makes visible. |
| VII:2 | 4.1 / 4.3 / 4.9–4.11 | Recast S2 as "Ratchet finds that ..." with the authors or the system as subject. |
| VII:2 | 4.14 | Trim or move "at the system level" leftward. |
| VII:2 | 5.1 | Strip-test "meaningfully". |
| VII:2 | AI-sweep | Same as 4.3. |
| VII:3 | 2.1 | Split into a memory paragraph and a tool/MCP paragraph, or open with a frame that covers both channels. |
| VII:3 | 3.1 / 3.2 / AI-sweep | Make the attack (or the channel) the running subject; put the systems after the verbs. |
| VII:4 | 2.5 | Cut the restated table controls; keep the paragraph's new claim (a tool binding needs gating on every change) and its citations. |
| VII:4 | 3.6 | Open on the tool-binding point. |
| VII:4 | 3.7 / 4.14 | Repeat the noun ("the binding") instead of "it". |
| VII:4 | 4.1 | Give S3 a real subject (who checks only at registration). |
| VII:5 | 2.5 | Shorten the VaG restatement to a back-reference to Section IV, and spend the space on what is new here (check before commitment, track after). |
| VII:5 | 4.1 / 4.3 / AI-sweep | Recast S3 with VaG (or its authors) as subject and verbs for "recovery", "checking", "tracking". |
| VII:5 | 4.14 | End S3 and S4 on content words rather than "after it" and "by itself". |
| VII:6 | 3.1 | Keep the rubric (or the team that edits it) as the subject through S2–S4. |
| VII:6 | 3.6 | End S1 on the behavior the story will show (overrating), or add a frame sentence. Keep the example first (house style: show before you name). |
| VII:6 | 4.9–4.11 | Split or shorten S1's stacked modifiers. |
| VII:7 | 2.5 / AI-sweep | Merge S4–S6 into one statement of the missing result. |
| VII:7 | 3.1 | Keep "surveyed systems" and "judge calibration" as the running topics. |
| VII:7 | 3.7 | Repeat "the judge" and "SkillCoach" instead of the two "it"s in S3. |
| VII:7 | 4.9–4.11 | Split S3 into the method and the result, and keep the authors' caveat as its own short sentence. |
| VII:8 | AI-sweep | Move the scope note ("not included in the scaffold scores") earlier, or attach it to the Supplementary pointer. |
| VII:9 | 2.5 | Point back to Section V for proxy overoptimization and shifting human criteria; keep only what is new here (repeated use, exposure, path dependence). Cutting citations is the author's call. |
| VII:9 | 3.1 / 3.2 / 4.1 / 4.3 / AI-sweep | Make the evaluator the running subject ("An evaluator optimized past a point ...", "An evaluator exposed unequally ..."). |
| VII:9 | 5.3 | State cited findings flat; keep "can" only where the uncertainty lives. |
| VII:10 | 3.7 | Signal the forward reference and name the hypothesis as Section IX names it; or move the hypothesis earlier (see AUTHOR FLAGS). |
| VII:10 | 4.3 | Use a verb: "implies, if ...". |
| VII:11 | 3.1 / 3.2 | Keep "failures" or "coordination failures" as the subject; give the study a named actor after the verb. |
| VII:11 | 4.1 / 4.3 | Recast S3 with the operator, or "routing and role assignments", as subject and a real verb. |
| VII:12 | 2.1 / 3.6 / 3.7 | Replace "a related boundary" with the actual claim (a scaffold tuned to one deployment can degrade another). |
| VII:12 | 2.5 / 4.14 / AI-sweep | Point back to Section II for the receiving-side check; cut the closing caveat or fold it into the claim. |
| VII:12 | 3.1 | Keep "a scaffold" as the subject. |
| VII:13 | 2.5 | Drop the near-verbatim table wording; name the failure ("plasticity loss") and add only what the table lacks. |
| VII:13 | 3.1 / 3.2 / 3.7 / 4.1 / 4.3 / AI-sweep | Say what lost-in-the-middle is a mechanism of, with the scaffold (or long context) as subject and a real verb. |
| VII:14 | 3.6 / 4.14 | Open on the section's point (controls exist, none runs them together); end S1 on "risks" or the classes, not on the caveat. |
| VII:14 | 3.7 | Name "failure surface" in the prose before using "the surface"; keep one word for the section's failures. |
| VII:14 | 5.3 | Calibrate the causal "because" (author decides; see AUTHOR FLAGS). |
| VIII:1 | 3.7 | Say equivalent to what (to local controls? to the sender's?), or cut "equivalent". |
| VIII:4 | 4.14 | Settle one name for the boundary in (b) and define the synonym once. |
| VIII:5 | 4.14 | End on "access" or "audit trail" rather than "it". |
| VIII:7 | 3.2 / 4.1 | Open S2 on the old element (property (b)) and put the excluded cases after the verb. |
| VIII:7 | 3.6 / 4.14 / 5.1 | Cut "here". |
| VIII:8 | 2.5 / 3.6 | Open on the finding (no system crosses the boundary, the closest stay within one operator) and let the table carry the per-system detail. |
| VIII:9 | 4.3 | "decide, without support, whether ...". |
| VIII:10 | 2.5 | Cut S3 or reduce it to a pointer; VaG's descendants finding is already stated twice. |
| VIII:10 | 3.7 | Name both antecedents ("the four properties and the receiving-side check"); introduce "rollback envelope" or use "reversal path". |
| VIII:11 | 4.14 / 5.1 | Strip "useful" and "extensively"; end S4 on "symbolic edits". |
| VIII:12 | 3.7 | "systems with delayed outcomes". |
| VIII:12 | 4.1 / 4.3 | Make the feedback (or the designer) the subject of S1; use a verb in S2 ("are the most direct way to test"). |
| VIII:13 | 4.3 / 5.1 | "can still inspect and reverse"; make the authors the actor of S2. |
| VIII:13 | AI-sweep | Merge the caveat in S2 into S1, or cut it if the Discussion carries it. |
| IX:1 | 3.6 | End the opening sentence on the themes (each line built one part of the loop). |
| IX:1 | 3.7 | Introduce "research lines" by name in S2; tie "uneven" to the finding it echoes. |
| IX:2 | 2.1 / 3.6 | Add a framing claim, or merge IX:2–3 into one paragraph that states what the rows show and cites them. |
| IX:2 | 2.5 | Keep the citations and cut the prose that repeats the table cells. |
| IX:2 | 4.9–4.11 / AI-sweep | Replace the trailing "corresponding to ..." with a main clause. |
| IX:3 | 2.1 / 3.2 | Frame both lines, or split them. |
| IX:3 | 2.5 | As IX:2. |
| IX:3 | 4.3 | "The lifecycle literature contributes ..." or "evaluates retirement ...". |
| IX:4 | 3.1 / 3.2 | Keep "research lines" as subject: "None began by recording failures; most study attribution only within their own substrate." |
| IX:4 | 4.1 / 4.3 / 5.1 | Make S3 affirmative with a character subject; strip-test "substantial". |
| IX:4 | 4.14 | End S4 on the substrate, not on "studies". |
| IX:5 | 2.5 | Cut S5's restatement of IX:1, or make S5 the paragraph's single claim and move S1–S3 under it. |
| IX:5 | 3.7 | Name what converges before "The convergence". |
| IX:5 | 4.9–4.11 | "SIA updates both and still treats them as separate levers". |
| IX:5 | 4.14 | End S2 on the decomposition, not "it". |
| IX:5 | AI-sweep | Move the optimality caveat to the paper's limitations, or keep only the scope clause. |
| IX:6 | AI-sweep | Name the mechanism: what the scaffold encodes, and at which scope. |
| IX:7 | 3.1 / 3.2 / 3.6 / 4.1 / 4.3 | Open on the distinction (broad model behavior vs customer requirements) and let RLHF work and Tiwari et al. follow as evidence. |
| IX:8 | 2.5 | Point back to the Introduction's schedule contrast instead of restating it. |
| IX:9 | 3.6 / 4.14 | End S1 on "targeted artifact changes" (the theme), with the hedge placed earlier. |
| IX:9 | 4.9–4.11 | Split S3 so the two pieces of evidence are not separated by the where-clause. |
| IX:10 | 3.6 | Let the opening sentence end on the catalogue of modes. |
| IX:10 | 5.1 | Strip "equally" or say why the result is relevant. |
| IX:11 | 3.1 | Keep "the artifact layer" or "targeted interventions" as the running subject. |
| IX:11 | 3.7 | Make the number agree ("these hypotheses" or "On these hypotheses"); the author confirms which. |
| IX:11 | 4.3 | "Persistent rules, memories, skills, and tool changes can represent those interventions inspectably". |
| IX:11 | 4.14 | End S4 on "the corpus". |
| IX:12 | 4.14 / 5.1 | Cut "subsequently". |
| IX:13 | 2.5 | Keep the two surveys' findings, which the table lacks, and cut the axis restatements. |
| IX:14 | 2.1 / 3.1 / 3.2 / AI-sweep | Frame the paragraph as "one-shot optimizers and self-improving harnesses", with "these works" as the running subject; strip "important". |
| IX:14 | 2.5 | Merge with IX:2's prompt-optimization line, or point back to it. |
| IX:14 | 5.3 | Drop "important". |
| IX:15 | 2.5 | Do not restate IX:12's unit of analysis; state what the joint reading yields. |
| IX:15 | 3.1 / 4.1 / 4.3 | Make the authors ("We read these works jointly ...") or the survey the subject. |
| IX:15 | 3.7 | Name the antecedent ("these precedents") and keep one word: "joint reading" or "comparison". |
| IX:15 | 4.14 / 5.1 / AI-sweep | End the section on its claim; move the Supplementary pointer into a parenthesis earlier. |

## (d) Role-level verdict per paragraph

Rule: re-draft if a role-level test fails (prelude 1.2, illustration 1.6, relevance/placement 1.5, wrong protagonist 3.1 where the fix is not just a pronoun), or if three or more of 2.5, 3.1, 3.2, 3.6, 3.7, 3.8 fail.

| ¶ | role-level test failed / passage-test count | verdict |
|---|---|---|
| VII_failure_surface:1 | none; 2 (3.6, 3.7) | keep-and-polish |
| VII_failure_surface:2 | 3.1 wrong protagonist (finding/retirement as subjects, not the accumulated artifacts); 3 (3.1, 3.2, 3.7) | re-draft |
| VII_failure_surface:3 | none at role level; 2 (3.1, 3.2). Also 2.1 frame fail: split candidate | keep-and-polish (split into memory and tool/MCP paragraphs) |
| VII_failure_surface:4 | none; 3 (2.5, 3.6, 3.7) | re-draft |
| VII_failure_surface:5 | none; 1 (2.5) | keep-and-polish |
| VII_failure_surface:6 | 1.6 illustration: pass (the case shows the mechanism in S3–S4; it is hypothetical, not data); 1.2: n/a (a subsection example, not a prelude); 2 (3.1, 3.6) | keep-and-polish |
| VII_failure_surface:7 | none; 3 (2.5, 3.1, 3.7) | re-draft |
| VII_failure_surface:8 | none; 0 | keep-and-polish |
| VII_failure_surface:9 | 3.1 wrong protagonist (the evaluator is the subject only in S1); 3 (2.5, 3.1, 3.2) | re-draft |
| VII_failure_surface:10 | none; 1 (3.7) | keep-and-polish |
| VII_failure_surface:11 | none; 2 (3.1, 3.2) | keep-and-polish |
| VII_failure_surface:12 | none; 4 (2.5, 3.1, 3.6, 3.7) | re-draft |
| VII_failure_surface:13 | none; 4 (2.5, 3.1, 3.2, 3.7) | re-draft |
| VII_failure_surface:14 | none; 2 (3.6, 3.7) | keep-and-polish |
| VIII_missing_architecture:1 | none; 1 (3.7) | keep-and-polish |
| VIII_missing_architecture:2 | none; 0 | keep-and-polish |
| VIII_missing_architecture:3 | none; 0 | keep-and-polish |
| VIII_missing_architecture:4 | none; 0 | keep-and-polish |
| VIII_missing_architecture:5 | none; 0 | keep-and-polish |
| VIII_missing_architecture:6 | none; 0 | keep-and-polish |
| VIII_missing_architecture:7 | none; 2 (3.2, 3.6) | keep-and-polish |
| VIII_missing_architecture:8 | none; 2 (2.5, 3.6) | keep-and-polish |
| VIII_missing_architecture:9 | none; 0 | keep-and-polish |
| VIII_missing_architecture:10 | none; 2 (2.5, 3.7) | keep-and-polish |
| VIII_missing_architecture:11 | none; 0 | keep-and-polish |
| VIII_missing_architecture:12 | none; 1 (3.7) | keep-and-polish |
| VIII_missing_architecture:13 | none; 0 | keep-and-polish |
| IX_families:1 | none; 2 (3.6, 3.7) | keep-and-polish |
| IX_families:2 | none; 2 (2.5, 3.6). Also 2.1 frame fail: merge with IX:3 under one framing claim | keep-and-polish |
| IX_families:3 | none; 2 (2.5, 3.2) | keep-and-polish |
| IX_families:4 | none; 2 (3.1, 3.2) | keep-and-polish |
| IX_families:5 | none; 2 (2.5, 3.7) | keep-and-polish |
| IX_families:6 | none at paragraph level (the subsection's placement fails 1.5 at section level; see below) | keep-and-polish |
| IX_families:7 | none; 3 (3.1, 3.2, 3.6) | re-draft |
| IX_families:8 | none; 1 (2.5) | keep-and-polish |
| IX_families:9 | none; 1 (3.6) | keep-and-polish |
| IX_families:10 | none; 1 (3.6) | keep-and-polish |
| IX_families:11 | none; 2 (3.1, 3.7) | keep-and-polish |
| IX_families:12 | none at paragraph level (the subsection's placement fails 1.5 at section level) | keep-and-polish |
| IX_families:13 | none; 1 (2.5) | keep-and-polish |
| IX_families:14 | 1.5 placement (prompt-optimization precedents sit eleven paragraphs away from IX:2's prompt-optimization line); 3 (2.5, 3.1, 3.2) | re-draft |
| IX_families:15 | none; 3 (2.5, 3.1, 3.7) | re-draft |

Section-level (for the plan, not a paragraph verdict): in Section IX, the subsections "Why specialization remains outside the weights" (IX:6–11) and "Relation to neighboring surveys" (IX:12–15) fail 1.5 relevance/placement against the section heading "How the research lines fit together". VII:10 also uses sec:why before the reader reaches it. This is a document-level Restructure candidate. Section VII fails 2.2: its point arrives in its last clause (VII:14 S3).

## AUTHOR FLAGS (fixes that would touch a claim, number, citation, quotation or cross-reference)

1. **Stale table labels and caption numbers.** The keys `tab:X-1` (in Section VII), `tab:IX-1` (VIII), `tab:VIII-1` (IX) and `tab:II-2` (IX), and the caption texts "Table X-1.", "Table IX-1.", "Table VIII-1.", "Table II-2.", carry pre-restructure section numbers. If the build prints the caption text literally, readers see wrong numbers. Changing a label or caption number is a cross-reference change.
2. **VII:10 forward reference.** "The failure-mode hypothesis discussed in Section REF(sec:why)" points to a later section (IX), and IX never uses the name "failure-mode hypothesis". The fix is either to move the sec:why subsection earlier (structure) or to reword the reference as a forward pointer; both touch a cross-reference.
3. **Placement of sec:why and of "Relation to neighboring surveys".** Both sit under "How the research lines fit together". Moving them is a document-level decision (Restructure), and Table II-2's label shows the neighboring-surveys material once sat in Section II.
4. **VII:1 S4 "The literature documents six of these failures in a measured case".** It is unclear what "a measured case" means: one study per failure, or a single study. Clarifying it may change the claim's scope.
5. **VII:7 S3 number load** ("50 paired instances from 10 held-out task families", "82% to 96%"). The house style asks for relationships over values in prose. Whether to keep all four numbers is the author's call.
6. **VII:9 S4 has no citation:** "Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite remains fixed."
7. **VII:9 repeats Section V's citations** (`@gao2023overoptimization`, `@shankar2024validators`) for the same claims. Cutting the repetition would remove citations from VII.
8. **VII:5 / VIII:10 / IV repeat VaG's descendants finding** (three statements, one citation, `@shang2026vag`). Deciding which statement stays affects the cross-reference in VIII:10 ("Section REF(sec:findings)").
9. **VII:13 S2**, "Long-context degradation [@liu2023lostmiddle] provides one related mechanism": the evidence for linking lost-in-the-middle to plasticity loss should be confirmed or the link stated more weakly.
10. **VII:14 S3**, "the surface stays largely unmitigated because no surveyed system runs them together": a causal claim and the section's point; its calibration should be confirmed.
11. **VIII Table IX-1**: the SkillForge "(c) partial" has no stated reason, and "not documented" vs. "not reported" may encode a real distinction. Both are data cells.
12. **IX:5 S2**, "GEPA, Meta-Harness, MOSS, RCL, PACE, and the harness-optimization papers all use it": Meta-Harness and MOSS are harness-optimization papers. Rewording to "the other harness-optimization papers" is correct only if that is what is meant.
13. **IX:10 S2–S3** tie growth to two different variables: catalogue size grows "slowly with observed experience", and the intervention budget grows "polylogarithmically with sequence length". Check both against the AoE text (math-claims discipline). The public wording elsewhere is "sublinear".
14. **IX:11 S3 "On that hypothesis"** (singular) after "these hypotheses": the author should confirm whether the argument rests on one hypothesis or both. This is the load-bearing three-paper argument, so do not trim it.
15. **IX:8 S3 "Persistent artifacts offer the cheaper path"**: a cost comparison with no citation.
16. **IX:4 S5 "consequently"**: a causal interpretation of the research history, stated flat.
17. **Table II-2 caption**, "is the only one to cover promotion across organizations": "only" holds among the nine surveys listed. Also, the Guo et al. row's "all four questions" is never defined.
18. **IX:1 S2's problem names vs. the Table VIII-1 "Started from" column**: aligning the wording may mean editing table cells.
19. **VII:3 S2 "major agent frameworks"**: confirm that "major" is the source's own characterization.
20. **Table X-1 "Evaluation fragility" cell**, "read non-independently": the meaning is unclear and may need the author's gloss.

## Group D (VII, VIII, IX): R-2 reverse outline

# Reverse outline, part D: Sections VII, VIII, IX

Word counts exclude citation brackets. "Tests failed" lists ledger columns first, then items from the flags-only table (after the semicolon).

## Paragraphs

| ¶ | role | its point in one sentence | protagonist | themes | evidence | words | tests failed |
|---|---|---|---|---|---|---|---|
| VII_failure_surface:1 | point (section opening) | An improvement loop alters the conditions of its own later decisions, and Table X-1 pairs seven such failures with the loop control that answers each. | failures (of the loop) | loop changes its own context; failures; controls | @sculley2015debt; Table X-1 | 94 | 3.6, 3.7, 4.14; 2.2, 4.15, 4.2 |
| VII_failure_surface:2 | evidence + explanation | Accumulated instructions and skills degrade following and blur attribution, so gated retirement, pruning and expiry keep new edits assessable. | accumulated artifacts (subjects hop) | accumulation; attribution; gated retirement | @jaroslawicz2025ifscale; @zhang2026ratchet | 73 | 3.1, 3.2, 3.7, 4.1, 4.3, 4.9–4.11, 4.14, 5.1, AI; 4.8 |
| VII_failure_surface:3 | evidence | Persistent memory and tool/MCP channels let attackers plant lasting errors. | attacks / channels (tour of systems) | memory poisoning; tool injection; MCP re-approval | @zou2024poisonedrag; @chen2024agentpoison; @xu2026mcfa; @greshake2023injection; @debenedetti2024agentdojo; @checkpoint2025mcpoison | 63 | 2.1, 3.1, 3.2, AI; 4.12, 4.15, one-claim |
| VII_failure_surface:4 | explanation (controls) | Contamination calls for provenance, write gating and reversible memory, plus tool bindings that are re-gated on every later change. | controls; the tool binding | provenance; write gating; tool binding under the gate | @su2026chronomem; @yu2026rollbackrepair; @wallace2024hierarchy | 46 | 2.5, 3.6, 3.7, 4.1, 4.14; 4.5 |
| VII_failure_surface:5 | point | Rollback must track derived artifacts, because restoring a contaminated skill leaves its descendants in place. | rollback | rollback; derivation; descendants | @shang2026vag | 61 | 2.5, 4.1, 4.3, 4.14, AI |
| VII_failure_surface:6 | illustration (subsection opening) | Editing a rubric that also judges later rubric edits makes the improvement process modify its own measuring instrument. | the rubric / the team (hops) | rubric revision; measuring instrument | none (hypothetical example; mirrors the appendix "Pitch review") | 65 | 3.1, 3.6, 4.9–4.11; 2.4 (noted) |
| VII_failure_surface:7 | point (finding) | Three scaffold systems calibrate a judge against people, but none keeps calibration across continuing rubric revisions and drift. | surveyed systems / judge calibration (hops) | reflexive gate; judge calibration; changing criterion | @skillforge2026; @hu2026skillchain; @zhu2026skillcoach | 113 | 2.5, 3.1, 3.7, 4.9–4.11, AI; 2.2, 4.15 |
| VII_failure_surface:8 | other view | Weight-level RL meets the same problem; among co-evolving reward methods only RLPR reports agreement with human labels. | weight-level methods | fixed vs co-evolving judges; human agreement | @gunjal2025rubrics; @jia2025writingzero; @shi2026references; @jin2026rlaes; @yu2025rlpr; @xu2026rubricarm; @ding2026evorubrics; @zhu2026score; @li2026rubricem; Supplementary S6 | 83 | AI |
| VII_failure_surface:9 | point + evidence | A fixed evaluator also degrades with repeated use, so a gate needs held-out checks, calibration and revision history. | the evaluator (subject only in S1) | repeated use; proxy overoptimization; drift; gate safeguards | @gao2023overoptimization; @singh2025leaderboard; @shankar2024validators | 73 | 2.5, 3.1, 3.2, 4.1, 4.3, 5.3, AI; 6.4, 4.12 |
| VII_failure_surface:10 | point | If failures concentrate in recurring modes, evaluation must oversample those modes, keep a held-out check, and test the failure-to-edit link, not just the score. | evaluation | recurring modes; held-out assessment; failure-edit link | @ong2026harnesseval; Section REF(sec:why) | 74 | 3.7, 4.3; 4.15 |
| VII_failure_surface:11 | point + evidence | Multi-agent coordination failures call for treating routing and roles as gated, reversible scaffold coordinates. | failures / routing and roles (hops) | deployment structure; coordination; roles as coordinates | @cemri2025mast | 48 | 3.1, 3.2, 4.1, 4.3 |
| VII_failure_surface:12 | point | A scaffold specialized to one deployment can degrade another; receiving-side evaluation and the evidence radius bound that risk. | a scaffold (hops) | specialization; receiving-side evaluation; evidence radius | none (restates Section II) | 47 | 2.1, 2.5, 3.1, 3.6, 3.7, 4.14, AI; 2.3 |
| VII_failure_surface:13 | point | Accumulated stale artifacts reduce adaptability, so expiry, pruning and rollback must stay available, especially under delayed feedback. | the scaffold (hops) | adaptability (plasticity loss); accumulation; expiry and rollback | @liu2023lostmiddle | 46 | 2.5, 3.1, 3.2, 3.7, 4.1, 4.3, AI; 2.3, 6.3 |
| VII_failure_surface:14 | point (section close) | Each feedback class has characteristic failures, and because no surveyed system runs the controls together, the failure surface stays largely unmitigated. | feedback classes, then production systems | feedback classes; risks; controls run together | Table X-1 (Dominant class column) | 68 | 3.6, 3.7, 4.14, 5.3; 6.3, 2.3 |
| VIII_missing_architecture:1 | point (section opening) | The components (optimizers, release platforms, registries) exist, but no surveyed system connects them so that one organization's improvement is shared with another under controls. | the surveyed systems / components | integration problem; local optimizers; release; registries | none (summarizes IV–VI) | 56 | 3.7 |
| VIII_missing_architecture:2 | transition | The missing combination is audited through four properties. | we | four properties | none | 8 | none |
| VIII_missing_architecture:3 | point (definition) | Property (a): an algorithmic criterion tests each proposed artifact change. | acceptance criterion | auto-gated local loop | none | 14 | 4.12 (list) |
| VIII_missing_architecture:4 | point (definition) | Property (b): artifacts can be promoted across independently governed organizations. | artifacts | cross-organization promotion | none | 13 | 4.14; 2.3, 4.12 |
| VIII_missing_architecture:5 | point (definition) | Property (c): a promoted artifact carries its history and audit trail under access policies. | a promoted artifact | lineage; access control | none | 22 | 4.14; 4.12 |
| VIII_missing_architecture:6 | point (definition) | Property (d): a harmful promotion can be reversed without a full redeploy. | a harmful promotion | rollback | none | 13 | 4.12 |
| VIII_missing_architecture:7 | housekeeping | Cross-tenant means cross-organization here, and sharing within one operator does not satisfy (b). | the terms / within-operator sharing | tenant = organization; operator boundary | none | 26 | 3.2, 3.6, 4.1, 4.14, 5.1 |
| VIII_missing_architecture:8 | evidence | The closest systems each cover some properties, but all stay within one operator, so no system rolls back a cross-organization promotion. | the closest systems | closest systems; one operator; no cross-boundary rollback | @yang2026federatedskill; @nie2026evolvenet; Table IX-1 | 86 | 2.5, 3.6; 2.2 |
| VIII_missing_architecture:9 | point | Receiving-side evaluation is a separate requirement, because a system could have all four capabilities and still promote an artifact that does not help its recipient. | receiving-side evaluation | receiving-side evaluation; promotion decision; recipient benefit | none | 44 | 4.3; 4.6 |
| VIII_missing_architecture:10 | point | The architecture that meets both needs five connected parts, with a recipient check that rejects non-improving promotions and rollback that tracks descendants. | the architecture | five parts; receiving tenant check; rollback envelope | Section REF(sec:findings) (VaG) | 76 | 2.5, 3.7 |
| VIII_missing_architecture:11 | other view | Federated learning is an analogy only where scaffold updates have a mergeable representation, because scaffold systems merge symbolic edits rather than numeric updates. | federated methods vs scaffold systems | representation; averaging; symbolic edits | @mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated; @guo2022promptfl | 71 | 4.14, 5.1; 4.5 |
| VIII_missing_architecture:12 | point | How much of promotion to automate should follow the feedback class: exact checks transfer most directly, outcomes need recipient evaluation, judged quality suits a human gate, delayed outcomes cannot support an immediate gate. | feedback classes | automation extent; feedback classes; promotion gate | none | 93 | 3.7, 4.1, 4.3; 4.12, 2.3 |
| VIII_missing_architecture:13 | point (section close) | The four properties are a target where an automatic local gate is supportable; the common requirement is evidence that stays meaningful where an edit is used, and the ability to reverse it. | the four properties / the common requirement | target; evidence meaningful where used; reversibility | none | 62 | 4.3, 5.1, AI; 4.6 |
| IX_families:1 | point (section opening) | Each research community built the part of the loop closest to its starting problem, which explains the uneven architecture. | research communities | history; starting problems; part of the loop | Table VIII-1 | 49 | 3.6, 3.7; 2.3 |
| IX_families:2 | evidence | Reflective evolution built proposal, RCL the generalization penalty, and harness optimization attribution within the orchestration graph. | research lines | proposal; generalization penalty; attribution | @agrawal2025gepa; @tiwari2026fastandslow; @vassilyev2026rcl; @lee2026metaharness; @lin2026ahe; @cai2026moss; @zehle2026cantante; @nguyen2026harnessevo; @chen2026harnessforge; @li2026growingharness | 69 | 2.1, 2.5, 3.6, 4.9–4.11, AI; 2.4, one-claim |
| IX_families:3 | evidence | The lifecycle line built gated retirement under platform limits; transfer and federation built measurement of how far an edit travels. | research lines | lifecycle hygiene; retirement; transfer | @zhang2026ratchet; @tanjim2026mocha; @liu2026skillsvote; @zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay; @shalev2026ict; @li2026combee; @qu2026coral; @ling2026pace; @wang2026evo2team; @yang2026federatedskill; @nie2026evolvenet | 55 | 2.1, 2.5, 3.2, 4.3; one-claim |
| IX_families:4 | point (explanation) | Because every line inherited its loss from a benchmark and began with trajectories, failure capture lags evaluation and proposal. | research lines (hops) | failure capture lags; inherited loss; attribution within substrate | none (inference from IX:2–3) | 72 | 3.1, 3.2, 4.1, 4.3, 4.14, 5.1; 6.3 |
| IX_families:5 | point | The lines converge on one decomposition (weights plus editable artifacts) and on comparable mechanisms, though none documents the full cross-organization process. | the convergence | convergence; weights/artifacts decomposition; comparable mechanisms | @hebbar2026sia; earlier citations | 77 | 2.5, 3.7, 4.9–4.11, 4.14, AI; 4.12, one-claim |
| IX_families:6 | point (subsection opening) | A general model and a particular deployment have different requirements, and the scaffold encodes the deployment's requirements at a narrower scope. | model vs deployment; the scaffold | different requirements; narrower scope | none | 58 | AI; 1.5 (section) |
| IX_families:7 | evidence | RLHF homogenization and the cost asymmetry between in-context and in-weight adaptation motivate separating broad behavior from customer requirements. | studies / Tiwari et al. (hops) | homogenization; adaptation cost; forgetting | @kirk2024understanding; @padmakumar2023diversity; @tiwari2026fastandslow; @dohare2024loss | 57 | 3.1, 3.2, 3.6, 4.1, 4.3; 2.3, 4.2 |
| IX_families:8 | other view + point | Adapters, distillation and routing can absorb local requirements but add lifecycles, so persistent artifacts are the cheaper path. | alternatives, then persistent artifacts | alternatives; separate lifecycles; cheaper path | @hu2021lora | 39 | 2.5; 6.3 |
| IX_families:9 | evidence (series hypothesis) | Beyond Exponential Decay argues that reliability depends on a sparse set of key decisions, a hypothesis that is limited when decisions grow with the task. | Beyond Exponential Decay | sparse key decisions; long-range dependence; limits | @arbuzov2025beyond | 92 | 3.6, 4.9–4.11, 4.14 |
| IX_families:10 | evidence (series hypothesis) | The Architecture of Errors argues that bounded deployments fail in a slowly growing catalogue of modes, so the intervention budget saturates, though not in unbounded domains. | The Architecture of Errors | catalogue of modes; intervention budget; unbounded domain | @arbuzov2026architecture | 66 | 3.6, 5.1 |
| IX_families:11 | point | If the hypotheses generalize, the gated, scoped artifact layer is the architecture the error structure calls for; the survey's findings do not depend on them. | the artifact layer (hops) | targeted interventions; architecture, not workaround; independence of findings | none (IX:9–10) | 95 | 3.1, 3.7, 4.3, 4.14 |
| IX_families:12 | other view (subsection opening) | Neighboring surveys organize by other axes; this one analyzes the acceptance decision, its feedback and its scope. | surveys | unit of analysis; decision; feedback; scope | Table II-2 | 57 | 4.14, 5.1; 1.5 (section) |
| IX_families:13 | other view | The closest governance precedents (Ding et al., Lin et al.) treat governance or rollback, but neither asks who gates an edit or covers cross-organization promotion. | the two surveys | governance precedents; gate; promotion | @ding2026alwayson; @lin2026memorysecurity | 57 | 2.5 |
| IX_families:14 | other view (lineage) | One-shot prompt optimizers and self-improving harnesses supply underlying mechanisms but are not deployed, promoted loops. | systems (tour) | prompt optimization; not deployed loops; mechanisms | @yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad; @ace2025agentic; @zhou2024symbolic; @zelikman2023stop; @robeyns2025sica | 74 | 2.1, 2.5, 3.1, 3.2, 5.1, 5.3, AI; 1.5 |
| IX_families:15 | point (section close) | The survey's contribution is reading these mechanisms jointly at deployment scope through its corpus, classification, feedback classes and audit. | the contribution (abstract) | joint reading; deployment scope; contributions | Supplementary S7 | 56 | 2.5, 3.1, 3.7, 4.1, 4.3, 4.14, 5.1, AI; 5.2 |

## Sections and subsections

| section | its opening's point sentence, quoted | themes named | order | does the heading carry a theme? |
|---|---|---|---|---|
| VII. How adaptation can undermine its own evidence {#sec:failure} | "An improvement loop changes the context in which its next decision is made." (The section's actual point, "Production systems provide individual controls, but the surface stays largely unmitigated because no surveyed system runs them together", is its last sentence.) | loop alters its own evidence; failures; controls; feedback classes | coordinate (by failure group: accumulation and contamination, evaluator change, scope/coordination/drift), closing on a logical summary by feedback class | yes ("adaptation undermines its own evidence"), although the section's point (controls exist but are not run together) is not in the heading |
| VII.1 Accumulation and contamination | "As instructions accumulate, following them becomes harder and latency increases [@jaroslawicz2025ifscale]." | accumulation; contamination (memory, tools); rollback across derivation | coordinate | partly: it is a two-noun label naming the failure types, not the claim (each needs a gated control) |
| VII.2 When the evaluator changes {#sec:reflexive} | "Consider a pitch-review assistant that consistently overrates decks claiming a large market without supporting numbers." (point sentence: "If the same rubric judges future rubric revisions, the improvement process is modifying its own measuring instrument.") | reflexive gate; judge calibration; evaluator unreliability; recurring modes | logical (example, then finding, then wider evaluator problems, then implication for evaluation) | yes |
| VII.3 Scope, coordination, and drift | "Some failures arise from the structure of the deployment." | coordination; specialization; plasticity; feedback classes | coordinate | no: a three-noun label list |
| VIII. What governed sharing would require {#sec:gap} | "The evidence so far identifies a practical integration problem." (point sentence: "The surveyed systems do not connect these capabilities into a process that learns in one organization and shares the resulting improvement with another under equivalent controls.") | integration problem; four properties; receiving-side evaluation; feedback-dependent automation | logical (problem, then audit properties, then closest systems, then extra requirement, then architecture, then analogy, then scope by feedback) | yes |
| IX. How the research lines fit together {#sec:families} | "The uneven architecture has a history." (point sentence: "Each developed the part of the loop most relevant to its initial problem.") | research lines; starting problems; part of the loop; convergence | coordinate (by research line) for IX:1–5, then two subsections not about research lines | partly: it covers IX:1–5 only; the subsections on specialization and neighboring surveys fall outside it (1.5) |
| IX.1 Why specialization remains outside the weights {#sec:why} | "A general model and a particular deployment face different requirements." | model vs deployment requirements; adaptation cost; series hypotheses; architecture, not workaround | logical | yes; but its placement under IX, and after VII:10 uses it, fails 1.5 |
| IX.2 Relation to neighboring surveys | "Existing surveys organize the field around agent evolution, persistent state, context engineering, skills, memory security, and harness design." (point sentence: "This survey follows a different unit of analysis: the decision that accepts a persistent change, the feedback supporting that decision, and the scope in which the change is subsequently used.") | unit of analysis; governance precedents; prompt-optimization lineage; joint reading | coordinate | no: a topic-label heading ("Relation to ..."); placement as related work at the end of IX fails 1.5 |

## Group E (X, Appendix XI, Appendix XII): S4 diagnostic ledger

# Diagnostic ledger E: Section X (open problems and conclusion), Appendix A (formal), Appendix B (gates)

Stage S4 (Diagnose), review only. Files: `cg_pre/X_open_problems_conclusion.md`, `cg_pre/appA_formal.md`, `cg_pre/appB_gates.md`.

Conventions:
- ¶ ids are `file:N`, N counting prose paragraphs from 1. Tables, display equations and headings are not paragraphs. A display equation inside a paragraph is n/a and is skipped when numbering sentences.
- In Section X the bold run-in head of each open-problem paragraph is called "lead" and is not numbered; S1 is the first sentence after it.
- Cross-document references: "§II" = `I_II_intro_loop.md` (sec:loop), "Intro ¶5/¶6" = paragraphs 5 and 6 of the Introduction, "§IV" = `IV_local_findings.md` line 15, "§V" = `V_feedback_signal_classes.md`, "§VII-A" = `VII_failure_surface.md` (sec:reflexive), "§VIII" = `VIII_missing_architecture.md`, "§IX-A" = `IX_families.md` (sec:why).
- House style (telegrapher style guide + task note) overrides the skill: no em-dashes (none found; the en-dash in "Robbins–Siegmund" is a name compound and correct), American spelling with "analogue" (consistent), mechanism over capability, one claim per paragraph, formal statements are scaffolding and are not to be flattened.

## (a) Mandatory ledger

| ¶ | kind | 2.1 frame | 2.5 redund | 3.1 POV/topics | 3.2 old→new | 3.6 opening stress | 3.7 referents | 3.8 sequence | 4.1 first words | 4.3 nominaliz. | 4.9–4.11 shape | 4.14 endings | 5.1 cuts | 5.3 hedges | 5.5 punct | AI-sweep |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X_open_problems_conclusion:1 | transition (1 sentence, 17 words) | n/a: short transition, exempt from 2.1–2.4 | pass | pass (one clause; subject "The remaining problems") | n/a: first sentence of the section (see 3.7) | pass (close call): ends "the decisions a deployment must make", the promised axis; the five heads that follow are tasks, not decisions | FLAG: S1 "The remaining problems" is presented as old, but nothing in the section, or at the end of §IX, has listed problems that remain | pass | pass | pass | pass | pass | FLAG: S1 "when expressed in terms of" is a phrase where a word does ("stated as") | pass | pass | FLAG: topic-announcement opener ("The remaining problems become more specific when expressed…") that announces rather than claims |
| X_open_problems_conclusion:2 | body (open problem 1: attribution) | pass: lead circles "Attributing", "editable cause" | FLAG: S1 "without identifying the instruction, memory, skill, or tool binding responsible" is the third statement of one proposition with the same list (Intro ¶5 "a failed output rarely identifies which instruction, memory, skill, or tool binding caused it"; §IV "A failed output does not reveal whether its cause was an instruction, a retrieved memory, a skill…") | FLAG: subjects hop "An exact check" → "No surveyed method" → "Slot attribution …, intervention-based attribution …, and contrastive multi-agent attribution" → "Observed outcomes"; attribution, the protagonist, is subject only in S3 | FLAG: S4 opens "Observed outcomes", new after S3's methods; it links back to S1's "exact check" over S3 | pass (close call): S1 ends "tool binding responsible"; the attribution theme is carried by "responsible" | FLAG: S2 "No surveyed method solves this" points to the gerund "identifying" buried in S1's "without" phrase, not to a stated noun | pass | FLAG: S3 subject is three method names with three citations; "provide" arrives after ~10 words plus citations | pass | FLAG: S3 citations interrupt the subject three times before the verb | pass ("responsible", "all substrates", "narrower starting points", "more confounded") | pass | pass (note: S4 "more confounded" is an unanchored comparative; it implies "than an exact check's") | pass | pass |
| X_open_problems_conclusion:3 | body (open problem 2: recipient) | pass: lead circles "improvement at the recipient" | FLAG: S4 "Connecting such checks to provenance, access control, and reversal remains an architectural problem" is X:6's proposition stated one paragraph early; S1 restates §II ("The promotion loop therefore asks for evidence at the receiving scope") | FLAG: subjects hop "A transferred artifact" → "Existing receiving-side checks" / "Evo2Team's failures" → "Federated Agent Optimization" → "Connecting such checks"; receiving-side evaluation holds only S2 and S4 | FLAG: S3 opens "Federated Agent Optimization", new to the section | pass: S1 ends "the receiving deployment's tasks and measure" | FLAG: S2 "show its coverage limits": "its" can be Evo2Team's or the receiving-side check's; grammar points to Evo2Team, sense to the check | pass | FLAG: S4 gerund subject "Connecting such checks to provenance, access control, and reversal" runs 9 words before "remains" | pass | pass | FLAG: S3 ends "does not implement it" with a pronoun (plus citation) in the stress position | pass | pass ("feasible in selected settings" is calibrated) | pass | pass (note: S2 "while" marks a real contrast) |
| X_open_problems_conclusion:4 | body (open problem 3: C3 calibration) | pass: lead circles "calibration", "criterion changes" | FLAG: S2 "no surveyed scaffold system reports calibration maintained through repeated revisions in deployment" restates §VII-A ("No surveyed system reports calibration maintained across continuing rubric revisions and deployment drift"); S3 restates §VII-A's RLPR sentence | FLAG: subjects hop "the open question" → "SkillCoach" → "no surveyed scaffold system" → "The neighboring reward literature" → "A useful solution"; the judge, the protagonist, is never a main-clause subject | FLAG: S2 opens "SkillCoach" and S3 opens "The neighboring reward literature", both new topics in the opening slot | pass (close call): S1's themes (judge, people, rubric revisions) sit in its second half, but the stress lands on "the rubric it applies" | pass (note: "it applies" = the judge; "it scores" = the criterion; both resolve) | pass | FLAG: S1 subject "the open question" + "is"; S3 abstract subject "The neighboring reward literature" | FLAG: S3 "lacks a reported human-agreement result for a co-evolving rubric or judge" freezes the action (no method reports that its co-evolving judge agrees with people) into a noun string | FLAG: S3 tacks the absolute "with RLPR's probability-based reward a distinct case" onto the main clause | FLAG: S3 ends on the exception "a distinct case"; S1 ends "it applies" | pass | FLAG: S3 "The neighboring reward literature also lacks" widens §VII-A's scope ("Among the co-evolving methods reviewed") to a whole literature (AUTHOR FLAG 2) | pass | pass |
| X_open_problems_conclusion:5 | body (open problem 4: C4 delay) | pass: lead circles "improvement", "delayed outcomes" | FLAG: S2–S3 restate §V ("Outcome gains alone are also insufficient to distinguish directed improvement from a successful search… [@ong2026harnesseval]") and §IV ("by downstream score alone, a harness optimizer cannot be told from trial and error [@ong2026harnesseval]"), the third use of one citation for one point; S1 restates Table V-1's C4 row ("No immediate per-edit gate") | FLAG: subjects hop "many edits" / "immediate per-edit acceptance" → "Proxy milestones and proposal pruning" / "downstream gains" → "Harness optimizers" | FLAG: S3 opens "Harness optimizers", not named before in the paragraph; "therefore" asserts a link its opening does not carry | pass (close call): S1's stress "is unavailable" is the point; the theme "per-edit acceptance" sits just before it | pass | pass | FLAG: S1 main subject "immediate per-edit acceptance" (nominalization) + "is unavailable" | FLAG: S1 pattern 1, "immediate per-edit acceptance is unavailable" (a gate cannot accept each edit when it is made) | pass | FLAG: S3 ends "as well as their final scores [cite]": the familiar item takes the stress, while the new demand ("their claims about why particular edits help") sits mid-sentence | pass | pass ("may still be useful" is just right) | pass | FLAG: S3's closing "as well as their final scores" repeats X:4 S4's "as well as the outputs it scores"; two adjacent paragraphs end on the same balance |
| X_open_problems_conclusion:6 | body (open problem 5: governed sharing) | pass: lead circles "local learning", "governed sharing" | FLAG: S3 "evaluate the recipient" repeats problem 2 (X:3); S1 restates Intro ¶6 ("None documents an automatic local improvement loop connected to promotion across organizations with versioned lineage, access control, and rollback") and X:3 S4 | pass (close call): "No surveyed system" → "The components" → "Their integration" → "the design" form a related set about the missing architecture | pass | pass: S1 ends on the four components, "and rollback" | FLAG: S4 "the design" is presented as old; no design is named in the paragraph (the nearest is "Their integration") | pass | FLAG: S3 subject "Their integration" (nominalization) + "must preserve" | FLAG: S3 pattern 1, "Their integration must preserve tenant isolation…" (a system that integrates them must…) | pass | pass ("and rollback", "different systems", "later withdrawn", "delayed evaluation") | pass | pass | pass | pass (S3 triplet carries content) |
| X_open_problems_conclusion:7 | point (conclusion restated) | pass: circles "persistent changes outside the weights", "evidence … fragmented" | pass (closing restatement exempt; note: S2–S3 track Intro ¶5–6 closely) | pass (close call): "The survey's central observation" → "Many systems" → "Fewer" / "the machinery"; systems hold S2–S3 | pass | pass: S1 ends "remains fragmented" | pass ("it addresses" = the local candidate) | pass | FLAG: S1 subject "The survey's central observation" + "is that" | FLAG: S1 pattern 1, "The survey's central observation is that…" (the survey finds that…) | FLAG: S3 (35 words) joins two clauses with different subjects by "and"; the second subject, "the machinery for transferring the resulting improvement to another organization", runs 10 words before "has not been assembled" | FLAG: S3 ends on the scope qualifier "in the public systems examined here" | FLAG: S1 "an important form of adaptation": "important" is an intensifier without a measure (AUTHOR FLAG 11) | pass (note: S3 "Fewer can reliably explain" matches the findings) | pass | FLAG: S1 "important" (intensifier cap is 0); S1 "while" and S2–S3 "Many … Fewer" are two balanced contrasts in 63 words, with X:8's antithesis next |
| X_open_problems_conclusion:8 | point (significance + now what) | pass: two-sentence opening ends "specializes"; circles "generalizes", "specializes", "governing" | FLAG: S1–S3 restate §IX-A's close nearly word for word ("a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization"), which §IX-A frames "On that hypothesis"; here it is stated flat | FLAG: subjects hop "The frontier model" → "The local scaffold" → "Reliability" → "That discipline"; four characters in four sentences | FLAG: S3 opens "Reliability", new to the paragraph and to the conclusion; the old item ("that specialization") sits after the verb | pass (close call): the two-beat opening ends on the theme "specializes"; "governing" arrives in S3 | FLAG: S4 "That discipline" relabels "governing that specialization" with a new noun, which readers must map back | pass | FLAG: S3 abstract subject "Reliability" + empty verb "comes from" | FLAG: S3 "Reliability comes from governing that specialization" (nominalization subject + empty verb) | pass | pass ("generalizes", "specializes", "be reversed", "the adapting system") | pass | FLAG: S3 "Reliability comes from governing" is a flat causal claim; §IX-A states it only conditionally and says "The survey does not test the hypotheses" (AUTHOR FLAG 1) | pass | FLAG: "The frontier model generalizes. The local scaffold specializes." is a tidy antithesis, followed by a colon-reveal triplet ("knowing what …, where …, and how …") in one 46-word paragraph; with X:7 the section is over the cap of about 1 flourish per 500 words (the antithesis echoes the title and is the one to keep) |
| appA_formal:1 | housekeeping (roadmap + scope note, 51 words; carries the "no new theorem" claim, so not exempt) | pass: circles "setup", "descent inequality", "noisy gate", "convergence proposition", "worked cases" | pass | pass (close call): "This appendix" → "No new theorem" → "the proposition" | pass | FLAG: S1 ends on the last roadmap item, "four worked cases"; the appendix's organizing concept (descent under a noisy gate, gate stability) sits mid-list | pass (note: "the proposition" resolves to "an informal convergence proposition", but no later text calls anything a proposition; see flags-only 2.3) | pass | pass | pass | pass (S1 is a 31-word parallel list) | pass ("worked cases", "versioned parameter") | FLAG: S2 "the ordinary target of local stochastic optimization": "target" is vague (the standard result of) | pass | pass | pass |
| appA_formal:2 | explanation (formal setup; display n/a) | pass: circles "fixed parameters", "scaffold", "discrete, symbolic, and versioned" | pass (note: S2 repeats §II's definition of L_D on purpose, so the appendix stands alone) | pass (close call: each sentence defines a new formal object; θ_s and z_t carry most sentences, and the hopping is inherent to a setup) | FLAG: S3 opens on "A candidate edit z_t ∼ Q_t(z \| H_t, θ_s^t)", where Q_t and H_t appear before S3's end defines them; S5 opens on a new term, "The finite directional difference" | pass: S1 ends "discrete, symbolic, and versioned" | pass ("its expected contribution" = mode m's) | pass | pass | pass | FLAG: S4 puts an 18-word conditional ("for a mode m that recurs with frequency f_m and carries per-occurrence loss s_m,") before its subject, then tacks on ", so high-frequency or high-severity modes are proposed first" | pass | pass | FLAG: S4 "so high-frequency or high-severity modes are proposed first" states a modeling assumption about Q_t as fact, and "so" derives a proposal order from an expected contribution (AUTHOR FLAG 4) | pass | pass |
| appA_formal:3 | explanation (formal result + reading; display n/a) | pass: circles "history", "descent bias", "estimator bias" | pass | pass (close call: formal definitions; "expected improvement" and ε_t carry the reading) | pass | FLAG: S1 ends on notation for the history ("together with θ_s^t"); the paragraph's point, expected improvement as margin minus bias, first appears in S5, after the display | FLAG: S5 "the gate's margin" names γ_t + τ_t, while §II defines the margin as τ_t alone ("τ_t≥0 is the acceptance margin") (AUTHOR FLAG 3) | pass | pass | pass | FLAG: S6 (59 words) runs four predicates for ε_t in one comma series; the C1 item embeds an absolute ("with the sampling error of a finite suite over the patch remaining"), and the labels switch form ("in C1" against "(C2)", "(C3)", "(C4)") | pass ("acceptance probability", "delayed signal (C4)") | pass | pass | pass (note: S6's items contain internal commas; semicolons would mark the item boundaries) | pass |
| appA_formal:4 | explanation (convergence: assumptions, sketch, interpretation, scope; 320 words) | pass: circles "conditional statement", "strong assumptions", "gate stability" | FLAG: S3 "(A3) is strong: … which needs attribution far more reliable than success with non-zero probability per failure" is repeated in appA:5 S5; S6 restates §II's "This is gate stability, not a claim of global optimality. A limited proposal process or biased evaluator can leave useful changes undiscovered or rejected." (the formal restatement is a close call) | FLAG: subjects hop "What follows" → imperative "Add" → "(A3)" → "The one-step inequality" → "The finite sum" → "This" → "A non-stationary deployment" → "Recency weighting, pruning, expiry, and rollback"; no character holds the paragraph | FLAG: S7 opens "A non-stationary deployment (D = D_t)" and S8 opens "Recency weighting, pruning, expiry, and rollback", both new; the old item ("that case") closes S8 | FLAG: S1's stress is the disclaimer "nothing in the survey depends on it"; the theme "gate stability" sits mid-sentence | pass (note: S2 "there" = at a non-gate-stable scaffold; S6 "This" = S5's conclusion; S8 "that case" = non-stationary D_t) | pass | FLAG: S1 "What follows is a conditional statement": a what-cleft with an abstract subject and "is" | pass | FLAG: S2 (~75 words) stacks three assumptions, an embedded "so that …" consequence and a trailing "; and let 0 ≤ L_D ≤ B"; S5 (~60 words) chains two colons, a "so" and an "and with (A4)" clause | FLAG: S1 ends "depends on it", S6 "biased to reject it", S7 "which are not supplied here", S8 "for that case": pronoun and scope endings | pass | pass ("(A3) is strong" and "nothing in the survey depends on it" are calibrated) | pass (note: S5 carries two colons in one sentence) | FLAG: three colon reveals in one paragraph ("(A3) is strong:", "The finite sum carries the content:", "falls outside this argument:") |
| appA_formal:5 | explanation (correspondence) | pass: circles "optimization concept", "scaffold analogue" | FLAG: S5 restates appA:4 S3 (A3 needs attribution stronger than "success with non-zero probability per failure"); S3 "Scaffold systems do not differentiate through instruction files" restates §II ("There is no analytic gradient through an instruction file or memory entry") | FLAG: subjects hop "Table REF(tab:A-1)" → "Credit assignment" → "Scaffold systems" / "They" → "The one-step inequality" / "the convergence statement" | FLAG: S5 opens "The one-step inequality", new after S4's account of how systems trace errors | FLAG: S1 is a table pointer ending "its scaffold analogue"; the paragraph's theme, credit assignment as attribution rather than backpropagation, first appears in S2 | pass ("They" = scaffold systems) | pass | pass | pass | FLAG: S5 (49 words) chains "that (A3) assumes, which is much stronger than …, success with …" after a semicolon join: a that-clause, a which-clause and an appositive tacked on | pass (note: S5 ends "per failure", the same ending as appA:4 S3) | pass | pass | pass | pass (note: "attribution, not backpropagation" is the paragraph's one antithesis; with appA:4 S6's "not convergence to an optimum" there are two in about 400 words) |
| appA_formal:6 | illustration (worked case: retrieval) | pass: circles "retrieved context", "decisive clause" | pass | pass: subjects follow the loop ("Failures" → "Attribution" → "The candidate edit" / "the gate") | pass | pass: S1 ends "the decisive clause" | pass | pass (failure → attribution → edit → gate) | pass | pass ("Attribution" is a term of art) | pass | pass | pass | pass | pass (note: S4 "Signal class C1 or C2." is a deliberate label fragment) | pass |
| appA_formal:7 | illustration (worked case: pitch review) | pass: circles "overrates decks", "rubric coordinate" | pass | pass: "The system" / "the failure cluster" → "The edit" / "the gate" → "What the edit changed" follow the loop | pass | pass: S1 ends "under-specified rubric coordinate" | pass | pass | pass (S3 what-cleft is a deliberate stress shift) | pass | pass | pass (close call: S3 ends on the label "class C3" after the stressed "the gate that will judge the next edit") | pass | pass | pass | pass (one colon reveal) |
| appA_formal:8 | illustration (worked case: tool use) | pass: circles "Calls fail", "under-specified" | pass | pass: "Calls" → "The responsible coordinate" → "The edit" / "the gate" | pass | pass: S1 ends "under-specified" | pass | pass | pass | pass | pass | pass ("refusals or latency") | pass | pass | pass ("Class C2." deliberate label fragment) | pass |
| appA_formal:9 | illustration (worked case: memory) | pass: circles "stale customer preference", "bad decisions" | pass | pass: "A stale customer preference" → "The responsible coordinate" → "The edit" / "the gate" → "Class C2" | pass | pass: S1 ends "causes bad decisions" | pass ("it" = the correction) | pass | pass | pass | pass | FLAG: S4 ends "a later outcome reveals it" (pronoun) | FLAG: S4 "observable only when a later outcome reveals it": "observable" and "reveals" state the same thing | FLAG: S3 "the gate checks that future behavior improves": a gate decides at acceptance and cannot observe future behavior, which S4 concedes (AUTHOR FLAG 9) | pass | pass |
| appB_gates:1 | context/point (frames Table B-1) | pass: circles "per-edit test G_t", "estimate of the loss change", "proposal pruning" | pass | FLAG: subjects hop "Section REF(sec:loop)" → "Surveyed systems" / "some of them" → "Table REF(tab:B-1)" | pass | pass (close call: S1 ends "an estimate of the loss change", the hinge the paragraph develops; its point, pruning versus estimators, is S2) | FLAG: S2 "some of them" can be the systems or the "several distinct ways"; the intended referent (gate families) is neither | pass | FLAG: S1 subject is a cross-reference, "Section REF(sec:loop) collapses", which hides the authors as actor | pass | FLAG: S2 (37 words) splits the comparative "better read as proposal pruning … than as estimators" with the relative "that precedes the per-edit gate" | pass | pass (note: "several distinct ways": "distinct" adds little) | pass | pass | pass |
| appB_gates:2 | explanation (two claims: estimator vs pruning; what each signal class leaves) | pass: circles "first five families", "descent guarantee" | FLAG: S2 "Semantic merge and archive selection are not estimators of Δ̂L_D" restates appB:1 S2 ("better read as proposal pruning … than as estimators of Δ̂L_D"); S6 restates Table V-1's C4 row ("No immediate per-edit gate; proposals are pruned and milestones stand in") | FLAG: subjects hop "The first five families" → "Semantic merge and archive selection" / "the descent argument" → "Multi-sample agreement" → imperative "Read" → "The only families" → "A delayed (C4) deployment" / "what it has" → "That"; families give way to deployments at S4 | FLAG: S4 "Read down the signal-class column." switches topic without a link; S5 opens on a new character, "a judged (C3) deployment" | FLAG: S1's stress, "inherit its descent guarantee", names only the first of two themes; the second (what each signal class leaves available) begins at S4 | FLAG: S3 "one that should not be conflated with it": "it" can be mini-batch averaging or the wait-for-k operation | pass | FLAG: S5 subject "The only families available to a judged (C3) deployment" runs 9 words before "are" | pass | FLAG: S3 (40 words) tacks a summative and a second "one that" clause onto a because-clause; S6 joins a main clause and a what-cleft with a colon | FLAG: S3 ends "conflated with it"; S7 ends on the cross-reference "Section REF(sec:signal)" | FLAG: S3 "is listed because" is metadiscourse about the table; S6 "at all" is an intensifier | FLAG: S1 "inherit its descent guarantee" is stronger than Appendix A, which gives a one-step inequality under (A1)–(A2) and says of the convergence statement "nothing in the survey depends on it"; S3 "the correct analogue" is an unhedged "correct" (AUTHOR FLAG 5) | pass | FLAG: intensifiers "correct" and "at all"; colon reveal in S6; summary close "That is the structural content of Section REF(sec:signal)." |

### Extra row: test 1.9 on Section X (conclusion)

| unit | test | result |
|---|---|---|
| Section X | 1.9 restated point · significance · now what | FLAG (partial pass). **Restated point:** present in X:7 S1 ("persistent changes outside the weights have become an important form of adaptation, while the evidence supporting those changes remains fragmented"), but it arrives in the second-last paragraph, after five open problems; the section opens on an announcement (X:1), not the point. **Significance:** X:8 gives it as an aphorism ("The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization"). The aphorism repeats §IX-A almost verbatim, drops that section's "On that hypothesis" condition, and introduces "Reliability", a term the survey never measures; it is not stated in the reader's terms (what a team that ships scaffold edits gains or risks). **Now what:** distributed over X:2–X:6 as five open problems, each with a requirement ("A useful solution must…", "the design must…"). The closing sentence ("That discipline must extend to the evaluations themselves when they become part of the adapting system") names a direction but no actor. **Repeats the introduction?** X:7 S2–S3 track Intro ¶5–6 closely; acceptable as restatement. **New topic?** Only the term "Reliability". **Generic uplift?** No. |

## (b) Flags only (other paragraph-level tests)

| ¶ | test | finding (quote the words) |
|---|---|---|
| X_open_problems_conclusion:1 | 5.2 | Topic announcement: "The remaining problems become more specific when expressed in terms of the decisions a deployment must make." |
| X_open_problems_conclusion:1 | 1.5 (relevance) | Promises a "decisions" frame, but the five heads are tasks ("Attributing…", "Establishing…", "Maintaining…", "Evaluating…", "Connecting…"), and none is phrased as the keep or share decision of §II. |
| X_open_problems_conclusion (section) | 1.7 | The five problems mix three axes: a local-loop step (attribution), promotion (recipient), signal classes (C3 calibration, C4 delay), then architecture (connecting). There is no nameable order, and the two promotion problems (X:3, X:6) are split by the two signal-class problems. |
| X_open_problems_conclusion (section) | 1.8 | Heading "Open problems and conclusion" is a label, not a theme. |
| X_open_problems_conclusion (section) | 2.3 | Reversal vocabulary drifts: "reversal" (X:3), "rollback" (X:6), "withdrawn" (X:6), "reversed" (X:8). Lineage vocabulary drifts: "provenance" (X:3) against "versioned lineage" (X:6). |
| X_open_problems_conclusion:2 | 4.8 | S3 whole subject "Slot attribution [@nguyen2026harnessevo], intervention-based attribution [@chu2026agentgrad], and contrastive multi-agent attribution [@zehle2026cantante]" is about 10 words plus three citations. |
| X_open_problems_conclusion:2 | 4.15 | "Slot attribution", "intervention-based attribution" and "contrastive multi-agent attribution" are unglossed; the reader cannot tell what each attributes to what. |
| X_open_problems_conclusion:3 | 4.15 | "unseen graphs": the conclusion reader meets "graphs" without §VI's context (Evo2Team routes over team graphs). "receiving-client gate" is a new term. |
| X_open_problems_conclusion:4 | 4.7 | Noun string "a reported human-agreement result". |
| X_open_problems_conclusion:4 | 4.15 | "human-gold references", "co-evolving" and "RLPR" are unglossed in the conclusion; "with RLPR's probability-based reward a distinct case" is opaque without §VII-A. |
| X_open_problems_conclusion:4 | 6.3 | S3 "The neighboring reward literature also lacks" claims more than §VII-A's "Among the co-evolving methods reviewed" supports (AUTHOR FLAG 2). |
| X_open_problems_conclusion:5 | 4.5 | S3 "Harness optimizers should therefore be assessed" is an agentless passive; who assesses (benchmark authors? reviewers?) is not stated. |
| X_open_problems_conclusion:6 | 4.12 | S1 coordinates a loop property ("automatic local acceptance") with three architecture parts ("promotion across organizations, versioned lineage with access control, and rollback"); §VIII lists five parts. The lists differ (AUTHOR FLAG 12). |
| X_open_problems_conclusion:7 | 4.8 | S3 second subject "the machinery for transferring the resulting improvement to another organization" (10 words, contains a nominalization). |
| X_open_problems_conclusion:7 | 4.12 | S3 "Fewer can reliably explain …, and the machinery … has not been assembled": "and" joins unlike subjects and hides an escalation ("and beyond that"). |
| X_open_problems_conclusion:7 | 6.3 | S1 "have become an important form of adaptation": the survey counts systems; it does not measure importance (AUTHOR FLAG 11). |
| X_open_problems_conclusion:8 | 4.15 | "Reliability" first appears as a key term in the final paragraph. |
| X_open_problems_conclusion:8 | 6.2 / 6.3 | Plain paraphrase: "Models generalize; scaffolds specialize; govern the scaffold by recording what each change improved, where, and how to undo it." The paraphrase shows the closing claim rests on §IX-A's untested hypothesis, stated here without its condition (AUTHOR FLAG 1). |
| appA_formal:1 | 2.3 | One object, four names: "an informal convergence proposition" (appA:1), "a conditional statement" (appA:4 S1), "the result" (appA:4 S6), "the convergence statement" (appA:5 S5). |
| appA_formal:1 | 4.6 | S2 "No new theorem is claimed" is a passive on the writers' own claim ("We claim no new theorem"). |
| appA_formal:1 | 1.5 (placement) | Table A-1 sits before "Setup" but is discussed in "Correspondence", four subsections later. |
| appA_formal:2 | 2.3 | "the six substrate coordinates of Section REF(sec:method)" fuses §III's "substrates" with §II's "coordinate" (an editable part, such as one memory entry) (AUTHOR FLAG 10). |
| appA_formal:2 | 4.15 | ⊕ is used in S5 ("θ_s ⊕ z") and in Table A-1 ("under ⊕") without definition; "mode" is used without recalling §II's definition. |
| appA_formal:2 | 3.5 | S4 "so high-frequency or high-severity modes are proposed first": the "so" claims a consequence that is an assumption about Q_t, and "or" does not match the product f_m s_m (AUTHOR FLAG 4). |
| appA_formal:3 | 2.2 / 2.4 | The framing sentence ("Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability.") comes after the display, and the paragraph opens on definitions. |
| appA_formal:3 | 4.12 | S6 series not parallel: "near zero … in C1, with …", "bounded by batching … (C2)", "equal to … and bounded only by … (C3)", "unavailable per edit … (C4)". |
| appA_formal:4 | 2.2 / 2.4 | Eight sentences and five jobs (assumptions, proof sketch, interpretation, non-stationary scope, continual-learning analogy). The point ("This is convergence of the loss and stability of the gate decision, not convergence to an optimum") is S6, mid-paragraph. This breaks the house rule of one claim per paragraph. |
| appA_formal:4 | 4.15 | "effective compactness of the reachable orbit", "admissible edit" and "non-gate-stable" are unglossed. |
| appA_formal:4 | 6.5 | A dense passage whose one-line justification ("included to make gate stability precise") is in S1 but whose structure does not show the reader where the result ends and the caveats begin. |
| appA_formal:5 | 1.5 (placement) | S1 "Table REF(tab:A-1) pairs each optimization concept…" points to a table placed at the appendix head. |
| appA_formal:7 | 5.6 | Tense shift: "What the edit changed was" (past) inside present-tense cases ("overrates", "points", "changes", "runs"). |
| appA_formal:7 | cross-ref | "the reflexive gate of Section REF(sec:signal)": §II and §V send the reader to Section REF(sec:reflexive) for its development (AUTHOR FLAG 8). |
| appA_formal:6–9 | 2.3 | Label form varies: "Signal class C1 or C2." (appA:6), ", class C3." (appA:7), "Class C2." (appA:8, appA:9). |
| appA_formal (worked cases) | 1.7 | The cases run retrieval (C1/C2), pitch review (C3), tool use (C2), memory (C2); the order follows neither signal class nor substrate. |
| appB_gates:1 | 4.2 | S1 "Section REF(sec:loop) collapses every production gate" puts a section where the authors act ("We collapsed…"). |
| appB_gates (Table B-1 cells) | caption/cell | Caption is fine. Cell problems: "Surrogate verifier" (a C1 family) lists "Voyager (game-state check: C2)"; the same row's "DGM (… score weights selection, not retention)" sits in a "Per-edit gate G_t" row although the note says the score does not decide retention; "Multi-sample agreement" states "false-accept rate decays as p^k rather than variance as 1/k", which holds only for independent errors with an all-must-pass rule (AUTHOR FLAGS 6, 7). |
| appB_gates:2 | 2.4 (one claim) | Two claims in one paragraph: S1–S3 (which families are estimators and which are pruning) and S4–S7 (what each signal class leaves available). |
| appB_gates:2 | 4.6 / 5.2 | S3 "Multi-sample agreement is listed because" is metadiscourse about the table. S7 "That is the structural content of Section REF(sec:signal)" is a summary close. |

## (c) Suggested moves (one per FLAG; what to do, not a rewrite)

| ¶ | test | move |
|---|---|---|
| X:1 | 3.7 | State what the problems remain after (the findings), or replace the sentence with the claim that organizes the five problems. |
| X:1 | 5.1 | Replace "when expressed in terms of" with a verb ("stated as"). |
| X:1 | AI-sweep | Turn the announcement into a claim that names the ordering axis of the problems, or cut it and let the first head open the section. |
| X:2 | 2.5 | Keep the gap in one short clause that points back to §IV; spend the sentence on what a solution must do. |
| X:2 | 3.1 | Make attribution (or "a method") the subject of most clauses; put the three methods after the verb. |
| X:2 | 3.2 | Move S4 next to S1 (both are about signal type), or open S4 on the old item ("Attribution is harder still when…"). |
| X:2 | 3.7 | Replace "this" with the noun ("this attribution"). |
| X:2 | 4.1 | Lead with a short subject and verb ("Three narrower methods offer starting points:") and list the methods after it. |
| X:2 | 4.9–4.11 | Same move as 4.1: move the citations into the post-verb list. |
| X:3 | 2.5 | Drop S4, which X:6 owns, or reduce it to a pointer to X:6. |
| X:3 | 3.1 | Make "receiving-side evaluation" (or "a receiving-side check") the running subject. |
| X:3 | 3.2 | Open S3 on the old item ("A receiving-client gate has been proposed by Federated Agent Optimization [cite] but not implemented"), keeping the claim. |
| X:3 | 3.7 | Repeat the noun ("the coverage limits of such checks") or name Evo2Team's check. |
| X:3 | 4.1 | Shorten the gerund subject, or make the actor ("No system yet connects…") the subject. |
| X:3 | 4.14 | End S3 on "not implemented" or "unimplemented", not "it". |
| X:4 | 2.5 | Point back to §VII-A for the evidence and keep only the open question plus the requirement in S4. |
| X:4 | 3.1 | Make the judge (or "a co-evolving judge") the subject of most clauses. |
| X:4 | 3.2 | Open S2 and S3 on old information (the judge, calibration) and put SkillCoach and the reward literature after the verb. |
| X:4 | 4.1 | Replace "the open question is how" with a character subject ("A judge must stay aligned…"). |
| X:4 | 4.3 | Unfreeze "lacks a reported human-agreement result" into a verb clause about reporting agreement. |
| X:4 | 4.9–4.11 | Split the RLPR exception into its own clause, or move it before the main claim. |
| X:4 | 4.14 | End S3 on the gap, not on "a distinct case"; end S1 on "rubric revisions" rather than "it applies". |
| X:4 | 5.3 | Author decides the scope wording (AUTHOR FLAG 2); no prose-only fix. |
| X:5 | 2.5 | Point back to §V for the argument and drop the third citation of ong2026harnesseval, or keep only the new requirement. |
| X:5 | 3.1 | Make "a delayed-outcome loop" (or "the evaluator") the running subject. |
| X:5 | 3.2 | Open S3 on old information (the attribution claim) before naming harness optimizers. |
| X:5 | 4.1 | Give S1 a character subject ("no gate can accept each edit as it is made"). |
| X:5 | 4.3 | Same as 4.1. |
| X:5 | 4.14 | Reorder S3 so "their claims about why particular edits help" lands in the stress position. |
| X:5 | AI-sweep | Vary the close of X:4 or X:5 so that two adjacent paragraphs do not end on "as well as". |
| X:6 | 2.5 | Drop "evaluate the recipient" (X:3 owns it) and keep the two requirements new here (tenant isolation, derived artifacts). |
| X:6 | 3.7 | Replace "the design" with "an integrated system" or the noun used in S3. |
| X:6 | 4.1 | Make the system the subject ("A system that integrates them must…"). |
| X:6 | 4.3 | Same as 4.1. |
| X:7 | 4.1 | Make the survey or the systems the subject ("The survey finds that…", or state the claim directly). |
| X:7 | 4.3 | Same as 4.1. |
| X:7 | 4.9–4.11 | Split S3 at "and"; move the scope qualifier to the front. |
| X:7 | 4.14 | Move "in the public systems examined here" to the front of the clause. |
| X:7 | 5.1 | Cut "important" or replace it with the measured relationship; author decides (AUTHOR FLAG 11). |
| X:7 | AI-sweep | Keep one contrast (the "Many … Fewer" pair) and state S1 without the "while" balance. |
| X:8 | 2.5 | Either point back to §IX-A for the aphorism or rephrase it so it adds the conclusion's own content (author must decide on the hypothesis condition). |
| X:8 | 3.1 | Keep the scaffold, or its governance, as the subject from S3 on. |
| X:8 | 3.2 | Open S3 on "That specialization" (old) and put the reliability claim after the verb. |
| X:8 | 3.7 | Reuse "governing" or "governance" instead of introducing "discipline". |
| X:8 | 4.1 | Give S3 an actor subject (who governs: the deployment or its team). |
| X:8 | 4.3 | Same as 4.1. |
| X:8 | 5.3 | Author decides whether to restore §IX-A's condition (AUTHOR FLAG 1). |
| X:8 | AI-sweep | Keep the title-echo antithesis; turn the colon-triplet into a plain sentence or keep it and drop X:7's "while" balance. |
| appA:1 | 3.6 | End S1 on the appendix's organizing concept (descent under a noisy gate), with the roadmap items before it. |
| appA:1 | 5.1 | Replace "ordinary target" with a precise phrase ("the standard result"), if the author agrees it means the same. |
| appA:2 | 3.2 | Name the proposal process and history before the symbol (as in "A proposal process Q_t, conditioned on the history H_t of …, draws a candidate edit z_t"). |
| appA:2 | 4.9–4.11 | Split S4: first the contribution f_m s_m, then the assumption about proposal order. |
| appA:2 | 5.3 | Mark the proposal order as an assumption (author decides, AUTHOR FLAG 4). |
| appA:3 | 3.6 | Open with the reading ("Expected improvement per step is the margin minus the bias, weighted by acceptance") or a one-line statement of what the inequality shows, then the definitions. |
| appA:3 | 3.7 | Author decides the name for γ_t + τ_t (AUTHOR FLAG 3). |
| appA:3 | 4.9–4.11 | Turn S6 into a semicolon series or a four-item list with one label form ("In C1, …; in C2, …"). |
| appA:4 | 2.5 | Keep the (A3) strength caveat in one place (here or appA:5) and point to it from the other. |
| appA:4 | 3.1 | Split into paragraphs by job (assumptions; sketch and result; what it does not show; non-stationary scope), each with one running subject; keep all math verbatim. |
| appA:4 | 3.2 | In the scope paragraph, open on old information ("The argument assumes a fixed deployment D") and end on the continual-learning analogues. |
| appA:4 | 3.6 | End S1 on "gate stability", with the disclaimer earlier or in its own sentence. |
| appA:4 | 4.1 | Replace the what-cleft with a direct subject ("The convergence statement below is conditional…"). |
| appA:4 | 4.9–4.11 | Set the assumptions (A3)–(A5) as a list; split S5 at its second colon. |
| appA:4 | 4.14 | Trim the pronoun and scope endings ("we do not supply them" → end on "rate of drift and of adaptation"; end S8 on "continual learning"). |
| appA:4 | AI-sweep | Keep one colon; turn the other two into periods or "because". |
| appA:5 | 2.5 | Merge S5 with appA:4 S3, keeping it in one place. |
| appA:5 | 3.1 | Make credit assignment (attribution) the running subject. |
| appA:5 | 3.2 | Open S5 on old information (attribution) and end on the two results it supports. |
| appA:5 | 3.6 | Lead with the attribution claim; move the table pointer into it or to the end. |
| appA:5 | 4.9–4.11 | Split S5 at the semicolon and reduce the that/which/appositive chain. |
| appA:9 | 4.14 | End S4 on "a later outcome". |
| appA:9 | 5.1 | Keep one of "observable" or "reveals". |
| appA:9 | 5.3 | Author decides what the gate checks at acceptance (AUTHOR FLAG 9). |
| appB:1 | 3.1 | Make the gate (or "gate families") the running subject; demote the section and table to prepositional pointers. |
| appB:1 | 3.7 | Replace "some of them" with "some families" (or "some of these instantiations"). |
| appB:1 | 4.1 | Put the authors or the gate in subject position ("Section REF(sec:loop) models every production gate as…" → "We model…"). |
| appB:1 | 4.9–4.11 | Move "that precedes the per-edit gate" after the comparison, or into its own clause. |
| appB:2 | 2.5 | Drop S2's restatement of appB:1 and keep only its new content (the descent argument applies to pruning composed with the gate). |
| appB:2 | 3.1 | Split at S4: one paragraph with families as subject, one with the deployment (by signal class) as subject. |
| appB:2 | 3.2 | Give the second paragraph an opening that links to the table's signal-class column as old information. |
| appB:2 | 3.6 | After the split, each paragraph's opening ends on its own theme. |
| appB:2 | 3.7 | Repeat the noun ("conflated with mini-batch averaging"). |
| appB:2 | 4.1 | Shorten the S5 subject ("A judged (C3) deployment can use only the two families whose estimator is a judge"). |
| appB:2 | 4.9–4.11 | Split S3's tacked-on clauses; replace S6's colon with a period. |
| appB:2 | 4.14 | End S3 on "mini-batch averaging"; end S7 on its content, not on a cross-reference, or cut S7. |
| appB:2 | 5.1 | Cut "is listed because" and "at all". |
| appB:2 | 5.3 | Author decides on "guarantee" and "correct" (AUTHOR FLAG 5). |
| appB:2 | AI-sweep | Cut the summary close (S7) or make it a substantive final claim; drop the intensifiers. |

## (d) Role-level verdicts

| ¶ | role-level test failed / passage-test failures (2.5, 3.1, 3.2, 3.6, 3.7, 3.8) | verdict |
|---|---|---|
| X_open_problems_conclusion:1 | none role-level (1.5 note only); 1 passage failure (3.7) | keep-and-polish (or cut, if the problems get an organizing claim elsewhere) |
| X_open_problems_conclusion:2 | 4 passage failures (2.5, 3.1, 3.2, 3.7) | re-draft |
| X_open_problems_conclusion:3 | 4 passage failures (2.5, 3.1, 3.2, 3.7) | re-draft |
| X_open_problems_conclusion:4 | wrong protagonist (3.1: the judge is never a subject; the fix is not a pronoun); 3 passage failures (2.5, 3.1, 3.2) | re-draft |
| X_open_problems_conclusion:5 | 3 passage failures (2.5, 3.1, 3.2) | re-draft |
| X_open_problems_conclusion:6 | 2 passage failures (2.5, 3.7) | keep-and-polish |
| X_open_problems_conclusion:7 | 0 passage failures | keep-and-polish |
| X_open_problems_conclusion:8 | wrong protagonist (3.1: model → scaffold → reliability → discipline); 4 passage failures (2.5, 3.1, 3.2, 3.7) | re-draft (the content needs an author decision first, AUTHOR FLAG 1) |
| appA_formal:1 | 1 passage failure (3.6) | keep-and-polish |
| appA_formal:2 | 1 passage failure (3.2) | keep-and-polish |
| appA_formal:3 | 2 passage failures (3.6, 3.7) | keep-and-polish |
| appA_formal:4 | wrong protagonist (3.1: eight subjects across five jobs); 4 passage failures (2.5, 3.1, 3.2, 3.6) | re-draft (split by job; all math and assumptions verbatim) |
| appA_formal:5 | relevance/placement 1.5 (points to a table placed four subsections earlier); 4 passage failures (2.5, 3.1, 3.2, 3.6) | re-draft |
| appA_formal:6 | 0 | keep-and-polish |
| appA_formal:7 | 0 | keep-and-polish |
| appA_formal:8 | 0 | keep-and-polish |
| appA_formal:9 | 0 | keep-and-polish |
| appB_gates:1 | 2 passage failures (3.1, 3.7) | keep-and-polish |
| appB_gates:2 | 5 passage failures (2.5, 3.1, 3.2, 3.6, 3.7); one claim per paragraph broken | re-draft (split at S4) |

## AUTHOR FLAGS (fixes that would touch a claim, number, citation, quotation or cross-reference)

1. **X_open_problems_conclusion:8 S1–S3.** "The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization" repeats §IX-A ("a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization"). §IX-A conditions it ("On that hypothesis") and adds "The survey does not test the hypotheses". Here it is stated flat. Restoring the condition, or keeping it unconditional, changes claim strength, so the author must decide.
2. **X_open_problems_conclusion:4 S3.** "The neighboring reward literature also lacks a reported human-agreement result for a co-evolving rubric or judge" widens §VII-A's "Among the co-evolving methods reviewed, only RLPR reports agreement with human labels" from the methods reviewed to a whole literature. Narrowing it is a claim change.
3. **appA_formal:3 S5.** "Per-step expected improvement is the gate's margin minus its estimator bias": the inequality's term is p_t(γ_t + τ_t), but §II defines the acceptance margin as τ_t ("τ_t≥0 is the acceptance margin"). Should the reading say "the margin plus the descent bias γ_t"? That is a change to a stated interpretation of the math.
4. **appA_formal:2 S4.** "Q_t is not uniform: … its expected contribution to the failure rate is f_m s_m, so high-frequency or high-severity modes are proposed first." This states a modeling assumption as a consequence. "high-frequency or high-severity" also does not match ranking by the product f_m s_m (a frequent mode of near-zero severity has a small product). Rewording changes the model statement.
5. **appB_gates:2 S1 and S3.** "inherit its descent guarantee": Appendix A gives a one-step inequality under (A1)–(A2), and of the convergence statement it says "nothing in the survey depends on it"; "guarantee" may overstate. S3 "the correct analogue" is also unhedged. Both are claim-strength words.
6. **Table B-1, "Multi-sample agreement" row.** "false-accept rate decays as p^k rather than variance as 1/k" holds for independent errors under an all-must-pass rule (VaG fits that description); SkillOpt-Lite's "consensus filter across rollouts" may be a majority rule. This is a mathematical claim, so check it.
7. **Table B-1, "Surrogate verifier" row.** It lists "Voyager (game-state check: C2)" in a C1 family, and "DGM (sandboxed compile-and-edit check; score weights selection, not retention)" in a row whose slot is "Per-edit gate G_t", although the note says the score does not decide retention. These are coding decisions, not prose.
8. **appA_formal:7.** "the reflexive gate of Section REF(sec:signal)": the term is introduced in §V (sec:signal), but §II and §V both send the reader to Section REF(sec:reflexive) for its development. The author may prefer sec:reflexive. That is a cross-reference change.
9. **appA_formal:9 S3.** "the gate checks that future behavior improves": a gate decides at acceptance and cannot observe future behavior (S4 concedes that the correction is "observable only when a later outcome reveals it"). Rewording (for example to replayed or held-out cases) changes what the gate is claimed to check.
10. **appA_formal:2 S1.** "the six substrate coordinates of Section REF(sec:method)": Θ_1 … Θ_6 are §III's substrates, but §II defines a coordinate as "an editable part of the scaffold" (e.g., one memory entry), which is finer. This is a terminology choice inside a formal definition.
11. **X_open_problems_conclusion:7 S1.** "have become an important form of adaptation": cutting the intensifier "important" weakens the significance claim; the survey counts systems and does not measure importance.
12. **X_open_problems_conclusion:6 S1.** The conclusion lists four components ("automatic local acceptance, promotion across organizations, versioned lineage with access control, and rollback"). §VIII lists five parts (per-tenant pools with provenance, isolation-respecting aggregation, receiving evaluation, lineage and access control, reversal), and the abstract lists five (evaluation, shared artifact pools, lineage, access control, rollback). This is a consistency check; aligning the lists changes a stated finding.

## Group E (X, Appendix XI, Appendix XII): R-2 reverse outline

# Reverse outline E: Section X, Appendix A, Appendix B

Word counts are approximate: they include citation keys, and for appendix paragraphs, inline math tokens. "Tests failed" lists the mandatory-ledger FLAGs plus the main flags-only items from `ledger_E.md`.

## Paragraphs

| ¶ | role | its point in one sentence | protagonist | themes | evidence | words | tests failed |
|---|---|---|---|---|---|---|---|
| X_open_problems_conclusion:1 | housekeeping | The open problems are sharper when stated as decisions a deployment must make. | "the remaining problems" | open problems; deployment decisions | none | 17 | 3.7, 5.1, AI-sweep, 5.2, 1.5 |
| X_open_problems_conclusion:2 | problem | No surveyed method attributes a failure to its responsible artifact across all substrates; three methods offer narrower starts, and observed outcomes make it harder. | none held (check → method → methods → outcomes); should be attribution | attribution; editable cause; substrates | nguyen2026harnessevo, chu2026agentgrad, zehle2026cantante | 61 | 2.5, 3.1, 3.2, 3.7, 4.1, 4.9–4.11, 4.8, 4.15 |
| X_open_problems_conclusion:3 | problem | Receiving-side evaluation is feasible in selected settings but limited in coverage and not connected to provenance, access control and reversal. | receiving-side checks (shares slots with artifact, FAO) | receiving deployment; receiving-side checks; coverage limits | Evo2Team (via §VI), yang2026fao | 65 | 2.5, 3.1, 3.2, 3.7, 4.1, 4.14, 4.15 |
| X_open_problems_conclusion:4 | problem | No surveyed system keeps a judge calibrated to people while its rubric keeps changing; a solution must evaluate the moving criterion too. | none held (question → SkillCoach → systems → literature → solution); should be the judge | judge calibration; rubric revisions; co-evolving criterion | zhu2026skillcoach; RLPR (via §VII-A) | 93 | 2.5, 3.1, 3.2, 4.1, 4.3, 4.9–4.11, 4.14, 5.3, 4.7, 4.15, 6.3 |
| X_open_problems_conclusion:5 | problem | With delayed outcomes no per-edit gate exists, so harness optimizers should be judged on their attribution claims, not only their final scores. | none held (acceptance → milestones → optimizers) | delayed outcomes; per-edit acceptance; attribution claims | ong2026harnesseval | 58 | 2.5, 3.1, 3.2, 4.1, 4.3, 4.14, AI-sweep, 4.5 |
| X_open_problems_conclusion:6 | problem | No system combines local acceptance with governed cross-organization promotion; an integration must preserve isolation, evaluate the recipient, handle withdrawn changes, and keep human or delayed decisions where feedback is weak. | the missing system / its integration | governed sharing; components; tenant isolation; withdrawal | none (restates §VIII) | 67 | 2.5, 3.7, 4.1, 4.3, 4.12 |
| X_open_problems_conclusion:7 | point | Persistent changes outside the weights are a major form of adaptation, but their evidence is fragmented: local tests are common, attribution is weak, and cross-organization transfer is unassembled. | systems | persistent changes; fragmented evidence; local test; transfer | none (restates findings) | 63 | 4.1, 4.3, 4.9–4.11, 4.14, 5.1, AI-sweep, 4.8, 4.12, 6.3 |
| X_open_problems_conclusion:8 | point (significance + now what) | Reliability comes from governing the scaffold's specialization (what it improved, where, how to reverse it), and that governance must cover the evaluations too. | none held (model → scaffold → reliability → discipline) | generalize / specialize; governing; reversibility; evaluations | none (echoes §IX-A) | 46 | 2.5, 3.1, 3.2, 3.7, 4.1, 4.3, 5.3, AI-sweep, 4.15, 6.2/6.3 |
| appA_formal:1 | housekeeping | The appendix formalizes the loop and claims no new theorem; the proposition is standard local stochastic optimization on a discrete, versioned parameter. | the appendix | setup; descent inequality; convergence; correspondence; worked cases | none | 51 | 3.6, 5.1, 2.3, 4.6, 1.5 (table placement) |
| appA_formal:2 | explanation | The scaffold is a discrete versioned parameter edited by a history-conditioned proposal process, with a gate that sees only a noisy estimate of each edit's loss change. | the scaffold θ_s and the edit z_t | fixed model; discrete scaffold; proposal Q_t; noisy estimate | §III (substrates), §II (L_D) | ~160 | 3.2, 4.9–4.11, 5.3, 2.3, 4.15, 3.5 |
| appA_formal:3 | explanation | Under positive descent bias and bounded estimator bias, expected per-step improvement is the margin minus the bias, weighted by acceptance probability, and the bias term differs by signal class. | the expected loss change (ε_t in S6) | conditioning on history; descent bias; estimator bias; signal classes | §V (signal classes) | ~180 | 3.6, 3.7, 4.9–4.11, 2.2/2.4, 4.12 |
| appA_formal:4 | explanation | Under strong added assumptions the loss converges and the gate becomes stable, which is not convergence to an optimum and does not cover a drifting deployment. | none held (eight subjects) | gate stability; (A3)–(A5); Robbins–Siegmund; non-stationarity | robbins1971convergence | 320 | 2.5, 3.1, 3.2, 3.6, 4.1, 4.9–4.11, 4.14, AI-sweep, 2.2/2.4, 4.15, 6.5 |
| appA_formal:5 | explanation | Scaffold credit assignment is attribution, not backpropagation; the one-step inequality needs only positive expected descent, while convergence needs far more reliable attribution. | none held (table → credit assignment → systems → inequality) | correspondence; attribution vs backpropagation; strength of (A3) | Table A-1; §II | 86 | 2.5, 3.1, 3.2, 3.6, 4.9–4.11, 1.5 |
| appA_formal:6 | evidence (worked case) | A retrieval failure is traced to a retrieval coordinate, edited, and gated on recall and accuracy without regressions (C1 or C2). | the loop's steps (failures → attribution → edit → gate) | retrieval coordinate; chunking; patch evaluation | none (hypothetical case) | 63 | none |
| appA_formal:7 | evidence (worked case) | A rubric edit in pitch review changes the gate that judges later edits, the reflexive case (C3). | the loop's steps | rubric coordinate; held-out decks; reflexive gate | §V cross-ref | 76 | 5.6, cross-ref (AUTHOR FLAG 8) |
| appA_formal:8 | evidence (worked case) | A tool-call failure is traced to schema, policy or clarification rule and gated on fewer failures without more refusals or latency (C2). | the loop's steps | tool schema; call policy; tool-call failures | none | 48 | 2.3 (label form) |
| appA_formal:9 | evidence (worked case) | A stale memory entry is corrected, expired or tagged and gated on behavior without losing useful history; the correction is visible only through a later outcome (C2). | the loop's steps | memory entry; provenance; expiry; later outcome | none | 60 | 4.14, 5.1, 5.3 |
| appB_gates:1 | point (frames table) | Surveyed systems instantiate the single per-edit gate in several ways, some of which are proposal pruning rather than loss estimators. | none held (section → systems → table) | per-edit gate; loss-change estimate; proposal pruning; signal class | Table B-1 | 68 | 3.1, 3.7, 4.1, 4.9–4.11, 4.2 |
| appB_gates:2 | explanation | Five families are gates and two are pruning; reading by signal class, judged deployments have only judge-based gates and delayed ones have no per-edit gate at all. | none held (families → deployments) | gate vs pruning; multi-sample agreement; C3/C4 availability | Table B-1; Appendix A; §V | 145 | 2.5, 3.1, 3.2, 3.6, 3.7, 4.1, 4.9–4.11, 4.14, 5.1, 5.3, AI-sweep, 2.4, 4.6/5.2 |

## Sections and subsections

| section | its opening's point sentence, quoted | themes named | order | does the heading carry a theme? |
|---|---|---|---|---|
| X. Open problems and conclusion | "The remaining problems become more specific when expressed in terms of the decisions a deployment must make." (The section's real point is X:7 S1: "persistent changes outside the weights have become an important form of adaptation, while the evidence supporting those changes remains fragmented.") | decisions; open problems (opening); fragmented evidence, governing specialization (end) | coordinate (five problems in mixed order: loop step, promotion, C3, C4, architecture), then point; no nameable principle orders the problems | No: "Open problems and conclusion" is a label |
| Appendix A. Formal statement of artifact-layer descent | "This appendix states the setup behind Section REF(sec:loop), a one-step descent inequality under a noisy gate, an informal convergence proposition, the optimization-analogy correspondence, and four worked cases." | descent inequality; noisy gate; convergence; correspondence | logical (setup → inequality → convergence → correspondence → cases), but Table A-1 sits before Setup | Yes ("artifact-layer descent") |
| A. Setup | "Let the frontier model have fixed parameters θ_M and let the scaffold be a structured object θ_s ∈ Θ_s = Θ_1 × ⋯ × Θ_6 over the six substrate coordinates of Section REF(sec:method); Θ_s is discrete, symbolic, and versioned." | fixed model; discrete versioned scaffold | logical (objects → loss → proposal → estimate → update) | No (label; acceptable in a formal appendix) |
| A. Descent inequality | "Write F_t for the history up to step t: the failures, corrections, edits, and gate decisions in H_t together with θ_s^t." (Point arrives in S5: "Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability.") | history; descent bias; estimator bias | logical (definitions → assumptions → inequality → reading → per-class reading) | Partly (names the result, not what it shows) |
| A. Convergence (informal) | "What follows is a conditional statement under strong assumptions, included to make gate stability precise; nothing in the survey depends on it." | gate stability; conditional | logical (assumptions → sketch → result → not-an-optimum → scope), all in one paragraph | No (label) |
| A. Correspondence | "Table REF(tab:A-1) pairs each optimization concept with its scaffold analogue." | optimization analogue; attribution not backpropagation | logical | No (label) |
| A. Worked cases | "*Retrieval.* Failures recur because retrieved context omits the decisive clause." (No section-level opening; the first case starts at once.) | retrieval; rubric; tool use; memory | coordinate (by substrate, not ordered by signal class: C1/C2, C3, C2, C2) | No (label) |
| Appendix B. Gate families and feedback-signal classes | "Section REF(sec:loop) collapses every production gate into one per-edit test G_t on an estimate of the loss change." (Point in S2: "some of them are better read as proposal pruning that precedes the per-edit gate than as estimators of Δ̂L_D.") | per-edit gate; gate families; proposal pruning; signal class | logical (frame → table → which are gates → what each class leaves) | Yes |


# S5 change logs (R-6 re-draft and R1-R9 polish, per group)

Post-pass edits by the coordinator after the S6 cold read: VI opening describes the grid before naming its rows; I ¶7 closing point sentence split; IX opening states why the loop is uneven; IX closing reworded so the supplement pointer keeps the '(Supplementary Material S7)' form; Appendix XI drops 'at the head of this appendix' (Table A-1 floats to the next page); abstract keeps 'artifact-layer optimization' and the feedback list is parenthesized; I ¶3 researcher-cost sentence opens 'Researchers pay a different cost'.

## Group A

# Changes, group A: abstract, Section I (Introduction), Section II (the loop)

Files edited: `cg_work/abstract.md`, `cg_work/I_II_intro_loop.md`. Paragraph ids follow `ledger_A.md` (pre-edit numbering). I_II:22 is now two Markdown paragraphs (loss; gate), and I_II:21 S1 moved into the first of them.

## 1. Change log by level

### Re-draft (R-6, from the plan; same claims, citations, numbers, REF tokens)

- **I_II:1 (prelude, kept inside the gate per D1).** Target role: prelude + shared context. Point: a deployed system changes while its model does not, and much useful experience now lives in persistent artifacts. Protagonist: the coding agent / deployed system. Moves: S1 now ends on the concept ("…uses the wrong naming convention"), scene moved to the front ("In one repository,"); "its instructions" → "the agent's instructions" (referent); "Similar changes happen" → "The same happens"; S5 rebuilt with a short subject that names the category the examples belong to: "Persistent artifacts like these, outside the model's weights, now accumulate much of the experience that makes an AI system useful in one setting." The thesis-level claim is NOT restated elsewhere in the Introduction (only in the abstract's S1–S2), so it stays and is flagged (AF-7). The one antithesis ("The model has not changed, but the deployed system has.") is kept as the section's single flourish.
- **I_II:6 (point, part 2).** Target role: point. Point: promotion is less assembled than the local loop: portable artifacts, checks inside one operator, no governed promotion across organizations. Protagonist: promotion / the surveyed systems. Moves: point first ("Promotion is more fragmented." + the "No surveyed system documents…" sentence, moved from last to second); S2–S3 ("A change that improves one deployment has been evaluated against that deployment's tasks and measure of success. Another deployment may need different behavior.") deleted as restatements of I_II:3 S4 and II-B/II closing (D9; no citations or numbers); "local improvement loop" → "local loop" (registry); comma before "with versioned lineage…" so the phrase attaches to promotion (interpretation, see 2). Paragraph now ends on the boundary ("within one operator").
- **I_II:7 (point, part 3 + closing point sentence).** Target role: point + the Introduction's closing point sentence. Protagonist: feedback. Moves: opening sentence names the theme and S6's automation claim ("Feedback differs across systems and supports different kinds of automation."); the four examples keep their wording except "A booked appointment provides a later, noisier outcome" → "is a later, noisier outcome" (the appointment is the outcome); "signals" (synonym) and "actually" (tic) removed; the paragraph ends on ONE point sentence naming the four themes in locked terms: "In the surveyed systems, the local gate is built nearly everywhere a local loop exists, the failure record and credit assignment that feed it are weaker, governed promotion across organizations is unassembled, and feedback helps explain this pattern, though no feedback establishes an improvement beyond what it measures." Every clause comes from I_II:5–7 and I_II:8 ("unassembled"); "weaker" keeps I_II:5's strength (the plan's "are not" would overstate it; see AF-11).
- **I_II:14 (definitions, II-B).** Target role: definition of receiving-side evaluation and evidence radius. Protagonist: the promotion loop's evidence. Moves: "conducted" cut; "the change" → "an edit" (registry); new term moved to the stress ("The scope for which the available evaluation supports an edit is its **evidence radius**"), merged with the "does not automatically enlarge" clause, which stays here as the definition home (D9b); "already" cut.
- **I_II:21 (taxonomy).** Target role: the five conditions separate three forms of maintenance. Protagonist: the conditions / the three forms. Moves: S1 ("The model weights remain fixed during this process, and the edits persist beyond the current interaction") moved out (placement 1.5) to the loss paragraph, where only its persistence clause survives ("For deployment $D$, with edits that outlast the current interaction, write…"); the fixed-weights half was deleted as a repeat of the same paragraph's "θ_M denotes the fixed model weights" (and of I_II:1 S3, I_II:2). Opening is now "These conditions distinguish three recurring forms of maintenance." The three forms are parallel ("In *patchwork*… In *random artifact search*… In artifact-layer descent, the trace from failure to cause directs the proposed edit, which is tested before acceptance."): fixes 3.7 "that trace" and 4.12. "change" → "edit". Last sentence kept verbatim (see 3).
- **I_II:29 (section close).** Target role: section close, two limits. Protagonist: the loop. Moves: opening ends on the theme ("From the loss definition, every loop inherits two limits."); "every such loop" → "every loop"; "that meaning" → "that scope" (interpretation); reordered so the section ends on the limit, not the pointer: "Revising the evaluator changes the objective itself, a complication we return to in Section REF(sec:reflexive), but the loop does not discover a better objective simply by accumulating edits." REF token kept. This is now the canonical statement of the scope caveat (D9a).

### R1 document

- I_II:3: explicit turn added ("But because edits are easy to make, edits of unknown value are easy to accumulate."); researcher cost added in one sentence, no citation or new fact (restates in cost form what III says the survey tests): "Researchers cannot tell whether a system described as self-improving improved anything, cannot compare two such systems, and may build on a loop with no acceptance test or no failure record." ("acceptance test" used for "gate" because the Introduction has not yet named the gate.)
- I_II:4: opens on what is unknown: "These situations leave two questions unanswered: what evidence justifies keeping a local edit, and what additional evidence justifies sharing it?"; the corpus sentence (256 systems) moved after the two loop definitions so "The first" follows the questions (ledger 1.5, 3.7) and the paragraph ends on the evidence base handed to I_II:5.
- I_II:7: closing point sentence (above).
- I_II:8: no longer ends on the release caveat. The evidence-base and release statements open the paragraph (and resolve "this evidence"); the roadmap follows and ends on "…the research lines that produced its components." S4 split from a tacked-on chain into a three-predicate sentence; "local adaptation" → "the local loop"; "governed sharing" → "governed promotion"; "these checks" → "gates" (interpretation); "the conditions under which artifact maintenance constitutes optimization" → "when maintaining artifacts counts as optimization".
- Abstract: sentences reordered so it ends on the finding: context (S1–S2) → survey (S3) → decisions and loops (S4–S5) → feedback classes and the scope limit (S9–S10) → contributions and framework (S11–S12, "We use this observation…" still follows its antecedent) → findings (S6, S7) → "The feedback available to a deployment helps explain this pattern." 234 words; "256 production and research systems" kept.

### R2 sections / paragraphs

- I_II:5: S1 "developed" → "built" (theme word of the point sentence); S2 subject-first ("Nearly every recently added system with a local loop has an automatic acceptance test: 89 of 96."); S3 ends on the artifact list ("…the instruction, memory, skill, or tool binding at fault"); "Meanwhile" (bluff) → "by contrast" (real contrast); "changes" → "edits".
- I_II:9 (II opening): S1–S2 merged so the opening ends on measurement ("…only by rerunning the agent on relevant tasks and comparing results"); "change" → "edit"; S3–S4 joined with a semicolon (S4 still ends "reverse it": one referent, the edit; left for the length budget).
- I_II:13: S1–S2 merged ("Suppose the naming rule helps in the original repository and the team considers adding it to a shared template."); S4 ends on its stress ("…about which the local evaluation says little").
- I_II:15: "the form of" cut; "through five conditions" → "by meeting five conditions" (criteria, not connector). Heading left unchanged (D6); prose uses the defined term.
- I_II:22: split into a loss paragraph and a gate paragraph (ledger 3.1, house rule one claim per paragraph); the gate paragraph opens "Instead, the gate estimates…"; S6 "is a practical instance of this rule" → "applies this rule in practice".
- Term registry (abstract, I, II): "local improvement loop" kept only at the abstract's definition and the Fig. 1 caption (raw LaTeX, untouched); "local adaptation loop"/"local adaptation" → "local loop"; "change/revision" → "edit" for scaffold edits (abstract S2, S3; I_II:3, 4, 5, 6, 9, 14, 17 item 2, 19 item 4, 21, 22, 23, 24, 26); "delayed rewards" → "delayed outcomes" (abstract); "task distribution" → "tasks" (abstract; registry bans it for the defined patch); "artifact-layer optimization" → "artifact-layer descent" in abstract prose (heading untouched); "cross-organization promotion" → "promotion across organizations" (abstract); "failure capture and attribution" → "failure records and credit assignment" (abstract).

### R3 flow

- I_II:2: "retraining it" → "retraining" (pronoun with two referents); "The distinction matters" → "The split matters because the two change on different schedules:" merged with the team/model example sentence.
- I_II:3 S3: referent fixed: "A memory may be corrected in the history while the system keeps retrieving the outdated entry." (interpretation).
- I_II:11: "or **coordinate**" → ": a **coordinate**" (gloss, not alternative); S5 nominalization chain → "An accepted edit is retained as a versioned artifact; a later regression can trigger rollback."
- I_II:12: "The evaluation" → "The gate's evaluation" (referent); "this" → "the patch loss" (S4); S5 ends on "the patch loss".
- I_II:19 (item 4): "the process" → "a process" (no prior referent).
- R3 re-run after every reorder: I_II:4 (questions → loops → corpus), I_II:6 (point moved forward), I_II:8 (evidence base first), I_II:21/22 (sentence moved), I_II:29 (reorder), abstract (reorder). Pronouns rechecked: abstract "Their feedback" = the two decisions; I_II:8 "its components" = the unassembled architecture (the only singular candidate); I_II:7 "feed it" = the local gate.

### R4 sentence

- I_II:3 S1: abstract subject "The ease of making a change" removed.
- I_II:20 (item 5): "only after a check of whether it lowers" → "only after a check tests whether it lowers" (same condition, verbalized).
- I_II:24: subject shortened ("Who writes an edit and who accepts it are separate roles."); "revision" → "edit" (×2); "who makes the acceptance decision" → "who decides whether to accept the edit".
- I_II:27 (None): "no acceptance decision is made" → "nothing accepts or rejects the edit" (actor-like subject parallel to Auto/Human).
- I_II:25 (Auto): metadiscourse cut: "Section REF(sec:signal) asks separately whether that judge has been calibrated against people." (REF kept).
- I_II:23 S2: opens on old information ("Improving edits eventually stop clearing the gate under additional coverage, compactness, and summable-bias assumptions."), statement unchanged (AF-2).

### R5 concision

- Cut: "actual" and "particular" (I_II:12), "already" (I_II:14), "actually" (I_II:7), "the form of" (I_II:15), "conducted" (I_II:14), "Together," (abstract), "first" (I_II:8); "to the extent that" → "as far as" (I_II:12); "a separate training, evaluation, and release process" → "separate training, evaluation, and release" (I_II:2); "without any process" → "but no process" (I_II:5).
- Redundancy (2.5): I_II:6 S2–S3 deleted; I_II:7 S6 folded into the opening and the point sentence; fixed-weights clause of old I_II:21 S1 deleted (kept in the equation gloss).

### R6 shape

- Abstract S6 (now near the end) subject-first; abstract feedback sentence no longer opens on four new terms ("Their feedback, whether exact checks, observed outcomes, judgments, or delayed outcomes, supports…"); abstract S4 ends on the evidence term ("whether enough evidence supports sharing it more widely").
- I_II:1 S5: 13-word subject replaced by a 4-word subject.
- I_II:8 S4: tacked-on relative chain removed.
- I_II:28: two short sentences joined with a semicolon; ending moved off the hedge.

### R8 integrity

- No claim, number, citation, quotation, or cross-reference changed. Calibration kept: "weaker" (not "not built") for the failure record in the point sentence; "documents" scope kept in I_II:6; "helps explain"/"partly" kept; "substantial" kept (see 3).

### R9 punctuation

- No em-dashes (0 in both files). American spelling throughout. Serial comma consistent. Semicolons used only between closely linked clauses (I_II:2, I_II:8 S1, I_II:9, I_II:11, I_II:24, I_II:28).

## 2. Interpretations and supplied doers

- **interpretation** I_II:3 S3: "A corrected memory may remain in the history while the system continues to retrieve the outdated entry" read as "the correction sits in the history while the outdated entry is still retrieved" → "A memory may be corrected in the history while the system keeps retrieving the outdated entry." Author to confirm which entry "remains".
- **interpretation** I_II:6: comma added so "with versioned lineage, access control, and rollback" attaches to promotion, not to organizations.
- **interpretation** I_II:7 S3: "A booked appointment provides a later, noisier outcome" → "is a later, noisier outcome".
- **interpretation** I_II:8: "these checks" → "gates"; "its components" kept, read as the unassembled architecture's components.
- **interpretation** I_II:13 S1: "improves the original repository" → "helps in the original repository" (the rule improves the agent's work there).
- **interpretation** I_II:29: "that meaning" → "that scope" (the measure and tasks just named); "every such loop" → "every loop" (Section II discusses only loops of this kind).
- **interpretation** abstract: "failure capture" → "failure records" (registry term for retained failures); "task distribution" → "tasks".
- **supplied doer**: none new. I_II:3 S1 removes "the ease… makes it easy" without adding an actor. The doer ambiguity in I_II:1 S4 ("when an assistant corrects a stored preference") and I_II:10 S2 (who groups failures) was left as written (see 3).

## 3. Ledger FLAGs deliberately left

- I_II:1 S4 (4.2): "an assistant corrects a stored preference": the corrector could be the user or the assistant; choosing one would invent a doer.
- I_II:1 (3.1): subjects still pass agent → engineer/session → model/system → artifacts; a narrative of one fix needs the engineer as actor, and the protagonist (the agent/system) opens and closes the paragraph.
- I_II:2 S2 (4.14): ends "control their use"; the referent is unambiguous and the alternatives add words or a repeat.
- I_II:2 S3 (4.13, 4.2, AF-8): "that a deployment can inspect and revise" left as is; the sentence carries the attribution to [@zaharia2024compound] and was changed only by dropping the final "it".
- I_II:5 S3 (4.1): subject "The steps that should supply those tests with well-founded candidates" kept (11 words): it opens on old information ("those tests"), and the subject-first variant cost words the length budget did not have.
- I_II:5 S4 (5.1): "substantial" kept: it carries the contrast between built release machinery and no proposal process; removing it weakens the claim.
- I_II:5 S2 (4.15): "recently added" not glossed in the Introduction (the corpus refresh is defined in III; a gloss would add a fact here).
- I_II:6 (4.15): "operator" left; it is the term the promotion section uses.
- I_II:7 (4.15): "local gate" appears in the point sentence before II-A defines "gate"; I_II:5 supplies the gloss "automatic acceptance test" two sentences of context earlier. Kept because the task requires the locked term in the point sentence.
- I_II:10 S2 (4.2/4.5): "Repeated failures are grouped… and prioritized" stays passive; the actor differs by system (team or system), which is what II-D classifies.
- I_II:14 S5 (4.14): ends "between them"; one referent (the scopes), and the alternatives repeat "scopes".
- I_II:18 (5.3): "can, at least sometimes, be traced" kept (AF-3).
- I_II:21 last sentence (4.14, 5.1, 5.3): "the optimization interpretation is correspondingly limited" kept verbatim; saying how the interpretation weakens would add claim content (AF-12).
- I_II:23 S2 (6.2): statement of the stability result kept (AF-2).
- I_II:25 (4.12): items remain unequal in length; Auto carries the citation and the calibration pointer.
- I_II:8 (1.7): roadmap still omits Section X (AF-10).
- Abstract (4.15): "lineage", "governed promotion", "gate types", "recently added systems" unglossed; glossing needs content the abstract budget does not hold.
- Abstract (6.3): "identifies what existing systems can already automate" kept (AF-6).

## 4. AUTHOR FLAGS

1. **I_II:22, undefined symbols** (ledger AF-1): π, x, λ undefined; math untouched.
2. **I_II:23 S2, stability result wording** (ledger AF-2): "improving edits eventually stop clearing the gate" can read as "good edits get rejected"; only the clause order changed.
3. **I_II:18, stacked hedge** (ledger AF-3): "can, at least sometimes, be traced" kept.
4. **I_II:20, "retained or promoted"** (ledger AF-4): promotion inside the local-loop conditions; kept.
5. **Abstract, "We use this observation to develop five conditions…"** (ledger AF-5): derivation claim kept; the reorder keeps the observation (S10) immediately before it, which is why the contributions now sit before the findings rather than at the end.
6. **Abstract, "identifies what existing systems can already automate"** (ledger AF-6): kept.
7. **I_II:1, "Persistent artifacts like these… now accumulate much of the experience…"** (ledger AF-7): thesis-level claim inside the prelude, no citation or pointer; not restated elsewhere in the Introduction, so it was kept rather than cut. Consider a pointer to III or a citation.
8. **I_II:2 S3, attribution to [@zaharia2024compound]** (ledger AF-8): not verified against the source; wording unchanged except the final pronoun "it" was dropped ("without retraining").
9. **Term registry** (ledger AF-9): heading "Five conditions for artifact-layer optimization" still differs from the defined term "artifact-layer descent"; the abstract now says "five conditions for artifact-layer descent" (per the pass instruction), which an abstract reader meets undefined. Author to decide the heading or the abstract wording.
10. **I_II:8, roadmap omits Section X** (ledger AF-10).
11. **I_II:7 point sentence vs plan wording.** The plan's point says the failure record and attribution are "not" built; the text's evidence (I_II:5, abstract, claims ledger) says "weaker"/"less developed". The point sentence uses "weaker". If the author wants "not", the evidence needs to support it.
12. **I_II:21, "the optimization interpretation is correspondingly limited"**: vague hedge in the stress position; a concrete statement (what a partly met condition costs) needs the author's wording.
13. **I_II:6 opening "Promotion is more fragmented."** replaces "Sharing adds a further limitation." The new opening is the abstract's own claim (abstract S7), brought into the Introduction so the paragraph opens on its point; confirm the comparison (more fragmented than the local loop) is intended here.
14. **Abstract, "failure capture and attribution" → "failure records and credit assignment"**: registry substitution; confirm "records" is acceptable for "capture" (the condition is "relevant failures are retained").
15. **I_II:3 researcher-cost sentence** (added per plan 1a/1c item 1): no citation; it restates in cost form the label test described in III ¶3. Confirm it may stand uncited.

## 5. Word counts

| file | before (cg_pre) | after (cg_work) | change |
|---|---|---|---|
| abstract.md | 237 | 234 | −3 |
| I_II_intro_loop.md | 1666 | 1666 | 0 |
| group | 1903 | 1900 | −3 (−0.2%) |

Within the group, the Introduction grew (turn + researcher cost in I_II:3; the closing point sentence in I_II:7), and the growth was paid for by cutting restatements (I_II:6 S2–S3, I_II:7 S6, the fixed-weights clause) and wordiness across Sections I–II.

## 6. Invariant check

`cg_invariants.py cg_pre cg_work`: no FAIL or WARN lines for `abstract.md` or `I_II_intro_loop.md` (citation keys, numbers, REF tokens, headings, raw LaTeX block, display equations, bold terms all identical); overall result at the final run: `CG INVARIANTS: PASS`. Em-dashes: 0 in both files.

## Group B

# Changes B: III_method.md, IV_local_findings.md (R-6 re-draft + S5 Polish R1-R9)

Files edited in place: cg_work/III_method.md, cg_work/IV_local_findings.md. Paragraph ids follow ledger_B.md (pre-edit numbering).

## (1) Change log by level

### Re-draft (R-6), from the plan's point outline and reverse_B

| ¶ | target role / point / protagonist | what changed |
|---|---|---|
| III:10 | explanation; "a score of 5 certifies different things on different substrates, so scores compare within a substrate"; protagonist: a score of 5 | Opens on the point (was S6, last). "This last distinction is important when interpreting the scores" cut (importance announcement, unresolved "This"). "A score of 5" / "it" is now the subject of every clause; the orchestration row restatement shortened; "closure of either loop" kept in one antithesis; the second antithesis ("is not a universal certificate") recast as "no top score is a universal certificate of complete optimization" (wording of the claim kept). |
| III:12 | housekeeping (scope note); "gate, feedback and governance counts describe only the 126 newest systems"; protagonist: the rows of the 126 systems | Subject is now the 126 systems' rows; ends on "that subset alone". S3 "This is not a gate count over all 256 systems" merged into S2 as a summative modifier ("a count that does not extend to all 256 systems"), resolving the bare "This". The 105/96/89 example kept (numbers invariant; AUTHOR FLAG 15). |
| IV:2 | illustration + method rationale; "SkillRL also leaves corrections untested; proposing an edit is not accepting it, so the survey classifies by acceptor"; protagonist: SkillRL, then the survey | Opens on old information ("SkillRL leaves its corrections untested by a different route") and stresses the mechanism; vague "exposes the same separation through a different mechanism" removed. The point "proposing an edit is not the same as accepting it" now stated here, once, in one clause; the rest of IV refers to it. Ending "triggers it" → "the edit's author and its trigger". "local acceptance gate" → "local gate" (registry). |
| IV:5 | evidence (prioritization); "retained failures are used in arrival order; two systems weight experience; recurrence-and-severity prioritization is uncommon"; protagonist: systems | Three statements of one proposition (S1, S2 "Few explicitly choose...", S5) reduced to one plus the specific gap. Exceptions now open on old information ("Two systems weight that experience instead: Task-CoEvolve ... and AutoSaddler ..."). The dangling "They ... determine it" removed; its content moved to S1 as "letting the most recent session determine the next update" (interpretation, see 2). "The general loop described earlier" → "the local loop" (registry). |
| IV:6 | problem; "credit assignment is the hard step, and harness-optimization papers name it the bottleneck"; protagonist: credit assignment | The empty beat "The next step is harder." now names the theme: "The next step, credit assignment, is harder, because a failed output does not reveal ..." (S1+S2 merged). S3 opens on old information ("This attribution step is what harness-optimization papers repeatedly identify as the bottleneck"); "attribution" kept there because the sentence reports the cited papers' framing. S4 attribution words kept unchanged ("reaches the same conclusion", AUTHOR FLAG 7). |
| IV:9 | evidence (skills by gate); "skill systems differ in where the gate sits, and some have none"; protagonist: skill systems | Opens on the theme. SkillChain's evidence is now stated only here, merging IV:9's and IV:12's wording ("adds a reflection gate after its judge, at which a person decides which refined skills are deployed"), with its citation; the dangling "on which" relative removed. S4 ("These differences would be obscured by classifying all three simply as systems that learn from feedback") deleted: it restated the proposer/acceptor reasoning now made once in IV:2 and its "all three" did not resolve; no citation or number in it. |
| IV:14 | explanation; "averaging and agreement are different mechanisms; both assume independence"; protagonist: the two mechanisms | Opening names both mechanisms in its stress ("Two mechanisms should not be conflated: averaging scores and requiring agreement"). The $p^k$ sentence now names the event ("each of which falsely accepts with probability $p$, gives an idealized false-acceptance probability of $p^k$"; interpretation, see 2). "The independence assumptions matter, and actual critics need not satisfy them" → "Both results assume independence, which actual critics need not satisfy." S6 (the shared trend, a second claim) moved to IV:13, where the systems it summarizes are; its "rather than" antithesis became "instead of". |

### R1 document / section structure

- Section IV opening segment (IV:1-IV:3) now ends on the section finding: IV:3 "Among recent systems with a local loop, however, automatic acceptance dominates: of the 105 ..., 96 have a local loop, and 89 of those use a program to retain or reject edits. Inside these loops, evaluation is comparatively mature, while the failure record and the credit assignment that should supply the gate are often incomplete." IV:1 S1 keeps "detecting a failure is not testing a fix". "nevertheless" (bluff) removed; "however" now marks the real contrast with IV:1-IV:2 (two systems without a gate vs the recent corpus); "reveals a less even picture" cliché removed.
- IV:8 (candidate generation) moved from the start of "Testing the candidate" to the end of "Finding the right thing to change", so IV-A now follows the loop order (failure record → prioritization → credit assignment → attribution methods → who proposes the candidate) and IV-B is about gates only. Headings unchanged.
- "Proposing an edit is not accepting it" stated once (IV:2); IV:9 keeps its systems and evidence without the reasoning; IV:12 refers to SkillChain by name only.
- IV:14 S6 moved to IV:13 (one claim per paragraph).
- III:13's source list no longer duplicates III:2: III:13 opens on the evidence range (the weighting frame) and the per-row documentation sentence (old S2) moved to the paragraph's end, so the weighting thread runs S1 → peer review → production claims → pooling.

### R2 sections / paragraphs (openings and themes)

- III:1: S2 "This allows systems ... to be compared by their behavior" → "We then compare systems with different names and application domains by their behavior" (bare "This", capability voice, hidden comparer). S1 "the persistent artifact it changes ... the decision that accepts it" → "the persistent artifact the system changes, the feedback that prompts a change, the decision that accepts the change" (one referent per "it").
- III:11: topic announcement "Table REF(tab:V-2) gives the corpus distribution." removed; the paragraph opens on the finding with the pointer in a parenthesis ("In the corpus distribution (Table REF(tab:V-2)), research systems hold the top marks ...").
- IV:3: see R1.
- IV:8: opens on the research case and states the point (intermittent improvement where proposal waits on a person) in sentence 2, before the two production cases.
- IV:10: "Orchestration has followed a similar progression" (no progression described before; "similar" unresolved) → "Orchestration has moved from score-guided search toward gated edits."
- IV:11: "The most widely deployed artifact remains a useful counterpoint" → "For instruction files, the most widely deployed artifact, prevalence does not settle effectiveness" (names the artifact and the point; "useful" cut); the old S3 ("Their prevalence does not settle their effectiveness") folded into this opening.
- IV:13: opening segment now ends on the theme ("acceptance increasingly depends on a body of evidence instead of one favorable observation"); "directly" cut.
- IV:19: "SkillOpt provides a concrete instance of all five conditions" → "SkillOpt meets all five conditions".

### R3 flow (point of view, old→new, referents, sequence, redundancy)

- III:4 S4 opens on old information: "These 256 systems occupy 269 scored rows, because a system may have one integrated row or several substrate-specific rows."
- III:6: "SkillOpt is classified from its paper and is not a row ..." → "SkillOpt is not a row in the 256-system score table" (classification already stated in III:5).
- III:7: Letta point kept here (its single statement); III:15 keeps only the one-clause list item.
- III:12: bare "This" resolved (see re-draft).
- III:13: S2 moved last (see R1); "corroborates it" ending → "corroborated by stronger evidence".
- III:15: "the human-local cells" → "the cells with a human local gate" (interpretation, see 2).
- IV:1: subjects now SkillForge → its judge → SkillForge → the judge's calibration; old→new opener "SkillForge is such a system" replaces "SkillForge illustrates this distinction" (unstated referent).
- IV:4: "failure history" → "failure record" (registry); "particular" cut.
- IV:7: "Existing solutions" → "Existing attribution methods" (theme); "the general attribution problem" → "credit assignment" (registry; "attribution" kept for the named methods); two closing sentences merged.
- IV:12: SkillChain repetition reduced to a name; "which belongs to promotion" (two antecedents) → "and both belong to promotion".
- IV:13: AutoSaddler's second role marked with "also ... its mini-batch failure signals".
- IV:17: "Research systems likewise divide" → "Research systems divide" ("likewise" was a bluff).
- IV:19: S2-S5 reordered to Section II's condition order: state, loss (condition 1), failure evidence (2), consensus attribution (3), edit operators (4), gate (5).
- IV:20: SkillOpt-Lite sentence recast to put what it keeps before what it drops; consensus result from IV:7 not restated.

### R4 sentence (characters and actions)

- III:3: gerund subject "Including the latter group provides a contrast set" → "The second group forms a contrast set, with which the survey can test ..."; S3 "Systems whose only update mechanism ... are excluded" → "We exclude systems whose only update mechanism is weight-level training, and systems without ...".
- III:5: participial opener "Applied to 202 of the 204 core systems ..." → "The audit covers 202 of the 204 core systems and 4 research systems ..."; the unaudited systems now have their own sentence.
- III:7 S4: "their treatment under relaxed audit rules is reported separately" → "we report their treatment under relaxed audit rules separately".
- III:8: "the ... memory categories follow Sumers et al." → "Following Sumers et al. [@sumers2023coala], we divide memory into episodic, semantic, and procedural categories".
- III:13: "are not pooled with ... in corpus-level statistics" → "Corpus-level statistics do not pool production claims with peer-reviewed evidence".
- IV:1: "Those replies drive updates to the skill, but the updated skill is committed without an acceptance test" → "SkillForge updates the skill from those replies but commits the updated skill without an acceptance test" (supplied doer, see 2).
- IV:15: "The evaluation of a new edit also depends on ..." → "How a new edit scores also depends on ...".
- IV:16: "have made substantial progress on" → "have advanced substantially on" (empty verb + nominalization; intensifier kept, AUTHOR FLAG B-16).
- IV:18: "support edit-level rollback" → "can roll back a single edit" (mechanism over capability); "The consequences of an edit may therefore outlast the edit itself" → "An edit's consequences may therefore outlast the edit".
- IV:19: "a candidate is accepted only when its score strictly improves" → "The gate accepts a candidate only when its score strictly improves" (supplied doer, see 2).
- IV:20: S1 attribution moved forward ("SkillOpt's authors test it on ... and report it best or tied in every cell"); "supports the importance of the gate" → "supports the view that the gate and this form of credit assignment matter"; trailing participle "while identifying the removed controls as stabilizers rather than necessities" → finite clause "and it identifies the removed controls as stabilizers, not necessities".

### R5 concision

- Cut: "subsequently" (III:5), "simply" (IV:9 S4, deleted), "directly" (IV:13), "itself" and "machinery" (IV:8: "the evaluation machinery ... the improvement process itself" → "evaluation ... improvement"), "particular" (IV:4), "useful" (IV:11), "principal" → "main" (III:15), "Looking inside those loops reveals" (IV:3).
- Announcements cut: III:10 S1, III:11 S1, IV:9 S4.
- Bridge: IV:21 S4 kept but shortened into the section's last sentence (see 3).

### R6 shape

- III:2 S3 split at the semicolon; the second sentence now ends on "inclusion rules" with the supplement pointer moved forward.
- III:4 S2: "under the rubric below" moved to the front.
- III:5 S2: ambiguous attachment fixed ("promoted, with versioning or lineage, beyond the deployment that produced it").
- III:6 S4: gapped coordination restored ("the audit's boundary cases are identified in the contrast set").
- III:9: "The common scoring scale" → "The shared scoring scale" (interpretation, see 2); the closing pointer "as specified in the table" → "The table's last column gives a separate score-5 requirement for each substrate."
- IV:3 S1: fronted 12-word phrase removed; point first, counts after the colon.
- IV:5 S3: 10-word new subject replaced by "Two systems weight that experience instead: ...".
- IV:8 S2 split into two sentences (prompt platforms; skill repositories); fronted "Where ..." clause shortened ("Where proposal instead waits on a person noticing a problem, ...").
- IV:11 S5 split: the measured results, then "It does not measure correctness".
- IV:12 S3: qualifier moved forward ("In this classification, ...") so the sentence ends on "no local gate".
- IV:14 S3: interruption between subject and verb recast as a relative clause after the object.

### R8 integrity

- No claim, number, citation, cross-reference, quotation, heading, table, caption, LaTeX block, or bold term changed (invariant check PASS).
- Section IV antitheses reduced from four "rather than" + three correctives to one "rather than" (IV:10, a source description) plus the deliberate negatives that carry claims (IV:1, IV:2 point, IV:17, IV:20 "not necessities").

### R9 punctuation

- No em-dashes. Semicolon chains reduced (III:2, III:8, IV:11). Colons only after complete clauses (IV:3, IV:5, IV:8, IV:12, IV:14 opening). Serial comma kept. American spelling throughout (no WARN lines for these files).

## (2) Interpretations and supplied doers

Interpretations (vague phrase replaced by specifics already in the text; author to confirm):
- IV:5 S1 "letting the most recent session determine the next update": moved from the exceptions' contrast ("rather than letting the most recent session determine it") to the general case of arrival-order use.
- IV:14 "gives an idealized false-acceptance probability of $p^k$": names the event that $p^k$ is the probability of (the combined gate falsely accepts), which the original left implicit. Also listed under AUTHOR FLAGS (math).
- IV:3 "the credit assignment that should supply the gate" for "the link from a failure to the responsible artifact" (Section II's definition of credit assignment; the plan's section point uses "that should supply it").
- III:15 "the cells with a human local gate" for "the human-local cells".
- III:9 "The shared scoring scale" for "The common scoring scale" (shared across substrates).
- III:12 "counts of these properties describe that subset alone" for "apply to those systems" + "This is not a gate count over all 256 systems".
- IV:9 "and some have none" (the opening's summary of SkillRL and SkillForge, which IV:2 states have no local gate).
- IV:10 "moved from score-guided search toward gated edits" (summary of S2-S3).
- IV:12 "VerificAgent's fact-checked, frozen memories" and "SkillChain's reflection gate" listed as the two curation cases of a human local gate (the original's two examples, now as a list).

Supplied doers:
- III:1 "We then compare" (the authors).
- III:3 "We exclude" (the authors).
- III:7 "we report their treatment" (the authors).
- III:8 "we divide memory" (the authors, following Sumers et al.).
- IV:1 "SkillForge updates the skill ... commits the updated skill" (the system).
- IV:19 "The gate accepts a candidate" (SkillOpt's held-out gate, named in IV:20).
- Not supplied: IV:2 who proposes SkillRL's skills (the agent or an optimizer; two plausible doers, left as "A success-rate threshold triggers proposals"). IV:15 who applies "lifecycle hygiene" (left agentless).

## (3) Ledger FLAGS deliberately left

- III:1 4.14: S1 still ends "the scope in which the result is used". Every recast that ends on "scope" broke the four-item parallel list that the plan's frame uses; the theme word is inside the final item.
- III:2 3.6: S1 still ends on the cutoff date. The corpus size and dates are the paragraph's point; the search-pass sentence follows immediately.
- III:2 5.1: "supported production reports" kept (AUTHOR FLAG 14).
- III:5 3.7: "the eight systems without an audit" kept (AUTHOR FLAG 1; number not fixed by instruction).
- III:7 3.7 / 4.14: "separately" still has no location; adding a pointer would add a cross-reference (AUTHOR FLAG 12).
- III:7 4.12: the three-way promotion list ("within one operator, into a shared bank or archive that later runs draw from, or across the agents and sessions of one deployment") left: it is unclear whether "within one operator" is an umbrella for the other two or a third alternative, so making it parallel would choose a meaning.
- III:10 5.1: "universal ... complete" both kept; dropping either changes the scope of the negated claim.
- III:12 2.5: the 105/96/89 example still duplicates the Table V-2 caption and IV:3 (numbers invariant; AUTHOR FLAG 15).
- III:13 term drift "industry exemplars" / "vendor-based exemplars" left; they may not be the same set.
- III:14 AI: "an auditable interpretation of public evidence, not a complete inventory" kept as the section's honest-accounting antithesis (house rule: honest accounting once).
- III:15 5.1: "the full score table with the released table" left (AUTHOR FLAG 13).
- III:4 / III:3 "contrast set" vs "contrast corpus" left (AUTHOR FLAG 2).
- IV:4 5.1: "more often" without a comparator kept (AUTHOR FLAG 10).
- IV:5 5.3: "nearly every system" kept (AUTHOR FLAG 9).
- IV:7 5.6: "attributes outcomes" vs "the attributes that recur" kept; both describe cited methods in their own terms.
- IV:7 1.6 note: Meta-Harness example kept (citation and claim).
- IV:10 4.15 "structural invariant", IV:13 4.15 "heterogeneous critics", IV:15 4.15 "lifecycle hygiene", IV:8 4.15 "AI co-author trailer", IV:11 4.15 "root AGENTS.md", "paired runs", "wall-clock", III:7 4.15 "operator": unglossed terms left; a gloss would add a definition not in the text.
- IV:10 AI: one "rather than" kept in the OptiMAS sentence (the section's single remaining antithesis; it describes the source's mechanism).
- IV:11 4.12: the list mixing products with AGENTS.md left (reordering would change what the citation sits on).
- IV:16 5.1 / 5.3 / AI: "substantially" kept; removing it weakens an evaluative claim (AUTHOR FLAG B-16).
- IV:17 3.1 / one claim per paragraph: S4-S5 (research memory designs) kept in the same paragraph; with "likewise" removed they read as the research side of the same point (history does not guarantee correction). A split would leave a two-sentence paragraph.
- IV:21 3.6 / AI bridge: S4 kept, shortened to "That separation becomes central once the same local procedure runs where correctness is harder to measure." It carries a claim and is not repeated within this file, so deleting it is outside the allowed edits; the author may cut it once Section V's opening carries the link (D10).
- IV:21 3.7: "the shared skill bank" vs "one markdown skill document" left (AUTHOR FLAG 8).
- IV (section) house formatting: five subsections kept (D6, D13); heading "What local adaptation actually closes" and "Testing the candidate" unchanged (headings frozen).
- III (section) 1.8 label headings unchanged (D6).

## (4) AUTHOR FLAGS (merged with ledger_B; none changed in the text)

1. III:5 "the eight systems without an audit": the audit covers 202 of 204 core systems (2 unaudited); the source of the other six is not stated (Supplementary S4.2.1 names the eight). State the composition or point to S4.2.1.
2. III:3 "contrast set" (self-described systems) vs III:4 "contrast corpus" (the 52 that fail the score filter): same set or two?
3. III:15 "the cells with a human local gate hold only curation and registries" vs IV:12 "prompt platforms and registries without a failure-driven proposal process have no local gate": do registries enter a human-local cell only under the relaxed boundaries? Say so if they do.
4. Table V-2 caption "none of the 126 scores 5 on any substrate": check against the score-5 systems with 2026 keys.
5. IV:14 "reduces the variance of their mean by a factor of $1/k$": the variance scales by $1/k$ (falls by a factor of $k$); phrase for the author. Also confirm the reviser's naming of $p^k$ as "an idealized false-acceptance probability" (interpretation).
6. IV:13-IV:14: which of SAGE-gate (paired per-item comparisons), VaG (three critics must pass) and AutoSaddler (mini-batch failure signals) is averaging and which is agreement? The paragraph still does not map them.
7. IV:6 "An evaluation of harness optimizers reaches the same conclusion" [@ong2026harnesseval]: confirm the source concludes that attribution is the bottleneck, not only that score alone cannot distinguish an optimizer from trial and error.
8. IV:21 "the shared skill bank" vs IV:19 "one markdown skill document used by a frozen agent": which does SkillOpt's gate admit edits into? (Bears on SkillOpt's two-loop pass in III.)
9. IV:5 "nearly every system uses them in arrival order": needs a count or a pointer to the coded column.
10. IV:4 "Production memory more often records preferences, successes, or conversation history": no comparator and no citation or data pointer.
11. "Table V-1"/"Table V-2" captions sit in Section III: internal labels renumbered by the build (per the task note, not an error; listed only for completeness).
12. III:7 "we report their treatment under relaxed audit rules separately": no location. The treatment appears in Section VI's paragraph on the audit's boundary cases ("Of six systems that promote without artifact lineage, five ..."); a cross-reference there would resolve it.
13. III:15 "the full score table with the released table (Supplementary Material S1)": reads as circular.
14. III:2 "supported production reports": what does "supported" mean (corroborated, as in III:13)?
15. The 105/96/89 counts appear in the Introduction ¶5, the Table V-2 caption, III:12 and IV:3. III:12 keeps them (numbers invariant); the author decides which statements stay.
16. (B-16) IV:16 "advanced substantially": an intensifier with no measure; replace with the observed relationship (three products record entry history) or keep.
17. IV:21 last sentence is a bridge to Section V; cut if Section V's opening (D10) carries the link.
18. IV:2: the doer of SkillRL's proposals (the agent or an optimizer) is not named; the reviser did not choose.
19. IV:3 now says "the credit assignment that should supply the gate": confirm this wording of the plan's section point (Section II's loop order: failure record → credit assignment → candidate → gate).

## (5) Word counts (wc -w, whole file incl. headings and tables)

| file | before (cg_pre) | after (cg_work) | change |
|---|---|---|---|
| III_method.md | 1521 | 1520 | -1 (-0.1%) |
| IV_local_findings.md | 1498 | 1476 | -22 (-1.5%) |
| group | 3019 | 2996 | -23 (-0.8%) |

## (6) Invariant result

`cg_invariants.py cg_pre cg_work`: no FAIL or WARN lines for III_method.md or IV_local_findings.md; overall "CG INVARIANTS: PASS" at the final run. Citation-key, number, REF-token, heading, table, caption, LaTeX-block, equation and bold-term multisets identical to cg_pre for both files; no em-dashes.

## Group C

# Changes C: Sections V (feedback classes) and VI (promotion)

Files: `cg_work/V_feedback_signal_classes.md`, `cg_work/VI_promotion.md`. Paragraph ids follow `ledger_C.md` (pre numbering). Registry substitutions required by the checker: V-D heading "Delayed and sparse outcomes: C4" -> "Delayed outcomes: C4"; Table IV-1 row label "C2 observable outcome" -> "C2 observed outcome".

## (1) Change log

### Re-draft (R-6): target role / point / protagonist, then the new paragraph

- **V:5** role: explanation (limit). Point: an exact check is exact about its output, not the deployment; stochastic outputs and a finite suite still have to be sampled. Protagonist: the check, then the gate. Gerund subjects replaced ("Estimating ... requires accounting" -> "A gate that estimates ... must account for both"); "that variation" (two referents) -> "both" after naming both sources; "as a whole" and "also" cut. Caveat (a) shrunk from its own sentence to a closing clause ("passing the suite establishes only what the suite tests"). "task distribution" -> "the patch" (registry: the patch is the defined term).
- **V:6** role: problem. Point: a reliable checker leaves two problems, attribution and the side effects of cheap, repeated acceptance. Protagonist: the checker / exact feedback. "Two problems remain even with a reliable checker" kept word for word, now followed by the two names; overfitting and pool growth are grouped as the second problem (interpretation, see 2). Antithesis "makes evaluation easier; it does not supply" -> "makes evaluation easier but supplies neither attribution nor lifecycle management". "also" cut; "overfit it" -> "overfit the scaffold to it".
- **V:13** role: problem. Point: a judge can be gamed and can move; editing the rubric makes the gate reflexive. Protagonist: the judge. Opening "Optimization introduces another risk" (empty verb, "another" with no first risk) -> "A judge can also be gamed, and it can move." S3 opens on old "this proxy overoptimization". Last sentence reordered so the paragraph ends on "**reflexive gate**" with the pointer first.
- **V:15** role: evidence. Point: C4 systems decide at intermediate points, which prune or consolidate without per-edit credit. Protagonist: systems in this class. Point moved to S1; the NanoResearch and CORAL cases follow in one sentence. The AlphaEvolve boundary note moved to V:4 (C1 subsection), next to the sentence introducing AlphaEvolve's exact evaluators; its [@alphaevolve2025] key moved with it. "on a heartbeat" -> "periodically" (interpretation).
- **V:18** role: other view, section close. Point: the expectations concern evidence, not executability; the gate grid makes the distinction explicit. Protagonist: the expectations. S4 (sharing caveat, no keys or numbers) deleted: its home is II-C/VI-A (D9b) and VI:1 restates it on the next page. Section now ends on the qualification ("without estimating a loss change") instead of on a caveat.
- **VI:3** role: point. Point: a lower average loss at a broad scope can conceal harm to one recipient, so the architecture adds receiving-side evaluation, separate from versioning and access control. Protagonist: the averaged loss, then the check. "The nesting makes an important limit visible" (empty verb, intensifier, no limit named) cut; S1 now names the limit and links to VI:2's aggregation ("therefore"). S2 opens "For this reason". S3 ends "whether the recipient should use it" (was "used there").
- **VI:6** role: point. Point: where the check runs matters, and so does what it covers. Protagonist: the check. Roll call of VI:4-VI:5 (S2, semicolon chain) cut; Evo2Team number kept; caveat (a) restatement shrunk to a clause ("its finite cases do not guarantee performance on all future tasks").
- **VI:10** role: evidence (two meanings of None). Point now first: "A None at the promotion gate has two meanings: sharing without a check, or no sharing at all." Letta told in real order (write -> optional review before applying -> merge -> push); 61-word S2 split into three sentences; "its Auto local gate" -> "Letta's Auto local gate"; "it should have been shared" -> "whether it should have been"; S4 restatement merged into S3 as a "so" clause; AutoAgent introduced as the second case. Closing antithesis "one shares without checking; the other does not share" removed (now the opening frame).
- **VI:12** role: evidence for VI-C. EDDOps given its own sentence after the repository study so that "none of these registries" covers only MCP registries, control planes, and governance registries; "provide/add" feature-list voice reduced ("MCP registries record namespaces and versions"). Point-last ("none of these registries generates ...") left: see 3.
- **VI:15** role: evidence -> point. Point first: "The occupied cells match the feedback-based expectations once automatic admission is distinguished from loss estimation." 11-word fronted phrase removed ("Where an [Auto × Auto] promotion gate estimates a loss change"); S2 restatement of VI:8 folded into a clause ("the cell's judged and delayed cases prune, rewrite, or merge instead").
- **VI:16** split into two paragraphs, one claim each: (a) the empty human-local cells (unchanged sentences); (b) the bottom row, opened by a frame "The bottom row, where no local gate operates, holds two kinds of system." SkillRL/SkillForge appositive moved after the verb ("because neither checks its failure-driven skill updates: new skills in SkillRL, rewrites in SkillForge").
- **VI:17** role: point (section close). Boundary-case sentences now open on old material ("The audit's boundary cases leave the grid unchanged. Six systems promote without artifact lineage."); "Spotify is one of them" -> "Five, including Spotify"; "the tier rule" -> "the evidence-tier rule". Colon reveal "What the grid reveals is a division of capabilities:" -> "Across the grid, capabilities divide:" with the finding's wording kept ("no system has both the learning of the top row and the governance of the bottom row").

### R1 document / R2 sections

- **V opening (V:2)**: links back to Section IV ("the previous section found a gate on such edits nearly everywhere a local loop exists"; no REF added) and ends its opening segment on the forecast "the class predicts where automatic acceptance and automatic promotion occur". Table pointer moved into a parenthetical. "evidence ... as a feedback signal" introduces "signal" from old "evidence" (synonym cycling fixed). Signal properties verbalized ("how soon the signal arrives, whether it is exact, and whether it depends on judgment").
- **VI opening (VI:1)**: now forecasts the section's finding in its last sentence, in VI:17's wording and orientation: "no surveyed system has both the learning of the top row (a program keeps the local edit) and the governance of the bottom row (no local gate)". Row orientation verified against `submission/figures/fig3_design_space_ieee.png`: rows are the local gate, Auto at top, None at bottom. "This is the additional decision" -> "Whether to adopt the edit is the additional decision".
- **D9 caveat accounting**: (a) measure-and-tasks: V:5 S4 and VI:6 S4 shrunk to clauses. (b) recipient evidence: V:10 S2 shrunk to a clause; V:18 S4 deleted; VI:1 kept short (section opening); VI:3 (home, VI-A) kept. (c) delayed credit: home V:14 S3 kept; V:15 S4 now the paragraph's point clause; V:16 S2 -> "Besides the credit problem"; V:17 first expectation's delayed clause cut (the "either loop" clause in the second expectation covers it).
- **V:15 AlphaEvolve note** moved to V:4 (C1).
- **VI:4** S5 ("These are concrete instances ...", restatement of S1, no keys/numbers) deleted.
- **VI:16** split (see Re-draft).

### R3 flow

- V:1: delay features moved to the stress ("is known only later", "only after months"); one sentence frame varied.
- V:3: S5 ends "the signal that supports that decision".
- V:4: "This makes" -> "Such a check is"; S5 "The broader benchmark score" -> "DGM's broader benchmark score" (referent).
- V:7: list subject moved after the verb ("An observed outcome records what happened after an episode: whether ..."); no longer mirrors the Table IV-1 C2 cell; noise sentence joined by a colon to its two examples.
- V:8: point moved to S1 ("In different systems, the same kind of outcome supports different operations."); "therefore" cut.
- V:9: "such as ..." interruption moved to the end of S1; "more generally" -> "generally".
- V:11: S2 ends on "being measured" -> "No independent exact answer exists for the preference being measured" (kept); S4 "earlier in the process" -> "applies its calibrated judge to replies" (interpretation).
- V:12: "this distinction" -> "do not record calibration" (referent).
- V:16: attribution moved left ("As the evaluation of harness optimizers emphasizes, ...").
- V:17: "either half" -> "either loop" (registry).
- VI:2: figure pointer moved to S1 parenthetical; "so" joins aggregation to the population change.
- VI:5: S1 names where the check sits ("at an aggregator or a server"); "They do not instantiate" -> "so neither system instantiates" (pronoun drift fixed); EvolveNet's aggregator clause moved forward.
- VI:7: garden path "that later runs reuse" -> "that later runs draw on"; "this shared environment" / "That pool" -> "the archive" (one name); "apply programmatic decisions" -> "make these admission decisions by program".
- VI:8: noun-pile subject replaced by systems as subjects ("NanoResearch merges semantically, AutoManual rewrites and consolidates by judgment, and ShareMem consolidates by judgment"); S3 -> "The feedback classes anticipated this distinction: a program can decide promotion where no per-edit estimate of improvement exists."
- VI:9: S6 split into two sentences; "which makes" (whole-clause referent) -> "That substitution makes"; CASCADE "also" cut.
- VI:11: S5 folded into S4 as a "so" clause after the citation; "markdown" -> "Markdown".
- VI:13: S3 and S4 merged ("In the surveyed descriptions, however, session feedback triggers neither ... so these platforms supply ...").
- VI:14: two pointer sentences merged; "while allowing ... to be compared" -> "and it sets their complementary capabilities side by side".

### R4 sentence

- V:3 S1 passive on own method -> "We assign each system to a class by the constraint that binds first"; S3 abstract subject -> "a signal with no independent ground truth is C3".
- V:4 "DGM makes a narrower acceptance decision" -> "DGM decides acceptance more narrowly".
- V:9 "They are treated as a distinguishable case" -> "We treat them as a separate case".
- V:10 "is not an evaluation of the recipient" -> "does not evaluate the recipient"; trailing participle "connecting the reliability of feedback to the integrity of its source" -> "Feedback in this class is also only as reliable as its source, because its channels can carry ..." (interpretation).
- V:12 "the meaning of its acceptances is less established" -> "what its acceptances mean is less established".
- V:17 "local automatic acceptance is most directly supported by" -> "exact checks and observed outcomes support local automatic acceptance most directly".

### R5 concision

- Cut: "as a whole" (V:5), "also" (V:5, V:6, VI:9), "important" (VI:3), "concrete" sentence (VI:4), "essential" (VI:8, see 3), "broad" (V:14), "more generally" (V:9).
- Net words: V prose 1214 -> 1213, VI prose 1336 -> 1334 (file totals below).

### R6 shape

- V:12 S1 split by a semicolon so "calibrated" precedes the stress "evidence of that preference".
- V:17 S4 split into two sentences (automatic promotion / human promotion and delayed feedback).
- VI:10 S2 (61 words) split into three.
- VI:17 S2 split; final sentence a plain claim.

### R8 integrity

- Letta's local review / promotion push now has visible doers (see 2). No claim strength changed; VI:9 evaluative wording kept word for word.

### R9 punctuation

- No em-dashes in either file. Semicolon chains removed in VI:6 S2 (cut) and VI:10 S2 (split). American spelling throughout ("catalogue"/"analogue" not used here).

## (2) Interpretations and supplied doers

Interpretations (specifics taken from the same or neighboring text; author to confirm):
- V:5 "a finite suite samples only part of the patch" (was "task distribution"; registry term).
- V:6 grouping overfitting and pool growth as one problem, "the side effects of cheap, repeated acceptance" (the original attributes overfitting to repeated optimization and pool growth to cheap acceptance).
- V:7 "An observed outcome records what happened after an episode" (rephrasing of "provides an observable result after an episode").
- V:10 "only as reliable as its source" for "connecting the reliability of feedback to the integrity of its source".
- V:11 SkillForge "applies its calibrated judge to replies" for "uses its calibrated judge earlier in the process" (supported by IV's opening: the calibration concerns which replies are inadequate).
- V:15 CORAL "periodically" for "on a heartbeat".
- V:16 "outcome gains alone cannot distinguish" for "are also insufficient to distinguish".
- V:17 "bloat" -> "pool growth"; "proxy optimization" -> "proxy overoptimization" (one name per concept, V:6 and V:13).
- VI:1 row glosses "(a program keeps the local edit)" / "(no local gate)", from the Fig. 3 axes and Table VII-1.
- VI:1 "Whether to adopt the edit" naming the decision that "This" pointed to.
- VI:7 "make these admission decisions by program" for "apply programmatic decisions within this shared environment"; "No candidate travels beyond the archive" for "That pool is as far as any of them travels".
- VI:8 "Automatic admissions differ in what they establish" for "Not every automatic admission has the same evidentiary meaning".
- VI:9 "That substitution" as the referent of "which".
- VI:15 "once automatic admission is distinguished from loss estimation" for "once the meaning of automatic admission is made explicit".
- VI:16b "where no local gate operates" and "holds two kinds of system" (frame from the figure axis and the two sentences that follow).

Supplied doers:
- V:3 "We" (the authors) assign classes.
- V:5 "A gate that estimates the change in patch loss" (the estimator in "Estimating ... requires").
- V:9 "We" (the authors) treat simulated outcomes as a separate case.
- VI:10 "Letta" pushes shared-memory changes (was passive "are then pushed").
- VI:16b "neither checks" (SkillRL, SkillForge) for "are kept unchecked".

## (3) Ledger FLAGs deliberately left, with reasons

- V:1 2.5 (vignette repeats the Introduction's four cases): cross-section author decision (D1 keeps the Introduction's prelude); the vignette stays as V's prelude.
- V:4 3.1 (system tour): the systems are instances of S1's exact check; one framing sentence precedes them.
- V:7 5.1 "meaningful": it is the term contrasted with "noisy or confounded"; no specific replacement in the text.
- V:9 2.4 (two claims) not split: splitting leaves two two-sentence paragraphs; both sentences concern what a gate can learn from C2 outcomes. V:9 5.3 hedge "usually ... more readily" kept (part of the claim).
- V:10 2.4 (promotion; poisoned channels): kept in one paragraph; the second claim is now its own sentence. A one-sentence paragraph would be worse.
- V:11 4.12 (CASCADE joined to the uncited repository review): wording kept; citation question is AUTHOR FLAG 8.
- V:14 5.1 "meaningful": cutting it would change the claim (outputs exist earlier; meaningful outcomes arrive later).
- V:16 "harness": source term (AUTHOR FLAG 13).
- V:17 4.12/4.13 "human promotion should hold": verb left (AUTHOR FLAG 11).
- V (section) AI cap: antitheses now V:5 S1, V:9 S4 (that/why), V:18 S1; three in about 1,200 words.
- VI:2 2.5 and Fig. 2 caption duplication: caption is a raw LaTeX block (invariant).
- VI:5 "harness", "aggregator": source terms.
- VI:7 2.2 point-last: the opening states the mechanism (admission to an archive); the closing sentence is its consequence. VI:7 S4 antithesis kept (claim wording).
- VI:11 4.1 seven-product list subject: moving it after the verb needs a passive or a derived count ("Seven tools"), which the invariants forbid adding.
- VI:12 2.2 point-last: role is evidence for VI-C's opening claim (VI:11 S1); the closing "none of these registries" sentence is the limit. VI:12 1.5 (relevance of "only one of 254 edits deprecated a skill") left: the relevance is not stated in the text, and supplying it would be a new claim.
- VI:13 "provide/supply" capability voice partly kept: the named controls (versions, thresholds, rollback) are the mechanism.
- VI:16 2.5 (S1 restates the Table VII-1 caption): caption is invariant; the prose sentence carries the "failure-driven loop" qualifier the caption lacks.
- VI:17 4.15 "the audit", "T5": no REF may be added; "evidence-tier rule" is the only gloss added.
- VI (section) AI cap: antitheses now VI:1 S2, VI:5 S4, VI:7 S4, VI:9 S7 (author-flagged wording); VI:10 S7 and VI:17's colon reveal removed.
- Table IV-1 / Table VII-1 cells and captions (faulty coordination, "lift", "climb", caption/header mismatch): table and caption lines are invariant.

## (4) AUTHOR FLAGS

1. **V:6 count.** "Two problems remain even with a reliable checker" kept word for word. The text lists three effects (attribution; overfitting the suite; pool growth). The re-draft names two problems, attribution and "the side effects of cheap, repeated acceptance", and places overfitting and pool growth under the second. Confirm that grouping, or change the count to "Three" and list them separately.
2. **Table labels** "Table IV-1" (tab:IV-1) in V and "Table VII-1" (tab:VII-1) in VI: internal labels the build renumbers (per the task note); not changed.
3. **V:14, The AI Scientist [@lu2024aiscientist]** illustrates "the setting" (was "the broad setting"), not a weeks-long delay across many edits. Example choice is the author's.
4. **VI:9 "the production-viable pairing rather than a compromise"**: wording kept exactly; the sentence was split and its "which" became "That substitution". Strength not changed; the author should calibrate it.
5. **VI:10 Letta classification**: the Auto local gate rests on an optional review ("with the option off, the system would sit in [None × None]"); no Letta citation in the paragraph ([@letta2026memfs] is cited in IV).
6. **Row orientation**: checked against `fig3_design_space_ieee.png` (rows = local gate; Auto top, None bottom). VI:1's new forecast and VI:17 use "top row"/"bottom row" in that orientation. [None × None] (SkillRL, SkillForge, failure-driven but unchecked) sits in the bottom row, so "the governance of the bottom row" refers to the [None × Auto] and [None × Human] occupants; confirm the wording.
7. **VI:6 "graphs"** (Evo2Team): source term; unexplained.
8. **Citations missing in the sentence**: V:10 (poisoned memories, injected tool instructions; VII cites zou2024poisonedrag, chen2024agentpoison, xu2026mcfa); V:11 (review of Anthropic's skills repository); VI:8 (AutoManual); VI:10 (Letta); VI:12 (EDDOps).
9. **V:8 SAGE** cited as an observed-outcome example while V:9 calls its AppWorld outcomes simulated.
10. **Table IV-1 C2 row** lists Sierra; the prose describes Sierra only at promotion (VI:9).
11. **V:17 "human promotion should hold the observed outcomes and judgments"**: the verb's intended relation is unclear.
12. **VI:7 "AlphaEvolve has produced gains used within Google"**: no citation in its own sentence.
13. **"harness"** (V:16, VI:5): likely the cited sources' term (ong2026harnesseval, nie2026evolvenet).
14. **VI:8 "essential" cut** ("The distinction ... is therefore essential"): treated as an intensifier per the ledger; restore if the author meant it as a claim.
15. **VI:12 EDDOps regrouped**: the original "EDDOps gates promotion ..., but none of these registries generates candidate artifacts from failures" may have meant to include EDDOps in the "none". It now stands as its own sentence before the registries, and "none of these registries" covers only MCP registries, control planes, and governance registries. Confirm whether EDDOps generates candidates.
16. **V:18 S4 deleted** ("In every class, sharing remains an additional empirical question: even the same exact checker must be applied to the recipient's relevant cases before broader performance is established."): no keys or numbers; covered by II-A ("Promotion must preserve that meaning or establish the improvement again"), II-C, and VI:1. Restore if the author wants the exact-checker case stated in V.
17. **V:2 link back** "the previous section found a gate on such edits nearly everywhere a local loop exists" paraphrases IV's finding (89 of 96) without the number or a REF; confirm the phrasing.

## (5) Word counts (wc -w, whole file incl. tables and LaTeX)

| file | before | after | change |
|---|---|---|---|
| V_feedback_signal_classes.md | 1526 | 1523 | -3 |
| VI_promotion.md | 1657 | 1655 | -2 |
| total | 3183 | 3178 | -5 (-0.2%) |

Prose only (excluding headings, tables, LaTeX): V 1214 -> 1213; VI 1336 -> 1334.

## (6) Invariant result

`cg_invariants.py cg_pre cg_work`: no FAIL or WARN lines for V_feedback_signal_classes.md or VI_promotion.md; overall "CG INVARIANTS: PASS" at the time of the final run. No em-dashes.

## Group D

# Changes, group D: Sections VII, VIII, IX (R-6 re-draft + S5 Polish R1-R9)

Files: `cg_work/VII_failure_surface.md`, `cg_work/VIII_missing_architecture.md`, `cg_work/IX_families.md`. Paragraph ids follow ledger_D numbering (prose paragraphs and list items, tables and captions not counted).

## (1) Change log by level

### Re-draft (R-6)

| ¶ | target role / point / protagonist (from plan + reverse_D) | what changed |
|---|---|---|
| VII:2 | evidence + explanation / accumulated artifacts degrade following and blur attribution; retirement keeps edits assessable / accumulated artifacts | Accumulated instructions are now the subject of S1 ("become harder to follow and slow the response"); Ratchet moved after the verb with its attribution kept ("At the system level, Ratchet finds that model-written skills need lifecycle hygiene before they produce gains"), which removes the 12-word nominalized subject, the empty verb "makes ... visible", the unresolved "the consequence" and the end on "at the system level". S3 recast with a doer for "caused it". |
| VII:4 | explanation / the tool binding needs controlled revision at every later change / the tool binding | Cut the restated Table X-1 controls ("provenance, write gating, and reversible memory changes"; "restricted tool permissions and an instruction privilege hierarchy"); the citations now attach to "the memory controls [@su2026chronomem; @yu2026rollbackrepair] and tool controls [@wallace2024hierarchy] listed in the table above". S1 now ends on the paragraph's point, "controlled revision of the tool binding itself". Gerund subject "Checking only the initial registration" -> "A check made only at the initial registration"; "authorized it" -> "authorized the binding". |
| VII:7 | point (finding) / judges are calibrated, but none is kept calibrated while the rubric changes / surveyed systems, then SkillCoach | Point moved to S2 and stated once ("Three scaffold systems ... report calibrating a judge against people ..., but no surveyed system reports calibration maintained across continuing rubric revisions and deployment drift"). Deleted the restatements S5-S6 ("The missing result is therefore more specific than an absence of calibrated judges. It concerns keeping calibration while the criterion keeps changing"); no keys or numbers in them. The 62-word S3 split into the audit with its authors' caveat, then the method and result; the two "it"s resolved ("its judge after editing it"; "The audit compares"). All four numbers and both zhu2026skillcoach keys kept. |
| VII:9 | point + evidence / a fixed evaluator degrades with repeated use, so a gate needs safeguards / the evaluator | Opening kept. Proxy overoptimization and shifting human criteria shrink to a pointer to Section V ("described for judged feedback") with both citations kept in the paragraph; the evaluator ("It remains subject to ...") is the subject. Path dependence and drift kept as new content. Hedges cut from four "can" to two (S1 general claim; Singh's cited mechanism). "Consequently" -> "therefore". |
| VII:12 | point / a scaffold specialized to one deployment can degrade another; the promotion loop's checks bound it / a scaffold | Vague opener "Specialization creates a related boundary" removed; the paragraph now opens on the table's own term, "Patch overfitting follows from specialization", then the mechanism. Receiving-side evaluation and the evidence radius kept as a pointer. Closing caveat "This does not eliminate uncertainty outside the evaluated cases" deleted as a restatement of II (D9a home: II-A/II-B "an accepted edit is evidence of improvement only on the measure and tasks evaluated"); it held no keys or numbers. |
| VII:13 | point / plasticity loss; controls must stay available for the system's lifetime / a scaffold | Names the failure ("a scaffold can lose plasticity"), cutting the near-verbatim table wording "old rules, polluted memories, and drifting tool versions" to "old and polluted artifacts" (interpretation). "provides one related mechanism" -> "is one mechanism related to this loss" (referent resolved; strength unchanged, see AUTHOR FLAG 9). |
| IX:7 | evidence / RLHF homogenization and adaptation cost motivate separating broad behavior from customer requirements / the distinction | Framing sentence first ("Two lines of work help motivate the distinction between broad model behavior and customer-specific requirements"), keeping "help motivate"; "Work on RLHF reports" -> "Studies of RLHF report"; "Tiwari et al. approach it" -> "approach the distinction". |
| IX:14 | other view (lineage) / optimizers of prompts, programs and scaffolds establish many underlying mechanisms / those optimizers | The frame now covers every system named ("Optimizers of prompts, where the first research line started, and of programs and scaffolds establish many of the underlying mechanisms") and ties to IX:2 / Table VIII-1's first row. The closing claim moved to the opening; "another important lineage" (intensifier) cut. Stays in its subsection (D11). |
| IX:15 | point (section close) / the survey's contribution is the joint reading at deployment scope / the survey | Abstract subject "The contribution here is their joint reading" -> "The survey's contribution is to read these precedents jointly"; "that comparison" (no antecedent) -> "the joint reading". The Supplementary pointer moved to the front of the last sentence, so Section IX now ends on "make the joint reading explicit" and not on "(Supplementary Material S7)". The four questions are kept (they are the "four questions" the Table II-2 Guo row refers to). |

### R1 document / R2 sections and paragraphs

- VII opening (VII:1): new S1 ties back to Section VI and to D10: "Each edit the loop keeps or promotes changes the context of its next decision." It replaces "An improvement loop changes the context in which its next decision is made", which ended on a passive. The table pointer now comes before the count ("Table REF(tab:X-1) pairs each failure with its control in the loop. The literature documents six of them ..."). A point sentence was added at the end of the opening segment: "Production systems provide the individual controls, but no surveyed system runs them together." This is VII:14 S3's factual clause, forecast (D10); VII:14 keeps the full sentence as the close.
- VII:3: framing sentence covers both channels ("Persistent memory and connected tools create another route to lasting error"), so the paragraph makes one claim (contamination channels). It stays one paragraph because VII:4 answers both channels.
- VII:5 (VaG): reduced to a pointer plus the new content. The derivation premise is now one sentence; VaG's result moved to a short clause with its key; the paragraph's new content (check before commitment, track afterward, history needed but not enough) is kept.
- VII:8: the scope note ("not included in the scaffold scores") moved from the paragraph's stress position to the first sentence, with the S6 pointer. The paragraph now ends on the RLPR finding.
- VII:10: "The failure-mode hypothesis discussed in Section REF(sec:why)" -> "The hypothesis in Section REF(sec:why), that failures in a bounded deployment fall into a catalogue of modes". IX-A has no proper name for it ("a hypothesis", "these hypotheses"), so the reference uses IX-A's own description (IX:10 "failures there fall into a catalogue of modes"). REF token kept. "adds a conditional implication" -> "has a conditional implication".
- VII:14: "these risks" -> "the failure surface" (one name for the section's failures; matches the Table X-1 caption); "the surface" in S3 -> "the failure surface". Opening no longer ends on the caveat ("No failure is exclusive to one feedback class, but the classes help organize the failure surface"). "observable outcomes" -> "observed outcomes" (registry).
- VIII:8: opens on the finding ("... compares the closest systems, and each covers only part of the four properties"). Restated table cells for FederatedSkill ("semantic skill exchange and an auditable server decision log") and EvolveNet ("evaluates shared merges and can return to the previous shared harness") cut to "both adapt locally and share the result, but stay within one operator"; both keys kept (interpretation; D7).
- VIII:10: VaG mention kept as a pointer (already only a REF, no key in VIII); "the rollback envelope" (a term that appears only in Table X-1) -> "the reversal path", the term S1 has just used.
- IX:1: "The uneven architecture has a history" -> "The loop's uneven development has a history" (ties to I ¶5's "built unevenly"; VIII never called the architecture uneven). "Different research communities" -> "Five research lines" (registry term; "five" moved from S4). "initial problem" -> "starting problem".
- IX:2: framing sentence added: "The first three lines each built one condition." (Table VIII-1 names conditions 4, 5, 3 for them.)
- IX:3: framing sentence added for both lines: "The last two lines study artifacts after they are kept." (interpretation).
- IX:5: the two claims are ordered as convergence (point), then caveat, then decomposition with examples, so the paragraph no longer ends on the defensive caveat. "The convergence" now has an antecedent ("The five lines converge: ...").
- IX:13: "The former" / "The latter" -> "The persistent-state survey" / "The memory-security survey". The table holds two "Ding et al." rows, so a name would be ambiguous.

### R3 flow

- VII:2, VII:7, VII:9: point of view fixed in the re-drafts (above). The pronouns and pointers now resolve: "the consequence" is gone; "its judge after editing it"; "the binding".
- VII:3: "In memory, ..." dropped; the attack list follows the frame directly. The ledger's S4 old-to-new flag ("In CVE-2025-54136") is left; see section 3.
- VII:11: "A study of multi-agent systems identifies" -> "Cemri et al. identify fourteen failure modes in multi-agent systems" (supplied doer). S3 gerund subject -> "Treated as editable scaffold coordinates, routing and role assignments become subject to ...".
- VIII:7: "The terms ... refer to the same boundary here" -> "In this audit, *cross-tenant* and *cross-organization* name the same boundary"; S2 now opens on the known "Property (b)" and ends on "within one operator".
- VIII:12: "those systems" (no antecedent) -> "systems with delayed outcomes".
- IX:4: "Building a record of recurring failures was none of their starting problems" -> "None began by recording recurring failures"; "within the substrate a particular line studies" -> "within each line's own substrate".
- Re-run rule: R3 re-checked on VII:1-5, VII:7-14, VIII:7-13, IX:1-5, IX:7, IX:11, IX:13-15 after the R4-R6 edits.

### R4 sentence

- VII:2 S2, VII:4 S2, VII:7 S3, VII:11 S2-S3, IX:7 S1, IX:15 S1: characters as subjects (see above).
- VII:5 S3: "VaG's limited recovery after such rollback supports checking contamination before commitment and tracking consequences after it" -> "VaG recovers little after such rollback [@shang2026vag], which supports checking for contamination before commitment and tracking consequences afterward".
- VIII:9: "It is kept separate" (passive on the authors' decision) -> "We keep it separate ..."; "making an unsupported decision about whether" -> "decide without support whether"; S2-S3 merged with "because" (interpretation).
- VIII:12 S1: "The extent of automation should depend on the feedback" -> "How far to automate should depend on the feedback"; S2 "Exact checks provide the most direct setting for testing" -> "With exact checks, a transferred skill can be tested most directly"; S4 reordered so it parallels the class series ("For judged quality, a human promotion gate supported by lineage and rollback is a reasonable design choice").
- IX:6 S4: capability voice "The scaffold provides a place to encode those requirements with a scope narrower" -> "The scaffold encodes those requirements at a scope narrower".
- IX:11 S2: "provide an inspectable representation for those interventions" -> "represent those interventions in inspectable form".

### R5 concision

- VII:7: two restating sentences deleted (S5-S6).
- VII:9: four "can" -> two.
- VIII:11: "useful" cut (strip test). "extensively" kept (see section 3).
- VIII:13: the defensive caveat merged into S1 ("... a target for the settings that can support an automatic local gate, not a requirement to automate every decision in every domain"); "preserve the ability to inspect and reverse its adoption" -> "still be able to inspect and reverse the edit's adoption".
- IX:10 S4: "Its negative result is equally relevant" -> "It also gives a negative result" ("equally relevant" fails the strip test).
- IX:12 S2: "subsequently used" -> "then used".
- IX:14: "important" cut.

### R6 shape and emphasis

- VII:1: the sentence ending "addresses it" is replaced ("... with its control in the loop"); Sculley et al. moved before the verb ("that Sculley et al. identified for machine-learning systems [@sculley2015debt]").
- VII:5: the endings "after it" and "by itself" -> "afterward" and "does not by itself perform the recovery".
- VIII:5 (list item c): ended on "access it" -> "and policies control who may access the artifact".
- VIII:11 S4: ended on "often through a language model" -> "The nearest scaffold systems instead often use a language model to select, revise, or merge symbolic edits."
- IX:2 S2: trailing participle "corresponding to the complexity penalty" -> "which corresponds to the complexity penalty".
- IX:5 S3: appositive "A system that updates both, SIA, still treats" -> "SIA updates both and still treats them as separate levers".
- IX:9 S3: the where-clause moved to the end, so it no longer splits the two coordinated objects ("Its evidence includes the accuracy recovered through majority voting ... and long-range dependence measured on one natural-text corpus, where fewer than a tenth of tokens depend on distant context").
- IX:11 S4: ended on "independently of them" -> "its findings about acceptance gates, feedback, and promotion rest on the corpus alone".

### R8 integrity

- No claim, number, citation, quotation or cross-reference changed. Attributions kept: Ratchet "finds", PoisonedRAG "demonstrates", SkillCoach's authors "describe ... as judge-assisted", RLHF studies "report", Tiwari et al. "approach", Ding et al.'s survey "finds".
- Grouped attributions (VII:4) keep the original split: su/yu for the memory controls, wallace for the tool controls.

### R9 punctuation

- No em-dashes. Colon reveals: at most one per paragraph in the rewritten text (VII:2, VII:10, VII:12, IX:5, IX:9). The semicolon chain in VII:14 is a parallel taxonomy and was left (house style allows it). Serial comma used throughout.

### AI-failure-mode sweep (rewritten sentences)

- Removed: the antithetical close in VII:7 S5-S6; "important" (IX:14); "useful" (VIII:11); "equally relevant" (IX:10); the capability voice in IX:6 ("provides a place to"); the empty verbs "makes ... visible" (VII:2) and "provides one related mechanism" (VII:13); the trailing participle in IX:2; the caveats in the stress position (VII:8, VII:12, VIII:13, IX:5); the tour framing in VII:3 and IX:14.
- Left: one "not X but Y" in IX:11 S3 (load-bearing three-paper argument; ledger says keep) and one in VIII:13 (the merged scope clause).

## (2) Interpretations and supplied doers

Interpretations (the author should confirm):
- VII:1: "Production systems provide the individual controls, but no surveyed system runs them together" forecasts VII:14 S3's factual clause in the opening (D10). The causal half ("stays largely unmitigated because") stays only in VII:14.
- VII:3: "Persistent memory and connected tools create another route to lasting error" widens the original frame ("Persistent memory creates ...") to cover the tool/MCP sentences.
- VII:4: "the memory controls ... and tool controls listed in the table above" stands for "provenance, write gating, and reversible memory changes" and "restricted tool permissions and an instruction privilege hierarchy", with the same keys on each.
- VII:9: "described for judged feedback" points to Section V's treatment of gao2023overoptimization and shankar2024validators; "human criteria that shift during grading" -> "the shifting human criteria" (Shankar's finding, stated without "can" as V states it).
- VII:12: "Patch overfitting follows from specialization" names the prose's failure with the Table X-1 row name.
- VII:13: "old and polluted artifacts" for "old rules, polluted memories, and drifting tool versions" (the table keeps the full list).
- VIII:8: "each covers only part of the four properties" (read from Table IX-1: no row is full in all four); "both adapt locally and share the result" (from the (a) full / (b) partial cells).
- VIII:9: "because" joins the separation decision to its reason (originally two juxtaposed sentences).
- IX:2: "The first three lines each built one condition" (Table VIII-1 conditions 4, 5, 3).
- IX:3: "The last two lines study artifacts after they are kept."
- IX:7: "Two lines of work help motivate" now covers Tiwari et al. as well as the RLHF studies (originally only the RLHF work "helps motivate"; Tiwari et al. "approach it").
- IX:14: "Optimizers of prompts, ... and of programs and scaffolds" as the frame for OPRO ... SICA; "where the first research line started" ties prompt optimization to Table VIII-1's first row.
- IX:15: "these precedents" for "their" (the antecedent is IX:13-14 as a whole).

Supplied doers:
- VII:11: "Cemri et al." for "A study of multi-agent systems" (from the key cemri2025mast; near-certain).
- VIII:9: "We" (the authors) for "It is kept separate".
- IX:7: "Studies of" for "Work on" (same actor, the cited studies).

## (3) Ledger FLAGs deliberately left

- VII:1 3.2 / AUTHOR FLAG 4: "in a measured case" kept verbatim (scope of the claim).
- VII:2 5.1: "meaningfully" kept. It carries the claim (an assessment that isolates the new edit), so dropping it would weaken the claim.
- VII:3 3.2: S4 still opens "In CVE-2025-54136". Recasting it would need a generalization from one case. One-claim split not done because VII:4 answers both channels together.
- VII:6 3.1 / 3.6 / 4.9-4.11: the example paragraph is unchanged. The house style puts the example first ("show before you name"), and the stacked modifier in S1 is short. A trial rewrite added words without making the case clearer.
- VII:7 AI-sweep (number load 50 / 10 / 82% / 96%): kept (invariant; AUTHOR FLAG 5).
- VII:9 6.4: S4 is still uncited (AUTHOR FLAG 6).
- VII:13 6.3: the strength of the lost-in-the-middle link is unchanged (AUTHOR FLAG 9).
- VII:14 5.3 / 6.3: the causal "because" is unchanged (AUTHOR FLAG 10).
- VIII:1 3.7: "under equivalent controls" kept. Saying what the controls are equivalent to would change the claim (new AUTHOR FLAG 21).
- VIII:3-6 4.12: the list items are still not fully parallel. They are definitions with bold terms; only (c)'s ending changed.
- VIII:4 4.14 / 2.3: "or customers" kept; dropping it changes the property's scope (new AUTHOR FLAG 22).
- VIII:11 5.1: "extensively" kept; it describes the size of the cited literature.
- VIII:12 4.12: S2-S5 are now closer to parallel ("With exact checks", "Observed outcomes", "For judged quality", "Delayed outcomes"), but not fully.
- IX:5 4.12: "the harness-optimization papers" alongside Meta-Harness and MOSS kept (AUTHOR FLAG 12).
- IX:8 2.5 / 6.3: "the cheaper path" kept (AUTHOR FLAG 15). S2 is a one-clause restatement of the Introduction that the argument needs locally.
- IX:9 3.6 / 4.14: S1 still ends on "may be effective". The hedge is part of the hypothesis framing (D4), and moving it would turn the hypothesis into a claim.
- IX:10 3.6: S1 ends on the setting ("evaluator expectations"). The bounded setting is a theme the negative result in S4 depends on.
- IX:11 3.1 / 3.7: "these hypotheses" -> "On that hypothesis" kept (AUTHOR FLAG 14; load-bearing three-paper argument).
- IX:12-13 2.5 (axis restatements of Table II-2): IX:13's findings sentences are kept. They are what the table lacks, and the "Neither asks ..." sentence is the paragraph's point.
- Section level, 1.5 (sec:why and "Relation to neighboring surveys" under IX): not moved (D11; AUTHOR FLAG 3).
- Captions and labels "Table X-1." etc.: internal labels the build renumbers; not changed (per instructions).

## (4) AUTHOR FLAGS

Carried from ledger_D (unchanged by this pass):
1. Stale table labels and caption numbers (tab:X-1, tab:IX-1, tab:VIII-1, tab:II-2). Reported as internal labels the build renumbers; confirm that the caption text is renumbered too.
2. VII:10 forward reference to Section REF(sec:why). The wording now uses IX-A's own description of the hypothesis ("failures in a bounded deployment fall into a catalogue of modes"), but the reference still points forward to Section IX. Moving sec:why earlier is a structural decision (D11).
3. Placement of sec:why and "Relation to neighboring surveys" under "How the research lines fit together" (D11).
4. VII:1 "documents six of these failures in a measured case": what "a measured case" means (one study per failure, or one study).
5. VII:7 number load (50 paired instances, 10 task families, 82% to 96%) against "relationships over values".
6. VII:9 "Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite stays fixed" has no citation.
7. VII:9 repeats Section V's keys (gao2023overoptimization, shankar2024validators). They are now framed as a pointer ("described for judged feedback"), but the keys remain in VII. Cutting them is the author's call.
8. VaG's descendants finding appears in IV (stated with its key), VII:5 (now one short clause with its key) and VIII:10 (a pointer via REF(sec:findings), no key). Decide whether VII:5 should drop the key and point to Section IV.
9. VII:13 "Long-context degradation [@liu2023lostmiddle] is one mechanism related to this loss": the link to plasticity loss is asserted, not shown.
10. VII:14 "the failure surface stays largely unmitigated because no surveyed system runs them together": a causal claim and the section's point.
11. Table IX-1: SkillForge "(c) partial" has no stated reason; "not documented" vs "not reported".
12. IX:5 "GEPA, Meta-Harness, MOSS, RCL, PACE, and the harness-optimization papers": Meta-Harness and MOSS are harness-optimization papers.
13. IX:10 growth variables (catalogue size with observed experience; intervention budget with sequence length): check against the AoE text (math-claims discipline).
14. IX:11 "these hypotheses" then "On that hypothesis": singular or plural.
15. IX:8 "Persistent artifacts offer the cheaper path": a cost comparison with no citation.
16. IX:4 "consequently": a causal reading of the history, stated flat.
17. Table II-2 caption "the only one to cover promotion across organizations" (holds among the nine listed); the Guo row's "all four questions" now has a referent nearby in IX:15's four questions, but the row and the caption name different sets (the caption lists loop closure, gate type, signal class, governance).
18. IX:1 problem names vs the Table VIII-1 "Started from" column (aligning them means editing table cells).
19. VII:3 "major agent frameworks": confirm that "major" is the source's own word.
20. Table X-1 "Evaluation fragility": "read non-independently" is unclear.

New in this pass:
21. VIII:1 "under equivalent controls": the text does not say what the controls are equivalent to (presumably those within one organization). Clarifying it would change the claim's wording.
22. VIII (b) "organizations or customers": the boundary has three names ("organizations or customers", "cross-tenant", "receiving tenant"). VIII:7 now defines cross-tenant = cross-organization "in this audit", but "or customers" in (b) widens the property. Decide whether to keep it.
23. VII:12: the deleted caveat ("This does not eliminate uncertainty outside the evaluated cases") relies on II's statement of the evidence radius (D9a). Confirm that VII needs no local restatement.
24. VIII:8: the cut prose descriptions of FederatedSkill ("semantic skill exchange", "auditable server decision log") and EvolveNet ("evaluates shared merges", "can return to the previous shared harness") now live only in Table IX-1. FederatedSkill's "semantic" exchange is not in the table's wording ("privacy-preserving aggregation of skill edits"). Restore it if the qualifier matters.

## (5) Word counts

| file | before (wc -w, whole file) | after | prose only (wc_D.py) before -> after |
|---|---|---|---|
| VII_failure_surface.md | 1267 | 1245 | 954 -> 929 |
| VIII_missing_architecture.md | 776 | 767 | 584 -> 573 |
| IX_families.md | 1574 | 1586 | 973 -> 985 |
| group total | 3617 | 3598 (-19, -0.5%) | 2511 -> 2487 (-1.0%) |

IX grew by 12 words because of the framing sentences added in IX:2, IX:3, IX:7 and IX:14, which the ledger asked for. VII and VIII shrank by more than that, so the group total is lower.

## (6) Final invariant result

`cg_invariants.py cg_pre cg_work`: `CG INVARIANTS: PASS`. No FAIL or WARN lines for VII_failure_surface.md, VIII_missing_architecture.md or IX_families.md (citation keys, numbers, REF tokens, headings, table lines, caption lines, raw LaTeX, display equations and bold terms are all identical modulo the registry substitution "observable outcomes" -> "observed outcomes"; no em-dashes; no British spellings).

## Group E

# Changes E: Section X, Appendix A, Appendix B (R-6 re-draft + S5 Polish R1-R9)

Files edited in place: `cg_work/X_open_problems_conclusion.md`, `cg_work/appA_formal.md`, `cg_work/appB_gates.md`. Paragraph ids follow `ledger_E.md` (pre-edit numbering). After the split, appA:4 becomes appA:4a-4e and appB:2 becomes appB:2a-2b.

## 1. Change log by level

### Re-draft (R-6)

| ¶ | target role / point / protagonist | what changed |
|---|---|---|
| X:2 | problem; no method attributes a failure to its editable cause across substrates; protagonist attribution (methods that attribute) | Opens on the gap ("No surveyed method attributes a failure to the responsible instruction, memory, skill, or tool binding across all substrates"), so the lead's "Attributing" is the old item. The restatement of Intro ¶5 / §IV (exact check detects, does not identify) shrinks to the clause "even where an exact check establishes that the output failed". The three methods move after a short subject and verb ("Three methods provide narrower starting points: ..."), with all three citations kept in the post-verb list. "this" (unresolved) is gone. Last sentence opens on "Attribution". |
| X:3 | problem; receiving-side evaluation is feasible in places but limited, and not yet connected to governance; protagonist receiving-side evaluation/checks | "show its coverage limits" → "show the limits of the checks' coverage" (pronoun resolved). "proposes a receiving-client gate but does not implement it" → "proposes but does not implement a receiving-client gate" (ends on the term, not "it"). S4 no longer states X:6's point: "remains an architectural problem" → "remains the architectural problem taken up last" (pointer to problem 5). "Existing" cut. |
| X:4 | problem; a judge must stay calibrated while its rubric changes; protagonist the judge | S1 opens on the judge as subject ("a judge must stay aligned with people across continuing revisions of its rubric"), replacing "the open question is how to keep". S2 joins SkillCoach and the gap with "but" (attribution to SkillCoach verbatim). S3 unfreezes "lacks a reported human-agreement result" → "also reports no human-agreement result", keeping the scope words "The neighboring reward literature also" (AUTHOR FLAG 2); the RLPR exception becomes its own clause after a semicolon. S4 kept. |
| X:5 | problem; delayed outcomes remove the per-edit gate, so optimizers must be judged on their attribution claims; protagonist the gate / harness optimizers | S1 "immediate per-edit acceptance is unavailable" → "no gate can accept each edit as it is made" (nominalization removed). S3 reordered so the new demand takes the stress: "assessed against both their final scores and their claims about why particular edits help [@ong2026harnesseval]". This also removes the repeated "as well as" ending shared with X:4. |
| X:8 | point (significance + now what); keep claim strength (D12) | S1-S3 unchanged verbatim (decision D12; AUTHOR FLAG X-1/1). S4 "That discipline must extend" → "Such governance must extend" (the relabel "discipline" removed; the pointer now names the act of S3). |
| appA:4 | explanation; split by job | Split into five paragraphs. (4a) assumptions: disclaimer first ("Nothing in the survey depends on the convergence statement below."), then "It holds under strong assumptions and is included to make gate stability precise."; the stacked assumption sentence is broken into labeled sentences "(A3) Proposal coverage with acceptance: ...", "(A4) Effective compactness of the reachable orbit.", "(A5) Summable bias, ...", "Let $0 \le L_D \le B$."; the (A3)-strength sentence keeps its first clause. (4b) proof sketch: the Robbins-Siegmund sentence. (4c) result: "The finite sum carries the content:" → "The content lies in the finite sum." and the second colon becomes ", meaning that". (4d) "This is convergence ..." → "The result is convergence ..." and the "; a globally suboptimal ..." clause becomes its own sentence. (4e) scope: opens on the old item ("The argument does not cover a non-stationary deployment ($D = D_t$)"), moves "not supplied here" inside, and ends on "continual learning". Every display equation and inline math token verbatim. |
| appA:5 | explanation; credit assignment is attribution, and the two results need different amounts of it; protagonist attribution | Table pointer restated with location ("Table REF(tab:A-1), at the head of this appendix, pairs ..."). "Scaffold systems do not differentiate ... They trace ..." merged with the attribution claim after a colon. Added the link sentence "The two formal results ask different things of that attribution." S5 split at the semicolon and at "which": "The convergence statement needs ... that (A3) assumes. That requirement is much stronger than the credit-assignment condition of Section REF(sec:loop), success with non-zero probability per failure." |
| appB:2 | split at "Read down the signal-class column." | (2a) families: S2's restatement of appB:1 shrinks to a relative clause ("which are not estimators of $\widehat{\Delta} L_D$"; the math token is kept); "Multi-sample agreement is listed because it is" → "Multi-sample agreement is" (metadiscourse cut); the trailing "one that should not be conflated with it" → "an operation distinct from, and not to be conflated with, mini-batch averaging" (ends on the noun, pronoun resolved). (2b) signal classes: opens "Read down the signal-class column for the structural content of Section REF(sec:signal)." (the summary close "That is the structural content of Section REF(sec:signal)." is folded into the opening, REF token kept); S5 subject shortened ("A judged (C3) deployment can use only the two families whose estimator is a judge."); "at all" cut; the colon/what-cleft split into two sentences. |

### R1 document

- X:1: the announcement ("The remaining problems become more specific when expressed in terms of the decisions a deployment must make.") → "Five problems remain, each sharper when stated as a decision a deployment must make." The section's opening now states the count and the organizing axis instead of presenting "the remaining problems" as old. The plan's "one per decision of the loop" was not written in, because the five heads do not map one-to-one onto the loop's decisions (see section 3).
- Section X conclusion test 1.9: the restated point (X:7) and significance (X:8) are kept in place; no new topic introduced.

### R2 sections and paragraphs

- appA:3: the framing sentence "Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability." moved from after the display to the paragraph's first sentence, so the subsection opens on its point.
- appA:4 and appB:2: split (see Re-draft), one claim per paragraph.
- appA:1 / appA:4 / appA:5: one name for one object: "an informal convergence proposition" and "the proposition" (appA:1) → "an informal convergence statement" and "the convergence statement"; appA:4 "a conditional statement" → "the convergence statement below" (matching appA:5's "the convergence statement").

### R3 flow

- X:6 S3 "Their integration must preserve" → "A system that integrates them must preserve"; S4 "the design must retain" → "such a system must retain" (pointer resolves to a stated noun). "The components exist in different systems." merged into S1 as "although the components exist in different systems".
- X:7: S3 split at "and"; the second clause now opens on its scope ("None of the public systems examined here has assembled the machinery for transferring the resulting improvement to another organization.").
- appB:1: "some of them" → "Some of these instantiations" (pointer resolved); comparative no longer split by the relative clause ("precede the per-edit gate and are better read as proposal pruning than as estimators of ...").
- appA:2: the proposal process and history are named before the symbol ("A candidate edit is drawn from a proposal process conditioned on the accumulated history $H_t$ of ...: $z_t \sim Q_t(z \mid H_t, \theta_s^t)$.").
- Re-run rule applied after every subject/opening change above; X:2-X:6 topic strings re-checked.

### R4 sentence

- appA:1 "No new theorem is claimed" → "We claim no new theorem" (supplied doer: the authors; the paper uses "we" elsewhere).
- appA:2 S4 split: "$Q_t$ is not uniform." then "A mode $m$ that recurs ... has expected contribution $f_m s_m$ to the failure rate, so ..." (the 18-word preposed conditional becomes the subject's relative clause; the "so" clause kept, AUTHOR FLAG 4).
- X:5 S1 and X:6 S3: nominalization subjects replaced (see above).

### R5 concision

- X:1 "when expressed in terms of" → "when stated as".
- appB:1 "several distinct ways" → "several ways".
- appB:2 "is listed because", "at all" cut.
- X:3 "Existing" cut. appA:4 "which are not supplied here" → "not supplied here" moved inside the clause.
- appA:9 "observable only when a later outcome reveals it" → "observable only through a later outcome" (doubled "observable/reveals" removed; ends on the noun).

### R6 shape

- appA:3 S6: four-item comma series → semicolon series with one label form ("for an exact check (C1) ...; ... for an observed outcome (C2); ... for a judged signal (C3); and ... for a delayed signal (C4)").
- X:3 S3, X:5 S3, appA:4e, appB:2a: endings moved off pronouns and qualifiers (see Re-draft).
- appA:7 tense: "What the edit changed was" → "What the edit changes is".

### R8 integrity

- No claim, number, citation, quotation, or cross-reference changed. Claim-strength words kept where flagged: "important" (X:7), "Reliability comes from governing that specialization" (X:8), "The neighboring reward literature also" (X:4), "the gate's margin" (appA:3), "inherit its descent guarantee" and "the correct analogue" (appB:2), "the gate checks that future behavior improves" (appA:9), "so high-frequency or high-severity modes are proposed first" (appA:2).

### R9 punctuation

- appA:4: three colon reveals reduced to one ((A3) definition colon and "(A3) is strong:" kept as definitional; "The finite sum carries the content:" and "is gate-stable:" removed).
- appB:2: colon reveal in S6 replaced by a period.
- appA:6-9 label form unified to "Class ..." ("Signal class C1 or C2." → "Class C1 or C2."; ", class C3." → ". Class C3.").
- appA:3: registry term "observable outcome" → "observed outcome" (allowed substitution).
- No em-dashes; American spelling with "analogue" kept.

## 2. Interpretations and supplied doers

| ¶ | type | entry |
|---|---|---|
| X:3 | interpretation | "show its coverage limits" → "show the limits of the checks' coverage": "its" resolved to the receiving-side checks (sense), not Evo2Team (grammar). |
| X:3 | interpretation | "remains an architectural problem" → "remains the architectural problem taken up last": identifies it with problem 5 (X:6). |
| X:5 | supplied doer | "immediate per-edit acceptance is unavailable" → "no gate can accept each edit as it is made" (doer: the gate). |
| X:6 | supplied doer | "Their integration" → "A system that integrates them"; "the design" → "such a system". |
| appA:1 | supplied doer | "No new theorem is claimed" → "We claim no new theorem" (the authors). |
| appA:3 | interpretation | "near zero for the check itself in C1, with the sampling error of a finite suite over the patch remaining" → "near zero for an exact check (C1), though the sampling error of a finite suite over the patch remains" (C1 named by its registry term; "the check itself" folded into the contrast with the suite's sampling error). |
| appA:4 | interpretation | "a conditional statement under strong assumptions" → "It holds under strong assumptions". |
| appA:5 | interpretation | "at the head of this appendix" states where Table A-1 sits in the source; see AUTHOR FLAG 15. |
| appB:2 | interpretation | "That is the structural content of Section REF(sec:signal)" folded forward into "Read down the signal-class column for the structural content of Section REF(sec:signal)": "That" read as the narrowing by signal class shown in the column. |
| appA:4 / appA:5 | interpretation | appA:4's "which needs attribution far more reliable than success with non-zero probability per failure" deleted as a repeat of appA:5's "much stronger than the credit-assignment condition of Section REF(sec:loop), success with non-zero probability per failure" (no citation or number in the deleted clause). |

## 3. Ledger FLAGs deliberately left (with reason)

- X:1 (1.5, plan): the plan asks for "one per decision of the loop", but the heads are tasks across three axes (local step, promotion, signal class, architecture), and the ledger notes they do not map one-to-one. Writing "one per decision" would add a claim; the opening keeps the original's "decision a deployment must make" frame with the count added.
- X section 1.7 (order of the five problems) and 1.8 (heading as label): headings and bold leads are frozen invariants; reordering the problems was not done (D6, D2).
- X section 2.3 vocabulary drift ("reversal"/"rollback"/"withdrawn"/"reversed"; "provenance"/"versioned lineage"): left, because the words name different components in §VIII (provenance of pools vs lineage of versions) and changing them risks changing the stated architecture (AUTHOR FLAG 12).
- X:3 4.15 "unseen graphs", "receiving-client gate": glossing "graphs" as team graphs would import §VI content; left.
- X:4 S3 ending on the RLPR exception: kept attached to the claim it qualifies; moving it before the claim would read it as a plain exception, which may change the claim (AUTHOR FLAG 2).
- X:4 4.15 "human-gold references", "co-evolving", "RLPR": terms of the cited work; glossing would add content.
- X:5 4.5 "should therefore be assessed": agentless; no doer is near-certain (benchmark authors, reviewers, or the field), so none supplied.
- X:6 2.5 "evaluate the recipient" (repeats X:3): kept, because it is one of the integration's stated requirements; deleting it would change the requirement list.
- X:7 4.1/4.3 "The survey's central observation is that": kept; it marks the restated point and matches the plan's own wording ("the central observation"). 5.1 "important": AUTHOR FLAG 11.
- X:8 2.5, 3.1, 3.2, 4.1, 4.3, 5.3, AI-sweep (S1-S3): frozen by decision D12 (AUTHOR FLAG 1). Only S4 was re-drafted.
- appA:1 3.6 (S1 ends on "four worked cases"): the roadmap follows the subsection order; reordering it to end on the organizing concept would misstate the order. 5.1 "ordinary target": the precise replacement ("standard result") needs the author's agreement.
- appA:1 1.5 (Table A-1 placed before Setup): table lines are invariant and the task keeps the table in place; the appA:5 pointer now says where it is.
- appA:2 4.15 (⊕ and "mode" undefined): defining them would add content.
- appA:3 3.7 "the gate's margin": AUTHOR FLAG 3.
- appA:4 4.15 ("effective compactness of the reachable orbit", "admissible edit", "non-gate-stable"): formal terms in a formal statement; not glossed.
- appA:4 (A3)-strength restatement close call (S6 vs §II "gate stability, not global optimality"): the formal restatement is kept as the appendix's own scope statement.
- appA:4 "or $\widehat{\Delta}$ may be biased to reject it": ends on a pronoun with a single clear referent ("the improving edit"); left.
- appA:9 5.3: AUTHOR FLAG 9.
- appB:1 4.1/4.2 "Section REF(sec:loop) collapses": cross-reference as subject left, since "the formalism of Section ..." adds words without a clearer actor and the authors' "we" would claim the collapse as the survey's act; reader effect is small.
- appB:2 5.3 "inherit its descent guarantee", "the correct analogue": AUTHOR FLAG 5.
- appB Table B-1 cell issues: AUTHOR FLAGS 6, 7 (table lines are invariant).
- appA worked-case order (1.7): the cases are in substrate order; reordering by class is a structural choice for the author.

## 4. AUTHOR FLAGS

1. **X:8 S1-S3** (= plan AUTHOR FLAG X-1, D12). "Reliability comes from governing that specialization" restates §IX-A without its "On that hypothesis" condition. Kept verbatim; the author decides.
2. **X:4 S3.** "The neighboring reward literature also reports no human-agreement result for a co-evolving rubric or judge" (reworded from "also lacks a reported human-agreement result", same claim) widens §VII-A's "Among the co-evolving methods reviewed" to a whole literature. Scope words kept.
3. **appA:3.** "the gate's margin" names $\gamma_t + \tau_t$, while §II defines the margin as $\tau_t$. Kept.
4. **appA:2.** "so high-frequency or high-severity modes are proposed first": an assumption about $Q_t$ stated as a consequence, and "or" does not match ranking by the product $f_m s_m$. Kept.
5. **appB:2.** "inherit its descent guarantee" (Appendix A gives a one-step inequality and says nothing in the survey depends on the convergence statement) and "the correct analogue" (unhedged). Kept.
6. **Table B-1, Multi-sample agreement row.** "false-accept rate decays as $p^k$ rather than variance as $1/k$" holds for independent errors under an all-must-pass rule; SkillOpt-Lite's consensus filter may be a majority rule.
7. **Table B-1, Surrogate verifier row.** Voyager coded C2 inside a C1 family; DGM's "score weights selection, not retention" in a "Per-edit gate" row.
8. **appA:7.** "the reflexive gate of Section REF(sec:signal)": §II and §V send the reader to Section REF(sec:reflexive) for its development.
9. **appA:9.** "the gate checks that future behavior improves": a gate decides at acceptance and cannot observe future behavior.
10. **appA:2.** "the six substrate coordinates of Section REF(sec:method)" fuses §III's substrates with §II's finer "coordinate".
11. **X:7.** "have become an important form of adaptation": the survey counts systems and does not measure importance.
12. **X:6.** The conclusion lists four components; §VIII lists five and the abstract lists five. Not aligned (a stated finding).
13. **X section vs plan.** The plan's Section X point sentence includes "feedback explains much of the pattern" in the central observation; X:7 does not say it. Not added (it would add a claim to the conclusion). The author may want it restated there.
14. **X:1.** The plan's "one per decision of the loop" is not written in (see section 3); the author may confirm the mapping or rephrase the heads (heads are invariant here).
15. **appA:5.** "at the head of this appendix" assumes Table A-1 renders near the appendix opening in the IEEE build; if the float drifts, drop the phrase. Check in the build render.
16. **X:3.** "remains the architectural problem taken up last" ties X:3's governance link to problem 5; confirm that the author intends the two to be the same problem.

## 5. Word counts (wc -w, including citation keys and inline math)

| file | before | after | change |
|---|---|---|---|
| X_open_problems_conclusion.md | 476 | 480 | +4 |
| appA_formal.md | 1223 | 1225 | +2 |
| appB_gates.md | 576 | 562 | -14 |
| group total | 2275 | 2267 | -8 (-0.4%) |

X and appA grow slightly because the appA:4 split adds labeled assumption sentences and appA:5 gains the table location and one link sentence; appB's cuts more than offset them. The group total does not grow.

## 6. Invariant result

`cg_invariants.py cg_pre cg_work`: no FAIL or WARN lines name `X_open_problems_conclusion.md`, `appA_formal.md`, or `appB_gates.md` (citation keys, numbers, REF tokens, headings, table lines, caption lines, raw LaTeX, display equations, bold terms all identical; no em-dash; no British spelling). The script's overall status reads FAIL because of lines for other groups' files, which are being edited in parallel.
