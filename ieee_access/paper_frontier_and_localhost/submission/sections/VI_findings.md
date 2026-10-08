## What the field has built {#sec:findings}

The corpus answers the question of Section REF(sec:intro) in one sentence: the local half of the loop is routine, and no surveyed system documents the governed second half. This section gives the evidence in three cuts. Per substrate, where the top mark is reached and where it is not; per missing piece, which parts of the second half are absent and in which signal class; and per cluster, which kinds of system have which half.

### The local loop is routine, and no substrate is finished

Nine in ten of the most recently added core systems close the local loop under an automatic gate, and none of them reaches the top mark on any substrate (Table REF(tab:VI-1)).

| Substrate | $n$ | Mean | Score-5 systems | Survey finding |
|------------|---:|----:|--------------------|----------------------------------|
| S1 Instructions | 15 | 3.07 | (none) | Rules persist across IDEs and agents; none closes both loops; ceiling 4 |
| S2 Skills | 50 | 3.34 | SAGE, COSPLAY | Most active research substrate; Loop 1 routinely automated; production repositories human-merged |
| S3 Memory | 50 | 3.06 | Cuadros et al. | Lineage shipped in products; enforced correction still absent |
| S4 Tools | 20 | 3.65 | MCP, Harvey, Hippocratic AI | Most mature production substrate; registries govern admission, not evaluation |
| S5 Orchestration | 37 | 3.08 | (none) | Topologies evolve under evaluation; one structurally gated instance; no two-loop system |
| S6 Governance | 45 | 3.02 | Braintrust, Vellum, LangSmith Hub, AGENTS.md/AAIF | Mature prompts-as-code; registries add lineage and rollback; no inner loop |
| Integrated | 52 | 3.81 | NanoResearch, AutoAgent, SkillRL | High-water mark; research systems without enterprise governance |

Table VI-1. Substrate maturity across the 256-system corpus. Column n counts scored rows on each substrate, Mean is the average score, and Score-5 systems reach the substrate's top mark; the integrated row counts systems scored across several substrates as one composite row. Of the most recently added 126 systems, 31 are skill systems and 102 are core; 92 of the core systems close Loop 1 under an automatic gate, and none of the 126 scores 5 on any substrate.

On the three substrates that hold adaptable content, only two systems reach the top mark, and both reach it inside one research environment. Instruction files persist across IDEs and agents (Claude Code, Cursor, AGENTS.md [@agentsmd2025], Windsurf, Continue.dev) and appear in a fifth to a quarter of coding-agent projects [@robbes2026agenticmuch; @galster2026harnessconfig], yet in a controlled study they raise inference cost by about a fifth without raising task success [@gloaguen2026agentsmd]. Skills are the most active research substrate: SAGE and COSPLAY close both halves of the loop [@wang2025sage; @wu2026cosplay], Loop 1 is routinely automated, and SkillChain's judge-approved edits pass a human reflection gate before they enter its skill bank, a two-stage local gate rather than a promotion loop [@hu2026skillchain]. Eleven skill systems treat retirement as a gated operation [@zhang2026librarydrift; @wei2026skillsmith; @pu2026skillops; @wang2026assay], and the public skill repositories are merged by hand [@shen2026whomaintains]. On orchestration, automated workflow search came first, in optimizable agent graphs [@zhuge2024gptswarm] and tree search over code-represented workflows [@zhang2024aflow]; topologies evolve under evaluation [@cheng2026optimas; @chu2026agentgrad; @chen2026harnessforge], TOCOMAS alone keeps a topology change only when it satisfies a structural invariant [@zhao2026tocomas], and Evo2Team promotes routing skills across teams [@wang2026evo2team].

Memory carries lineage without enforced correction. Production memory records its own history, in Letta's git-backed Context Repositories [@letta2026memfs], Mem0's per-memory history [@mem02026history], and Zep's bitemporal facts [@zep2026facts]. Research memory splits into write-gating and provenance on one side [@wang2026toki; @xu2026ppmf; @margalit2026governed] and verifier-gated failure loops on the other [@yu2026recuris; @wang2026memguard; @sun2026vermem]. Among the memory systems that gate writes or correct from failures, only Cuadros et al. does both, which is why it alone reaches the top mark.

Tools and governance hold the machinery of a second loop without the first, which is how they reach the top mark with no inner loop (Section REF(sec:method)). MCP registries split into catalogues, with namespaces and version records but no scanning, and control planes, with scanning, access control, and quarantine [@agenticcommunity2026mcpgateway; @microsoft2026apicentermcp; @truefoundry2026mcpgateway]; none has evaluation-gated promotion. The governance registries bring lineage and rollback [@kang2026registry; @quessadavial2026acm; @qin2026governed], and none of them has an inner loop.

No system matures all six substrates at once. Research systems learn fast and lack enterprise governance; production systems govern well and learn slowly; open standards solve artifact portability but not adaptation. This pattern is not a quirk of the corpus: it tracks which constraints each kind of system was built to satisfy.

### Where the second loop should be, five pieces are missing

Walk the second half of the loop from the failure that starts it to the promotion that ends it, and five pieces are missing or rare across the core corpus. Each is missing in a particular feedback-signal class, which is the first sign that the gap is not one gap but several.

