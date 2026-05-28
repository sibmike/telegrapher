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
| §3.5 SkillOpt: a recent worked instance of artifact-layer descent | Case study grounding the §3 formalism in a concrete recent system | **Appendix G** (full correspondence with Algorithm-1 pointers; per-baseline differentiation; §9 property audit; cost-and-bloat note) |
| §4 Six scaffold substrates | Coordinate decomposition | (substrate rubric table stays in body) |
| §5 Survey method | One-paragraph method summary | **Appendix B** (full inclusion/exclusion, tiers, scoring, sensitivity) |
| §6 Substrate maturity is uneven | One-paragraph unevenness claim | **Appendix F.1** (per-substrate distribution table) |
| §7 Four clusters | One-paragraph cluster naming | **Appendix F.2 + F.4** (cluster table, per-cluster walks with metrics, Tran & Kiela bound) |
| §8 The two-loop design space | Matrix + populated/empty summary | **Appendix F.5** (cell-by-cell discussion, DGM dual-mode note) |
| §9 The missing architecture: governed cross-tenant scaffold optimization | Four properties + DP-FedAvg-as-analogy one-liner | **Appendix F.6 + F.7** (closest approaches, deployment-dependence) |
| §10 A new failure surface | Single paragraph naming the seven failure modes | (body-only, already concentrated) |
| §11 Conclusion | Two paragraphs | (body-only) |

Appendix A (representative survey rows), Appendix C (gate-type → estimator-family mapping), and Appendix D (contrast set) carry over identically from the long version. Appendix G is new in v3 and supplies the SkillOpt walkthrough that grounds §3.5.

## Loss audit

Per the paper-compression skill's Step 7. The audit confirms that no important element of the long version vanishes silently in compression.

| Original element (long version) | Status | Location in short version |
|---|---|---|
| §1 thesis + decoder paragraph | preserved | §1 |
| §1 deferred-work pointer | preserved (compressed) | §1 closing sentence |
| §2 three constraints + Kirk/Padmakumar evidence | preserved | §2 |
| §2 scaffold-uniquely-satisfies bullet list | preserved as 1 sentence | §2 |
| §2 placement-question paragraph | preserved | §2 closing |
| §2 three-stage taxonomy table (Patchwork / Random artifact search / Artifact-layer descent) | new in framing revision | §2 closer (mirrors long-version §2.5) |
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
| §9.1 $(r, n, d)$-patch-completeness operationalisation (v2 fix) | cut in editorial pass — distracted from the optimizer thesis; pointer sentence in §9 | (removed) |
| §10 failure surface (v2 IFScale framing fix) | preserved verbatim | §10 |
| §11 conclusion | preserved (compressed) | §11 |
| Appendix A (30 representative rows) | preserved verbatim | Appendix A |
| Appendix B (data appendix) | preserved + extended with §5 detail | Appendix B |
| Appendix C (gate-type → estimator-family) | preserved verbatim | Appendix C |
| Appendix D (contrast set ≈38 systems) | preserved verbatim, with v3 SkillOpt pointers appended to DSPy and TextGrad rows | Appendix D |
| §3.5 SkillOpt case study (v3 addition) | new in v3 — concrete worked instance of the §3 descent picture | §3.5 |
| Appendix G SkillOpt walkthrough (v3 addition) | new in v3 — full correspondence + per-baseline differentiation + §9 audit + cost note | Appendix G |
| §3.5 convergent landscape (v3.1 addition) | new in v3.1 — convergence framing paragraph + 5-row landscape table + 4-claim synthesis | §3.5 |
| Appendix G restructure (v3.1 addition) | new in v3.1 — G.1 landscape overview; G.4–G.9 per-cluster walks (GEPA+Tiwari / RCL / Harness / Multi-objective+lifecycle / Cross-task transfer / Synthesis) | Appendix G |
| §2 Tiwari et al. theoretical anchor (v3.1) | new in v3.1 — independent two-timescale motivation alongside Kirk/Padmakumar | §2 |
| §9 closest-approaches CORAL/PACE/Meta-Harness (v3.1) | new in v3.1 — extends the partition with three new closest approaches | §9 + Appendix F.2 |
| §10 Ratchet + Ong et al. failure-surface findings (v3.1) | new in v3.1 — hygiene as Stage-1 precondition; informed Loop-1 vs. Stage-2 trial-and-error | §10 |

### What was deleted (with note)

| Element | Reason for deletion |
|---|---|
| §3 five-related-work paragraph (CoALA, Du, Gao, Fang, ACE) | The related-work positioning is low signal for the body and reappears implicitly through Appendix D contrast-set classifications. Kept the substantive CoALA / self-evolution-survey distinction implicit in §3's framing rather than as an enumerated paragraph. |
| §1 closing "architectural review … deferred to follow-on practitioner work" sentence | Compressed into §1's closing sentence pointing at the practitioner companion paper; the long-form forward-pointer was redundant with the abstract's deferred-companion note. |

