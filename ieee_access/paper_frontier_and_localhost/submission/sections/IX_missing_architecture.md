## The missing architecture: governed cross-tenant scaffold optimization {#sec:gap}

What is missing is specific. Four properties define an architecture that no surveyed system instantiates:

- (a) **auto-gated Loop 1**: the commit criterion is an algorithmic threshold;
- (b) **cross-organization promotion**: Loop 2 routes artifacts between organizations (we use *cross-tenant* and *cross-organizational* interchangeably);
- (c) **versioned lineage with access control**: promoted artifacts carry versions, audit trails, and role-based access policies;
- (d) **rollback**: a bad promotion can be reverted without redeploy.

The closest approaches split these properties among them, and no row of Table REF(tab:IX-1) is full on promotion across organizations.

| System | (a) auto-gated Loop 1 | (b) cross-organization promotion | (c) versioned lineage with access control | (d) rollback |
|----------------|----------|------------------------|----------------------|------------------|
| FederatedSkill [@yang2026federatedskill] | full | partial: privacy-preserving aggregation of skill patches across heterogeneous clients that sit under one operator | partial: auditable per-modification decision log | none |
| EvolveNet [@nie2026evolvenet] | full | partial: held-out merge gate at the aggregator, but clients are benchmark partitions, not organizations | none: no lineage, no access control | full: rollback to the previous shared harness after a failed round |
| SkillForge [@skillforge2026] | full | partial: cross-team within one enterprise | partial | not documented |
| Governance-first registries [@kang2026registry; @qin2026governed; @quessadavial2026acm] | none: no inner loop | none | partial: lineage without access control | full, with evidence |
| MCP control planes [@agenticcommunity2026mcpgateway] | none: no inner loop | none | partial: access control without evaluation-gated promotion | not reported |

Table IX-1. The closest approaches to governed cross-organization scaffold optimization, scored against the four properties.

Row by row, the partition is plain: the systems with a local loop carry the automatic gate and part of the promotion, the registries carry lineage and rollback without an inner loop, and the control planes carry access control alone. Rollback appears inside one federated round and inside single deployments, as edit-level reversal [@wei2026skillsmith; @gao2026skillaudit] and as an admission test that rejects edits which cannot be undone [@sah2026evoundo]. No system rolls back a promotion that has crossed an organization boundary, because none makes such a promotion (Supplementary Material S4).

In machine-learning terms, what is missing is a cross-tenant aggregator with an automated evaluation gate at the scaffold layer. It would carry five parts: per-tenant artifact pools, each tagged with provenance; an aggregation step across tenants that respects tenant isolation; a held-out evaluation at the receiving tenant that blocks a promotion whenever it does not lower that tenant's patch loss; versioned lineage with access control; and a rollback envelope on every promoted artifact. The federated-learning analogy [@mcmahan2017fedavg; @mcmahan2018dpfedavg; @kairouz2021federated] is useful only in the limit where artifacts are mergeable update representations; federated prompt tuning, in which participants learn a shared prompt rather than shared weights [@guo2022promptfl], is the weight-side precedent closest to that limit. In surveyed practice Loop 2 is selection and merge, and the nearest systems aggregate program edits with a language model, not by averaging.

Whether the architecture *should* be built depends on the feedback-signal class, not on the application domain (Section REF(sec:signal)). Where the signal is exact, automatically gated cross-tenant promotion of a test-validated skill would be low-risk, and receiving-side evaluation is cheap to add. Where it is an observable outcome, the sending side's outcome does not transfer, so promotion should be automated only behind receiving-side evaluation, the check that would catch a scaffold over-fitted to one deployment before it propagates to another. Even that check is necessary rather than sufficient: some of Evo2Team's transfers still fail on new graphs after target-side confirmation [@wang2026evo2team]. Where it is judged, a human gate on Loop 2 is a design feature, and governance means lineage and rollback around a human decision. Where it is delayed, property (a) cannot be met, and what remains is lineage and rollback without an automatic gate. Safety-critical domains, the usual case for human gates, are judged or delayed domains with high stakes. Naming the four properties turns a vague gap into an audit criterion that any future system can be measured against; naming the signal class says which of the four a given deployment should expect to meet.
