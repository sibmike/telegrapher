---
title: "Frontier and Localhost: How Production AI Learns Outside the Weights (Short Version)"
author:
  - Mikhail L. Arbuzov
  - Alexey A. Shvets
  - Sisong Bei
date: ""
header-includes:
  - \usepackage{xurl}
---

**Abstract**

Reliability in production LLM systems has migrated out of the weights. Across approximately 130 production and research systems surveyed between January 2023 and May 2026, practitioners repeatedly wrap frozen frontier models in a *localhost scaffold* of instructions, skills, memories, tools, orchestration graphs, and governance pipelines that updates from deployment feedback on a cadence the weights cannot match. We argue this scaffold is doing learning in a precise sense — discrete, gated, patch-local stochastic descent over a structured artifact space — and we identify the architecture's two-loop structure (local update; cross-context promotion under a gate) as the recurring design. Thirteen research systems plus two industry exemplars satisfy a strict composite-two-loop criterion; placing them on a 3×3 matrix of gate types leaves three populated cells and three empty cells. The consequential empty cell is enterprise full-auto: automated local evolution combined with governed cross-tenant promotion, versioned lineage with RBAC, and rollback — in ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer. This short version states the argument and its supporting tables; full formalism, per-system evidence, cluster walks, cell-by-cell matrix discussion, and the audit trail live in Appendices E and F and in the supplementary bundle.

---

## 1. The gradient moved outside the model

The standard mental model of an LLM system is the model: pre-training fixes the weights, fine-tuning nudges them, deployment wraps a thin prompt-plus-tool layer around the result and ships. Production in 2025–2026 has stopped behaving this way. Frontier models update on cycles measured in months; the systems built on top of them — markdown files, persistent memories, retrieved skills, registered tools, evaluation suites, agent topologies, version-controlled prompt repositories, PR-gated governance — update continuously. The fast learning is no longer in the weights. It is in a fast-changing *localhost* scaffold wrapped around a slow-changing frontier.

Once the framing is in place the field snaps together. A Claude Skill is a learned procedural weight kept outside the model. A Cursor Rule is a local parameter for one project's distribution shift. A RAG connector is patch-specific memory access. A tool registry is capability provisioning along an axis the base model cannot reach. A PR review against a shared rule repository is a promotion gate on a federated update. An eval suite that blocks merge is a validation-loss check before promotion. A cross-tenant artifact repository is federated-style artifact aggregation across distributed shards (scope expansion under a gate, not arithmetic averaging — we sharpen this in §3 and §9). The mechanisms were already there; only the name was missing.

This paper surveys approximately 130 production and research systems, identifies the six substrates where the scaffold lives, formalises the two-loop architecture (local update, cross-context promotion under a gate), and names an empty corner of the design space — automated local scaffold evolution combined with governed cross-organisation promotion, versioned lineage with RBAC, and rollback — as the most consequential open architecture problem. The compression of v2 of this paper into a short body plus extended appendices is the present document; the long version lives at `paper_frontier_and_localhost.{md,pdf}` in the same arXiv bundle.

## 2. Why patch errors live outside the weights

The scaffold is not merely where production systems happen to store patches. Under the constraints production imposes — high update cadence, per-tenant specificity, inspectability, reversibility — it is the *dominant practical substrate* for patch-specific adaptation, because the weight substrate fails several of those constraints at once.

**Frontier training optimises for breadth.** The weights are tuned for cross-patch generalisation: they smooth over local conventions, contradictory tenant preferences, and rare workflow-specific failures in order to preserve broad competence across millions of unseen deployments. The smoothing is the training objective, not an artefact: RLHF reduces output diversity and homogenises preferred styles across users (Kirk et al., 2024; Padmakumar & He, 2023), and instruction-tuning data composition rewards patterns that generalise across the annotator pool rather than patterns specific to any one deployment. The frontier model is therefore *trained to be unable* to encode a single tenant's idiosyncrasies as preferred behaviour.

**Production reliability is achieved in depth.** Inside a single deployment patch, reliability is determined by exactly what global training had to smooth away: local naming conventions, team-specific workflows, idiosyncratic tool chains, customer-specific risk tolerances, recurring local mistakes, hidden evaluator expectations. The per-patch quantities from our previous work (failure-mode catalogue size, hard-fraction, mode-discovery rate) are local by construction, and a library calibrated to one patch under-covers the next.

**Encoding every patch in the weights is structurally infeasible.** Three constraints rule out the obvious approach. *Economic:* millions of patches multiplied by billions of parameters times per-patch fine-tuning cost is not a viable training-compute budget. *Release-cycle:* the patch wants daily updates; weight releases ship quarterly at best. *Cross-patch interference:* overfitting the weights to one tenant's preferences degrades adjacent tenants whose preferences contradict.

Per-tenant fine-tunes, LoRA adapters, distilled small models, and learned routing each absorb some patch residuals in principle. The survey finds that in practice the scaffold dominates because it is the substrate that satisfies all four production constraints at once — cheap, inspectable, reversible, locally scoped, and updatable on a daily cadence rather than a release cadence. The placement question that *Architecture of Errors* left open — where do the interventions live? — has this as its answer: the frontier model generalises, the localhost scaffold specialises, and reliability comes from governing that specialisation.

## 3. Artifact-layer descent

Scaffold evolution is learning in a precise sense. A failure is observed, a candidate edit is proposed, a gate (an eval suite, an LLM-judge, an RL threshold, a reviewer's PR) estimates whether the edit reduces patch loss, accepted edits persist, and some of them are promoted up a scope hierarchy. Stated in optimisation language, this is discrete, gated, patch-local stochastic descent over a structured artifact space, with a noisy gate standing in for the gradient and a governance system standing in for the learning rate. The substrate happens to be discrete, symbolic, and human-readable rather than continuous and differentiable; the gate is mediated by humans, evals, or surrogate verifiers rather than computed by chain rule. The descent picture is mechanism when stated conditions hold and modeling language otherwise.

**Assumptions and scope of the formalization.** The descent argument below holds when: (i) the frontier model parameters $\theta_M$ are fixed during the adaptation window; (ii) scaffold edits are persistent, inspectable artifacts distinct from transient context; (iii) the patch admits a measurable operational loss; (iv) the proposal process can attribute failures to scaffold coordinates with non-zero probability; (v) gates are imperfect estimators of finite directional loss change rather than oracle access to the true loss change; (vi) Loop-2 promotion is scope expansion under a gate, not arithmetic averaging of comparable updates. Survey claims of the form "no surveyed system has X" are bounded by the audited public corpus and the survey cutoff of May 2026.

**Patch scope hierarchy.** *Patch* is used throughout this paper with a defined scope hierarchy: USER ⊂ PROJECT ⊂ STACK ⊂ TENANT ⊂ CORE. A USER patch is one human's account or fork; a PROJECT is one repository, workflow, or product workspace; a STACK is a curated bundle of projects under one team; a TENANT is an organisation or customer; CORE is the cross-tenant universal scope. Each level induces its own loss as an average over the patches it contains. When the text says "cross-tenant promotion" it specifically means moving artifacts up to the TENANT or CORE level; "patch-specific adaptation" without qualifier means descent on a USER or PROJECT-level loss.

The patch loss is the expected residual failure rate of the model–scaffold composite on patch $D$:

$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right],$$

where $\theta_s$ is a structured scaffold parameter object over six substrate coordinates and $\ell$ is an operational loss (failure indicator, user-correction rate, eval error, schema violation, reviewer disagreement). The important distinction is substrate: $\theta_M$ is fixed during deployment; $\theta_s$ is the object being fit.

A failure does not yield an analytic gradient; it yields a candidate edit. The gate $G_t$ accepts the edit if its noisy estimate of the directional loss change clears a margin. The accepted edit applies to the current scaffold; rejected edits leave the scaffold unchanged:

$$\theta_s^{t+1} = \begin{cases} \theta_s^t \oplus z_t, & G_t(z_t)=1, \\ \theta_s^t, & G_t(z_t)=0, \end{cases}$$

with the gate accept condition

$$G_t(z_t)=1 \iff \widehat{\Delta}_{z_t} L_D(\theta_s^t) + \lambda\,\Omega(z_t) \leq -\tau_t,$$

