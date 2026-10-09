"""Generate the paper figures.

Greyscale, sans-serif, vector PDF at the spec canvas sizes; PNG previews at 200 dpi.
Run:  python make_figures.py            (arXiv sizes, from this directory)
      python make_figures.py --ieee --out <dir> --counts '{...}'   (IEEE Access sizes, suffix _ieee)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
SHADE = "#E6E6E6"
LIGHT = "#F2F2F2"
LW = 1.0


OUT = {"dir": HERE, "suffix": "", "size": None}   # overridden by --ieee (see main)


def canvas(w, h):
    """Axes in a (w x h)-inch coordinate frame. With OUT['size'] set, the figure is rendered
    at that physical size while keeping the same coordinate frame, so geometry scales and
    text (in points) does not; fonts stay >= 6.5 pt at IEEE column width."""
    fw, fh = OUT["size"] or (w, h)
    fig = plt.figure(figsize=(fw, fh))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def save(fig, stem):
    fig.savefig(os.path.join(OUT["dir"], stem + OUT["suffix"] + ".pdf"))
    fig.savefig(os.path.join(OUT["dir"], stem + OUT["suffix"] + ".png"), dpi=200)
    plt.close(fig)


def box(ax, cx, cy, w, h, text, fs=9, fill="white", ls="-", rounded=True, style="normal", weight="normal"):
    if rounded:
        p = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.06",
                           lw=LW, ec="black", fc=fill, ls=ls)
    else:
        p = Rectangle((cx - w / 2, cy - h / 2), w, h, lw=LW, ec="black", fc=fill, ls=ls)
    ax.add_patch(p)
    if text:
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, style=style, weight=weight, linespacing=1.15)
    return p


def diamond(ax, cx, cy, w, h, text, fs=8):
    pts = [(cx - w / 2, cy), (cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2)]
    ax.add_patch(Polygon(pts, closed=True, lw=LW, ec="black", fc="white"))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, linespacing=1.1)


def arrow(ax, p0, p1, label=None, lpos=None, fs=8, rad=0.0, ha="center", va="bottom", style="italic"):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, lw=LW, color="black",
                        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    if label:
        lx, ly = lpos if lpos else ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
        ax.text(lx, ly, label, ha=ha, va=va, fontsize=fs, style=style)


def polyline_arrow(ax, pts, label=None, lpos=None, fs=8, ha="center", va="bottom"):
    for i in range(len(pts) - 2):
        ax.plot([pts[i][0], pts[i + 1][0]], [pts[i][1], pts[i + 1][1]], color="black", lw=LW, solid_capstyle="round")
    arrow(ax, pts[-2], pts[-1])
    if label:
        ax.text(lpos[0], lpos[1], label, ha=ha, va=va, fontsize=fs, style="italic")


# ---------------------------------------------------------------- Figure 1: Loop 1 (the local fix)
def fig1():
    """Six stations left to right: log -> cluster -> trace+propose -> gate -> persist -> hand-off to Loop 2.
    One idea per box; the return path under the row says the deployment keeps running."""
    W, H = 7.2, 2.5
    fig, ax = canvas(W, H)
    y = 1.62
    bw, bh = 1.0, 0.76
    pitch = 1.17
    xs = [0.62 + i * pitch for i in range(6)]
    dw, dh = 1.0, 0.92
    # Loop 1 group box around the first five stations
    ax.add_patch(Rectangle((0.08, 0.30), xs[4] + bw / 2 + 0.10 - 0.08, 2.06, lw=LW, ec="black", fc="none", ls=(0, (4, 3))))
    ax.text(0.12, 2.39, "Loop 1: the local fix, inside one deployment", ha="left", va="bottom", fontsize=8.5)

    box(ax, xs[0], y, bw, bh, "Deployment runs;\nfailures are\nlogged", fs=7.5)
    box(ax, xs[1], y, bw, bh, "Cluster into\nrecurring modes,\nranked by frequency\nand severity", fs=7)
    box(ax, xs[2], y, bw, bh, "Trace one mode to\none scaffold\ncoordinate and\npropose one edit", fs=7)
    diamond(ax, xs[3], y, dw, dh, "Gate: does\nthe patch\nloss fall?", fs=7)
    box(ax, xs[4], y, bw, bh, "Edit persists,\nversioned (rolled\nback if it later\nregresses)", fs=7, fill=SHADE)
    box(ax, xs[5], y, bw, bh, "Loop 2:\nhow far may\nthe edit travel?\n(Fig. 2)", fs=7.5, fill=LIGHT, ls=(0, (4, 3)))

    arrow(ax, (xs[0] + bw / 2, y), (xs[1] - bw / 2, y))
    arrow(ax, (xs[1] + bw / 2, y), (xs[2] - bw / 2, y))
    arrow(ax, (xs[2] + bw / 2, y), (xs[3] - dw / 2, y))
    arrow(ax, (xs[3] + dw / 2, y), (xs[4] - bw / 2, y), "yes",
          lpos=((xs[3] + dw / 2 + xs[4] - bw / 2) / 2, y + 0.04), fs=7)
    arrow(ax, (xs[4] + bw / 2, y), (xs[5] - bw / 2, y))
    # reject: straight down from the diamond
    arrow(ax, (xs[3], y - dh / 2), (xs[3], 0.84), "no: discarded", lpos=(xs[3], 0.78), fs=7, va="top")
    # the deployment keeps running: from the persisted edit back to the log
    polyline_arrow(ax, [(xs[4], y - bh / 2), (xs[4], 0.50), (xs[0], 0.50), (xs[0], y - bh / 2)],
                   label="the deployment keeps running with the edited scaffold", lpos=((xs[0] + xs[3]) / 2 - 0.1, 0.54), fs=7.5)
    save(fig, "fig1_descent")


# ---------------------------------------------------------------- Figure 2: Loop 2 (the promotion ladder)
def fig2():
    """Five nested scopes drawn as a ladder. An edit rises one rung at a time; each rung has a gate;
    the dashed line is the evidence radius; the top rung crosses tenants."""
    W, H = 3.5, 3.4
    fig, ax = canvas(W, H)
    rungs = [("USER", "one person's account or fork"), ("PROJECT", "one repository or workspace"),
             ("STACK", "a team's bundle of projects"), ("TENANT", "one organization or customer"),
             ("CORE", "shared by every tenant")]
    x0, x1 = 1.2, 3.4
    bh, pitch, ybase = 0.40, 0.62, 0.50
    cx = (x0 + x1) / 2
    ys = [ybase + i * pitch for i in range(5)]
    for (name, desc), y in zip(rungs, ys):
        ax.add_patch(Rectangle((x0, y - bh / 2), x1 - x0, bh, lw=LW, ec="black", fc=SHADE if name == "CORE" else "white"))
        ax.text(cx, y + 0.07, name, ha="center", va="center", fontsize=8, weight="bold")
        ax.text(cx, y - 0.09, desc, ha="center", va="center", fontsize=6.8)
    ax_x = x0 + 0.28
    labels = ["gate: the wider loss must fall", "checked where the edit arrives", None, "cross-tenant: no surveyed system"]
    for i in range(4):
        ya, yb = ys[i] + bh / 2, ys[i + 1] - bh / 2
        arrow(ax, (ax_x, ya), (ax_x, yb))
        ym = (ya + yb) / 2
        if labels[i] is None:
            ax.plot([x0, x1], [ym, ym], color="black", lw=LW, ls=(0, (3, 2)))
            ax.text(ax_x + 0.14, ym, "evidence radius: the edit rises no further", ha="left", va="center",
                    fontsize=6.5, style="italic", bbox=dict(fc="white", ec="none", pad=0.8))
        else:
            ax.text(ax_x + 0.14, ym, labels[i], ha="left", va="center", fontsize=6.5, style="italic")
    # left-hand annotations
    ax.text(0.58, ys[0], "Loop 1\nedits here", ha="center", va="center", fontsize=7, style="italic")
    arrow(ax, (0.96, ys[0]), (x0, ys[0]))
    ym2 = (ys[1] + ys[3]) / 2
    ax.text(0.58, ym2, "Loop 2\npromotes\nupward,\none gate\nper rung", ha="center", va="center", fontsize=7, style="italic")
    arrow(ax, (0.96, ym2), (x0, ym2))
    ax.text(W / 2, 0.11, "rung loss = mean failure rate over the deployments it contains", ha="center", va="center", fontsize=6.5)
    save(fig, "fig2_scope")


# ---------------------------------------------------------------- Figure 3
def fig3():
    W, H = 4.8, 3.8
    fig, ax = canvas(W, H)
    cols = ["Loop 2: Auto", "Loop 2: Human", "Loop 2: None"]
    rows = ["Loop 1: Auto", "Loop 1: Human", "Loop 1: None"]
    small = OUT["suffix"] == "_ieee"          # column-width rendering: tighter grid, smaller type
    cw, ch = (1.05, 0.95) if small else (1.15, 0.95)
    gx0, gy0 = (1.45, 0.25) if small else (1.05, 0.25)
    f_hdr, f_main, f_sub, f_empty = (7.5, 7, 7.0, 6.5) if small else (9, 9, 8, 8)
    cells = {
        (0, 0): ("shade", "Research full-auto", "SkillOpt, AlphaEvolve"),
        (0, 1): ("shade", "Production hybrid", "Sierra, Devin"),
        (0, 2): ("light", None, "no promotion gate"),
        (1, 0): ("blank", None, "—"),
        (1, 1): ("blank", None, "—"),
        (1, 2): ("light", None, "curation"),
        (2, 0): ("shade", "Governance-first", "prompts-as-code"),
        (2, 1): ("light", None, "registries"),
        (2, 2): ("light", None, "ungated loop"),
    }
    if small:
        # IEEE Access article (October-2026 corpus, Section VII, strict "who decides" axes): Letta's
        # ungated push sits in [Auto x None]; registries have no failure-driven loop and sit in
        # [None x Human]; curation is the only human-gated cell; [Human x Auto] and [Human x Human] are empty.
        cells.update({
            (0, 2): ("light", None, "no promotion gate\n(Letta: ungated\npush, lineage)"),
            (1, 2): ("light", None, "curation:\nagent drafts,\nperson checks"),
            (2, 1): ("light", None, "MCP registries,\ncommunity hub"),
            (2, 2): ("light", None, "ungated loop:\nSkillRL, SkillForge"),
        })
    for r in range(3):
        for c in range(3):
            kind, main, sub = cells[(r, c)]
            x = gx0 + c * cw; y = gy0 + (2 - r) * ch
            fc = {"shade": SHADE, "light": LIGHT, "blank": "white"}[kind]
            ax.add_patch(Rectangle((x, y), cw, ch, lw=LW, ec="black", fc=fc))
            if main:
                if small:   # two-line titles so bold text stays inside a 0.77 in physical cell
                    main = {"Research full-auto": "Research\nfull-auto", "Production hybrid": "Production\nhybrid",
                            "Governance-first": "Governance-\nfirst"}.get(main, main)
                    ax.text(x + cw / 2, y + ch / 2 + 0.17, main, ha="center", va="center", fontsize=f_main, weight="bold", linespacing=1.0)
                    ax.text(x + cw / 2, y + ch / 2 - 0.22, sub.replace(", ", ",\n"), ha="center", va="center", fontsize=f_sub, linespacing=1.0)
                else:
                    ax.text(x + cw / 2, y + ch / 2 + 0.10, main, ha="center", va="center", fontsize=f_main, weight="bold")
                    ax.text(x + cw / 2, y + ch / 2 - 0.14, sub, ha="center", va="center", fontsize=f_sub)
            else:
                ax.text(x + cw / 2, y + ch / 2, sub, ha="center", va="center", fontsize=f_empty, style="italic", color="#333333")
    for c, name in enumerate(cols):
        ax.text(gx0 + c * cw + cw / 2, gy0 + 3 * ch + 0.10, name, ha="center", va="bottom", fontsize=f_hdr)
    for r, name in enumerate(rows):
        ax.text(gx0 - 0.08, gy0 + (2 - r) * ch + ch / 2, name, ha="right", va="center", fontsize=f_hdr)
    save(fig, "fig3_design_space")


# ---------------------------------------------------------------- Figure 4 (IEEE version)
def fig4(counts):
    """Corpus-flow diagram: candidate pool -> core / contrast -> strict audit -> passes.
    counts: dict with keys total, may, oct, core, contrast, strict_pass, industry, relaxed_only."""
    W, H = 3.5, 3.0
    fig, ax = canvas(W, H)
    # Column-width figure: full-width boxes 3.3 in, split boxes 1.62 in, three text lines each,
    # so every line stays inside its box at 7-7.5 pt (the earlier 2.6/1.25 in boxes overflowed).
    bw, bh, sw, dx = 3.3, 0.56, 1.62, 0.86
    cx = W / 2
    ys = [2.65, 1.87, 1.09, 0.31]
    box(ax, cx, ys[0], bw, bh, f"{counts['total']} unique systems scored\n(six substrates, 0–5 ruler)\n{counts['may']} in the first pass, +{counts['oct']} in the second", fs=7.5)
    # split row
    box(ax, cx - dx, ys[1], sw, bh, f"core corpus: {counts['core']}\n(score ≥ 3 on\nsome substrate)", fs=7, fill=SHADE)
    box(ax, cx + dx, ys[1], sw, bh, f"contrast: {counts['contrast']}\n(fails the\nfirst filter)", fs=7, fill=LIGHT)
    box(ax, cx, ys[2], bw, bh, "composite two-loop audit\n(Loop 1 from session signal;\nLoop 2 across contexts with versioning or lineage)", fs=7.5)
    box(ax, cx - dx, ys[3], sw, bh, f"pass: {counts['strict_pass']} research\n+ {counts['industry']} industry\nexemplars", fs=7, fill=SHADE)
    box(ax, cx + dx, ys[3], sw, bh, f"promote with no lineage: {counts['relaxed_only']}\n(fail the audit on\ngovernance alone)", fs=7, fill=LIGHT)
    arrow(ax, (cx - 0.3, ys[0] - bh / 2), (cx - dx, ys[1] + bh / 2))
    arrow(ax, (cx + 0.3, ys[0] - bh / 2), (cx + dx, ys[1] + bh / 2))
    arrow(ax, (cx - dx, ys[1] - bh / 2), (cx - 0.3, ys[2] + bh / 2))
    arrow(ax, (cx - 0.3, ys[2] - bh / 2), (cx - dx, ys[3] + bh / 2))
    arrow(ax, (cx + 0.3, ys[2] - bh / 2), (cx + dx, ys[3] + bh / 2))
    save(fig, "fig4_corpus_flow")


IEEE_SIZES = {  # physical sizes for the two-column IEEE Access layout (column 3.5 in, text 7.16 in)
    "fig1": (7.16, 7.16 * 2.5 / 7.2),
    "fig2": (3.5, 3.4),
    "fig3": (3.5, 3.5 * 3.8 / 4.8),
}

if __name__ == "__main__":
    import argparse, json
    ap = argparse.ArgumentParser()
    ap.add_argument("--ieee", action="store_true", help="render at IEEE sizes with suffix _ieee into --out")
    ap.add_argument("--out", default=HERE)
    ap.add_argument("--counts", default=None, help="JSON dict for fig4 (IEEE only)")
    a = ap.parse_args()
    OUT["dir"] = a.out
    if a.ieee:
        OUT["suffix"] = "_ieee"
        OUT["size"] = IEEE_SIZES["fig1"]; fig1()
        OUT["size"] = IEEE_SIZES["fig2"]; fig2()
        OUT["size"] = IEEE_SIZES["fig3"]; fig3()
        OUT["size"] = None
        if a.counts:
            fig4(json.loads(a.counts))
        print("wrote IEEE-size figures in", a.out)
    else:
        fig1(); fig2(); fig3()
        print("wrote fig1_descent, fig2_scope, fig3_design_space (.pdf + .png) in", a.out)
