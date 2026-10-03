# Evidence cards for Supplementary S7 (extended related work)

One card per neighbour named in S7. Every factual statement in S7 traces to a card. Verification sources are the arXiv abs/HTML pages or vendor documents fetched during the October-2026 sweeps (`scratchpad/m1_*.md`, 2026-10-03) or fetched directly on 2026-10-03 for this section. "Hinge" is the condition that differs in this survey's setting, stated neutrally.

## Commitment 1 — the unit of classification is a closed feedback loop over a persisted artifact (not the mechanism edited)

### gao2026selfevolving — Gao et al., "A Survey of Self-Evolving Agents", TMLR (Jan 2026), arXiv:2507.21046
- Setting: self-evolving agents; organizing axes what / when / how / where to evolve.
- Loop treatment: timing axis (intra- vs inter-test-time), not loop closure; "human in the loop" mentioned as a design option for validating a new tool.
- Governance: none.
- Hinge: classifies by what is evolved and when; this survey classifies by whether a gated loop closes and whether a second loop promotes.
- Verification: sweep C, PART 2 (abs + HTML).

### fang2025comprehensive — Fang et al., "A Comprehensive Survey of Self-Evolving AI Agents", arXiv:2508.07407 (Aug 2025)
- Setting: unified framework (system inputs, agent system, environment, optimizers); single-agent, multi-agent, domain-specific.
- Loop treatment: optimizer loop implicit; no gate-type or governance axis.
- Hinge: same as above.
- Verification: sweep C, PART 2.

### zhou2026selfevolvingcoding — Zhou et al., "Self-Evolving Coding Agents", arXiv:2608.03392 (Aug 2026), 108 methods
- Setting: coding agents; taxonomy by evolution target (framework, memory, skills, tools, workflow, environment), timing, code-specific signals.
- Loop treatment: formal admission rule Admit(k) = [delta > eps][Check = 1] (closest to a gate); "human feedback or approval can accompany system-generated updates"; notes "a passing test checks only selected behavior".
- Governance: library drift, outcome-based retirement, contaminated descendants; no cross-tenant dimension.
- Hinge: single domain (code, i.e., C1 signals); this survey spans substrates and signal classes and audits governance.
- Verification: sweep C, PART 2.

### ding2026alwayson — Ding et al., "Always-On Agents", arXiv:2606.30306 (Jun 2026), 435 works coded
- Six diagnostic dimensions per state item: authority, scope, mutability, provenance, recoverability, actionability; lifecycle write ... audit, rollback.
- Finding (quoted): literature "concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it".
- Hinge: governance of state items, not of an optimization loop; no gate-type or signal axis; no cross-organization promotion dimension.
- Verification: sweep C, PART 2; abs fetched 2026-09-20.

### lin2026memorysecurity — Lin et al., "A Survey on Long-Term Memory Security in LLM Agents", arXiv:2604.16548, EMNLP 2026, ~90 works
- Six lifecycle phases × four security objectives; five VMG primitives (write authorization, provenance visibility, principal-scoped retrieval, rollbackability, verified forgetting).
- Hinge: security of memory; carries a governance axis with principal scoping and rollbackability, but no loop-closure, gate-type, or signal axis and no promotion dimension.
- Verification: sweep C, PART 2.

### guo2026harness — Guo et al., "From Question Answering to Task Completion: A Survey on Agent System and Harness Design", arXiv:2606.20683 (Jun 2026)
- Model–harness lens; six runtime responsibilities (observation, context, control, action, state, verification); paradigm progression prompt -> workflow -> context -> harness engineering -> agent-native training.
- Quoted: "the harness itself is becoming learnable"; mechanical feedback in software ("builds, unit tests, linters, and execution logs") noted as a signal other domains lack.
- Hinge: design of the harness; loop closure and signal verifiability are discussed, not classification axes; no tenancy.
- Verification: sweep C, PART 2.

### xia2026harnessing — Xia et al., "Harnessing Agent Skills: Architectural Patterns and a Reference Architecture", arXiv:2606.20631 (May 2026), 8 systems
- Four responsibility layers (Supply Chain, Mediation, Execution Control, Evidence & Feedback); ten patterns; "Candidate changes are proposed and validated rather than directly mutating active or shared skills"; collective evolution rated "research-informed", not practitioner-standard.
- Hinge: reference architecture for one substrate (skills); no scoring across systems, no gate-type or signal classification.
- Verification: sweep A (v) and sweep C, PART 2.

