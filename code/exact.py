"""Exact g0..g12 (lambda/n = sum g_j n^-j) evaluated to high precision.
k_j forms from deriv/RESULT.json; MZVs evaluated by own path-splitting at 1/2 (own code, same idea as
the deriv seat).  Controls: zeta(2,1)=zeta(3), comparison with deriv's 100-digit MZV values."""
import json, re, sys, os
import mpmath as mp
from fractions import Fraction

RES = 'data/deriv_RESULT.json'

def c2w(comp):
    w = []
    for s in comp:
        w += [0] * (s - 1) + [1]
    return tuple(w)

def _series(u, N, cache):
    # coefficients c_i of H(u;x)=sum c_i x^i, u ends in 1; H(a u';x)=int_0^x f_a H(u';t)dt
    if u in cache:
        return cache[u]
    a, up = u[0], u[1:]
    if not up:
        res = [mp.mpf(0)] + [mp.mpf(1) / i for i in range(1, N + 1)]
    else:
        h = _series(up, N, cache)
        res = [mp.mpf(0)] * (N + 1)
        if a == 0:
            for i in range(1, N + 1):
                res[i] = h[i] / i
        else:
            cum = mp.mpf(0)
            for i in range(1, N + 1):
                cum += h[i - 1]
                res[i] = cum / i
    cache[u] = res
    return res

def _half(u, N, cache, hc):
    if not u:
        return mp.mpf(1)
    if u in hc:
        return hc[u]
    c = _series(u, N, cache)
    s = mp.mpf(0); p = mp.mpf(1)
    for i in range(1, N + 1):
        p /= 2
        s += c[i] * p
    hc[u] = s
    return s

def mzv(comp, dps):
    with mp.workdps(dps + 20):
        N = int((dps + 20) * 3.33) + 60
        w = c2w(comp); cache = {}; hc = {}
        s = mp.mpf(0)
        for k in range(len(w) + 1):
            outer = tuple(1 - a for a in reversed(w[:k]))
            s += _half(outer, N, cache, hc) * _half(w[k:], N, cache, hc)
        return +s

TOK = re.compile(r'zeta(?:\(([\d,]+)\)|(\d+))(?:\^(\d+))?\*?')

def monomial(key, dps, zc):
    pos = 0; val = mp.mpf(1)
    while pos < len(key):
        m = TOK.match(key, pos)
        if not m:
            raise ValueError('cannot parse ' + key)
        comp = tuple(int(x) for x in m.group(1).split(',')) if m.group(1) else (int(m.group(2)),)
        e = int(m.group(3)) if m.group(3) else 1
        if comp not in zc:
            zc[comp] = mp.zeta(comp[0]) if len(comp) == 1 else mzv(comp, dps)
        val *= zc[comp] ** e
        pos = m.end()
    return val

def exact_k(dps):
    d = json.load(open(RES))
    zc = {}
    with mp.workdps(dps + 20):
        K = [mp.mpf(1), mp.mpf(-1) / 2, mp.mpf(7) / 8]
        for j in range(3, 13):
            e = d['k%d' % j]
            q = Fraction(e['rational'])
            v = mp.mpf(q.numerator) / q.denominator
            for key, c in e['zeta'].items():
                q = Fraction(c)
                v += mp.mpf(q.numerator) / q.denominator * monomial(key, dps, zc)
            K.append(v)
    return K, zc, d

def exact_g(dps):
    K, zc, d = exact_k(dps)
    with mp.workdps(dps + 20):
        g = [mp.fsum(K[i] * K[j - i] for i in range(j + 1)) for j in range(13)]
    return g, K, zc, d

if __name__ == '__main__':
    dps = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    mp.mp.dps = dps + 20
    print('control zeta(2,1)-zeta(3):', mp.nstr(mzv((2, 1), dps) - mp.zeta(3), 3))
    print('control zeta(2,2,2)-pi^6/7!:', mp.nstr(mzv((2, 2, 2), dps) - mp.pi ** 6 / mp.factorial(7), 3))
    g, K, zc, d = exact_g(dps)
    ref = d['v2']['mzv_values_100_digits']
    for comp, v in zc.items():
        if len(comp) > 1:
            key = 'zeta(%s)' % ','.join(map(str, comp))
            print(key, 'vs deriv 100-digit:', mp.nstr(v - mp.mpf(ref[key]), 3))
    for j in (8, 10, 11, 12):
        num = d['k%d' % j].get('numeric_80') if 'numeric_80' in d['k%d' % j] else d['decimal_values'].get('k%d' % j)
        print('k%d' % j, mp.nstr(K[j], 40), 'deriv:', str(num)[:42])
    json.dump({'dps': dps, 'g': [mp.nstr(x, dps + 5) for x in g], 'k': [mp.nstr(x, dps + 5) for x in K]},
              open('out/exact_g.json', 'w'))
    print('g12 =', mp.nstr(g[12], 30))
