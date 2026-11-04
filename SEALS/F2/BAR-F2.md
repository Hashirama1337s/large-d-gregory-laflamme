# BAR-F2 - plain Pade, no pole law: does the black-string series resum to the AdS screening mass at new off-grid d? (sealed 2026-11-03)
Referee's strike (REFEREE-FEAST). Predictions from PRED-F2.json / predict_F2.py: plain diagonal [25/25] Pade of lambda(n)/n
(g0..g12 exact + g13..g50 np/RESULT.json), evaluated at n = -d; NO K, NO c(m), no AdS input. No AdS value at these d exists anywhere
in the lab (d = 2.25 was evaluated once by the lead's F1 post hoc PIPELINE, not by an AdS solver).

Sealed predictions (m^2, r0 = L = 1):
d = 2.25 : 4.109486379294573852609984799096104366259   bar_abs 5.93e-6
d = 3.25 : 4.81580621784263385901407356129713661797    bar_abs 1.01e-8
d = 6.5  : 7.785729384100830426657530533626601859545   bar_abs 3.16e-13
d = 13.3 : 14.44458477988057179597637157194610235423   bar_abs 2.1e-20

Predictions (verdict_F2.py, hashed now):
- P1..P4: |blind AdS m^2 - prediction| <= 3 x bar_abs at each d (blind value must be trusted to < bar_abs/10).
- P5 (order-convergence): at every d the [25/25] value is closer to the blind value than the [23/23] value (error falls with order).
- No null that cannot fail is claimed.
