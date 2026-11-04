# BAR-K5 - blind replication of the 5NLO coefficient of the large-D Gregory-Laflamme / negative-mode series

Sealed 2026-11-02 before the blind seat (seatB/) starts. [owner] picked menu item #1 ("#1 zeta formula").

## In plain words
One of our agents (seat C) computed a famous black-hole number in thousands of dimensions with 55-85 digits and read off
the next, never-published term of its series: k5 = -1335/256 + (47/4) zeta(3) - 38 zeta(5). One agent is not enough. A second
agent, who never sees seat C's code, numbers or formula, builds its own solver from the physics alone, computes the same
number at its own choice of dimensions, fits the series, and reports what it gets. We predict, now, before it runs, that it
lands on the same formula to at least 30 digits. If it doesn't, the claim is dead or wounded, and we say so.

## Object
lambda(n) = k_GL^2 r0^2: the static Gregory-Laflamme threshold of the uniform black string in D = n + 4 dimensions
= minus the static s-wave negative eigenvalue of the Lichnerowicz operator on (n+3)-dimensional Euclidean
Schwarzschild-Tangherlini (r0 = horizon radius). Series k_GL r0 = sqrt(n) sum_j k_j n^-j, lambda/n = sum_j g_j n^-j.
Published (to be confirmed by the gate seat from the sources): k0..k4 = 1, -1/2, 7/8, 2 zeta3 - 25/16, 363/128 - 5 zeta3.

Sealed reference values (closed.py, mpmath 80 dps):
- k3 = 0.841613806319188570799476323022899981529972584680997763584543   g3 = 0.808227612638377141598952646045799963059945169361995527169086
- k4 = -3.17434701579797142699869080755724995382493146170249440896136   g4 = -6.42468283791513142479685793813739988917983550808598658150726
- k5 (claim) = -30.4939298333228243471449650876077609946804860060718249939601   g5 (claim) = -56.340688489789097268392155802368197067858588527249409492686
- seat C lambda(4) = 0.767657050092100429344004377681 (30 digits)
- seat C k6 (numerical, unidentified) = -38.066385714840371975203724541647915454106839816528694409829

## Blind seat rules (in its brief, not this file)
The seat does not read: gravity-frontier/seats/*, MENU.md, WAYPOINTS.md, memory, this BAR file, closed.py. It may read published
papers. It must use a master equation formulation of its own choice that is NOT Asnin et al. 0706.1555 eq. (2.2) (seat C's),
derived or transcribed from an opened source, and its own nodes (n >= 100) and precision (>= 70 digits for lambda).
It reports: lambda(n) at d = 4 (n = 1), at n = 27 and n = 47 (d = 30, 50), its fitted g3..g8 and k3..k8 with its own error estimate.

## Predictions (scored by verdict_k5.py on seatB/RESULT.json; FAILED is a result)
- C1 (positive control, published terms): blind g3 and g4 match the sealed g3, g4 to relative error < 1e-25. FAILED otherwise
  (then the blind fit or the published transcription is wrong; P1 is then VOID, not HOLDS).
- C2 (positive control, d = 4): blind lambda(4) matches seat C's value to < 1e-25 relative AND rounds to LPPS 0.7677 (4 digits).
- P1 (main): blind k5 matches the sealed closed form to relative error < 1e-30. HOLDS iff so. 1e-30 > |rel err| >= 1e-15 = PARTIAL
  (reported as FAILED for the 30-digit claim). Worse = FAILED.
- P2: blind k6 matches seat C's k6 to relative error < 1e-25.
- P3: blind lambda at d = 30 and d = 50 match seat C's table (26.07475246167124, 46.04284561..., 16 printed digits) to 1e-14 relative.
- N1 (null, wrong constant): the formula with -37 zeta5 instead of -38 zeta5 misses blind k5 by > 1e-2 relative (sanity of scale).
- N2 (null, identification): mpmath pslq on the basis {blind k5, 1, zeta3} (no zeta5), maxcoeff 1e6, maxsteps 1e6, tol 1e-30,
  returns no relation; and on {blind k5 * (1 + 1e-25), 1, zeta3, zeta5} returns no relation with maxcoeff 1e5.

## Descriptive only
g7, g8 values and agreement with seat C; growth of |g_k|; run time and memory (memcap peak).

## What is NOT claimed even if all HOLD
Novelty (gate seat decides); an analytic derivation of k5 (numerical identification only, at 30+ digits from two independent
implementations); anything about convergence of the 1/n series.