### ding2026skilleval — Ding et al., "Agent Skill Evaluation and Evolution: Frameworks and Benchmarks", arXiv:2606.11435 (Jun 2026)
- Four evolution paradigms × six benchmark categories; open directions: reputation systems, permission boundaries, user confirmation, "explicit versioning and dependency graphs".
- Hinge: evaluation and evolution treated "as sequential, decoupled stages"; no loop-closure or governance audit.
- Verification: sweep C, PART 2.

### mei2025context — Mei et al., "A Survey of Context Engineering for LLMs", arXiv:2507.13334 (Jul 2025), 1,411 papers
- Components (retrieval/generation, processing, management) × system implementations (RAG, memory, tool-integrated reasoning, multi-agent).
- Hinge: no loop, gate, signal, or governance axis.
- Verification: sweep C, PART 2.

### ren2026selfimprovementsurvey — Ren et al., "Self-Improvements in Modern Agentic Systems", arXiv:2607.13104 (Jul 2026)
- Agent = foundation model × operational scaffold; self-improvement as a "self-induced update operator"; organized by update target and driving signal; notes weak credit assignment and benchmark-overfitting threats.
- Hinge: closest framing to this survey's decomposition; organizes by target and signal, not by loop closure, gate type, or governance.
- Verification: sweep B (vii).

## Commitment 2 — the gate is classified as algorithmic, human, or absent on each of two loops

### Prompt-optimization lineage (contrast corpus; optimizer state, no persisted deployment artifact distinct from the optimizer)
- **yang2023opro** — "Large Language Models as Optimizers" (OPRO), Yang, Wang, Lu, Liu, Le, Zhou, Chen; arXiv:2309.03409; ICLR 2024. Optimizes "instructions that maximize the task accuracy" by having the LLM generate new candidates from a prompt containing previous solutions and their scores; improvements "up to 8% on GSM8K, and by up to 50% on Big-Bench Hard tasks" over human-designed prompts. Verified from abs page 2026-10-03.
- **guo2023evoprompt** — "EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers", Guo, Wang, Guo, Li, Song, Tan, Liu, Bian, Yang; arXiv:2309.08532; ICLR 2024. Evaluated on 31 datasets; "up to 25% on BBH" over human-engineered and prior automatic prompts; population improved "based on the development set". Verified from abs page 2026-10-03.
- **fernando2023promptbreeder** — "Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution", Fernando, Banarse, Michalewski, Osindero, Rocktäschel; arXiv:2309.16797 (Sep 2023). Evolves task-prompts and mutation-prompts; evaluated on arithmetic and commonsense reasoning benchmarks and hate-speech classification. No statement about persisting or promoting prompts across deployments. Verified from abs page 2026-10-03.
- **khattab2023dspy** — "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines", Khattab, Singhvi, Maheshwari, Zhang, Santhanam, Vardhamanan, Haq, Sharma, Joshi, Moazam, Miller, Zaharia, Potts; arXiv:2310.03714 (Oct 2023). Compiles "LM pipelines as text transformation graphs"; a compiler "optimize[s] any DSPy pipeline to maximize a given metric" and modules "learn (by creating and collecting demonstrations)". The abs page does not address persistence of optimized prompts as deployment artifacts. Verified from abs page 2026-10-03.
- **yuksekgonul2024textgrad** — TextGrad; in corpus bib; backpropagates textual feedback through variables in a compound system; no artifact distinct from optimizer state (per the May audit, S4).
- Hinge for the whole lineage: each optimizes a prompt or program against a development set once; the artifact is the optimizer's output, not a persisted, versioned deployment object that is edited from session signal and promoted under a second gate. They sit in the contrast corpus (score < 3) or at the Loop-1-only boundary.

### Classic single-loop agents (in corpus, S4 of the supplementary)
- **shinn2023reflexion** (NeurIPS 2023), **wang2023voyager** (2023), **madaan2023selfrefine** (2023), **yao2023react** (2023): verbal reinforcement, skill libraries, and in-context self-correction; Reflexion and Voyager persist artifacts and close Loop 1; Self-Refine and ReAct do not persist. Verified in the May audit (arXiv short, Appendix D).
- Hinge: Loop 2 absent in all four.

## Commitment 3 — the feedback signal is classified by verifiability (exact / outcome / judged / delayed)