where $\widehat{\Delta}$ is the gate's estimator of the loss change, $\Omega \geq 0$ is a complexity penalty on the edit (instruction length, tool-permission breadth, promotion scope), $\lambda \geq 0$ regularises that penalty, and $\tau_t \geq 0$ is the required improvement margin. Production systems implement this without writing the equation: an eval blocks a merge on regression, a reviewer rejects a vague rule, a governance system prevents a local artifact from being shared until evidence accumulates. Different surveyed gate families instantiate the abstraction differently — eval-cascade, RL-threshold, LLM-judge, surrogate verifier, reviewer-judgment for the per-edit gate; semantic-merge and MAP-Elites archive selection as proposal-pruning steps that *precede* the per-edit gate. The per-system mapping is in Appendix C.

**Two loops follow naturally.** Loop 1 is within-context: a session feedback signal triggers an update to a persisted local artifact. Loop 2 is cross-context: a local artifact is promoted to a shared scope under explicit versioning. They map cleanly onto two distinct quantities in the optimisation analogy. *Edit magnitude* — how much a single accepted edit changes the local scaffold under $\oplus$ — plays the role of learning rate. *Promotion radius* — how many downstream patches the accepted edit affects — controls *which loss is being descended on*: USER-level acceptance descends on one patch's $L_D$; PROJECT promotion descends on an average over a project's patches; CORE or cross-tenant promotion descends on a federated average over many tenants' losses. Learning rate and radius are independently controllable, and the gate must be calibrated against both. Governance is not administrative overhead; it is the regularization system that prevents a small-magnitude edit from being descended on the wrong loss.

Each loop has a gate. Gates are **Auto-gated** when the decision is an operationalised algorithmic criterion (RL threshold, eval score, LLM-judge with quantified agreement, surrogate verifier, benchmark cascade), **Human-gated** when the decision is reviewer judgment, and **None** when the loop is absent. These five terms — Loop 1, Loop 2, Auto-gated, Human-gated, None — anchor §§5–9.

The descent argument is *mechanism* when five conditions hold: measurable patch loss, residual capture, failure-to-coordinate credit assignment, candidate delta synthesis, and a gate that estimates directional loss change before persistence or promotion. It is *metaphor* when those conditions are absent. Appendix E formalises the assumptions A1–A5 needed for a one-step descent inequality and a convergence proposition of the loss to a $G$-stable scaffold, and works through the RAG, pitch-review, tool-use, and memory cases that make the mechanism visible.

## 4. Six scaffold substrates

A patch-plastic scaffold composes six substrates. They are the coordinates of $\theta_s$, each independently editable.

| Substrate | What persists | Score-5 mark |
|---|---|---|
| **S1 — Instructions** | Project/team/org rules attached to a workspace | Versioned, two-loop, Auto-gated promotion |
| **S2 — Skills** | Procedural artifacts (code/text) loaded on demand | Skill bank self-modifies on failure, unit-test gated, versioned, promoted |
| **S3 — Memory** | Cross-session experience (episodic / semantic / procedural) | Provenance + versioning + correction pathways |
| **S4 — Tools** | Vetted action surface + context schemas | Domain-curated bundle is the product; eval-gated tool versions |
| **S5 — Orchestration** | Multi-role graph + routing | Population/policy updates from outer-loop signal |
| **S6 — Governance** | Versioning, promotion, audit, rollback | dev→staging→prod with eval thresholds + audit log + rollback |

The 0–5 rubric is uniform across substrates: **0** ephemeral; **1** persistent local; **2** persistent + tool attachment, no feedback; **3** multi-scope or feedback but no automated promotion; **4** automated feedback updates the scaffold (one loop closed); **5** two-loop versioned promotion plus governance (both loops closed). We adopt this six-coordinate decomposition because each coordinate is independently editable in production systems; alternative partitions (e.g., separating evals from governance) are possible, and the descent argument of §3 is invariant to the partition so long as the independent-editability property holds.

## 5. Survey method

The survey covers approximately 130 unique LLM systems published or productionised between January 2023 and May 2026 — approximately 90 satisfying the patch-plastic discriminator (score ≥ 3 on at least one substrate) and forming the **core corpus**, approximately 38 commonly described as agentic or self-improving but failing at least one discriminator and held aside as a **contrast corpus**. A separate, stricter audit applied to 22 candidate systems uses a *composite two-loop* criterion: Loop 1 modifies a persisted artifact from session signal *and* Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage. Thirteen research systems pass the strict audit, plus two industry exemplars (Sierra Agent OS 2.0, Cognition Devin) evaluated using vendor documentation as primary evidence and explicitly flagged in §8. Full inclusion/exclusion criteria, evidence-tier definitions (T1 peer-reviewed; T2 arXiv; T3 production claim; T4 open-source artifact; T5 industry blog), scoring discipline, sensitivity analysis under two natural relaxations of the criterion, and the per-system audit trail are in Appendix B, with the master CSV and per-substrate evidence harvests bundled under `supplementary/`.

## 6. Substrate maturity is uneven

Aggregating the survey by substrate gives a maturity gradient: tools and integrated systems are the most production-mature; skills and orchestration lag; instructions are ubiquitous but shallow; memory is widespread but rarely versioned. The unevenness is the survey's central empirical pattern. The field has independently converged on the six substrates, but no system matures all six at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation; vertical-bundle vendors solve patch specificity but rarely expose cross-tenant promotion. Per-substrate score distributions, score-5 exemplars, and the five surprising absences that fall out of the discriminator (failure-triggered memory rare in production; cross-customer skill promotion absent; memory versioning mostly unsolved; scaffold-level curriculum unspecified; Loop-2 overfitting detection missing) are in Appendix F. Each absence reappears as a Paper-4 target in §11.

## 7. Four clusters

Four archetypal clusters recur across the corpus. **Research full-auto** systems automate both loops under algorithmic gates (NanoResearch, SkillRL, AlphaEvolve, DGM, ADAS, Voyager) and demonstrate that the architecture works; enterprise governance is uniformly absent. **Production hybrid** systems pair an algorithmic Loop-1 gate with a reviewer-judgment Loop-2 gate (SkillForge, CASCADE, Sierra Agent OS 2.0, Cognition Devin) and represent the production-viable cell. **Governance-first** systems automate Loop 2 only — eval-gated CI blocks promotion on regression — but lack Loop 1 because the candidate artifacts are engineer-authored (Braintrust, Vellum, LangSmith Hub, W&B Weave, Agenta, LangFuse); we frame this as *MLOps for scaffolds*, distinct from MLOps for weights. **Open standards** systems converge across vendors on artifact format and tool attachment (AGENTS.md in over 60,000 GitHub repositories with measured efficiency gains; MCP as the cross-vendor tool standard; Claude Skills, Cursor Rules, Copilot custom instructions, Windsurf, Continue.dev, Zed, Replit on a common markdown-plus-tool pattern). Convergence across vendors is the strongest evidence the architecture is real rather than a single vendor's local optimum. Per-cluster system walks with metrics, the orchestration-bounding result of Tran & Kiela (2026), and the vertical-bundle vendor placement are in Appendix F.

## 8. The two-loop design space

