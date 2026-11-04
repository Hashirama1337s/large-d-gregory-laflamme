# BAR-F1 predictions: AdS_{d+1} black-brane static sound-channel screening mass m^2(d) = d * F_pert(-d) from BLACK-STRING data only
# (g0..g40 round2/gall.json, g41..g50 np/RESULT.json; pole law R_N from resurg/R1 with K = sqrt(e)/(2 pi) derived, c(m) measured).
# Fixed rule (written before any AdS value at these d exists): ensemble N0 in {1,3,5} x (J,M) in {(40,20),(46,23),(50,25)};
# prediction = median of the 9; error bar = max |member - median|. Also the flat-side null at n = +3, +5.
import json, mpmath as mp
mp.mp.dps = 60
B = '<lab>/NEXT-2026-11-02/zeta-k5/'
g = [mp.mpf(s) for s in json.load(open(B + 'round2/gall.json'))['g']]
npg = json.load(open(B + 'np/RESULT.json'))['g']
for j in range(41, 51): g.append(mp.mpf(npg[str(j)]))
K = mp.sqrt(mp.e) / (2 * mp.pi)
def c(m): return 1 - mp.mpf(1) / (12 * m) + mp.mpf('3.40759') / m**2 - mp.mpf('3.781') / m**3
def R(N):
    m = 2 * N; return (-1)**N * K * m * (mp.e**2 / m)**(m / 2) * c(m)
NMAX = 400
Rs = {N: R(N) for N in range(1, NMAX)}
def F(n, N0, J, M):
    r = [g[0]] + [g[j] - sum(Rs[N] * (2 * N)**(j - 1) for N in range(N0, NMAX)) for j in range(1, J + 1)]
    p, q = mp.pade(r[:2 * M + 1], M, M)
    x = 1 / n
    return mp.polyval(p[::-1], x) / mp.polyval(q[::-1], x) + sum(Rs[N] / (n - 2 * N) for N in range(N0, NMAX))
ENS = [(N0, J, M) for N0 in (1, 3, 5) for (J, M) in ((40, 20), (46, 23), (50, 25))]
out = {}
for d in ['2.5', '3.5', '4.5', '5.5', '7', '8', '10']:
    dd = mp.mpf(d); vals = sorted([dd * F(-dd, *e) for e in ENS])
    med = vals[4]; bar = max(abs(v - med) for v in vals)
    out[d] = {"m2_pred": mp.nstr(med, 30), "bar_abs": mp.nstr(bar, 3), "bar_rel": mp.nstr(bar / med, 3)}
    print(d, out[d])
nul = {}
for n in ('3', '5'):
    nn = mp.mpf(n); vals = sorted([nn * F(nn, *e) for e in ENS]); nul[n] = mp.nstr(vals[4], 20)
    print('flat null n =', n, 'lambda_pert =', nul[n])
json.dump({"pred": out, "flat_null_lambda_pert": nul}, open('PRED-F1.json', 'w'), indent=1)