- **Rubric-reward line** (14 papers; cards in `scratchpad/m1_memory_surveys_rubrics.md`, PART 3, each verified from abs/HTML): gunjal2025rubrics (fixed rubric, fixed judge; pairwise accuracy vs expert-preferred responses read from a plot), jia2025writingzero (GenRM fixed during policy RL), yu2025rlpr (scorer co-evolves by construction; ROC-AUC 0.95 math / 0.82 general vs human annotations), xu2026rubricarm (rubric generator and judge co-trained, then frozen for policy training), shi2026references (RefEval 79.1% agreement with human annotations), bhattarai2026rubricgrounded (frozen judge; "no human-agreement" measurement stated), ding2026evorubrics (adversarial co-evolution; no human number), zhu2026score (shared actor as solver and evaluator; no human number), li2026rubricem (rubric buffer; no human number), jin2026rlaes (QWK 0.803 vs single human rater 0.805), jia2026openrubric (meta-rubric fixed; 82.3–93.0% agreement), lv2026queryrubrics (65.68% vs 71.4% human ceiling), plesner2026cheapverifier (calibrated against LLM golden judges, not humans), chen2026rubricsurvey (survey).
- Hinge: weight-side; the survey borrows the gate constructions and the fixed-vs-co-evolved distinction, and does not score these methods.
- **guo2026harness** notes mechanical feedback as a software-specific advantage (see above); **zhou2026selfevolvingcoding** notes a passing test is "incomplete feedback". Neither makes verifiability a classification axis.

## Commitment 4 — a four-property governance audit (auto-gated Loop 1; cross-organization promotion; versioned lineage with access control; rollback)

### nie2026evolvenet — EvolveNet, arXiv:2608.04968 (Aug 2026)
- Federated broadcast / client-local optimization / server-side merge; merge accepted iff |Fixed| ≥ |Broken| on a server-side held-out slice; "If the revised candidate also fails, the round rolls back to h^(t)"; "Rollback always targets the previous shared harness".
- Clients described as "data-local agent deployments" across "users, organizations, databases, repositories"; evaluation uses benchmark partitions as clients; no RBAC, no version IDs, no receiving-side re-validation; authors note "a program edit can itself encode client information".
- Hinge: (b) framed, not demonstrated across organizations; (d) partial; (c) absent.
- Verification: sweeps A (i) and B (i), HTML.

### yang2026federatedskill — FederatedSkill, arXiv:2606.03143 (Jun 2026)
- Clients = agent instances with (backbone, harness) profiles; semantic skill diffs as the unit of communication; server-side evolution agent applies/adapts/rejects per client with an "auditable decision log" recording source patch, reward, justification; up to +44.4% success over isolated self-evolution across 20 task families.
- Hinge: clients under one operator; acceptance from the source client's reward, not a held-out evaluation at the receiver; no RBAC, no rollback.
- Verification: HTML fetched 2026-09-20.

### kang2026registry (EDDOps), quessadavial2026acm (ACM), qin2026governed (Governed Capability Evolution)
- EDDOps: DRAFT -> APPROVED by auto eval gates (faithfulness ≥ 0.80, correctness ≥ 0.90) then human sign-off; supersedes/superseded_by lineage; emergency rollback PUBLISHED -> DRAFT; "does not address Role-Based Access Control". ACM: immutable revisions and baselines enabling rollback; RBAC "absent". GCE: seven-stage pipeline with gated activation, monitoring, rollback; 72.4% rollback recovery under drift. All three have Loop 1 = None.
- Hinge: governance without an inner loop from session signal.
- Verification: sweep C, PART 1.

### agenticcommunity2026mcpgateway, microsoft2026apicentermcp, truefoundry2026mcpgateway, mcp2026registry
- MCP control planes: OIDC-scope RBAC, fail-closed scan admission, quarantine (agentic-community gateway); version lifecycle and access management (Azure API Center); collaborator RBAC and tool-call approval (TrueFoundry docs; versioning/rollback claimed on a blog, not shown in docs); official registry: no scanning, no private servers, status preview.
- Hinge: admission and access governance with no evaluation-gated promotion; [Human × Human].
- Verification: sweep B (i), vendor docs dated 2026.

### letta2026memfs — Letta MemFS / Context Repositories (vendor docs, blog 2026-02-12, changelog 0.27.21–0.33.2)
- Git-backed memory, every edit committed; shared memory across cloud agents auto-pushed; optional agent-side review "doesn't require user approval"; rollback only via git history.
- Hinge: lineage without a gate; agent-side, not human, review.
- Verification: sweep C, PART 1.

### mcmahan2017fedavg, mcmahan2018dpfedavg — FedAvg (AISTATS 2017), DP-FedAvg (ICLR 2018)
- Parameter-space averaging of client updates with (DP-FedAvg) user-level differential privacy.
- Hinge: averaging of comparable numeric updates; scaffold promotion is selection and merge over symbolic artifacts.
- Verification: proceedings/dblp pages, 2026-09-20.

