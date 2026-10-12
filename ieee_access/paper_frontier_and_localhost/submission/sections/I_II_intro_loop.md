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
\includegraphics[width=\textwidth]{fig1_descent_ieee}
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
