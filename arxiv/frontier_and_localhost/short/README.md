# Frontier and Localhost — short version

Compressed version of *Frontier and Localhost: How Production AI Learns Outside the Weights* (Arbuzov, Shvets & Bei, 2026).

- **Long version** (26 pages): `../paper_frontier_and_localhost.pdf` — full v2 with reviewer-fix revisions.
- **Short version** (this directory, 21 pages total, ~6.5-page body): `paper_frontier_and_localhost_short.pdf` — body fitted under a 9-page budget; appendices unconstrained.

Both versions share the same survey audit trail in `supplementary/` (copied identically). Either bundle is independently submittable to arXiv.

## What is in the body vs. in the appendices

The short version compresses by relocation rather than deletion. The body carries the *persuasion path* — the story arc, the claims, the load-bearing tables, and the minimum machinery needed to make the descent picture readable. The appendices carry the *verification payload* — full formalism, per-system evidence, cluster walks, cell-by-cell matrix discussion.

| Body section | Story-arc role | Where the supporting machinery moved |
|---|---|---|
| §1 The gradient moved outside the model | Opening | (none — body-only) |
| §2 Why patch errors live outside the weights | Why the scaffold is where adaptation had to land | (none — body-only) |
| §3 Artifact-layer descent | What the scaffold is doing, mechanistically | **Appendix E** (mechanism stack, A1–A5, convergence proposition, correspondence table, worked cases) |
| §4 Six scaffold substrates | Coordinate decomposition | (substrate rubric table stays in body) |
| §5 Survey method | One-paragraph method summary | **Appendix B** (full inclusion/exclusion, tiers, scoring, sensitivity) |
| §6 Substrate maturity is uneven | One-paragraph unevenness claim | **Appendix F.1** (per-substrate distribution table) |
| §7 Four clusters | One-paragraph cluster naming | **Appendix F.2 + F.4** (cluster table, per-cluster walks with metrics, Tran & Kiela bound) |
| §8 The two-loop design space | Matrix + populated/empty summary | **Appendix F.5** (cell-by-cell discussion, DGM dual-mode note) |
| §9 The empty corner | Four properties + DP-FedAvg one-liner | **Appendix F.6 + F.7** (closest approaches, deployment-dependence) |
| §9.1 Patch-completeness as operational hypothesis | $(r, n, d)$-operationalisation | (body-only, already terse) |
| §10 A new failure surface | Single paragraph naming the seven failure modes | (body-only, already concentrated) |
| §11 Conclusion | Two paragraphs | (body-only) |

Appendix A (representative survey rows), Appendix C (gate-type → estimator-family mapping), and Appendix D (contrast set) carry over identically from the long version.

## Loss audit

Per the paper-compression skill's Step 7. The audit confirms that no important element of the long version vanishes silently in compression.

| Original element (long version) | Status | Location in short version |
|---|---|---|
| §1 thesis + decoder paragraph | preserved | §1 |
| §1 deferred-work pointer | preserved (compressed) | §1 closing sentence |
| §2 three constraints + Kirk/Padmakumar evidence | preserved | §2 |
| §2 scaffold-uniquely-satisfies bullet list | preserved as 1 sentence | §2 |
| §2 placement-question paragraph | preserved | §2 closing |
| §3 intro + estimators-of-same-quantity prose | preserved (compressed) | §3 opening |
| §3 patch scope hierarchy USER ⊂ PROJECT ⊂ STACK ⊂ TENANT ⊂ CORE | preserved verbatim | §3 |
| §3 *Assumptions and scope* box (v2 reviewer fix) | preserved verbatim | §3 |
| §3 Loop 1 / Loop 2 + Auto/Human/None definition | preserved | §3 |
| §3 five-related-work paragraph (CoALA, Du, Gao, ACE) | dropped (low signal in body; partially in F) | — |
| §3.1 six-operation mechanism stack | preserved verbatim | Appendix E.1 |
| §3.2 formal setup (θ_M, Θ_s, L_D) | preserved (one equation in body, full in E.2) | §3 + E.2 |
| §3.2 update rule + gate inequality | preserved with motivation sentences | §3 |
| §3.2 correspondence table | preserved verbatim | Appendix E.5 |
| §3.2 credit-assignment-without-chain-rule paragraph | preserved verbatim | Appendix E.6 |
| §3.2 four worked cases (RAG / pitch / tool / memory) | preserved verbatim | Appendix E.7 |
| §3.2 Assumption A1 + A2 + descent inequality | preserved verbatim | Appendix E.3 |
| §3.2 Proposition with A3/A4/A5 | preserved verbatim | Appendix E.4 |
| §3.2 Loop 1 / Loop 2 mathematical interpretation | preserved | §3 (compressed) + Appendix E.8 (full) |
| §3.2 overfitting paragraph + non-stationary-patch note | preserved verbatim | Appendix E.9 |
| §3.2 five-mechanism-conditions summary | preserved (compressed) | §3 closing |
| §4 substrate rubric table | preserved verbatim | §4 |
| §4 why-six-substrates caveat (v2 fix) | preserved | §4 |
| §5 method paragraph | preserved (compressed) | §5 |
| §5 inclusion criteria | preserved verbatim | Appendix B |
| §5 exclusion criteria | preserved verbatim | Appendix B |
| §5 evidence-tier definitions T1–T5 | preserved verbatim | Appendix B |
| §5 scoring discipline | preserved verbatim | Appendix B |
| §5 composite-two-loop criterion | preserved (compressed) | §5 |
| §5 industry-exemplar disclosure | preserved | §5 |
| §5 sensitivity analysis (v2 fix) | preserved verbatim | Appendix B |
| §5 survey-window + 2026-dating flag | preserved | Appendix B |
| §5 audit-trail pointer | preserved | §5 + Appendix B |
| §6.1 substrate maturity table | preserved verbatim | Appendix F.1 |
| §6.1 unevenness commentary | preserved (compressed) | §6 |
| §6.2 cluster table with sierra footnote | preserved verbatim | Appendix F.2 |
| §6.3 five surprising absences | preserved verbatim | Appendix F.3 |
| §7 four cluster prose walks | preserved verbatim | Appendix F.4 |
| §7 AlphaTensor / Winograd Strassen caveat (v2 fix) | preserved verbatim | Appendix F.4 |
| §7 CASCADE within-benchmark framing (v2 fix) | preserved verbatim | Appendix F.4 |
| §7 Tran & Kiela orchestration bound (v2 fix) | preserved verbatim | Appendix F.4 |
| §7 vertical-bundle paragraph | preserved verbatim | Appendix F.4 |
| §8 matrix table | preserved verbatim | §8 |
| §8 count statement + populated/empty cells | preserved | §8 |
| §8 cell-by-cell commentary | preserved verbatim | Appendix F.5 |
| §8 cross-cutting findings (n=1; AlphaEvolve depth) | preserved (compressed) | §8 |
| §8 DGM dual-mode footnote | preserved verbatim | Appendix F.5 |
| §9 four properties (a)–(d) | preserved verbatim | §9 |
| §9 no-system-has-all-four statement | preserved | §9 |
| §9 closest-approaches enumeration | preserved verbatim | Appendix F.6 |
| §9 DP-FedAvg empty-corner statement | preserved verbatim | §9 + Appendix F.7 |
| §9 deployment-dependent paragraph | preserved verbatim | Appendix F.7 |
| §9.1 $(r, n, d)$-patch-completeness operationalisation (v2 fix) | preserved verbatim | §9.1 |
| §10 failure surface (v2 IFScale framing fix) | preserved verbatim | §10 |
| §11 conclusion | preserved (compressed) | §11 |
| Appendix A (30 representative rows) | preserved verbatim | Appendix A |
| Appendix B (data appendix) | preserved + extended with §5 detail | Appendix B |
| Appendix C (gate-type → estimator-family) | preserved verbatim | Appendix C |
| Appendix D (contrast set ≈38 systems) | preserved verbatim | Appendix D |

