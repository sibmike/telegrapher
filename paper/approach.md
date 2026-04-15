# Telegraph English — Approach Description

## 1. What Is Telegraph English?

Start with the transformation. Given the original sentence

> *"According to research by Johnson and colleagues (2023), the application of machine learning techniques to medical diagnostics resulted in a 27.5% increase in early detection rates while simultaneously reducing false positives by approximately 12% compared to traditional methods."*

Telegraph English compresses to:

```
ML→MEDICAL-DIAGNOSTICS: EARLY-DETECTION+27.5% ∧ FALSE-POSITIVE-12% [JOHNSON:2023]
```

Sixty-eight tokens collapse to fourteen, and each surviving unit — the causal direction, the two quantitative claims, the citation — sits on a separate, addressable line. That is what TE *does*: rewrite natural language into a symbol-rich dialect whose compression is a byproduct of structural rewriting, not statistical token deletion.

TE is a grammar, expressed as a 430-line prompt that an LLM uses as its system message during the rewrite. The grammar's line-structure rule — every line is one atomic fact — is what links compression to the properties we describe below. Compression ratios adapt to information density; dense technical paragraphs compress modestly, verbose framing compresses aggressively. Across LongBench-v2, the mean ratio is ~50%, and accuracy loss on key-fact QA stays under one percentage point on GPT-4.1.

---

## 2. A Full-Pipeline Format, Not an Input Preprocessor

Token-deletion compressors work on the prompt and stop there. Generated output passes through the next pipeline stage uncompressed, so multi-step systems cannot compound the savings. TE is different in kind: because the output is itself valid TE — a rewrite, not a subset — every downstream stage consumes the same format.

The practical consequence is that each pipeline stage benefits from compression exactly once, paid upfront, and every retrieval, every generation, every onward message carries the smaller payload. The LLM call that performs the rewrite is the only expensive step; ranking, filtering, updating, and reassembly are string operations on atomic lines.

A typical deployment looks like this:

- **Compress** source documents into TE; store the output as JSONL.
- **Embed** the TE lines directly — each line is already a semantic chunk, so no separate chunking stage is required.
- **Store** the embeddings and TE text in a vector database. Storage footprint drops roughly in proportion to the compression ratio.
- **Retrieve** by embedding the query and pulling the nearest lines. Because lines are individually addressable, retrieval returns atomic facts, not arbitrary text windows.
- **Expand on demand** when full-fidelity source is needed. Each TE line carries an ID that maps back to the original chunk for lossless recovery.

The defining property is not any single step; it is that no step needs to re-compress or re-chunk. The expensive rewrite happens once per document. Everything downstream is cheap.

---

## 3. Core Grammar Rules (v5 — Final)

The full specification lives in [`../code/prompts/compression_v5.txt`](../code/prompts/compression_v5.txt). Key principles:

### 3.1 Foundations

- **Atomic line** — one claim, step, event, or question per line (newline or `;` separation)
- **Semantic compression** — drop text only if it is fully inferable from what remains; *fidelity outranks brevity*
- **Upper-case default** — write in UPPER-CASE unless case itself carries information (proper names, code, math variables, SI unit symbols)
- **Target** — ~5× token reduction when feasible, but correctness, auditability, and reversibility always take priority

### 3.2 Symbol System

TE uses a precise, non-interchangeable set of relationship operators:

| Symbol | Meaning | Example |
|:------:|---------|---------|
| `=` | Definition or equality only | `VELOCITY=DISTANCE/TIME` |
| `→` | Causation / flow | `HEAT→EXPANSION` |
| `↛` | Negated causation | `LACK-VITAMIN D ↛ STRONG-BONES` |
| `⇒` | Logical implication | `RAIN⇒WETNESS` |
| `⇔` | Bidirectional equivalence | `P⇔Q` |
| `∴` | Therefore / conclusion | `X>Y ∧ Y>Z ∴ X>Z` |
| `∵` | Because / reason | `MOTOR-FAILURE ∵ OVERLOAD` |
| `↑` / `↓` | Increase / decrease | `TEMPERATURE↑`, `PRESSURE↓` |
| `∧` / `∨` / `¬` | AND / OR / NOT | `A∧B`, `A∨B`, `¬EVIDENCE` |
| `≈` / `≠` | Approximately / not equal | `COST≈USD10M`, `HYPOTHESIS≠THEORY` |
| `VS` | Contrast (never causal) | `MODEL-A VS MODEL-B` |

