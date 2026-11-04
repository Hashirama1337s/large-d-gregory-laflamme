# BAR-NP - the divergence law of the 1/D series (council Pick 1 + Pick 2), sealed 2026-11-03 before any coefficient beyond g40 exists

## In plain words
The great-minds council found (post hoc, on g16..g40) that the 1/D series diverges by one exact law: the non-perturbative piece
behaves like K n (e^2/(-n))^(n/2), i.e. e^n n^(-n/2) with phase e^(-i pi n/2), K ~ 0.2625 - the far-zone Bessel function K_{n/2}(kr)
and its continuation phase. If that is real, it PREDICTS coefficients nobody has computed: g41..g50. We print them now, hash this
file, and only then compute g41..g50 from new high-precision eigenvalue runs. This is a test where we could be wrong.

## Sealed predictions (council/glance/g12_pred.json, produced by g12_predict.py from fits on j <= 40 only)
g41 = +4.894870097e43   g42 = +2.295833674e45   g43 = +5.07800423e46   g44 = +2.839423519e47   g45 = -2.616937664e49
g46 = -1.234267323e51   g47 = -2.862308576e52   g48 = -1.624214729e53   g49 = +1.723434326e55   g50 = +8.671689731e56
(g_j = coefficients of lambda/n in powers of 1/n, same normalisation as round2/gall.json)

## Predictions (scored by verdict_np.py, hashed with this file and the council scripts)
- P1: each new g41..g50 (computed independently of the council's fit) lies within 3% of the table above (5% allowed at j = 44, 48,
  near sign changes). HOLDS iff all ten; else FAILED (reported per j). Requires each new g_j trusted to better than 1%.
- P2: a free 6-parameter fit of the same form on j = 30..50 gives exponent a in [0.495, 0.505] and Im s in [pi/2 - 0.005, pi/2 + 0.005].
- P3 (Pick 2, resummation): applying the council's law-subtracted Borel scheme (council/glance/g6_resum2.py, unchanged except for
  reading coefficients through j = 50) gives relative error in lambda(1) < 0.5% and in lambda(2) < 1e-4. FAILED if lambda(1) error > 1%.
- N1 (null for P3): the same scheme with the phase removed (Im s = 0) does NOT improve on plain Borel-Pade at n = 1, 2, 3.
- Descriptive: K vs sqrt(e)/(2 pi) = 0.262404 with the extended data (named target, not a claim).

## Inputs and independence
New coefficients from a seat that computes lambda(n) at large n with seat B's solver (seatB/gl.py) or its own, at precision high
enough for g41..g50 to < 1% (estimate before running), and extracts g_j by fitting with exact g0..g12 subtracted (deriv/RESULT.json).
That seat must not read council/ (the predictions).