The composite-two-loop systems sit in a 3×3 matrix indexed by gate type on each loop.

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillRL, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoAgent, AutoManual | SkillForge, CASCADE, Sierra OS 2.0†, Cognition Devin† | MAE\*, MetaGen\*, MetaReflection\*, CLIN\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in surveyed corpus]** | *(none)* |
| **Loop-1 None** | ExpeL (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repo\*, DSPy\*, TextGrad\* | Self-Refine\*, ReAct\*, Mem0\* |

*Asterisks fail at least one composite-two-loop criterion; included for contrast.* † Industry exemplar evaluated using vendor documentation as primary evidence.

Three cells are populated. **[Auto × Auto]** holds eleven research systems with machine-evaluated decision criteria on both loops. **[Auto × Human]** is the production-viable cell — Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. **[None × Auto]** holds the governance-first prompts-as-code systems with eval-gated CI but no failure-triggered candidate generation. Three cells are empty for distinct structural reasons: **[Human × Auto]** because if humans author candidates manually, automated promotion offers little leverage; **[Human × Human]** because no public system in the May 2026 survey window pairs reviewer-authored candidates with reviewer-gated promotion (a candidate occupant would be a solo or small-team workflow where the marginal cost of a bad auto-merge exceeds the marginal cost of human latency); **[Human × None]** because a system requiring human authorship on Loop 1 without any Loop 2 collapses to engineer-edits-a-config and is not patch-plastic in the sense of §3.

Two cross-cutting findings sharpen the picture. **Noise reduction via batching is largely absent in the surveyed auto-gated systems**: every auto-gated system fires at $n = 1$ per generation step, absorbing estimator noise statistically via the per-edit gate rather than aggregating evidence across multiple proposals. Multi-sample agreement filters (accept only when $k$ independent proposals converge) are a tractable design dimension that no surveyed system has formalised; their noise-reduction behaviour is qualitatively distinct from mini-batch averaging (false-accept rate shrinks roughly as $p^k$ rather than variance shrinking as $1/k$), and the two should not be conflated. **Multi-layer hierarchies are under-explored**: only AlphaEvolve demonstrates explicit depth in the auto-gated cluster (via cascade evaluator and MAP-Elites archive); the other twelve composite-two-loop systems treat their artifact pool as flat. The full cell-by-cell discussion, the closest-approaches enumeration that supports §9's empty-corner claim, and the DGM dual-mode footnote are in Appendix F.

## 9. The empty corner

Four properties define what we call **enterprise full-auto**:

- (a) **Auto-gated Loop 1** — the commit criterion is an algorithmic threshold.
- (b) **Multi-tenant cross-org promotion** — Loop 2 routes artifacts between organisations.
- (c) **Versioned lineage with RBAC** — promoted artifacts carry semantic versions, audit trails, and access-control policies.
- (d) **Rollback** — a bad promotion can be reverted without redeploy.

No surveyed system has all four. The closest approaches partition the requirements: AlphaEvolve has (a) and partial (b) within a single organisation; SkillForge has (a) and (b) within one enterprise with partial (c) via VFS commits; Sierra Agent OS 2.0 has (b) and partial (a); the governance-first cluster has (c) and (d) explicitly but no (a) or (b) in the strict sense. The full enumeration is in Appendix F. In ML terms, the empty corner is a *DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer*: per-tenant artifact pools with tenant-tagged provenance, aggregation across tenants with operator-tunable privacy bounds, an automated eval gate blocking promotion when patch loss does not decrease, versioned lineage with RBAC, and a rollback envelope on every promoted artifact. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. Whether the corner *should* be filled is deployment-dependent (in safety-critical domains, reviewer-judgment gates may be a design feature rather than a defect); the narrower survey claim — that no public system currently fills it — is what matters for the next two years of architecture work.

### 9.1 Patch-completeness as an operational hypothesis

The two-tier architecture also raises a measurable question about generality in production:

> A model–scaffold composite is *(r, n, d)-patch-complete* for a deployment patch $D$ when its residual error rate on a stationary patch eval suite of size $n$ stays at or below $r$ over a deployment window of $d$ days.

The definition makes patch-completeness an empirical property of a specific deployment and a specific eval rather than a philosophical claim about generality. We are not aware of any surveyed system that has formally demonstrated $(r, n, d)$-patch-completeness with held-out evaluation and a stationary patch over a non-trivial $d$. The framework predicts such demonstrations should appear in narrow production verticals — a coding agent confined to one repository with stable conventions, a legal agent confined to a stable due-diligence workflow — once eval discipline catches up with deployment scope. The governance question is then operational: at what residual rate $r$ and over what window $d$ is local competence load-bearing enough to require governance attention even before global robustness is established? §10 catalogues the failure surface that the answer must account for.

## 10. A new failure surface

Patch-plasticity introduces failure modes weight-only systems do not have. **Scaffold bloat** is the dominant near-term risk: IFScale (Jaroslawicz et al., 2025) reports latency growing roughly 35× for one reasoning model (o4-mini) as instruction count scales from 10 to 250, and the best frontier model in that benchmark (Gemini 2.5 Pro) drops to 68% accuracy at 500 instructions, with weaker models degrading further; the underlying mechanism (lost-in-the-middle, instruction interference; Liu et al., 2023) persists across model generations even when individual frontier-model scaling improves. **Poisoned memory** is the dominant security risk (PoisonedRAG reports 90%+ attack success rate against standard RAG; Memory Control Flow Attacks report >90% vulnerability across major LLM agent frameworks). **Prompt injection via tools and MCP** is the dominant cross-vendor attack surface (CVE-2025-54136 "MCPoison" demonstrated a public MCP-server compromise pathway). **Eval fragility** is the dominant ecosystem risk: the Leaderboard Illusion documents up to 112% relative performance gains under differential training-data access — eval suites are themselves patch-plastic artifacts and must survive Goodhart's Law. **Coordination failures** are documented in MAST (14 failure modes, $\kappa = 0.88$ agreement, dominantly role-confusion and context-loss). **Patch overfitting** is structural (scaffolds tuned to a deployment over-fit it). **Plasticity loss at the scaffold level** is the slow-moving risk: context rot, instruction conflict, memory pollution, tool-version drift produce a scaffold-level analogue of weight-level plasticity loss; no surveyed system treats pruning or expiration as a first-class operation. The patch-plastic surface is real, quantified by 2024–2026 work, and largely unmitigated in production.

## 11. Conclusion

The field did not wait for frontier weights to become perfectly reliable. It built a second learning system around them — made of markdown files, skills, memories, tools, orchestration graphs, eval suites, PRs, version histories, and rollback buttons. The mechanisms were already there; what changed in 2025–2026 is that the combination became dense enough across vendors that the convergence reads as architecture. Once you name it, the empty corners become concrete engineering targets, the most consequential being enterprise full-auto: Auto-gated Loop 1 plus governed multi-tenant cross-org Loop 2, with versioned lineage, RBAC, and rollback. In ML language, a DP-FedAvg-style cross-tenant aggregator with an automated eval gate at the scaffold layer. Whether the corner should be filled is deployment-dependent; that it has not been is the survey's headline finding.

Practical generality therefore arrives locally first: not as a universal mind, but as model–scaffold systems whose competence is fitted to bounded worlds and is in principle measurable through the $(r, n, d)$-patch-completeness condition of §9.1. The frontier model generalises. The localhost scaffold specialises. Reliability comes from governing that specialisation, and the most consequential open architecture problem is the one that combines automated local evolution with auditable cross-tenant aggregation.

---

## Appendix A. Representative survey rows

The full per-system spreadsheet is `supplementary/p3_master_scores.csv`. The 30 rows below are a representative spot-check covering all six substrates, both research and production, and all four clusters of §7. *Loop 1* and *Loop 2* columns apply to systems satisfying the composite-two-loop criterion; *n/a* means the loop is absent. *PP* is the integrated patch-plasticity score (0–5); *Evidence* abbreviates the strongest available source tier (T1 peer-reviewed; T2 arXiv; T3 production claim; T4 open-source artifact; T5 industry blog).

```{=latex}
\begingroup\small
```

| System | Year | Substrate | Loop 1 | Loop 2 | PP | Evidence | Why included |
|------------|---:|-----------|-------|-------|---:|------------------|------------------------------------|
| NanoResearch | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2605.10813) | Tri-level Skills/Memory/Policy co-evolution; cleanest full-auto exemplar |
| AutoAgent | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2603.09716) | Dual-cycle Execution+Evolution + elastic memory orchestration |
| SkillRL | 2026 | Integrated | Auto | Auto | 5 | T2 (arXiv:2602.08234) | Recursive skill-augmented RL with $\text{SR}<0.4$ threshold gate |
| AlphaEvolve | 2025 | Integrated | Auto | Auto | 4 | T2/T3 (arXiv:2506.13131) | Production proof-point: Borg +0.7%, Gemini kernel +23%, FlashAttention +32.5% |
| DGM | 2025 | Integrated | Auto | Auto | 4 | T2 (arXiv:2505.22954) | Recursive self-modifying code; SWE-bench 20%→50% |
| ADAS | 2024 | Integrated | Auto | Auto | 4 | T2 (arXiv:2408.08435) | Meta-agent search; Turing-complete agent representation |
| SkillForge | 2026 | Integrated | Auto | Human | 4 | T2 (arXiv:2604.08618) | Production hybrid exemplar; LLM-judge >90% + VFS versioning |
| CASCADE | 2025 | Integrated | Auto | Human | 4.5 | T2 (arXiv:2512.23880) | Largest within-benchmark ablation gain: +57.9 pp on SciSkillBench |
| EvolveR | 2025 | Integrated | Auto | Auto | 3 | T2 (arXiv:2510.16079) | Experience-driven lifecycle; accepted at ICML 2026 |
| Voyager | 2023 | Integrated | Auto | Auto | 4 | T2 (arXiv:2305.16291) | Foundational skill-library result; 3.3× items, 15.3× tech-tree milestones |
| AGENTS.md | 2025 | S1 Instructions | n/a | n/a | 2 | T3/T4 (agents.md) | Cross-vendor standard; 60k+ repos; Lulla 2026 measures −28.6% runtime |
| Claude Code CLAUDE.md | 2025 | S1 Instructions | n/a | n/a | 4 | T3/T4 (docs.anthropic.com) | Four scoping levels including org-IT policy + auto-memory layer; ceiling for S1 |
| Cursor Rules | 2024 | S1 Instructions | n/a | n/a | 3 | T3/T4 (\url{docs.cursor.com/rules}) | `.cursor/rules/*.mdc` multi-scope + MCP attach; git-tracked |
| Anthropic Agent Skills | 2025 | S2 Skills | n/a | Human | 3 | T3 (\url{anthropic.com/engineering}) | Progressive disclosure spec; LangChain replication 29%→95% pass-rate |
| SAGE | 2025 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2512.17102) | +8.9% SGC, 26% fewer steps, 59% fewer tokens on AppWorld |
| COSPLAY | 2026 | S2 Skills | Auto | Auto | 5 | T2 (arXiv:2604.20987) | Co-evolving decision agent + learnable skill bank; long-horizon tasks |
| Reflexion | 2023 | S3 Memory | Auto | n/a | 4 | T1 (NeurIPS 2023; arXiv:2303.11366) | Canonical failure-triggered episodic memory; +8% HotpotQA |
| Generative Agents | 2023 | S3 Memory | Auto | n/a | 4 | T1 (UIST 2023; arXiv:2304.03442) | Reflection + importance memory primitive |
| Cuadros et al. governed collaborative memory | 2026 | S3 Memory | Auto | Auto | 5 | T2 (arXiv:2605.04264) | Only surveyed memory system with full provenance + versioning + correction |
| MCP | 2024 | S4 Tools | n/a | n/a | 5 | T3 (modelcontextprotocol.io) | Cross-vendor standard; thousands of public servers; substantial enterprise adoption |
| Harvey | 2026 | S4 Tools | n/a | n/a | 5 | T3 (harvey.ai) | 400K queries/day; 18,000+ workflows; 200+ legal data sources |
| Hippocratic AI | 2026 | S4 Tools | n/a | n/a | 5 | T3 (hippocraticai.com) | \$3.5B valuation; 30% readmission reduction; 360% care-capacity boost |
| Multi-Agent Evolve (MAE) | 2025 | S5 Orchestration | Auto | n/a | 4 | T2 (arXiv:2510.23595) | RL co-evolution of Proposer/Solver/Judge population; one loop closed, no Loop-2 |
| Cemri et al. (AG2) | 2025 | S5 Orchestration | n/a | n/a | 3 | T2 (arXiv:2503.13657) | Specialisation +4.5 pp on GSM-Plus ($p = 0.03$); MAST 14 failure modes |
| Braintrust | 2024 | S6 Governance | n/a | Auto | 5 | T3 (braintrust.dev) | Prompts-as-code: immutable commits, eval-gated PR merge, sub-5 min rollback |
| Vellum | 2024 | S6 Governance | n/a | Auto | 5 | T3 (vellum.ai) | Same governance pattern; production deployment with eval thresholds |
| LangSmith Hub | 2024 | S6 Governance | n/a | Auto | 5 | T3 (\url{smith.langchain.com}) | Prompt repository with environment promotion and eval blocking |
| Self-Refine\* | 2023 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2303.17651) | Fails the patch-plastic discriminator: in-context iteration only |
| Mem0\* | 2024 | (contrast) | n/a | n/a | 2 | T3/T4 (mem0.ai) | Fails Loop 2: per-user memory with no cross-context promotion path |
| Tran \& Kiela\* | 2026 | (contrast) | n/a | n/a | 1 | T2 (arXiv:2604.02460) | Single-agent baselines match or beat multi-agent under matched thinking-token budgets — orthogonal finding constraining S5 claims |

