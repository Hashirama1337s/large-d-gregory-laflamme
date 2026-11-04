"""Score BAR-SB from SB/blind/RESULT.json: {"residues": {"-12": str, "-16": str, "-22": str, "-24": str, "-28": str, "-32": str, "-21": str, "-25": str},
 "gap": {"16.4": str, "28.4": str}} (gap = lambda_flat(n)/n - F_AdS(-n))."""
import json, re, mpmath as mp
def num(v):
    m = re.match(r"\s*([-+]?[0-9.]+(e[-+]?[0-9]+)?)", v)
    return mp.mpf(m.group(1)) if m else None
mp.mp.dps = 30
R = json.load(open("<lab>/NEXT-2026-11-03/feast/SB/blind/RESULT.json"))
pred = {"-12": "-0.1741247", "-16": "-8.7487513e-3", "-22": "3.56e-5", "-24": "-4.5777574e-6", "-28": "-5.8435724e-8", "-32": "-5.487887e-10"}
res = {}; signs = True; sizes = True
for d, p in pred.items():
    x = num(R["residues"][d]); p = mp.mpf(p)
    tol = 2e-3 if int(d) <= -24 else 2e-2
    if x is None:  # predicted pole reported as NOT a pole -> fails both sign and size for this point
        signs = False; sizes = False; print(f"d={d} NOT A POLE (reported) pred {mp.nstr(p,8)} -> FAILED point"); continue
    dev = abs(x / p - 1)
    signs &= mp.sign(x) == mp.sign(p); sizes &= dev < tol
    print(f"d={d} res {mp.nstr(x,8)} pred {mp.nstr(p,8)} dev {mp.nstr(dev,3)} tol {tol}")
res["P1"] = "HOLDS" if signs else "FAILED"; res["P2"] = "HOLDS" if sizes else "FAILED"
gp = {"16.4": ("-0.016762385", 1e-2), "28.4": ("-9.9201511e-8", 1e-3)}; ok = True
for n, (p, tol) in gp.items():
    x = mp.mpf(R["gap"][n]); dev = abs(x / mp.mpf(p) - 1); ok &= dev < tol; print(f"gap n={n} {mp.nstr(x,8)} pred {p} dev {mp.nstr(dev,3)} tol {tol}")
res["P3"] = "HOLDS" if ok else "FAILED"
odd = all(num(R["residues"][d]) is not None and abs(num(R["residues"][d])) < 1e-9 for d in ("-21", "-25")); res["P4"] = "HOLDS" if odd else "FAILED"
print(res); json.dump(res, open("<lab>/NEXT-2026-11-03/feast/SB/verdict-SB.json", "w"), indent=1)