### 3.3 Temporal & Modal Tags

```
DATE:YYYY-MM-DD               (exact, ISO only)
PAST:    NOW:    FUTURE:      (state)
REPEAT:                       (recurring)
Relative → YESTERDAY:, TOMORROW:, LAST-HOUR:, IN-15-MIN:
Modality → POSSIBLE:, NECESSARY:, LIKELY:, UNLIKELY:
Numeric confidence → CONF=0.87
```

### 3.4 Question & Answer

`Q:` introduces a question; `A:` introduces its answer.

```
Q: WHO DISCOVERED PENICILLIN?
A: ALEXANDER FLEMING [FLEMING:1929]
```

### 3.5 Role & Scope Tags

```
AGENT:, PATIENT:, INSTRUMENT:, LOCATION:
DEF:   — one-line definitions
CTX:   — shared context; omit subject until context shifts
```

Nested scope uses exactly two spaces of indentation (never tabs).

### 3.6 Hyphen Grouping

- **When:** 2–4-word established concept (< 25 characters)
- **How:** `ERROR-TRACEABILITY`, `LONG-CONTEXT`
- **Avoid:** ad-hoc groups > 25 chars
- **Consistency:** once hyphenated, reuse the exact form throughout

### 3.7 Numbers, Units & Financial Formats

```
Percent:        +12%, ↓3%
Percent-points: +2.5PT
Currency:       USD10.5 M (code-first; M/K/B for magnitudes)
Y/Y, Q/Q, H/H: Y/Y-4.2%   Q/Q+1.8%
Temperature:    37°C (no space before unit)
Ranges:         5–10 (en-dash)
Scientific:     2.5×10⁻⁷
Measurements:   5 kg, 12 km, 2.3 GHz (proper SI case)
```

### 3.8 Citations & Identifiers

- Inline: `[AUTH:YEAR]` or `[A1:Y1; A2:Y2]`
- Legal: `[CASE:CITE]`
- Identifiers: `ARXIV:`, `DOI:`, `ISBN:`, `PMID:`
- URLs: `URL:https://example.com/file.pdf`
- Files: `FILE:data.csv`

### 3.9 Structured Blocks

- **CODE** — inline ≤ 80 chars or fenced
- **TABLE** — compress ≤ 4×4, else fenced
- **MATH** — inline `$…$` ≤ 40 chars, else fenced LaTeX
- Headings use `H1:`, `H2:` to preserve hierarchy

---

## 4. Compression Levels

| Level | Target Ratio | Use Case |
|-------|-------------|----------|
| `L1` (light) | ~2× | High-fidelity, minimal loss |
| `L3` (default) | ~5× | Balanced compression/accuracy |
| `L5` (max) | ≥10× | Maximum compression, acceptable detail loss |

---

## 5. Information Distillation Process

TE compression follows a six-pass sequence:

1. **Concept identification** — extract key entities and topics
2. **Claim extraction** — isolate individual factual claims
3. **Relation mapping** — identify causal, logical, and temporal links
4. **Redundancy kill** — remove duplicated or inferable information
5. **Verify claims & numbers** — cross-check all quantitative data
6. **Cross-check citations** — ensure all references are preserved

### Token Elimination Priority

Eliminate in order: articles → prepositions → connectors → auxiliaries → descriptors. Use symbol characters (`≈`, `↑`, `∧`) to replace multi-word phrases. Merge related concepts with `/` (`SIGNAL/NOISE`).

---

## 6. Quality Gate (12-Point Checklist)

Every TE output must pass all of these before finalization:

