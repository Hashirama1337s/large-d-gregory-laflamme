"""Score BAR-R1 from resurg/RESULT.json: {"K_derived": str, "a": str, "s": str or [re, im], "lambda1": str, "lambda1_err": str, "lambda2": str, "lambda2_err": str}"""
import json, mpmath as mp
mp.mp.dps = 40
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/resurg/RESULT.json"))
res = {}
K = mp.mpf(R["K_derived"]) if "K_derived" in R else None
res["P1"] = "HOLDS" if K is not None and 0.2615 <= K <= 0.2635 else "FAILED"; print("P1", res["P1"], K)
a = mp.mpf(R.get("a", "nan")); s = R.get("s")
s = mp.mpc(*map(mp.mpf, s)) if isinstance(s, list) else (mp.mpc(s) if s else None)
okP2 = s is not None and abs(a - mp.mpf(1)/2) < 1e-12 and abs(s - mp.mpc(-1, mp.pi/2)) < 1e-12
res["P2"] = "HOLDS" if okP2 else "FAILED"; print("P2", res["P2"], a, s)
for key, name, true, bar in (("lambda1", "P3", "0.76765705009210042934400437768", 1e-7), ("lambda2", "P4", "1.6101484684250746", 1e-8)):
    if key not in R: res[name] = "VOID"; print(name, "VOID"); continue
    x, t, eb = mp.mpf(R[key]), mp.mpf(true), mp.mpf(R.get(key + "_err", "0"))
    e = abs(x - t) / t; cover = abs(x - t) <= abs(eb)
    res[name] = "HOLDS" if e < bar and cover else ("PARTIAL(FAILED)" if e < 1e-5 else "FAILED")
    print(name, res[name], f"rel {mp.nstr(e,3)} bar {bar} errbar covers {cover}")
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-R1.json", "w"), indent=1)
