"""Generate the three paper figures specified in FIGURE_SPEC.md.

Greyscale, sans-serif, vector PDF at the spec canvas sizes; PNG previews at 200 dpi.
Run:  python make_figures.py   (from this directory)
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
    text (in points) does not; fonts stay >= 8 pt at IEEE column width."""
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


# ---------------------------------------------------------------- Figure 1
def fig1():
    W, H = 6.0, 3.2
    fig, ax = canvas(W, H)
    bw, bh = 0.68, 0.62
    y = 1.92
    xs = [0.48, 1.28, 2.08, 2.90, 3.78]   # five boxes
    dw = 0.70                              # diamond width/height
    # Loop 1 group box
    ax.add_patch(Rectangle((0.08, 0.42), 4.18, 2.38, lw=LW, ec="black", fc="none", ls=(0, (4, 3))))
    ax.text(0.12, 2.86, "Loop 1 (one deployment)", ha="left", va="bottom", fontsize=9)
    # Loop 2 group box
    l2x, l2w = 4.42, 1.50
    ax.add_patch(Rectangle((l2x, 0.85), l2w, 1.95, lw=LW, ec="black", fc="none", ls=(0, (4, 3))))
    ax.text(l2x + 0.04, 2.86, "Loop 2 (promotion)", ha="left", va="bottom", fontsize=9)

    box(ax, xs[0], y, bw, bh, "Failure\n(residual)")
    box(ax, xs[1], y, bw, bh, "Identify\nscaffold\ncoordinate")
    box(ax, xs[2], y, bw, bh, "Candidate\nedit")
    diamond(ax, xs[3], y, dw, dw + 0.16, "Gate: does\npatch loss\ndrop?", fs=7)
    box(ax, xs[4], y, bw, bh, "Persist in\nscaffold", fill=SHADE)
    # prune box below persist
    py = 1.06
    box(ax, xs[4], py, 0.60, 0.42, "Prune /\nroll back", fs=8)
    # Loop 2 boxes (arrow between them offset right so the label fits inside the group box)
    gx = l2x + l2w / 2
    gbw = 0.92
    oy = 1.12
    box(ax, gx, y, gbw, 0.50, "Promotion\ngate", fill=SHADE)
    box(ax, gx, oy, gbw, 0.50, "Other\ndeployments")

    # plain arrows 1->2->3->4
    arrow(ax, (xs[0] + bw / 2, y), (xs[1] - bw / 2, y))
    arrow(ax, (xs[1] + bw / 2, y), (xs[2] - bw / 2, y))
    arrow(ax, (xs[2] + bw / 2, y), (xs[3] - dw / 2, y))
    # accept 4->5 (label above the box tops, clear of both shapes)
    arrow(ax, (xs[3] + dw / 2, y), (xs[4] - bw / 2, y), "accept",
          lpos=((xs[3] + dw / 2 + xs[4] - bw / 2) / 2, y + 0.46))
    # reject 4->3 (return above)
    arrow(ax, (xs[3], y + (dw + 0.16) / 2), (xs[2] + 0.10, y + bh / 2), "reject",
          lpos=((xs[3] + xs[2]) / 2 + 0.02, y + 0.66), rad=0.45)
    # regress 5 -> prune (down), prune -> 5 (up), two parallel verticals
    arrow(ax, (xs[4] + 0.10, y - bh / 2), (xs[4] + 0.10, py + 0.21), "regress", fs=7.5,
          lpos=(xs[4] + 0.15, (y - bh / 2 + py + 0.21) / 2), ha="left", va="center")
    arrow(ax, (xs[4] - 0.10, py + 0.21), (xs[4] - 0.10, y - bh / 2))
    # next failure: leaves Persist's right edge, runs under the row back to box 1
    x0 = xs[4] + bw / 2 + 0.10
    polyline_arrow(ax, [(xs[4] + bw / 2, y - 0.22), (x0, y - 0.22), (x0, 0.62), (xs[0], 0.62), (xs[0], y - bh / 2)],
                   label="next failure", lpos=((x0 + xs[0]) / 2, 0.66))
    # 5 -> promotion gate
    arrow(ax, (xs[4] + bw / 2, y), (gx - gbw / 2, y))
    # promotion gate -> other deployments, labelled inside the Loop 2 box
    ax_x = gx + 0.30
    arrow(ax, (ax_x, y - 0.25), (ax_x, oy + 0.25))
    ax.text(ax_x - 0.07, (y - 0.25 + oy + 0.25) / 2, "bounded by\nevidence radius", ha="right", va="center",
            fontsize=7.5, style="italic")
    save(fig, "fig1_descent")