- [ ] Formatting consistency (headings, spacing, indentation)
- [ ] Symbol usage precise; no interchangeable use
- [ ] No more than 3 consecutive symbols (except inside `URL:`)
- [ ] Numbers & units follow SI conventions
- [ ] Abbreviations defined at first use as `FULL-TERM(ABBR)`; glossary if > 6
- [ ] Quotes/dialogue attributed with proper tags
- [ ] Domain metadata complete (authors, judges, dates, etc.)
- [ ] Line length ≤ 80 chars; split with `;` if needed
- [ ] Logical chains > 2 symbols wrapped in `( … )`
- [ ] Information preserved — no hallucination, no omission
- [ ] Citations & identifiers correctly formatted
- [ ] Capital consistency — TE tokens UPPER-CASE except case-sensitive items

---

## 7. How TE Differs from LLMLingua2

| Aspect | Telegraph English | LLMLingua2 |
|--------|-------------------|------------|
| **Mechanism** | Semantic rewrite into atomic fact lines | Binary token-deletion classifier (XLM-RoBERTa-large) |
| **Compression ratio** | Document-adaptive (~50% avg) | Fixed ratio (e.g., rate=0.33 or 0.50) |
| **Content adaptivity** | Adjusts to information density | Same ratio regardless of content |
| **Semantic integrity** | Preserves complete meaning units | Can sever logical links between tokens |
| **Domain generalization** | Rule-based; works across all domains | Limited by training distribution (MeetingBank) |
| **Pipeline position** | Full-workflow format (compress → embed → store → retrieve) | Input-only preprocessor |
| **Multi-agent systems** | Native protocol; no recompression needed | Requires recompression at each step |
| **Auditability** | Human-readable after learning ~40 symbols | Microsoft acknowledges "may be difficult for humans to understand" |
| **Reversibility** | Every TE line expands to one unambiguous sentence | No structured reverse mapping |

---

## 8. Compression Examples

**Original:** *"According to research by Johnson and colleagues (2023), the application of machine learning techniques to medical diagnostics resulted in a 27.5% increase in early detection rates while simultaneously reducing false positives by approximately 12% compared to traditional methods."*

**Telegraph English:**
```
MACHINE-LEARNING→MEDICAL-DIAGNOSTICS: EARLY-DETECTION+27.5% ∧ FALSE-POSITIVE-12% [JOHNSON:2023]
```

**Original:** *"Earnings per share (EPS) were $3.42 for the fourth quarter, exceeding analyst expectations of $3.25..."*

**Telegraph English:**
```
EPS=USD3.42 Q4 VS EXPECTED=USD3.25 ROE=21.8% FISCAL-YEAR
```

---

## 9. Use Cases

| Domain | Application |
|--------|-------------|
| **RAG platforms** | 2–3× more context with fewer hallucinations |
| **Vector databases** | 65% lower storage and write costs |
| **API cost control** | Reduce spending across GPT, Claude, Gemini endpoints |
| **Long-context chat** | Richer conversation history without model upgrades |
| **Legal** | Fine-detail preservation for case law and contracts |
| **Biomedical** | Nuanced qualifications in literature review |
| **Financial** | Numerical precision for earnings, ratios, forecasts |
| **Edge deployment** | Cost optimization with smaller models (4o-mini, nano) |

---

## 10. Licensing

| Component | License |
|-----------|---------|
| Core specifications | CC-BY-SA 4.0 |
| Reference implementation | MIT |
| Datasets | CC0 (Public Domain) |
| Cloud API (future) | At-cost pricing through non-profit effort |

---

## 11. Research Roadmap

- **Key token preservation theory** — formal analysis of which tokens matter most
- **Domain-specific dialects** — specialized TE variants for law, medicine, finance
- **Embedding geometry impact** — how compression affects vector space structure
- **TE as preprocessing for smaller models** — enabling edge deployment
- **Multilingual test sets** — extending beyond English (in development)
- **Adaptive compression threshold** — dynamic detail preservation based on confidence scores
- **TE-to-TE summarization** — iterative compression for extreme reduction