```{=latex}
\endgroup
```

*Asterisks mark contrast systems included for definitional clarity.*

---

## Appendix B. Data appendix

**Corpus size.** The supplementary file `p3_master_scores.csv` contains approximately 130 unique LLM systems scored across the six substrates. Because a system can be scored on multiple substrates, the row count in the CSV exceeds the unique-system count.

**Core / contrast split.** Approximately 90 unique systems satisfy the patch-plastic discriminator (score ≥ 3 on at least one substrate) and form the core corpus. The remaining ≈ 38 systems form the contrast corpus — commonly described as agentic or self-improving in public discourse but failing at least one discriminator. Appendix D enumerates representative contrast systems.

**Inclusion criteria.** Any system that (a) wraps a foundation model with at least one persistent artifact updated from deployment signal, or (b) is named in the public discourse as a "self-improving," "scaffolded," or "agentic" system. The contrast set (Self-Refine, ReAct, plain Mem0, DSPy/TextGrad) is included so the discriminator has something to mark against.

**Exclusion criteria.** Systems whose only update mechanism is weight-level fine-tuning or RLHF — these are model-side, not scaffold-side, and belong to the self-evolution literature this paper differentiates from. Systems with no public evidence of deployment (white papers without code, demos, or production claim).

**Evidence tiers.** Each system carries one or more of: (T1) peer-reviewed publication; (T2) arXiv preprint; (T3) production claim with metrics; (T4) open-source artifact; (T5) industry-blog or interview-level documentation. T1/T4 carry highest weight in cluster analysis; T3 is admissible where the claim is concrete (specific benchmark, named integration target); T5 is admissible only when corroborated by T1–T4 elsewhere. Tier flags are propagated to cluster claims through the per-row evidence column in Appendix A; T3 production claims are not pooled with T1/T2 evidence when computing cluster-level statistics.

**Evidence-tier distribution.** Of the core corpus, approximately one quarter carry T1 evidence, roughly half carry T2 evidence, and the remainder carry T3 or T4 evidence as the primary tier.

**Survey window and dating.** January 2023 – May 2026. Preprint-only systems carry T2 evidence and are flagged in Appendix A. A fraction of T2 work is recent enough that ablations may yet be revised; cluster-level claims are robust to dropping any single T2 system.

**Scoring discipline.** Each system received a substrate-by-substrate 0–5 score against the rubric of §4 and an integrated patch-plasticity (PP) score in {0,1,2,3,3.5,4,4.5,5}. Half-scores were used sparingly when one criterion was clearly met and another partially. Ambiguous cases were resolved conservatively (downward). Scoring is single-rater; the CSV exposes every per-system score so reviewers can audit ambiguous classifications independently against the per-substrate evidence harvests.

**Composite two-loop criterion (sensitivity analysis).** The strict count of thirteen research systems satisfying the composite-two-loop criterion changes under two natural relaxations. Under (a) — counting any of versioning, lineage, or rollback as Loop-2 governance — the count rises to approximately seventeen by re-admitting MAE, MetaGen, MetaReflection, and CLIN. Under (b) — admitting session signal that updates optimizer state without persisting an artifact distinct from optimiser state — the count rises to approximately fifteen by re-admitting DSPy and TextGrad. The qualitative findings (Auto×Auto well-populated; [Human × Human] and [Human × Auto] empty in the surveyed corpus; governance-first cluster in [None × Auto]; enterprise full-auto cell empty) survive both relaxations.

**Supplementary files (shipped under `supplementary/`).**

| File | Contents |
|---|---|
| `p3_master_scores.csv` | Per-system, per-substrate 0–5 scores with evidence citations |
| `p3_harvest_s1_instructions.md` … `p3_harvest_s6_governance.md` | Per-substrate evidence harvests |
| `p3_harvest_integrated.md` | Cross-substrate integrated audit |
| `p3_harvest_composite_two_loop.md` | Strict composite-two-loop audit, 22 candidates |
| `p3_harvest_failure_modes.md` | Evidence harvest for §10 failure surface |
| `p3_prior_art_check.md` | Prior-art reconciliation against adjacent literatures |

---

## Appendix C. Gate type → estimator-family mapping

The §3 formalism collapses production gates into a single per-edit gate $G_t$ that estimates the directional loss change $\widehat{\Delta}_{z_t} L_D$. In practice, surveyed gates instantiate that abstraction in several distinct ways, and some are better read as *proposal-pruning* steps that precede the per-edit gate rather than as direct $\widehat{\Delta}$ estimators.

