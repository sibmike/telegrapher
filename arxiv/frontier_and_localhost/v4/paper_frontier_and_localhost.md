---
title: "Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights"
author:
  - |
    Mikhail L. Arbuzov  
    Independent Researcher  
    mike.arbuzov54@gmail.com
  - |
    Lee Mosbacker  
    Independent Researcher  
    lee.mosbacker@gmail.com
  - |
    Sisong Bei  
    Independent Researcher  
    qurining@gmail.com
  - |
    Ziwei Dong  
    Independent Researcher  
    ziwei.dong@alumni.emory.edu
  - |
    Dmitri Kalaev  
    Independent Researcher  
    kalaevdr@gmail.com
  - |
    Alexey A. Shvets  
    Palo Alto Networks  
    ashvets@paloaltonetworks.com
date: ""
abstract: |
  Deployed AI systems change through instructions, skills, memories, tools, and orchestration long before their model weights are updated. These changes accumulate experience, but their persistence alone does not establish that the system is improving. This survey examines how 256 production and research systems turn experience into lasting changes outside the weights. We distinguish two decisions: whether an edit improves the deployment that produced it, and whether there is enough evidence to share it more widely. Together, these decisions define a local improvement loop and a promotion loop. Among recently added systems with a local adaptation loop, automatic acceptance tests are present in nearly every one (89 of 96), while failure capture and attribution remain less developed. Promotion is more fragmented: the surveyed systems provide evaluation, shared artifact pools, lineage, access control, and rollback in different combinations, but none documents their integration into governed promotion across organizations. The feedback available to a deployment helps explain this pattern. Exact checks, observed outcomes, judgments, and delayed rewards support different acceptance rules and expose different limitations. In every case, an accepted edit is supported only for the measure and task distribution on which it was evaluated. We use this observation to develop five conditions for artifact-layer optimization, a classification of feedback and gate types, and four properties for auditing cross-organization promotion. The resulting framework identifies what existing systems can already automate and where new evidence or human judgment is still required.
header-includes:
  - \usepackage{xurl}
  - \usepackage{calc}
  - \DeclareUnicodeCharacter{2260}{\ensuremath{\neq}}
  - \DeclareUnicodeCharacter{2265}{\ensuremath{\geq}}
  - \DeclareUnicodeCharacter{2264}{\ensuremath{\leq}}
  - \DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}
  - \DeclareUnicodeCharacter{2282}{\ensuremath{\subset}}
  - \DeclareUnicodeCharacter{2248}{\ensuremath{\approx}}
  - \DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
  - \DeclareUnicodeCharacter{2211}{\ensuremath{\sum}}
  - \DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}
  - \DeclareUnicodeCharacter{03B5}{\ensuremath{\varepsilon}}
  - \DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
  - \DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
  - \DeclareUnicodeCharacter{03A9}{\ensuremath{\Omega}}
  - \DeclareUnicodeCharacter{03B8}{\ensuremath{\theta}}
  - \DeclareUnicodeCharacter{2208}{\ensuremath{\in}}
  - \DeclareUnicodeCharacter{2026}{\ldots}
  - \DeclareUnicodeCharacter{2020}{\dag}
  - \DeclareUnicodeCharacter{2021}{\ddag}
  - \DeclareUnicodeCharacter{00A7}{\S}
  - \DeclareUnicodeCharacter{03BA}{\ensuremath{\kappa}}
  - \DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
  - \DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
  - \DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}
  - \DeclareUnicodeCharacter{03B3}{\ensuremath{\gamma}}
  - \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
  - \DeclareUnicodeCharacter{2218}{\ensuremath{\circ}}
  - \DeclareUnicodeCharacter{2212}{-}
  - \DeclareUnicodeCharacter{2070}{\ensuremath{^0}}
  - \DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}
  - \DeclareUnicodeCharacter{200B}{\hskip0pt}
---
## Introduction {#sec:intro}

A coding agent repeatedly uses the wrong naming convention in a repository. An engineer adds a line to its instructions, and the next session follows the convention. The model has not changed, but the deployed system has. Similar changes happen when an assistant corrects a stored preference, acquires a reusable skill, or learns which tool to call. Much of the experience that makes an AI system useful in one setting now accumulates in these persistent artifacts outside the model's weights.

We call this layer the **scaffold**. It includes instructions, skills, memory, tools, orchestration, and the evaluation and governance rules that control their use. In the language of compound AI systems [@zaharia2024compound], it is the part surrounding the model that a deployment can inspect and revise without retraining it. The distinction matters because the two parts change on different schedules. A team can revise an instruction or tool binding as soon as a problem is understood, while a new model requires a separate training, evaluation, and release process.

The ease of making a change also makes it easy to accumulate changes whose value is unknown. A rule added after one incident may prevent a recurring error, conflict with another rule, or merely make the prompt longer. A corrected memory may remain in the history while the system continues to retrieve the outdated entry. Even a demonstrably useful change can become harmful when copied into a deployment with different tasks or conventions.

These situations raise two questions. What evidence justifies keeping a local change? What additional evidence justifies sharing it? This survey uses those questions to examine 256 public production and research systems. The first defines a **local loop**: identify a recurring failure, propose a change to the responsible artifact, and test whether the change helps. The second defines a **promotion loop**: decide whether the change should be adopted by another project, team, or organization, and preserve enough history to reverse that decision.

The systems surveyed have developed these loops unevenly. Automatic tests for accepting a local edit are present in nearly every recently added system that has a local loop: 89 of 96. The steps that should supply those tests with well-founded candidates are weaker: failures are often not retained in a usable form, and a failed output rarely identifies which instruction, memory, skill, or tool binding caused it. Meanwhile, production platforms have built substantial versioning and release machinery without any process that proposes changes from deployment experience.

Sharing adds a further limitation. A change that improves one deployment has been evaluated against that deployment's tasks and measure of success. Another deployment may need different behavior. Shared formats and registries make artifacts portable, but they do not establish that an artifact will help its recipient. Some surveyed systems check transferred changes within one operator. None documents an automatic local improvement loop connected to promotion across organizations with versioned lineage, access control, and rollback.

The feedback available to each system helps explain these differences. A compiler or test suite can check a candidate immediately. A booked appointment provides a later, noisier outcome. A writing task may depend on a judge, whose preferences can drift. A research decision may take months to evaluate. These signals support different kinds of automation, and none establishes an improvement beyond what it actually measures.

The survey develops a framework for reading this evidence. We first define the two loops and the conditions under which artifact maintenance constitutes optimization. After describing the corpus and scoring method, we examine local adaptation, the feedback that constrains it, and the evidence needed for promotion. The later sections consider failures that arise when these checks are missing, specify the unassembled architecture for governed sharing, and connect the findings to the research lines that produced its components. The evidence consists of published methods and public documentation; the survey introduces no new experiments. Its scores and classifications are released for inspection.

## From a local fix to a measured improvement {#sec:loop}

Adding a naming rule after an error is a reasonable response. To learn whether it works, however, the team must run the agent again on relevant tasks and compare the results. If the change helps, it should persist. If it causes regressions, the team needs a way to reject or reverse it. Repeating this process turns a growing collection of fixes into a procedure for improving the deployment.

### The local loop

The procedure starts with a record of failures: rejected answers, user corrections, failed tool calls, evaluation regressions, or unsuccessful tasks. Repeated failures are grouped into modes and prioritized by frequency and severity. For each selected mode, the system tries to identify the artifact responsible. A stale memory entry calls for a different intervention from a missing tool argument or an ambiguous instruction.

We call this step **credit assignment**. It links an observed failure to an editable part of the scaffold, or **coordinate**. The system then proposes a candidate edit and evaluates it against the current scaffold. The acceptance test is the **gate**. An accepted edit is retained as a versioned artifact; subsequent evidence of regression can trigger rollback. Fig. REF(fig:descent) shows the complete local loop.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{figures/fig1_descent}
\caption{The local improvement loop. Recurring failures guide a proposed scaffold edit. An acceptance gate tests the change before it persists, and later regressions can trigger rollback. Sharing the accepted edit requires a separate promotion decision (Fig. REF(fig:scope)).}
\label{fig:descent}
\end{figure*}
```

The evaluation must be tied to the deployment's actual workload. A deployment serves a particular distribution of users, tasks, and conventions, which we call its **patch**. Its **patch loss** measures failure on that distribution. Depending on the application, this may be a task-failure rate, correction rate, retrieval error, or another operational measure. A gate can establish an improvement only to the extent that its evaluation estimates this loss.

### The second decision: whether to share the fix

Suppose the naming rule improves the original repository. The team may now consider adding it to a shared template. That decision changes the population on which the rule will act. Other repositories may follow a different convention, and the local evaluation says little about them.

The promotion loop therefore asks for evidence at the receiving scope. We call this **receiving-side evaluation**: a check conducted on the tasks of the deployment that would adopt the edit. The **evidence radius** is the scope for which the available evaluation supports the change. A local success does not automatically enlarge that radius. Section REF(sec:design) develops the scopes and examines systems that already transfer artifacts between them.

### Five conditions for artifact-layer optimization

We use **artifact-layer descent** for the form of maintenance that connects recurring failures to measured improvements through five conditions:

1. **A measurable patch loss:** the deployment has a defined measure of success or failure.
2. **A failure log:** relevant failures are retained as evidence for later changes.
3. **Credit assignment:** failures can, at least sometimes, be traced to the scaffold coordinates responsible.
4. **A candidate edit:** the process proposes a change to those coordinates.
5. **An acceptance gate:** an edit is retained or promoted only after a check of whether it lowers the relevant loss.

The model weights remain fixed during this process, and the edits persist beyond the current interaction. These conditions distinguish three recurring forms of maintenance. In *patchwork*, an engineer adds a rule after an incident without measuring the result. In *random artifact search*, a system tests many variants and keeps a winner without tracing failures to their causes. Artifact-layer descent uses that trace to direct the proposed change and tests it before acceptance. Where the conditions are only partly met, the optimization interpretation is correspondingly limited.

For deployment $D$, write the patch loss as
$$L_D(\theta_s)=\mathbb{E}_{x\sim D}\!\left[\ell(\pi(\theta_M,\theta_s,x))\right],$$
where $\theta_M$ denotes the fixed model weights, $\theta_s$ the editable scaffold, and $\ell$ the operational loss. A proposal process uses the failure history to produce an edit $z_t$. There is no analytic gradient through an instruction file or memory entry. Instead, the gate estimates the change in loss and accepts when that estimate clears a required margin:
$$G_t(z_t)=1\iff\widehat{\Delta}_{z_t}L_D(\theta_s^t)+\lambda\Omega(z_t)\leq-\tau_t.$$
Here $\Omega\geq0$ penalizes edit complexity and promotion breadth, and $\tau_t\geq0$ is the acceptance margin. An evaluation that blocks a regressing merge is a practical instance of this rule. A reviewer or governance process can also instantiate the gate by requiring stronger evidence for a broader or more complex change.

Appendix REF(app:formal) gives the update rule and a one-step descent inequality under assumptions on the gate's estimation bias. With additional coverage, compactness, and summable-bias assumptions, improving edits eventually stop clearing the gate. This is **gate stability**, not a claim of global optimality. A limited proposal process or biased evaluator can leave useful changes undiscovered or rejected.

### Who proposes and who decides

The author of an edit and the authority that accepts it are separate. An agent may draft a revision that a person approves; an engineer may write a revision that an automatic evaluation rejects. We classify the gate by who makes the acceptance decision:

- **Auto:** a program applies a check, including a verifier, evaluation threshold, or language-model judge [@zheng2023judge]. Whether that judge has been calibrated against people is a separate question, which Section REF(sec:signal) takes up.
- **Human:** a person decides whether to accept the change.
- **None:** no acceptance decision is made, either because the loop is absent or because every proposed edit is retained.

A pair such as [Auto × Human] denotes an automatic local gate followed by a human promotion gate. These labels describe the decision mechanism. They do not, by themselves, establish that the decision is well supported.

The loss definition imposes two limits on every such loop. First, an accepted edit is evidence of improvement only on the measure and tasks evaluated. Promotion must preserve that meaning or establish the improvement again. Second, the loop optimizes a defined objective. It does not discover a better objective simply by accumulating edits. Revising the evaluator changes the objective itself, a complication we return to in Section REF(sec:reflexive).

## Corpus and method {#sec:method}

We read each system's public method or documentation for four things: the persistent artifact it changes, the feedback that prompts the change, the decision that accepts it, and the scope in which the result is used. This allows systems with different names and application domains to be compared by their behavior.

### Scope and selection

The corpus contains 256 unique systems from January 2023 through the October 2026 cutoff. The first search pass identified 130 systems by May 2026; the second added 126. Sources include research papers, public repositories, product documentation, and supported production reports; the search families, evidence tiers, and inclusion rules are recorded with the released data (Appendix REF(app:data)).

A system enters the survey if it adapts a foundation model through a persistent artifact updated from deployment signal, or if it is publicly described as self-improving, scaffolded, or agentic. Including the latter group provides a contrast set: the survey can test whether those descriptions correspond to persistent adaptation. Systems whose only update mechanism is weight-level training are excluded, as are systems without public evidence of release or deployment.

We apply two filters. The first admits a system to the **core corpus** if it scores at least 3 on at least one scaffold substrate under the rubric below. Of the 256 systems, 204 form the core corpus and 52 the contrast corpus. A system may have one integrated row or several substrate-specific rows, so the 256 systems occupy 269 scored rows.

The second filter is a **two-loop audit**. It asks whether session feedback changes a persistent artifact and whether that artifact is subsequently promoted beyond the deployment that produced it, with versioning or lineage. Applied to 202 of the 204 core systems and to 4 research systems classified from their papers alone (SkillOpt, FederatedSkill, SkillClaw, and ChronoMem), it admits 11 research systems and 3 industry exemplars; the eight systems without an audit are listed with the contrast set (Appendix REF(app:contrast)). Fig. REF(fig:corpus) summarizes the selection.

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\textwidth]{figures/fig4_corpus_flow}
\caption{Corpus selection. The 256 systems occupy 269 scored rows. The first filter separates core from contrast systems; the two-loop audit then checks persistent local adaptation and promotion with lineage. The audit includes the additional paper-based classifications described in the text.}
\label{fig:corpus}
\end{figure}
```

The research systems passing the audit are NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual, and CASCADE. The industry exemplars are Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories. SkillOpt is classified from its paper and is not a row in the 256-system score table. The remaining paper-based systems are identified in the data notes (Appendix REF(app:data)) and the audit's boundary cases in the contrast set (Appendix REF(app:contrast)).

Passing this audit does not establish governed sharing across organizations. All passing systems promote within one operator, into a shared bank or archive that later runs draw from, or across the agents and sessions of one deployment. Letta passes on the lineage of its shared-memory updates even though those updates have no acceptance gate. Six further systems promote across contexts without lineage on the promoted artifact; their treatment under relaxed audit rules is reported separately.

### Substrates and scoring

The scaffold has six substrates: instructions, skills, memory, tools, orchestration, and governance. These are the possible targets of a proposed edit. Table REF(tab:V-1) describes them; the episodic, semantic, and procedural memory categories follow Sumers et al. [@sumers2023coala].

| Substrate | What persists | A score of 5 requires |
|-----------|----------------------------|----------------------------|
| S1 Instructions | Project, team, or organization rules attached to a workspace | Versioned rules promoted under an automatic gate |
| S2 Skills | Procedures, as code or text, loaded on demand | A skill bank that edits itself on failure, test-gated, versioned, and promoted |
| S3 Memory | Experience kept across sessions: episodic, semantic, procedural | Provenance, versions, and a correction path for every entry |
| S4 Tools | The vetted action surface and its schemas | Evaluation-gated tool versions; a curated bundle as the product |
| S5 Orchestration | The multi-role graph and its routing | Topology updated from deployment feedback by a loop outside the agent's own run |
| S6 Governance | Versioning, promotion, audit, rollback | Staged promotion with evaluation thresholds, an audit log, and rollback |

Table V-1. The six scaffold substrates, what each holds, and what a system must do on it to score 5.

The common scoring scale runs from 0 to 5. At 0 an artifact is ephemeral. At 1 it persists locally; at 2 it persists with tool attachment but without feedback. At 3 it either spans scopes without a gate or is updated from feedback by a person. At 4 a program updates it from feedback. The score-5 requirement depends on the substrate, as specified in the table.

This last distinction is important when interpreting the scores. Instructions and skills require both loops to reach 5. Orchestration requires a topology updated from deployment feedback by a loop outside the agent's own execution. Memory, tools, and governance are scored for their corresponding governance capabilities, so a registry can score 5 without generating local edits. Integrated rows measure breadth and depth of adaptation, not closure of either loop. The scale therefore supports substrate-specific comparisons; a top score is not a universal certificate of complete optimization.

Table REF(tab:V-2) gives the corpus distribution. Research systems hold the top marks on skills, memory, and the integrated row. Production platforms and standards hold them on tools and governance. No system reaches the top score across all six substrates, and none reaches it on instructions or orchestration.

| Substrate | $n$ | Mean | Score-5 systems | What the corpus holds on it |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents and nothing measures them; no system closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | The local loop closes under a program in the research systems; the production repositories merge by hand |
| S3 Memory | 50 | 3.06 | Cuadros et al. | The ledger ships in products; the correction a gate would enforce is absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | The most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies change under an evaluation gate; one structurally gated instance; no two-loop system with lineage |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md under the Agentic AI Foundation (AAIF) | Prompts-as-code mature; registries add lineage and rollback; no local loop generates a candidate |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | Breadth and depth of adaptation, not the loop; reached only by research systems without enterprise governance |

Table V-2. Substrate maturity across the 256-system corpus. Column n counts scored rows on each substrate, Mean is the average score, and Score-5 systems reach the substrate's top mark; the integrated row counts systems scored across several substrates as one row. Of the 126 most recently added systems, 105 are core and 32 are skill systems; 96 of those core systems have a local loop and 89 close it under a program, and none of the 126 scores 5 on any substrate.

For the 126 most recently added systems, gate types, feedback classes, and governance properties are recorded as explicit columns of the released table, so counts based on those columns apply to those systems. For example, 96 of their 105 core systems have a local loop, and 89 of those close it under a program. This is not a gate count over all 256 systems.

### Evidence and limitations

The evidence ranges from peer-reviewed studies and open-source artifacts to vendor claims. Every row of the released table carries its source and a one-line justification, and the rows for the 126 most recently added systems also carry an evidence tier. Peer-reviewed papers and open-source artifacts receive the greatest weight. A production claim must name a benchmark or integration target, and a blog or interview is counted only when stronger evidence corroborates it. Production claims are not pooled with peer-reviewed evidence in corpus-level statistics; vendor-based exemplars are identified as such.

One author scored all systems. Ambiguous cases were rounded down, and half-scores were used only when one criterion was clearly met and another partly met. Independent re-rating remains future work. The classifications should be read as an auditable interpretation of public evidence, not a complete inventory of private production behavior.

We also test the audit under alternative boundaries: counting rollback as sufficient promotion governance, allowing promotion without governance, and admitting loops that persist only optimizer state. Membership changes under these relaxations, but the principal structural findings remain: [Auto × Auto] stays well populated, the human-local cells hold only curation and registries, Letta alone passes with an ungated promotion, and no relaxation adds governed promotion across organizations (Section REF(sec:gap)). The sensitivity analysis is released with the data notes (Appendix REF(app:data)) and the full score table with the released table (Appendix REF(app:scores)).

## What local adaptation actually closes {#sec:findings}

A system can detect a failure, explain it, and write a plausible correction without ever establishing that the correction helps. SkillForge illustrates this distinction. Its judge agrees with people more than nine times in ten and identifies replies that should be rewritten. Those replies drive updates to the skill, but the updated skill is committed without an acceptance test [@skillforge2026]. The calibration concerns which replies are inadequate. It does not measure the effect of the resulting skill changes.

SkillRL exposes the same separation through a different mechanism. A success-rate threshold triggers proposals for new skills, and the skill bank accepts each proposal unconditionally [@skillrl2026]. Both systems respond to experience, yet neither has the local acceptance gate defined in Section REF(sec:loop). This is why the survey records who accepts an edit separately from who generates it or which signal triggers it.

Among the 105 core systems most recently added to the corpus, 96 have a local loop, and automatic acceptance is nevertheless the dominant pattern among them: 89 use a program to retain or reject changes. Looking inside those loops reveals a less even picture. Evaluation is comparatively mature, while the failure record and the link from a failure to the responsible artifact are often incomplete.

### Finding the right thing to change

A useful failure history must retain what went wrong in a form that supports later comparison. Production memory more often records preferences, successes, or conversation history. Only one field report in the corpus describes a store of dead ends intended to prevent their recurrence, and that evidence comes from a single self-reported deployment [@helwig2026memory]. The persistent store may therefore be extensive while the particular record needed for failure-driven adaptation is missing.

Even when failures are retained, nearly every system uses them in arrival order. Few explicitly choose which recurring modes deserve attention. Task-CoEvolve's variance-weighted task sampling and AutoSaddler's mini-batch failure signals are exceptions [@miyai2026taskcoevolve; @park2026autosaddler]. They weight the experience used for the next update rather than letting the most recent session determine it. The general loop described earlier would prioritize both recurrence and severity; this remains uncommon in the surveyed implementations.

The next step is harder. A failed output does not reveal whether its cause was an instruction, a retrieved memory, a skill, or the route through a group of agents. Harness-optimization papers repeatedly identify this attribution problem as the bottleneck [@lin2026ahe; @zehle2026cantante; @lee2026metaharness; @nguyen2026harnessevo; @liu2026skillsvote]. An evaluation of harness optimizers reaches the same conclusion: by downstream score alone, a harness optimizer cannot be told from trial and error [@ong2026harnesseval].

Existing solutions usually operate within one substrate. Meta-Harness preserves candidate harnesses and the record of which edits helped [@lee2026metaharness]. SkillsVote attributes outcomes to the skill, exploration, or environment before admitting an update [@liu2026skillsvote]. SkillOpt-Lite keeps only the attributes that recur across rollouts, and its ablation finds this consensus mechanism load-bearing [@shen2026skilloptlite]. These methods give the proposal process more useful evidence. None solves the general attribution problem across all six scaffold substrates.

### Testing the candidate

Research systems commonly generate candidates by reflecting on trajectories. In production prompt platforms, an engineer writes the candidate and session feedback never triggers one, while public skill repositories depend on contributors. A field study of five such repositories finds that every substantive edit was committed under a named human account and merged by a person, most carrying an AI co-author trailer [@shen2026whomaintains]. Where proposal generation depends on a person noticing a problem, the evaluation machinery can run automatically while the improvement process itself remains intermittent.

On skills, SAGE and COSPLAY close both local and promotion loops inside a research environment [@wang2025sage; @wu2026cosplay]. SkillChain adds a human reflection decision after the judge, on which refined skills are deployed [@hu2026skillchain]. SkillRL and SkillForge, described above, leave the proposed changes unchecked. These differences would be obscured by classifying all three simply as systems that learn from feedback.

Orchestration has followed a similar progression. Early systems searched for agent topologies under an evaluation score [@zhuge2024gptswarm; @zhang2024aflow]. More recent systems evaluate proposed topology changes before keeping them; TOCOMAS also requires a structural invariant [@chu2026agentgrad; @chen2026harnessforge; @zhao2026tocomas]. OptiMAS is an exception: its optimizer reads trajectories and validation scores to write the next configuration, but the score informs the edit rather than supplying a keep-if-better decision [@cheng2026optimas]. No orchestration system closes both loops with lineage on the promoted artifact.

The most widely deployed artifact remains a useful counterpoint. Instruction files are present across Claude Code, Cursor, AGENTS.md [@agentsmd2025], Windsurf, and Continue.dev, and adoption studies find them in roughly a fifth to a quarter of coding-agent projects [@robbes2026agenticmuch; @galster2026harnessconfig]. Their prevalence does not settle their effectiveness. One controlled study reports higher inference cost without improved task success [@gloaguen2026agentsmd]. Another toggles the root AGENTS.md in paired runs on 124 pull requests and reports about 29% lower median wall-clock time and 17% fewer median output tokens, with total tokens approximately unchanged; it does not measure correctness [@lulla2026empirical]. The studies measure different outcomes and disagree on cost. Neither establishes a general task-success benefit from accumulating instruction files.

Human local gates appear only in curation. VerificAgent uses fact-checked, frozen memories [@nguyen2025verificagent], and in SkillChain a person decides, at a reflection gate, which refined skills are deployed. Prompt platforms and registries without a failure-driven proposal process have no local gate in this classification. Their checks act on release or admission to a shared pool, which belongs to promotion.

### Gathering enough evidence to accept

An acceptance test can itself be too noisy to support a decision from one run. Several newer systems address this directly. SAGE-gate, a statistical acceptance method unrelated to SAGE, uses paired per-item comparisons before committing an edit [@wang2026sagegate]. VaG requires three heterogeneous critics to pass [@shang2026vag]. AutoSaddler uses mini-batch failure signals in validation-based selection [@park2026autosaddler].

These mechanisms should not be conflated. Averaging $k$ independent noisy scores reduces the variance of their mean by a factor of $1/k$. Requiring agreement among $k$ independent checks, each with false-acceptance probability $p$, gives the idealized probability $p^k$. The independence assumptions matter, and actual critics need not satisfy them. Appendix REF(app:gates) distinguishes the gate families and their roles. The shared development is that acceptance increasingly depends on a body of evidence rather than one favorable observation.

### Maintaining the artifacts that survive

