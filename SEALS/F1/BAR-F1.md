# BAR-F1 - the Stokes switch: black-string series = AdS plasma screening mass (sealed 2026-11-03 before any AdS value at these d exists)

## In plain words
Two blind seats (frontier, next-boss) found that our flat-space black-string 1/n series, with the derived Bessel pole law subtracted
and added back exactly, evaluated at n = -d, reproduces the AdS_{d+1} black-brane static sound-channel screening mass at d = 3..6
(d = 4 = N = 4 SYM plasma mass gap, to ~2e-11). If the 1/D expansion really is one function with two faces - the bare sum on the AdS side,
the sum plus a Bessel completion on the flat side - it must PREDICT the AdS screening mass at dimensions nobody computed. We print those
predictions now (PRED-F1.json, predict_F1.py, fixed 9-member ensemble rule), hash, and only then let a blind seat compute the AdS values.

## Sealed predictions (m^2 in units r0 = L_AdS = 1; static sound channel, lowest mode; m^2 = -q^2)
d = 2.5 : 4.25692455371037929487439764769   bar_abs 1.05e-5
d = 3.5 : 5.0236875228429017540718944916    bar_abs 2.4e-8
d = 4.5 : 5.90695002030383197398576285136   bar_abs 3.13e-10
d = 5.5 : 6.83509228232788074482030900152   bar_abs 8.44e-12
d = 7   : 8.2663162210597664454422586253    bar_abs 8.4e-14
d = 8   : 9.23464724111336277063967797368   bar_abs 5.66e-15
d = 10  : 11.189855546568147821690403193    bar_abs 4.88e-17

## Predictions (scored by verdict_F1.py, hashed with this file)
- P1..P7: for each d above, |blind AdS m^2 - prediction| <= 3 x bar_abs. HOLDS iff all seven (requires the blind value trusted to
  better than bar_abs/10). Per-d results reported.
- P8 (headline): relative error at d = 4.5 below 1e-9 AND at d = 7 below 1e-13.
- N1 (null, flat side): the same pipeline evaluated at n = +3, +5 (lambda_pert = 0.95943667473538799589, 0.062628221420310855226)
  MISSES the true flat thresholds lambda(3) = 2.49879056118..., lambda(5) = 4.35617574792... by more than 10% (the Bessel completion).
- Positive control for the blind seat: its own d = 4 and d = 6 values match the published 2.3361 pi T (m^2 = 5.457) and 7.308.

## Not claimed even if all HOLD
A proof that the AdS side needs no completion; anything about other channels; novelty beyond the gate (GATE pending: INSPIRE citers of
1211.2815 / 1312.7874 scanned by two seats - nothing on screening/glueball/Borel).
