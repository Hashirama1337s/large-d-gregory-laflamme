# BAR-DERIV - blind analytic derivation of the 5NLO and 6NLO terms (sealed 2026-11-02 before the seat starts)

## In plain words
So far k5 and k6 are "identified": read off from 60-100-digit numbers by a guarded constant-finder, confirmed by independent
codes. That is strong evidence, not a derivation. A new seat that is NOT told our answers will now try to DERIVE the series
analytically - order by order perturbation theory of the black string's static perturbation equation at large n, with the
integrals done exactly (harmonic polylogarithms / multiple zeta values). We predict, now, that its exact output equals our
identified formulas. If it does, the formulas become derived results (pending a referee); if it does not, one side is wrong.

## Blindness
The seat may read published literature (including k0..k4 of 1502.02820 / 1802.08191, and methods papers). It may NOT read:
<lab>/NEXT-2026-11-02/zeta-k5/ outside deriv/, <lab>/NEXT-2026-11-02/gravity-frontier/, <lab>/NEXT-2026-10-30/WATCH/,
<private folder>/ (memory). It is told only that "the lab has numerical values for higher orders; derive them".

## Rules for what counts as derived
Final coefficients must come from exact symbolic integration / reduction (e.g. HPL shuffle algebra, MZV tables), not from
numerical fitting or PSLQ. Numerical checks are allowed as checks and must be reported as such.

## Predictions (scored by verdict_deriv.py, hashed with this file; FAILED is a result)
- C1 (control): the seat's derivation (not a citation) outputs k3 = 2 zeta3 - 25/16 and k4 = 363/128 - 5 zeta3.
- P1: its derived k5 equals -1335/256 + (47/4) zeta3 - 38 zeta5 exactly (checked by the scorer: the seat's closed form evaluated
  at 100 digits differs from ours by < 1e-90, AND the seat's rational/zeta coefficients match term by term).
- P2: its derived k6 equals 9923/1024 - (213/8) zeta3 + 139 zeta5 + 2 zeta3^2 - 160 zeta6 exactly (same test).
- If the seat does not reach an order: that prediction is VOID (reported with how far it got). A derived value that differs: FAILED.

## Not claimed even if all HOLD
A rigorous asymptotic theorem (remainder bounds); orders the seat did not derive; anything about k7+ unless derived.
