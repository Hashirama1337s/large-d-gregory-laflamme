"""Score BAR-ADS from adsB/RESULT.json: {"exists": bool, "c": str, "a": {"1": str, ..., "8": str}, "digits": {...}}"""
import json, mpmath as mp
mp.mp.dps = 80
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/adsB/RESULT.json"))
z = {j: mp.zeta(j) for j in range(2, 9)}; z3, z5 = z[3], z[5]
z53 = mp.nsum(lambda m: (z3 - mp.zeta(3, m)) / m ** 5, [1, mp.inf])
L = {3: 4*z3, 4: -8*z3, 5: 16*z3 - 76*z5, 6: -32*z3 + 240*z5 - 320*z[6],
     7: 64*z3 - 656*z5 + 1600*z[6] + 292*z[7] + 384*z3*z[4],
     8: -128*z3 + 1664*z5 - 6400*z[6] + 4136*z[7] - 2304*z3*z[4] + 13984*z[8] + 3840*z3*z5 + 640*z53}
res = {}
res["P0"] = "HOLDS" if R.get("exists") else "FAILED"; print("P0", res["P0"])
c = mp.mpf(R["c"]) if "c" in R else None
res["P1"] = "HOLDS" if c is not None and abs(c - 1) < mp.mpf(10) ** -20 else "FAILED"; print("P1", res["P1"], "c =", c)
a = {int(k): mp.mpf(v) for k, v in R.get("a", {}).items()}
ok = all(j in a for j in range(1, 9))
if ok:
    for j in (1, 2):
        ok &= abs(a[j]) < mp.mpf(10) ** -25; print(f"  a{j} = {mp.nstr(a[j],5)}")
    for j in range(3, 9):
        pred = (-1) ** j * L[j]; e = abs(a[j] - pred) / abs(pred); bar = 25 if j <= 6 else 15
        ok &= e < mp.mpf(10) ** -bar; print(f"  a{j} rel {mp.nstr(e,3)} (bar 1e-{bar})")
res["P2"] = "HOLDS" if ok else "FAILED"; print("P2", res["P2"])
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-ADS.json", "w"), indent=1)
