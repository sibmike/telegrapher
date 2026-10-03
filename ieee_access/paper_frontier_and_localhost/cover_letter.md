# Cover letter — IEEE Access

**Manuscript:** Frontier and Localhost: A Survey of How Production AI Learns Outside the Weights
**Article type:** Survey
**Corresponding author:** Mikhail L. Arbuzov (mike.arbuzov54@gmail.com)

Dear Editor,

We submit a survey article on how production systems built on large language models adapt outside the model weights: in instruction files, skills, memories, tool registries, orchestration graphs, evaluation suites, and governance pipelines. The engineering community now maintains this layer in every serious deployment, but it maintains it as patchwork. Our survey of 256 production and research systems (January 2023 to October 2026) reads the layer as one adaptation surface, states the loop that would turn patchwork into optimization and the five conditions under which that loop is a mechanism, and classifies every system by which loops it closes and whether each gate is algorithmic or human.

The contribution a reader can act on is threefold. First, a classification of the feedback signal available to a deployment, from an exact test to a delayed and sparse reward, that tells an engineer in advance which automation is reachable and which failure will dominate. Second, a scored and released corpus (score table in the Supplementary Material) with a published rubric, so every classification can be re-derived. Third, a four-property audit criterion for the architecture no surveyed system instantiates, governed cross-tenant scaffold optimization with lineage, access control, and rollback, together with the failure surface that the gap leaves open.

The article is a survey and reports no new experiments; it is accompanied by an audit of every absolute claim against the October-2026 literature. An earlier version of the survey was circulated as a preprint and submitted to a non-archival workshop; this article extends it with the feedback-signal classification (Section IV), a rescored corpus with a later cutoff, and a restructured argument. {{TODO: confirm preprint status and link for the editor.}} The manuscript is not under consideration elsewhere. All authors have approved the submission. An AI assistant was used for literature search, citation checking, and editing, as disclosed in the Acknowledgment.

Suggested reviewers: {{TODO(authors)}}.

Sincerely,
Mikhail L. Arbuzov, on behalf of the authors