# ---------------------------------------------------------------- Figure 2
def fig2():
    W, H = 4.2, 3.4
    fig, ax = canvas(W, H)
    names = ["CORE", "TENANT", "STACK", "PROJECT", "USER"]
    x0, y0, x1, y1 = 0.15, 0.40, 3.95, 3.30
    dx, dy = 0.26, 0.36
    rects = []
    for i, n in enumerate(names):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, lw=LW, ec="black", fc="white"))
        ax.text(x0 + 0.06, y1 - 0.05, n, ha="left", va="top", fontsize=9, weight="bold")
        rects.append((x0, y0, x1, y1))
        x0 += dx; y0 += dy * 0.35; x1 -= dx; y1 -= dy
    ux0, uy0, ux1, uy1 = rects[-1]
    ucx, ucy = (ux0 + ux1) / 2, (uy0 + uy1) / 2 - 0.10
    ax.plot([ucx], [ucy], marker="o", ms=4, color="black")
    ax.text(ucx + 0.08, ucy, "Loop 1 (local)", ha="left", va="center", fontsize=8, style="italic")
    # outward arrow from USER up-right through every ring to just inside the CORE edge
    cx0, cy0, cx1, cy1 = rects[0]
    p0 = (ucx - 0.20, ucy + 0.14); p1 = (cx1 - 0.35, cy1 - 0.10)
    arrow(ax, p0, p1)
    # label to the right of the arrow's lower half, three short lines so it stays inside CORE
    ax.text(ucx + 0.55, ucy + 0.78, "Loop 2 promotion —\nbounded by\nevidence radius", ha="left", va="center",
            fontsize=7.5, style="italic", bbox=dict(fc="white", ec="none", pad=1.0))
    # bracket under the bottom edge spanning the two outer rings' right-hand bands (CORE + TENANT)
    xl, xr = rects[2][2], rects[0][2]   # STACK right edge .. CORE right edge
    by = rects[0][1] - 0.06
    ax.plot([xl, xl, xr, xr], [by + 0.05, by, by, by + 0.05], color="black", lw=LW)
    ax.text((xl + xr) / 2, by - 0.05, "cross-tenant", ha="center", va="top", fontsize=8, style="italic")
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
    f_hdr, f_main, f_sub, f_empty = (7.5, 7, 6.5, 6.5) if small else (9, 9, 8, 8)
    cells = {
        (0, 0): ("shade", "Research full-auto", "SkillOpt, AlphaEvolve"),
        (0, 1): ("shade", "Production hybrid", "SkillForge"),
        (0, 2): ("light", None, "no promotion"),
        (1, 0): ("light", None, "engineering logic"),
        (1, 1): ("light", None, "none surveyed"),
        (1, 2): ("blank", None, "—"),
        (2, 0): ("shade", "Governance-first", "prompts-as-code"),
        (2, 1): ("blank", None, "—"),
        (2, 2): ("blank", None, "—"),
    }
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
    counts: dict with keys total, core, contrast, strict_candidates, strict_pass, industry."""
    W, H = 3.5, 2.6
    fig, ax = canvas(W, H)
    bw, bh = 2.6, 0.40
    cx = W / 2
    ys = [2.30, 1.65, 1.00, 0.35]
    box(ax, cx, ys[0], bw, bh, f"{counts['total']} unique systems scored\n(six substrates, 0–5 rubric; {counts['may']} by May 2026, +{counts['oct']} in the Oct 2026 sweep)", fs=7.5)
    # split row
    box(ax, cx - 0.72, ys[1], 1.25, bh, f"core corpus: {counts['core']}\n(score ≥ 3 on some substrate)", fs=7.5, fill=SHADE)
    box(ax, cx + 0.72, ys[1], 1.25, bh, f"contrast: {counts['contrast']}\n(fails the discriminator)", fs=7.5, fill=LIGHT)
    box(ax, cx, ys[2], bw, bh, "composite two-loop audit\n(Loop 1 from session signal and gated Loop 2 with versioning or lineage)", fs=7.5)
    box(ax, cx - 0.72, ys[3], 1.25, bh, f"pass: {counts['strict_pass']} research\n+ {counts['industry']} industry exemplars", fs=7.5, fill=SHADE)
    box(ax, cx + 0.72, ys[3], 1.25, bh, f"promote without lineage: {counts['relaxed_only']}\n(enter only under relaxation)", fs=7.5, fill=LIGHT)
    arrow(ax, (cx - 0.3, ys[0] - bh / 2), (cx - 0.72, ys[1] + bh / 2))
    arrow(ax, (cx + 0.3, ys[0] - bh / 2), (cx + 0.72, ys[1] + bh / 2))
    arrow(ax, (cx - 0.72, ys[1] - bh / 2), (cx - 0.3, ys[2] + bh / 2))
    arrow(ax, (cx - 0.3, ys[2] - bh / 2), (cx - 0.72, ys[3] + bh / 2))
    arrow(ax, (cx + 0.3, ys[2] - bh / 2), (cx + 0.72, ys[3] + bh / 2))
    save(fig, "fig4_corpus_flow")


IEEE_SIZES = {  # physical sizes for the two-column IEEE Access layout (column 3.5 in, text 7.16 in)
    "fig1": (7.16, 7.16 * 3.2 / 6.0),
    "fig2": (3.5, 3.5 * 3.4 / 4.2),
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
