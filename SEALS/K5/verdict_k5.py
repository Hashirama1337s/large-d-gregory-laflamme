"""Score BAR-K5 (sealed 8ee216d2e92f9346) exactly as sealed, from seatB/RESULT.json. POST HOC items labelled."""
import json
import mpmath as mp

mp.mp.dps = 120
R = json.load(open("<lab>/NEXT-2026-11-02/zeta-k5/seatB/RESULT.json"))
z3, z5 = mp.zeta(3), mp.zeta(5)
k = [1, -mp.mpf(1) / 2, mp.mpf(7) / 8, -mp.mpf(25) / 16 + 2 * z3, mp.mpf(363) / 128 - 5 * z3,
     -mp.mpf(1335) / 256 + mp.mpf(47) / 4 * z3 - 38 * z5]
g = [mp.fsum(k[i] * k[K - i] for i in range(K + 1)) for K in range(6)]
rel = lambda a, b: abs(mp.mpf(a) - b) / abs(b)
out = []

def item(name, ok, detail):
    out.append((name, "HOLDS" if ok else "FAILED", detail)); print(f"{name}: {'HOLDS' if ok else 'FAILED'}  {detail}")

e3, e4 = rel(R["g"]["3"], g[3]), rel(R["g"]["4"], g[4])
item("C1", e3 < 1e-25 and e4 < 1e-25, f"g3 rel {mp.nstr(e3,3)}, g4 rel {mp.nstr(e4,3)}")
lamC = mp.mpf("0.767657050092100429344004377681")
e = rel(R["lambda_d4"], lamC)
item("C2", e < 1e-25 and mp.nstr(mp.mpf(R["lambda_d4"]), 4) == "0.7677", f"lambda4 rel {mp.nstr(e,3)} (seat C has 30 digits), 4-digit {mp.nstr(mp.mpf(R['lambda_d4']),4)}")
e5 = rel(R["k"]["5"], k[5])
item("P1", e5 < 1e-30, f"k5 rel {mp.nstr(e5,3)}")
k6C = mp.mpf("-38.066385714840371975203724541647915454106839816528694409829")
e6 = rel(R["k"]["6"], k6C)
item("P2", e6 < 1e-25, f"k6 rel {mp.nstr(e6,3)}")
e30 = rel(R["lambda_n27"], mp.mpf("26.07475246167124")); e50 = rel(R["lambda_n47"], mp.mpf("46.04284561245624"))
item("P3", e30 < 1e-14 and e50 < 1e-14, f"d30 rel {mp.nstr(e30,3)}, d50 rel {mp.nstr(e50,3)}")
kb = mp.mpf(R["k"]["5"])
wrong = -mp.mpf(1335) / 256 + mp.mpf(47) / 4 * z3 - 37 * z5
en = rel(kb, wrong) if False else abs(kb - wrong) / abs(kb)
item("N1", en > 1e-2, f"-37 zeta5 variant misses by rel {mp.nstr(en,3)}")
with mp.workdps(40):
    r1 = mp.pslq([kb, 1, z3], tol=mp.mpf(10) ** -30, maxcoeff=10 ** 6, maxsteps=10 ** 6)
    r2 = mp.pslq([kb * (1 + mp.mpf(10) ** -25), 1, z3, z5], tol=mp.mpf(10) ** -30, maxcoeff=10 ** 5, maxsteps=10 ** 6)
item("N2", r1 is None and r2 is None, f"no-zeta5 basis -> {r1}; perturbed -> {r2}")

print("\nPOST HOC (not sealed): seat B identified k6 = 9923/1024 - (213/8)zeta3 + 139 zeta5 + 2 zeta3^2 - 160 zeta6;")
z6 = mp.zeta(6)
k6x = mp.mpf(9923) / 1024 - mp.mpf(213) / 8 * z3 + 139 * z5 + 2 * z3 ** 2 - 160 * z6
print("  vs seat C k6 (57 digits, unidentified): rel", mp.nstr(rel(k6C, k6x), 3))
print("  vs seat B fitted k6:", mp.nstr(rel(R["k"]["6"], k6x), 3))
json.dump({n: v for n, v, _ in out}, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-K5.json", "w"), indent=1)