## Cards added 2026-10-03 (reviewer-pass "missing citations" sweep)

Metadata for every entry below was verified from the arXiv abstract page or the publisher page by a verification pass on 2026-10-03; mechanism statements come from the abstract or the method section as noted. None of these cards carries a number into the paper.

### zhou2024symbolic — Agent Symbolic Learning, arXiv:2406.18532 (Jun 2024)
- Treats prompts, tools, and the pipeline that connects them as symbolic parameters; updates them with "textual loss", "textual gradient", and symbolic optimizers in a back-propagation analogue, within one agent.
- Hinge: one deployment, benchmark score as the only gate, no promotion, no artifact governance. Closest precedent for optimizing the scaffold as a whole.
- Verification: arXiv abs + HTML, 2026-10-03.

### zelikman2023stop — STOP, COLM 2024, arXiv:2310.02304
- A scaffolding program improves itself: the seed improver calls a language model to rewrite the improver, and the improved improver is kept when its utility rises; evaluated on algorithmic tasks.
- Hinge: single program, single utility, no persistence beyond the run.
- Verification: arXiv abs; venue from OpenReview/COLM listing, 2026-10-03.

### robeyns2025sica — Self-Improving Coding Agent, arXiv:2504.15228 (Apr 2025)
- The agent edits its own harness (tools, scaffolding code) with the same coding tools it uses for tasks, and keeps the edit when the benchmark score rises.
- Hinge: one deployment, benchmark gate, no promotion or governance.
- Verification: arXiv abs, 2026-10-03.

### suzgun2025cheatsheet — Dynamic Cheatsheet, arXiv:2504.07952 (Apr 2025)
- A persistent, evolving memory for a black-box language model at test time; the model curates reusable strategies and code snippets across problems.
- Hinge: Loop 1 persists the artifact; no second loop. Sits with the agent-memory line in S7.2.
- Verification: arXiv abs, 2026-10-03.

### shankar2024validators — EvalGen / "Who Validates the Validators?", arXiv:2404.12272 (Apr 2024)
- Assisted generation of evaluation criteria and assertions for LLM outputs, aligned to human grades; reports "criteria drift": graders revise their own criteria as they grade more outputs.
- Hinge: measured on human evaluators of model outputs, not on a judge under scaffold edit. Used in IV (C3) and XI (problem 3) as the nearest measurement of a moving gate.
- Verification: arXiv abs + HTML (criteria-drift finding in the abstract), 2026-10-03.

### gao2023overoptimization — Reward-model overoptimization, arXiv:2210.10760 (Oct 2022)
- Scaling laws for the gap between a proxy reward model and a gold reward model under best-of-n and RL optimization; the gold score peaks and then falls as optimization continues.
- Hinge: weight-side proxy reward; the paper uses it as the measured form of Goodhart for C3 gates (IV, X).
- Verification: arXiv abs, 2026-10-03.

### zheng2023judge — LLM-as-a-Judge / MT-Bench, NeurIPS 2023 D&B, arXiv:2306.05685
- Introduces MT-Bench and Chatbot Arena; measures agreement between strong LLM judges and human preference and catalogues judge biases (position, verbosity, self-enhancement).
- Hinge: the judge is a fixed evaluator of fixed outputs; the paper cites it only as the vocabulary for the Auto gate's "language-model judge" (III).
- Verification: arXiv abs; venue from NeurIPS proceedings, 2026-10-03.

### hu2021lora — LoRA, arXiv:2106.09685 (Jun 2021)
- Low-rank adapter matrices trained with frozen base weights; the per-tenant adapter cited in II-A as the weight-side alternative to scaffold adaptation.
- Verification: arXiv abs, 2026-10-03.

### greshake2023injection, debenedetti2024agentdojo, chen2024agentpoison, wallace2024hierarchy — injection and poisoning (Table X-1)
- Greshake et al. (arXiv:2302.12173): indirect prompt injection through retrieved or tool-returned content in LLM-integrated applications. AgentDojo (arXiv:2406.13352): a dynamic evaluation environment for prompt-injection attacks and defenses on tool-using agents. AgentPoison (arXiv:2407.12784): backdoors planted in an agent's long-term memory or RAG knowledge base. Instruction Hierarchy (arXiv:2404.13208): training models to prioritize privileged (system) instructions over lower-privilege inputs.
- Hinge: all four are attacks on or defenses for a fixed scaffold; the paper cites them as the measured attack surface that gated promotion must also pass through.
- Verification: arXiv abs for each, 2026-10-03.