No other element was deleted. Every paragraph in the v2 long version is either in the short body or in an appendix above.

### Page budget audit

- **Target body**: 9 pages (soft).
- **Actual body** (§1–§11, including abstract): ~12 pages after the v3.1 convergent-landscape addition (was ~11 in v3.0, ~6.5 in v2). The body now exceeds the soft 9-page target by 3 pages; the excess sits in §3.5 (convergent landscape table + synthesis paragraph) and small ripple edits in §2/§9/§10.
- **Result**: over the soft 9-page target. The expansion is intentional: the convergence is the strongest evidence for the §9 missing-architecture claim, and burying it in the appendix would understate the contribution. If a venue requires a strict 9-page body, candidates for re-relegation to appendix are the §3.5 convergent-landscape table (which is fully duplicated in G.1) and the §3.5 synthesis paragraph (which is fully duplicated in G.9).
- **Appendix span**: extended by ~5 pages for the restructured Appendix G (G.1–G.9 new; G.10–G.11 lifted from v3.0).
- **References span**: extended by 14 entries (the convergent-cluster citations) plus SkillOpt from v3.0.

## What is new in v3.1 (convergent landscape)

A short literature scan after the v3.0 SkillOpt case study found that SkillOpt is one of at least fourteen independent research threads in 2025–2026 that converge on artifact-layer descent from different substrate angles. v3.1 expands §3.5 from a single-system case study into a convergent-landscape map, with the full per-cluster walks landing in a restructured Appendix G.

- **§2** — Tiwari et al. (2026) added as independent two-timescale (in-context / in-weights) motivation alongside the Kirk/Padmakumar evidence.
- **§3.5** — re-titled "SkillOpt and the convergence on artifact-layer descent." The SkillOpt walkthrough is unchanged; a new convergence-framing paragraph names the 14-system cluster, a compact landscape table indexes the four complementary clusters and what each leaves open in §3 terms, and a synthesis paragraph names the four well-supported claims (scaffold-vs-weights decomposition; credit assignment as central bottleneck; hygiene as precondition; cross-org Loop 2 unfilled).
- **§9** — closest-approaches paragraph extended with CORAL (async multi-agent Loop 2 within one system), PACE (two-timescale architecture under small-frozen-model constraints), and Meta-Harness (Loop 1 over the orchestration substrate).
- **§10** — scaffold-bloat paragraph extended with Ratchet's hygiene-as-precondition finding ($+0.0$ pp without hygiene vs. $+16.2$ pp with four hygiene mechanisms); eval-fragility paragraph extended with Ong et al.'s direct-evaluation finding that current harness optimisers cannot be distinguished from Stage-2 trial-and-error by downstream score alone.
- **Appendix F.2** — closest-approaches enumeration mirrored with CORAL/PACE/Meta-Harness bullets.
- **Appendix G** — fully restructured into eleven subsections: G.1 convergent landscape overview + indexed table; G.2 SkillOpt full correspondence (lifted from v3.0); G.3 SkillOpt per-baseline differentiation (lifted); G.4 GEPA + Tiwari + reflective-evolution family (new); G.5 Reflective Context Learning (Vassilyev et al., new); G.6 harness-optimisation cluster — Meta-Harness, AHE, MOSS, CANTANTE, Ong et al. (new); G.7 multi-objective + lifecycle — MOCHA, Ratchet (new); G.8 cross-task transfer + evidence radius — ICT, Combee, CORAL, PACE (new); G.9 synthesis with four claims (new); G.10 SkillOpt §9 audit (lifted); G.11 cost and bloat (lifted, with hygiene cross-link).
- **Appendix A** — 7 new representative rows: GEPA, Meta-Harness, MOSS, RCL, PACE, CORAL, Ratchet.
- **`references.bib`** — 14 new BibTeX entries; new % O, % Q, % V section markers added.
- **Body References section** — 14 new entries in alphabetical position.
- **The long version** is still not updated; the v3.0 + v3.1 long-version port remains the next work item.

## What is new in v3 (SkillOpt-only — historical)

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
- (cut in editorial pass) $(r, n, d)$-operationalised patch-completeness was preserved through v2 but removed from the short body in the editorial pass to keep the focus on the optimizer thesis; a one-sentence pointer remains in §9.
- Sensitivity analysis under two relaxations (Appendix B).
- OpenCore removed from every body and appendix location; audit trail in `supplementary/` retains the historical record with a `supplementary/README.md` explaining the omission.

## Building locally

```
bash build.sh
```

Produces `paper_frontier_and_localhost_short.{tex,pdf,zip}`. The zip is the arXiv source bundle (tex + `supplementary/` tree).
