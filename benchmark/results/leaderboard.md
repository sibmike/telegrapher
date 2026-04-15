# CKPB Leaderboard

Accuracy on the CKPB dual suite, by compressor and evaluation model. Compression ratio is the mean across items.

## key_facts

| Compressor | Eval model | N | Accuracy | Compression |
|---|---|---:|---:|---:|
| `llmlingua2_33` | `gpt-4.1` | 4080 | 92.2% | 66.6% |
| `llmlingua2_33` | `gpt-4o-mini` | 4080 | 90.6% | 66.6% |
| `llmlingua2_50` | `gpt-4.1` | 4080 | 94.9% | 49.4% |
| `llmlingua2_50` | `gpt-4o-mini` | 4080 | 94.6% | 49.4% |
| `telegraph_english` | `gpt-4.1` | 4080 | 99.1% | 41.5% |
| `telegraph_english` | `gpt-4o-mini` | 4080 | 95.7% | 41.5% |

## fine_facts

| Compressor | Eval model | N | Accuracy | Compression |
|---|---|---:|---:|---:|
| `llmlingua2_33` | `gpt-4o` | 801 | 89.0% | 66.7% |
| `llmlingua2_33` | `gpt-4o-mini` | 801 | 72.8% | 66.7% |
| `llmlingua2_50` | `gpt-4o` | 801 | 93.3% | 49.7% |
| `telegraph_english` | `gpt-4o` | 801 | 96.5% | 42.2% |

---

**Notes.** Compression ratio is `compressed_tokens / original_tokens` (tiktoken `cl100k_base`). Lower is more compressed. `telegraph_english` uses adaptive compression; the reported mean varies by suite.