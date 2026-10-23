## Appendix: Formal statement of artifact-layer descent {#app:formal}

This appendix states the setup behind Section REF(sec:loop), a one-step descent inequality under a noisy gate, an informal convergence statement, the optimization-analogy correspondence, and four worked cases. We claim no new theorem; the convergence statement is the ordinary target of local stochastic optimization under noisy estimators, restated for a discrete, versioned parameter.

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

Let the frontier model have fixed parameters $\theta_M$ and let the scaffold be a structured object $\theta_s \in \Theta_s = \Theta_1 \times \cdots \times \Theta_6$ over the six substrate coordinates of Section REF(sec:method); $\Theta_s$ is discrete, symbolic, and versioned. For a deployment $D$, $L_D(\theta_s) = \mathbb{E}_{x \sim D}[\ell(\pi(\theta_M, \theta_s, x))]$. A candidate edit is drawn from a proposal process conditioned on the accumulated history $H_t$ of failures, corrections, rejected outputs, evaluation regressions, and prior accepted edits: $z_t \sim Q_t(z \mid H_t, \theta_s^t)$. $Q_t$ is not uniform. A mode $m$ that recurs with frequency $f_m$ and carries per-occurrence loss $s_m$ has expected contribution $f_m s_m$ to the failure rate, so high-frequency or high-severity modes are proposed first. The finite directional difference is $\Delta_z L_D(\theta_s) = L_D(\theta_s \oplus z) - L_D(\theta_s)$; the gate sees only a noisy estimate $\widehat{\Delta}_z L_D$. The update is
$$\theta_s^{t+1} = \theta_s^t \oplus z_t \text{ if } G_t(z_t) = 1, \quad \theta_s^{t+1} = \theta_s^t \text{ otherwise.}$$

### Descent inequality

Per-step expected improvement is the gate's margin minus its estimator bias, weighted by acceptance probability. Write $\mathcal{F}_t$ for the history up to step $t$: the failures, corrections, edits, and gate decisions in $H_t$ together with $\theta_s^t$. Because the proposal $Q_t$ depends on the whole history and not on $\theta_s^t$ alone, every expectation and probability below conditions on $\mathcal{F}_t$. Assume (A1) positive descent bias on accepted edits, $\mathbb{E}[\widehat{\Delta}_{z_t} L_D \mid G_t = 1, \mathcal{F}_t] \le -\gamma_t - \tau_t$ for some $\gamma_t > 0$, and (A2) bounded estimator bias on accepted edits, $|\mathbb{E}[\Delta_{z_t} L_D - \widehat{\Delta}_{z_t} L_D \mid G_t = 1, \mathcal{F}_t]| \le \varepsilon_t$. With $p_t = \Pr(G_t = 1 \mid \mathcal{F}_t)$,
$$\mathbb{E}[L_D(\theta_s^{t+1}) \mid \mathcal{F}_t] \le L_D(\theta_s^t) - p_t(\gamma_t + \tau_t) + p_t\,\varepsilon_t.$$
In the feedback-signal classes of Section REF(sec:signal), $\varepsilon_t$ is near zero for an exact check (C1), though the sampling error of a finite suite over the patch remains; bounded by batching for an observed outcome (C2); equal to the judge's bias, and bounded only by calibration, for a judged signal (C3); and unavailable per edit for a delayed signal (C4).

### Convergence (informal)

Nothing in the survey depends on the convergence statement below. It holds under strong assumptions and is included to make gate stability precise. Add three assumptions. (A3) Proposal coverage with acceptance: at every non-gate-stable scaffold, $Q_t$ places probability at least $q > 0$ on an admissible edit with $\mathbb{E}[\Delta_z L_D] \le -\delta$, and the gate accepts such an edit with probability at least $q' > 0$, so that $p_t(\gamma_t + \tau_t) \ge q q' \delta$ there. (A4) Effective compactness of the reachable orbit. (A5) Summable bias, $\sum_t p_t \varepsilon_t < \infty$. Let $0 \le L_D \le B$. (A3) is strong: it asks for a uniform lower bound on proposing and accepting an edit that lowers the loss by at least $\delta$.

The one-step inequality is then of the Robbins–Siegmund form, a non-negative process that decreases in expectation up to a summable perturbation $p_t \varepsilon_t$, so $L_D(\theta_s^t)$ converges almost surely and $\sum_t p_t(\gamma_t + \tau_t) < \infty$ almost surely [@robbins1971convergence].

The content lies in the finite sum. A bounded loss cannot pay for infinitely many accepted edits with a positive expected margin, so under (A3) the process visits non-gate-stable scaffolds only finitely often. With (A4), the limit set of $\{\theta_s^t\}$ is gate-stable, meaning that no admissible edit clears the gate with negative expected directional loss in the limit.

The result is convergence of the loss and stability of the gate decision, not convergence to an optimum. A globally suboptimal gate-stable scaffold is consistent with it, because $Q_t$ may never propose the improving edit or $\widehat{\Delta}$ may be biased to reject it.

The argument does not cover a non-stationary deployment ($D = D_t$). Tracking a moving optimum would need further assumptions, not supplied here, on the rate of drift and of adaptation. For that case, recency weighting, pruning, expiry, and rollback are the scaffold-level analogues of the machinery used in continual learning.

### Correspondence

Table REF(tab:A-1) pairs each optimization concept with its scaffold analogue. Credit assignment here is attribution, not backpropagation: scaffold systems do not differentiate through instruction files but trace an output error to an upstream coordinate, manually or with a judge or verifier. The two formal results ask different things of that attribution. The one-step inequality needs only that accepted edits have positive expected descent. The convergence statement needs attribution reliable enough to supply the uniformly improving proposals that (A3) assumes. That requirement is much stronger than the credit-assignment condition of Section REF(sec:loop), success with non-zero probability per failure.

### Worked cases

*Retrieval.* Failures recur because retrieved context omits the decisive clause. Attribution traces the error to the retrieval coordinate: chunking, query rewriting, metadata filter, embedding model, reranker, or context-packing rule. The candidate edit tightens chunk boundaries or adds a metadata constraint, and the gate checks that recall and answer accuracy improve on the patch evaluation without degrading adjacent cases. Class C1 or C2.

*Pitch review.* The system repeatedly overrates decks that claim a large market without numbers, and the failure cluster points at an under-specified rubric coordinate. The edit changes "evaluate market size" into "require a numeric estimate and a source; if absent, cap the score"; the gate runs the revised rubric against held-out decks with human scores. What the edit changes is the gate that will judge the next edit: the reflexive gate of Section REF(sec:signal). Class C3.

*Tool use.* Calls fail because optional parameters are under-specified. The responsible coordinate may be the tool schema, the call policy, or the clarification rule. The edit adds required fields or a pre-call uncertainty check; the gate checks that tool-call failures fall without raising refusals or latency. Class C2.

*Memory.* A stale customer preference is repeatedly retrieved and causes bad decisions. The responsible coordinate is a memory entry together with its provenance, priority, and expiry policy. The edit corrects, expires, or version-tags the entry; the gate checks that future behavior improves without erasing useful history. Class C2, with the correction itself observable only through a later outcome.