### What was deleted (with note)

| Element | Reason for deletion |
|---|---|
| §3 five-related-work paragraph (CoALA, Du, Gao, Fang, ACE) | The related-work positioning is low signal for the body and reappears implicitly through Appendix D contrast-set classifications. Kept the substantive CoALA / self-evolution-survey distinction implicit in §3's framing rather than as an enumerated paragraph. |
| §1 closing "architectural review … deferred to follow-on practitioner work" sentence | Compressed into §1's closing sentence pointing at the practitioner companion paper; the long-form forward-pointer was redundant with the abstract's deferred-companion note. |

No other element was deleted. Every paragraph in the v2 long version is either in the short body or in an appendix above.

### Page budget audit

- **Target body**: 9 pages.
- **Actual body** (§1–§11, including abstract): ~6.5 pages — §10 ends on page 6; §11 sits at the top of page 7; Appendix A starts on page 7.
- **Result**: under budget. Density caps from the paper-compression skill (≤1 equation per paragraph; ≤2–3 important numbers per paragraph; one formal result per subsection) were respected; padding the body to reach exactly 9 pages would violate those caps. If a reviewer or venue requires a longer body, candidates for re-promotion from appendix to body are: F.1 substrate maturity distribution table; F.2 cluster table; one of E.3 (descent inequality) or E.4 (convergence proposition).
- **Appendix span**: pages 7–18 (Appendix A starts on 7; Appendix B on 9; References starts on 19).
- **References span**: pages 19–21.

## What this version preserves from v2

Every reviewer-fix from the long-version v2 revision is present in the short version:

- Kirk 2024 / Padmakumar & He 2023 evidence for the breadth-optimisation claim (§2).
- Patch scope hierarchy USER ⊂ PROJECT ⊂ STACK ⊂ TENANT ⊂ CORE (§3).
- *Assumptions and scope* box at the top of §3 (the v2 fix that lets reviewers understand when the descent picture is mechanism vs. metaphor).
- Hedged "federated-style artifact aggregation, not arithmetic averaging" Loop-2 framing (§3, §9).
- Hedged "dominant practical substrate" language (§2; replaces "only reasonable substrate").
- DGM collapsed to a single matrix entry with dual-mode footnote (Appendix F.5).
- Reconciled counts (~130 systems, 13 strict + 2 industry, nine failed in the composite audit).
- AlphaTensor / Winograd caveat on the Strassen claim (Appendix F.4).
- CASCADE "within-benchmark" framing (Appendix F.4).
- IFScale framing correction — 68% is best-model-at-N=500, 35× is latency on one reasoning model (§10).
- $(r, n, d)$-operationalised patch-completeness (§9.1, replacing v1's AGI rhetoric).
- Sensitivity analysis under two relaxations (Appendix B).
- OpenCore removed from every body and appendix location; audit trail in `supplementary/` retains the historical record with a `supplementary/README.md` explaining the omission.

## Building locally

```
bash build.sh
```

Produces `paper_frontier_and_localhost_short.{tex,pdf,zip}`. The zip is the arXiv source bundle (tex + `supplementary/` tree).