| Gate family | What it estimates | Slot in §3 formalism | Representative systems |
|---|---|---|---|
| **Eval-cascade** | $\widehat{\Delta} L_D$ on a held-out task suite; cascaded through cheap-to-expensive evaluators | Per-edit gate $G_t$ | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| **RL-threshold** | Reward improvement vs. a deployment threshold | Per-edit gate $G_t$ | SkillRL, SAGE, EvolveR |
| **LLM-judge with calibration** | Pairwise- or rubric-scored quality, calibrated against human agreement | Per-edit gate $G_t$ | SkillForge (Loop 1), CASCADE (consolidation gate) |
| **Surrogate verifier** | Symbolic, learned, or test-case verifier producing pass/fail or graded score | Per-edit gate $G_t$ | DGM (sandboxed code), Voyager (in-game verifier) |
| **Reviewer-judgment** | Human credit assignment via PR review or expert sign-off | Per-edit gate $G_t$ (human-instantiated) | SkillForge (Loop 2), Sierra Agent OS 2.0, Anthropic skills repo |
| **Semantic-merge** | Whether a candidate is semantically duplicated by, or compatible with, existing scaffold artifacts | *Proposal-pruning* preceding $G_t$ | NanoResearch (orchestrator semantic-merge step) |
| **MAP-Elites / archive selection** | Whether a candidate populates a previously unfilled cell in a behavior-diversity archive | *Proposal-pruning* preceding $G_t$ | AlphaEvolve (archive), ADAS (meta-agent search) |
| **Multi-sample agreement** | Whether $k$ independent proposals or evaluations converge on the same direction; false-accept rate decays as $p^k$ rather than variance shrinking as $1/k$ | *Aggregation filter* (qualitatively distinct from mini-batch averaging) | Under-explored in the surveyed corpus |

The eval-cascade, RL-threshold, LLM-judge, surrogate-verifier, and reviewer-judgment families directly populate the per-edit gate $G_t$ of §3 and inherit its descent guarantees (under the assumptions of Appendix E). The semantic-merge and archive-selection families are not estimators of $\widehat{\Delta} L_D$ — they constrain the proposal distribution rather than judging individual candidate quality, and the descent argument therefore applies to the composition (proposal-pruning ∘ per-edit gate). Multi-sample agreement filters are listed for completeness because they are the correct ML analogue for "wait for $k$ pieces of evidence before accepting an edit," which is *not* the same operation as mini-batch averaging and should not be conflated with it.

---

## Appendix D. Contrast set

The contrast corpus of approximately 38 systems is included to make the patch-plastic discriminator audit-able. Representative entries:

| System | Year | Primary discriminator failure | Brief reason |
|---|---|---|---|
| Self-Refine (Madaan et al.) | 2023 | No persistent artifact | In-context iteration only |
| ReAct (Yao et al.) | 2023 | No persistent artifact | Thought-act-observe loop is intra-session |
| Reflexion (Shinn et al.) | 2023 | No Loop 2 | Per-agent episodic memory without promotion |
| Generative Agents | 2023 | No Loop 2 | Per-agent reflection + importance memory |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks |
| Mem0 (vanilla) | 2024 | No Loop 2 | Per-user memory; no cross-context promotion |
| Zep | 2024 | No Loop 2 | Per-agent/session knowledge graph |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent |
| DSPy | 2023 | No artifact distinct from optimiser state | Prompt-template optimization |
| TextGrad | 2024 | No artifact distinct from optimiser state | Same boundary case as DSPy |
| MetaGen | 2026 | No Loop 2; no cross-session persistence | Role pool dynamic within single inference call |
| MAE (Multi-Agent Evolve) | 2025 | No Loop 2 | Co-evolution within Proposer/Solver/Judge triplet |
| MetaReflection | 2024 | No Loop 2 | Per-agent semantic memory |
| CLIN | 2023 | No cross-instance promotion | Causal abstractions per-agent-per-environment |
| LangGraph, AutoGen, CrewAI | 2023–2024 | Framework only | Orchestration frameworks; not deployed systems |
| Tran & Kiela | 2026 | Single-agent baseline | Constrains S5 maturity claims (see Appendix F) |
| W&B Weave, Agenta, LangFuse | 2024 | No Loop 1 | Observability / eval-as-code |
| Mobile-Agent-E, Cradle, OS-Copilot | 2024–2025 | No Loop 2 | Self-evolving but per-session/per-deployment |
| Agent S, Agent S2 | 2024–2025 | No Loop 2 | Computer-use agentic framework |
| ACE (Zhang et al.) | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook |
| Cursor Rules (vanilla) | 2024 | No Loop 2 | Per-project artifacts |
| GitHub Copilot custom instructions, Windsurf, Continue.dev, Zed AI rules | 2024 | No Loop 1 | Engineer-authored at repo base branch |
| Replit `replit.md` | 2025 | Loop 2 absent | Self-writing scaffold but per-workspace |
| Aider conventions, Lovable knowledge | 2024 | No Loop 1 | Engineer-authored convention files |

The full per-system exclusion log lives in `supplementary/p3_master_scores.csv` and the per-substrate evidence harvests.

---

## Appendix E. Formalization of artifact-layer descent

This appendix supplies the verification machinery for §3. The body states the descent picture as a mechanism; this appendix derives the one-step descent inequality, states the convergence proposition with its assumptions, gives the full optimisation-analogy correspondence, walks four concrete cases, and clarifies what credit assignment without chain rule means.

### E.1 The mechanism stack

The abstract update rule of §3 expands into six operations that every patch-plastic system must perform — whether explicitly engineered or accidentally emergent.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, eval regressions, tool-call failures. The Loop-1 signal source. Without it, $z_t$ has no provenance.
2. **Mode discovery.** Cluster repeated failures into patch-specific error modes — the *Architecture of Errors* catalogue, instantiated locally per patch.
3. **Delta synthesis.** Convert a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, an eval case. This produces $z_t$.
4. **Delta validation.** Estimate whether the edit reduces $L_D$ without collateral damage on adjacent inputs. The gate $G_t$ — Auto-gated when the check is an algorithmic criterion, Human-gated when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted edit stays in the local fork or climbs the scope hierarchy — project, stack, organisation, cross-tenant. Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, detect over-fitting. Without this, accumulated edits produce the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline. Surveyed systems implement them partially and unevenly: research full-auto systems excel at (3) and (4); production governance leaders at (5); industry hybrids at most of (1)–(5) but rarely (6). Implementation patterns are deferred to follow-on practitioner work.

### E.2 Setup and notation

Let the frontier model have fixed parameters $\theta_M$. Let the scaffold be a structured parameter object
$$\theta_s \in \Theta_s = \Theta_1 \times \Theta_2 \times \Theta_3 \times \Theta_4 \times \Theta_5 \times \Theta_6,$$
where the six coordinates correspond to the six substrates of §4. The space $\Theta_s$ is discrete, symbolic, and versioned. For a deployment patch $D$, define patch loss as
$$L_D(\theta_s) = \mathbb{E}_{x \sim D}\!\left[\ell(\pi(\theta_M, \theta_s, x))\right].$$

A candidate edit $z_t \in \mathcal{A}(\theta_s^t)$ is drawn from a proposal process $z_t \sim Q_t(z \mid H_t, \theta_s^t)$, where $H_t$ is the accumulated history of failures, corrections, rejected outputs, eval regressions, reviewer comments, tool-call traces, and prior accepted deltas, and conditioning on $\theta_s^t$ ensures admissibility at the current scaffold. The finite directional difference induced by the edit is
$$\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s).$$
A useful edit is one with $\Delta_z L_D < 0$. The gate's noisy estimate of this quantity is $\widehat{\Delta}_z L_D$.

### E.3 Descent inequality

The gate operates on the *estimator*, not the truth. The descent argument distinguishes them.

**Assumption A1 (positive descent bias on accepted edits).** There exists $\gamma_t > 0$ such that
$$\mathbb{E}\!\left[\widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t\right] \leq -\gamma_t - \tau_t.$$
The gate's accept-threshold $\tau_t$ ensures accepted edits clear the margin under the estimator.

**Assumption A2 (bounded estimator bias on accepted edits).** There exists $\varepsilon_t \geq 0$ such that
$$\big|\mathbb{E}\!\left[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t = 1, \theta_s^t\right]\big| \leq \varepsilon_t.$$

Combining A1 and A2 with the gated update rule of §3 and writing $p_t = \Pr(G_t = 1 \mid \theta_s^t)$,
$$\mathbb{E}\!\left[L_D(\theta_s^{t+1}) \mid \theta_s^t\right] \leq L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t \varepsilon_t.$$
This is descent under a noisy estimator: per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability.

### E.4 Convergence proposition

**Proposition (convergence of loss, informal).** Assume A1, A2, bounded loss $0 \leq L_D \leq B$, and additionally:

- **A3 (proposal coverage).** At every non-$G$-stable scaffold there exists $\delta > 0$ such that $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \leq -\delta$.
- **A4 (effective compactness).** The reachable scaffold orbit takes values in a finite or precompact subset of $\Theta_s$.
- **A5 (persistent acceptance with summable bias).** $\sum_t p_t (\gamma_t + \tau_t) = \infty$ and $\sum_t p_t \varepsilon_t < \infty$.

