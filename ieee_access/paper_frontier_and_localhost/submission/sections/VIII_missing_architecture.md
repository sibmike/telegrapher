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

The extent of automation should depend on the feedback. Exact checks provide the most direct setting for testing a transferred skill, although the recipient still needs relevant test cases. Observed outcomes require evaluation on the recipient's workload because the sender's outcome is not portable evidence of success. Where quality is judged, a human promotion gate is a design feature, supported by lineage and rollback. Delayed outcomes cannot support the per-edit automatic local gate in property (a); those systems still benefit from provenance and reversibility around proposals and milestones.

Thus the four properties define a target for the settings that can support an automatic local gate. They should not be interpreted as a requirement to automate every decision in every domain. The common requirement is that the evidence attached to an edit remain meaningful where it is used, and that the system preserve the ability to inspect and reverse its adoption.
