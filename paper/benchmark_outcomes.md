# Telegraph English — Benchmark Outcomes

## 1. Benchmark Setup

### Dataset

- **Source:** LongBench-v2 — 503 records, filtered to 339 QA-suitable documents
- **Chunking:** Max 1,000 words per chunk with overlap
- **Compression:** Each chunk compressed via the Telegraph Translator prompt (v5) using OpenAI API (GPT-4.1 / o4-mini)
- **Output format:** JSONL with original text, compressed text, token counts, compression ratio, and document/chunk IDs

### Compression Statistics

| Metric | Value |
|--------|-------|
| Average compression | ~50% token reduction |
| Compression range | 16–87% |
| Compression approach | Document-adaptive (varies by information density) |
| Token counting | tiktoken-based |

### QA Evaluation Methodology

1. **QA generation:** GPT-4.1 generates a single QA pair from the original (uncompressed) text
2. **Answer variants:** Creates a "modified answer" (reworded but identical meaning)
3. **Distractors:** Generates 3 plausible but incorrect answer choices
4. **Testing:** Multiple-choice (4 options) answered by the evaluation model on both original and compressed text
5. **Scoring:** Accuracy = fraction of correct MC answers

---

## 2. Test Suites

| Suite | QA Pairs | Focus |
|-------|----------|-------|
| **key_facts** | 4,081 | Core concepts, headline facts, main claims |
| **fine_facts** | 801 | Buried details, specific numbers, edge-case qualifications |

---

## 3. Models Tested

- **GPT-4.1** — flagship; used for QA generation and as evaluation model
- **GPT-4o** — previous flagship
- **GPT-4o-mini** — cost-optimized small model
- **GPT-4.1-nano** — smallest/cheapest model
- **Fine-tuned GPT-4o** — domain-tuned variant (928 rows in benchmark)

---

## 4. Accuracy Results

### 4.1 Key Facts (4,081 QA pairs)

| Model | Original | Telegraph English | LLMLingua2-50 | TE Drop (pp) | LLML2-50 Drop (pp) |
|-------|----------|-------------------|---------------|--------------|---------------------|
| **GPT-4.1** | 1.000 | **0.991** | 0.990 | −0.9 | −1.0 |
| **GPT-4o-mini** | 0.991 | **0.957** | 0.946 | −3.4 | −4.5 |
| **GPT-4.1-nano** | 0.980 | **0.950** | 0.949 | −3.0 | −3.1 |

**Takeaway:** On headline facts, TE matches or slightly outperforms LLMLingua2-50 across all models. Both methods lose minimal accuracy on large models (< 1pp on GPT-4.1), but the gap widens on smaller models.

### 4.2 Fine Facts (801 QA pairs)

| Model | Original | Telegraph English | LLMLingua2-50 | TE Drop (pp) | LLML2-50 Drop (pp) |
|-------|----------|-------------------|---------------|--------------|---------------------|
| **GPT-4o** | 0.996 | **0.965** | 0.933 | −3.1 | −6.3 |
| **GPT-4o-mini** | 0.938 | **0.843** | 0.820 | −9.5 | −11.8 |

**Takeaway:** Fine details suffer 3–4× more compression loss than key concepts. TE holds a clear advantage — particularly on 4o-mini where it preserves an extra 2.3pp over LLMLingua2-50. Against the more aggressive LLMLingua2-33, the TE advantage grows to ~11pp.

### 4.3 Accuracy Hierarchy (Best to Worst)

1. **Original (uncompressed)** — baseline
2. **Telegraph English (~50%)** — 1–3pp drop on key_facts, 3–11pp on fine_facts
3. **LLMLingua2-50 (50% deletion)** — moderate compression, consistently worse than TE
4. **LLMLingua2-33 (67% deletion)** — aggressive compression, significant accuracy loss (up to 21pp on fine_facts)

---

## 5. Head-to-Head: TE vs LLMLingua2

### 5.1 Methodological Comparison

| Aspect | Telegraph English | LLMLingua2 |
|--------|-------------------|------------|
| **Method** | Rewrites text into atomic fact lines with adaptive ratio | Token deletion via XLM-RoBERTa-large classifier at fixed ratio |
| **Adaptivity** | Adjusts compression to information density | Same ratio regardless of content density |
| **Semantic integrity** | Preserves complete meaning units | Can sever logical links between remaining tokens |
| **Domain generalization** | Rule-based; works across all domains | Trained on MeetingBank; effectiveness decreases on other distributions |
| **Auditability** | Human-readable after ~40 symbols | Microsoft notes outputs "may be difficult for humans to understand" |
| **Pipeline scope** | Full workflow (compress → embed → store → retrieve) | Input-only preprocessing |

### 5.2 Where TE Wins Most

| Scenario | TE Advantage |
|----------|-------------|
| **Smaller models (4o-mini, nano)** | Larger accuracy gap; structured format helps weaker models |
| **Detail-heavy tasks (fine_facts)** | Up to 11pp advantage over LLML2-33 |
| **Multi-agent pipelines** | Compresses at every step, not just input |
| **Dense technical content** | Adaptive ratio preserves more in information-dense passages |

