# Pade-order convergence table (internal referee recompute)

Not a sealed test. Recomputed by an internal referee (a separately briefed seat of the lab, not external peer review)
while reviewing the first finite-d test (BAR-F1), and transcribed from the referee's report with no change to any
number; only the referee's note on where the scripts ran was shortened. Key: "sealed coefficients" = data/gall.json
(the file BAR-F1 used); "np/RESULT g13..g50" = data/np_RESULT.json; "R1" = the pole law (K, c(m)). This table is
Appendix C of the paper.


- Recompute (referee scripts conv.py/conv2.py), relative error, pole-subtracted, N0 = 3:

| d | sealed coefficients, M = 20 / 25 | np/RESULT g13..g50, M = 20 / 24 / 25 | plain Pade (no R1), np coefficients, M = 20 / 25 |
|---|---|---|---|
| 3.5 | 1.5e-10 / 2.3e-10 | 1.5e-10 / 1.8e-11 / 1.8e-11 | 4.2e-10 / 1.7e-10 |
| 4 | 1.5e-11 / 2.5e-11 | 1.5e-11 / 1.4e-12 / 1.4e-12 | 4.6e-11 / 1.6e-11 |
| 4.5 | 1.8e-12 / 3.3e-12 | 1.8e-12 / 1.3e-13 / 1.4e-13 | 6.0e-12 / 1.8e-12 |
| 7 | 3.2e-16 / 8.5e-16 | 3.2e-16 / 9.1e-18 / 9.4e-18 | 1.0e-15 / 2.3e-16 |
| 10 | 1.1e-19 / 4.8e-19 | 1.0e-19 / 1.2e-21 / 1.3e-21 | 7.9e-20 / 5.1e-20 |

  With the sealed coefficient file the error stops improving after M = 20. The cause is gall.json digits (g38: 10, g40: 7), whereas np/RESULT.json has g40 to ~6e-36. With the accurate set the error keeps falling, though not monotonically (bump at M = 22). Optimal truncation of the bare series gives only 1.4e-3 at d = 4 (j = 3).
