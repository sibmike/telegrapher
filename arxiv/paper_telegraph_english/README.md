# Telegraph English

> *Semantic Prompt Compression via Structured Symbolic Rewriting*
>
> Mikhail L. Arbuzov, Alexey A. Shvets, Sisong Bei

## The argument

Telegraph English (TE) is a compression protocol that rewrites natural-language text into a symbol-rich, formally-structured format. Where token-deletion methods like LLMLingua-2 train a classifier to remove low-information tokens at a fixed ratio, TE performs a full semantic rewrite: decomposing text into atomic fact lines, substituting verbose phrases with about forty logical and relational symbols, and letting the compression ratio adapt to each document's information density.

A consequence of this design (one not initially set out to achieve) is that compression and semantic chunking collapse into a single operation. Each output line is an independently addressable fact, so the compressed representation is simultaneously a semantic index. Individual lines can be retained at full fidelity, reduced to headings, updated with new information, or pruned when they become redundant. The expensive LLM rewrite happens once; everything after is string manipulation.

On 4,081 question-answer pairs from LongBench-v2, evaluated across five OpenAI models and two difficulty levels, TE preserves 99.1% accuracy on key facts with GPT-4.1 at roughly 50% token reduction, and outperforms LLMLingua-2 at matched compression ratios on every model and task tested. The gap widens on smaller models, up to eleven percentage points on fine-detail tasks, which suggests that explicit relational structure compensates for limited model capacity.

The full project, with grammar specification, compression prompt, benchmark data, and reference implementation, lives in the [main repository](../../README.md).

## Read the paper

- **PDF**: [`paper_telegraph_english.pdf`](paper_telegraph_english.pdf)
- **Source (Markdown)**: [`paper_telegraph_english.md`](paper_telegraph_english.md)
- **LaTeX source**: [`paper_telegraph_english.tex`](paper_telegraph_english.tex)

To rebuild the PDF locally: `bash build.sh`.

## Citation

```bibtex
@misc{arbuzov2025telegraph,
  title  = {Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting},
  author = {Arbuzov, Mikhail L. and Shvets, Alexey A. and Bei, Sisong},
  year   = {2025},
  url    = {https://github.com/sibmike/telegrapher}
}
```

## License

Paper text and grammar specification: **CC-BY-SA-4.0**. Reference implementation in [`../../code/`](../../code/) is **MIT**.
