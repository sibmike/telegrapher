## The missing architecture: governed cross-tenant scaffold optimization {#sec:gap}

The missing piece of the loop is governed cross-tenant promotion, the step that carries an edit from one organization to another under a gate, and four properties make it specific enough to audit for. Named as four properties, the gap becomes something a reader can check any system against, their own included, and no surveyed system holds all four.

The four properties are these:

(a) **auto-gated local loop**: the commit criterion is an algorithmic threshold;
(b) **cross-organization promotion**: the promotion loop routes artifacts between organizations (we use *cross-tenant* and *cross-organizational* interchangeably);
(c) **versioned lineage with access control**: promoted artifacts carry versions, audit trails, and role-based access policies;
(d) **rollback**: a bad promotion can be reverted without redeploy.

All four describe the artifact: how it is made and how far it may travel. Receiving-side evaluation, the check without which no promotion is safe, is not among them, because it is a property of the gate where the edit arrives rather than of the artifact. Section REF(sec:design) records where that check exists, and the architecture below includes it as its third part.

The closest approaches split the four properties among them. No row of Table REF(tab:IX-1) is full on promotion across organizations.

| System | (a) auto-gated local loop | (b) cross-organization promotion | (c) versioned lineage with access control | (d) rollback |
|--------------|------------------|----------------------|--------------------|----------------|
| FederatedSkill [@yang2026federatedskill] | full | partial: privacy-preserving aggregation of skill edits across heterogeneous clients that sit under one operator | partial: auditable per-modification decision log | none |
| EvolveNet [@nie2026evolvenet] | full | partial: held-out merge gate at the aggregator, but clients are benchmark partitions, not organizations | none: no lineage, no access control | full: rollback to the previous shared harness after a failed round |
| SkillForge [@skillforge2026] | none: a calibrated judge selects the failures, nothing tests the rewrite | none: skill versions stay in the scenario deployment | partial | not documented |
| Governance-first registries [@kang2026registry; @qin2026governed; @quessadavial2026acm] | none: no inner loop | none | partial: lineage without access control | full, with evidence |
| MCP control planes [@agenticcommunity2026mcpgateway] | none: no inner loop | none | partial: access control without lineage | not reported |

Table IX-1. The closest approaches to governed cross-organization scaffold optimization, scored against the four properties.

The partition is sharp. The two federated systems carry the automatic gate and part of the promotion. SkillForge carries a calibrated judge and part of the lineage, but no acceptance test and no promotion. The registries carry lineage and rollback without a local loop, and the control planes carry access control alone. Rollback exists inside one federated round and, as Section REF(sec:findings) records, inside single deployments; no system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion (Supplementary Material S4).

In machine-learning terms, what is missing is a cross-tenant aggregator with an automated evaluation gate at the scaffold layer. It would carry five parts: per-tenant artifact pools, each tagged with provenance; an aggregation step across tenants that respects tenant isolation; a held-out evaluation at the receiving tenant that blocks a promotion whenever it does not lower that tenant's patch loss; versioned lineage with access control; and a rollback envelope on every promoted artifact. The federated-learning analogy [@mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated] is useful only in the limit where artifacts are mergeable update representations. Federated prompt tuning, in which participants learn a shared prompt rather than shared weights [@guo2022promptfl], is the weight-side precedent closest to that limit. In surveyed practice the promotion loop is selection and merge: the nearest systems aggregate program edits with a language model, not by averaging.

Whether the architecture *should* be built depends on the feedback-signal class, not on the application domain (Section REF(sec:signal)). Where the signal is an exact check, automatically gated cross-tenant promotion of a test-validated skill would be low-risk, and receiving-side evaluation is cheap to add. Where it is an observed outcome, the sending side's outcome does not transfer, so promotion should be automated only behind receiving-side evaluation. That check re-establishes the lift under the receiver's own measure, and it would catch a scaffold over-fitted to one deployment before it propagates to another. Even that check is necessary rather than sufficient: some of Evo2Team's transfers still fail on new graphs after target-side confirmation [@wang2026evo2team].

Where the signal is a judgment, a human promotion gate is a design feature, and governance means lineage and rollback around a human decision. With a delayed reward, property (a), the auto-gated local loop, cannot be met; what remains is lineage and rollback without an automatic gate. Safety-critical domains, the usual case for human gates, are judged or delayed domains with high stakes. Whatever the class, the measure bound of Section REF(sec:loop) holds: where tenants measure different things, as they usually do across organizations, no lift transfers without the receiving-side check.
