# Reproducing the headline numbers

Requirements: Python 3 (tested with 3.11.9) and mpmath (tested with 1.3.0). Nothing else. Each script runs in seconds.
Run every command from the top folder of this deposit (the folder that holds paper.md); the scripts use relative paths and
fail from any other folder. Create the output folder `out` first. The two scorers also write out/verdict-F1.json and
out/verdict-F2.json.

```
mkdir out
python code/exact.py 450
python code/predict_F2.py
python code/verdict_F2.py
python code/verdict_F1.py
```

The scripts read only data/ and write only to out/.

## 1. The k-series and g0..g12 from the closed forms

`python code/exact.py 450` evaluates k0..k12 from the closed forms in data/deriv_RESULT.json (the multiple zeta values are
computed by the script itself) and forms g0..g12. Expected output:

```
control zeta(2,1)-zeta(3): 9.27e-471
control zeta(2,2,2)-pi^6/7!: -5.8e-472
zeta(5,3) vs deriv 100-digit: 3.82e-102
zeta(7,3) vs deriv 100-digit: -3.53e-103
zeta(3,5,3) vs deriv 100-digit: 1.84e-103
zeta(9,3) vs deriv 100-digit: -2.88e-103
k8 7040.441351121886676844141884827666125749 deriv: 7040.44135112188667684414188483
k10 -458974.76560774945668322451881088123808 deriv: -458974.765607749456683224518811
k11 -3969169.087163384208740858022157027434121 deriv: -3969169.087163384208740858022157027434120
k12 1249860.146161162545968094075434265798143 deriv: 1249860.1461611625459680940754342657981433
g12 = 5567003.10599882547884229812993
```

The "vs deriv 100-digit" lines compare with the 100-digit values stored in the result file, so they show that file's precision.
out/exact_g.json is byte-identical to data/exact_g.json. (With a smaller argument, for example `python code/exact.py 120`, the
two control lines read 0.0 and about -2e-141, the k and g lines are unchanged, and out/exact_g.json then holds fewer digits.)

## 2. The plain-Pade prediction (BAR-F2)

`python code/predict_F2.py` builds the [25/25] Pade approximant of lambda(n)/n from g0..g12 (data/exact_g.json) and
g13..g50 (data/np_RESULT.json) and evaluates it at n = -d. Expected output:

```
2.25 {'m2_pred': '4.109486379294573852609984799096104366259', 'bar_abs': '5.93e-6', 'bar_rel': '1.44e-6'}
3.25 {'m2_pred': '4.81580621784263385901407356129713661797', 'bar_abs': '1.01e-8', 'bar_rel': '2.1e-9'}
6.5 {'m2_pred': '7.785729384100830426657530533626601859545', 'bar_abs': '3.16e-13', 'bar_rel': '4.06e-14'}
13.3 {'m2_pred': '14.44458477988057179597637157194610235423', 'bar_abs': '2.1e-20', 'bar_rel': '1.46e-21'}
```

out/PRED-F2.json is byte-identical to data/F2_PRED.json, the sealed prediction file (SHA-256 0ad8521f9f2e11e0...; see
SEALS/HASHES.md).

## 3. Scoring BAR-F2

`python code/verdict_F2.py` scores the sealed predictions (data/F2_PRED.json) against the blind AdS values
(data/F2_blind_RESULT.json). Expected output:

```
P1 d=2.25 HOLDS rel25 2.2e-7 rel23 5.36e-7 3*bar 1.78e-5
P2 d=3.25 HOLDS rel25 5.84e-10 rel23 2.52e-9 3*bar 3.03e-8
P3 d=6.5 HOLDS rel25 1.17e-15 rel23 4.18e-14 3*bar 9.48e-13
P4 d=13.3 HOLDS rel25 2.6e-23 rel23 1.43e-21 3*bar 6.3e-20
P5 HOLDS
```

## 4. Scoring BAR-F1

`python code/verdict_F1.py` scores the sealed F1 predictions (data/F1_PRED.json) against the blind AdS values
(data/F1_blind_RESULT.json). Expected output:

```
P1 d=2.5 HOLDS  |diff| 1.97e-7  rel 4.64e-8  3*bar 3.15e-5
P2 d=3.5 HOLDS  |diff| 1.08e-9  rel 2.16e-10  3*bar 7.2e-8
P3 d=4.5 HOLDS  |diff| 1.72e-11  rel 2.92e-12  3*bar 9.39e-10
P4 d=5.5 HOLDS  |diff| 5.05e-13  rel 7.39e-14  3*bar 2.53e-11
P5 d=7 HOLDS  |diff| 5.32e-15  rel 6.43e-16  3*bar 2.52e-13
P6 d=8 HOLDS  |diff| 3.63e-16  rel 3.93e-17  3*bar 1.7e-14
P7 d=10 HOLDS  |diff| 3.22e-18  rel 2.88e-19  3*bar 1.46e-16
P8 HOLDS 2.92e-12 6.43e-16
N1 HOLDS
control m2_d4 5.45726570676677989179021030501638051744 published 5.457
control m2_d6 7.308348316874099901335470196462750329299 published 7.308
```

(N1 is the flat-side null that could not fail; the paper reports it as a fact, not a test.) The F1 predictions themselves
came from a pole-subtracted ensemble that needs the strength K and the measured correction c(m); that predictor is kept as a
sealed record in SEALS/F1/ and is not part of this reproduction.

## 5. Checking the files

```
sha256sum -c MANIFEST.sha256
```

checks every file in the deposit. SEALS/HASHES.md lists, for each sealed-test file, the hash written at sealing and the hash
of the deposited copy. The data files PRED-F1, PRED-F2, both blind result files, deriv_RESULT.json and np_RESULT.json are
verbatim and match their sealed hashes. Copies in SEALS/ marked "redacted" can be checked only against their own listed hash.

## What the scripts are

code/ holds copies of the lab's scripts in which only file paths were changed, to paths relative to this deposit:
code/exact.py (evaluation of the closed forms), code/predict_F2.py (sealed BAR-F2 predictor), code/verdict_F2.py and
code/verdict_F1.py (sealed scorers). The sealed originals, redacted only for paths, are in SEALS/F2/ and SEALS/F1/.