### kairouz2021federated, guo2022promptfl — federated learning survey; PromptFL (IX, S7.4)
- Kairouz et al. (arXiv:1912.04977; Foundations and Trends in ML 2021): the field's reference catalogue of open problems. PromptFL (arXiv:2208.11625; note: 2208.12268 is the different paper FedPrompt): participants cooperatively learn a shared prompt rather than shared weights.
- Hinge: PromptFL is the weight-side precedent closest to the "mergeable update" limit where the FedAvg analogy holds; the artifact is still a numeric soft prompt, averaged, not a symbolic artifact selected and merged.
- Verification: arXiv abs for both; publisher page for Kairouz returned 403, year kept as arXiv 2019 with the journal in the note, 2026-10-03.

### packer2023memgpt, zhao2024expel, wang2024awm, xu2025amem — agent-memory line (S7.2)
- MemGPT (arXiv:2310.08560): virtual context management that pages information between a bounded context and external storage. ExpeL (AAAI-24, arXiv:2308.10144): extracts insights and an experience bank from training tasks and reuses them at inference. Agent Workflow Memory (arXiv:2409.07429): induces reusable workflows from past trajectories and injects them into memory. A-MEM (NeurIPS 2025, arXiv:2502.12110): Zettelkasten-style memory with linked, evolving notes.
- Hinge: each persists the artifact inside one agent (Loop 1); none promotes it beyond the agent that wrote it.
- Verification: arXiv abs for each; venues from AAAI and NeurIPS listings, 2026-10-03.

### zhou2022ape, pryzant2023protegi, opsahlong2024miprov2, cheng2024trace — prompt and program optimization (S7.2)
- APE (arXiv:2211.01910): LLM-generated instruction candidates selected by a score. ProTeGi (EMNLP 2023, arXiv:2305.03495): natural-language "gradients" from minibatch errors, edits searched by beam search. MIPRO (EMNLP 2024, arXiv:2406.11695): joint instruction and demonstration optimization for multi-stage programs under a stochastic mini-batch surrogate. Trace / OPTO (arXiv:2406.16218): the optimizer receives the execution trace and the feedback and proposes updates to any traced parameter.
- Hinge: one optimization run against a fixed task distribution; the output is a prompt or program, not a versioned deployment artifact under a second gate.
- Verification: arXiv abs for each; venues from ACL Anthology, 2026-10-03.

### zhang2024aflow, zhuge2024gptswarm — workflow search (VI S5, S7.2)
- AFlow (arXiv:2410.10762): Monte Carlo tree search over workflows represented as code. GPTSwarm (ICML 2024, arXiv:2402.16823; printed title "Language Agents as Optimizable Graphs"): agents as computational graphs with node-level and edge-level optimization.
- Hinge: topology is the optimized object, under a benchmark score, within one run; cited as the precedent for the corpus's S5 topology evolution.
- Verification: arXiv abs; ICML listing for GPTSwarm, 2026-10-03.

### romeraparedes2024funsearch, lu2024aiscientist — FunSearch (Nature 625, 2024); AI Scientist (arXiv:2408.06292)
- FunSearch: an evolutionary procedure pairing a pretrained LLM that proposes programs with a systematic evaluator; AlphaEvolve's predecessor. AI Scientist: a pipeline that generates ideas, runs experiments, writes the paper, and reviews it.
- Hinge: FunSearch is a C1/C4 archive system without promotion; AI Scientist is the paper's example of a C4 signal (research output judged long after the edit).
- Verification: Nature DOI 10.1038/s41586-023-06924-6; arXiv abs, 2026-10-03.

### sculley2015debt, zaharia2024compound — framing citations (X, II-A)
- Sculley et al. (NIPS 2015): technical debt specific to machine-learning systems (entanglement, hidden feedback loops, configuration debt). Zaharia et al. (BAIR blog, 18 Feb 2024): state-of-the-art results increasingly come from compound systems with several components rather than a single model.
- Hinge: used as framing only; the paper's claim is that scaffold maintenance adds its own entries to the debt ledger and that the scaffold is the non-model part of a compound system.
- Verification: NeurIPS proceedings page; BAIR blog page, 2026-10-03.

### braintrust2026docs, vellum2026docs, langsmith2026hub — prompts-as-code platforms (VI governance-first)
- Braintrust: prompts pinned to a version or resolved by environment. Vellum: per-environment release tags and release history. LangSmith: a commit hash per prompt save with staging and production tags.
- Hinge: immutable versions with evaluation thresholds and rollback; no Loop 1, because candidates are authored by engineers. These are the three systems the maturity table names as S6 score-5.
- Verification: vendor documentation pages, accessed 2026-10-03.
