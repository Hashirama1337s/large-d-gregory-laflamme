"""Score BAR-K8 (sealed 12089bfbf0135cac) exactly as sealed.
Usage: py -3.11 verdict_k8.py <k7 string> <k7 trusted digits> <k8 string> <k8 trusted digits>
(values = round 2's best k7, k8 from its own new node runs, copied from its report/JSON by the lead)."""
import sys
import json
import mpmath as mp

mp.mp.dps = 130
k7s, d7, k8s, d8 = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
z = {j: mp.zeta(j) for j in range(2, 9)}
z3, z5 = z[3], z[5]
K = [mp.mpf(1), -mp.mpf(1) / 2, mp.mpf(7) / 8, -mp.mpf(25) / 16 + 2 * z3, mp.mpf(363) / 128 - 5 * z3,
     -mp.mpf(1335) / 256 + mp.mpf(47) / 4 * z3 - 38 * z5,
     mp.mpf(9923) / 1024 - mp.mpf(213) / 8 * z3 + 139 * z5 + 2 * z3 ** 2 - 160 * z[6]]
k7f = (-mp.mpf(37193) / 2048 + mp.mpf(3771) / 64 * z3 - mp.mpf(1685) / 4 * z5 - 9 * z3 ** 2 + 880 * z[6]
       + 146 * z[7] + 192 * z3 * z[4])
res = {}

def item(name, verdict, detail):
    res[name] = verdict; print(f"{name}: {verdict}  {detail}")

# C1: zeta(5,3) and the stuffle identity
z53 = mp.nsum(lambda m: (z3 - mp.zeta(3, m)) / m ** 5, [1, mp.inf])
z35 = mp.nsum(lambda m: (z5 - mp.zeta(5, m)) / m ** 3, [1, mp.inf])
st = abs(z53 + z35 + z[8] - z3 * z5)
item("C1", "HOLDS" if st < mp.mpf(10) ** -70 and mp.nstr(z53, 19).startswith("0.03770767298484754") else "FAILED",
     f"stuffle residual {mp.nstr(st,3)}, zeta(5,3) = {mp.nstr(z53,25)}")

e7 = abs(mp.mpf(k7s) - k7f) / abs(k7f)
item("P1", "HOLDS" if e7 < mp.mpf(10) ** -60 else "FAILED", f"k7 rel {mp.nstr(e7,3)} (round2 digits {d7})")
k8B = mp.mpf("7040.441351121886676844141884827666125748803801605022813358790642121349612")
e8 = abs(mp.mpf(k8s) - k8B) / abs(k8B)
item("P2", "HOLDS" if e8 < mp.mpf(10) ** -55 else "FAILED", f"k8 rel vs seat B {mp.nstr(e8,3)}")

# L8 from exact k0..k7 and round 2's k8: log of the series, coefficient of eps^8
Kall = K + [k7f, mp.mpf(k8s)]
# log series via power series: L = log(1 + u), u = sum_{j>=1} k_j eps^j
u = [mp.mpf(0)] + Kall[1:9]
def mul(a, b):
    c = [mp.mpf(0)] * 9
    for i in range(9):
        for j in range(9 - i):
            c[i + j] += a[i] * b[j]
    return c
L = [mp.mpf(0)] * 9; p = [mp.mpf(1)] + [mp.mpf(0)] * 8
for m in range(1, 9):
    p = mul(p, u)
    for j in range(9):
        L[j] += (-1) ** (m + 1) * p[j] / m
L8 = L[8]
basis_names = ["1", "zeta3", "zeta5", "zeta3^2", "zeta6", "zeta7", "zeta3zeta4", "zeta2zeta5", "zeta8", "zeta3zeta5",
               "zeta(5,3)", "zeta2zeta3^2"]
B = [mp.mpf(1), z3, z5, z3 ** 2, z[6], z[7], z3 * z[4], z[2] * z5, z[8], z3 * z5, z53, z[2] * z3 ** 2]
trusted = d8  # L8 inherits k8's digits (k0..k7 exact)
fd = int(trusted * 0.75)
def pslq(x, digits):
    with mp.workdps(digits):
        return mp.pslq([+x] + [+b for b in B], tol=mp.mpf(10) ** -(digits - 3), maxcoeff=10 ** 7, maxsteps=10 ** 6)
rel = pslq(L8, fd)
verified = False
if rel and rel[0] != 0:
    r = (rel[0] * L8 + mp.fsum(c * b for c, b in zip(rel[1:], B))) / rel[0]
    hold = abs(r) < mp.mpf(10) ** -(trusted - 3) * max(1, abs(L8))
    relp = pslq(L8 * (1 + mp.mpf(10) ** -(fd - 5)), fd)
    null_ok = (not relp) or (list(relp) != list(rel) and list(relp) != [-q for q in rel])
    verified = hold and null_ok
    print(f"  relation (find {fd} digits): {rel}; holdout residual {mp.nstr(abs(r),3)}; null -> {relp}")
    coeff = {n: mp.mpf(-c) / rel[0] for n, c in zip(basis_names, rel[1:])}
    print("  L8 =", " + ".join(f"({mp.nstr(v,12)})*{n}" for n, v in coeff.items() if v != 0))
if not verified:
    for P in ("P3", "P4", "P5"):
        item(P, "VOID", f"no verified relation on B8 (trusted digits {trusted}, find {fd})")
else:
    item("P3", "HOLDS" if coeff["1"] == mp.mpf(255) / 16 else "FAILED", f"rational {coeff['1']}")
    item("P4", "HOLDS" if coeff["zeta3"] == -64 else "FAILED", f"zeta3 {coeff['zeta3']}")
    item("P5", "HOLDS" if coeff["zeta3^2"] == 0 else "FAILED", f"zeta3^2 {coeff['zeta3^2']}")
relN = pslq(L8 * (1 + mp.mpf(10) ** -(fd - 5)), fd)
item("N1", "HOLDS" if (not relN) or (rel and list(relN) != list(rel)) else "FAILED", f"perturbed -> {relN}")
json.dump(res, open("<lab>/NEXT-2026-11-02/zeta-k5/verdict-K8.json", "w"), indent=1)