The evaluation of a new edit also depends on the artifacts already present. Stale or conflicting skills can cause failures that obscure the effect of the candidate under test. Ratchet reports no gain from model-written skills over a no-skill baseline until lifecycle hygiene is applied, while human-curated skills provide a double-digit gain [@zhang2026ratchet]. Eleven surveyed skill systems now treat removal as an operation that must pass a check, just as admission does [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay] (Appendix REF(app:audit)).

Memory products have made substantial progress on a different part of maintenance: recording an entry's history. Letta's Context Repositories use git, Mem0 retains per-memory history, and Zep represents facts bitemporally [@letta2026memfs; @mem02026history; @zep2026facts]. These records can explain what the system remembers and how that state arose.

History does not guarantee correction. A study of five production backends finds that all five still return facts that were revoked [@shen2026revoked]. The record contains the change, but retrieval does not reliably enforce it. Research systems likewise divide between provenance and write controls [@wang2026toki; @xu2026ppmf; @margalit2026governed; @sun2026vermem] and verifier-gated failure correction [@yu2026recuris; @wang2026memguard]. Cuadros et al.'s governed collaborative memory combines provenance, versioning, and correction, earning the top memory score [@cuadros2026governed].

Reversal has its own limits. SkillSmith and SkillAudit support edit-level rollback [@wei2026skillsmith; @gao2026skillaudit], and EvoUndo rejects edits that cannot be undone [@sah2026evoundo]. VaG finds that reversing a contaminated skill recovers little once other skills have been derived from it [@shang2026vag]. The consequences of an edit may therefore outlast the edit itself. Section REF(sec:failure) returns to this problem when considering promotion and artifact descendants.

### A complete local example

SkillOpt provides a concrete instance of all five conditions [@yang2026skillopt]. Its persistent state is one markdown skill document used by a frozen agent. Rollout and reflection batches supply the failure evidence. A consensus filter helps attribute recurring errors, and bounded add, delete, and replace operations propose changes. A held-out exact-match split supplies the loss, and a candidate is accepted only when its score strictly improves.

Across six benchmarks, seven target models, and three harnesses, SkillOpt is best or tied in every cell reported by its authors. Its follow-up, SkillOpt-Lite, removes a rejected-edit buffer and slow update schedule while retaining the held-out gate and consensus filter; it matches or exceeds the original [@shen2026skilloptlite]. This comparison supports the importance of the gate and this form of credit assignment in that setting, while identifying the removed controls as stabilizers rather than necessities.

SkillOpt also evaluates transfer across models, harnesses, and benchmarks. Those experiments measure how far the learned artifact remains useful. They are distinct from the acceptance decision that admits an edit to the shared skill bank. This distinction becomes central once the same local procedure is used in settings where correctness is harder to measure.

## What the feedback allows a gate to know {#sec:signal}

A coding agent changes a repository rule and receives a test result within seconds. A scheduling assistant changes its booking procedure and learns later whether an appointment was made. A marketing assistant changes its tone instructions and receives a reviewer's preference. A research assistant changes its strategy and may wait months to learn whether the direction was productive.

All four systems can propose a persistent edit. What differs is the evidence available for accepting it. The signal's timing, exactness, and dependence on judgment determine how well a gate can estimate the change in loss. We divide the surveyed systems into four feedback classes, summarized in Table REF(tab:IV-1).

| Class | The signal the gate receives | What the gate can be | What stays hard | Corpus examples |
|---------|------------------------|--------------------|----------------------|--------------|
| C1 exact | A check that returns pass or fail, or an exact score, at once and repeatably: tests, compilers, answer keys | An automatic check, run over enough cases, and enough repeated runs of a stochastic agent, to sample the task mix | The lift is bounded and specific, an improvement in what the check measures on the cases it ran; the check names the failed output, not the coordinate that caused it; a check that is also the target can be gamed | DGM, AlphaEvolve, SkillOpt |
| C2 observable outcome | A real result one episode later: a booked slot, a merged pull request, a closed ticket; noisy and confounded | An automatic threshold over batched episodes; a person at promotion | The outcome says *that* the episode failed, not *why*; the channel can be poisoned | Devin, Sierra, SAGE, SkillRL, PACE, Voyager |
| C3 judged | A rater, a rubric, or a model judge; no ground truth | A judge calibrated against people; a person at promotion | The rubric is itself a scaffold coordinate, so the gate judges edits to itself; the proxy gets optimized past the point where it tracks quality | SkillForge, CASCADE, skills-repository review |
| C4 delayed | An outcome weeks or months later, once per many edits | No immediate per-edit gate; proposals are pruned and milestones stand in until the outcome arrives | Credit across many edits; drift; the loop cannot be told from random search | NanoResearch, CORAL, the AI Scientist |

Table IV-1. The four feedback-signal classes. Reading across a row: what the gate receives, what it can therefore be, and what it cannot fix.

The classes are assigned by the constraint that binds first. A long delay makes a signal C4 even when the eventual outcome is objective. Among timely signals, the absence of an independent ground truth makes the signal C3. Among timely objective signals, repeatable exact checks distinguish C1 from noisy observed outcomes in C2. A system may use several signals, but its operative acceptance decision must be read against the signal that supports it.

### Exact checks: C1

A compiler, proof checker, schema validator, or exact-match answer key can decide a specified property immediately and repeatably. This makes an automatic gate straightforward to implement. AlphaEvolve scores candidates through a cascade of exact evaluators [@alphaevolve2025], and SkillOpt uses held-out exact-match evaluation [@yang2026skillopt]. DGM makes a narrower acceptance decision: it retains self-modifications that pass a sandboxed compile-and-edit functionality check on ten benchmark tasks. The broader benchmark score weights parent selection from the archive rather than determining retention [@zhang2025darwin].

Exactness applies to the check, not to the deployment as a whole. Repeating a deterministic check on the same output yields the same answer, but an agent produces stochastic outputs, and a finite suite samples only part of the task distribution. Estimating the change in patch loss still requires accounting for that variation. Passing the suite also establishes only the properties the suite tests.

Two problems remain even with a reliable checker. A failed test may not identify the instruction or skill that caused the failure, and repeated optimization against the same suite can overfit it. Cheap acceptance can also allow the artifact pool to grow without sufficient pruning. Exact feedback makes evaluation easier; it does not supply attribution or lifecycle management.

### Observed outcomes: C2

A booked appointment, closed ticket, merged pull request, or successful tool call provides an observable result after an episode. The result is meaningful but may be noisy or confounded. A user can accept an incorrect answer or reject a correct one, and a merged pull request reflects more than the agent's technical performance.

Devin reads merged pull requests as feedback [@cognition2025devinreview]. SAGE measures task success in AppWorld [@wang2025sage], and PACE uses failure signals from a deployed small model [@ling2026pace]. SkillRL uses a success-rate threshold only to trigger proposals, without testing whether the proposed skills should remain [@skillrl2026]. The same kind of outcome can therefore support different operations in different systems.

Simulated outcomes, such as those in Voyager's game world or SAGE's AppWorld, remove the user confound and can be sampled repeatedly. They are treated as a distinguishable case within C2. For observed outcomes more generally, an automatic gate needs a positive margin and enough episodes or independent evidence to absorb noise. Even then, the result usually reveals that the task failed more readily than why it failed.

Promotion is harder because another deployment may differ in users, tasks, and acceptance behavior. A sender's successful outcome is not an evaluation of the recipient. This class also depends on channels that can carry poisoned memories or injected tool instructions, connecting the reliability of feedback to the integrity of its source.

### Judgments: C3

For style, persuasion, design, or other preference-dependent tasks, a gate relies on a person, rubric, reference comparison, or model judge. There is no independent exact answer to the preference being measured. CASCADE uses a human-and-agent gate for memory consolidation [@huang2025cascade], and a reviewer approves promotion into Anthropic's skills repository. SkillForge uses its calibrated judge earlier in the process, to identify replies that motivate a rewrite [@skillforge2026].

A program can make these decisions, but its score must be calibrated against the human judgment it is intended to represent before the score is treated as evidence of that preference. The gate labels deliberately do not record this distinction: an uncalibrated model judge is still an Auto gate, though the meaning of its acceptances is less established. SkillForge, SkillChain, and SkillCoach report calibration measurements [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach]; no other surveyed judge does.

Optimization introduces another risk. A scaffold can become better at satisfying the judge while becoming worse at the underlying task. Reward-model research measures this form of proxy overoptimization [@gao2023overoptimization]. Human evaluation is not fixed either: Shankar et al. find that evaluators' criteria change as they grade more outputs [@shankar2024validators]. If the system also edits the rubric, it changes the instrument used to assess subsequent edits. This **reflexive gate** is developed in Section REF(sec:reflexive).

### Delayed and sparse outcomes: C4

Research programs and open-ended discovery may produce meaningful outcomes only after weeks or months and many intervening edits. The AI Scientist illustrates the broad setting by generating ideas, conducting experiments, and writing a paper [@lu2024aiscientist]. The eventual outcome cannot usually be assigned to each preceding scaffold change.

Systems in this class consequently use intermediate decisions. NanoResearch merges skills by semantic compatibility [@xu2026nanoresearch]. CORAL promotes findings into shared memory on a heartbeat [@qu2026coral]. These operations can prune or consolidate proposals, but they do not estimate each edit's contribution to the eventual loss. AlphaEvolve's archive diversity does not make it a delayed-signal example: its candidates have already been scored by exact evaluators, so archive selection is a search strategy within C1 [@alphaevolve2025].

For C4, the descent interpretation applies only to whatever proxy gate is available or to an evaluation at the longer horizon. Temporal credit assignment remains unresolved, and the environment can change before the result arrives. Outcome gains alone are also insufficient to distinguish directed improvement from a successful search, a limitation emphasized in the evaluation of harness optimizers [@ong2026harnesseval].

### Consequences for the two loops

The classification yields three expectations that can be checked against the corpus. First, local automatic acceptance is most directly supported by exact checks and observed outcomes. Judged acceptance depends on calibration, while delayed feedback cannot evaluate edits individually until the outcome arrives. Second, automatic promotion that estimates a loss change should occur only where a comparable check can be applied at the recipient, in exact and re-runnable simulated settings, and human promotion should hold the observed outcomes and judgments. Delayed feedback supports no immediate per-edit gate on either half. Third, the main failure risks should differ: overfitting to a suite and bloat under exact feedback, corrupted outcome channels under C2, proxy optimization under C3, and drift under C4.

These are expectations about the evidence a gate can establish, not restrictions on whether software can execute a decision. A program can merge two judged artifacts or prune a delayed proposal without estimating a loss change. Section REF(sec:design) makes this qualification explicit in the gate grid. In every class, sharing remains an additional empirical question: even the same exact checker must be applied to the recipient's relevant cases before broader performance is established.

## When a local improvement is shared {#sec:design}

A rule can be useful in one repository and inappropriate in the next. Copying the file transfers the instruction, but not the evidence that justified it. The recipient must either share the relevant evaluation conditions or test the change on its own workload. This is the additional decision that separates local adaptation from promotion.

### Scope and receiving-side evaluation

