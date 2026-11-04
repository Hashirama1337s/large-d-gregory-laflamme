"""Score BAR-DERIV from deriv/RESULT.json: keys "k3","k4","k5","k6" -> {"rational": "p/q", "zeta": {"zeta3": "p/q", ...}} or absent."""
import json
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 110
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/deriv/RESULT.json"))
ours = {"k3": (F(-25, 16), {"zeta3": F(2)}), "k4": (F(363, 128), {"zeta3": F(-5)}),
        "k5": (F(-1335, 256), {"zeta3": F(47, 4), "zeta5": F(-38)}),
        "k6": (F(9923, 1024), {"zeta3": F(-213, 8), "zeta5": F(139), "zeta3^2": F(2), "zeta6": F(-160)})}
val = {"zeta3": mp.zeta(3), "zeta5": mp.zeta(5), "zeta3^2": mp.zeta(3) ** 2, "zeta6": mp.zeta(6), "zeta2": mp.zeta(2), "zeta4": mp.zeta(4)}
def ev(r, z): return mp.mpf(r.numerator) / r.denominator + mp.fsum(mp.mpf(c.numerator) / c.denominator * val[k] for k, c in z.items())
def get(key):
    if key not in R: return None
    d = R[key]; return F(d["rational"]), {k: F(v) for k, v in d.get("zeta", {}).items() if F(v) != 0}
res = {}
for key, name in (("k3", "C1a"), ("k4", "C1b"), ("k5", "P1"), ("k6", "P2")):
    g = get(key)
    if g is None: res[name] = "VOID"; print(name, "VOID (not derived)"); continue
    same = g[0] == ours[key][0] and g[1] == ours[key][1]
    diff = abs(ev(*g) - ev(*ours[key]))
    res[name] = "HOLDS" if same and diff < mp.mpf(10) ** -90 else "FAILED"
    print(name, res[name], "term-by-term", same, "numeric diff", mp.nstr(diff, 3), "seat:", g)
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-DERIV.json", "w"), indent=1)
