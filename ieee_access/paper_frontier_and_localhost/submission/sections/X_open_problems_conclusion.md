## Open problems and conclusion {#sec:open}

The remaining problems become more specific when expressed in terms of the decisions a deployment must make.

**Attributing a failure to an editable cause.** An exact check can establish that an output failed without identifying the instruction, memory, skill, or tool binding responsible. No surveyed method solves this across all substrates. Slot attribution [@nguyen2026harnessevo], intervention-based attribution [@chu2026agentgrad], and contrastive multi-agent attribution [@zehle2026cantante] provide narrower starting points. Observed outcomes make the problem harder because their causes are more confounded.

**Establishing improvement at the recipient.** A transferred artifact must be evaluated against the receiving deployment's tasks and measure. Existing receiving-side checks show that this is feasible in selected settings, while Evo2Team's failures on unseen graphs show its coverage limits. Federated Agent Optimization proposes a receiving-client gate but does not implement it [@yang2026fao]. Connecting such checks to provenance, access control, and reversal remains an architectural problem.

**Maintaining calibration while the criterion changes.** For judged tasks, the open question is how to keep a judge aligned with people while revising the rubric it applies. No surveyed scaffold system reports this measurement. The neighboring reward literature also lacks a reported human-agreement result for a co-evolving rubric or judge, with RLPR's probability-based reward a distinct case. A useful solution must evaluate the moving criterion as well as the outputs it scores.

**Evaluating improvement with delayed outcomes.** When many edits occur before a meaningful result arrives, per-edit acceptance is unavailable. Proxy milestones and proposal pruning may still be useful, but downstream gains alone do not establish successful attribution. Harness optimizers should therefore be assessed against their claims about why particular edits help, as well as their final scores [@ong2026harnesseval].

**Connecting local learning to governed sharing.** No surveyed system combines automatic local acceptance, promotion across organizations, versioned lineage with access control, and rollback. The components exist in different systems. Their integration must preserve tenant isolation, evaluate the recipient, and account for artifacts derived from a change that is later withdrawn. Where feedback cannot support automatic acceptance, the design must retain the corresponding human decision or delayed evaluation.

The survey's central observation is that persistent changes outside the weights have become an important form of adaptation, while the evidence supporting those changes remains fragmented. Many systems can test a local candidate. Fewer can reliably explain which recurring failure it addresses, and the machinery for transferring the resulting improvement to another organization has not been assembled in the public systems examined here.

The frontier model generalizes. The local scaffold specializes. Reliability comes from governing that specialization: knowing what each change improved, where that evidence applies, and how the change can be reversed. That discipline must extend to the evaluations themselves when they become part of the adapting system.
