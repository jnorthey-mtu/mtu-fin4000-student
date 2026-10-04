#!/usr/bin/env python3
"""Redraw the figures used by the mini guides (PNG, saved in study-guides/mini/img/)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "study-guides" / "mini" / "img"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})


def bond(y, c=0.06, n=10, f=1000):
    t = np.arange(1, n + 1)
    cf = np.full(n, c * f); cf[-1] += f
    return float((cf / (1 + y) ** t).sum())


def stats(y=0.06, c=0.06, n=10, f=1000):
    t = np.arange(1, n + 1)
    cf = np.full(n, c * f); cf[-1] += f
    pv = cf / (1 + y) ** t
    p = pv.sum()
    D = (t * pv).sum() / p
    conv = (pv * (t ** 2 + t)).sum() / (p * (1 + y) ** 2)
    return p, D, D / (1 + y), conv


def fig_price_yield():
    p0, D, Dm, C = stats()
    ys = np.linspace(0.02, 0.10, 200)
    actual = np.array([bond(y) for y in ys])
    dy = ys - 0.06
    dur = p0 * (1 - Dm * dy)
    durc = p0 * (1 - Dm * dy + 0.5 * C * dy ** 2)
    fig, ax = plt.subplots(figsize=(6.4, 3.8), dpi=200)
    ax.plot(ys * 100, actual, color="#1f4e79", lw=2.2, label="Actual price")
    ax.plot(ys * 100, dur, color="#c0504d", lw=1.6, ls="--", label=f"Duration only (D* = {Dm:.2f})")
    ax.plot(ys * 100, durc, color="#4f8f3a", lw=1.6, ls=":", label=f"Duration + convexity (C = {C:.2f})")
    ax.scatter([6], [p0], color="black", zorder=5)
    ax.annotate("Priced at par:\n6% YTM, $1,000", (6, p0), (6.5, 1180), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_xlabel("Yield to maturity (%)"); ax.set_ylabel("Bond price ($)")
    ax.set_ylim(700, 1500); ax.grid(alpha=0.25); ax.legend(loc="upper right", fontsize=8, frameon=False)
    ax.set_title("10-year, 6% annual-coupon bond: price vs. yield", fontsize=10)
    fig.tight_layout(); fig.savefig(OUT / "mini-07-price-yield-curve.png"); plt.close(fig)
    return p0, D, Dm, C


def fig_sector_rotation():
    x = np.linspace(-np.pi, np.pi, 400)
    y = -np.cos(x)  # peak at both ends, trough in the middle
    fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=200)
    ax.plot(x, y, color="#1f4e79", lw=2.4)
    ax.axhline(0, color="gray", lw=0.6, ls=":")
    boxes = [
        (-np.pi, 1.75, "PEAK", "Natural resources", "#fde9d9"),
        (-1.55, 1.2, "CONTRACTION", "Defensives: food,\npharma, utilities", "#e6e6e6"),
        (0.0, -1.85, "TROUGH", "Financials, then capital goods", "#e2f0d9"),
        (1.55, 1.2, "EXPANSION", "Cyclicals:\ndurables, autos", "#dbe9f6"),
        (np.pi, 1.75, "PEAK", "Natural resources", "#fde9d9"),
    ]
    for xx, yy, head, body, col in boxes:
        ax.text(xx, yy, f"{head}\n{body}", ha="center", va="center", fontsize=7.6,
                bbox=dict(boxstyle="round,pad=0.35", fc=col, ec="#888", lw=0.7))
    ax.scatter([-np.pi, 0.0, np.pi], [1, -1, 1], color="#1f4e79", zorder=5, s=18)
    ax.set_xlim(-4.3, 4.3); ax.set_ylim(-2.6, 2.5); ax.axis("off")
    ax.set_title("Sector rotation over the business cycle (after BKM Ch. 17)", fontsize=10)
    fig.tight_layout(); fig.savefig(OUT / "mini-09-sector-rotation.png"); plt.close(fig)


def box(ax, xy, w, h, text, fc):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.04", fc=fc, ec="#555", lw=1))
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=8.2)


def arrow(ax, a, b, text, dy=0.0, color="#1f4e79"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, lw=1.6, color=color))
    ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + dy, text, ha="center", va="center", fontsize=7.6, color=color)


def fig_notebook():
    fig, ax = plt.subplots(figsize=(6.4, 3.4), dpi=200)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); ax.axis("off")
    box(ax, (0.2, 2.0), 3.0, 2.2, "FRONT END\nJupyterLab, Notebook\nor VS Code\n\ncells, rendered Markdown\nand LaTeX, output area", "#dbe9f6")
    box(ax, (6.8, 2.0), 3.0, 2.2, "KERNEL (ipykernel)\nseparate Python process\n\nNAMESPACE (memory):\nx = 10, y = 20, imports...", "#e2f0d9")
    arrow(ax, (3.3, 3.55), (6.7, 3.55), "execute_request: cell text", dy=0.28)
    arrow(ax, (6.7, 2.65), (3.3, 2.65), "results: text, plots, errors", dy=-0.28, color="#c0504d")
    box(ax, (0.2, 0.2), 3.0, 1.0, "NOTEBOOK FILE (.ipynb)\ncells + saved outputs + metadata\n(no kernel memory)", "#fff2cc")
    arrow(ax, (1.7, 2.0), (1.7, 1.25), "", color="#555")
    ax.text(2.3, 1.62, "save / open", ha="left", va="center", fontsize=7.6, color="#555")
    ax.text(8.3, 1.2, "Restart kernel: memory wiped\nRe-run a cell: reuses memory", ha="center", va="center", fontsize=7.6,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#aaa", lw=0.7))
    ax.set_title("Notebook architecture: front end, kernel, memory", fontsize=10)
    fig.tight_layout(); fig.savefig(OUT / "mini-13-notebook-architecture.png"); plt.close(fig)


if __name__ == "__main__":
    print("bond stats (price, D, D*, convexity):", fig_price_yield())
    fig_sector_rotation(); fig_notebook()
    for p in sorted(OUT.glob("*.png")):
        print("wrote", p.name)
