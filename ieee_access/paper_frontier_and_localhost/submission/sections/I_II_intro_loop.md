## Introduction {#sec:intro}

In one repository, a coding agent repeatedly uses the wrong naming convention. An engineer adds a line to the agent's instructions, and the next session follows the convention. The model has not changed, but the deployed system has. The same happens when an assistant corrects a stored preference, acquires a reusable skill, or learns which tool to call. Persistent artifacts like these, outside the model's weights, now accumulate much of the experience that makes an AI system useful in one setting.

We call this layer the **scaffold**. It includes instructions, skills, memory, tools, orchestration, and the evaluation and governance rules that control their use. In the language of compound AI systems [@zaharia2024compound], it is the part surrounding the model that a deployment can inspect and revise without retraining. The split matters because the two change on different schedules: a team can revise an instruction or tool binding as soon as a problem is understood, while a new model must go through separate training, evaluation, and release.

But because edits are easy to make, edits of unknown value are easy to accumulate. A rule added after one incident may prevent a recurring error, conflict with another rule, or merely make the prompt longer. A memory may be corrected in the history while the system keeps retrieving the outdated entry. Even a demonstrably useful edit can become harmful when copied into a deployment with different tasks or conventions. Researchers pay a different cost: without knowing whether a system tests its edits, they cannot tell whether a system described as self-improving improved anything, cannot compare two such systems, and may build on a loop with no acceptance test or no failure record.

These situations leave two questions unanswered: what evidence justifies keeping a local edit, and what additional evidence justifies sharing it? The first defines a **local loop**: identify a recurring failure, propose an edit to the responsible artifact, and test whether it helps. The second defines a **promotion loop**: decide whether another project, team, or organization should adopt the edit, and preserve enough history to reverse that decision. This survey uses those questions to examine 256 public production and research systems.

The surveyed systems have built these loops unevenly. Nearly every recently added system with a local loop has an automatic acceptance test: 89 of 96. The steps that should supply those tests with well-founded candidates are weaker: failures are often not retained in a usable form, and a failed output rarely identifies the instruction, memory, skill, or tool binding at fault. Production platforms, by contrast, have built substantial versioning and release machinery but no process that proposes edits from deployment experience.

Promotion is more fragmented. No surveyed system documents an automatic local loop connected to promotion across organizations, with versioned lineage, access control, and rollback. Shared formats and registries make artifacts portable, but they do not establish that an artifact will help its recipient. Some surveyed systems check transferred edits within one operator.

Feedback differs across systems and supports different kinds of automation. A compiler or test suite can check a candidate immediately. A booked appointment is a later, noisier outcome. A writing task may depend on a judge whose preferences can drift. A research decision may take months to evaluate. In the surveyed systems, then, the local gate is built nearly everywhere a local loop exists, the failure record and credit assignment that feed it are weaker, and governed promotion across organizations is unassembled. Feedback helps explain this pattern, and no feedback establishes an improvement beyond what it measures.

The survey develops a framework for reading its evidence, which consists of published methods and public documentation; it introduces no new experiments, and its scores and classifications are released for inspection. We define the two loops and when maintaining artifacts counts as optimization, then describe the corpus and scoring method and examine the local loop, the feedback that constrains it, and the evidence needed for promotion. The later sections consider failures that arise without gates, specify the unassembled architecture for governed promotion, and connect the findings to the research lines that produced its components.

## From a local fix to a measured improvement {#sec:loop}

Adding a naming rule after an error is reasonable, but the team learns whether it works only by rerunning the agent on relevant tasks and comparing results. If the edit helps, it should persist; if it causes regressions, the team needs a way to reject or reverse it. Repeating this process turns a growing collection of fixes into a procedure for improving the deployment.

### The local loop

The procedure starts with a record of failures: rejected answers, user corrections, failed tool calls, evaluation regressions, or unsuccessful tasks. Repeated failures are grouped into modes and prioritized by frequency and severity. For each selected mode, the system tries to identify the artifact responsible. A stale memory entry needs a different fix from a missing tool argument or an ambiguous instruction.

We call this step **credit assignment**. It links an observed failure to an editable part of the scaffold: a **coordinate**. The system then proposes a candidate edit and evaluates it against the current scaffold. The acceptance test is the **gate**. An accepted edit is retained as a versioned artifact; a later regression can trigger rollback. Fig. REF(fig:descent) shows the complete local loop.

