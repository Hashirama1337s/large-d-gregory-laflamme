# BAR-F2 predictions (referee's strike): PLAIN diagonal Pade of the black-string 1/n series - NO pole law, no K, no c(m).
# Coefficients: exact g0..g12 (np/exact_g.json) + g13..g50 (np/RESULT.json). F(n) = lambda(n)/n = sum g_j n^-j; m^2(d) = d * F(-d).
# Rule fixed before any AdS value at these d exists: prediction = [25/25] Pade at eps = -1/d; bar = max deviation of [23/23], [24/24] from it.
import json, mpmath as mp
mp.mp.dps = 80
B = 'data/'
E = json.load(open(B + 'exact_g.json'))['g']; N = json.load(open(B + 'np_RESULT.json'))['g']
g = [mp.mpf(E[j] if isinstance(E, list) else E[str(j)]) for j in range(13)] + [mp.mpf(N[str(j)]) for j in range(13, 51)]
def pade_at(M, x):
    p, q = mp.pade(g[:2 * M + 1], M, M)
    return mp.polyval(p[::-1], x) / mp.polyval(q[::-1], x)
out = {}
for d in ['2.25', '3.25', '6.5', '13.3']:
    dd = mp.mpf(d); x = -1 / dd
    v = {M: dd * pade_at(M, x) for M in (23, 24, 25)}
    bar = max(abs(v[M] - v[25]) for M in (23, 24))
    out[d] = {"m2_pred": mp.nstr(v[25], 40), "bar_abs": mp.nstr(bar, 3), "bar_rel": mp.nstr(bar / v[25], 3)}
    print(d, out[d])
json.dump({"pred": out}, open('out/PRED-F2.json', 'w'), indent=1)
