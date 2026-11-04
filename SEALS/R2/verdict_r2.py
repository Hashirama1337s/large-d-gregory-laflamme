"""Score BAR-R2 from allorders/TOWERS.json: {"max_order": int, "rational": [str fractions Lam_0..], "zeta3": [...], "zeta5": [...], "zeta2": [...]}
(lists indexed by j = 0..max_order; coefficient of the named constant appearing LINEARLY with no other MZV factor)."""
import json
from fractions import Fraction as F
import sympy as sp
T = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/allorders/TOWERS.json"))
N = int(T["max_order"]); e = sp.symbols("e")
def ser(expr):
    s = sp.series(expr, e, 0, N + 1).removeO()
    return [F(str(sp.nsimplify(s.coeff(e, j)))) for j in range(N + 1)]
pred = {"rational": ser((1 + e) / (1 + 2 * e)),
        "zeta3": ser(4 * e**3 * (1 + e) / (1 + 2 * e)**2),
        "zeta5": ser(-4 * e**5 * (19 + 16 * e) * (1 + e) / (1 + 2 * e)**3),
        "zeta2": [F(0)] * (N + 1)}
res = {}
for key, name in (("rational", "P1"), ("zeta3", "P2"), ("zeta5", "P3"), ("zeta2", "P4")):
    got = [F(x) for x in T[key]]
    bad = [j for j in range(min(len(got), N + 1)) if got[j] != pred[key][j]]
    res[name] = ("HOLDS" if not bad else f"FAILED at j={bad[0]}") + ("" if N >= 25 else " (VOID beyond max_order < 25)")
    print(name, res[name], f"(checked j = 0..{min(len(got)-1, N)})", "" if not bad else f"got {got[bad[0]]} pred {pred[key][bad[0]]}")
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-R2.json", "w"), indent=1)
