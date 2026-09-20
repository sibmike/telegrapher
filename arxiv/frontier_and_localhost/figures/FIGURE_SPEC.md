# Figure generation spec — self-contained

This file fully specifies three diagrams for an academic paper. **A generator
needs no other context.** Use the label text **verbatim** (do not paraphrase,
expand abbreviations, or "improve" wording). Each figure is a simple
box-and-arrow / grid diagram — no icons, no gradients, no 3-D, no colour.

Output one file per figure:
- `fig1_descent.pdf`
- `fig2_scope.pdf`
- `fig3_design_space.pdf`

The **caption** text listed under each figure is NOT drawn inside the image — it
is added later by the document. Only draw the "in-image text."

---

## Global constraints (read first)

**Layout target.** The paper is single-column with a text width of about
**5.5 inches (14 cm)**. Design every figure to be legible at that printed width.

**Size.** Use the exact canvas size given per figure (inches). Do not rely on the
document scaling the image — author at final size so fonts stay crisp.

**Fonts.** Sans-serif (e.g., Helvetica/Arial). Minimum text size **8 pt** at the
canvas size; prefer 9–10 pt for primary node labels and ~8 pt for secondary/edge
labels. If any label would fall below 8 pt to fit, enlarge the box instead.

**Palette (greyscale only).**
- Box outline: black, ~1 pt stroke.
- Default box fill: white.
- "Shaded / highlighted" fill: light grey (~15% black, e.g. `#E6E6E6`).
- "Empty / inactive" fill: very light grey (~7%, e.g. `#F2F2F2`) or white with a dashed outline.
- Text: black. Arrows: black, ~1 pt, solid; arrowheads small and filled.

**Format.** Vector **PDF** preferred (crisp at any scale). If raster, PNG at
**≥300 dpi** at the canvas size. No transparency issues — white background.

**General style.** Plenty of white space; straight or gently-elbowed arrows
(orthogonal routing is fine); rounded-rectangle boxes are acceptable. Keep it
clean and textbook-plain.

---

## Figure 1 — `fig1_descent.pdf`

### What this figure illustrates (the concept, not just the boxes)

The paper's thesis: modern AI systems increasingly improve *outside the model
weights*, by editing a persistent **scaffold** — the prompts, rules, memories,
skills, tools, and orchestration wrapped around a frozen model (the paper calls
this artifact $\theta_s$). Most teams maintain that scaffold as ad-hoc
**patchwork**: something fails, someone bolts on a fix, the pile grows, and
nobody tracks what helped or when to prune. The paper argues there is a
disciplined alternative that behaves like **stochastic gradient descent — but
over a text artifact instead of weights**. Figure 1 *is* that disciplined loop;
it is the paper's central mechanism, and every later section asks which real
systems have closed which parts of it. Read the diagram as **one optimisation
step, repeated forever**:

- **Failure (residual)** = the learning signal. The slice of a deployment's error
  the current scaffold did not handle — the analogue of a loss signal in training.
- **Identify scaffold coordinate** = *credit assignment*. Locate which part of the
  scaffold caused the failure (a stale memory, an under-specified instruction, a
  missing tool argument, a brittle retrieval rule, a misrouted agent edge).
  "Coordinate" because the scaffold has six independently-editable parts; the
  failure points at one. This is the hardest, most-often-missing step.
- **Candidate edit** = the proposed change to that coordinate — the analogue of a
  gradient step (a new rule, a rewritten skill, a corrected memory entry).
- **Gate: does patch loss drop?** = *validation*. "Patch loss" is a measurable
  error rate on the bounded slice of work this deployment actually does (its
  "patch"). The gate is an imperfect estimator (an eval score, an LLM-judge, a
  test suite) asking whether the edit truly lowers that loss. This gate is what
  separates disciplined descent from guessing.
- **accept / reject** = keep the edit if it helps; otherwise propose another. A
  rejection is information, not waste.
- **Persist in scaffold** = *the parameter update*. The accepted edit becomes a
  durable, inspectable part of $\theta_s$ — this is the actual learning.
- **regress → prune / roll back** = descent is not monotone. An edit that looked
  good can later degrade, so the loop must be able to revert it. Without this the
  scaffold bloats and rots; reversibility is a first-class operation.
- **next failure (return arrow)** = the loop never "finishes." Closing the loop is
  what makes this *descent* rather than a one-off fix.

That cycle is **Loop 1**: it works on a *single* deployment's scaffold and drives
down *that* deployment's loss.

**Loop 2** (Promotion gate → Other deployments, *bounded by evidence radius*) is
the decision to **share** a validated edit — from one repo to a team template,
from one tenant's playbook to a cross-tenant library. The constraint that matters
is **evidence radius**: an edit may travel only as far as the evidence that it
generalises. In one line: *Loop 1 descends one loss; Loop 2 changes which loss is
being optimised.* The paper's headline gap is that almost no real system runs
Loop 2 under an automated, governed gate.

**What the reader should take away:** the scaffold is not a junk drawer of fixes —
it is a parameter being optimised, with a governor (evidence radius) on how far
each update is allowed to generalise.

### Drawing spec

**Canvas:** 6.0 in wide × 3.2 in tall. Landscape flow, read left→right with one
return loop.

**Two groups side by side, BOTH drawn in greyscale.** The diagram is one big
dashed box on the left (`Loop 1`) and a smaller dashed box on the right
(`Loop 2`). Persist lives *inside* Loop 1; only the promotion step crosses into
Loop 2.

