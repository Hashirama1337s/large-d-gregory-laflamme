# BAR-R1 - resurgence: decode the far-zone sector and reach D = 5 / 4D Euclidean Schwarzschild (sealed 2026-11-03)

## In plain words
The council found (post hoc) that the 1/D series diverges by a law from the far-zone Bessel function K_{n/2}, with a phase and
strength K ~ 0.2625. A resurgence seat will now DERIVE that sector analytically and use it, with the exact coefficients, to predict
lambda(1) = (k_GL r0)^2 at n = 1 (the 4D Euclidean Schwarzschild negative mode x 4) WITHOUT using any small-n value.

## Protocol rules (the seat must follow; scored by the lead)
- Before evaluating at n = 1 or n = 2, the seat writes resurg/PROTOCOL-R1.md (the exact resummation rule, ensemble, error bar)
  and its sha256 into resurg/PROTOCOL-R1.sha256; scripts may read lambda(1), lambda(2) only in a final scoring script run after that.
  Tuning allowed only on n >= 3 values.

## Predictions (scored from resurg/RESULT.json)
- P1 (analytic strength): the seat's DERIVED (not fitted) far-zone prefactor K lies in [0.2615, 0.2635] (council's fit 0.2625 +- 0.001).
- P2 (exponents): the derived large-order law has a = 1/2 and phase s = -1 + i pi/2 exactly (council's fitted values), or the seat
  shows why not (then FAILED with the derived values reported).
- P3 (the reach): the protocol's prediction of lambda(1) has relative error < 1e-7 versus 0.76765705009210042934400437768 AND the
  stated error bar covers the truth. Relative error in [1e-7, 1e-5): PARTIAL (reported as FAILED for P3). Worse: FAILED.
- P4: same for lambda(2) (1.6101484684250746...) with bar 1e-8.
- Descriptive: whether Tension 1 (approximants overshoot by ~6.7e-5 e^(-1.45 n)) is the far-zone sector (sign, size, n-dependence).