```{=latex}
\begin{figure*}[!t]
\centering
\includegraphics[width=\textwidth]{fig1_descent_ieee}
\caption{The local improvement loop. Recurring failures guide a proposed scaffold edit. An acceptance gate tests the change before it persists, and later regressions can trigger rollback. Sharing the accepted edit requires a separate promotion decision (Fig. REF(fig:scope)).}
\label{fig:descent}
\end{figure*}
```

The gate's evaluation must be tied to the deployment's workload. A deployment serves a distribution of users, tasks, and conventions, which we call its **patch**. Its **patch loss** measures failure on that distribution. Depending on the application, the patch loss may be a task-failure rate, correction rate, retrieval error, or another operational measure. A gate can establish an improvement only as far as its evaluation estimates the patch loss.

### The second decision: whether to share the fix

Suppose the naming rule helps in the original repository and the team considers adding it to a shared template. That decision changes the population the rule will act on. Other repositories may follow a different convention, about which the local evaluation says little.

The promotion loop therefore asks for evidence at the receiving scope. We call this **receiving-side evaluation**: a check on the tasks of the deployment that would adopt the edit. The scope for which the available evaluation supports an edit is its **evidence radius**, and a local success does not automatically enlarge that radius. Section REF(sec:design) develops the scopes and examines systems that transfer artifacts between them.

### Five conditions for artifact-layer optimization

We use **artifact-layer descent** for maintenance that connects recurring failures to measured improvements by meeting five conditions:

1. **A measurable patch loss:** the deployment has a defined measure of success or failure.
2. **A failure log:** relevant failures are retained as evidence for later edits.
3. **Credit assignment:** failures can, at least sometimes, be traced to the scaffold coordinates responsible.
4. **A candidate edit:** a process proposes an edit to those coordinates.
5. **An acceptance gate:** an edit is retained or promoted only after a check tests whether it lowers the relevant loss.

These conditions distinguish three recurring forms of maintenance. In *patchwork*, an engineer adds a rule after an incident without measuring the result. In *random artifact search*, a system tests many variants and keeps a winner without tracing failures to their causes. In artifact-layer descent, the trace from failure to cause directs the proposed edit, which is tested before acceptance. Where the conditions are only partly met, the optimization interpretation is correspondingly limited.

For deployment $D$, with edits that outlast the current interaction, write the patch loss as
$$L_D(\theta_s)=\mathbb{E}_{x\sim D}\!\left[\ell(\pi(\theta_M,\theta_s,x))\right],$$
where $\theta_M$ denotes the fixed model weights, $\theta_s$ the editable scaffold, and $\ell$ the operational loss. A proposal process uses the failure history to produce an edit $z_t$. There is no analytic gradient through an instruction file or memory entry.

Instead, the gate estimates the change in loss and accepts the edit when that estimate clears a required margin:
$$G_t(z_t)=1\iff\widehat{\Delta}_{z_t}L_D(\theta_s^t)+\lambda\Omega(z_t)\leq-\tau_t.$$
Here $\Omega\geq0$ penalizes edit complexity and promotion breadth, and $\tau_t\geq0$ is the acceptance margin. An evaluation that blocks a regressing merge applies this rule in practice. A reviewer or governance process can also instantiate the gate by requiring stronger evidence for a broader or more complex edit.

Appendix REF(app:formal) gives the update rule and a one-step descent inequality under assumptions on the gate's estimation bias. Improving edits eventually stop clearing the gate under additional coverage, compactness, and summable-bias assumptions. This is **gate stability**, not a claim of global optimality. A limited proposal process or biased evaluator can leave useful edits undiscovered or rejected.

### Who proposes and who decides

Who writes an edit and who accepts it are separate roles. An agent may draft an edit that a person approves; an engineer may write an edit that an automatic evaluation rejects. We classify the gate by who decides whether to accept the edit:

- **Auto:** a program applies a check, including a verifier, evaluation threshold, or language-model judge [@zheng2023judge]. Section REF(sec:signal) asks separately whether that judge has been calibrated against people.
- **Human:** a person decides whether to accept the edit.
- **None:** nothing accepts or rejects the edit, either because the loop is absent or because every proposed edit is retained.

A pair such as [Auto × Human] denotes an automatic local gate followed by a human promotion gate. These labels describe the decision mechanism; by themselves, they do not establish that the decision is well supported.

From the loss definition, every loop inherits two limits. First, an accepted edit is evidence of improvement only on the measure and tasks evaluated. Promotion must preserve that scope or establish the improvement again. Second, the loop optimizes a defined objective. Revising the evaluator changes the objective itself, a complication we return to in Section REF(sec:reflexive), but the loop does not discover a better objective simply by accumulating edits.
