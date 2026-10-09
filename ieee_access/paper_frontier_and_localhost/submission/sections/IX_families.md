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

Per-customer adapters [@hu2021lora], distilled models, and learned routing can absorb some local requirements. They also introduce separate training, evaluation, and serving lifecycles. In practice they are rare. Adaptation lands in persistent artifacts, the one substrate that is cheap, inspectable, reversible, scoped to one customer, and updatable daily.

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

The contribution here is their joint reading at deployment scope: whether an artifact persists, whether a local acceptance decision is made, which signal supports it, and what authorizes use elsewhere. The 256-system corpus, two-loop classification, feedback classes, and governance audit make that comparison explicit. An extended discussion separates these contributions from their precedents (Supplementary Material S7).
