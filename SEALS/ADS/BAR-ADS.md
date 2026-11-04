# BAR-ADS - out-of-domain test: our Ricci-flat series predicts an AdS black-brane number (sealed 2026-11-03 before the seat starts)

## In plain words
[owner] 11-03: "find the new limit". The AdS/Ricci-flat correspondence (Caldarelli-Camps-Gouteraux-Skenderis 2012; used in
1502.02820 Sec. 4: nbar -> -nbar, k -> i k) maps our black string in D = n+4 to a black brane in AdS_{d+1} with n = -d. If it
holds beyond the orders anyone checked, our DERIVED series predicts the static (zero-frequency) sound-channel mode of the AdS
black brane at imaginary momentum - a screening mass of the dual strongly coupled plasma - in every dimension d. A blind seat
computes that AdS number from the AdS equations alone (never seeing our formulas). We predict, now, that its large-d series is ours
with n -> -d. This is a test that could fail.

## Prediction in formulas
lambda(n) = n(n+1)/(n+2) exp(L(1/n)), L = sum_{j>=3} L_j n^-j (L_1 = L_2 = 0), with (derived, deriv/RESULT.json; round2 L_exact):
L3 = 4z3; L4 = -8z3; L5 = 16z3 - 76z5; L6 = -32z3 + 240z5 - 320z6; L7 = 64z3 - 656z5 + 1600z6 + 292z7 + 384z3z4;
L8 = -128z3 + 1664z5 - 6400z6 + 4136z7 - 2304z3z4 + 13984z8 + 3840z3z5 + 640z(5,3).
Map n = -d: q*^2 = lambda(-d) = -d(d-1)/(d-2) * exp( sum_j L_j (-1/d)^j ), i.e. screening mass m^2(d) = -q*^2 (units r0 = L_AdS = 1).

## Predictions (scored by verdict_ads.py, hashed with this file)
- P0 (existence): the AdS_{d+1} Schwarzschild black brane has a static (omega = 0) normalizable sound-channel mode at imaginary
  momentum for large d, whose m^2(d) grows like d (the seat reports the lowest such mode).
- P1 (normalisation): c := lim m^2(d) (d-2)/(d(d-1)) = 1 to 1e-20 in r0 = L = 1 units. If FAILED, P2 is still scored with the
  seat's measured c divided out (declared now).
- P2 (the real test): the seat's fitted coefficients a_j of log( m^2(d) (d-2) / (c d (d-1)) ) = sum_j a_j d^-j satisfy
  a_1 = a_2 = 0 (|a| < 1e-25) and a_j = (-1)^j L_j for j = 3..6 to relative 1e-25, j = 7, 8 to relative 1e-15.
  HOLDS iff all; else FAILED (report per j).
- Descriptive: the seat's m^2 at d = 3, 4 vs any published screening masses it opens (e.g. N = 4 SYM, d = 4); how well the
  resummed series reproduces them.

## Not claimed even if all HOLD
A proof of the map at all orders; anything about non-perturbative terms.