We distinguish five nested scopes. **USER** covers one person's account or fork. **PROJECT** covers a repository, workflow, or product workspace. **STACK** is a team's curated bundle of projects. A **TENANT** is an organization or customer, and **CORE** is the scope shared by all tenants. A wider scope aggregates the losses of the deployments it contains. Promotion changes which population the edit is intended to improve, as shown in Fig. REF(fig:scope).

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\textwidth]{figures/fig2_scope}
\caption{Promotion scopes, from a user account to the shared core. Wider adoption changes the population on which an edit acts. Receiving-side evaluation checks whether the improvement is supported for the recipient.}
\label{fig:scope}
\end{figure}
```

The nesting makes an important limit visible. A lower average loss at a broad scope can conceal harm to an individual recipient. The proposed architecture in Section REF(sec:gap) therefore includes a held-out check at the receiving tenant. Versioning and access control govern whether an edit may be delivered and reversed; receiving-side evaluation tests whether it should be used there.

Several systems already evaluate transfers within one operator. ShareMem consolidates memories from one user for another and evaluates them in the receiving context [@hu2026sharemem]. XRepoSkill verifies a rule in at least two repositories [@guo2026xreposkill]. Evo2Team promotes routing skills between teams and confirms them at the target [@wang2026evo2team]. These are concrete instances of evidence being gathered beyond the source deployment.

Federated systems place the check elsewhere. EvolveNet merges a shared harness only when the merge fixes at least as many held-out items as it breaks, but that check occurs at the aggregator [@nie2026evolvenet]. FederatedSkill's server agent applies, adapts, or rejects each client's edit and records the decision [@yang2026federatedskill]. Their clients are partitions or agent instances under one operator, not independently governed customer organizations. They do not instantiate a receiving-organization gate.

The location of the evaluation matters, and its coverage still matters after it is correctly located. ShareMem, XRepoSkill, and Evo2Team check the receiving context; EvolveNet checks the shared merge; FederatedSkill records a server decision. Even in Evo2Team, nearly a fifth of confirmed transfers fail on graphs not covered by confirmation. A receiving-side check provides necessary evidence for adoption, but finite evaluation does not guarantee performance on all future tasks.

### Automatic, human, and unchecked promotion

Research systems often promote by admitting a candidate to a bank or archive that later runs reuse. SkillOpt, DGM, ADAS, Voyager, and SAGE apply programmatic decisions within this shared environment [@yang2026skillopt; @zhang2025darwin; @hu2024adas; @wang2023voyager; @wang2025sage]. AlphaEvolve and its predecessor FunSearch score candidates before archive admission [@alphaevolve2025; @romeraparedes2024funsearch]. AlphaEvolve has produced gains used within Google, but it is a research loop within one operator, rather than a product for governed sharing between organizations. That pool is as far as any of them travels, and none has access control, audited promotion, or a gate at a receiving organization.

Not every automatic admission has the same evidentiary meaning. NanoResearch's semantic merge, AutoManual's judged rewriting and consolidation, and ShareMem's judged consolidation are programmatic decisions, but none of them estimates a candidate's reduction in patch loss. The distinction anticipated by the feedback classes is therefore essential: an automatic promotion decision can exist where a per-edit improvement estimate does not.

Production systems more often retain a person at the promotion decision. Sierra routes generated insights through human-authored expert answers [@sierra2025os20]. In Devin, the same pull-request merge serves two roles: it supplies an observed outcome to local adaptation and records the reviewer's approval for the persistent repository [@cognition2025devinreview]. Spotify's optimized prompts and plans enter production after online A/B testing and a launch decision [@palumbo2026spotify]. CASCADE also combines human and agent approval for memory consolidation [@huang2025cascade]. In each, the person at the promotion gate stands in for the exact signal production lacks, which makes a program on the local gate with a person on the promotion gate the production-viable pairing rather than a compromise.

Letta's Context Repositories take a different path. Locally, background reflection writes memory edits and merges them back automatically; the only check on a local edit in the released evidence is an optional agent review before the edit is applied, which is the basis for its Auto local gate, and with that option off the system would sit in [None × None]. Shared-memory changes are then pushed with git lineage but without an acceptance check. The record explains what was shared, while leaving whether it should have been shared unresolved. In many other systems, promotion is absent altogether. AutoAgent, for example, revises the tool and peer descriptions of one agent without propagating those revisions to another deployment [@wang2026autoagent]. Both cases receive None at the promotion gate, but for different reasons: one shares without checking; the other does not share.

### What formats, registries, and release platforms provide

Much of the infrastructure needed for sharing already exists independently of these learning loops. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit use git-tracked markdown artifacts attached to workspaces, with a tool layer organized around MCP-style interfaces [@galster2026harnessconfig; @barbaste2026harnessengineering]. This convergence makes artifacts easier to carry between runtimes. A study of repository-level loops nevertheless finds that the runtime state of the adaptation process remains outside version control [@lulla2026loopengineering]. The portable file does not necessarily carry the history that produced it.

Public repositories provide a shared scope with human admission. In a study of five skill repositories, every substantive change was committed under a named human account and merged by a person; only one of 254 edits deprecated a skill [@shen2026whomaintains]. MCP registries provide namespaces and version records, while control planes add scanning, access control, or quarantine [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. Governance registries add lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed]. EDDOps gates promotion on evaluation thresholds before a human sign-off, but none of these registries generates candidate artifacts from failures.

Braintrust, Vellum, and LangSmith Hub likewise provide immutable versions, evaluation thresholds, and rollback [@braintrust2026docs; @vellum2026docs; @langsmith2026hub]. Engineers author the candidates, and evaluations can block a regressing release. In the surveyed descriptions, session feedback does not trigger candidate generation or the release process. These platforms supply much of the machinery for controlled change without closing the failure-driven local loop.

### The two decisions viewed together

Fig. REF(fig:design) places the local and promotion gates on a common grid. Table REF(tab:VII-1) summarizes the occupants and their signals. The grid distinguishes a system that generates and tests improvements from one that distributes human-authored artifacts under admission control, while allowing their complementary capabilities to be compared.

```{=latex}
\begin{figure}[htbp]
\centering
\includegraphics[width=0.52\textwidth]{figures/fig3_design_space}
\caption{Local and promotion gates. Each axis records who accepts a change: a program, a person, or no gate. None includes both absent promotion and unchecked sharing; the text distinguishes these cases.}
\label{fig:design}
\end{figure}
```

| Cell | Who keeps the local edit, who lets it climb | Who is there | Signal found there |
|--------------------|------------------------------------|--------------------------------------|------------------------------|
| [Auto × Auto] | A program keeps it; a program lets it climb | Research systems that close both halves inside one environment or one operator | Exact and simulated outcomes; delayed and judged only under pruning or merging |
| [Auto × Human] | A program keeps it; a person lets it climb | Production systems with a reviewer on promotion, and CASCADE | Observed outcomes and judgments |
| [Auto × None] | A program keeps it; nothing lets it climb | Letta's ungated push; systems that promote nothing | As on the local gate |
| [Human × None] | A person keeps it; nothing lets it climb | Curation | Judged |
| [None × Auto] | No failure triggers a candidate; a threshold gates release | Prompts-as-code platforms and governance registries | No failure-driven loop |
| [None × Human] | No failure triggers a candidate; a person admits | Open standards, MCP registries, community hubs | No failure-driven loop |
| [None × None] | Nothing checks or promotes the edit | SkillRL and SkillForge, unchecked skill loops | Outcomes and judgments |

Table VII-1. The gate grid read cell by cell: who keeps a local edit and who lets it climb, which systems sit in the cell, and the feedback signal they gate on. [Human × Auto] and [Human × Human] hold no surveyed system.

Among [Auto × Auto] systems whose promotion gate estimates a loss change, the operative signals are exact checks or simulated outcomes. The judged and delayed cases use pruning, rewriting, or merging rather than that estimate. [Auto × Human] contains observed outcomes and judgments, with no exact-signal system in the surveyed cell. These patterns match the feedback-based expectations once the meaning of automatic admission is made explicit.

The [Human × Auto] and [Human × Human] cells are empty in the surveyed set: no system combines a human local gate on a failure-driven loop with subsequent promotion. Human local decisions occur in curation. The bottom row includes comparison systems without a failure-driven local loop, such as prompt platforms, registries, and community hubs including Buildrix [@jiang2026buildrix]. SkillRL and SkillForge occupy [None × None] because their failure-driven skill updates, new skills in SkillRL and rewrites in SkillForge, are kept unchecked.

The audit's boundary cases do not change this structure. Of six systems that promote without artifact lineage, five have sufficient evidence under the tier rule and enter already occupied cells when the audit is relaxed; Spotify is one of them. The sixth, Future AGI's prompt lifecycle, has only uncorroborated T5 evidence. No relaxation yields governed promotion across organizations. What the grid reveals is a division of capabilities: no system has both the learning of the top row and the governance of the bottom row.

## How adaptation can undermine its own evidence {#sec:failure}

An improvement loop changes the context in which its next decision is made. New rules can conflict with old ones, a corrected memory can still be retrieved in its earlier form, and a frequently reused evaluator can become a target. These failures extend the technical-debt concerns identified for machine-learning systems by Sculley et al. [@sculley2015debt]. The literature documents six of these failures in a measured case; a seventh, overfitting to one deployment, follows from the scope of the loss rather than from a measurement. Table REF(tab:X-1) connects each to the control that addresses it.

| Failure | What goes wrong | The loop piece that answers it | Dominant class |
|------------|------------------------------|------------------------------|----------|
| Scaffold bloat | Rules and skills accumulate until the model follows them worse and the gate has no clean signal | Complexity penalty $\Omega$ in the gate; pruning and expiry as first-class gated operations | C1, C3 |
| Poisoned memory | An attacker writes an entry that later retrieval trusts | Provenance on every entry; write gating; a rollback envelope | C2 |
| Injection via tools and MCP | A tool's output or a connected server carries instructions into context | Narrow tool permissions; a privilege hierarchy over instructions; tool bindings pass the same promotion gate as any other coordinate | C2 |
| Evaluation fragility | The suite that gates edits is itself edited, gamed, and read non-independently | Held-out evaluations scoped within evidence radius, weighted toward recurring modes, re-read as the target drifts, checked against attribution | C3 (primary), C1 |
| Coordination failures | Multi-agent roles blur and context is lost between agents | Orchestration topology treated as a scaffold coordinate under the same gate and rollback discipline | C2 |
| Patch overfitting | A scaffold tuned to one deployment degrades another | Evidence-radius discipline at promotion; receiving-side held-out evaluation | C2 |
| Plasticity loss | Old rules, polluted memory, and drifting tool versions crowd out adaptation | Expiry and rollback as explicit loop operations rather than retrospective hygiene | C4 |

Table X-1. The failure surface of patchwork scaffold maintenance: what goes wrong, the piece of the loop that answers it, and the feedback-signal class in which it dominates.

### Accumulation and contamination

As instructions accumulate, following them becomes harder and latency increases [@jaroslawicz2025ifscale]. Ratchet's finding that model-written skills need lifecycle hygiene before producing gains makes the consequence visible at the system level [@zhang2026ratchet]. Conflicting or obsolete artifacts also complicate attribution: an evaluation may detect failure without revealing whether the cause is the new candidate or an older artifact. Gated retirement, pruning, and expiry preserve the conditions under which a new edit can be meaningfully assessed.

Persistent memory creates another route to lasting error. PoisonedRAG demonstrates attacks on retrieved knowledge [@zou2024poisonedrag], AgentPoison plants backdoors in long-term memory or knowledge bases [@chen2024agentpoison], and memory control-flow attacks operate across major agent frameworks [@xu2026mcfa]. Tool outputs and connected servers can also insert instructions into the model's context [@greshake2023injection; @debenedetti2024agentdojo]. In CVE-2025-54136, a previously approved MCP configuration could be changed without renewed approval [@checkpoint2025mcpoison].

These failures motivate provenance, write gating, and reversible memory changes [@su2026chronomem; @yu2026rollbackrepair], together with restricted tool permissions and an instruction privilege hierarchy [@wallace2024hierarchy]. The tool binding itself must be subject to controlled revision. Checking only the initial registration leaves later changes outside the decision that authorized it.

Rollback also needs to account for derivation. If a contaminated skill has been used to create other skills, restoring its earlier version does not remove those descendants. VaG's limited recovery after such rollback [@shang2026vag] supports checking contamination before commitment and tracking consequences after it. A version history is a prerequisite for this work, but it does not perform the recovery by itself.

### When the evaluator changes {#sec:reflexive}

Consider a pitch-review assistant that consistently overrates decks claiming a large market without supporting numbers. The team revises its rubric from "evaluate market size" to "require a numeric estimate and a source." The edit may improve reviews, but it also changes the standard used to evaluate subsequent behavior. If the same rubric judges future rubric revisions, the improvement process is modifying its own measuring instrument.

This is the reflexive-gate problem introduced with C3 feedback. The survey finds three scaffold systems reporting calibration of a judge against people: SkillForge, SkillChain, and SkillCoach [@skillforge2026; @hu2026skillchain; @zhu2026skillcoach]. SkillCoach also evaluates a judge after editing it: offline, it compares its initial and evolved rubrics against human-gold references on 50 paired instances from 10 held-out task families, and trajectory-filtering consistency rises from 82% to 96%, an audit its authors describe as judge-assisted rather than a new human annotation study [@zhu2026skillcoach]. No surveyed system reports calibration maintained across continuing rubric revisions and deployment drift. The missing result is therefore more specific than an absence of calibrated judges. It concerns keeping calibration while the criterion keeps changing.

Weight-level reinforcement learning has encountered a related problem in extending verifiable rewards to open-ended tasks. Some methods hold the judge fixed, using checklists, pairwise preferences, references, or rubrics [@gunjal2025rubrics; @jia2025writingzero; @shi2026references; @jin2026rlaes]. Others update the reward, rubric, or judge alongside the policy [@yu2025rlpr; @xu2026rubricarm; @ding2026evorubrics; @zhu2026score; @li2026rubricem]. Among the co-evolving methods reviewed, only RLPR reports agreement with human labels, and its reward is a probability rather than a rubric. The comparison is tabulated in the audit notes (Appendix REF(app:audit)); these weight-side methods are not included in the scaffold scores.

Even a fixed evaluator can become unreliable through repeated use. Optimizing a proxy beyond a point can reduce the underlying quality [@gao2023overoptimization]. Unequal exposure to evaluation data can create apparent performance gains [@singh2025leaderboard]. Evaluations of agent trajectories are also path-dependent, and deployment tasks drift while the suite remains fixed. Human criteria themselves can shift during grading [@shankar2024validators]. Consequently, a gate needs its own held-out checks, calibration where judgment is involved, and revision history.

The failure-mode hypothesis discussed in Section REF(sec:why) adds a conditional implication: if deployment failures concentrate in recurring modes, uniformly sampled tasks may underrepresent the modes that most need correction. Evaluation should then include those modes while preserving a held-out assessment. The requirement is broader than improving a benchmark score: score alone cannot tell a harness optimizer from trial and error [@ong2026harnesseval], so the evaluation must also test the claimed link between failures and edits.

### Scope, coordination, and drift

Some failures arise from the structure of the deployment. A study of multi-agent systems identifies fourteen failure modes, prominently including role confusion and context lost between agents [@cemri2025mast]. Treating routing and role assignments as editable scaffold coordinates makes them subject to evaluation and rollback alongside instructions and skills.

Specialization creates a related boundary. A scaffold adapted to one deployment can degrade another because the tasks and preferred behavior differ. Receiving-side evaluation limits this risk at promotion; the evidence radius records where the improvement has been tested. This does not eliminate uncertainty outside the evaluated cases.

Finally, the scaffold can become less adaptable as old rules, polluted memories, and drifting tool versions accumulate. Long-context degradation [@liu2023lostmiddle] provides one related mechanism. Expiry, pruning, and rollback must remain available throughout the system's lifetime, especially when delayed feedback arrives too slowly to keep the artifacts current.

The feedback classes help organize these risks without making them exclusive to one class. Exact checks invite suite overfitting and cheap accumulation; observable outcomes depend on channels vulnerable to poisoning and injection; judged feedback is exposed to proxy optimization and moving criteria; delayed feedback makes drift difficult to correct promptly. Production systems provide individual controls, but the surface stays largely unmitigated because no surveyed system runs them together.

## What governed sharing would require {#sec:gap}

The evidence so far identifies a practical integration problem. Local optimizers can propose and test changes. Release platforms can version artifacts and reverse deployments. Registries can govern admission and access. The surveyed systems do not connect these capabilities into a process that learns in one organization and shares the resulting improvement with another under equivalent controls.

We audit that missing combination through four properties:

(a) **An auto-gated local loop:** an algorithmic acceptance criterion tests a proposed artifact change.
(b) **Cross-organization promotion:** artifacts can be promoted between independently governed organizations or customers.
(c) **Versioned lineage with access control:** a promoted artifact carries its history and audit trail, with policies controlling who may access it.
(d) **Rollback:** a harmful promotion can be reversed without redeploying the whole system.

The terms *cross-tenant* and *cross-organization* refer to the same boundary here. Sharing among agents, users, or benchmark partitions within one operator does not establish property (b).

Table REF(tab:IX-1) compares the closest systems. FederatedSkill combines local adaptation with semantic skill exchange and an auditable server decision log [@yang2026federatedskill]. EvolveNet evaluates shared merges and can return to the previous shared harness [@nie2026evolvenet]. Both remain within one operator. Governance registries supply lineage and rollback without a local learning loop, and MCP control planes supply access control alone. Rollback exists inside one federated round and inside single deployments; no system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion.

| System | (a) auto-gated local loop | (b) cross-organization promotion | (c) versioned lineage with access control | (d) rollback |
|--------------|------------------|----------------------|--------------------|----------------|
| FederatedSkill [@yang2026federatedskill] | full | partial: privacy-preserving aggregation of skill edits across heterogeneous clients that sit under one operator | partial: auditable per-modification decision log | none |
| EvolveNet [@nie2026evolvenet] | full | partial: held-out merge gate at the aggregator, but clients are benchmark partitions, not organizations | none: no lineage, no access control | full: rollback to the previous shared harness after a failed round |
| SkillForge [@skillforge2026] | none: a calibrated judge selects the failures, nothing tests the rewrite | none: skill versions stay in the scenario deployment | partial | not documented |
| Governance-first registries [@kang2026registry; @qin2026governed; @quessadavial2026acm] | none: no inner loop | none | partial: lineage without access control | full, with evidence |
| MCP control planes [@agenticcommunity2026mcpgateway] | none: no inner loop | none | partial: access control without lineage | not reported |

Table IX-1. The closest approaches to governed cross-organization scaffold optimization, scored against the four properties.

Receiving-side evaluation is an additional requirement on the promotion decision. It is kept separate from the four-property audit, which records loop, scope, and governance capabilities. A system could satisfy those capabilities while still making an unsupported decision about whether an artifact benefits its recipient.

An architecture that addresses both would contain five connected parts: per-tenant artifact pools with provenance; an aggregation or selection process that respects tenant isolation; held-out evaluation at the receiving tenant; versioned lineage and access control; and a defined reversal path for each promoted artifact. The recipient's check would reject a promotion that does not lower its own patch loss. VaG's result (Section REF(sec:findings)) suggests that the rollback envelope would also need to track an artifact's descendants.

Federated learning offers a useful comparison, but the representation being shared is different. FedAvg combines comparable numeric updates, and its privacy and deployment problems have been extensively studied [@mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated]. Federated prompt tuning moves the learned object to a shared prompt [@guo2022promptfl]. The nearest scaffold systems instead select, revise, or merge symbolic edits, often through a language model. Averaging is an appropriate analogy only where the artifact updates have a mergeable representation.

The extent of automation should depend on the feedback. Exact checks provide the most direct setting for testing a transferred skill, although the recipient still needs relevant test cases. Observed outcomes require evaluation on the recipient's workload because the sender's outcome is not portable evidence of success. Where quality is judged, a human promotion gate is a reasonable design choice, supported by lineage and rollback. Delayed outcomes cannot support an immediate per-edit automatic local gate of the kind property (a) describes; those systems still benefit from provenance and reversibility around proposals and milestones.

Thus the four properties define a target for the settings that can support an automatic local gate. They should not be interpreted as a requirement to automate every decision in every domain. The common requirement is that the evidence attached to an edit remain meaningful where it is used, and that the system preserve the ability to inspect and reverse its adoption.

## How the research lines fit together {#sec:families}

The uneven architecture has a history. Different research communities began with different problems: improving prompts, learning in context, selecting agent workflows, maintaining skill libraries, or transferring experience. Each developed the part of the loop most relevant to its initial problem. Table REF(tab:VIII-1) places five such lines side by side.

| Research line | Started from | The part of the loop it built | What it leaves open |
|------------|--------------------|------------------------------|------------------------|
| Reflective evolution | Prompt optimization and continual learning | Condition 4, the candidate: proposal by reflection over trajectory evidence; the two-timescale case for editing outside the weights | A persistent artifact; a bounded step; a held-out gate |
| Reflective context | Learning in context as a setting of its own | Condition 5, the penalty: the learned object in context space; a generalization penalty, the $\Omega$ of the gate | A cross-deployment promotion loop |
| Harness optimization | Orchestration and harness engineering | Condition 3, the trace: attribution of a failure to one slot of the orchestration graph; source-level edits | Attribution across substrates; a governed promotion loop; access control; rollback |
| Lifecycle and multi-objective | Skill pools that bloat under platform limits | The gate on removal: gated retirement; hygiene as a precondition; a hard frontier as the shape of $\Omega$ | Closing the loop as descent; retiring a promoted artifact's descendants |
| Transfer and federation | How far an edit travels | The promotion loop, the check on arrival: evidence radius measured one task at a time; cross-client aggregation; receiving-side confirmation | A cross-organization gate, lineage, and rollback |

Table VIII-1. Five research lines converging on artifact-layer descent: the problem each started from, the part of the loop it built, and what it leaves open.

Prompt optimization and reflective evolution developed ways to propose edits from trajectory evidence, together with an argument for adapting artifacts on a faster schedule than weights [@agrawal2025gepa; @tiwari2026fastandslow]. Reflective Context Learning formalizes learning in context and the need to control generalization, corresponding to the complexity penalty in the acceptance rule [@vassilyev2026rcl]. Harness optimization treats source-level orchestration changes as the learned object and repeatedly identifies attribution as its difficult step [@lee2026metaharness; @lin2026ahe; @cai2026moss; @zehle2026cantante; @nguyen2026harnessevo; @chen2026harnessforge; @li2026growingharness].

The lifecycle literature starts from a different constraint: skill pools can become too large or internally inconsistent to remain useful. Its contributions include evaluated retirement, hygiene, and optimization under platform limits [@zhang2026ratchet; @tanjim2026mocha; @liu2026skillsvote; @zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay]. Transfer and federation ask how far a learned artifact remains useful, progressing from cross-task measurements to receiving-team confirmation and shared client updates [@shalev2026ict; @li2026combee; @qu2026coral; @ling2026pace; @wang2026evo2team; @yang2026federatedskill; @nie2026evolvenet].

This history helps explain why evaluation and proposal mechanisms are more developed than failure capture. Each research line inherits its loss from its benchmark and begins with available trajectories. Building a record of recurring failures was none of their starting problems. Attribution receives substantial attention, but usually within the substrate a particular line studies. The local loop has consequently developed from evaluation backward toward the evidence needed to choose a useful edit.

The convergence supports a shared decomposition of the system into weights and editable artifacts. GEPA, Meta-Harness, MOSS, RCL, PACE, and the harness-optimization papers all use it. A system that updates both, SIA, still treats them as separate levers [@hebbar2026sia]. The convergence does not establish that one architecture is optimal, and none of these lines documents the complete cross-organization process. It shows that different starting problems repeatedly lead to comparable mechanisms for proposing, testing, retaining, and reusing changes.

### Why specialization remains outside the weights {#sec:why}

A general model and a particular deployment face different requirements. The model must work across many settings. A deployment must follow its own conventions, honor its users' preferences, and avoid failures that may be rare globally but frequent locally. The scaffold provides a place to encode those requirements with a scope narrower than the model's entire user population.

Work on reinforcement learning from human feedback reports reduced output diversity and more homogeneous preferences [@kirk2024understanding; @padmakumar2023diversity]. This helps motivate the distinction between broad model behavior and customer-specific requirements. Tiwari et al. approach it from adaptation cost: in-context changes are cheap but capacity-bounded, while in-weight adaptation is more expressive and can introduce forgetting and loss of plasticity [@tiwari2026fastandslow; @dohare2024loss].

Per-customer adapters [@hu2021lora], distilled models, and learned routing can absorb some local requirements. They also introduce separate training, evaluation, and serving lifecycles. Persistent artifacts offer the cheaper path: they are inspectable, reversible, scoped to one customer, and updatable daily.

Two earlier papers in this series offer a hypothesis for why targeted artifact changes may be effective. *Beyond Exponential Decay* argues that long-output reliability depends on a sparse set of key decisions rather than a uniform error probability at every token [@arbuzov2025beyond]. Its evidence includes long-range dependence measured on one natural-text corpus, where fewer than a tenth of tokens depend on distant context, and the accuracy recovered through majority voting on reasoning benchmarks. Its argument is limited when the number of consequential decisions grows with the task, as in long-horizon agentic work.

*The Architecture of Errors* considers a bounded deployment with recurring tasks, tools, and evaluator expectations [@arbuzov2026architecture]. It argues that failures there fall into a catalogue of modes whose size grows slowly with observed experience. Under its assumptions, the intervention budget grows polylogarithmically with sequence length and becomes constant once the catalogue saturates. Its negative result is equally relevant: a finite catalogue cannot cover an unbounded domain.

If these hypotheses generalize, a deployment may be improved through a manageable set of targeted interventions. Persistent rules, memories, skills, and tool changes provide an inspectable representation for those interventions. On that hypothesis the gated and scoped artifact layer is not a workaround for an inadequate model but the architecture the error structure calls for: a frontier model that generalizes, a local scaffold that specializes, and reliability that comes from governing the specialization. The survey does not test the hypotheses; its findings about acceptance gates, feedback, and promotion follow from the corpus independently of them.

### Relation to neighboring surveys

Existing surveys organize the field around agent evolution, persistent state, context engineering, skills, memory security, and harness design. This survey follows a different unit of analysis: the decision that accepts a persistent change, the feedback supporting that decision, and the scope in which the change is subsequently used. Table REF(tab:II-2) records the distinction for each neighboring survey.

| Survey | Scope | How this survey differs |
|-------------|---------------|----------------------------------------------|
| Gao et al. [@gao2026selfevolving] | self-evolving agents | organizes by what, when, how, and where an agent evolves; the gate that accepts an edit, and the edit's scope, are mentioned but not classified |
| Fang et al. [@fang2025comprehensive] | self-evolving agents | organizes by inputs, agent system, environment, and optimizer; loop closure appears in passing, gates and promotion do not |
| Zhou et al. [@zhou2026selfevolvingcoding] | self-evolving coding agents (108 methods) | organizes by evolution target, timing, and code signal; closest on reversibility, with no gate or promotion axis |
| Ding et al. [@ding2026alwayson] | persistent-state agents (435 works) | organizes by authority, scope, mutability, provenance, and recoverability of state; governance is an axis, the gate on an edit is not |
| Lin et al. [@lin2026memorysecurity] | memory security (~90 works) | organizes by lifecycle phase and security objective; principal scoping and rollback are axes, feedback and promotion are not |
| Guo et al. [@guo2026harness] | agent system and harness design | organizes by six runtime responsibilities; touches all four questions without classifying by any |
| Xia et al. [@xia2026harnessing] | skill-mediated agents (8 systems) | organizes by four responsibility layers and ten patterns; loop closure and governance appear as patterns, not as axes |
| Ding et al. [@ding2026skilleval] | skill evaluation and evolution | organizes by four evolution paradigms and six benchmark classes; evaluation is the subject, the gate it feeds is not |
| Mei et al. [@mei2025context] | context engineering (1,411 papers) | organizes by components and system implementations; adaptation loops lie outside its scope |

Table II-2. Neighboring surveys and where this one departs from each. This survey classifies by loop closure, gate type, signal class, and governance, and is the only one to cover promotion across organizations.

The closest governance precedents are Ding et al.'s survey of persistent-state agents and Lin et al.'s memory-security survey [@ding2026alwayson; @lin2026memorysecurity]. The former finds greater attention to accumulating and retrieving state than to governing, recovering, or relinquishing it. The latter treats scoping and rollback as security primitives. Neither asks who gates an edit, and neither covers promotion across organizations.

Prompt optimization supplies another important lineage: OPRO, EvoPrompt, Promptbreeder, DSPy, and TextGrad optimize a prompt or program once against development evidence and are not deployed loops [@yang2023opro; @guo2023evoprompt; @fernando2023promptbreeder; @khattab2023dspy; @yuksekgonul2024textgrad]. ACE persists an evolving playbook but never promotes it [@ace2025agentic]. Agent symbolic learning treats prompts, tools, and pipelines as symbolic parameters [@zhou2024symbolic]; STOP improves its own scaffolding program [@zelikman2023stop]; and SICA edits its harness to improve benchmark performance [@robeyns2025sica]. These works establish many of the underlying mechanisms.

The contribution here is their joint reading at deployment scope: whether an artifact persists, whether a local acceptance decision is made, which signal supports it, and what authorizes use elsewhere. The 256-system corpus, two-loop classification, feedback classes, and governance audit make that comparison explicit. An extended discussion separates these contributions from their precedents (Appendix REF(app:related)).

## Open problems and conclusion {#sec:open}

The remaining problems become more specific when expressed in terms of the decisions a deployment must make.

**Attributing a failure to an editable cause.** An exact check can establish that an output failed without identifying the instruction, memory, skill, or tool binding responsible. No surveyed method solves this across all substrates. Slot attribution [@nguyen2026harnessevo], intervention-based attribution [@chu2026agentgrad], and contrastive multi-agent attribution [@zehle2026cantante] provide narrower starting points. Observed outcomes make the problem harder because their causes are more confounded.

**Establishing improvement at the recipient.** A transferred artifact must be evaluated against the receiving deployment's tasks and measure. Existing receiving-side checks show that this is feasible in selected settings, while Evo2Team's failures on unseen graphs show its coverage limits. Federated Agent Optimization proposes a receiving-client gate but does not implement it [@yang2026fao]. Connecting such checks to provenance, access control, and reversal remains an architectural problem.

**Maintaining calibration while the criterion changes.** For judged tasks, the open question is how to keep a judge aligned with people across continuing revisions of the rubric it applies. SkillCoach shows that an evolved rubric can be audited offline against human-gold references [@zhu2026skillcoach]; no surveyed scaffold system reports calibration maintained through repeated revisions in deployment. The neighboring reward literature also lacks a reported human-agreement result for a co-evolving rubric or judge, with RLPR's probability-based reward a distinct case. A useful solution must evaluate the moving criterion as well as the outputs it scores.

**Evaluating improvement with delayed outcomes.** When many edits occur before a meaningful result arrives, immediate per-edit acceptance is unavailable. Proxy milestones and proposal pruning may still be useful, but downstream gains alone do not establish successful attribution. Harness optimizers should therefore be assessed against their claims about why particular edits help, as well as their final scores [@ong2026harnesseval].

**Connecting local learning to governed sharing.** No surveyed system combines automatic local acceptance, promotion across organizations, versioned lineage with access control, and rollback. The components exist in different systems. Their integration must preserve tenant isolation, evaluate the recipient, and account for artifacts derived from a change that is later withdrawn. Where feedback cannot support automatic acceptance, the design must retain the corresponding human decision or delayed evaluation.

The survey's central observation is that persistent changes outside the weights have become an important form of adaptation, while the evidence supporting those changes remains fragmented. Many systems can test a local candidate. Fewer can reliably explain which recurring failure it addresses, and the machinery for transferring the resulting improvement to another organization has not been assembled in the public systems examined here.

The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization: knowing what each change improved, where that evidence applies, and how the change can be reversed. That discipline must extend to the evaluations themselves when they become part of the adapting system.

## Acknowledgments {-}

The authors used an AI assistant (Claude, Anthropic) to help search the literature, check citations, and edit prose; all claims, scores, and classifications were reviewed and approved by the authors.

```{=latex}
\bibliography{references}
\appendix
```

## Formal statement of artifact-layer descent {#app:formal}

This appendix states the setup behind Section REF(sec:loop), a one-step descent inequality under a noisy gate, an informal convergence proposition, the optimization-analogy correspondence, and four worked cases. No new theorem is claimed; the proposition is the ordinary target of local stochastic optimization under noisy estimators, restated for a discrete, versioned parameter.

| Optimization concept | Scaffold analogue |
|--------------|----------------------------------------------|
| Parameter vector | Instructions, skills, memories, tools, routing graphs, and governance rules, evaluation gates among them |
| Loss | Failure, user correction, evaluation regression, retrieval miss, tool error, schema violation |
| Gradient estimate | Credit assignment identifying the coordinate responsible for a failure |
| Step | Accepted scaffold edit; step size is edit magnitude under $\oplus$ |
| Aggregated update | Several recurring failures combined before an update, by averaging or by agreement across $k$ proposals |
| Update radius | Promotion scope: which loss is descended (USER, PROJECT, STACK, TENANT, CORE) |
| Validation loss | Held-out patch evaluation before merge |
| Regularization | Complexity penalty $\Omega(z)$, bloat control, cross-patch regression checks |
| Overfitting | Scaffold improves on this deployment and degrades elsewhere |
| Rollback | Reverting a harmful accepted update |

Table A-1. Optimization concepts and their scaffold analogues.

### Setup

Let the frontier model have fixed parameters $\theta_M$ and let the scaffold be a structured object $\theta_s \in \Theta_s = \Theta_1 \times \cdots \times \Theta_6$ over the six substrate coordinates of Section REF(sec:method); $\Theta_s$ is discrete, symbolic, and versioned. For a deployment $D$, $L_D(\theta_s) = \mathbb{E}_{x \sim D}[\ell(\pi(\theta_M, \theta_s, x))]$. A candidate edit $z_t \sim Q_t(z \mid H_t, \theta_s^t)$ is drawn from a proposal process conditioned on the accumulated history $H_t$ of failures, corrections, rejected outputs, evaluation regressions, and prior accepted edits. $Q_t$ is not uniform: for a mode $m$ that recurs with frequency $f_m$ and carries per-occurrence loss $s_m$, its expected contribution to the failure rate is $f_m s_m$, so high-frequency or high-severity modes are proposed first. The finite directional difference is $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$; the gate sees only a noisy estimate $\widehat{\Delta}_z L_D$. The update is
$$\theta_s^{t+1} = \theta_s^t \oplus z_t \text{ if } G_t(z_t) = 1, \quad \theta_s^{t+1} = \theta_s^t \text{ otherwise.}$$

### Descent inequality

Write $\mathcal{F}_t$ for the history up to step $t$: the failures, corrections, edits, and gate decisions in $H_t$ together with $\theta_s^t$. Because the proposal $Q_t$ depends on the whole history and not on $\theta_s^t$ alone, every expectation and probability below conditions on $\mathcal{F}_t$. Assume (A1) positive descent bias on accepted edits, $\mathbb{E}[\widehat{\Delta}_{z_t} L_D \mid G_t = 1, \mathcal{F}_t] \le -\gamma_t - \tau_t$ for some $\gamma_t > 0$, and (A2) bounded estimator bias on accepted edits, $|\mathbb{E}[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t = 1, \mathcal{F}_t]| \le \varepsilon_t$. With $p_t = \Pr(G_t = 1 \mid \mathcal{F}_t)$,
$$\mathbb{E}[L_D(\theta_s^{t+1}) \mid \mathcal{F}_t] \le L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t\,\varepsilon_t.$$
Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability. In the feedback-signal classes of Section REF(sec:signal), $\varepsilon_t$ is near zero for the check itself in C1, with the sampling error of a finite suite over the patch remaining, bounded by batching for an observable outcome (C2), equal to the judge's bias and bounded only by calibration for a judged signal (C3), and unavailable per edit for a delayed signal (C4).

### Convergence (informal)

What follows is a conditional statement under strong assumptions, included to make gate stability precise; nothing in the survey depends on it. Add (A3) proposal coverage with acceptance: at every non-gate-stable scaffold, $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \le -\delta$, and the gate accepts such an edit with probability at least $q' > 0$, so that $p_t(\gamma_t + \tau_t) \ge q q' \delta$ there; (A4) effective compactness of the reachable orbit; and (A5) summable bias, $\sum_t p_t \varepsilon_t < \infty$; and let $0 \le L_D \le B$. (A3) is strong: it asks for a uniform lower bound on proposing and accepting an edit that lowers the loss by at least $\delta$, which needs attribution far more reliable than success with non-zero probability per failure. The one-step inequality is then of the Robbins–Siegmund form, a non-negative process that decreases in expectation up to a summable perturbation $p_t \varepsilon_t$, so $L_D(\theta_s^t)$ converges almost surely and $\sum_t p_t(\gamma_t + \tau_t) < \infty$ almost surely [@robbins1971convergence]. The finite sum carries the content: a bounded loss cannot pay for infinitely many accepted edits with a positive expected margin, so under (A3) the process visits non-gate-stable scaffolds only finitely often, and with (A4) the limit set of $\{\theta_s^t\}$ is gate-stable: no admissible edit clears the gate with negative expected directional loss in the limit. This is convergence of the loss and stability of the gate decision, not convergence to an optimum; a globally suboptimal gate-stable scaffold is consistent with the result, because $Q_t$ may never propose the improving edit or $\widehat{\Delta}$ may be biased to reject it. A non-stationary deployment ($D = D_t$) falls outside this argument: tracking a moving optimum would need further assumptions on the rate of drift and of adaptation, which are not supplied here. Recency weighting, pruning, expiry, and rollback are the scaffold-level analogues of the machinery continual learning uses for that case.

### Correspondence

Table REF(tab:A-1) pairs each optimization concept with its scaffold analogue. Credit assignment here is attribution, not backpropagation. Scaffold systems do not differentiate through instruction files. They trace an output error to an upstream coordinate, manually or with a judge or verifier. The one-step inequality needs only that accepted edits have positive expected descent; the convergence statement needs attribution reliable enough to supply the uniformly improving proposals that (A3) assumes, which is much stronger than the credit-assignment condition of Section REF(sec:loop), success with non-zero probability per failure.

### Worked cases

*Retrieval.* Failures recur because retrieved context omits the decisive clause. Attribution traces the error to the retrieval coordinate: chunking, query rewriting, metadata filter, embedding model, reranker, or context-packing rule. The candidate edit tightens chunk boundaries or adds a metadata constraint, and the gate checks that recall and answer accuracy improve on the patch evaluation without degrading adjacent cases. Signal class C1 or C2.

*Pitch review.* The system repeatedly overrates decks that claim a large market without numbers, and the failure cluster points at an under-specified rubric coordinate. The edit changes "evaluate market size" into "require a numeric estimate and a source; if absent, cap the score"; the gate runs the revised rubric against held-out decks with human scores. What the edit changed was the gate that will judge the next edit: the reflexive gate of Section REF(sec:signal), class C3.

*Tool use.* Calls fail because optional parameters are under-specified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The edit adds required fields or a pre-call uncertainty check; the gate checks that tool-call failures fall without raising refusals or latency. Class C2.

*Memory.* A stale customer preference is repeatedly retrieved and causes bad decisions. The responsible coordinate is a memory entry together with its provenance, priority, and expiry policy. The edit corrects, expires, or version-tags the entry; the gate checks that future behavior improves without erasing useful history. Class C2, with the correction itself observable only when a later outcome reveals it.

## Gate families and feedback-signal classes {#app:gates}

Section REF(sec:loop) collapses every production gate into one per-edit test $G_t$ on an estimate of the loss change. Surveyed systems instantiate that test in several distinct ways, and some of them are better read as proposal pruning that precedes the per-edit gate than as estimators of $\widehat{\Delta} L_D$. Table REF(tab:B-1) lists the families, the slot each occupies, representative systems, and the feedback-signal class (Section REF(sec:signal)) each family serves.

| Gate family | What it estimates | Slot in Section REF(sec:loop) | Signal class | Representative systems |
|------------|----------------------|--------------|--------------|--------------------|
| Surrogate verifier | Pass or fail from tests, a symbolic checker, or an exact match | Per-edit gate $G_t$ | C1 | DGM (sandboxed compile-and-edit check; score weights selection, not retention), SkillOpt (held-out exact match), Voyager (game-state check: C2) |
| Evaluation cascade | $\widehat{\Delta} L_D$ on a held-out task suite, cheap-to-expensive evaluators | Per-edit gate $G_t$ | C1 when the suite is exact; C2 when it is a task suite | AlphaEvolve, Braintrust, Vellum, LangSmith Hub |
| RL threshold | Reward improvement against a deployment threshold | Per-edit gate $G_t$ | C2 | SAGE, PACE |
| LLM judge with calibration | Pairwise or rubric score, calibrated against human agreement | Per-edit gate $G_t$ | C3 | SkillChain (judge stage, before its human reflection gate) |
| Reviewer judgment | Human credit assignment by pull-request review, expert sign-off, or a user's acceptance | Per-edit gate $G_t$, human-instantiated | C3 (and C2 when the reviewer has outcome data) | Sierra Agent OS 2.0, Anthropic skills repository, CASCADE (a person and an agent approve consolidation into shared memory) |
| Semantic merge | Whether a candidate duplicates or conflicts with existing artifacts | Proposal pruning before $G_t$ | C4 (also a pre-filter in C2, C3) | NanoResearch orchestrator, FederatedSkill server agent, EvolveR (admission: cosine pre-filter plus LLM equivalence judgment on each distilled principle; retention: periodic pruning on per-principle success rate) |
| Archive selection | Whether a candidate improves on, or diversifies, an archive of already-scored programs | Proposal pruning before $G_t$ | Any; inherits the class of the evaluator that scored the archive (C1 in AlphaEvolve) | AlphaEvolve (MAP-Elites-style database), ADAS |
| Multi-sample agreement | Whether $k$ independent proposals or evaluations agree; false-accept rate decays as $p^k$ rather than variance as $1/k$ | Aggregation filter on the estimate | C2, C3 noise absorption | VaG (three heterogeneous critics must all pass); SkillOpt-Lite (consensus filter across rollouts) |

Table B-1. Gate families, their slot in the formalism, and the feedback-signal class each serves.

The first five families populate $G_t$ directly and, under the assumptions of Appendix REF(app:formal), inherit its descent guarantee. Semantic merge and archive selection are not estimators of $\widehat{\Delta} L_D$; they constrain the proposal distribution, and the descent argument applies to the composition of pruning and gate. Multi-sample agreement is listed because it is the correct analogue of "wait for $k$ pieces of evidence before accepting an edit", a different operation from mini-batch averaging and one that should not be conflated with it. Read down the signal-class column. The only families available to a judged (C3) deployment are the two whose estimator is a judge. A delayed (C4) deployment has no family that estimates the loss change per edit at all: what it has is semantic merge before the gate and whatever proxy milestone stands at the horizon. That is the structural content of Section REF(sec:signal).

## Data appendix {#app:data}


**Corpus and window.** The corpus holds 256 unique systems from January 2023 to the October 2026 cutoff, released as two files. `p3_master_scores.csv` holds the 130 first-pass systems in 140 rows; `p3_refresh_2026-10.csv` holds the 126 second-pass systems in 133 rows, four of which re-audit a first-pass system and replace its row rather than add a system. The corpus therefore has 140 + 133 − 4 = 269 substrate-level rows. A system may be scored on several substrates, so rows outnumber systems, and Table 2 of the main article counts rows.

**Two passes.** Every system in either pass is scored against one rubric, from its own method section or documentation. First-pass systems were found in arXiv, vendor documentation, and public repositories through May 2026. Second-pass systems, found from June to the October 2026 cutoff, come from six query families: self-evolving skills and skill lifecycle; harness and context optimization; agent memory governance; prompt-as-code and evaluation-gated promotion; federated or multi-tenant skill sharing; and multi-agent topology evolution. Some were reached instead through the citations of the first-pass systems closest to the missing architecture of Section REF(sec:gap). The second pass was a systematic search of the field, not only a search around the known systems, so the per-substrate statistics pool both passes.

**Inclusion and exclusion.** A system enters the corpus if it either wraps a foundation model with at least one persistent artifact updated from deployment signal or is described in public as "self-improving," "scaffolded," or "agentic." The contrast set enters through the second criterion and is kept on purpose, so that the discriminator has something to mark against (Self-Refine, ReAct, TextGrad, OPRO, engineer-authored convention files; Appendix REF(app:contrast-1-1)). Two kinds of system are excluded: those whose only update mechanism is weight-level fine-tuning or reinforcement learning, which are model-side and belong to the self-evolution literature this survey positions against, and those with no public evidence of deployment or release, such as white papers without code, demos, or a production claim.

**Two filters.** The patch-local discriminator admits a system to the core corpus when it scores at least 3 on at least one substrate. Of the 256 systems, 204 pass it, 99 of them first-pass. The other 52, 31 of them first-pass, form the contrast corpus: systems described in public as agentic or self-improving that fail the discriminator. Each second-pass contrast row gives its exclusion reason in the released CSV. The stricter composite two-loop audit then asks whether Loop 1 modifies a persisted artifact from session signal and whether Loop 2 has an explicit cross-context promotion mechanism with versioning or lineage. Representative first-pass members of both groups, contrast systems and core systems that fail the composite audit, are listed in Appendix REF(app:contrast-1).

**Systems outside the released table.** Fifteen named systems have no row in the released table. Ten are treated at mechanism level in the main text and this supplement: SkillOpt, GEPA, Meta-Harness, CORAL, PACE, MOSS, RCL, FederatedSkill, SkillClaw, and ChronoMem. Each was classified from its paper after the first pass closed and is placed by that reading, in the matrix or among the research families. The other five are contrast or boundary entries, classified from their papers and marked with a dagger in Appendix REF(app:contrast-1): ReAct, MetaGen, MetaReflection, CLIN, and ACE. The corpus counts (256, 204, 52) exclude all fifteen. SkillOpt is nonetheless one of the eleven research systems that pass the composite audit, because the audit was applied to it from its paper.

**Evidence tiers.** Each system carries one or more of five tiers: (T1) peer-reviewed publication; (T2) arXiv preprint; (T3) production claim with metrics; (T4) open-source artifact; (T5) industry blog or interview. T1 and T4 weigh most in cluster analysis. T3 counts where the claim is concrete, naming a benchmark or an integration target; T5 counts only when T1–T4 evidence corroborates it elsewhere. Tier flags reach cluster claims through the per-row evidence column of the released CSV, and T3 production claims are never pooled with T1 or T2 evidence in a cluster-level statistic.

**Tier distribution.** In the first-pass core corpus, about a quarter of the systems carry T1 evidence as their primary tier, roughly half carry T2, and the rest T3 or T4. Preprint-only systems in either pass carry T2, recorded per row in the released CSV. Some T2 work is recent enough that its ablations may yet be revised; the cluster-level claims survive dropping any single T2 system.

**Scoring discipline.** Each system is scored substrate by substrate on the survey's 0–5 rubric and also receives an integrated patch-local-adaptation score in {0, 1, 2, 2.5, 3, 3.5, 4, 4.5, 5}. Half-scores are used sparingly, where one criterion is clearly met and another only partly, and ambiguous cases are rounded down. Every score comes from a single rater. The full score table is therefore published, each row with a one-line justification in the released CSVs, so that any ambiguous classification can be checked independently (Appendix REF(app:scores)).

**Composite two-loop criterion (sensitivity analysis).** The strict composite audit passes eleven research systems, all first-pass except SkillOpt, and three industry exemplars. Two natural relaxations change that count.

The governance relaxation counts any of versioning, lineage, or rollback as Loop-2 governance. It re-admits MAE, MetaGen, MetaReflection, and CLIN from the first pass, raising the research count to approximately fifteen, and of the second-pass promoters below it admits EvolveNet alone, whose rollback to the previous shared harness counts.

Six second-pass systems promote across users, clients, teams, or repositories with no versioning or lineage on the promoted artifact: EvolveNet, Evo2Team, XRepoSkill, ShareMem, Spotify's recommendation loop, and Future AGI's prompt lifecycle. They fail the audit on governance alone. RASO, which retrieves skills from a public corpus, is not among them, because inbound retrieval is not a promotion (Appendix REF(app:contrast-2-1)). A weaker relaxation that asks only for an explicit promotion mechanism, with no governance property at all, would admit five of them, all landing in [Auto × Auto] except Spotify's loop, which would land in [Auto × Human]; none would open a new cell. The sixth, Future AGI's prompt lifecycle, rests on T5 evidence alone, which the tier rule above does not count without corroboration, so it is not admitted under any rule.

The optimizer-state relaxation admits as Loop 1 a session signal that updates optimizer state without persisting an artifact distinct from that state. It re-admits DSPy and TextGrad from the first pass, raising the research count to approximately thirteen. It admits no second-pass system. The second-pass contrast rows are benchmarks, evaluation and attack studies, registries, audits, and conceptual frameworks, plus one orchestrator whose adaptation lives in the weights, and none of them persists optimizer state as its only artifact.

The qualitative findings hold under every relaxation: [Auto × Auto] is well populated; [Human × Auto] and [Human × Human] are empty; [Human × None] holds only curation workflows and [None × Human] only registries, all of which fail the composite audit; the governance-first cluster sits in [None × Auto]; Letta alone passes the audit with an ungated promotion; and no system adds governed cross-tenant promotion.

---

## The mechanism stack and continual-learning notes {#app:mechanism}

### The mechanism stack {#app:mechanism-1}

The update rule of Section REF(sec:loop) expands into six operations that every patch-local system performs, whether by explicit engineering or by accident.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, evaluation regressions, and tool-call failures. This is the signal source of Loop 1; without it, $z_t$ has no provenance.
2. **Mode discovery and credit assignment.** Cluster repeated failures into the deployment's own error modes (the catalogue of *The Architecture of Errors* [@arbuzov2026architecture], instantiated locally for one patch) and attribute each mode to the scaffold coordinate responsible for it (the correspondence note of Appendix REF(app:formal)).
3. **Delta synthesis.** Turn a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, or an evaluation case. This produces $z_t$.
4. **Delta validation.** Estimate whether the edit lowers $L_D$ without collateral damage on adjacent inputs. The gate $G_t$ is Auto when the check is an algorithmic criterion and Human when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted edit stays in the local fork or climbs the scope hierarchy: PROJECT, STACK, TENANT, CORE. This is Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, and detect overfitting. Without this operation, accumulated edits produce the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline, and surveyed systems implement them partially and unevenly. Research full-auto systems excel at operations 3 and 4, governance-first systems at operation 5, and production hybrids at most of operations 1 to 5 but rarely at operation 6. Implementation patterns for each operation lie outside this survey.

### Loop 1 and Loop 2 as descent steps of different radius {#app:mechanism-2}

Loop 1 proposes and validates local descent steps on a single $L_D$. Loop 2 widens the update radius: it selects, merges, and promotes accepted local edits so that they apply to a larger set of patch losses averaged together. Acceptance at USER scope descends on a single $L_D$. PROJECT promotion descends on a loss averaged over the project, and STACK promotion widens the average further. TENANT promotion descends on a tenant-wide average; CORE promotion, the cross-tenant level, descends on an average over tenants. The two-loop design space is therefore more than a taxonomy of engineering patterns: it records *which loss each surveyed system is descending on*, and which estimator gates the step.

### Overfitting in scaffold adaptation {#app:mechanism-3}

In weight training, overfitting is usually a defect. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve generality across patches, so they must smooth over local conventions and rare workflow-specific failures. A deployment's patch needs the opposite: selective specialization to its own residuals. The scaffold is therefore a layer meant to overfit, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold edit that improves one repository, hospital workflow, or legal diligence process may degrade performance elsewhere. That is not a contradiction; it is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

In non-stationary patches ($D = D_t$), the same descent mechanism tracks a moving optimum rather than converging once. Recency weighting, replay, pruning, expiry, and rollback are therefore not optional hygiene; they are the scaffold-level analogues of continual-learning machinery.

---

## Contrast set, matrix membership, and closest approaches (May 2026 corpus) {#app:contrast}

The tables in this section describe the first-pass corpus, which closed in May 2026; the second-pass systems that occupy a cell of the Section REF(sec:design) matrix are named in the cell-by-cell discussion that follows the matrix.

### Contrast set {#app:contrast-1}

Two tables mark the two boundaries of the survey. The first lists representative members of the first-pass contrast corpus: 31 systems that fail the patch-local discriminator, scoring below 3 on every substrate. The second lists core systems, each scoring at least 3 on some substrate, that still fail the stricter composite two-loop criterion, so that the asterisked entries of the matrix in Appendix REF(app:contrast-2-1) can be checked.

Two marks recur. An asterisk, used in the matrix, marks a system that fails at least one criterion of the composite audit and is included for contrast. A dagger has two uses: in the two contrast tables it marks a system classified from its paper because the score table has no row for it (ReAct, MetaGen, MetaReflection, CLIN, ACE); in the matrix it marks an industry exemplar evaluated with vendor documentation as the primary evidence (Sierra Agent OS 2.0, Cognition Devin).

#### Contrast corpus: fails the patch-local discriminator {#app:contrast-1-1}

| System | Year | Discriminator failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Self-Refine [@madaan2023selfrefine] | 2023 | No persistent artifact | In-context iteration only |
| ReAct [@yao2023react]† | 2023 | No persistent artifact | Thought-act-observe loop is intra-session |
| TextGrad [@yuksekgonul2024textgrad] | 2024 | No artifact distinct from optimizer state | Textual-gradient optimization; SkillOpt [@yang2026skillopt] (Section REF(sec:findings); Appendix REF(app:families)) adds the persistent `best_skill.md`, held-out validation gate, rejected-edit memory, and textual learning-rate schedule that TextGrad lacks. |
| OPRO, Toolformer | 2023 | No persistent deployment artifact | Optimization or tool use inside a single training or inference run |
| Aider conventions, Lovable knowledge | 2024 | No feedback loop | Engineer-authored convention files |
| AGENTS.md (as a standard) | 2025 | No feedback loop | Cross-vendor artifact format as a workspace file; adoption measured, adaptation absent (Section REF(sec:findings)). The specification's governance under the AAIF is a separate S6 entry, "AGENTS.md / AAIF" |
| LangChain Skills, HuggingFace Agent Skills, CrewAI Skills | 2025–2026 | No feedback loop | Curated skill packs without failure-triggered update |
| Tran & Kiela [@tran2026singleagent] | 2026 | Not a system | Single-agent baselines match or beat multi-agent under matched thinking-token budgets; constrains S5 claims (see Section REF(sec:findings)) |

#### Core corpus, fails the composite two-loop criterion {#app:contrast-1-2}

| System | Year | Composite-criterion failure | Brief reason |
|----------------|-------|------------------------|----------------------------------------|
| Reflexion [@shinn2023reflexion] | 2023 | No Loop 2 | Per-agent episodic memory without promotion |
| Generative Agents | 2023 | No Loop 2 | Per-agent reflection + importance memory |
| ExpeL | 2023 | Loop boundary blurred | Experience bank built from training tasks |
| Mem0 (vanilla) | 2024 | No Loop 2 | Per-user memory; no cross-context promotion |
| Zep | 2024 | No Loop 2 | Per-agent/session knowledge graph |
| ChatGPT Memory | 2024 | No Loop 2 | Per-user persistence |
| Claude Memory | 2025 | No Loop 2 | Per-conversation-thread persistence |
| MemGPT | 2023 | No Loop 2 | Virtual-context management per agent |
| DSPy | 2023 | No artifact distinct from optimizer state | Prompt-template optimization; SkillOpt [@yang2026skillopt] (Section REF(sec:findings); Appendix REF(app:families)) realizes the artifact-bearing form. |
| MetaGen† | 2026 | No Loop 2; no cross-session persistence | Role pool dynamic within single inference call |
| MAE (Multi-Agent Evolve) | 2025 | No Loop 2 | Co-evolution within Proposer/Solver/Judge triplet |
| MetaReflection† | 2024 | No Loop 2 | Per-agent semantic memory |
| CLIN† | 2023 | No cross-instance promotion | Causal abstractions per-agent-per-environment |
| LangGraph, AutoGen, CrewAI | 2023–2024 | Framework only | Orchestration frameworks; not deployed systems |
| W&B Weave, Agenta, Langfuse | 2024 | No Loop 1 | Observability / eval-as-code |
| Mobile-Agent-E, Cradle, OS-Copilot | 2024–2025 | No Loop 2 | Self-evolving but per-session/per-deployment |
| Agent S, Agent S2 | 2024–2025 | No Loop 2 | Computer-use agentic framework |
| ACE [@ace2025agentic]† | 2025 | No Loop 2 in surveyed form | Single-context evolving playbook |
| Cursor Rules (vanilla) | 2024 | No Loop 2 | Per-project artifacts |
| GitHub Copilot custom instructions, Windsurf, Continue.dev, Zed AI rules | 2024 | No Loop 1 | Engineer-authored at repo base branch |
| Replit `replit.md` | 2025 | Loop 2 absent | Self-writing scaffold but per-workspace |
| SkillForge [@skillforge2026] | 2026 | No Loop 2 | A judge flags failed replies that drive each skill rewrite; the rewrite is committed without an acceptance test, versions stay in the scenario deployment, and engineers review replies, not skill versions |
| AutoAgent [@wang2026autoagent] | 2026 | No Loop 2 | Per-agent tool and peer descriptions revised on an uncalibrated consistency judgment; never promoted or versioned |
| SkillRL [@skillrl2026] | 2026 | No gate on either loop | A success rate below 0.4 triggers skill proposals; the skill bank takes each one as an unconditional union |

The contrast systems fail the discriminator in three main ways: they iterate in context only, they have no feedback loop, or they are not systems at all. Core systems fail the composite criterion mostly for want of a Loop 2.


### Matrix membership and closest approaches {#app:contrast-2}

#### Two-loop matrix: cell-by-cell discussion {#app:contrast-2-1}

Both axes record who decides, as Section REF(sec:loop) defines: a gate is Auto when a program applies a check, Human when a person decides, and None when the step is absent or runs unchecked. An engineer-authored or registrant-supplied artifact with no failure trigger therefore has Loop 1 None in both passes, and who supplies each candidate is listed separately in the occupant table at the end of this section.

The first-pass matrix, with the marks of Appendix REF(app:contrast-1):

| | **Loop-2 Auto-gated** | **Loop-2 Human-gated** | **Loop-2 None** |
|---|---|---|---|
| **Loop-1 Auto-gated** | NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual | CASCADE, Sierra Agent OS 2.0†, Cognition Devin† | AutoAgent\*, MAE\*, MetaGen\*, MetaReflection\*, CLIN\*, DSPy\*, TextGrad\* |
| **Loop-1 Human-gated** | **[empty by engineering logic]** | **[empty in the first pass]** | *(none)* |
| **Loop-1 None** | ExpeL\* (weak), Braintrust\*, LangSmith Hub\*, Vellum\* | Anthropic skills repository\* | Self-Refine\*, ReAct\*, Mem0\*, SkillRL\*, SkillForge\* |

The matrix places the first-pass systems audited under the composite criterion, with SkillOpt, and the contrast entries marked with an asterisk. Every matrix entry that passes the audit sits in [Auto × Auto] or [Auto × Human]: the ten research systems of the first cell, with CASCADE, are the eleven research systems of Section REF(sec:method), and Sierra Agent OS 2.0 and Cognition Devin are two of its three industry exemplars. The third exemplar, Letta's Context Repositories, is a second-pass system.

Three placements need a word. DSPy and TextGrad sit in [Auto × None] because their Loop 1 is automated but persists only optimizer state, which only the optimizer-state relaxation of Appendix REF(app:data) would count as a persisted artifact. DGM sits in [Auto × Auto] although its local gate is a validity check rather than a loss estimate: the archive admits every child that compiles and can still edit code, the benchmark score weights parent selection rather than deciding retention, and no person decides anything in the loop, since self-modifications are evaluated without human intervention [@zhang2025darwin]. SkillRL sits in [None × None] although its loop is failure-driven: a per-category success rate below 0.4 triggers new skill proposals, and the skill bank takes each proposal as an unconditional union, so the step that keeps an edit runs unchecked, and the bank never leaves its run. SkillForge sits beside it for the same reason: a calibrated judge selects the failed replies that drive each skill rewrite, the rewrite is committed without an acceptance test, every version stays in the scenario deployment, and its support engineers review replies, not skill versions.

COSPLAY and Cuadros et al., which are first-pass rows, and PACE, CORAL, GEPA, Meta-Harness, MOSS, and RCL, which were classified from their papers after the first pass closed, carry no composite audit, so they are neither placed in the matrix nor counted in Section REF(sec:method). Second-pass systems record their gate pairs in the released score table, and the paragraphs below name those that occupy a cell.

**[Auto × Auto]** is the most populated cell: ten systems, each with a machine-evaluated criterion on both loops. Speed on both loops is what its members share; cross-organization governance is what every one of them lacks.

**[Auto × None]** holds the systems whose local loop is gated and whose promotion has no gate, whether because nothing is promoted or because everything is. One audit passer sits here: Letta's Context Repositories push shared memory across agents automatically, with git lineage and no evaluation of any kind, so the composite audit admits them on lineage and the matrix records a promotion that nothing decides (Section REF(sec:design)). Mem0 Platform, TOKI, Learning on the Job, and RASO sit here with no promotion at all; RASO retrieves skills from a read-only public corpus, which is inbound retrieval rather than promotion [@chu2026raso]. One first-pass system joins them, starred because it has no Loop 2: AutoAgent's analyzer accepts revisions to one agent's tool and peer descriptions on an uncalibrated consistency judgment, and nothing leaves that agent's store. VACE belongs here too although its gate is a held-out check: it compares a candidate harness with the incumbent against the freshly trained checkpoint of the same run, so the edit is made and kept inside one training run [@qi2026vace].

**[Auto × Human]** is the production-viable cell. Loop 1 fires at machine speed under an algorithmic criterion, and Loop 2 waits for a person before an edit propagates; the pairing reconciles the speed of automation with a reviewer's accountability. CASCADE, Sierra Agent OS 2.0, and Cognition Devin occupy it: a human-and-agent consolidation gate, human-authored expert answers, and a reviewer's merge of a pull request each put a person on promotion.

Six second-pass systems promote across users, clients, teams, or repositories with no versioning or lineage on the promoted artifact, so they sit outside the strict audit: EvolveNet, Evo2Team, XRepoSkill, ShareMem, Spotify's recommendation loop, and Future AGI's prompt lifecycle. Were the audit to ask for a promotion mechanism and no governance property at all, five of them would enter, all landing in [Auto × Auto] except Spotify's loop in [Auto × Human], without opening a new cell; the sixth, Future AGI's prompt lifecycle, rests on T5 evidence alone and is not admitted under any rule (Appendix REF(app:data)).

**[None × Auto]** holds the governance-first prompts-as-code systems: Braintrust, LangSmith Hub, and Vellum. Their Loop 2 is real, since evaluation-gated CI blocks a promotion on regression. They have no Loop 1 in the patch-local sense, because engineers author the candidate artifacts at their desks and session feedback never triggers one, and the asterisks record exactly that: governance without inner-loop adaptation. The cell is informative because it shows what survives when only the outer loop is automated. ExpeL, starred and also marked weak, sits here for a different reason: its experience bank is built from training tasks, which blurs the boundary of its loop, so it fails the audit (Appendix REF(app:contrast-1-2)).

**[Human × Auto]** is empty in both passes: no surveyed system puts a person on the local gate of a failure-driven loop and then promotes the result by program. A plausible occupant would ship person-approved skills through an automatic held-out evaluation; no published system does.

**[Human × Human]** is empty too. The registries that a first reading puts here (Azure API Center, the agentic-community MCP Gateway and Registry, TrueFoundry, Buildrix) have no failure-driven loop: a person registers an artifact and a person, or an admission scan, approves its use, which is a promotion gate on a registrant-supplied artifact. They sit in **[None × Human]** with the Anthropic skills repository and Agentic Configuration Management, whose lifecycle states a governance role assigns, and the five public skill repositories of the field study (Section REF(sec:design)) show the same shape in practice. Enoch's checkpoint-and-validate protocol moves one agent's state between hosts and is neither loop. The released table records these re-codings (Appendix REF(app:audit-7)).

**[Human × None]** is the curation cell, also filled only from the second pass and single-loop by construction. In VerificAgent an agent drafts, a person fact-checks, and the result is frozen; in SkillChain a judge filters the candidate edits and a person decides, at a reflection gate, which refined skills are deployed; in the Davis et al. case study one engineer both writes and accepts the governance mechanisms that failures call for (Section REF(sec:design)). Curation stays patch-local, rather than collapsing into an engineer editing a configuration file, because the candidate answers a failure and a person decides whether it stays.

The occupants, with the variable the matrix does not show:

| Cell | Systems | Candidate source | Loop 1 gate | Promotion mechanism | Loop 2 gate |
|--------|----------------------|----------------|--------------|------------------|---------------|
| [Auto × Auto] | NanoResearch, SkillOpt, AlphaEvolve, ADAS, DGM, Voyager, SAGE, EvolveR, CoEvoSkills, AutoManual | agent proposals from trajectories or failures | evaluator, verifier, or threshold | merge into a shared bank or archive | the same evaluator, on the shared bank |
| [Auto × Human] | CASCADE, Sierra Agent OS 2.0, Cognition Devin | agent proposals | calibrated judge or outcome threshold | release to the team or product | reviewer, domain expert, or merge approval |
| [Auto × None] | Letta Context Repositories; Mem0 Platform, TOKI, Learning on the Job, RASO, VACE; AutoAgent | agent (Letta: sleep-time subagents) | automatic write gate (RASO: validation-set acceptance; VACE: held-out comparison against the incumbent harness; AutoAgent: an uncalibrated consistency judgment) | Letta: unconditional git push to shared memory; the others: none | none |
| [None × Auto] | Braintrust, LangSmith Hub, Vellum, Governed Capability Evolution; EDDOps, with a sign-off after the threshold | engineers | none (no failure-driven loop) | evaluation-gated release | evaluation threshold |
| [None × Human] | Azure API Center, MCP Gateway and Registry, TrueFoundry, Buildrix, Anthropic skills repository, Agentic Configuration Management | registrants, contributors, engineers | none | admission to a registry, merge into a shared repository, or a lifecycle state | approval by a person (the MCP Gateway adds an automated admission scan) |
| [None × None] | SkillRL, SkillForge | agent proposals from a success-rate trigger or a judge's failure flags | none (the rewrite is kept unchecked) | none | none |
| [Human × None] | VerificAgent, SkillChain, Davis et al. | agent drafts (VerificAgent; SkillChain after a judge); the engineer (Davis et al.) | a person | none | none |

#### Closest approaches to governed cross-tenant scaffold optimization {#app:contrast-2-2}

Section REF(sec:gap) defines the four properties: (a) an auto-gated Loop 1, (b) cross-organization promotion, (c) versioned lineage with access control, and (d) rollback. The closest approaches split them among themselves:

- **AlphaEvolve** has (a) and a partial (b) confined to one organization; it has no mechanism for promotion across organizations.
- **NanoResearch** has (a) at the research level, and its paper describes no enterprise governance layer.
- **SkillOpt** has (a) fully and a partial (c), through its exported `best_skill.md` artifact and protected slow-update field. Its reported positive transfer across models, harnesses, and benchmarks is an empirical measurement of evidence radius. It implements neither (b) nor explicit rollback (d). The walkthrough in Appendix REF(app:families) maps each of its design decisions onto the loop.
- **CORAL** [@qu2026coral] has a partial (a) through reflection-written shared memory and an automatic Loop 2 through heartbeat-based promotion; it has no (b), no formal access control for (c), and no (d). It is the only system classified before the second pass whose Loop 2 runs asynchronously across multiple agents inside one organization, through shared persistent memory. Evo2Team and ShareMem, second-pass systems, promote across teams and across users without versioning.
- **PACE** [@ling2026pace] has (a) at small-model production timescales and a fast/slow two-timescale pair of loops that consolidates across one deployment's own episodes, not across deployments; it has no (b) and no formal (c) or (d). It is the closest demonstration that the two-loop architecture runs under small-frozen-model constraints.
- **Meta-Harness** [@lee2026metaharness] has (a) over the harness (substrate S5), with a filesystem of candidates that records credit assignment and serves as the accumulated history $H_t$ of Appendix REF(app:formal). It has no cross-organization promotion, no access control, and no rollback.
- **SkillForge** has no (a), since its calibrated judge selects failures and nothing tests the rewrite, and a partial (c) through VFS commits, but no (b): each rewritten skill version stays in the scenario deployment that produced it, and its support engineers review replies, not skill versions; (d) is undocumented in the public report.
- **Sierra Agent OS 2.0** has a partial (a). Its cross-organization promotion is claimed in vendor documentation only and not counted as evidence under the tier rule of Section REF(sec:method), and its GitHub-style Workspaces give some lineage but not access control with rollback in the strict sense.
- **FederatedSkill** [@yang2026federatedskill] has (a) and, with EvolveNet (Table 6 of the main article), the strongest partial (b) among the surveyed systems: heterogeneous clients, each a backbone-plus-harness profile under one federation operator, exchange semantic skill diffs, and a server-side evolution agent applies, adapts, or rejects each patch per client. An auditable decision log, recording source patch, reward, and justification for each modified path, gives a partial (c); there is no access control and no (d).
- **SkillClaw** [@ma2026skillclaw] has a partial (a), through a nightly validation step, and a partial (b) across the users of one shared, synchronized skill repository; it reports no (c) or (d).
- **ChronoMem** [@su2026chronomem] has (d) and the versioning half of (c) for the memory substrate alone: whole-memory snapshots, version histories, and natural-language rollback inside Google's Agent Development Kit. It has no Loop 1, no (b), and no access control.
- **Vellum, Braintrust, and LangSmith Hub** have (c) and (d) explicitly but neither (a) nor (b) in the strict sense; they are governance-first by construction.

No surveyed system combines (b), (c), and (d) under any gate type. The cross-organization governance triad is unfilled on its own, whether or not Loop 1 is auto-gated.

#### Whether the missing architecture should be built {#app:contrast-2-3}

Whether the missing architecture should be built depends on the feedback-signal class, not on the application domain: safety-critical domains such as medical decision support, legal advice, and financial advice, where a reviewer's gate on promotion is a design feature rather than a defect, are judged or delayed domains with high stakes. Section REF(sec:gap) gives the argument class by class.

---

## The convergent research families, system by system {#app:families}

This appendix walks the convergent research families of Section REF(sec:families) system by system, at the level of mechanism, so that each conclusion of that section can be checked against what the systems do. The walkthroughs were written before the second pass and updated where the audit of Appendix REF(app:audit) revised a claim; the members the second pass adds to each family are cited in Section REF(sec:families) and appear in Appendix REF(app:scores).

### The convergent landscape {#app:families-1}

SkillOpt [@yang2026skillopt] is the clearest instance of artifact-layer descent we found, and it is one of at least eighteen independent research threads from 2025–2026 that converge on the same disciplined, gradient-like update for the scaffold layer. They converge from different starting points: GEPA from prompt optimization and Tiwari et al. from continual learning; RCL from cognitive-agent learning; Meta-Harness, AHE, MOSS, CANTANTE, and Ong et al. from harness engineering; MOCHA and Ratchet from skill-deployment constraints; ICT, Combee, CORAL, and PACE from cross-task, multi-agent, and production deployment. Each instantiates a different subset of the five conditions of Section REF(sec:loop), and each exposes a different gap.

By substrate (Section REF(sec:method)), GEPA and RCL work on the prompt and context layer (S1–S2); the harness family on orchestration (S5), with MOSS reaching into source code (S2+S5); MOCHA and Ratchet on skills under deployment constraints (S2); the transfer family on integrated memory-plus-orchestration stacks (S3+S5); and SkillOpt on an integrated stack led by S2.

No member of any family combines the four properties of Section REF(sec:gap): (a) auto-gated Loop 1, (b) cross-organizational Loop 2, (c) versioned lineage with role-based access control (RBAC), and (d) rollback. The loop of Section REF(sec:loop) is realized in fragments across the families, and every member leaves the Section REF(sec:gap) gap open.

### SkillOpt: full correspondence {#app:families-2}

The table maps each component of SkillOpt to its quantity in Section REF(sec:loop), with the role that quantity plays and a pointer into the published procedure (Algorithm 1 of the SkillOpt paper).

| Section REF(sec:loop) quantity | SkillOpt instantiation | Section REF(sec:loop) role explained | Algorithm pointer |
|--------------|------------------------|------------------------|------------------------|
| $\theta_s$ (scaffold) | `best_skill.md` — a 379–1,995-token markdown document | the trainable external state of the frozen target model; persistent and exported as the deployment artifact | $s_{\text{best}}$ (Algorithm 1, lines 1, 22, 37) |
| $L_D$ (patch loss) | benchmark-native hard score / exact-match on a held-out test split | scalar quality signal that the optimizer is implicitly minimizing | $\textsc{Evaluate}(M, h, s, D)$ (lines 2, 17, 37) |
| $Q_t$ (proposal) | optimizer-model reflection over failure and success minibatches; failures and successes analyzed separately, then merged with priority on failure fixes | proposal distribution conditioned on accumulated rollout evidence and current scaffold | optimizer calls $O$ for failure analysis, success analysis, and merge (lines 9–11) |
| $z_t$ (edit) | structured add/delete/replace patch on the skill (or rewrite-from-suggestions in rewrite mode) | the candidate update applied via $\oplus$ to the current scaffold | rank/clip to $\eta_t$ edits, apply to obtain $\tilde s$ (lines 12–13) |
| $\eta_t$ (textual learning rate) | bounded per-step edit budget; constant / linear / cosine / autonomous schedules; default cosine with floor $\eta_t=2$ | edit-magnitude controller; the step size of Section REF(sec:loop) in textual form | rank/clip step (line 12); schedule applied per epoch |
| $G_t$ (gate) | held-out selection-split accept gate, strictly greater than current selection score | the per-edit gate $G_t$ — accepts only when $\widehat{\Delta}_{z_t} L_D$ improves the selection score | comparison at line 20; cache lookup at lines 14–18 |
| rejected-edit buffer | epoch-local store of failed proposals and the score drop they caused | converts rejected steps into negative feedback for later proposals within the same epoch; zero deployment cost | $\mathcal B$ updated at line 26; reset at line 5 |
| slow/meta update | epoch-end longitudinal guidance written to a markup-fenced protected slow-update field, still passed through $D_{\text{sel}}$ | second-order consolidation across adjacent epochs; step-level edits cannot overwrite the protected slow-update field | lines 28–31; gate applied to injected guidance |
| optimizer-side meta skill | $m_{\text{meta}}$ — a prompt-side summary of which edits helped, which failed, and which failures persisted | training-time guidance for $Q_t$; never shipped with the deployed artifact | lines 33–34 (training-side only) |

The mapping is one-to-one at the level of Algorithm 1: every Section REF(sec:loop) quantity has a named, code-level counterpart, and every SkillOpt control surface maps onto a Section REF(sec:loop) quantity. SkillOpt is therefore the clearest instance we found in which the loop of Section REF(sec:loop) is *mechanism* rather than *metaphor*: all five conditions are instantiated.

### What SkillOpt does that prior textual-optimization systems do not {#app:families-3}

SkillOpt is compared with six baselines under one protocol (same target model, held-out test split, and scorer), and each baseline lacks a specific piece of the loop.

- **TextGrad** [@yuksekgonul2024textgrad] backpropagates textual feedback through a compound system's variables but leaves no artifact distinct from optimizer state, which is why Appendix REF(app:contrast-1) places it outside the core corpus; it has no step bound, held-out gate, or rejected-edit buffer. SkillOpt leads it on direct chat by $+5.9$ to $+34.0$ points across benchmarks at GPT-5.5 scale, and at all seven target-model scales.
- **GEPA** [@agrawal2025gepa] evolves prompts by reflection under Pareto-style selection. Its target is a prompt rather than a persistent skill, its selection is not a strictly-greater held-out gate, and nothing bounds an accepted edit, so one edit can rewrite the prompt wholesale. SkillOpt matches or beats it in every reported cell of its main results table [@yang2026skillopt].
- **Trace2Skill** [@ni2026trace2skill] distils trajectory-local lessons into reusable skills offline. No held-out loop accepts or rejects each candidate, so delta validation (operation 4 of Appendix REF(app:mechanism-1)) and the rejected-edit buffer are missing. SkillOpt leads it by $+5.0$ to $+19.0$ points at GPT-5.5 direct chat.
- **EvoSkill** [@alzubi2026evoskill], the strongest baseline inside the Codex and Claude Code harnesses, evolves a skill folder from failure analysis. Its credit assignment is genuine, but per-step folder edits are unbounded and rejected edits are not kept. SkillOpt leads it by $+14.0$ inside Codex and $+3.2$ inside Claude Code on the GPT-5.5 five-benchmark average.
- **A human-written skill** (145–516 tokens per benchmark) persists but never updates: the no-Loop-1 ceiling.
- **A one-shot LLM skill**, generated once by GPT-5.5 from the benchmark description, never updates and proposes without rollout evidence: the untrained-scaffold baseline.

ABSTRAL [@song2026abstral] and EvoTest [@he2025evotest], cited by SkillOpt but not measured, work at the multi-agent-design and test-time-configuration layer and fall outside the comparison.

The live difference across the six is four controls: a persistent edit target distinct from optimizer state ($\theta_s$); a held-out gate on every acceptance ($G_t$, with estimator $\widehat\Delta$ and threshold $\tau_t$); rejected edits kept as negative feedback for $Q_t$; and a bounded, scheduled edit budget ($\eta_t$). SkillOpt is the first system we found that has all four, run as one offline training loop whose deployed artifact, a 379–1,995-token markdown file, needs no optimizer calls at inference.

Its follow-up, SkillOpt-Lite [@shen2026skilloptlite], asks which controls are necessary. Recasting skill optimization as zeroth-order search, it keeps three principles: trajectory exploration through the file system, consensus attribute mining (attributes common across heterogeneous rollouts, single-sample quirks discarded), and a held-out gate strictly disjoint from the training failures. It drops minibatch reflection pooling, the rejected-edit buffer, the slow update, and the learning-rate schedule. It still converges faster and scores higher than full SkillOpt (LiveMath $+8.8$ points at GPT-5.5, $+25.4$ at GPT-5.4-nano). The gate and a consensus form of credit assignment are load-bearing; negative-feedback retention and the bounded step are stabilizers whose value depends on the benchmark. None of this touches the governance properties of Section REF(sec:gap).

### GEPA, Tiwari, and the reflective-evolution family {#app:families-4}

The immediate predecessor to SkillOpt's optimizer framing is **GEPA** [@agrawal2025gepa]. It shows that natural-language reflection over execution trajectories can provide a richer adaptation signal than sparse scalar rewards for prompt evolution in compound AI systems. GEPA samples trajectories containing reasoning steps, tool calls, and tool outputs; reflects on them to diagnose failures and propose prompt updates; and maintains a Pareto frontier of candidate prompts rather than greedily mutating only the current best. Across six tasks, GEPA outperforms GRPO by 6% on average and by up to 20% while using up to 35× fewer rollouts, and also outperforms MIPROv2 in the reported aggregate comparison. In Section REF(sec:loop) vocabulary, GEPA strongly instantiates the proposal side, $Q_t$, through trajectory-conditioned reflection, and uses Pareto-based candidate selection as a proposal and pruning mechanism. What it does not instantiate is the full SkillOpt-style artifact lifecycle: a bounded edit budget on a reusable skill document, a strictly-greater held-out gate on each accepted skill update, a rejected-edit buffer used as negative feedback, and an exported deployment artifact with governance hooks.

**Tiwari et al.** [@tiwari2026fastandslow] supply the broader framing from the optimization side, arguing that restricting learning to *either* in-context adaptation (prompt optimization) *or* in-weights adaptation (RL or fine-tuning) is unnecessary and costly. In-context adaptation is cheap and rapid but capacity-bounded; in-weights adaptation is expressive but induces catastrophic forgetting and loss of plasticity [@dohare2024loss]. The scaffold layer of Section REF(sec:families) is the substrate that absorbs what in-context adaptation can carry cheaply, leaving the weights free to generalize. Tiwari et al. reach the two-timescale motivation from optimization and Section REF(sec:families) reaches it from production reliability; the two framings are independent and reinforce each other.

### Reflective Context Learning: a parallel formalization {#app:families-5}

The most direct independent convergence on the Section REF(sec:loop) formalization comes from **Reflective Context Learning** [RCL; @vassilyev2026rcl]. Their opening observation is that "the fundamental problems of learning, including credit assignment, overfitting, forgetting, local optima, and high-variance learning signals, persist whether the learned object lies in parameter space or context space," and that current methods are "fragmented and ad hoc" precisely because they address these challenges one at a time rather than as a unified optimization problem over the context. The parallel to Section REF(sec:loop)'s argument, that scaffold maintenance needs the discipline of weight-space optimization applied to an external artifact layer, is exact and was arrived at independently.

RCL maps onto Section REF(sec:loop) as follows. The *learned context* is $\theta_s$. The *reflection signal* is a form of credit assignment identifying which context coordinate caused a failure (Appendix REF(app:mechanism-1), operation 2). The *generalization penalty* that RCL introduces to prevent narrow sample-specific rules is structurally the complexity penalty $\Omega(z)$ of the gate condition. Where RCL and Section REF(sec:loop) differ is in Loop-2 scope: RCL is framed around single-agent cross-task generalization, while Section REF(sec:loop)'s Loop 2 is cross-deployment, cross-tenant, and cross-organizational promotion. The convergence is nonetheless significant: two research threads starting from different motivations (production reliability in Section REF(sec:loop), cognitive agent learning in RCL) arrive at the same formal observation that the classical learning problems do not disappear when the learned object moves outside the weights.

### The harness-optimization cluster {#app:families-6}

A second family optimizes the *harness*, the code and configuration that wrap a frozen model, rather than skill documents. It names credit assignment as the central unsolved problem of scaffold evolution, and its solutions instantiate two operations of the mechanism stack in Appendix REF(app:mechanism-1): mode discovery with credit assignment (operation 2) and delta validation (operation 4).

**Meta-Harness** [@lee2026metaharness] starts from the observation that system performance "depends not only on model weights, but also on their harness", the scaffold-versus-weights decomposition stated for this substrate. Existing text optimizers, it finds, "compress feedback too aggressively" for credit assignment, so it gives an outer-loop proposer filesystem access to the source code, scores, and execution traces of every prior candidate. The edit history becomes the credit-assignment signal. In Section REF(sec:loop) terms the filesystem is the accumulated history $H_t$ that conditions the proposal $Q_t$, and the outer loop closes Loop 1 over orchestration (S5) rather than skills (S2).

**Agentic Harness Engineering** [AHE; @lin2026ahe] comes at the problem from observability. It names three obstacles: a heterogeneous action space across editable components, voluminous trajectories that bury the actionable signal, and edits whose effect is hard to attribute. They are, in order, coordinate identification (operation 2), residual capture (operation 1), and the credit-assignment half of operation 2. AHE's answer, three observability pillars that give every editable harness component a file-level representation, builds the coordinate decomposition that Section REF(sec:loop) assumes. Descent needs that instrumentation as much as it needs the loop.

**MOSS** [@cai2026moss] observes that earlier self-evolving systems "confine evolution to text-mutable artifacts" and leave the harness untouched. Routing, hook ordering, state invariants, and dispatch live in code, so a whole class of structural failure is, in MOSS's phrase, "physically unreachable from the text layer". MOSS therefore extends Loop 1 to rewriting source code, evolving skills (S2) and orchestration (S5) together. The consequence for Section REF(sec:gap): a governed optimizer that covers only text artifacts leaves the code substrate ungoverned.

**CANTANTE** [@zehle2026cantante] takes up credit assignment in multi-agent scaffolds, where "scores are available only at the system level, whereas the parameters governing agent behavior are local". It contrasts rollouts of several jointly acting configurations to split a system-level reward into per-agent update signals. That gives the credit-assignment step a concrete mechanism when the scaffold is spread across agents (S5): the attribution, succeeding with non-zero probability per failure, that the correspondence note of Appendix REF(app:formal) requires.

**Harness-optimizer evaluation** [@ong2026harnesseval] finds that judging scaffold optimizers "solely by observing target agents' performance gains" misses intermediate erroneous edits that hinder performance, and that it is "unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error". That is the line between Stage 2 and Stage 3 of Section REF(sec:loop), measured. An optimizer that cannot tell informed updates from lucky ones operates in Stage 2, whatever its benchmark gains.

**HARNESSEVO** [@nguyen2026harnessevo] turns the diagnosis into a measurement. It splits the harness into four separately evolvable slots (role, task strategy, tool and format rules, reflection and control) and attributes value by leave-one-in and leave-one-out evolution. On ALFWorld with a 7B target model nearly all of the gain sits in the reflection and control slot (leave-one-in +0.119; the other slots individually null). Spread evenly, a fixed 64-rollout budget leaves every slot below the optimizer's effective search floor, so each freezes at its seed; concentrated on the high-value slot, it recovers the gain (0.642 to 0.761). On WebShop the effect is absent. Credit assignment over coordinates has to precede budget allocation, and which coordinate carries the value depends on the task.

### Multi-objective and lifecycle constraints {#app:families-7}

Descent on a single loss misses two kinds of constraint: the platform limits a deployed skill must satisfy, and the hygiene of the artifact pool from which the gate draws its signal.

**MOCHA** [@tanjim2026mocha] observes that agent skills are "multi-field artifacts subject to hard platform constraints": descriptions are truncated for routing, instruction bodies are compacted by progressive disclosure, and co-resident skills compete for the context window. A skill must maximize task performance and satisfy those limits at once, and optimizing performance alone yields skills that pass benchmarks but degrade on real deployment infrastructure. MOCHA navigates the constraint frontier with *Chebyshev annealing*. It operationalizes the complexity penalty $\Omega(z)$ of the gate, and it shows that the scalar $\Omega$ of Section REF(sec:loop) simplifies what is, in production, a Pareto frontier.

**Ratchet** [@zhang2026ratchet] places the bottleneck elsewhere. LLM-authored skills deliver $+0.0$ pp over no-skill baselines while human-curated ones deliver $+16.2$ pp, which points away from the optimizer, the mechanism that proposes and accepts edits, and toward *lifecycle management*: whether skills are written, retrieved, curated, and retired correctly. Four hygiene mechanisms (outcome-driven retirement, a bounded active cap, meta-skill authoring, and pattern canonicalization) lift the $+0.0$ pp floor substantially before any optimizer runs.

The finding clarifies a precondition of descent rather than refuting it. The gate needs a meaningful signal: if retrieval injects the wrong skill into every rollout, the proposal process conditions on corrupted evidence and descent degrades to random search. Ratchet's mechanisms keep residual capture and mode discovery (operations 1 and 2) working. Retirement keeps stale artifacts out of the residual signal, the active cap keeps scaffold bloat from making retrieval unreliable, and canonicalization collapses near-duplicates so that proposals condition on one clean artifact set. A system with strong hygiene and no optimizer sits at Stage 1 with a clean scaffold; one with a strong optimizer and poor hygiene sits at Stage 2 with a noisy loss. Stage 3 needs both.

**SkillsVote** [@liu2026skillsvote] carries the lifecycle argument to an open ecosystem. It profiles a million-scale open-source skill corpus for environment requirements, quality, and verifiability, synthesizes tasks for the verifiable subset, and exposes skills through agentic library search before execution. After execution it splits each trajectory into skill-linked subtasks and attributes their outcomes to skill guidance, agent exploration, environment, or result signals; only successful, reusable discoveries pass into evidence-gated updates. Attribution thus happens at the admission gate rather than inside the optimizer, credit assignment used as a filter on residual capture. The redundancy and environment sensitivity SkillsVote measures are the bloat and drift of Section REF(sec:failure), arising here from many authors rather than one loop.

### Cross-task transfer and evidence radius {#app:families-8}

Several papers measure what Section REF(sec:loop) calls the *evidence radius* of a scaffold artifact, how far an edit validated in one context keeps helping when redeployed elsewhere, without using the term.

**In-context Training** [ICT; @shalev2026ict] tests cross-task self-improvement: whether experience distilled from one set of tasks transfers to unseen ones. Its finding that "current reflection-based methods can only self-correct within a single task instance" measures the radius at its lower bound, one task. ICT tries to widen it by distilling reflections into reusable lessons, which instruments Loop 2 empirically: does an edit that passed the gate on one task's $L_D$ still help across a distribution of unseen tasks?

**Combee** [@li2026combee] reaches the same measurement through scale. ACE [@ace2025agentic] showed that a system prompt which accumulates and organizes strategies through agentic interaction improves on a static prompt for a single agent; Combee learns from the traces of many agents running in parallel. Each proposal then draws on a wider deployment distribution, and the promoted artifact is tested against a larger average of patch losses. This is not cross-organizational promotion. Combee measures how much of the evidence-radius benefit parallelism inside one organization captures.

**CORAL** [@qu2026coral] runs long-lived agents that explore, reflect, and collaborate through shared persistent memory, asynchronous execution, and heartbeat-based interventions. A finding one agent writes to the shared store becomes available to all, so the store is the cross-agent promoted artifact and the heartbeat a form of auto-gated Loop-2 promotion; there is no versioned lineage, RBAC, or rollback. CORAL is the only fully asynchronous multi-agent Loop-2 promotion mechanism among the systems classified before the second pass; in the full corpus, Evo2Team and ShareMem add cross-team and cross-user promotion without versioning (Appendix REF(app:audit-3)).

**PACE** [@ling2026pace] is a production-oriented two-timescale design for small language-model agents. The fast timescale adapts prompts, parsers, validators, and control logic from failure signals within a deployment, as Loop 1 does; the slow timescale consolidates across the deployment's own episodes, a Loop 2 whose radius is one deployment. The two-loop structure holds on small, frozen production models, not only under frontier-model assumptions, and persists even when the optimizer and the target are the same frozen small model.

**SkillClaw** [@ma2026skillclaw] and **FederatedSkill** [@yang2026federatedskill] are the two systems of these walkthroughs whose Loop 2 crosses users rather than tasks or agents; in the full corpus, EvolveNet, ShareMem, and XRepoSkill also promote across users, clients, or repositories, each inside one operator (Section REF(sec:design)). SkillClaw aggregates many users' trajectories, turns recurring behavioral patterns into skill-set updates, and synchronizes the updated skills across users; its evaluation runs a day-night cycle in which simulated users generate trajectories by day and the system reflects, proposes, validates, and deploys by night. FederatedSkill exchanges semantic skill diffs, structured patches over a local library shipped with the task reward that produced them, so that clients share what they learned without sharing raw trajectories. A server-side evolution agent aggregates the diffs into a per-client capability matrix (covered, absorbing, broken, gap) and applies, adapts, or rejects each peer patch per client, logging source patch, reward, and justification for every modified path. Across 20 task families it reports up to +44.4% success and −37.5% compute against isolated self-evolution. FederatedSkill is the first surveyed system in which Loop 2 aggregates artifact updates rather than promoting a single artifact, and its decision log is the first lineage record at an aggregator. Its acceptance, though, uses the source client's reward rather than a held-out evaluation at the receiving client.

### Synthesis: what the convergence establishes {#app:families-9}

Sections REF(sec:findings) and REF(sec:families) draw four conclusions from the families, and the walkthroughs support them as follows.

1. **The scaffold-versus-weights decomposition is independently confirmed.** GEPA, Meta-Harness, MOSS, RCL, and PACE all begin from the observation that model weights and the external artifact layer are distinct adaptation surfaces with different cost, reversibility, and scope properties. No surveyed paper disputes this decomposition; the variation is in which substrate each paper targets (skill document, harness code, system prompt, shared memory).

2. **Credit assignment is the central engineering bottleneck.** AHE, CANTANTE, Meta-Harness, the harness-optimizer evaluation of Ong et al. [@ong2026harnesseval], HARNESSEVO, and SkillsVote all identify credit assignment, attributing a system-level failure to a specific scaffold coordinate, as the problem that separates disciplined Loop-1 evolution from trial-and-error. It is operation 2 of Appendix REF(app:mechanism-1), the attribution that the correspondence note of Appendix REF(app:formal) requires, and it remains unsolved in the general multi-substrate case.

3. **Lifecycle hygiene is a precondition for descent, not an alternative to it.** Ratchet establishes that the gradient-analog mechanism of Section REF(sec:loop) requires a maintained scaffold. A dirty artifact pool (stale, bloated, miscurated) keeps the gate $G_t$ from receiving a meaningful signal. Hygiene and optimization are sequential dependencies, not competing paradigms.

4. **No surveyed system combines Loop-1 automation with cross-organizational Loop-2 governance.** SkillOpt has the strongest Loop-1 closure and the most systematic evidence-radius measurement, but it does not implement cross-organizational promotion, versioned lineage with RBAC, or rollback. CORAL implements asynchronous cross-agent promotion within one system but not across organizations. PACE implements two-timescale consolidation within one deployment. Meta-Harness implements Loop-1 closure over the harness substrate but no Loop-2 promotion mechanism. FederatedSkill federates skill patches across clients under one operator, with a decision log but no RBAC or rollback, and EvolveNet adds a held-out merge gate and round rollback without lineage or RBAC. The four-property gap of Section REF(sec:gap) is narrowed on (b) and (d) by different systems and closed on none, and the independent convergence of several research threads on the same single-organization ceiling confirms it.

### SkillOpt against Section 8's four properties {#app:families-10}

Mapped onto Section REF(sec:gap)'s four properties of governed cross-tenant scaffold optimization:

- (a) **Auto-gated Loop 1.** *Satisfied.* The held-out selection-split gate at strictly-greater margin instantiates $G_t$.
- (b) **Multi-tenant cross-org promotion.** *Absent.* SkillOpt is a single-organization research system; there is no governed cross-tenant aggregator.
- (c) **Versioned lineage with RBAC.** *Partial.* The exported `best_skill.md` is a versioned artifact, and the protected slow-update field separates fast and slow consolidation. There is no documented RBAC layer or audit-trail policy, and `edit_apply_report.json` is an operational log rather than an access-controlled lineage system.
- (d) **Rollback.** *Absent.* The training loop selects the best validation-gated skill and exports it; no rollback envelope on deployed artifacts is reported.

The cross-model, cross-harness, and cross-benchmark transfer experiments reported by SkillOpt are *empirical evidence-radius measurements*: a skill optimized in one (model, benchmark, harness) cell continues to improve performance when redeployed in nearby cells without further optimization. In Section REF(sec:loop) vocabulary, this is a measured Loop-2 *radius* for the artifact, not a *governance mechanism* for promoting it. Both readings are useful: SkillOpt is the strongest Loop-1 proof and supplies the first systematic transfer evidence at the scaffold layer, while the Section REF(sec:gap) cross-tenant governance triad ((b), (c), (d)) remains unfilled.

### Cost and bloat {#app:families-11}

SkillOpt reports 0.6M to 46.4M training tokens per absolute test-point gain (their Table 6), with the procedural benchmarks (SpreadsheetBench, OfficeQA, LiveMath) at the cheap end and search/visual benchmarks (SearchQA, DocVQA) an order of magnitude more expensive per point. The deployed artifact remains 379–1,995 tokens regardless. This is, to our knowledge, the first published cost-per-point figure for scaffold-layer descent, and it complements the Section REF(sec:failure) scaffold-bloat discussion (and the Ratchet hygiene-precondition finding walked in Appendix REF(app:families-7)): the textual learning rate $\eta_t$ with cosine decay keeps the deployed skill compact even when the optimizer explores many more edits than are accepted (only 1–4 edits survive into the final skill across the six benchmarks). The mechanism that prevents the deployed artifact from bloating is exactly the complexity penalty $\Omega(z)$ of Section REF(sec:loop), instantiated as a hard cap on accepted edits per step rather than a soft regularizer.

---

## Audit of the first-pass draft's absolute claims against the full corpus {#app:audit}


The first-pass draft of this survey, written on the 130 systems of the first pass, made absolute claims of the form *no surveyed system*, *only X*, *first*, *absent*, and *empty cell*; each row below sets one of them against the full corpus of 256 systems and records what that corpus shows. A claim **holds** when the full corpus bears it out as worded, is **sharpened** when it is true and the corpus supports a more precise statement, is **revised** when the corpus contradicts its wording, and is **dropped** when the article no longer makes it; for sharpened and revised claims the Evidence column also states the claim as the full corpus supports it. Evidence names the systems that decide each verdict, and parenthetical numbers such as 2608.04968 are arXiv identifiers.

### The four properties of Section 8 {#app:audit-1}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| No public system combines (a) auto-gated Loop 1, (b) cross-organization promotion, (c) versioned lineage with role-based access control (RBAC), (d) rollback | **holds** | Across the 126 second-pass systems: no system demonstrates promotion across organizations, and EvolveNet has a partial (b) inside one operator (its clients are benchmark partitions, "organizations" only in motivation), while RASO, which retrieves from a public corpus, promotes nothing; MemClaw is single-tenant in its evaluation, and Buildrix is an open community hub whose artifacts a person approves, with no failure-driven loop; (c) appears as lineage without RBAC everywhere (EDDOps, Agentic Configuration Management (ACM), MemClaw, Letta, Mem0 history) and as RBAC without versioned promotion in the MCP control planes (agentic-community gateway, TrueFoundry); (d) is demonstrated by Governed Capability Evolution and EDDOps and claimed by EvolveNet (round rollback) and EvoUndo (recoverability as admission), none of which has (a)+(b). |
| "No surveyed system meets the FedAvg limit; FederatedSkill comes closest" | **sharpened** | EvolveNet (2608.04968) comes nearer: it broadcasts a shared harness, optimizes it locally at each client, merges on the server only when the merge fixes at least as many held-out items as it breaks, and rolls back to the previous shared harness after a failed round. It is still selection and merge over program edits, not averaging, so neither it nor FederatedSkill meets the FedAvg limit. |
| Fourth conclusion on the research families: "FederatedSkill comes closest … narrowed on one property, closed on none" | **revised** | The two closest approaches are FederatedSkill (decision log; no gate at the receiving client) and EvolveNet (held-out merge gate and round rollback; no lineage or RBAC). The gap is narrowed on (b) and (d) by different systems and closed on none (Table REF(tab:IX-1)). |
| "no member of the Section REF(sec:families) research families provides (d), and only FederatedSkill provides even a partial (b)" | **revised** | (d) appears in EvolveNet (round rollback), SkillSmith and SkillAudit (edit-level rollback inside one agent), Growing Harness, WDA, and Co-Harness (rollback within an optimization run; Co-Harness adds a partial (c), a versioned diff registry without access control), and EvoUndo (recoverability as an admission test); EvolveNet provides a partial (b). Rollback appears inside single deployments and inside one federated round; no system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion. |

### Matrix cells {#app:audit-2}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| "Three cells are populated; the rest are empty for structural reasons" | **revised** | Single-loop and governance-only systems occupy these cells, under the definition of Section REF(sec:loop) that a gate records who decides and not who supplies the candidate: [None × Human] (MCP registries: Azure API Center, agentic-community MCP Gateway & Registry, TrueFoundry; Buildrix; the Anthropic skills repository; ACM), [Human × None] (VerificAgent, SkillChain's second-stage reflection gate, Davis et al. governance conversion), [Auto × None] (Letta's ungated push; Mem0 Platform, TOKI, Learning on the Job, RASO), [None × Auto] (Governed Capability Evolution; EDDOps, with a sign-off after the threshold), [None × None] (SkillRL and SkillForge, failure-driven skill loops that run unchecked; Official MCP Registry; Enoch's migration protocol; Continual Harness's unchecked self-edit; the revocation guard). Two cells hold every audit passer whose promotion has a gate, a third holds the governance-first platforms, Letta passes with no promotion gate, and the human-gated row holds only curation (Section REF(sec:design)). |
| "[Human × Auto] is empty by engineering logic … no published example exists" | **holds** | No system in the full corpus puts a person on the local gate of a failure-driven loop and promotes by program. MCP Gateway & Registry adds an automated security scan to a human admission, but it has no failure-driven local loop, so it sits in [None × Human]. |
| "[Human × Human] is empty in the surveyed corpus" | **holds, after re-coding** | The registries and the community hub that a first reading places here have no failure-driven loop and sit in [None × Human] (first row). The occupant the first-pass draft predicted, solo or small-team workflows, is documented by "Who Maintains Agent Skills?" (2609.05677): across five public skill repositories every substantive edit is human-authored and human-merged, 62% are AI co-authored, and there is 1 deprecation in 254 edits; that shape is [None × Human] too, because no loop fires from session signal (Section REF(sec:design)). |
| "[Human × None] is structurally improbable" | **revised** | VerificAgent (agent-drafted memories, human fact-check, frozen bank), SkillChain's second-stage human reflection gate, and the Davis et al. governance conversion occupy the cell. It is the human-curation cell, single-loop by construction. |
| "Nearly every auto-gated system fires at n = 1" (accepts an edit on a single evaluation) | **revised** | Batched or statistical acceptance is common, and has been since mid-2026: SAGE-gate (paired per-item test), Future AGI (paired bootstrap CI), AutoSaddler (mini-batch failure signals), MGM, ModularRSI (evidence across tasks), VaG (3-of-3 critics), EvolveNet (fixed ≥ broken on held-out), VACE, HackProbe, PROCTOR. Evidence is batched before acceptance, with SAGE-gate and VaG as instances (Section REF(sec:findings)). |
| "no surveyed system has formalized agreement as a k-of-n acceptance rule" | **revised** | VaG requires all three heterogeneous critics to pass (3-of-3), and SkillSpec is consensus-gated, so agreement-based acceptance exists. The distinction between agreement and averaging stands: under agreement the false-accept rate decays as $p^k$, under averaging the variance decays as $1/k$ (Appendix REF(app:gates)). |
| "Only AlphaEvolve demonstrates explicit multi-layer depth" | **sharpened** | HarnessBank, JIT-Agent, and MGM keep archives for lineage, and VaG adds tiered subset selection; none pairs a cascade evaluator with a diversity archive. AlphaEvolve is the only system that combines the two. |

### "Only" and "first" {#app:audit-3}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| CORAL "the only asynchronous multi-agent Loop-2 mechanism in the corpus" | **revised** | Evo2Team (2609.34135) promotes routing and communication skills across teams of 4–32 agents with target-side confirmation, and ShareMem pools memory across users. CORAL is the only such mechanism among the systems classified before the second pass; in the full corpus Evo2Team and ShareMem add cross-team and cross-user promotion without versioning (Appendix REF(app:families-8)). |
| AlphaEvolve Strassen claim | **holds** (attributed) | The claim is AlphaEvolve's reported improvement on Strassen's algorithm for 4×4 matrix multiplication. The result is taken from the AlphaEvolve report and was not independently measured; with that attribution in the same sentence, the claim holds. |
| "CASCADE reports the largest within-benchmark ablation gain in the corpus" | **dropped** | Not established for the 126 second-pass systems, and ablation gains measured on different benchmarks are not comparable. The article does not make the claim. |
| ChronoMem and rollback repair "the first surveyed instances of the rollback envelope" | **revised** | Memory rollback also appears in Mi-Memory (as a design) and Letta (git history), and checkpoint-rollback studies (2608.29381, 2608.15939) show rollback unsafe. VerMem keeps prior versions and soft-deleted records but has no operation that reverses an edit; the "Restore" in its tool table moves episodic fragments of the current task back into context. ChronoMem and rollback repair are among the first instances, and the checkpoint-rollback studies are the counter-evidence. |
| Cuadros "only surveyed memory system with full provenance + versioning + correction" | **holds** | The memory-governance systems of the second pass (TOKI, PPMF, TMA-NM, MemClaw, He & Yu) each carry provenance or lineage without correction loops or versioning, and the auto-gated memory loops (Recuris, MemGuard, Compiled Memory) carry no lineage, while VerMem keeps prior versions without an operation that reverts a write. |
| SkillOpt "cleanest published instance" / "first to instantiate all four simultaneously" | **sharpened** | SkillOpt-Lite (2607.03451) removes two of the four controls and matches or beats SkillOpt; VALVE instantiates a held-out gate that rejects a candidate before commit and never reverts an accepted update, and SkillSmith and SkillAudit instantiate held-out gates with edit-level rollback. SkillOpt is the first system we found that instantiates all four, and its own follow-up shows that two of them are stabilizers rather than necessities (Appendix REF(app:families-3)). |
| FederatedSkill "first … federated aggregation … first lineage record at the aggregator" | **holds** | EvolveNet (August 2026) postdates it and keeps no lineage record. |
| SkillOpt "first published cost-per-point figure" | **holds** | The full corpus contains no earlier figure. |

### Absences {#app:audit-4}

| Claim | Verdict | Evidence |
|----------------------------|----------|----------------------------------------------|
| "production deployments sit at Stage 1 or 2; none reaches Stage 3" | **sharpened** | Spotify (2609.30297) runs automated prompt and planning optimization gated by human launch and A/B metrics; this is Stage 3 on Loop 1 with a human Loop 2: production deployments that reach Stage 3 on the local loop promote behind a human gate or, in Letta's case alone, by an ungated push (Section REF(sec:loop)). SkillForge (2604.08618) stops short of it: a judge that agrees with experts more than nine times in ten flags the failed replies that drive each skill rewrite, but the rewrite is committed without an acceptance test, and support engineers review replies, not skill versions. |
| No S1 system scores 5; "no instruction system closes both loops" | **holds** | On S1, n=15 and the maximum score is 4. Adoption studies point the same way: context files raise cost by more than 20% without raising success (Gloaguen), and context files dominate configuration while skills are rare (Galster). |
| "Anthropic's skills repository is one-pool with PR review but no automated eval gate" | **holds** | The study of public skill repositories (2609.05677) observes human merges and no evaluation gate. |
| "correctable, versioned memory is rare; production memory lacks failure-triggered correction and versioned lineage" | **revised** | Letta Context Repositories (git-backed memory, every edit committed, shared memory auto-pushed), Mem0's per-memory history and feedback endpoint, and Zep's bitemporal invalidation make lineage common in production memory. Failure-triggered correction is not common, and 2609.08258 shows revoked facts still outranking their replacements in five backends. Production memory is versioned, but correction is not enforced (Section REF(sec:findings)). |
| No S5 system scores 5; "topology evolution is rare" | **sharpened** | With MAE and Memento-Skills corrected to 4 (Appendix REF(app:audit-7)), S5 has no score of 5 in either pass. Gated topology evolution exists: TOCOMAS keeps only candidates that satisfy structural invariants; Evo2Team promotes across teams; AgentGrad and HarnessForge update S5 under an evaluation gate. OptiMAS updates S5 through an LLM optimizer that reads a running validation score and reverts an edit only when its own analysis refutes it, with no keep-if-better test (its Algorithm 2 returns the last configuration, and the only programmatic check is structural validity). Topology evolution is rare and, where it exists, gated by evaluation alone except in TOCOMAS, which adds a structural invariant, and OptiMAS, where the evaluation informs the edit rather than gating it. |
| "no system matures all six at once" | **holds** | None of the 126 second-pass systems scores 5 on any substrate. |
| "Failure-triggered memory is rare in production" | **holds** | One field report exists (SIx Harness, N=1, self-reported); Letta's dreaming writes from conversation history, not from failures. |
| "Cross-customer skill promotion is nearly absent" | **holds** | ShareMem, EvolveNet, and XRepoSkill promote across users, clients, or repositories inside one operator; none promotes across customers or organizations with evidence. |
| "Memory versioning is mostly unsolved outside Cuadros et al. and ChronoMem" | **revised** | The evidence is the same as for the claim that production memory lacks versioned lineage (fourth row of this table): Letta, Mem0 history, Zep bitemporal facts, TOKI audit rows, and MemClaw supersession chains all version memory. Memory versioning is common, not confined to Cuadros et al. and ChronoMem. |
| "Scaffold-level curriculum is unspecified in nearly every surveyed system" | **sharpened** | Task-CoEvolve (variance-weighted task sampling) and AutoSaddler (mini-batch failure signals) specify it; they remain the exception. |
| "Held-out evals at Loop-2 promotion are absent" | **revised** | Receiving-side evaluation exists: ShareMem (evaluation tasks belong to a different user), XRepoSkill (independent verification in ≥2 repositories), Evo2Team (target-side confirmation; 4 of 22 transfers still fail on new graphs). VACE's held-out gate compares two harnesses on the next checkpoint of the same training run, so it is a Loop-1 check rather than receiving-side evaluation and is not counted here. EvolveNet gates the merge on a server-side held-out slice but runs no check at the receiving client, and Federated Agent Optimization (2610.01195) proposes a receiving-client gate without implementing it. Receiving-side evaluation at promotion is rare, not absent (Section REF(sec:design)). |
| Research full-auto cluster: "enterprise governance is uniformly absent" | **holds** | No second-pass [Auto × Auto] system reports RBAC or audited promotion. |
| Governance-first cluster: "no patch-local inner loop" | **holds** | EDDOps, ACM, Governed Capability Evolution, and the MCP control planes all lack an inner loop. |
| "AGENTS.md in over 60,000 repositories" | **revised** | Adoption is measured directly rather than by one repository count: a 2,853-repository study (Galster), a 128,018-project adoption study (Robbes: 22–29% of coding-agent projects), and 36,710 repositories mined for loop engineering (Lulla, 2608.21884), alongside a controlled study in which context files raise cost without raising success (Gloaguen; Section REF(sec:findings)). |
| "no surveyed system treats pruning or expiration as a first-class gated operation (outside Ratchet, SkillOpt, ChronoMem)" | **revised** | Retirement is a gated operation in at least eleven skill systems (Library Drift: retire when n ≥ 100 and contribution ≤ −0.10 with a cap of 50; SkillSmith; SkillOps; ASSAY; HiSME; SkeMex; MUSE-Autoskill; SkillMAS; SafeEvolve; Double Ratchet; SkillGen), and expiry is a product control in Mem0, Zep, and LangGraph Platform. Pruning and expiry are first-class operations; what remains rare is pruning of a promoted artifact's descendants, which VaG shows is structurally irreversible. |
| The failure surface is "largely unmitigated in production" | **holds** | Revocation is unenforced in five production backends (2609.08258), checkpoint rollback is unsafe in three frameworks (2608.29381), and 16 deployed frameworks keep no evidentiary record (Hearsay, 2609.32495). |
| Multi-sample agreement is "under-explored; SkillOpt-Lite nearest" | **revised** | The evidence is the same as for the two acceptance-rule claims of Appendix REF(app:audit-2), single-evaluation acceptance and k-of-n agreement: SAGE-gate, VaG, and SkillSpec. Agreement-based acceptance is instantiated, not under-explored (Appendix REF(app:gates)). |
| "No surveyed paper disputes the scaffold-vs-weights decomposition" | **holds** | SIA (2605.27276) updates harness and weights together but keeps them as distinct levers. |
| Credit assignment "remains unsolved in the general multi-substrate case" | **holds** | HARNESSEVO (slot attribution), AgentGrad (intervention-based), and CANTANTE (contrastive) each solve one substrate's case. |

### The three predictions of Section 5 {#app:audit-5}

Section REF(sec:signal) predicts from the signal classes which cells of the design space each class can reach, and Section REF(sec:design) confirms the predictions; the first two rows give the systems behind the two cells Section REF(sec:signal) assigns, and the third row gives those behind its claim about the reflexive gate.

| Claim | Statement | Verdict | Evidence |
|-----|-----------------------|----------|------------------------------------------|
| First | An [Auto × Auto] system whose gate estimates the loss change per edit should run on a C1 signal or a simulated C2 environment; one that works on a C4 signal should prune proposals rather than estimate | **holds** | Before the second pass: DGM, Voyager, AlphaEvolve, SkillOpt, SAGE, EvolveR, CoEvoSkills (C1 or simulated C2); NanoResearch (semantic merge, C4) and CORAL (heartbeat, C4) prune. AutoManual estimates nothing: its Builder reads each episode's trajectory and binary outcome and writes or rewrites rules by its own judgment, with no test of the edit, and its Consolidator merges and deletes rules once they exceed twelve, so it decides by a model judge over a simulated outcome (C3 over C2) and prunes, and the claim does not bear on it. SkillRL and AutoAgent no longer sit in [Auto × Auto] (Appendix REF(app:audit-7)). Second pass: EvolveNet, Evo2Team, XRepoSkill (C1 code signals or re-runnable benchmark outcomes, the simulated C2 of Section REF(sec:signal)); ShareMem (judged consolidation, C3, measured on Mind2Web); Letta (no gate). |
| Second | [Auto × Human] should hold only C2 and C3 systems, because the human on Loop 2 substitutes for the exact signal that Loop 1 lacks | **holds** | CASCADE (C3), Sierra (C2/C3), Devin (C2 merge outcome), Spotify (C3 judge locally, C2 A/B behind human launch). No C1 system occupies the cell; SkillForge, also C3, promotes nothing and sits in [Auto × None]. |
| Third | No scaffold system should yet calibrate a judged gate under the reflexive condition | **sharpened** | Three scaffold systems report calibration: SkillForge (>90% agreement), SkillChain ($\kappa$ 0.72 to 0.91), and SkillCoach (trajectory-filter consistency 82→96% against human gold). SkillCoach also audits its evolved rubric offline against human-gold references; none reports calibration maintained across continuing rubric revisions in deployment. On the weight side, no method that co-evolves a rubric or judge reports agreement with people apart from RLPR, whose reward is a probability rather than a rubric (Appendix REF(app:audit-6)). |

### The rubric-reward comparison {#app:audit-6}

Reinforcement learning from verifiable rewards trains weights on exact signals, and extending it to writing and other open-ended tasks has produced the judged gates that a C3 scaffold loop can borrow. These are weight-side methods and the corpus does not score them; Section REF(sec:signal) reads one distinction from them, whether the rubric or judge is held fixed while the policy learns or moves with it. The comparison covers fourteen papers, thirteen methods and one survey. Of the methods, eight hold the rubric or judge fixed during policy optimization and five co-evolve it. Five report a human-agreement figure. Four of them hold the gate fixed, and the fifth, RLPR, co-evolves a probability reward rather than a rubric, checked against human labels. No method that co-evolves a rubric or judge reports one.

| Gate during policy optimization | Papers | Members | Agreement with human judgment |
|--------------|----------|------------------------------------|--------------------------|
| Held fixed | 8 methods | Rubrics as Rewards, an instance-specific checklist scored by a fixed judge [@gunjal2025rubrics]; Writing-Zero, a pairwise judge trained on writing principles and frozen for policy training [@jia2025writingzero]; reference-guided evaluation [@shi2026references]; an essay scorer trained against a fixed rubric of binary items [@jin2026rlaes]; a study of cheap training-time verifiers [@plesner2026cheapverifier]; Rubric-Grounded RL, the Open Rubric System, and query-specific rubrics learned from human preferences [@bhattarai2026rubricgrounded; @jia2026openrubric; @lv2026queryrubrics] | Reference-guided evaluation reaches 79.1% agreement with human annotations; the essay scorer reaches a quadratic weighted kappa of 0.803 against a single human rater's 0.805; the cheap-verifier study calibrates against language-model golden judges, not people |
| Co-evolved with the policy | 5 methods | RLPR, scoring by the policy's own probability of a fixed reference [@yu2025rlpr]; Rubric-ARM, alternating updates of a rubric generator and a judge at the reward-model stage [@xu2026rubricarm]; EvoRubrics, SCORE, and RubricEM, updating rubrics adversarially or from a rubric buffer within training [@ding2026evorubrics; @zhu2026score; @li2026rubricem] | RLPR only, for its probability reward against human labels; no method that co-evolves a rubric or judge reports a figure |
| Survey | 1 survey | A survey of rubric evaluation, which names the dynamic regime as the trend [@chen2026rubricsurvey] | — |

The only co-evolving method with a human-agreement figure, RLPR, co-evolves a probability reward, not a rubric. No method that co-evolves a rubric or judge reports agreement with people. That is the reflexive-gate problem of Section REF(sec:signal), seen from the weight side.

### Recount of the full corpus {#app:audit-7}

The full corpus holds 256 unique systems, 130 from the first pass and 126 from the second; 204 form the core corpus and 52 the contrast corpus. None of the 126 second-pass systems scores 5 on any substrate. The composite two-loop audit passes 11 research systems and 3 industry exemplars: Sierra Agent OS 2.0, Cognition Devin, and Letta's Context Repositories, whose shared-memory push carries git lineage but no gate. The 6 second-pass systems that promote across contexts with no versioning or lineage on the promoted artifact are EvolveNet, Evo2Team, XRepoSkill, ShareMem, Spotify, and Future AGI. Of these, EvolveNet alone carries rollback and so enters under the governance relaxation of Appendix REF(app:data); the first five enter only if the audit drops its governance requirement altogether; Future AGI's evidence is T5 only, so it enters not at all.

Two first-pass rows are corrected before the recount. The row "Governed Collaborative Memory / SSGM" conflated Cuadros et al. (2605.04264) with SSGM (Lam et al., 2603.11768); it is split, and SSGM, a conceptual framework, scores 2. MAE and Memento-Skills were scored 5 on S5 in the released CSV while the first-pass draft's table said no orchestration system reaches 5; both close one loop only and score 4 under the uniform rubric, which moves the first-pass S5 mean from 2.68 to 2.58.

Nine second-pass rows had their gate labels re-coded on 2026-10-08 under the definition of Section REF(sec:loop), which records who decides and not who supplies the candidate: Letta's Loop-2 label moved from Auto to None (an ungated git push of shared memory; the row still passes the composite audit on its lineage); the Loop-1 label of Azure API Center, the agentic-community MCP Gateway & Registry, the Official MCP Registry, TrueFoundry, Buildrix, the revocation guard, and "Who Maintains Agent Skills?" moved from Human to None (artifacts registered or authored by people, with no failure-driven loop), and Enoch's checkpoint-and-validate protocol moved to None on both loops (a migration of one agent's state, not a promotion). The MCP Gateway's Loop-2 label now records its automated admission scan beside the human approval, and the field study's Loop-2 label records that maintainers merge. No score changed; the cells of Section REF(sec:design) and Appendix REF(app:contrast-2-1) follow the re-coded labels.

Five more rows were corrected on 2026-10-08 after a reading of the full texts against the same definition. RASO's Loop-2 label moved from Auto to None: it accepts a rewritten skill only if the rewrite beats the incumbent on a validation split, but the optimized skill never leaves the task, and its use of a public corpus is inbound retrieval, not a promotion. Three first-pass systems leave the composite audit. SkillForge moves from [Auto × Human] to [Auto × None]: its judge flags the failed replies that drive each skill rewrite, the rewrite is committed without an acceptance test, its support engineers review replies and not skill versions, and no skill version leaves the scenario deployment. On the final consistency pass SkillForge moved on to [None × None], since nothing tests its rewrite, the same reading that places SkillRL there. SkillRL's Loop-1 label is None: a per-category success rate below 0.4 triggers new skill proposals, and the skill bank takes each one as an unconditional union, a step that runs unchecked. AutoAgent moves from [Auto × Auto] to [Auto × None]: its analyzer accepts text revisions on an uncalibrated consistency judgment, and each revision stays, unversioned, in one agent's own store. Co-Harness's governance entry now records a partial (c), its versioned diff registry, and (d) within one run, and its signal class records C1 for the held-out gate beside C2 for attribution. The audit therefore passes 11 research systems rather than 14, [Auto × Auto] holds ten research systems rather than twelve, the [Auto × Human] cell of Appendix REF(app:contrast-2-1) holds CASCADE, Sierra Agent OS 2.0, and Cognition Devin, and six systems rather than seven promote without lineage. No score changed.

The recount runs over all substrate-level rows and gives the counts of Table 2 of the main article; its last line is the first pass alone (systems / core / contrast) after the two corrections.

```{=latex}
\begingroup\footnotesize
```

```
rows: 269  unique systems: 256  core: 204  contrast: 52
substrate            n   mean  score-5 systems
INTEGRATED           52   3.81  AutoAgent, NanoResearch, SkillRL
S1_Instructions      15   3.07  (none)
S2_Skills            50   3.34  COSPLAY, SAGE
S3_Memory            50   3.06  Governed Collaborative Memory (Cuadros et al.)
S4_Tools             20   3.65  Harvey, Hippocratic AI, MCP
S5_Orchestration     37   3.08  (none)
S6_Governance        45   3.02  AGENTS.md / AAIF, Braintrust, LangSmith Hub, Vellum
First pass alone (after corrections): 130 / 99 / 31; S5 mean 2.58.
```

```{=latex}
\endgroup
```

## Extended related work {#app:related}

The main article makes four design commitments that another survey could make differently: it classifies systems by whether a feedback loop closes over a persisted artifact, rather than by which mechanism is edited; it labels the gate on each of two loops as algorithmic, human, or absent; it classifies the signal that feeds the gate by verifiability; and it audits governance against four named properties. Each commitment meets a separate line of prior work. This section traces what each line established, the setting it assumed, and the condition that changes here, so that a reader can see the differences without the article having to argue for them. Every description below is taken from the cited work's own abstract, method section, or documentation; the evidence record is released with the article.

### Loop closure as the unit of classification {#app:related-1}

The surveys of self-evolving agents organize the field by what is evolved and when. Gao et al. [@gao2026selfevolving] ask what, when, how, and where to evolve, with a timing axis that separates adaptation inside a test-time episode from adaptation between episodes, and they note that a human in the loop can validate a newly created tool. Fang et al. [@fang2025comprehensive] give a unified frame of system inputs, agent system, environment, and optimizers, and cover single-agent, multi-agent, and domain-specific settings. Zhou et al. [@zhou2026selfevolvingcoding] taxonomize 108 self-evolving coding methods by evolution target, timing, and code-specific signal, and they come closest to a gate: their admission rule accepts an update when it improves a metric by a margin and passes a check, and they observe that a passing test "checks only selected behavior". Ren et al. [@ren2026selfimprovementsurvey] describe an agent as a foundation model times an operational scaffold and treat self-improvement as a self-induced update operator organized by target and driving signal. Surveys of agent memory [@du2026memory; @huang2026secondhalf; @luo2026storage], context engineering [@mei2025context; @hua2025context2], and agent skills [@zhou2026agentskills; @ding2026skilleval; @xia2026harnessing] do the same for their substrate: each catalogues mechanisms and, in the skills surveys, lifecycle stages.

What this line established is the inventory. The substrates this article scores are the ones these surveys name, and the mechanisms it finds in the corpus are the ones they catalogue. The setting they assume is a mechanism-centered one: a system is described by what it edits. The condition that changes here is the question asked of each system. Whether a loop closes at all, whether it closes under a gate, and whether a second loop promotes the result are properties that the mechanism inventory does not determine, and they are what the two-loop audit of Section REF(sec:method) measures. Zhou et al.'s admission rule is the nearest precedent for the gate; it is stated for one domain, code, where the check is a test, and this article asks what the rule becomes when the check is a judge or a delayed outcome.

### The gate as algorithmic, human, or absent {#app:related-2}

Three lines bear on gate type. The first is prompt and program optimization, which a reader will expect to see named. APE treats the instruction as a program and selects among LLM-proposed candidates [@zhou2022ape]; ProTeGi forms natural-language "gradients" from minibatches that criticize the current prompt and searches edits with beam search [@pryzant2023protegi]; OPRO has the language model propose new instructions from a prompt that lists previous candidates with their scores and reports gains of up to 8% on GSM8K and up to 50% on Big-Bench Hard over human-designed prompts [@yang2023opro]; EvoPrompt applies evolutionary operators to a prompt population and improves it against a development set, with gains of up to 25% on BBH across 31 datasets [@guo2023evoprompt]; Promptbreeder evolves task prompts and the mutation prompts that modify them, evaluated on arithmetic and commonsense reasoning and on hate-speech classification [@fernando2023promptbreeder]. DSPy compiles pipelines of language-model calls into text-transformation graphs and optimizes each pipeline to a metric by creating and collecting demonstrations [@khattab2023dspy], MIPRO proposes instructions and demonstrations jointly for multi-stage programs under a stochastic mini-batch surrogate [@opsahlong2024miprov2], TextGrad backpropagates textual feedback through the variables of a compound system [@yuksekgonul2024textgrad], and Trace generalizes the pattern to any computation whose execution trace can be shown to an optimizer [@cheng2024trace]. This line established that a development-set score is a usable gate for an algorithmic proposer and that the proposer can be the model itself. The setting it assumes is a single optimization run against a fixed task distribution. The condition that changes here is persistence and scope: these optimizers produce a prompt or program as the optimizer's output, not a versioned deployment artifact edited from session signal and promoted under a second gate. That is why OPRO and TextGrad score below the core-corpus threshold and DSPy, which persists only optimizer state, closes no second loop; Appendix REF(app:contrast-1) lists all three. SkillOpt is the point where the lineage crosses into the corpus, by adding a persistent skill document, a held-out acceptance gate, and a rejected-edit buffer to the same proposer (Sections REF(sec:findings) and REF(sec:families)).

The second line optimizes the scaffold as a whole rather than one prompt, and it is the nearest precedent for the loop of Section REF(sec:loop). Agent symbolic learning treats prompts, tools, and the pipeline that connects them as symbolic parameters and updates them with textual losses and gradients [@zhou2024symbolic]; STOP has a scaffolding program recursively rewrite the code that improves it [@zelikman2023stop]; a self-improving coding agent edits its own harness and raises its benchmark score as a result [@robeyns2025sica]; and workflow search optimizes the orchestration graph itself, by node and edge optimization over agent graphs [@zhuge2024gptswarm] or by tree search over code-represented workflows [@zhang2024aflow]. These established that the whole scaffold is an optimizable object and that textual feedback can drive its updates. Each runs within one deployment under a benchmark score, with no promotion to other deployments and no governance of the artifact it produces; the two-loop audit of Section REF(sec:method) is the measurement of exactly those two absences.

The third line is the classic single-loop agents and their memories: Reflexion's verbal reinforcement into episodic memory [@shinn2023reflexion], the reflection-and-importance memory of generative agents [@park2023generative], Voyager's growing skill library [@wang2023voyager], the experience bank ExpeL extracts from training tasks [@zhao2024expel], MemGPT's virtual context management [@packer2023memgpt], Agent Workflow Memory's induced and reused workflows [@wang2024awm], the Zettelkasten-style organization of A-MEM [@xu2025amem], the persistent test-time memory of Dynamic Cheatsheet [@suzgun2025cheatsheet], the evolving context playbook of agentic context engineering [@ace2025agentic], and the in-context iteration of Self-Refine and ReAct [@madaan2023selfrefine; @yao2023react]. They established that a frozen model can improve across episodes through an artifact it writes, and the cognitive-architecture framing of Sumers et al. [@sumers2023coala] gave that artifact the episodic, semantic, and procedural division this article's memory substrate uses. Reflexion, generative agents, Voyager, ExpeL, MemGPT, Agent Workflow Memory, A-MEM, Dynamic Cheatsheet, and the context playbook persist the artifact and close Loop 1; Self-Refine and ReAct do not persist it. None promotes the artifact beyond the agent that wrote it, which is the absence the second loop of this article is defined to measure.

### Verifiability of the feedback signal {#app:related-3}

No surveyed work classifies systems by the verifiability of the signal that feeds the gate, but three lines come near it. Guo et al. [@guo2026harness] note that software engineering provides mechanical feedback, in the form of builds, unit tests, linters, and execution logs, that most other domains lack; Zhou et al. [@zhou2026selfevolvingcoding] note that even a passing test is incomplete feedback. The judged end of the spectrum has its own measurements: language-model judges agree with human preference at rates that make them usable evaluators of open-ended answers [@zheng2023judge], a proxy reward optimized past a point lowers the true score [@gao2023overoptimization], and people who grade model outputs revise their own criteria as they grade, so that the evaluator drifts along with the evaluated [@shankar2024validators]. The second line is the weight-side effort to extend reinforcement learning from verifiable rewards into domains without verifiers. Rubrics as Rewards generates an instance-specific checklist before training and scores responses with a fixed judge [@gunjal2025rubrics]; Writing-Zero trains a pairwise generative judge on writing principles and holds it fixed during policy training [@jia2025writingzero]; reference-guided evaluation reaches 79.1% agreement with human annotations across the datasets its authors test [@shi2026references]; an essay scorer trained against a fixed rubric reaches a quadratic weighted kappa of 0.803 against a single human rater's 0.805 [@jin2026rlaes]. A second group moves the gate with the policy: RLPR scores by the policy's own probability of a fixed reference [@yu2025rlpr], Rubric-ARM alternates updates of a rubric generator and a judge [@xu2026rubricarm], and EvoRubrics, SCORE, and RubricEM update rubrics adversarially or from a rubric buffer within training [@ding2026evorubrics; @zhu2026score; @li2026rubricem]. The groups part on human calibration: among the methods that move the gate with the policy, only RLPR, whose reward is a probability rather than a rubric, reports agreement with human labels, and no method that co-evolves a rubric or judge does (Appendix REF(app:audit-6) gives the tally). One study calibrates its verifier against language-model golden judges rather than people [@plesner2026cheapverifier], and a survey of rubric evaluation names the dynamic regime as the trend [@chen2026rubricsurvey].

This line established the gate constructions for judged signals: checklists, references, pairwise judges, and rubric buffers. The setting it assumes is weight-space optimization with the policy as the learner. The condition that changes here is the learner: when the scaffold is what learns, the rubric is itself a scaffold coordinate, so the fixed-versus-co-evolved distinction becomes the question of whether a gate under edit can be calibrated at all. The article borrows the constructions and the distinction; it does not score the methods.

### Governance: lineage, access control, rollback, and promotion across organizations {#app:related-4}

Three lines bear on the four-property audit. The first is governance surveys. Ding et al. [@ding2026alwayson] code 435 works on six dimensions per state item, including provenance and recoverability, and find the literature "concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it". Lin et al. [@lin2026memorysecurity] organize memory security by lifecycle phase and name five primitives, among them principal-scoped retrieval and rollbackability. Neither carries a promotion dimension, and neither scores whether an inner loop fires from session signal.

The second line is the systems that come closest to the four properties. FederatedSkill exchanges semantic skill diffs between clients that are agent instances under one operator, and a server-side evolution agent applies, adapts, or rejects each patch per client while writing an auditable decision log of source patch, reward, and justification; it reports up to 44.4% higher success than isolated self-evolution across 20 task families [@yang2026federatedskill]. EvolveNet broadcasts a shared harness, optimizes it locally at each client, and merges only when a merge fixes at least as many held-out items as it breaks, rolling back to the previous shared harness after a failed round; its authors describe clients as spanning users and organizations, evaluate on benchmark partitions, and note that a program edit can itself encode client information [@nie2026evolvenet]. The registries supply the remaining properties without an inner loop: EDDOps promotes through automatic evaluation thresholds and human sign-off with supersession lineage and emergency rollback, and does not implement role-based access control [@kang2026registry]; Agentic Configuration Management keeps immutable revisions and baselines that enable rollback [@quessadavial2026acm]; Governed Capability Evolution gates activation and rolls back on monitoring, recovering in 72.4% of drift cases in its proof of concept [@qin2026governed]; and the MCP control planes add role-based access and quarantine without an evaluation gate [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]. Letta's Context Repositories commit every memory edit to git and push shared memory across agents without a gate [@letta2026memfs].

The third line is federated learning. FedAvg averages client updates in parameter space [@mcmahan2017fedavg], DP-FedAvg adds user-level differential privacy [@mcmahan2018dpfedavg], the field's open problems are catalogued in Kairouz et al. [@kairouz2021federated], and PromptFL moves the federated object from weights to a shared prompt that participants learn cooperatively [@guo2022promptfl]. The setting is numeric updates that are comparable by construction. The condition that changes here is the artifact: scaffold promotion is selection and merge over symbolic objects, and the nearest systems aggregate program edits with a language model rather than by averaging, which is why the article uses the federated analogy only as a limit.

### What is and is not new {#app:related-5}

The ingredients have precedent, and the article says so. The six substrates are the inventory of the self-evolving-agent, memory, context, skill, and harness surveys, and the memory taxonomy is CoALA's. The gate as a development-set score is the prompt-optimization lineage; the scaffold as an optimizable object is agent symbolic learning, STOP, and workflow search; the persisted artifact that closes Loop 1 is Reflexion, Voyager, and the agent-memory line; the admission rule with a margin and a check is Zhou et al.'s; the gate constructions for judged signals are the rubric-reward line; provenance, recoverability, and rollback as governance dimensions are Ding et al. and Lin et al.; federated aggregation of artifact patches is FederatedSkill and EvolveNet. What is new is the combination and the measurement: a corpus of 256 systems scored on one rubric and released; a classification of each by which of two loops it closes and under which gate type; a classification of the signal that feeds the gate into four verifiability classes, with the demonstration that the class fixes the reachable cells of the design space and the dominant failure; and an audit of every system against four governance properties, with the finding that none meets all four and that the two nearest, FederatedSkill and EvolveNet, each narrow different properties without meeting the set. These are the claims of the abstract and the introduction. Three limits bound them: scoring is single-rater over public evidence of uneven strength (Section REF(sec:method)), the corpus closes at the October 2026 cutoff, and the evidence is the published behavior of the 256 systems rather than new experiments (Section REF(sec:intro)).

## Full score table {#app:scores}

Every scored (substrate, system) row of the corpus: 130 systems scored by May 2026 and 126 added by the October 2026 sweep. Scores follow the 0–5 rubric of the main text (Table 1); Loop 1 / Loop 2 gate types and signal classes are recorded for the October rows (the gate pairs of the first-pass systems audited under the composite criterion are in the matrix of Appendix REF(app:contrast-2-1)). Substrate codes: INT integrated, S1 instructions, S2 skills, S3 memory, S4 tools, S5 orchestration, S6 governance. A year of “—” marks a classical system that predates the survey window. The CSV files with per-row justifications are released as ancillary files with this preprint.

```{=latex}
\begingroup\scriptsize
```

| Sub. | System | Score | Year | Source | Loop 1 | Loop 2 | Class | Added |
|---|------------|---|---|------------|-----|-----|-----|----|
| INT | ADAS / Meta Agent Search | 4 | 2024 | arXiv:2408.08435 |  |  |  | May 26 |
| INT | Agent S / S2 | 4.5 | 2024 | arXiv:2410.08164 |  |  |  | May 26 |
| INT | Agent Workflow Memory (AWM) | 3.5 | 2024 | arXiv:2409.07429 |  |  |  | May 26 |
| INT | AlphaEvolve | 4 | 2025 | arXiv:2506.13131 |  |  |  | May 26 |
| INT | AutoAgent | 5 | 2026 | arXiv:2603.09716 |  |  |  | May 26 |
| INT | AutoManual | 3.5 | 2024 | NeurIPS 2024 |  |  |  | May 26 |
| INT | AutoSaddler | 4 | 2026 | arXiv:2608.23041 | Auto | None | C2 | Oct 26 |
| INT | CaptainAgent | 2.5 | 2024 | arXiv:2405.19425 |  |  |  | May 26 |
| INT | CASCADE | 4.5 | 2025 | arXiv:2512.23880 |  |  |  | May 26 |
| INT | ChatDev | 3 | 2023 | arXiv:2307.07924 |  |  |  | May 26 |
| INT | Co-Harness | 4 | 2026 | arXiv:2607.22688 | Auto | None | C1,C2 | Oct 26 |
| INT | CoEvoSkills | 3.5 | 2026 | arXiv:2604.01687 |  |  |  | May 26 |
| INT | Cognition Devin | 3 | 2024 | cognition.​ai |  |  |  | May 26 |
| INT | Continual Harness | 4 | 2026 | arXiv:2605.09998 | None | None | C4 | Oct 26 |
| INT | Cradle | 4 | 2024 | arXiv:2403.03186 |  |  |  | May 26 |
| INT | Darwin Gödel Machine | 4 | 2025 | arXiv:2505.22954 |  |  |  | May 26 |
| INT | Double Ratchet | 4 | 2026 | arXiv:2607.12790 | Auto | None | C3 anchored by C1 | Oct 26 |
| INT | EvolveNet | 4 | 2026 | arXiv:2608.04968 | Auto | Auto | C1,C2 | Oct 26 |
| INT | EvolveR | 4 | 2025 | arXiv:2510.16079 |  |  |  | May 26 |
| INT | ExpeL | 3.5 | 2023 | arXiv:2308.10144 |  |  |  | May 26 |
| INT | Generative Agents | 4 | 2023 | arXiv:2304.03442 |  |  |  | May 26 |
| INT | GenericAgent | 4 | 2026 | arXiv:2604.17091 | Auto | None | C2 | Oct 26 |
| INT | GITM | 3 | 2023 | arXiv:2305.17144 |  |  |  | May 26 |
| INT | HarnessBank | 4 | 2026 | arXiv:2607.13683 | Auto | None | C2 | Oct 26 |
| INT | HarnessX | 4 | 2026 | arXiv:2606.14249 | Auto | None | C2 | Oct 26 |
| INT | Hippocratic AI Polaris | 3.5 | 2024 | hippocraticai.​com |  |  |  | May 26 |
| INT | JARVIS-1 | 3.5 | 2023 | arXiv:2311.05997 |  |  |  | May 26 |
| INT | JIT-Agent | 4 | 2026 | arXiv:2608.25593 | Auto | None | C2 | Oct 26 |
| INT | Life-Harness | 4 | 2026 | arXiv:2605.22166 | Auto | None | C2 | Oct 26 |
| INT | Mendel Gödel Machine (MGM) | 4 | 2026 | arXiv:2608.07645 | Auto | None | C1 | Oct 26 |
| INT | MetaGPT | 3.5 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| INT | Mobile-Agent-E | 4.5 | 2025 | arXiv:2501.11733 |  |  |  | May 26 |
| INT | ModularRSI | 4 | 2026 | arXiv:2609.14857 | Auto | None | C2 | Oct 26 |
| INT | NanoResearch | 5 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| INT | OpenCore | 4 | 2025 | github.​com/​sibmike/​opencore |  |  |  | May 26 |
| INT | OpenHands / CodeAct | 3 | 2024 | arXiv:2407.16741 |  |  |  | May 26 |
| INT | OS-Copilot / FRIDAY | 4 | 2024 | arXiv:2402.07456 |  |  |  | May 26 |
| INT | Plan4MC | 2.5 | 2023 | GitHub/​arXiv |  |  |  | May 26 |
| INT | SAGE | 4 | 2025 | arXiv:2512.17102 |  |  |  | May 26 |
| INT | Sakana AI Scientist | 3 | 2024 | arXiv:2408.06292 |  |  |  | May 26 |
| INT | ScholarEvolve | 4 | 2026 | arXiv:2609.40169 | Auto | None | C2 | Oct 26 |
| INT | SIA | 4 | 2026 | arXiv:2605.27276 | Auto | None | C2 | Oct 26 |
| INT | Sierra Agent OS | 4 | 2024 | sierra.​ai |  |  |  | May 26 |
| INT | Sierra Agent OS 2.0 | 3 | 2025 | sierra.​ai/​blog/​agent-os-2-0 |  |  |  | May 26 |
| INT | SkillForge | 4 | 2026 | arXiv:2604.08618 |  |  |  | May 26 |
| INT | SkillMAS | 4 | 2026 | arXiv:2605.09341 | Auto | None | C2 | Oct 26 |
| INT | SkillOS | 3 | 2026 | SemanticScholar:​2653e4c7 |  |  |  | May 26 |
| INT | SkillRL | 5 | 2026 | arXiv:2602.08234 |  |  |  | May 26 |
| INT | TTHE | 4 | 2026 | arXiv:2607.08124 | Auto | None | C3 | Oct 26 |
| INT | VACE | 4 | 2026 | arXiv:2609.37105 | Auto | None | C2 | Oct 26 |
| INT | Voyager | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| INT | Workspace Optimization (DreamTeam) | 3 | 2026 | arXiv:2605.09650 | Auto | None | C1 | Oct 26 |
| S1 | AGENTS.md | 2 | 2026 | arXiv:2601.20404 |  |  |  | May 26 |
| S1 | Aider Conventions | 2 | 2024 | aider.​chat |  |  |  | May 26 |
| S1 | Claude Code CLAUDE.md | 4 | 2025 | docs.​anthropic.​com |  |  |  | May 26 |
| S1 | Cody / Sourcegraph | 2 | 2024 | sourcegraph.​com |  |  |  | May 26 |
| S1 | Continue.dev Rules | 3 | 2024 | docs.​continue.​dev |  |  |  | May 26 |
| S1 | Cursor Rules | 3 | 2024 | docs.​cursor.​com/​rules |  |  |  | May 26 |
| S1 | GitHub Copilot Custom Instructions | 3 | 2024 | docs.​github.​com |  |  |  | May 26 |
| S1 | GRACE | 4 | 2026 | arXiv:2607.09175 | Auto | None | C2 | Oct 26 |
| S1 | Lovable Knowledge | 2 | 2024 | docs.​lovable.​dev |  |  |  | May 26 |
| S1 | Meta Context Engineering (MCE) | 4 | 2026 | arXiv:2601.21557 | Auto | None | C2 | Oct 26 |
| S1 | Replit replit.md | 4 | 2025 | docs.​replit.​com |  |  |  | May 26 |
| S1 | Spotify conversational-recommendation loop | 4 | 2026 | arXiv:2609.30297 | Auto | Human | C3 | Oct 26 |
| S1 | VS Code Copilot Instructions | 3 | 2024 | code.​visualstudio.​com |  |  |  | May 26 |
| S1 | Windsurf Cascade Rules | 3 | 2024 | docs.​windsurf.​com |  |  |  | May 26 |
| S1 | Zed AI Rules | 3 | 2024 | zed.​dev/​docs |  |  |  | May 26 |
| S2 | AgentVerse | 1 | 2023 | arXiv:2308.10848 |  |  |  | May 26 |
| S2 | Anthropic Claude Agent Skills | 3 | 2025 | anthropic.​com/​engineering |  |  |  | May 26 |
| S2 | Anthropic/skills GitHub repo | 2 | 2025 | github.​com/​anthropics/​skills |  |  |  | May 26 |
| S2 | ASSAY | 4 | 2026 | arXiv:2606.15390 | Auto | None | C2 | Oct 26 |
| S2 | AutoSkill | 3 | 2026 | arXiv:2603.01145 | Auto | None | C3 | Oct 26 |
| S2 | Buildrix | 3 | 2026 | arXiv:2606.25139 | None | Human | C3 | Oct 26 |
| S2 | ChatGPT Plugins (legacy) | 1 | 2023 | openai.​com |  |  |  | May 26 |
| S2 | Claude Code Skills | 3 | 2025 | docs.​anthropic.​com |  |  |  | May 26 |
| S2 | COSPLAY | 5 | 2026 | arXiv:2604.20987 |  |  |  | May 26 |
| S2 | CrewAI Skills | 2 | 2025 | docs.​crewai.​com |  |  |  | May 26 |
| S2 | HiSME | 4 | 2026 | arXiv:2605.28390 | Auto | None | C1,C3 | Oct 26 |
| S2 | HuggingFace Agent Skills | 2 | 2025 | huggingface.​co |  |  |  | May 26 |
| S2 | LangChain Skills | 2 | 2025 | langchain.​com |  |  |  | May 26 |
| S2 | Library Drift curator | 4 | 2026 | arXiv:2605.19576 | Auto | None | C1 | Oct 26 |
| S2 | Meta Context Engineering (MCE) | 4 | 2026 | arXiv:2601.21557 | Auto | None | C2 | Oct 26 |
| S2 | MetaGPT (SOP-as-skill) | 3 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| S2 | MetaSkill-Evolve | 4 | 2026 | arXiv:2607.05297 | Auto | None | C2 | Oct 26 |
| S2 | Microsoft Semantic Kernel Plugins | 2 | 2024 | learn.​microsoft.​com |  |  |  | May 26 |
| S2 | MUSE-Autoskill | 4 | 2026 | arXiv:2605.27366 | Auto | None | C1,C2 | Oct 26 |
| S2 | NanoResearch Skill Bank | 4 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S2 | OpenAI Custom GPTs / Actions | 2 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S2 | Personalized developer skills (Huang-Du-Lan) | 3 | 2026 | arXiv:2608.10319 | Auto | None | C3 | Oct 26 |
| S2 | RASO | 4 | 2026 | arXiv:2609.38024 | Auto | None | C2 | Oct 26 |
| S2 | SAGE | 5 | 2025 | arXiv:2512.17102 |  |  |  | May 26 |
| S2 | SCAFFOLD | 4 | 2026 | arXiv:2609.05511 | Auto | None | C2 | Oct 26 |
| S2 | SE-GoS | 4 | 2026 | arXiv:2609.08228 | Auto | None | C2 | Oct 26 |
| S2 | SkeMex | 4 | 2026 | arXiv:2606.09365 | Auto | None | C2 | Oct 26 |
| S2 | Skill Issues (Bauplan) | 4 | 2026 | arXiv:2606.01185 | Auto | None | C1,C3 | Oct 26 |
| S2 | SKILL.md smells (Hong-Imani-Ahmed) | 1 | 2026 | arXiv:2607.01456 | None | None | - | Oct 26 |
| S2 | SkillAudit | 4 | 2026 | arXiv:2606.14239 | Auto | None | C3,C1-partial | Oct 26 |
| S2 | SkillBoost | 4 | 2026 | arXiv:2607.26643 | Auto | None | C1 | Oct 26 |
| S2 | SkillChain | 4 | 2026 | arXiv:2606.12984 | Auto->Huma | None | C3,C2 | Oct 26 |
| S2 | SkillComposer | 4 | 2026 | arXiv:2606.06079 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillEvoReg | 4 | 2026 | arXiv:2609.30861 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillFoundry | 3 | 2026 | arXiv:2604.03964 | Auto | None | C1 | Oct 26 |
| S2 | SkillGen | 4 | 2026 | arXiv:2605.10999 | Auto | None | C2 | Oct 26 |
| S2 | SkillGLoW | 4 | 2026 | arXiv:2609.02217 | Auto | None | C2 | Oct 26 |
| S2 | SkillLift | 4 | 2026 | arXiv:2609.15396 | Auto | None | C3 inner, C2 outer | Oct 26 |
| S2 | SkillOps | 4 | 2026 | arXiv:2605.13716 | Auto | None | C2 | Oct 26 |
| S2 | SkillSmith | 4 | 2026 | arXiv:2606.01314 | Auto | None | C1,C2 | Oct 26 |
| S2 | SkillSpec (consensus-gated) | 4 | 2026 | arXiv:2610.00704 | Auto | None | C1,C2 | Oct 26 |
| S2 | SuperAGI Toolkits | 1 | 2024 | github.​com/​TransformerOptimus |  |  |  | May 26 |
| S2 | TRUSS | 3 | 2026 | arXiv:2608.17588 | Auto | None | C1,C2 | Oct 26 |
| S2 | VALVE | 4 | 2026 | arXiv:2609.32990 | Auto | None | C1 | Oct 26 |
| S2 | VCE-Skill | 4 | 2026 | arXiv:2608.16544 | Auto | None | C1,C2 | Oct 26 |
| S2 | Voyager | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| S2 | Web2BigTable | 3 | 2026 | arXiv:2604.27221 | Auto | None | C1,C2 | Oct 26 |
| S2 | Who Maintains Agent Skills? (empirical) | 2 | 2026 | arXiv:2609.05677 | None | Human | C3 | Oct 26 |
| S2 | WikiSkill | 4 | 2026 | arXiv:2608.27454 | Auto | None | C2 | Oct 26 |
| S2 | XRepoSkill | 4 | 2026 | arXiv:2609.36807 | Auto | Auto-parti | C1 | Oct 26 |
| S3 | A-MEM | 3 | 2025 | NeurIPS 2025 |  |  |  | May 26 |
| S3 | Agent-native memory system evaluation (Zhou et a | 2 | 2026 | arXiv:2606.24775 | n/a | n/a | n/a | Oct 26 |
| S3 | AIM privacy-aware interoperable memory (Johnson  | 3 | 2026 | arXiv:2609.12320 | Auto | None | C3 | Oct 26 |
| S3 | Beyond the Harness (enterprise Text-to-SQL cards | 3 | 2026 | arXiv:2608.22830 | Auto | None | C2 | Oct 26 |
| S3 | ChatGPT Memory | 3 | 2024 | openai.​com |  |  |  | May 26 |
| S3 | Claude Memory | 3 | 2025 | anthropic.​com |  |  |  | May 26 |
| S3 | Cognee | 3 | 2024 | github.​com/​topoteretes/​cognee |  |  |  | May 26 |
| S3 | Compiled Memory (Rhodes & Kang) | 4 | 2026 | arXiv:2603.15666 | Auto-gated | None | C1 | Oct 26 |
| S3 | Control-plane placement / ForgetEval (Yang) | 2 | 2026 | arXiv:2606.15903 | n/a | n/a | n/a | Oct 26 |
| S3 | FRESH failure-aware heterogeneous graph memory ( | 4 | 2026 | arXiv:2609.28003 | Auto | None | C2 | Oct 26 |
| S3 | GateMem multi-principal memory-governance benchm | 2 | 2026 | arXiv:2606.18829 | n/a | n/a | n/a | Oct 26 |
| S3 | Gemini Code Assist Memory | 4 | 2025 | cloud.​google.​com |  |  |  | May 26 |
| S3 | Generative Agents | 3 | 2023 | arXiv:2304.03442 |  |  |  | May 26 |
| S3 | Governed Collaborative Memory (Cuadros et al.) | 5 | 2026 | arXiv:2605.04264 |  |  |  | May 26 |
| S3 | HippoRAG | 2 | 2024 | arXiv |  |  |  | May 26 |
| S3 | Honest Lying mitigation / programmatic failure s | 4 | 2026 | arXiv:2605.29463 | Auto | None | C1/C2 | Oct 26 |
| S3 | KV-cache rollback consistency (Zhang & Yang) | 2 | 2026 | arXiv:2608.15939 | n/a | n/a | n/a | Oct 26 |
| S3 | LangChain Primitives (legacy) | 1 | 2023 | langchain.​com |  |  |  | May 26 |
| S3 | LangGraph Long-Term Memory | 3 | 2024 | langchain.​com |  |  |  | May 26 |
| S3 | LangGraph Store / LangMem (2026 refresh) | 3 | 2026 | docs.​langchain.​com/​oss/​python | None | None | n/a | Oct 26 |
| S3 | Learning on the Job | 4 | 2026 | arXiv:2607.22157 | Auto+​Human | None | C2,C3 | Oct 26 |
| S3 | Letta MemFS + Context Repositories + Dreaming (2 | 4 | 2026 | docs.​letta.​com/​letta-code | Auto | None | C3 | Oct 26 |
| S3 | Mem0 | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | Mem0 Platform (2026 refresh: history, feedback,  | 3 | 2026 | docs.​mem0.​ai/​api-reference | Auto | None | C3 | Oct 26 |
| S3 | MemAudit post-hoc poisoned-memory audit (Tan et  | 3 | 2026 | arXiv:2605.23723 | Auto | None | C2 | Oct 26 |
| S3 | MemClaw / Governed Shared Memory (Margalit et al | 3 | 2026 | arXiv:2606.24535 | Auto | None | C3 | Oct 26 |
| S3 | MemGPT / Letta | 3 | 2023 | arXiv:2310.08560 |  |  |  | May 26 |
| S3 | MemGuard persisted verifier signals (Wang et al. | 4 | 2026 | arXiv:2608.21867 | Auto-gated | None | C3 | Oct 26 |
| S3 | MemoryBank | 3 | 2023 | Zhong et al.​ |  |  |  | May 26 |
| S3 | Mi-Memory lifecycle framework (Liu et al.; Xiaom | 3 | 2026 | arXiv:2607.18975 | Auto | None | C3 | Oct 26 |
| S3 | MIRIX | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | MPBench memory-poisoning study (Dash et al.) | 2 | 2026 | arXiv:2606.04329 | n/a | n/a | n/a | Oct 26 |
| S3 | NanoResearch Memory Module | 3 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S3 | PPMF provenance-preserving memory firewall (Xu e | 3 | 2026 | arXiv:2607.29167 | Auto | None | C1 | Oct 26 |
| S3 | REALM retrieval-driven memory reconsolidation (S | 4 | 2026 | arXiv:2609.16053 | Auto | None | C2/C3 | Oct 26 |
| S3 | Recuris recursive experiential-working memory (Y | 4 | 2026 | arXiv:2608.24876 | Auto-gated | None | C2 | Oct 26 |
| S3 | Reflexion | 4 | 2023 | arXiv:2303.11366 |  |  |  | May 26 |
| S3 | Revocation guard / Revoked but Still Authoritati | 3 | 2026 | arXiv:2609.08258 | None | None | C1 | Oct 26 |
| S3 | Safe to Resume? checkpoint-rollback continuity ( | 2 | 2026 | arXiv:2608.29381 | n/a | n/a | n/a | Oct 26 |
| S3 | ShareMem | 4 | 2026 | arXiv:2609.32511 | Auto | Auto-parti | C3 | Oct 26 |
| S3 | SIx Harness / Memory as Infrastructure (Helwig) | 3 | 2026 | arXiv:2609.05510 | Auto | None | C2 | Oct 26 |
| S3 | SOAR Cognitive Architecture | 4 | — | Newell/​Laird |  |  |  | May 26 |
| S3 | SSGM stability-and-safety governed memory (Lam e | 2 | 2026 | arXiv:2603.11768 | None | None | n/a | Oct 26 |
| S3 | Stale constraints in inherited memory (Nakayashi | 2 | 2026 | arXiv:2608.25553 | n/a | n/a | n/a | Oct 26 |
| S3 | TMA-NM origin-bound memory authority (Louck) | 3 | 2026 | arXiv:2606.24322 | Auto | None | C1 | Oct 26 |
| S3 | TOKI bitemporal operator algebra (Wang) | 3 | 2026 | arXiv:2606.06240 | Auto or Hu | None | C3 | Oct 26 |
| S3 | Trust-scored memory sanitization (Devarangadi Su | 2 | 2026 | arXiv:2601.05504 | Auto gate | None | n/a | Oct 26 |
| S3 | Typed provenance + assertion guardrails / Stored | 3 | 2026 | arXiv:2609.02127 | Auto | None | C1 | Oct 26 |
| S3 | Utility Under Attack (Karunanidhi) | 2 | 2026 | arXiv:2608.21230 | n/a | n/a | n/a | Oct 26 |
| S3 | VerificAgent human-verified frozen memory (Nguye | 3 | 2025 | arXiv:2506.02539 | Human | None | C3 | Oct 26 |
| S3 | VerMem verifiable memory management (Sun et al.) | 4 | 2026 | arXiv:2608.03137 | Auto | None | C2/C3 | Oct 26 |
| S3 | Voyager Skill Library | 4 | 2023 | arXiv:2305.16291 |  |  |  | May 26 |
| S3 | Zep / Graphiti | 3 | 2025 | arXiv |  |  |  | May 26 |
| S3 | Zep / Graphiti bitemporal facts (2026 refresh) | 3 | 2026 | help.​getzep.​com | Auto | None | C3 | Oct 26 |
| S4 | Anthropic Tool Use API | 4 | 2024 | docs.​anthropic.​com |  |  |  | May 26 |
| S4 | Browser Tools (Playwright/Computer Use) | 3 | 2024 | anthropic.​com |  |  |  | May 26 |
| S4 | Claude Code Tool API | 4 | 2024 | docs.​anthropic.​com |  |  |  | May 26 |
| S4 | Code Interpreter | 3 | 2023 | openai.​com |  |  |  | May 26 |
| S4 | Cursor MCP Integration | 4 | 2024 | docs.​cursor.​com |  |  |  | May 26 |
| S4 | Devin / SWE-agent Tool Harness | 4 | 2024 | cognition.​ai |  |  |  | May 26 |
| S4 | Gemini Function Calling | 3 | 2024 | ai.​google.​dev |  |  |  | May 26 |
| S4 | GPT Actions | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | Harvey (Legal Vertical) | 5 | 2024 | harvey.​ai |  |  |  | May 26 |
| S4 | Hippocratic AI | 5 | 2024 | hippocraticai.​com |  |  |  | May 26 |
| S4 | LangChain Tools Abstraction | 3 | 2023 | langchain.​com |  |  |  | May 26 |
| S4 | LangGraph Tool Nodes | 4 | 2024 | langchain.​com |  |  |  | May 26 |
| S4 | LlamaIndex Tool Ecosystem | 4 | 2023 | llamaindex.​ai |  |  |  | May 26 |
| S4 | Model Context Protocol (MCP) | 5 | 2024 | modelcontextprotocol.​io |  |  |  | May 26 |
| S4 | OpenAI Assistants API | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | OpenAI Function Calling | 3 | 2023 | platform.​openai.​com |  |  |  | May 26 |
| S4 | Sierra | 4 | 2024 | sierra.​ai |  |  |  | May 26 |
| S4 | SkillSmith | 4 | 2026 | arXiv:2606.01314 | Auto | None | C1 | Oct 26 |
| S4 | Toolformer | 2 | 2023 | arXiv:2302.04761 |  |  |  | May 26 |
| S4 | ToolLLM / ToolBench | 3 | 2023 | arXiv:2307.16789 |  |  |  | May 26 |
| S5 | AgentConductor | 0 | 2026 | arXiv:2602.17100 | None | None | C2 | Oct 26 |
| S5 | AgentGrad | 4 | 2026 | arXiv:2609.08572 | Auto | None | C2 | Oct 26 |
| S5 | AgentVerse | 2 | 2023 | arXiv:2308.10848 |  |  |  | May 26 |
| S5 | AutoGen / MagenticOne | 3 | 2024 | arXiv:2308.08155 |  |  |  | May 26 |
| S5 | AWS Bedrock Multi-Agent | 2 | 2024 | aws.​amazon.​com |  |  |  | May 26 |
| S5 | Bilevel Autoresearch | 4 | 2026 | arXiv:2603.23420 | Auto | None | C1 | Oct 26 |
| S5 | CAMEL | 1 | 2023 | arXiv |  |  |  | May 26 |
| S5 | ChatDev | 2 | 2023 | arXiv:2307.07924 |  |  |  | May 26 |
| S5 | ContextEvo | 4 | 2026 | arXiv:2609.34649 | Auto | None | C2 | Oct 26 |
| S5 | Control System for Frozen Agents (Paul) | 4 | 2026 | arXiv:2607.25415 | Auto | None | C2 | Oct 26 |
| S5 | CrewAI | 3 | 2025 | docs.​crewai.​com |  |  |  | May 26 |
| S5 | Evo2Team | 4 | 2026 | arXiv:2609.34135 | Auto | Auto | C2 | Oct 26 |
| S5 | Growing Harness | 4 | 2026 | arXiv:2609.26760 | Auto | None | C2 | Oct 26 |
| S5 | HARBOR | 4 | 2026 | arXiv:2604.20938 | Auto | None | C2 | Oct 26 |
| S5 | HarnessForge | 4 | 2026 | arXiv:2606.01779 | Auto | None | C2 | Oct 26 |
| S5 | Inspect AI | 2 | 2024 | ukgovernmentbeis.​github.​io |  |  |  | May 26 |
| S5 | Institutional MAS architectures (Fei et al.) | 1 | 2026 | arXiv:2604.27691 | None | None | C2 | Oct 26 |
| S5 | LangGraph | 3 | 2024 | langchain.​com |  |  |  | May 26 |
| S5 | Letta | 3 | 2025 | letta.​com |  |  |  | May 26 |
| S5 | LlamaIndex Workflows | 2 | 2024 | llamaindex.​ai |  |  |  | May 26 |
| S5 | Memento-Skills | 4 | 2026 | arXiv |  |  |  | May 26 |
| S5 | MetaGPT | 2 | 2023 | arXiv:2308.00352 |  |  |  | May 26 |
| S5 | Microsoft Semantic Kernel | 2 | 2024 | learn.​microsoft.​com |  |  |  | May 26 |
| S5 | Multi-Agent Evolve (MAE) | 4 | 2025 | arXiv |  |  |  | May 26 |
| S5 | OpenAI AgentKit | 4 | 2025 | openai.​com |  |  |  | May 26 |
| S5 | OpenAI Swarm | 1 | 2024 | openai.​com |  |  |  | May 26 |
| S5 | OpenHands / CodeAct | 3 | 2024 | arXiv:2407.16741 |  |  |  | May 26 |
| S5 | OptiMAS | 4 | 2026 | arXiv:2608.21918 | None | None | C2 | Oct 26 |
| S5 | PluginRSI | 4 | 2026 | arXiv:2609.32423 | Auto | None | C2 | Oct 26 |
| S5 | Pydantic AI | 2 | 2024 | pydantic.​dev |  |  |  | May 26 |
| S5 | Recursive Harness Self-Improvement (RHI) | 4 | 2026 | arXiv:2607.15524 | Auto | None | C3 | Oct 26 |
| S5 | Skill-MAS (meta-skill) | 4 | 2026 | arXiv:2606.18837 | Auto | None | C2 | Oct 26 |
| S5 | TACO | 4 | 2026 | arXiv:2604.19572 | Auto | None | C2 | Oct 26 |
| S5 | Task-CoEvolve | 4 | 2026 | arXiv:2608.20169 | Auto | None | C2 | Oct 26 |
| S5 | TOCOMAS | 4 | 2026 | arXiv:2609.37953 | Auto | None | C2 | Oct 26 |
| S5 | Vertex AI Agent Builder | 4 | 2024 | cloud.​google.​com |  |  |  | May 26 |
| S5 | Workflow-Designing Agents (WDA) | 4 | 2026 | arXiv:2609.32458 | Auto | None | C2 | Oct 26 |
| S6 | Agenta | 3 | 2024 | agenta.​ai |  |  |  | May 26 |
| S6 | Agentic Configuration Management ACM (Quessada-V | 3 | 2026 | arXiv:2608.11166 | None | Human | n/a | Oct 26 |
| S6 | AGENTS.md / AAIF | 5 | 2025 | agents.​md |  |  |  | May 26 |
| S6 | Anthropic skills repo | 4 | 2025 | github.​com/​anthropics/​skills |  |  |  | May 26 |
| S6 | Azure API Center MCP registry | 3 | 2026 | learn.​microsoft.​com | None | Human | - | Oct 26 |
| S6 | Braintrust | 5 | 2024 | braintrust.​dev |  |  |  | May 26 |
| S6 | Cleric.ai | 2 | 2025 | cleric.​ai |  |  |  | May 26 |
| S6 | Competence Not Accuracy | 2 | 2026 | arXiv:2608.18719 | None | None | - | Oct 26 |
| S6 | Constitutional AI | 2 | 2022 | Anthropic |  |  |  | May 26 |
| S6 | Cursor Rules | 3 | 2024 | cursor.​com |  |  |  | May 26 |
| S6 | Decagon | 2 | 2026 | decagon.​ai |  |  |  | May 26 |
| S6 | DSPy compile | 3 | 2024 | dspy.​ai |  |  |  | May 26 |
| S6 | EvolveNet | 4 | 2026 | arXiv:2608.04968 | Auto | Auto | C2 | Oct 26 |
| S6 | EvoUndo | 4 | 2026 | arXiv:2608.28363 | Auto | None | C1 | Oct 26 |
| S6 | From Prompts to Contracts | 2 | 2026 | arXiv:2607.08028 | None | None | C1 | Oct 26 |
| S6 | Future AGI prompt lifecycle | 4 | 2026 | futureagi.​com/​blog | Auto | Auto | C3 | Oct 26 |
| S6 | GitHub Copilot enterprise | 4 | 2026 | github.​com |  |  |  | May 26 |
| S6 | Governance conversion (Davis et al. case study) | 3 | 2026 | arXiv:2607.01087 | Human | None | C2 | Oct 26 |
| S6 | Governed Capability Evolution (Qin et al.) | 3 | 2026 | arXiv:2604.08059 | None | Auto | C2 | Oct 26 |
| S6 | HackProbe | 3 | 2026 | arXiv:2609.04665 | Auto | None | C1 | Oct 26 |
| S6 | Inspect AI | 3 | 2024 | ukgovernmentbeis.​github.​io |  |  |  | May 26 |
| S6 | LangFuse | 3 | 2024 | langfuse.​com |  |  |  | May 26 |
| S6 | LangSmith Hub | 5 | 2024 | smith.​langchain.​com |  |  |  | May 26 |
| S6 | MCP Gateway & Registry (agentic-community) | 3 | 2026 | github.​com/​agentic-community | None | Human | C1 | Oct 26 |
| S6 | NanoResearch | 2 | 2026 | arXiv:2605.10813 |  |  |  | May 26 |
| S6 | Official MCP Registry | 2 | 2026 | modelcontextprotocol.​io | None | None | - | Oct 26 |
| S6 | OpenAI AgentKit Evals | 3 | 2025 | openai.​com |  |  |  | May 26 |
| S6 | OPRO | 2 | 2023 | arXiv |  |  |  | May 26 |
| S6 | Organizational Control Layer (Shi et al.) | 2 | 2026 | arXiv:2606.04306 | None | None | n/a | Oct 26 |
| S6 | Registry-Governed Agent Lifecycle / EDDOps on AW | 3 | 2026 | arXiv:2607.00345 | None | Auto+​Human | C3 | Oct 26 |
| S6 | Reward-Free Pairwise Validator | 4 | 2026 | arXiv:2607.14408 | Auto | None | C3 | Oct 26 |
| S6 | Runtime Skill Audit | 2 | 2026 | arXiv:2606.11671 | None | None | - | Oct 26 |
| S6 | Runtime-Independent Persistent Agents (Enoch) | 3 | 2026 | arXiv:2609.00546 | None | None | C1 | Oct 26 |
| S6 | SafeEvolve | 4 | 2026 | arXiv:2608.12851 | Auto | None | C3,C2 | Oct 26 |
| S6 | SAGE statistical acceptance gate (≠ SAGE 2512.17 | 4 | 2026 | arXiv:2609.36043 | Auto | None | C2 | Oct 26 |
| S6 | Self-Refine | 1 | 2023 | Madaan et al.​ |  |  |  | May 26 |
| S6 | Sierra Ghostwriter | 2 | 2026 | sierra.​ai |  |  |  | May 26 |
| S6 | SkillCoach | 3 | 2026 | arXiv:2607.01874 | Auto | None | C3,C1 | Oct 26 |
| S6 | SkillProbe | 2 | 2026 | arXiv:2603.21019 | None | None | - | Oct 26 |
| S6 | SkillSpec (intent-masked correctness) | 2 | 2026 | arXiv:2609.06052 | None | None | - | Oct 26 |
| S6 | TextGrad | 2 | 2024 | arXiv |  |  |  | May 26 |
| S6 | TrueFoundry MCP Gateway | 3 | 2026 | truefoundry.​com/​docs | None | Human | - | Oct 26 |
| S6 | Vellum | 5 | 2024 | vellum.​ai |  |  |  | May 26 |
| S6 | Verifier-as-Gatekeeper (VaG) | 4 | 2026 | arXiv:2608.05810 | Auto | None | C2 | Oct 26 |
| S6 | W&B Weave (Prompts) | 3 | 2024 | weave-docs.​wandb.​ai |  |  |  | May 26 |

```{=latex}
\endgroup
```
