# BAR-SB - the Stokes bridge (sealed 2026-11-03 before any residue at these d or bridge gap at these n is computed)

## In plain words
Council seat G (feast) found, post hoc at two points, that the AdS black-brane static screening function continued to NEGATIVE
boundary dimension d = -n equals the black-string threshold minus the derived Bessel (far-zone) term of strength sqrt(e)/(2 pi), and
that it has poles at even negative d whose residues match the derived one-instanton residues R_N (0.57% at d = -20). If the 1/D
expansion is one resurgent function whose two faces (plasma, black hole) are joined by this Stokes term, the pole residues and the
bridge gaps at NEW points are predicted. A blind seat computes them by contour integration in complex d (adsB-type solver).

## Definitions
F_AdS(d) := m^2(d)/d (AdS static sound screening, r0 = L = 1), continued analytically in complex d; residue Res_{d=-2N} F_AdS
computed by contour integral on two radii. Bridge gap at n: G(n) := lambda_flat(n)/n - F_AdS(-n) (lambda_flat = black-string threshold).
R1 one-instanton residues: R_N = (-1)^N K m (e^2/m)^(m/2) c(m), m = 2N, K = sqrt(e)/(2 pi), c(m) = 1 - 1/(12m) + 3.40759/m^2 - 3.781/m^3.

## Sealed predictions (council G-council.md Pick 2; R1 law)
Residues of F_AdS at d = -12, -16, -22, -24, -28, -32:
 -0.1741247, -8.7487513e-3, +3.56e-5, -4.5777574e-6, -5.8435724e-8, -5.487887e-10
Bridge gaps: G(16.4) = -0.016762385, G(28.4) = -9.9201511e-8.

## Predictions (scored by the lead from SB/blind/RESULT.json)
- P1 sign pattern: every computed residue has the sign of the prediction above (pattern -(-1)^N with the predicted flip at d = -22).
- P2 size: |residue/pred - 1| < 2e-3 for N >= 12 (d <= -24) and < 2e-2 for d = -12, -16, -22; deviations shrink with N.
- P3 bridge: |G/pred - 1| < 1e-2 at n = 16.4 and < 1e-3 at n = 28.4.
- P4 odd null: |Res F_AdS| < 1e-9 at d = -21 and d = -25 (no poles at odd negative d).
- Descriptive: fitted c0, c1 from the residues (target c0 = 1 to 1e-6 -> exact Stokes strength sqrt(e)/(2 pi); c1 = -1/12 to 1e-4).
