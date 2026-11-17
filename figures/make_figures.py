"""Draw the README figures of large-d-gregory-laflamme from the data the repository ships.

Usage:  python figures/make_figures.py <repo root>
Needs Python 3.11, matplotlib 3.11 and mpmath. Writes figures/*.svg next to this script.

Every plotted number is read from shipped files:
  data/F2_PRED.json, data/F2_blind_RESULT.json   sealed plain-Pade predictions and blind 40-digit answers (BAR-F2)
  data/F1_PRED.json, data/F1_blind_RESULT.json   sealed first-test predictions and blind answers (BAR-F1)
  paper.md (tables of sections 5.2 and 5.3)      which test dimensions were fresh
  data/exact_g.json                              exact g0..g12 (lambda/n = sum g_j n^-j), 450 digits
  data/deriv_RESULT.json                         decimal k_j and k11, k12 (cross-check of the k_j rebuilt from g)
  SEALS/R1/BAR-R1.md                             the reference value lambda(2) used by the sealed test BAR-R1
"""
import json
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import mpmath as mp

# ---------------------------------------------------------------- brand style (figures/STYLE.md)
BG, BORDER, GRID, AXC, TXT, ACC = "#1c2026", "#2f353d", "#22272e", "#9aa4ae", "#e8edf2", "#39ff14"
CAT = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#0ca30c", "#9085e9", "#e66767"]
W_IN = 12.5  # 900 pt viewBox width

plt.rcParams.update({
    "svg.fonttype": "none", "svg.hashsalt": "moki-julio",
    "font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 16, "axes.labelsize": 17, "xtick.labelsize": 15, "ytick.labelsize": 15,
    "axes.facecolor": BG, "figure.facecolor": "none", "savefig.facecolor": "none",
    "axes.edgecolor": AXC, "axes.labelcolor": TXT, "xtick.color": AXC, "ytick.color": AXC,
    "text.color": TXT, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1.0,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
    "legend.fontsize": 14, "lines.linewidth": 2.0, "axes.axisbelow": True,
})


def new_fig(h_in):
    fig = plt.figure(figsize=(W_IN, h_in))
    fig.patches.append(FancyBboxPatch((0.004, 0.006), 0.992, 0.988, boxstyle="round,pad=0,rounding_size=0.015",
                                      transform=fig.transFigure, facecolor=BG, edgecolor=BORDER, linewidth=1.5,
                                      zorder=-10))
    return fig


def title(fig, main, sub):
    fig.text(0.035, 0.94, main, fontsize=21, fontweight="bold", color=TXT, va="top")
    fig.text(0.035, 0.94 - 0.075 * 6.0 / fig.get_figheight(), sub, fontsize=15, color=AXC, va="top")


def save(fig, out, name):
    path = os.path.join(out, name)
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print("wrote figures/" + name)


