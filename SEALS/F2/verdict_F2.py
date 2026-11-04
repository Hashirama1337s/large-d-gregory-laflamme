"""Score BAR-F2 from F2/blind/RESULT.json {"m2": {"2.25": str, "3.25": str, "6.5": str, "13.3": str}}; recomputes [23/23] from predict_F2 defs for P5."""
import json, mpmath as mp
mp.mp.dps = 80
src = open("<lab>/NEXT-2026-11-03/feast/F2/predict_F2.py", encoding="utf-8").read().split("out = {}")[0]
exec(src)
P = json.load(open("<lab>/NEXT-2026-11-03/feast/F2/PRED-F2.json"))["pred"]
R = json.load(open("<lab>/NEXT-2026-11-03/feast/F2/blind/RESULT.json"))["m2"]
res = {}; p5 = True
for i, d in enumerate(["2.25", "3.25", "6.5", "13.3"], start=1):
    x = mp.mpf(R[d]); p = mp.mpf(P[d]["m2_pred"]); bar = mp.mpf(P[d]["bar_abs"])
    res[f"P{i}"] = "HOLDS" if abs(x - p) <= 3 * bar else "FAILED"
    v23 = mp.mpf(d) * pade_at(23, -1 / mp.mpf(d)); p5 &= abs(p - x) < abs(v23 - x)
    print(f"P{i} d={d} {res[f'P{i}']} rel25 {mp.nstr(abs(x-p)/x,3)} rel23 {mp.nstr(abs(x-v23)/x,3)} 3*bar {mp.nstr(3*bar,3)}")
res["P5"] = "HOLDS" if p5 else "FAILED"; print("P5", res["P5"])
json.dump(res, open("<lab>/NEXT-2026-11-03/feast/F2/verdict-F2.json", "w"), indent=1)