### 5.3 Why TE Outperforms

Four factors, argued briefly here and in more detail in the main paper's §6.1.

The most fundamental is that TE operates on claims, not tokens. Compression ratios follow information density — dense passages resist reduction, verbose ones collapse — which a fixed-ratio token-deletion method cannot match by construction. The second is explicit relational structure: `∴`, `VS`, and `→` survive compression and preserve the logical spine of the source, where deleting a connective forces the downstream model to guess. The third is co-reference stability; one-claim-per-line with upper-case entities largely removes pronouns from the output, so there is nothing to strand when compression removes their antecedents. The last is task alignment — the grammar was designed to keep extractable facts, not to minimise entropy, and factual QA is what these benchmarks measure.

The caveat attached to all four: this evidence is for QA over technical corpora. Whether the same mechanisms dominate under summarisation, translation, or non-technical genres is an open question.

---

## 6. Token Cost Analysis

### Single-Prompt Scenario (2,000 input tokens)

At $10/M-token pricing:
- **Savings:** ~$13 per 1,000 API calls

### Multi-Agent Pipeline (2,000 input + 5 agent steps × 400 tokens each)

| Method | Total Tokens | Cost per 1K calls | Savings |
|--------|-------------|-------------------|---------|
| **Original** | 4,000 | $40 | — |
| **LLMLingua2** | ~3,300 | $33 | $7 (input-only compression) |
| **Telegraph English** | ~1,600 | $16 | $24 (compresses at every step) |

**Key insight:** LLMLingua2 only compresses the initial prompt; TE serves as a native protocol across all pipeline stages, compounding savings.

---

## 7. Error Profile

- **Total errors on key_facts (GPT-4.1):** 187 cases where the model answered correctly on original text but failed on TE
- **Error pattern:** Fine details (dates, units, conditional qualifications) are the primary failure mode
- **Fine_facts sensitivity:** 3–4× higher compression loss than key concepts across all methods
- **Detailed error data:** Available in `benchmark_error_report.txt` (~2 MB)

---

## 8. Data Files Reference

| File | Contents |
|------|----------|
| `benchmark_41.csv` | GPT-4.1 benchmark results (4,081 rows) |
| `benchmark_4omini.csv` | GPT-4o-mini benchmark results |
| `benchmark_fine_4o.csv` | Fine-tuned GPT-4o results (928 rows) |
| `llml2_33.csv`, `llml2_50.csv` | LLMLingua2 baselines at 33% and 50% |
| `llml2_30_41.csv` | LLMLingua2-30 with GPT-4.1 |
| `compression_stats.csv` | Compression ratio statistics |
| `benchmark_error_report.txt` | Detailed error analysis |
| `benchmarks/` directory | 28 subdirectories with per-model/batch results (~56K files) |

---

## 9. Key Findings Summary

Across every compression level we tested, TE outperforms LLMLingua-2 — and the gap is not uniform. On large models the two methods are nearly indistinguishable; GPT-4.1 loses under a percentage point on key facts regardless of which compressor produced the input. The interesting cases sit below the flagship tier.

Smaller models benefit most from TE. Where GPT-4.1-nano or GPT-4o-mini has to reconstruct relationships from token-deleted fragments, it often fails; where the same model reads TE's explicit symbols, it doesn't have to guess. Structured compression, it seems, compensates for limited inferential capacity — which is precisely the capacity constraint that makes cost-sensitive deployments choose smaller models in the first place.

Fine details are where the methods actually separate. Key facts carry enough redundancy that almost any compressor preserves them; buried numerical qualifiers, boundary conditions, and near-miss distractors do not have that safety margin. On the fine-facts suite against LLML2-33, TE holds an 11-percentage-point lead — the kind of gap that matters for legal, medical, and financial applications where a qualifier is the answer.

Two secondary findings are worth flagging. First, because TE persists as a native format across a pipeline rather than compressing only the input, the cost savings compound across multi-agent workflows in a way that input-only compressors cannot match. Second, the compression ratio is adaptive by design — ranging from 16% on sparse verbose text to 87% on dense technical passages — so the aggregate mean ("~50%") hides genuinely different behaviours on different document types.

---

## 10. Research Roadmap

### Immediate Priorities

1. **Error analysis on fine_facts failures** — classify missing token types (dates, units, conditionals)
2. **Adaptive compression threshold** — dynamic detail preservation based on confidence scores
3. **Benchmark expansion** — compare against additional compression baselines

### Strategic Directions

- Develop "detail-aware" TE variants for high-precision domains (legal, biomedical)
- Explore selective expansion for agent memory applications
- Integrate confidence-based compression knobs (`CONF=` tags) for adaptive quality/cost trade-offs
- Multilingual test sets (in development)
- TE-to-TE summarization for iterative compression
