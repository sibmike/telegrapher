# S3. The mechanism stack and continual-learning notes

## S3.1 The mechanism stack

The update rule of Section II expands into six operations that every patch-local system performs, whether by explicit engineering or by accident.

1. **Residual capture.** Log failures, corrections, rejected outputs, user edits, evaluation regressions, and tool-call failures. This is the signal source of Loop 1; without it, $z_t$ has no provenance.
2. **Mode discovery and credit assignment.** Cluster repeated failures into the deployment's own error modes (the catalogue of *The Architecture of Errors* [@arbuzov2026architecture], instantiated locally for one patch) and attribute each mode to the scaffold coordinate responsible for it (the correspondence note of the formal appendix).
3. **Delta synthesis.** Turn a recurring mode into a candidate scaffold edit: an instruction rewrite, a new skill, a memory correction, a tool binding, an orchestration change, or an evaluation case. This produces $z_t$.
4. **Delta validation.** Estimate whether the edit lowers $L_D$ without collateral damage on adjacent inputs. The gate $G_t$ is Auto when the check is an algorithmic criterion and Human when it is reviewer judgment.
5. **Promotion control.** Decide whether the accepted edit stays in the local fork or climbs the scope hierarchy: PROJECT, STACK, TENANT, CORE. This is Loop 2.
6. **Drift and bloat control.** Expire stale rules, prune conflicting memories, roll back regressed skills, and detect overfitting. Without this operation, accumulated edits produce the scaffold-level analogue of plasticity loss.

Each operation is the locus of a separate engineering discipline, and surveyed systems implement them partially and unevenly. Research full-auto systems excel at operations 3 and 4, governance-first systems at operation 5, and production hybrids at most of operations 1 to 5 but rarely at operation 6. Implementation patterns for each operation lie outside this survey.

## S3.2 Loop 1 and Loop 2 as descent steps of different radius

Loop 1 proposes and validates local descent steps on a single $L_D$. Loop 2 widens the update radius: it selects, merges, and promotes accepted local edits so that they apply to a larger set of patch losses averaged together. Acceptance at USER scope descends on a single $L_D$. PROJECT promotion descends on a loss averaged over the project, and STACK promotion widens the average further. TENANT promotion descends on a tenant-wide average; CORE promotion, the cross-tenant level, descends on an average over tenants. The two-loop design space is therefore more than a taxonomy of engineering patterns: it records *which loss each surveyed system is descending on*, and which estimator gates the step.

## S3.3 Overfitting in scaffold adaptation

In weight training, overfitting is usually a defect. In scaffold adaptation, local overfitting is partly the point. Frontier weights are trained to preserve generality across patches, so they must smooth over local conventions and rare workflow-specific failures. A deployment's patch needs the opposite: selective specialization to its own residuals. The scaffold is therefore a layer meant to overfit, but one whose overfitting is scoped, inspectable, versioned, gated, and reversible. A scaffold edit that improves one repository, hospital workflow, or legal diligence process may degrade performance elsewhere. That is not a contradiction; it is patch adaptation. The mistake is promoting that edit beyond its evidence radius.

In non-stationary patches ($D = D_t$), the same descent mechanism tracks a moving optimum rather than converging once. Recency weighting, replay, pruning, expiry, and rollback are therefore not optional hygiene; they are the scaffold-level analogues of continual-learning machinery.

---
