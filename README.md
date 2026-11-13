# When a black string cracks: the Gregory-Laflamme threshold to order 1/n^12

**The exact recipe for when a stretched black hole (a black string) starts to break apart, pushed from five terms to thirteen; summed the right way, those 13 exact terms plus 38 numerical ones predicted how a hot holographic plasma screens a disturbance to about 15 digits.**

[![DOI 10.5281/zenodo.23940227](brand/doi.svg)](https://doi.org/10.5281/zenodo.23940227) ![Licence: text and data CC BY 4.0, code MIT](brand/licence.svg) [![Moki & Julio lab map](brand/lab.svg)](https://github.com/Hashirama1337s)

Moki & Julio · 2026 · version 1.0

**Read** [paper.md](paper.md) · **Re-run** [REPRODUCE.md](REPRODUCE.md) (Python + mpmath, seconds) · **Check**
[SEALS/HASHES.md](SEALS/HASHES.md) · **Companion** [Paper II](https://github.com/Hashirama1337s/airy-edge-hydrodynamics)

## In plain words

Many black-hole questions are hard to solve exactly in our four dimensions. They become simple when the number of
dimensions is very large. The price is that every answer comes as an endless list of corrections, one per power of 1/D.

A **black string** is a black hole stretched along an extra dimension. If it is long enough, it is unstable and starts to
break up. A picture that helps (it is only a picture): a thin stream of water from a tap, which beads into drops once it is
long enough. Where the picture breaks: there is no water and no surface tension here, only the geometry of space and time,
and we compute only the point where the trouble *starts*, not what happens after.

That starting point is one number, the **Gregory-Laflamme threshold**. Five terms of its list were published in 2015 and
2018. We now have thirteen in all, derived by exact algebra and checked against numbers computed separately. The terms are
built from famous constants, the zeta values (for example zeta(3) = 1 + 1/8 + 1/27 + 1/64 + ...), including rarer
"multiple" zeta values such as zeta(5,3) and zeta(3,5,3).

The surprise came next. The list grows so fast that adding terms eventually makes things worse: there is strong numerical
evidence that it never converges. But a standard change of variables turns the same list into a statement about a hot
plasma of the kind studied with holography (a way of modelling a hot plasma with a black hole in one extra dimension).
Summed with a standard rational method, the 13 exact terms plus 38 computed numerically (51 in all) predicted that
plasma's screening mass (how strongly it damps a still disturbance) to about 9 digits at d = 3.25 and about 15 digits at
d = 6.5, two dimensions it had not been tuned on. The same method does not work in the other direction, for the black
string itself in low dimensions.

Why "d = 3.25"? The formulas can be evaluated at any d, whole or not. A non-integer d is a mathematical test point, not a
real space, and that makes it a fair exam: nothing had been tuned there.

Every scored prediction was written down and hashed before a separate, blind seat computed the answer, except where the
scorecards flag otherwise. Failures are listed as failures.

## At a glance

*The exact claims, for specialists. Terms are explained in "How it works" and "Words you will meet".*

- **Series.** The static threshold lambda(n) = (k_GL r0)^2 in D = n + 4 is derived analytically in closed form through
  n^-12 within the standard large-D matched-asymptotic framework. zeta(5,3) enters at order 8; at order 11 an irreducible
  depth-three value (zeta(3,5,3) in our basis). The derived k11, k12 reproduced numerics sealed first to 2.5e-64 and 1.9e-59.
- **Large-order law.** A law fitted on coefficients through g40 predicted g41..g50 within 0.3 % (bar 3 %; 5 % at j = 44, 48).
- **Resummation.** Continued to n = -d, plain Pade [25/25] gives the static sound-channel screening mass of the AdS_{d+1}
  black brane with blind relative error 1.2e-15 at fresh d = 6.5 and 5.8e-10 at fresh d = 3.25; a first, pole-subtracted
  test gave 2.2e-10, 2.9e-12 and 7.4e-14 at fresh d = 3.5, 4.5, 5.5.
- **Tension.** Any term the resummation misses on the AdS side is below 2e-11 at d = 4 (a training point) and 3e-12 at
  fresh d = 4.5, a tension with the heuristic extension to AdS of the expected non-perturbative corrections.

Full wording, prior art and disclosures: [paper.md](paper.md) (Appendix B lists every protocol slip). The scorecard:

![Scorecard of every sealed test](scorecard.svg)

Full technical record: [TECHNICAL.md](TECHNICAL.md).

## What we do not claim

- No remainder bounds on any closed form; the far zone is treated as beyond all orders (the standard assumption). The
  internal referee covered the derivation through n^-10; k11 and k12 rest on the derivation seat plus the sealed numerics.
- Divergence of the series is strong numerical evidence, not a proof.
- No resummation reached D = 5 to the sealed accuracy, and the same Pade pipeline misses the black-string threshold at
  n = 3 and 5 by 62 % and 99 %. Several sealed tests FAILED (BAR-NP P3, BAR-R1 P3-P4, BAR-SB P1-P3), including a
  proposed bridge through negative d.
- No proof that the resummation converges; the error falls overall with Pade order, not monotonically.
- The F2 target values come from F1's master equation, cross-checked by separately written code but not by an independent
  equation.
- The large-order law rests on one sealed prediction set (g41..g50) and one sealed exponent fit, with no sealed null
  extrapolation beside them.
- The internal referee is a separately briefed seat of the same lab, not external peer review. Disclosed slips are in
  Appendix B of the paper; none changed a verdict.

## How it works

### The idea

One list of numbers, two uses. Read directly, it describes a black string in D = n + 4 dimensions. Replace n by -d (the
"mirror", known as the AdS/Ricci-flat map), and it describes a black brane in anti-de Sitter space with d boundary
dimensions: the holographic plasma.

```mermaid
flowchart LR
  A[Black string in D = n + 4<br/>when does it start to crack?] --> B[13 exact terms + 38 computed<br/>numerically: 51 in all]
  B --> C[Mirror: n becomes -d]
  C --> D[Rational resummation<br/>Pade 25/25]
  D --> E[Screening mass of the<br/>AdS plasma at any d]
  E --> F[Checked against blind<br/>40-digit computations]
```

Where the mirror analogy breaks: the two sides have different boundary conditions. The dictionary was checked on the
list of terms (to order n^-4 in 2015, and here numerically, term by term, for orders 3 to 8), which does not make it
automatic for everything you build from it. It worked towards the plasma side; it did not work back on the black-string
side at low dimension.

### A worked example

The threshold wavenumber times the horizon radius is written k_GL r0 = sqrt(n) (k0 + k1/n + k2/n^2 + ...). Its square is
lambda(n) = (k_GL r0)^2, and lambda(n)/n = g0 + g1/n + g2/n^2 + ... is the form we resum. The first k terms are 1, -1/2
and 7/8. Then zeta
values appear: k3 = 2 zeta(3) - 25/16, and k5 = -1335/256 + (47/4) zeta(3) - 38 zeta(5) = -30.4939... Further out the terms
grow fast:

| term | value |
|---|---|
| k5 | -30.49392983... |
| k8 | 7040.44135112... |
| k10 | -458974.765607... |
| k11 | -3969169.08716... |
| k12 | 1249860.14616... |

You can watch the runaway happen. At D = 6, the sum through the 1/n^4 term is off by 2.4 %; adding the next term makes it
off by 110 %. Measured another way, the size of the j-th coefficient g_j, taken to the power 1/j, rises from 3.3 at
j = 8 to 11.2 at j = 40.

So instead of adding terms one by one, we fit a **fraction**, a ratio of two polynomials of degree 25 (a Pade approximant),
that agrees with the list g0..g50: the 13 exact terms plus 38 computed numerically from high-precision solutions
(51 in all). Evaluated at n = -d it gives the plasma's screening mass m^2(d). At d = 6.5 the sealed
prediction was m^2 = 7.785729384100830426657530533626601859545; a blind seat then computed the true value, and the
relative error was 1.17e-15. As a control at d = 4 (a training point, so not a test) the series agrees with the five
published digits, m = 2.3361 pi T, and with a 40-digit computation to 2e-11.

## Reproduce and reuse

Questions this lets you answer:

- What is the static screening mass of the AdS_{d+1} black brane at a non-integer d, say 3.25 or 6.5?
- What are k0..k12 and g0..g12 to 450 digits, or the closed forms of k3..k12?
- Do the sealed predictions, verdicts and hashes check out?

**Re-run the headline numbers** (Python 3 and mpmath, nothing else; run from the top folder). `-c core.autocrlf=false`
keeps the files byte for byte as committed; on Windows a default clone converts line endings and every line of the hash
check then fails.

```
git clone -c core.autocrlf=false https://github.com/Hashirama1337s/large-d-gregory-laflamme
cd large-d-gregory-laflamme
mkdir out
python code/exact.py 450
python code/predict_F2.py
python code/verdict_F2.py
python code/verdict_F1.py
sha256sum -c MANIFEST.sha256
```

`code/verdict_F2.py` should end with

```
P1 d=2.25 HOLDS rel25 2.2e-7 rel23 5.36e-7 3*bar 1.78e-5
P2 d=3.25 HOLDS rel25 5.84e-10 rel23 2.52e-9 3*bar 3.03e-8
P3 d=6.5 HOLDS rel25 1.17e-15 rel23 4.18e-14 3*bar 9.48e-13
P4 d=13.3 HOLDS rel25 2.6e-23 rel23 1.43e-21 3*bar 6.3e-20
P5 HOLDS
```

Every expected output is listed in [REPRODUCE.md](REPRODUCE.md). `MANIFEST.sha256` on the main branch covers the files
as they are now, including this README. To check the archived release (the Zenodo v1.0 deposit) instead, run
`git checkout v1.0` right after `cd`, then the same commands.

**Reuse the resummation at your own d.** This is the recipe of `code/predict_F2.py`, trimmed to a function (run it from
the top folder):

```python
import json, mpmath as mp
mp.mp.dps = 80
E = json.load(open('data/exact_g.json'))['g']        # exact g0..g12
N = json.load(open('data/np_RESULT.json'))['g']      # fitted g13..g50
g = [mp.mpf(E[j]) for j in range(13)] + [mp.mpf(N[str(j)]) for j in range(13, 51)]
p, q = mp.pade(g[:51], 25, 25)

def m2(d):
    """Pade [25/25] screening mass m^2(d) of the AdS_{d+1} black brane (units r0 = L_AdS = 1)."""
    d = mp.mpf(d); x = -1 / d
    return d * mp.polyval(p[::-1], x) / mp.polyval(q[::-1], x)

print(mp.nstr(m2('6.5'), 20))   # 7.7857293841008304267, the sealed BAR-F2 prediction
```

Compare `m2(4)` with the published 5.457 and `m2(6)` with 7.308. The tests cover 2.25 <= d <= 13.3; outside that range
the function is untested, and it does not work for the black string itself (positive n) at low dimension.

## Words you will meet

- **Black string** - a black hole stretched along an extra dimension; uniform ones are unstable when long enough.
- **Gregory-Laflamme threshold** - the wavelength at which that instability starts.
- **Large-D (1/n) expansion** - solving in very many dimensions and correcting term by term; here D = n + 4.
- **Multiple zeta value** - a nested sum such as zeta(5,3) = sum over a > b >= 1 of a^-5 b^-3.
- **Divergent (asymptotic) series** - a list whose partial sums first improve, then run away.
- **Pade approximant** - a fraction of two polynomials chosen to match a series; it can make sense where the plain sum
  does not.
- **AdS black brane / holography** - a black hole with a flat (planar) horizon in anti-de Sitter space, used as a model
  of a hot plasma.
- **Screening mass** - how quickly the plasma damps a static disturbance with distance.
- **Sealed test / blind seat** - predictions hashed before the answer exists; the answer computed by a separate seat that
  cannot see them.
- **Zeta value** - zeta(s) = 1 + 1/2^s + 1/3^s + ...; for example zeta(3) = 1 + 1/8 + 1/27 + ...
- **Fresh point** - a dimension d the predictor was never tuned on.

## How to cite

```
Moki & Julio (2026). The Gregory-Laflamme threshold to order 1/n^12 and its resummation to AdS screening masses. Version 1.0. Zenodo. https://doi.org/10.5281/zenodo.23940227
```

The DOI always resolves to the newest archived version. Version 1.0 is 10.5281/zenodo.23940228. Machine-readable: [CITATION.cff](CITATION.cff).
Text and data: CC BY 4.0 (`LICENSE`). Code in `code/`: MIT (`LICENSE-CODE`).

## Related projects

- [airy-edge-hydrodynamics](https://github.com/Hashirama1337s/airy-edge-hydrodynamics): where the fluid series of a holographic plasma stops working, followed to large dimension
- [certified-chen-lebrun-weber](https://github.com/Hashirama1337s/certified-chen-lebrun-weber): a certified computed approximation of the Chen-LeBrun-Weber Einstein metric
- All projects: [the Moki & Julio lab map](https://github.com/Hashirama1337s)

---

*Prepared with AI assistance; what was checked, and by what, is stated above.*