**Group A — label `Loop 1 (one deployment)` (one dashed box).** Inside it, five
boxes left→right forming a cycle, with `Persist in scaffold` as the LAST box
*inside this box*:
1. `Failure (residual)`
2. `Identify scaffold coordinate`
3. `Candidate edit`
4. `Gate: does patch loss drop?`  (diamond/decision shape if easy, else a box)
5. `Persist in scaffold`

Plus one small box, `Prune / roll back`, just **below** box 5 (still inside the
Loop 1 box).

**Group B — label `Loop 2 (promotion)` (a second, smaller dashed box, also greyscale).** Two boxes:
- `Promotion gate`
- `Other deployments`

**Arrows (the quoted word is the arrow's label):**
- 1 → 2 → 3 → 4 (plain).
- 4 → 5 labelled `accept`.
- 4 → 3 labelled `reject` (short return up to box 3).
- 5 → `Prune / roll back` labelled `regress`, and `Prune / roll back` → 5 (a short
  arrow back up to Persist — a rolled-back edit restores the scaffold). Prune /
  roll back has NO other outgoing arrow.
- 5 → 1: a single long arrow running under the row, labelled `next failure`,
  closing the Loop-1 cycle. It must originate at box 5 (`Persist in scaffold`) —
  NOT at `Prune / roll back`.
- 5 → `Promotion gate` (this is the only arrow that leaves Group A and enters
  Group B) → `Other deployments`; label the `Promotion gate → Other deployments`
  arrow `bounded by evidence radius`.

**Each group label appears once**, above its box (do not repeat it below).

**Avoid (a first render got these wrong):**
- **No icons or clipart** in any box — text only.
- **Greyscale only** — do not colour Loop 2 (no pink/blue/red fills); use the
  light-grey fills from the global palette.
- **`Persist in scaffold` goes INSIDE the Loop 1 box**, not floating between the
  two groups.
- **`next failure` starts at Persist**, and `Prune / roll back` loops back to
  Persist — the rollback box must not sit on the `next failure` return line.
- Each loop label appears **once** (not duplicated top and bottom).

**Caption (added later, not drawn):** *Artifact-layer descent. Loop 1 turns a
failure into a gated, persisted edit on one deployment's scaffold; Loop 2
promotes a validated edit to other deployments, only as far as its evidence
radius supports.*

---

## Figure 2 — `fig2_scope.pdf`

**Canvas:** 4.2 in wide × 3.4 in tall. Concentric nested rectangles.

**In-image text — five nested rectangles, OUTERMOST to innermost (each fully
contains the next):**
1. `CORE` (outermost)
2. `TENANT`
3. `STACK`
4. `PROJECT`
5. `USER` (innermost, smallest)

Place each label at the **top edge inside** its own rectangle so all five are
visible (do not center, or inner labels collide). Nest them like Russian dolls.

**Two annotations:**
- A small arrow or dot at the innermost `USER`/`PROJECT` region labelled
  `Loop 1 (local)`.
- An outward-pointing arrow starting near `USER` and pointing out through the
  rings toward `CORE`, labelled `Loop 2 promotion — bounded by evidence radius`.
- A brace or bracket spanning the two outer rings (`TENANT`, `CORE`) labelled
  `cross-tenant`.

**Caption (added later, not drawn):** *Patch scope hierarchy. Each level's loss
averages the patches it contains. Loop 1 descends a USER/PROJECT loss; Loop 2
promotes upward; "cross-tenant promotion" means reaching TENANT or CORE.*

---

## Figure 3 — `fig3_design_space.pdf`

**Canvas:** 4.8 in wide × 3.8 in tall. A 3×3 grid of square cells with row and
column headers outside the grid.

**Column headers (top, left→right):** `Loop 2: Auto` , `Loop 2: Human` , `Loop 2: None`
**Row headers (left, top→bottom):** `Loop 1: Auto` , `Loop 1: Human` , `Loop 1: None`

**Cell contents (row, column) — fill exactly these nine cells:**
- (Loop1 Auto, Loop2 Auto): SHADED. Text: `Research full-auto` / smaller line: `SkillOpt, AlphaEvolve`
- (Loop1 Auto, Loop2 Human): SHADED. Text: `Production hybrid` / smaller: `SkillForge`
- (Loop1 Auto, Loop2 None): empty fill. Small text: `no promotion`
- (Loop1 Human, Loop2 Auto): empty fill. Small text: `engineering logic`
- (Loop1 Human, Loop2 Human): empty fill. Small text: `none surveyed`
- (Loop1 Human, Loop2 None): very-light/blank. Small text: `—`
- (Loop1 None, Loop2 Auto): SHADED. Text: `Governance-first` / smaller: `prompts-as-code`
- (Loop1 None, Loop2 Human): very-light/blank. Small text: `—`
- (Loop1 None, Loop2 None): very-light/blank. Small text: `—`

So exactly **three shaded cells** (the populated ones) and the rest light/blank.
Shaded = light grey fill; the three "reasoned-empty" cells (`no promotion`,
`engineering logic`, `none surveyed`) get the very-light fill with their reason in
~8 pt italic; the three `—` cells stay blank/white.

**Caption (added later, not drawn):** *The two-loop design space. Three cells are
populated; the rest are empty for structural reasons. No populated system adds
governed cross-tenant promotion — the missing architecture discussed in the text.*

---

## Embed widths (for the document author — not the generator)
- Fig 1: full text width (`width=\linewidth`).
- Fig 2: ~0.6 of text width, centred.
- Fig 3: ~0.8 of text width, centred.