- **Failures are not captured** (C2). Deployed memory systems record preferences and successful facts, not residuals, so the loop has nothing to cluster. The one field report of stores written from dead-ends to prevent recurrence describes a single, self-reported deployment [@helwig2026memory].
- **Which sessions inform the next edit is left to chance** (C2). Nearly every system takes failures in the order they arrive. Task-CoEvolve's variance-weighted task sampling and AutoSaddler's mini-batch failure signals are the exceptions [@miyai2026taskcoevolve; @park2026autosaddler].
- **Memory is versioned, but correction is not enforced** (C2, C3). Git-backed and bitemporal memory ship in products, and five production backends still return facts that were revoked [@shen2026revoked].
- **Promotion is rarely checked where the edit arrives** (C1, C2). ShareMem gives evaluation tasks to a different user, XRepoSkill verifies in at least two repositories, Evo2Team confirms at the target team, and VACE evaluates the candidate with the receiving model held fixed [@qi2026vace]; even Evo2Team's confirmation lets nearly a fifth of its transfers fail on new graphs. EvolveNet has no such check, and the federated optimization framework that proposes a receiving-client gate has not implemented it [@yang2026fao].
- **No promotion crosses an organization** (all classes). ShareMem, EvolveNet, XRepoSkill, and RASO promote across users, clients, or repositories inside one operator [@hu2026sharemem; @nie2026evolvenet; @guo2026xreposkill; @chu2026raso]. No system promotes across customers or organizations with evidence.

The last piece is the thesis of this article. The four before it are the reasons a system that tried to add it would have little to promote and no way to check what it promoted.

### Four kinds of system, each with half the loop

Sort the core corpus by which half of the loop it automates and four clusters appear (Table REF(tab:VI-2)). Each has one half of the loop; none has both halves governed.

| Cluster | Representative systems | Loop 1 / Loop 2 | What the cluster shows |
|------------|------------------------|----------|------------------------------|
| Research full-auto | NanoResearch, SkillOpt, SkillRL, AlphaEvolve, DGM, ADAS, Voyager, EvolveNet, Evo2Team, XRepoSkill | Auto / Auto | Both loops can run under algorithmic gates and benchmark gains compound; enterprise governance is uniformly absent |
| Production hybrid | SkillForge, CASCADE, Sierra Agent OS 2.0, Cognition Devin, Spotify's recommendation loop [@palumbo2026spotify] | Auto / Human | An algorithmic Loop-1 gate with a reviewer on Loop 2 is the production-viable cell; Spotify adds online A/B gating |
| Governance-first | Braintrust, Vellum, LangSmith Hub, EDDOps, Agentic Configuration Management, Governed Capability Evolution | None / Auto or Human | Evaluation-gated promotion, lineage, and rollback exist; candidate generation is manual and no inner loop fires from session signal |
| Open standards and registries | AGENTS.md, MCP, Anthropic Agent Skills, Cursor Rules, the MCP control planes | None / Human, or None / None | Cross-vendor convergence on artifact format and tool attachment; registries govern admission and access but do not evaluate |

Table VI-2. Four clusters of the core corpus.

*Research full-auto* systems show that the architecture works when both gates are algorithmic [@xu2026nanoresearch; @wang2026autoagent; @romeraparedes2024funsearch; @alphaevolve2025; @zhang2025darwin; @hu2024adas; @wang2023voyager]. AlphaEvolve is the clearest case: it pairs an evaluator with an evolutionary archive, as FunSearch did before it, and reports production gains at Google. EvolveNet, Evo2Team, and XRepoSkill extend the loop from a single deployment to a federation of deployments. What every member lacks is governance: no access control and no audited promotion.

*Production hybrid* systems show that the production-viable pairing is an algorithmic gate on Loop 1 with a reviewer on Loop 2. SkillForge illustrates it most plainly: a judge that agrees with people more than nine times in ten passes each skill diff, and support engineers decide whether it ships [@skillforge2026]. Sierra routes agent-generated insights through human-authored expert answers [@sierra2025os20], Devin's merged pull requests are its promotion step [@cognition2025devinreview], and Spotify launches automatically optimized prompts and plans only behind an online A/B test. In every member the human on Loop 2 does the work that the missing exact signal cannot.

*Governance-first* systems automate Loop 2 alone. The prompts-as-code platforms [@braintrust2026docs; @vellum2026docs; @langsmith2026hub] and the governance registries [@kang2026registry; @quessadavial2026acm; @qin2026governed] keep immutable versions, evaluation thresholds, and rollback, but they have no Loop 1: engineers author the candidates, and session feedback never triggers one. This is MLOps for scaffolds, distinct from MLOps for weights.

*Open standards and registries* converge across vendors on format and attachment. Claude Agent Skills, Cursor Rules, GitHub Copilot instructions, Windsurf, Continue.dev, Zed, and Replit all keep a git-tracked markdown artifact attached to a workspace with an MCP-style tool layer [@galster2026harnessconfig; @barbaste2026harnessengineering], a convergence that Section REF(sec:families) reads as evidence that the architecture is real. What the cluster lacks is adaptation: its registries govern admission and access but do not evaluate, and in the repositories that run autonomous loops, the runtime state of those loops sits outside version control [@lulla2026loopengineering].
