"""Score BAR-K11 from deriv/RESULT.json (keys k11, k12 with 'numeric_80' string, plus exact forms) and deriv/RESULT.json k3..k10 unchanged."""
import json, mpmath as mp
mp.mp.dps = 100
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/deriv/RESULT.json"))
tgt = {"k11": (mp.mpf("-3969169.0871633842087408580221570274341207636791972664152844296"), 55),
       "k12": (mp.mpf("1249860.1461611625459680940754342657981433145624769458693114"), 50)}
res = {}
for key, name in (("k11", "P1"), ("k12", "P2")):
    if key not in R or "numeric_80" not in R[key]:
        res[name] = "VOID"; print(name, "VOID"); continue
    x = mp.mpf(R[key]["numeric_80"]); t, d = tgt[key]
    e = abs(x - t) / abs(t)
    res[name] = "HOLDS" if e < mp.mpf(10) ** -d else "FAILED"
    print(name, res[name], f"rel {mp.nstr(e,3)} (bar 1e-{d})")
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-K11.json", "w"), indent=1)
