# BAR-K8 - sealed predictions from the log structure (next-boss seat, 2026-11-02), before round 2 reports

Sealed by the lead before reading any round2/ output. Source of the predictions: nextboss/NB-K5.md (post hoc on seat B k7).

## In plain words
The next-boss seat noticed that the LOGARITHM of the series is much simpler than the series:
  log(k_GL r0 / sqrt n) = 1/2 log((n+1)/(n+2)) + 2 zeta3 / (n^2 (n+2)) + [zeta5, zeta6, ... terms from n^-5 on]
If that structure is real, the rational part and the zeta3 part of EVERY order are fixed in advance, and zeta3^2 never appears
in the log. It used this to predict two pieces of the n^-7 term, then found k7 by PSLQ - both pieces came out exactly. That was
after the fact. Now we predict the n^-8 term BEFORE anyone looks at round 2's new numbers.

## Definitions
L_j = coefficient of n^-j in log( sum_i k_i n^-i ), k0 = 1 (so L is the log of k_GL r0 / sqrt n).
Structure predictions: rational part of L_j = coefficient of n^-j in 1/2 log((n+1)/(n+2)) = (1/2)(-1)^(j+1)(1 - 2^j)/j;
zeta3 part of L_j (j >= 3) = 2 * (-2)^(j-3).
- j = 7: rational -127/14, zeta3 +32 (these were PREDICTED before PSLQ, confirmed post hoc).
- j = 8: rational 255/16 = 15.9375, zeta3 -64.

k7 (next-boss identification, POST HOC, one implementation):
k7 = -37193/2048 + (3771/64) zeta3 - (1685/4) zeta5 - 9 zeta3^2 + 880 zeta6 + 146 zeta7 + 192 zeta3 zeta4
   = 895.132117053873211867759986049731754772900287524303213719885047106476066524617
Seat B sharpened k8 (pre-seal, seatB/RESULT.json) = 7040.441351121886676844141884827666125748803801605022813358790642121349612

## Predictions (scored by verdict_k8.py, written and hashed with this file; FAILED is a result)
- P1 (k7, new data): round 2's best k7 (its own new node runs) matches the k7 formula above to relative error < 1e-60.
- P2 (k8 consistency): round 2's best k8 matches seat B's sharpened k8 to relative error < 1e-55.
- P3 (structure, rational): with k0..k7 exact (k7 from the formula), L8 computed from round 2's k8 is identified by guarded PSLQ
  on the fixed basis B8 = {1, zeta3, zeta5, zeta3^2, zeta6, zeta7, zeta3*zeta4, zeta2*zeta5, zeta8, zeta3*zeta5, zeta(5,3), zeta2*zeta3^2}
  (find digits <= 75% of trusted, holdout on the rest, perturbation null) AND its rational coefficient is exactly 255/16.
- P4 (structure, zeta3): in that relation the zeta3 coefficient is exactly -64.
- P5 (structure, no zeta3^2 in the log): in that relation the zeta3^2 coefficient is exactly 0.
- If no verified relation is found (insufficient digits or the basis is wrong): P3-P5 are VOID (not HOLDS, not FAILED), reported
  with the digit count. If a verified relation is found with different coefficients: FAILED.
- N1 (null): L8 perturbed by 10^-(find_digits - 5) relative gives no verified relation on B8.
- C1 (control for the constant): our computed zeta(5,3) satisfies the stuffle identity zeta(5,3) + zeta(3,5) + zeta(8) = zeta3*zeta5
  to < 1e-70, and zeta(5,3) = 0.0377076729848475440... to the printed digits (literature value; checked by the identity, not trusted alone).

## Not claimed even if all HOLD
A derivation (still numerical identification); anything about convergence; k8 from more than one implementation.