def load(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------- figure 1: sealed predictions vs blind answers
def fresh_status(root):
    """Return {d: status} from the BAR-F1 and BAR-F2 tables of paper.md (sections 5.2, 5.3)."""
    text = open(os.path.join(root, "paper.md"), encoding="utf-8").read()
    out = {}
    for sec in ("### 5.2", "### 5.3"):
        block = text.split(sec, 1)[1].split("\n### ", 1)[0]
        for m in re.finditer(r"^\| ([0-9.]+) \| ([a-z ,-]+) \|", block, re.M):
            out[(sec, m.group(1))] = m.group(2).strip()
    return out


def rel_errors(pred, blind):
    rows = []
    for d, p in pred["pred"].items():
        b = mp.mpf(blind["m2"][d])
        rel = abs(mp.mpf(p["m2_pred"]) - b) / b
        passline = 3 * mp.mpf(p["bar_abs"]) / b
        rows.append((float(d), float(rel), float(passline), d))
    return sorted(rows)


def fig_blind(root, out):
    mp.mp.dps = 60
    status = fresh_status(root)
    f2 = rel_errors(load(root, "data/F2_PRED.json"), load(root, "data/F2_blind_RESULT.json"))
    f1 = rel_errors(load(root, "data/F1_PRED.json"), load(root, "data/F1_blind_RESULT.json"))

    fig = new_fig(7.4)
    title(fig, "Sealed predictions against blind answers",
          "Screening mass of the holographic plasma at dimensions the method had not been tuned on")
    ax = fig.add_axes([0.105, 0.13, 0.86, 0.66])
    ax.set_yscale("log")
    series = [("### 5.3", f2, CAT[0], "o", "Plain Padé [25/25] test (BAR-F2)"),
              ("### 5.2", f1, CAT[1], "s", "First test, pole-subtracted (BAR-F1)")]
    for sec, rows, col, mk, _ in series:
        for d, rel, pl, key in rows:
            fresh = status[(sec, key)] == "fresh"
            ax.plot([d, d], [rel, pl], color=col, lw=1, alpha=0.35, zorder=1)
            ax.plot(d, pl, marker="_", ms=22, mew=2, color=AXC, zorder=2)
            ax.plot(d, rel, marker=mk, ms=11, mew=2, color=col, mfc=col if fresh else BG, zorder=3)
    spots = {"3.25": (1.65, 3e-15, "left"), "6.5": (7.0, 1e-22, "left")}
    for d, rel, pl, key in f2:
        if status[("### 5.3", key)] == "fresh":
            dig = int(mp.nint(-mp.log10(rel)))
            x, y, ha = spots[key]
            ax.annotate("fresh d = %s: error %s\n(about %d digits right)" % (key, mp.nstr(mp.mpf(rel), 2), dig),
                        (d, rel), xytext=(x, y), textcoords="data", fontsize=14, color=TXT, ha=ha, va="center",
                        arrowprops=dict(arrowstyle="-", color=AXC, lw=1, shrinkB=8))
    ax.set_xlim(1.5, 14.2)
    ax.set_ylim(1e-24, 1e-3)
    ax.set_xlabel("dimension d of the plasma (non-integer d are mathematical test points)")
    ax.set_ylabel("relative error, log scale")
    ax.yaxis.set_major_locator(matplotlib.ticker.LogLocator(numticks=12))
    handles = [Line2D([], [], color=CAT[0], marker="o", ls="", ms=11, mew=2, label=series[0][4]),
               Line2D([], [], color=CAT[1], marker="s", ls="", ms=11, mew=2, label=series[1][4]),
               Line2D([], [], color=AXC, marker="o", ls="", ms=11, mew=2, mfc=BG, label="hollow: not a fresh point"),
               Line2D([], [], color=AXC, marker="_", ls="", ms=22, mew=2, label="pass line (3 × sealed bar)")]
    ax.legend(handles=handles, loc="upper right", ncol=2, columnspacing=1.4, handletextpad=0.4)
    save(fig, out, "blind-test.svg")
    return f1, f2


# ---------------------------------------------------------------- figure 2: partial sums run away at D = 6
def sqrt_series(g):
    k = [mp.sqrt(g[0])]
    for j in range(1, len(g)):
        s = g[j] - sum(k[i] * k[j - i] for i in range(1, j))
        k.append(s / (2 * k[0]))
    return k


def fig_partial(root, out):
    mp.mp.dps = 120
    g = [mp.mpf(x) for x in load(root, "data/exact_g.json")["g"]]
    assert len(g) == 13
    k = sqrt_series(g)
    der = load(root, "data/deriv_RESULT.json")
    for j, v in der["decimal_values"].items():          # cross-check against the derivation seat's decimals
        assert abs(k[int(j[1:])] - mp.mpf(v)) <= mp.mpf(10) ** -25 * max(1, abs(mp.mpf(v))), j
    for j in ("k11", "k12"):
        assert abs(k[int(j[1:])] - mp.mpf(der[j]["numeric_80"])) < mp.mpf(10) ** -60, j
    bar = open(os.path.join(root, "SEALS/R1/BAR-R1.md"), encoding="utf-8").read()
    lam2 = mp.mpf(re.search(r"lambda\(2\) \(([0-9.]+)\.\.\.\)", bar).group(1))
    n = mp.mpf(2)
    true = mp.sqrt(lam2)                                  # k_GL r0 at n = 2 (D = 6)
    errs, s = [], mp.mpf(0)
    for j in range(13):
        s += k[j] / n ** j
        errs.append(float(abs(mp.sqrt(n) * s - true) / true))
    best = min(range(13), key=lambda j: errs[j])

    fig = new_fig(6.6)
    title(fig, "Past the 1/n⁴ term, more exact terms make it far worse",
          "Black string in D = 6: the exact series summed term by term, compared with the true threshold")
    ax = fig.add_axes([0.15, 0.14, 0.815, 0.63])
    ax.set_yscale("log")
    ax.plot(range(13), [100 * e for e in errs], color=ACC, marker="o", ms=9, zorder=3)
    ax.annotate("best: through the 1/n⁴ term,\noff by %.1f %%" % (100 * errs[best]),
                (best, 100 * errs[best]), xytext=(22, 0), textcoords="offset points", fontsize=14,
                ha="left", va="center")
    ax.annotate("one more term:\noff by about %d %%" % int(float("%.2g" % (100 * errs[best + 1]))),
                (best + 1, 100 * errs[best + 1]),
                xytext=(-14, 30), textcoords="offset points", fontsize=14, ha="right", va="bottom",
                arrowprops=dict(arrowstyle="-", color=AXC, lw=1, shrinkB=6))
    ax.annotate("all 13 exact terms:\noff by about %s %%" % format(round(100 * errs[12], -3), ",.0f"),
                (12, 100 * errs[12]), xytext=(12.45, 1.5e3), textcoords="data", fontsize=14,
                ha="right", va="top", arrowprops=dict(arrowstyle="-", color=AXC, lw=1, shrinkB=6))
    ax.set_xticks(range(13))
    ax.set_xlim(-0.4, 12.6)
    ax.set_ylim(1, 6e5)  # the d = 11 point (2.62e5 %) must not touch the top edge
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: format(v, ",.0f") + " %"))
    ax.set_xlabel("last term included (power of 1/n, with D = n + 4 = 6)")
    ax.set_ylabel("error of the partial sum, log scale")
    save(fig, out, "partial-sums-d6.svg")
    return errs, true


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python make_figures.py <repo root>")
    root = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    out = here if os.path.basename(here) == "figures" else os.path.join(here, "figures")
    os.makedirs(out, exist_ok=True)
    f1, f2 = fig_blind(root, out)
    errs, true = fig_partial(root, out)
    print("BAR-F2 relative errors:", ", ".join("d=%s %s" % (r[3], mp.nstr(mp.mpf(r[1]), 3)) for r in f2))
    print("BAR-F1 relative errors:", ", ".join("d=%s %s" % (r[3], mp.nstr(mp.mpf(r[1]), 3)) for r in f1))
    print("D = 6 reference k_GL r0 =", mp.nstr(true, 8))
    print("D = 6 partial-sum errors (%):", ", ".join("%d:%.3g" % (j, 100 * e) for j, e in enumerate(errs)))


if __name__ == "__main__":
    main()
