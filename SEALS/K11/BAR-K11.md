# BAR-K11 - sealed blind test: the analytic recursion's k11 and k12 vs numerics it has never seen (2026-11-03)

## In plain words
The derivation seat produced k3..k10 by pure algebra. The referee's next strike: push it two orders further, blind. We already
hold numerical values of the next two coefficients from round 2's 160-digit runs (seat B's solver; the derivation seat never saw
them). We print those numbers here, hash this file, and only then ask the seat to extend its recursion. If its exact k11 and k12
reproduce these digits, the derivation has predicted something it could not have tuned to.

## Sealed numerical targets (k11_numeric.py: round2/fitsub8.json g11, g12 with the derived exact k0..k10 subtracted)
k11 = -3969169.0871633842087408580221570274341207636791972664152844296   (g11 trusted ~63 digits)
k12 =  1249860.1461611625459680940754342657981433145624769458693114      (g12 trusted ~59 digits)

## Predictions (scored by verdict_k11.py, hashed with this file)
- P1: the seat's derived k11 (exact form, evaluated by the seat at >= 80 digits and re-evaluated by the lead where constants allow)
  agrees with the sealed k11 to relative error < 1e-55.
- P2: derived k12 agrees with the sealed k12 to relative error < 1e-50.
- If the seat does not reach an order: VOID. Disagreement beyond the bound: FAILED (then numerics or algebra is wrong - investigate both).
- C1 (control): its re-run reproduces its own k3..k10 unchanged.

## Not claimed
Anything beyond k12; a rigorous asymptotic theorem (far zone remains a standard matched-asymptotics assumption).