Then $L_D(\theta_s^t)$ is a non-negative supermartingale up to summable noise; $L_D(\theta_s^t) \to L_\infty$ almost surely for some random $L_\infty \geq 0$; and the limit set of $\{\theta_s^t\}$ is **$G$-stable**: no admissible edit clears the gate with negative expected directional loss in the limit.

The proposition claims convergence of the *loss* and stability of the *gate decision*, not convergence to a global or local optimum of $L_D$. A globally suboptimal $G$-stable scaffold is consistent with the result — when $Q_t$ never proposes the improving edit, or when $\widehat{\Delta}$ is biased to reject an improving direction. This is the ordinary target of local stochastic optimization under noisy estimators rather than a guarantee of optimality.

### E.5 Optimisation-analogy correspondence

| Optimization concept | Scaffold analogue |
|---|---|
| Parameter vector | Instructions, skills, memories, tools, routing graphs, eval gates, governance rules |
| Forward pass | Model–scaffold composite executing on patch input |
| Loss | Failure, user correction, eval regression, retrieval miss, tool error, schema violation |
| Finite directional difference | $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$ |
| Gradient estimate | Credit assignment identifying the scaffold coordinate responsible for the failure |
| SGD step | Accepted scaffold edit |
| Aggregated update | Multiple recurring failures aggregated before update (either by sampling — *mini-batch averaging* — or by sign-of-direction agreement across $k$ proposals — *multi-sample voting*) |
| Learning rate | Edit magnitude under $\oplus$ |
| Update radius | Promotion scope — which loss is being descended on (USER, PROJECT, STACK, TENANT, CORE) |
| Validation loss | Held-out patch eval before merge |
| Regularization | Complexity penalty $\Omega(z)$, bloat control, cross-patch regression checks |
| Overfitting | Scaffold improves on this patch and degrades elsewhere |
| Rollback | Reverting a harmful accepted update |

### E.6 Credit assignment without chain rule

Scaffold systems do not compute chain-rule derivatives through markdown files or tool registries, and the correspondence above deliberately omits a "backpropagation" row. They do, however, perform *credit assignment* through a pipeline: if the final answer fails, the responsible coordinate may be a retrieval configuration three layers upstream, a missing tool schema constraint, an underspecified instruction, a stale memory, or a bad orchestration edge. Engineers do this manually; LLM-judges and surrogate verifiers do it semi-automatically. The operation is *attribution* — output error is assigned to an upstream coordinate — rather than backpropagation. The descent argument of §3 needs only that this attribution succeeds with non-zero probability per failure (assumption (iv) of the scope box), not that it is performed by chain rule.

### E.7 Worked cases

**RAG.** Suppose failures recur because retrieved context omits the decisive clause. The observed loss is not "the model hallucinated." Credit assignment traces the error to the retrieval coordinate: chunking, query rewrite, metadata filter, embedding model, reranker, citation policy, or context-packing rule. The candidate edit might tighten chunk boundaries, add a metadata constraint, change the reranker, or insert a regression eval containing the missed clause. The gate tests whether retrieval recall and answer accuracy improve on the patch eval without degrading adjacent cases. If accepted, the scaffold has moved downhill on the local loss surface.

**Pitch review.** Suppose the system repeatedly overrates decks claiming a "huge market" without numeric evidence. The failure cluster identifies an under-specified rubric coordinate. The candidate edit changes "evaluate TAM size" into "require a numeric market estimate and source; if absent, cap TAM score at 4/10." The gate runs the revised rubric against held-out decks with human scores. If agreement improves without damaging unrelated criteria, the edit is committed.

**Tool-using agent.** Suppose calls repeatedly fail because optional parameters are underspecified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The candidate edit adds required fields, constrained decoding, or a pre-call uncertainty check. The gate estimates whether tool-call failure decreases without increasing refusal, latency, or unnecessary clarification.

**Memory.** Suppose a stale customer preference is repeatedly retrieved and causes bad decisions. The failure is not a weight error. The responsible coordinate is a memory entry plus its provenance, priority, and expiry policy. The candidate edit corrects, expires, or version-tags the memory. The gate checks whether the correction improves future behavior without erasing useful history.

### E.8 Loop 1 and Loop 2 as descent steps of different radius

Loop 1 proposes and validates local descent steps on a single $L_D$. Loop 2 expands the update radius — it selects, merges, and promotes accepted local edits so that they apply to a larger averaging set of patch losses. USER-level acceptance descends on a single $L_D$; PROJECT promotion descends on a project-averaged loss; STACK promotion widens the average further; CORE / cross-tenant promotion descends on a federated average. The two-loop design space is therefore not just a taxonomy of engineering patterns: it is a taxonomy of *which loss each surveyed system is descending on*, gated by which estimator.

### E.9 Overfitting in scaffold adaptation

In weight training, overfitting is usually a defect. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve cross-patch generality; they must smooth over local conventions and rare workflow-specific failures. A deployment patch needs the opposite: selective specialization to local residuals. The scaffold is therefore an intentionally overfittable layer, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold that improves one repository, hospital workflow, or legal diligence process may degrade performance elsewhere. That is not a contradiction; it is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

In non-stationary patches ($D = D_t$), the same descent mechanism tracks a moving optimum rather than converging once. This is why recency weighting, replay, pruning, expiry, and rollback are not optional hygiene; they are the scaffold-level analogues of continual-learning machinery.

---

## Appendix F. Survey detail

This appendix carries the per-substrate distributions, the per-cluster system walks, the cell-by-cell two-loop matrix discussion, the closest-approaches enumeration for the empty corner, and the orchestration-bounding result of Tran & Kiela. It supplies the verification material for §§6–9.

