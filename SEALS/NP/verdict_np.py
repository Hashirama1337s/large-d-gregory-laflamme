"""Score BAR-NP P1 from np/RESULT.json {"g": {"41": str, ..., "50": str}, "rel_err": {"41": float, ...}}.
P2, P3, N1 are scored by running council/glance/g2_fit.py (window j = 30..50) and g6_resum2.py with the new coefficients;
any code change limited to input reading, diff disclosed in LOG (declared in BAR-NP before results)."""
import json, mpmath as mp
mp.mp.dps = 40
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/np/RESULT.json"))
P = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/council/glance/g12_pred.json"))
ok = True; rows = []
for j in range(41, 51):
    s = str(j)
    if s not in R["g"]: ok = False; rows.append(f"g{j}: MISSING"); continue
    x, p = mp.mpf(R["g"][s]), mp.mpf(P[s]); tol = 0.05 if j in (44, 48) else 0.03
    e = abs(x - p) / abs(p); trusted = R.get("rel_err", {}).get(s, 1.0) < 0.01
    good = e < tol and trusted; ok &= good
    rows.append(f"g{j}: new {mp.nstr(x,8)} pred {mp.nstr(p,8)} rel {mp.nstr(e,3)} tol {tol} trusted<1% {trusted} -> {'ok' if good else 'MISS'}")
print("\n".join(rows)); print("P1", "HOLDS" if ok else "FAILED")
json.dump({"P1": "HOLDS" if ok else "FAILED"}, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-NP.json", "w"), indent=1)
