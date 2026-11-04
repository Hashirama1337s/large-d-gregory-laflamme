"""Score BAR-F1 from <lab>/NEXT-2026-11-03/feast/F1/blindAdS/RESULT.json {"m2": {"2.5": str, ..., "10": str}, "digits": {...}, "m2_d4": str, "m2_d6": str}"""
import json, mpmath as mp
mp.mp.dps = 50
P = json.load(open("<lab>/NEXT-2026-11-03/feast/F1/PRED-F1.json"))["pred"]
R = json.load(open("<lab>/NEXT-2026-11-03/feast/F1/blindAdS/RESULT.json"))
res = {}; allok = True
for i, d in enumerate(["2.5", "3.5", "4.5", "5.5", "7", "8", "10"], start=1):
    if d not in R.get("m2", {}): res[f"P{i}"] = "VOID"; allok = False; print(f"P{i} d={d} VOID"); continue
    x = mp.mpf(R["m2"][d]); p = mp.mpf(P[d]["m2_pred"]); bar = mp.mpf(P[d]["bar_abs"])
    ok = abs(x - p) <= 3 * bar; allok &= ok
    res[f"P{i}"] = "HOLDS" if ok else "FAILED"
    print(f"P{i} d={d} {res[f'P{i}']}  |diff| {mp.nstr(abs(x-p),3)}  rel {mp.nstr(abs(x-p)/x,3)}  3*bar {mp.nstr(3*bar,3)}")
e45 = abs(mp.mpf(R["m2"].get("4.5", "nan")) - mp.mpf(P["4.5"]["m2_pred"])) / mp.mpf(P["4.5"]["m2_pred"])
e7 = abs(mp.mpf(R["m2"].get("7", "nan")) - mp.mpf(P["7"]["m2_pred"])) / mp.mpf(P["7"]["m2_pred"])
res["P8"] = "HOLDS" if e45 < 1e-9 and e7 < 1e-13 else "FAILED"; print("P8", res["P8"], mp.nstr(e45, 3), mp.nstr(e7, 3))
l3, l5 = mp.mpf("2.4987905611804067816629204648"), mp.mpf("4.3561757479203580")
n1 = abs(mp.mpf("0.95943667473538799589") - l3) / l3 > 0.1 and abs(mp.mpf("0.062628221420310855226") - l5) / l5 > 0.1
res["N1"] = "HOLDS" if n1 else "FAILED"; print("N1", res["N1"])
for k, t in (("m2_d4", "5.457"), ("m2_d6", "7.308")):
    print("control", k, R.get(k), "published", t)
json.dump(res, open("<lab>/NEXT-2026-11-03/feast/F1/verdict-F1.json", "w"), indent=1)