### F.1 Substrate maturity distribution

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|--------------|---:|----:|----------------------|-------------------------------------------------------|
| **S1 — Instructions** | 12 | 2.83 | *(none)* | Rules persist across IDEs and agents (Claude Code's CLAUDE.md, Cursor Rules, AGENTS.md, Windsurf, Continue.dev) but no surveyed instruction system closes both an automated inner loop and a governed two-loop promotion. Ceiling held at 4 by Claude Code and Replit |
| **S2 — Skills** | 16 | 2.62 | SAGE, COSPLAY | Research frontier is active (failure-triggered skill update); production governance is weaker. Anthropic's skills repository is one-pool with PR review but no automated eval gate |
| **S3 — Memory** | 19 | 3.16 | Cuadros et al. governed collaborative memory | Cross-session memory is widespread; *correctable, versioned* memory is rare. Production memory systems (ChatGPT Memory, Claude Memory, Mem0, Zep, MemGPT) treat memory as append-only |
| **S4 — Tools** | 19 | 3.63 | MCP, Harvey, Hippocratic AI | Most mature production substrate. Tool bundles are the commercial unit; MCP is the cross-vendor standard with broad public-server ecosystem and substantial enterprise adoption |
| **S5 — Orchestration** | 19 | 2.68 | *(none)* | Multi-agent topologies exist (LangGraph, AutoGen, CrewAI) but topology *evolution* is rare; MAE comes closest with RL co-evolution of Proposer/Solver/Judge population but lacks Loop-2 cross-context promotion and so does not satisfy the score-5 rubric |
| **S6 — Governance** | 21 | 3.05 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | High production maturity for prompts-as-code — immutable commits, eval-gated PR merge, sub-five-minute rollback — typically without inner-loop adaptation |
| **INTEGRATED** | 34 | 3.74 | NanoResearch, AutoAgent, SkillRL | The high-water mark when present, but the cluster is dominated by research systems lacking enterprise governance |

### F.2 Cluster table with representative systems

| Cluster | Representative systems (year, PP score) | Loop 1 / Loop 2 | What the cluster proves |
|--------------|------------------------------|--------------|------------------------------------------|
| Research full-auto | NanoResearch (2026, 5), SkillRL (2026, 5), AlphaEvolve (2025, 4), DGM (2025, 4), ADAS (2024, 4), Voyager (2023, 4) | Auto / Auto | Both loops can be fully automated under algorithmic gates; benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge (2026, 4), CASCADE (2025, 4.5), Sierra OS 2.0 (2025, 3)[^sierra-dual], Cognition Devin (2024, 3) | Auto / Human | Algorithmic Loop-1 gate plus reviewer-judgment Loop-2 gate is the production-viable cell; SkillForge is the architectural exemplar |
| Governance-first | Braintrust, Vellum, LangSmith Hub (all 2024, S6 = 5) | None / Auto | Eval-gated promotion exists; candidate generation is manual; no patch-plastic inner loop |
| Open standards | AGENTS.md (2025), MCP (2024), Claude Skills (2025), Cursor Rules (2024) | Mixed / Mixed | Vendor-cross convergence on artifact format and tool attachment; tens of thousands of AGENTS.md repositories; broad MCP server ecosystem with substantial enterprise adoption |

[^sierra-dual]: Sierra Agent OS 2.0 also appears in the *Open standards / vertical-bundle* discussion in F.4 because its commercial product wraps a vertical workflow around the standardised agent-OS surface; we place it primarily in *Production hybrid* on the basis of its Loop-1/Loop-2 gate types.

### F.3 Surprising absences

Five absences stand out across the patch-plastic core corpus:

1. **Failure-triggered memory is rare in production.** Deployed memory systems prefer recording preferences and successful facts; only Reflexion, the Voyager skill library, Gemini Code Assist's PR-rejection memory, and the classical SOAR chunking pattern explicitly record residuals. The most obvious Loop-1 signal is the one production memory systems mostly ignore.
2. **Cross-customer skill promotion is absent.** AGENTS.md is cross-vendor; Anthropic's skills repository is one-pool. No surveyed system has a vetted cross-organisational marketplace with eval-gated promotion.
3. **Memory versioning is mostly unsolved.** Only the Cuadros et al. (2026) governed collaborative memory framework provides explicit provenance, versioning, and correction pathways.
4. **Scaffold-level curriculum is absent.** No surveyed system selects *which* sessions inform the gradient. Every session contributes equally; weighting by recency, severity, or representativeness has not been published.
5. **Overfitting detection at Loop-2 promotion is absent.** No surveyed system runs a held-out eval set per project to catch scaffolds that over-fit one deployment before they propagate to another.

### F.4 Per-cluster walks

**Research full-auto.** **NanoResearch** (Xu et al., 2026) co-evolves Skills, Memory, and Policy with a semantic-merge orchestrator; Innovation 4.96 → 5.65 and Compliance 6.66 → 8.96 across three rounds. **SkillRL** (arXiv:2602.08234) uses RL reward distillation with a hard threshold at task-category accuracy below 0.4 and reports +15.3% over strong baselines. **AlphaEvolve** (DeepMind, 2025) runs a Gemini-driven ensemble with a cascade evaluator and a MAP-Elites archive, deployed at Google to gain +0.7% Borg compute worldwide, +23% on the Gemini training kernel, +32.5% on FlashAttention, and the first general-field, recursively applicable improvement over Strassen's 1969 bound on 4×4 complex matrix multiplication (48 scalar multiplications). The honest framing matters: AlphaTensor (Fawzi et al., 2022) had already found a 47-multiplication algorithm over GF(2), and Winograd reported a 48-multiplication method for commutative rings that was not recursively applicable; AlphaEvolve's contribution is the first improvement that holds in general fields and admits recursive composition. **DGM** (Zhang et al., 2025) modifies its own source code with archive-based parent selection; SWE-bench 20% → 50%. The cluster maximises velocity. Enterprise governance is uniformly absent.

**Production hybrid.** **SkillForge** (Alibaba Cloud, arXiv:2604.08618) drives auto-generated skill diffs through an LLM-judge with >90% human agreement (the Loop-1 gate); human support engineers review what the LLM-judge passes (the Loop-2 gate). VFS version commits provide full lineage. **CASCADE** (Huang et al., 2025) reports the largest within-benchmark ablation gain in the surveyed corpus — 93.3% vs. 35.4% on SciSkillBench (+57.9 pp) — driven by memory consolidation gated by human-agent collaboration. The headline gain is not directly comparable to AlphaEvolve's production +0.7% Borg or DGM's +30 pp on the broader SWE-bench: it is measured on a single benchmark designed to reward the very mechanism CASCADE adds, and should be read as evidence of mechanism-on-benchmark fit rather than as a cross-cluster effect size. **Sierra Agent OS 2.0** routes AI-driven Insights through human-authored Expert Answers in GitHub-style Workspaces. **Cognition Devin** ships dynamic in-session tool creation with a 67% PR-merge rate (the merged PRs are the Loop-2 promotion). This is the production-viable cell.

**Governance-first.** **Braintrust**, **Vellum**, **LangSmith Hub**, **W&B Weave**, **Agenta**, **LangFuse**. The pattern is *prompts-as-code*: immutable commits, semantic-version tag pointers, PR-blocked merges on eval regression, sub-five-minute rollback. Engineers iterate the artifacts manually; the eval pipeline gates the promotion. We frame this as **MLOps for scaffolds**, distinct from MLOps for weights.

**Open standards.** **AGENTS.md** (Linux Foundation, December 2025) is now in over 60,000 GitHub repositories; Lulla et al. (2026) report −28.64% wall-clock and −16.58% tokens with no quality loss after adding an AGENTS.md scaffold. **MCP** (Anthropic, 2024) has become the cross-vendor standard with thousands of public servers and substantial enterprise adoption. **Claude Agent Skills**, **Cursor Rules**, **GitHub Copilot custom instructions**, **Windsurf rules**, **Continue.dev rules**, **Zed AI rules**, **Replit `replit.md`** all converge on the same pattern: a git-tracked markdown artifact attached to a workspace, with an MCP-style tool layer for actions. Convergence across vendors is the strongest evidence the architecture is real rather than a single vendor's local optimum.

The four clusters do not partition the corpus — many systems sit between two clusters — but they capture the architectural variation. **Vertical-bundle vendors** (Harvey for legal, Hippocratic AI for healthcare, Sierra for customer experience) sit between *open standards* and *production hybrid*: the bundle is the commercial unit; the underlying model is mostly the same one a competitor would use.

**Tran & Kiela (2026) orchestration bound.** One result from the orchestration literature bounds how strongly the cluster discussion can be read as evidence for multi-agent architectures specifically. Tran & Kiela (2026) report that single-agent LLMs match or beat multi-agent systems on multi-hop reasoning when thinking-token budgets are matched; the implication is that observed maturity gaps on S5 (orchestration) may reflect the rarity of governed topology *evolution* and the conflation of agent-count with compute-budget rather than a structural deficit of multi-agent designs. The orchestration cluster is therefore better read as evidence that production has converged on flat agent topologies and on tool-mediated rather than role-mediated decomposition, not as evidence that orchestration is the binding maturity constraint.

### F.5 Two-loop matrix: cell-by-cell discussion

**[Auto × Auto]** is most populated (eleven systems). Every member has a machine-evaluated decision criterion on both loops. Velocity is the cluster's defining property; the lack of cross-organisational governance is its uniform weakness.

**[Auto × Human]** is the production-viable cell — Loop 1 fires at machine speed under an algorithmic criterion, Loop 2 requires human approval before propagation. The pattern reconciles automation velocity with reviewer accountability. SkillForge's LLM-judge + reviewer pipeline is the architectural exemplar. CASCADE, Sierra, and Devin instantiate variants; the industry exemplars (Sierra, Devin) are marked with † because vendor documentation rather than peer-reviewed metrics is the primary evidence.

**[None × Auto-gated]** holds the governance-first prompts-as-code systems (Braintrust, LangSmith Hub, Vellum). They have a real Loop 2 — eval-gated CI blocks promotion on regression — but no Loop 1 in the patch-plastic sense because the candidate artifacts are authored by engineers at their desks rather than triggered by session feedback. The asterisks mark this: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated.

**[Human × Auto]** is empty by engineering logic: if humans author candidates manually, automated promotion offers little leverage. A speculative occupant would be "expert curation + auto-distribution" (expert-authored skills automatically gated through a held-out eval before shipping); no published example exists.

**[Human × Human]** is empty in the surveyed corpus. A candidate occupant would be a reviewer-authored-and-reviewer-promoted artifact pipeline targeting solo and small-team workflows where automation cost exceeds review latency. No public example was found during the May 2026 survey window.

**[Human × None]** is structurally improbable: a system requiring human authorship on Loop 1 but with no Loop 2 collapses to "engineer-edits-a-config" and is not patch-plastic in the sense of §3.

**DGM dual-mode note.** DGM operates in both [Auto × Auto] (primary archive-based evolution) and [Auto × Human] (sandboxed code-modification review) modes depending on deployment configuration; we list it once in the dominant cell.

### F.6 Closest approaches to the empty corner

The four properties of enterprise full-auto are (a) auto-gated Loop 1, (b) multi-tenant cross-org promotion, (c) versioned lineage with RBAC, (d) rollback. Closest approaches partition the requirements:

- **AlphaEvolve** has (a) and partial (b) within a single organisation; no cross-org promotion mechanism.
- **NanoResearch** has (a) at the research level; no enterprise governance layer described.
- **SkillForge** has (a) and (b) within one enterprise, partial (c) via VFS commits; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has (b) and partial (a); the GitHub-style Workspaces provide some lineage but not RBAC-with-rollback in the strict sense.
- **Vellum / Braintrust / LangSmith Hub** have (c) and (d) explicitly but no (a) or (b) in the strict sense — these are governance-first systems by construction.

No surveyed system combines (b), (c), and (d) under any gate type — the cross-organisational governance triad is itself unfilled, independently of whether Loop 1 is auto-gated.

### F.7 Deployment-dependence of the empty corner

Whether the corner *should* be filled is deployment-dependent. In safety-critical domains — medical decision support, legal advice, financial advice — reviewer-judgment gates may be a design feature rather than a defect, and the human latency is the point. The narrower survey claim is what matters: no public system currently combines automated local scaffold evolution with governed cross-organisation promotion, versioned lineage with RBAC, and rollback. Naming the corner converts a vague gap into a specific four-property audit criterion that any future system can be measured against. The shortest demonstrable path appears to build on AlphaEvolve's cascade evaluator + MAP-Elites archive, extending federation from within-DeepMind multi-target to cross-customer multi-tenant — but the architectural surface, not the timeline, is what this paper claims.

---

## References

AGENTS.md. (2025). AGENTS.md: A cross-vendor open standard for agent instructions. Linux Foundation. <https://agents.md>

Agashe, S., Han, J., Gan, S., Yang, J., Li, A., & Wang, X. E. (2024). Agent S: An open agentic framework that uses computers like a human. *arXiv preprint arXiv:2410.08164*.

Agashe, S., et al. (2025). Agent S2: A compositional generalist-specialist framework for computer use agents. *arXiv preprint arXiv:2504.00906*.

Anthropic. (2024). Model Context Protocol specification. <https://modelcontextprotocol.io>

Arbuzov, M. L., Bei, S., Dong, Z., Kalaev, D., & Shvets, A. A. (2025). Beyond exponential decay: Rethinking error accumulation in large language models. *arXiv preprint arXiv:2505.24187*.

Arbuzov, M. L., Shvets, A. A., & Bei, S. (2026). The architecture of errors: Logarithmic mode discovery and polylogarithmic intervention budgets for long-context LLM reliability. *arXiv preprint* (forthcoming).

Cemri, M., et al. (2025). Why do multi-agent LLM systems fail? *arXiv preprint arXiv:2503.13657*. Introduces the MAST taxonomy.

Chen, M., Li, Y., Yang, Y., Yu, S., Lin, B., & He, X. (2024). AutoManual: Constructing instruction manuals by LLM agents via interactive environmental learning. *NeurIPS 2024*. arXiv:2405.16247.

Chen, Y., et al. (2025). Multi-Agent Evolve: LLM self-improve through co-evolution. *arXiv preprint arXiv:2510.23595*.

Cuadros, D. F., Maiga, A.-A., Meskhidze, H., & Curtis-Trudel, A. (2026). Governed collaborative memory as artificial selection in LLM-based multi-agent systems. *arXiv preprint arXiv:2605.04264*.

Dohare, S., et al. (2024). Loss of plasticity in deep continual learning. *Nature*, 632(8026), 768–774.

Du, P. (2026). Memory for autonomous LLM agents: Mechanisms, evaluation, and emerging frontiers. *arXiv preprint arXiv:2603.07670*.

Fang, J., Peng, Y., Zhang, X., et al. (2025). A comprehensive survey of self-evolving AI agents: A new paradigm bridging foundation models and lifelong agentic systems. *arXiv preprint arXiv:2508.07407*.

Fawzi, A., Balog, M., Huang, A., et al. (2022). Discovering faster matrix multiplication algorithms with reinforcement learning. *Nature*, 610(7930), 47–53. (DeepMind AlphaTensor.)

Gao, H.-a., Geng, J., Hua, W., et al. (2026). A survey of self-evolving agents: What, when, how, and where to evolve on the path to artificial super intelligence. *Transactions on Machine Learning Research*. arXiv:2507.21046.

Harvey. (2026). Harvey product overview. <https://www.harvey.ai>

Hippocratic AI. (2026). Polaris clinical outcome evidence. <https://www.hippocraticai.com>

Hu, S., Lu, C., & Clune, J. (2024). Automated design of agentic systems (ADAS). *arXiv preprint arXiv:2408.08435*.

Huang, X., et al. (2025). CASCADE: Cumulative agentic skill creation through autonomous development and evolution. *arXiv preprint arXiv:2512.23880*.

Jaroslawicz, D., et al. (2025). How many instructions can LLMs follow at once? *arXiv preprint arXiv:2507.11538*. Introduces the IFScale benchmark.

Kirk, R., Mediratta, I., Nalmpantis, C., et al. (2024). Understanding the effects of RLHF on LLM generalisation and diversity. *ICLR 2024*. arXiv:2310.06452.

Liu, N. F., et al. (2023). Lost in the middle: How language models use long contexts. *TACL*. arXiv:2307.03172.

Liu, X., et al. (2026). SkillForge: Forging domain-specific, self-evolving agent skills in cloud technical support. *arXiv preprint arXiv:2604.08618*. Accepted at ACM SIGIR 2026 Industry Track.

Lulla, J. L., et al. (2026). On the impact of AGENTS.md files on the efficiency of AI coding agents. *arXiv preprint arXiv:2601.20404*.

Madaan, A., et al. (2023). Self-Refine: Iterative refinement with self-feedback. *NeurIPS 2023*. arXiv:2303.17651.

Novikov, A., et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. *arXiv preprint arXiv:2506.13131*. (DeepMind.)

Padmakumar, V., & He, H. (2023). Does writing with language models reduce content diversity? *arXiv preprint arXiv:2309.05196*.

Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *UIST 2023*. arXiv:2304.03442.

Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*. arXiv:2303.11366.

Sierra. (2025). Agent OS 2.0: From answers to memory and action. <https://sierra.ai/blog/agent-os-2-0>

Singh, S., et al. (2025). The leaderboard illusion. *arXiv preprint arXiv:2504.20879*.

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive architectures for language agents (CoALA). *Transactions on Machine Learning Research*. arXiv:2309.02427.

Tran, D., & Kiela, D. (2026). Single-agent LLMs outperform multi-agent systems on multi-hop reasoning under equal thinking token budgets. *arXiv preprint arXiv:2604.02460*.

Wang, G., et al. (2023). Voyager: An open-ended embodied agent with large language models. *arXiv preprint arXiv:2305.16291*.

Wang, J., et al. (2025). Reinforcement learning for self-improving agent with skill library. *arXiv preprint arXiv:2512.17102*. Method named SAGE.

Wang, X., et al. (2026). AutoAgent: Evolving cognition and elastic memory orchestration for adaptive agents. *arXiv preprint arXiv:2603.09716*.

Wu, R., et al. (2025). EvolveR: Self-evolving LLM agents through an experience-driven lifecycle. *arXiv preprint arXiv:2510.16079*. Accepted at ICML 2026.

Wu, X., et al. (2026). Co-evolving LLM decision and skill bank agents for long-horizon tasks. *arXiv preprint arXiv:2604.20987*. Framework named COSPLAY.

Xia, P., et al. (2026). SkillRL: Evolving agents via recursive skill-augmented reinforcement learning. *arXiv preprint arXiv:2602.08234*.

Xu, Jinhang, et al. (2026). NanoResearch: Co-evolving skills, memory, and policy for personalized research automation. *arXiv preprint arXiv:2605.10813*.

Xu, Zhenlin, et al. (2026). From storage to steering: Memory control flow attacks on LLM agents. *arXiv preprint arXiv:2603.15125*. Introduces the MCFA attack class.

Zhang, J., et al. (2025). Darwin Gödel machine: Open-ended evolution of self-improving agents. *arXiv preprint arXiv:2505.22954*. (Body text refers to this as DGM.)

Zhou, Y., Shu, W., Su, Y., et al. (2026). A comprehensive survey on agent skills: Taxonomy, techniques, and applications. *arXiv preprint arXiv:2605.07358*.

Zou, W., et al. (2024). PoisonedRAG: Knowledge corruption attacks to retrieval-augmented generation of large language models. *arXiv preprint arXiv:2402.07867*. Accepted at USENIX Security 2025.
