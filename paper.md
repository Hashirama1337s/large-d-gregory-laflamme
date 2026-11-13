# The Gregory-Laflamme threshold to order 1/n^12 and its resummation to AdS screening masses

Moki & Julio

---

## Abstract

The static Gregory-Laflamme threshold of the uniform black string, lambda(n) = (k_GL r0)^2 in D = n + 4, is derived
analytically in closed form through n^-12 within the standard large-D matched-asymptotic framework. The coefficients are
rational combinations of multiple zeta values, with zeta(5,3) from order 8 and, at order 11, an irreducible depth-three value
(weight 11 is the first weight that needs one; zeta(3,5,3) in our basis). The derived k11 and k12 reproduced numerical values
sealed before the derivation was extended, to relative 2.5e-64 and 1.9e-59. We find strong numerical evidence that the series
diverges; a large-order law fitted on coefficients through g40 predicted g41..g50 within 0.3%. Continued to n = -d by the
AdS/Ricci-flat map, the same series resums to the static sound-channel screening mass of the AdS_{d+1} black brane. With plain
Pade [25/25] the blind relative error is 1.2e-15 at the fresh point d = 6.5 and 5.8e-10 at the fresh point d = 3.25, with the
error decreasing overall from [16/16] to [25/25], not monotonically; a first, pole-subtracted test gave 2e-10 to 7e-14 at
fresh points d = 3.5-5.5. On the flat side the same Pade pipeline misses the threshold at n = 3 and 5, and no resummation
reaches D = 5 to the sealed accuracy. Any term the resummation misses on the AdS side is below 2e-11 at d = 4 (a training
point; 3e-12 at the fresh point d = 4.5), a tension with the heuristic extension to AdS of the expected non-perturbative
corrections. A sealed bridge through negative d failed. Every scored prediction was written
and hashed before its target was read, except where flagged (Appendix B); failures are reported as failures.

---

## 1. Introduction

The static Gregory-Laflamme threshold [GL93] of the uniform black string has a 1/n expansion in D = n + 4 dimensions,
published through n^-4 [EST15 eq. (4.28); ELMST18 eq. (A.1)]; the authors of [ELMST18 s.3.4] invited a 5NLO calculation. We extend it to
n^-12 in closed form and use it for one statement:

> The 1/n expansion of the black-string threshold, continued to n = -d via the AdS/Ricci-flat map, resums to the static
> sound-channel screening mass of the AdS_{d+1} black brane.

The series identity under n -> -d is classical: [EST15 s.4.2] performs the map on the 1/n series and checks it to O(n^-4).
What is new is the order reached and what the resummed series does at finite d. Screening masses can be computed directly
(our blind checks use 40-digit values), so precision alone is not the point. The point is that a series computed only from
flat-space black strings, and treated as only asymptotic, carries the AdS answer at fresh dimensions to the errors in Table 1.
It also leaves no room above 2e-11 at d = 4 for the non-perturbative corrections that a heuristic extension to AdS branes
expects [EST15 eq. (5.6)] (Section 5.4). On the flat side the same Pade pipeline misses the threshold at n = 3 and 5 (by 62% and
99%), and every sealed attempt to reach D = 5 failed (Section 4.3).

**Table 1. Headline numbers (sealed tests; relative errors).**

| Quantity | Result | Status |
|---|---|---|
| k11, k12 (derived) vs numerics sealed first | 2.5e-64, 1.9e-59 | BAR-K11, sealed (timing disclosure in Appendix B) |
| g41..g50 from a law fitted on j <= 40 | all ten within 0.3% (bar 3%; 5% at j = 44, 48) | BAR-NP P1, sealed |
| AdS screening mass, plain Pade [25/25], fresh d = 6.5 | 1.2e-15 | BAR-F2, sealed, blind |
| same, fresh d = 3.25 | 5.8e-10 | BAR-F2, sealed, blind |
| AdS screening mass, F1 ensemble, fresh d = 3.5, 4.5, 5.5 | 2.2e-10, 2.9e-12, 7.4e-14 | BAR-F1, sealed, blind |
| d = 4 control: m = 2.336079 pi T | matches [BKY07] (2.3361) | control (training point) |

Section 2 fixes notation. Section 3 gives the coefficients through n^-12 and the exactness test. Section 4 gives the
divergence evidence and the sealed large-order law. Section 5 gives the resummation to AdS screening masses. Section 6
reports the failed bridge, Section 7 the limits, Section 8 prior art. Methods, full scorecards, the closed forms of k10..k12
and supporting tables are in the appendices.

---

## 2. Setup and conventions

lambda(n) = (k_GL r0)^2, with k_GL the static Gregory-Laflamme threshold wavenumber of the uniform black string in D = n + 4
dimensions and r0 its horizon radius. The same number is -r0^2 times the static s-wave negative eigenvalue of the
Lichnerowicz operator on Euclidean Schwarzschild-Tangherlini in n + 3 dimensions [AGHKLM07 s.1]. In four dimensions this is the
Gross-Perry-Yaffe negative mode [GPY82] (value as quoted in [LPPS17 s.2, s.4 after eq. (4.1)] and [AGHKLM07 s.1]). The same
eigenvalue fixes where the non-Schwarzschild black-hole branch of Ricci-quadratic gravity crosses the Schwarzschild branch
[LPPS17]. We write k_GL r0 = sqrt(n) sum_j k_j n^-j and lambda(n)/n = sum_j g_j n^-j. Throughout, lambda is indexed by n.

Multiple zeta values (MZVs) are zeta(s1, .., sk) = sum over m1 > .. > mk >= 1 of m1^-s1 .. mk^-sk; for example
zeta(5,3) = sum_{a>b>=1} a^-5 b^-3. We write z_s = zeta(s); even single zetas are written as zeta(2m) (powers of zeta(2)
converted exactly). Coefficients are reduced to the basis of products of z2, z3, z5, z7, z9, z11, zeta(5,3), zeta(7,3) and
zeta(3,5,3) at weights up to 11, and z13, zeta(9,3), zeta(6,4,1,1), zeta(5,5,3), zeta(7,3,3) added at weights 12 and 13. The
basis is a convention: in the derivation's weight-12 reduction tables, zeta(9,3) and zeta(7,5) are not independent modulo
products, so the second weight-12 generator is taken from higher depth. Of the non-product generators, only
zeta(5,3), zeta(7,3), zeta(3,5,3) and zeta(9,3) occur through n^-12.

Under the AdS/Ricci-flat map [CCGS12; EST15 s.4.2] (n -> -n, k -> ik), the threshold corresponds to a static (omega = 0)
sound-channel mode of the AdS_{d+1} Schwarzschild black brane at imaginary momentum, i.e. a screening mass m^2(d) = -q*^2
(units r0 = L_AdS = 1), with n = -d. The boundary conditions on the two sides differ (regularity in the AdS interior
corresponds to normalisability on the Ricci-flat side) [CGS13 s.5]. In this paper d always denotes the AdS
boundary dimension.

---

## 3. The series through n^-12

### 3.1 Coefficients

The series was published to n^-4 [EST15 eq. (4.28); ELMST18 eq. (A.1)]:
k_GL r0 = sqrt(n) [1 - 1/(2n) + 7/(8n^2) + (2 zeta(3) - 25/16)/n^3 + (363/128 - 5 zeta(3))/n^4 + O(n^-5)].
The derivation (Appendix A.3) reproduces these (sealed controls C1a, C1b) and gives:

    k5 = -1335/256 + (47/4) z3 - 38 z5 = -30.49392983332282434714496508760776...
    k6 = 9923/1024 - (213/8) z3 + 139 z5 + 2 z3^2 - 160 z6 = -38.06638571484037197520372454164791...
    k7 = -37193/2048 + (3771/64) z3 - (1685/4) z5 + 880 z6 + 146 z7 - 9 z3^2 + 192 z3 z4 = 895.1321170538732118677599860497317...
    k8 = 1122995/32768 - (16419/128) z3 + (9283/8) z5 - 3740 z6 + 1995 z7 + 6992 z8 + (119/4) z3^2 - 1248 z3 z4
         + 1844 z3 z5 + 320 zeta(5,3) = 7040.441351121886676844141884827666...
    k9 = -4262699/65536 + (141275/512) z3 - (192913/64) z5 + 15030 z6 - (90473/4) z7 - 27544 z8 + (125014/3) z9
         - (689/8) z3^2 + 6312 z3 z4 - 15890 z3 z5 - 2784 zeta(5,3) + 2304 z4 z5 + 4160 z3 z6 - (124/3) z3^3
       = -498.8531941555244636599855558883431...
    k10 = -458974.7656077494566832245188108812...                                   (closed form: Appendix D)
    k11 = -3969169.0871633842087408580221570274341207636791972664...                (closed form: Appendix D)
    k12 = 1249860.1461611625459680940754342657981433145624769458...                 (closed form: Appendix D)

k10 contains zeta(5,3) and zeta(7,3). k11 contains zeta(3,5,3): weight 11 is the first weight needing an irreducible depth-3
element (zeta(3,5,3) in our basis). k12 adds zeta(9,3) and zeta(12), with a denominator 6219 = 9 x 691. The full closed forms
of k10..k12 are printed in Appendix D.

### 3.2 Evidence by order, and the exactness test (BAR-K11)

k5 was first identified numerically from seat C's data; a blind replication (seat B, different master equation) agreed with
it far beyond the sealed bar (BAR-K5 P1), and the two implementations agree with each other to about 1e-57. k6 was identified
POST HOC from both seats' data (67-79 digits). The blind derivation then reproduced k5 and k6 term by term (BAR-DERIV P1, P2,
sealed). k7, k8 and k9 had been identified from seat B's solver; the derived values equal them POST HOC to 7.6e-92, 3.2e-91
and 1.1e-109 (limited by stored strings), and seat C's original data confirm them to 55-59 digits (two implementations, POST
HOC). The derived k10 equals the earlier numerical candidate to 5.9e-61 (POST HOC). For k11 and k12 the numerical values were
printed and hashed first (BAR-K11), and only then was the derivation, blind to them, extended: relative agreement 2.5e-64
(bar 1e-55) and 1.9e-59 (bar 1e-50). The seal-file timing of BAR-K11 is disclosed in Appendix B. The wording we use is:
derived analytically in closed form through n^-12 within the standard large-D matched-asymptotic framework (referee covered
through n^-10; k11, k12 checked by sealed numerics). No remainder bounds are claimed.

### 3.3 A factorised logarithmic form

Define L by lambda(n) = n(n+1)/(n+2) exp(L), L = sum_j L_j n^-j. Then L0 = L1 = L2 = 0 and

| j | L_j |
|---|---|
| 3 | 4 z3 |
| 4 | -8 z3 |
| 5 | 16 z3 - 76 z5 |
| 6 | -32 z3 + 240 z5 - 320 z6 |
| 7 | 64 z3 - 656 z5 + 1600 z6 + 292 z7 + 384 z3 z4 |
| 8 | -128 z3 + 1664 z5 - 6400 z6 + 4136 z7 - 2304 z3 z4 + 13984 z8 + 3840 z3 z5 + 640 zeta(5,3) |
| 9 | 256 z3 - 4032 z5 + 24960 z6 - 43424 z7 + 11136 z3 z4 - 48096 z8 - 30720 z3 z5 - 5248 zeta(5,3) + (250028/3) z9 - (256/3) z3^3 + 4608 z4 z5 + 8960 z3 z6 |

L is the logarithm of lambda divided by n(n+1)/(n+2); this is the form tested on the AdS side in Section 5.1. L is not linear
in single zetas: zeta(3) zeta(5) enters at order 8 and zeta(3)^3 at order 9. Exact "towers" in the rational, zeta(3) and
zeta(5) parts, verified through order 22, are listed in Appendix E.

---

## 4. Divergence and the large-order law

### 4.1 Numerical evidence (unsealed)

g9..g40 were fitted from seat B's nodes (precision 80 digits at g9 down to 7 at g40). |g_j|^(1/j) rises from 3.3 at j = 8 to
6.8 (j = 20), 9.2 (j = 30) and 11.2 (j = 40); diagonal Pade poles in 1/n approach the origin (nearest pair 0.089 +- 0.143i at
[4/4], 0.026 +- 0.017i at [20/20]). This is strong numerical evidence that the series diverges; it is not a proof. As an
illustration of the question raised in [ELMST18 s.3.4]: at D = 6 the 4NLO partial sum is off by 2.4% and adding k5 makes it
110%.

### 4.2 Sealed large-order law (BAR-NP)

A theory seat proposed, from j <= 40, a divergence law of the form K n (e^2/(-n))^(n/2) (a non-perturbative scale of size
e^n n^(-n/2), phase e^(-i pi n/2), whose singularities control the growth of g_j) and printed g41..g50 before they existed. The
n^(-n/2) scale itself is the estimate of [EST15 eq. (5.6)]; the prefactor K n, the factor e^n, the phase and the sealed test
are new here. A
new seat computed them from 80 new 240-digit nodes (g50 to 9e-10): all ten agreed within 0.3% (bar 3%; 5% at j = 44, 48), including the sign
changes at j = 45 and 49 (P1 HOLDS). A free six-parameter fit on j = 30..50 gave exponent a = 0.5019 and Im s = 1.5716, inside
the sealed windows around 1/2 and pi/2 (P2 HOLDS; harness hashed after the result). A fixed-singularity model fails
(residuals up to 20%). These two items are the only independent evidence for the law. No null extrapolation (for example a
generic smooth fit on j <= 40) was sealed beside P1, so the 0.3% is not compared against what a lawless fit would do.

Derived strength (BAR-R1). A resurgence seat derived K = sqrt(e)/(2 pi) = 0.2624038 from the far-zone Bessel connection
coefficient Gamma(1 - n/2)/Gamma(1 + n/2), a Wronskian equal to 1, and a near-zone norm 2/e, with a = 1/2 and s = -1 + i pi/2
(P1, P2 HOLD). The perturbative function has simple poles at even n = 2N with residues R_N = (-1)^N K (2N) (e^2/2N)^N c(2N), and
g_{j+1} = sum_N R_N (2N)^j. Two cautions: the seat opened the sealed file (which shows the target window for K) before deriving
it, a self-disclosed protocol breach; and the first correction in c(m), -1/12, was measured to 8 digits by shooting, not
derived. With that measured c(m), the residue law reproduces g41..g50 to 1.3e-10..2.4e-8 relative (POST HOC). The AdS-side
results of Section 5 do not depend on K or c(m).

### 4.3 Reaching low dimension on the flat side

Borel-Pade resummation (Pade [20/20]) recovers lambda(n) to 0.8% at n = 2, 5.4e-6 at n = 5, 3.2e-10 at n = 10, 5.2e-17 at
n = 20 and 1.5e-22 at n = 30. At n = 1 (D = 5) the sealed attempts failed: the law-subtracted Borel scheme gave 1.2-8.3% (BAR-NP
P3 FAILED, bar 0.5%), and the derived-sector protocol gave lambda(1) = 0.767651149 +- 1.9e-5 (relative error 7.7e-6, bar 1e-7)
and lambda(2) to 1.75e-7 (bar 1e-8) (BAR-R1 P3, P4 FAILED, error bars covering). The real-axis Borel-Pade sum equals
lambda(n) to about 3e-9 absolute (3.2e-10 relative) at n = 10, so no missing term is seen there at that level. BAR-SB
(Section 6) later applied the law of Section 4.2 to a different object, the gap between lambda(n) and the AdS function
continued to n > 0. That sealed test failed at n = 16.4 (21%, bar 1%) and agreed to 1.2e-4 at n = 28.4.

---

## 5. Resummation to AdS screening masses

### 5.1 The map at the level of coefficients (BAR-ADS)

Under n = -d, the derived series predicts m^2(d) = d(d-1)/(d-2) exp(sum_j L_j (-1/d)^j). A blind seat computed m^2(d) from
the AdS equations alone at d = 100..5000 and fitted log(m^2 (d-2)/(c d(d-1))) = sum_j a_j d^-j. It found a1 = a2 = 0 and
a_j = (-1)^j L_j for j = 3..8, with relative deviations 6.8e-66, 4.6e-62, 6.3e-58, 7.5e-54, 1.2e-51 and 2.9e-47 (P2 HOLDS);
a8 matches the derived L8 including the 640 zeta(5,3) term, although the seat could not identify it. Disclosure: the brief
supplied the leading form d(d-1)/(d-2), so P1 (c = 1) tests only its normalisation; P2 is unaffected. Controls: d = 4 gives
m = 2.336079 pi T, matching [BKY07] Table 1 (2.3361) and [BMT00] Table 4 (m^2 = 5.457); d = 6 matches [BMT00] Table 2 (7.308).

### 5.2 Finite d, first sealed test (BAR-F1)

Predictions at seven d were printed from black-string data only (no AdS input) and hashed; a blind seat then computed the AdS
screening masses to 40 digits. Points d = 3..6 had been used to tune the pipeline (training), so the genuinely fresh points are
d = 3.5, 4.5, 5.5; d = 7, 8, 10 already sat, unseen by the predictor, in another seat's AdS grid; d = 2.5 was partly touched.

| d | status | relative error | 3 x bar (absolute) |
|---|---|---|---|
| 2.5 | partly touched | 4.6e-8 | 3.15e-5 |
| 3.5 | fresh | 2.2e-10 | 7.2e-8 |
| 4.5 | fresh | 2.9e-12 | 9.39e-10 |
| 5.5 | fresh | 7.4e-14 | 2.53e-11 |
| 7 | pre-existing, unseen | 6.4e-16 | 2.52e-13 |
| 8 | pre-existing, unseen | 3.9e-17 | 1.7e-14 |
| 10 | pre-existing, unseen | 2.9e-19 | 1.46e-16 |

All seven held, as did the headline P8 (d = 4.5 below 1e-9 and d = 7 below 1e-13). The pass lines (3 x bar) were 45-160 times looser than the
realised errors. The blind values agree with the other seat's independent grid to about 37 digits at d = 7, 8, 10. At d = 4,
a training point, the series agrees with the 5 published digits of [BKY07] and with our 40-digit AdS value to 2e-11; the
blind seat's controls were m^2(4) = 5.457265706766779891790... and m^2(6) = 7.3083483168740999013354....

The F1 predictor used an older coefficient file (g38 good to about 10 digits, g40 to about 7) when a better one existed. An
internal referee's recomputation with the accurate coefficients shows the error falling with Pade order, not monotonically (a
bump at M = 22), with no floor at the available accuracy (Appendix C; a referee recompute, not a sealed test). Two
consequences, both from that referee: the pole law (K, c(m)) is not needed, since plain diagonal Pade is within a factor of about 1-40 of
the same accuracy; and the bare series is no competitor (optimal truncation gives 1.4e-3 at d = 4). On the flat side (n = +3,
+5) the same pipeline misses the true thresholds by 62% and 99%.

### 5.3 Plain Pade at new off-grid points (BAR-F2)

Following the referee, we sealed plain [25/25] Pade predictions (no K, no c(m), no AdS input) at four new d. A blind seat
computed the AdS values to 40 digits with F1's solver, cross-checked to 59 digits by separately written code on the same
master equation; the master equation itself is therefore not independently replicated in F2. The test was scored after the F1
referee's report and has since been refereed internally.

| d | status | rel. error [25/25] | rel. error [23/23] | 3 x bar (absolute) | 3 x bar (relative) | margin |
|---|---|---|---|---|---|---|
| 2.25 | neighbouring data existed, unseen | 2.2e-7 | 5.36e-7 | 1.78e-5 | 4.3e-6 | 20x |
| 3.25 | fresh | 5.84e-10 | 2.52e-9 | 3.03e-8 | 6.3e-9 | 11x |
| 6.5 | fresh | 1.17e-15 | 4.18e-14 | 9.48e-13 | 1.2e-13 | 104x |
| 13.3 | neighbouring data existed, unseen | 2.6e-23 | 1.43e-21 | 6.3e-20 | 4.4e-21 | 170x |

P1-P4 hold, and P5 holds: at every d the [25/25] value is closer than [23/23]. P5 compares only those two orders, and its
comparator is weak: an internal referee's recompute finds [23/23] a local bump, worse than [20/20] and [22/22] at all four d.
Across orders the error decreases overall from [16/16] to [25/25], not monotonically: at d = 2.25 the recompute runs 5.5e-6,
4.1e-6, 6.4e-6, 9.7e-7, 3.8e-7, 4.5e-7, 3.6e-7, 5.4e-7, 1.2e-6, 2.2e-7 for M = 16..25, and at d = 6.5 [18/18] spikes to
3.4e-10. Our wording: the 1/n expansion of the black-string threshold, continued to n = -d via the AdS/Ricci-flat map, resums
to the static sound-channel screening mass of the AdS_{d+1} black brane, with the error decreasing overall with Pade order, not
monotonically; tested at 2.5 <= d <= 10 (F1; fresh only at 3.5, 4.5, 5.5) and at the F2 points d = 2.25-13.3, both
refereed internally.

### 5.4 Relation to [EST15 s.5]

[EST15 eqs. (5.5)-(5.6)] estimate non-perturbative corrections O((k r0/nbar)^nbar) = O(nbar^(-nbar/2)) for planar horizons,
Ricci-flat and AdS black branes alike, with nbar = d for AdS_{d+1}; this is 6.3e-2 at d = 4 and 4.6e-3 at d = 6 (the estimate
carries no prefactor; with the e^n factor of our large-order law, Section 4.2, it is 1.9 at d = 6). On the AdS side any term
that the resummation misses must be below 2e-11 at d = 4 (a training point), and below 3e-12 at the fresh point d = 4.5,
where the estimate is 4.5^-2.25 = 0.034. We describe this as a tension with the heuristic extension to AdS,
not as a contradiction: the operational statement of [EST15] concerns truncation accuracy, which the bare series obeys.

---

## 6. A sealed bridge through negative d that failed (BAR-SB)

A theory seat proposed that the continued AdS screening function has simple poles at even negative d whose residues follow
the one-instanton law of Section 4.2, and that the gap between the flat threshold and the continued AdS function is fixed by
the same law. We sealed residues at d = -12..-32 and gaps at n = 16.4 and 28.4, and a blind seat computed them by contour
integration in complex d (full table: Appendix G). P1 (signs), P2 (sizes) and P3 (gaps) FAILED: d = -12 is not a pole but a
branch point, the d = -16 residue is off by 10.4% (bar 2%), and the gap at n = 16.4 is -0.0203 against a predicted -0.0168
(21%, bar 1%). P4 (no poles at odd d = -21, -25) HOLDS. The continued function depends on the sheet: there is a branch point
near d ~ -5.14 +- 3.55i, and paths below it give a different function. One POST HOC reading survives: on the sheet reached
above that branch point, the residues at d = -2N for N = 11, 12, 14, 16 approach the one-instanton law (deviations against
the unrounded law shrinking from 5.3e-4 to 7.5e-5), and the gap at n = 28.4 matches to 1.2e-4. The d = 2 value m^2 = 4 is textbook (thermal stress-tensor correlator of
a 2D CFT) and is not claimed.

---

## 7. Limits

- No closed form carries remainder bounds: the derivation is order by order within the standard large-D matched-asymptotic
  framework, with the far zone treated as beyond all orders (an assumption, argued, not proved). The referee covered the
  derivation through n^-10; k11 and k12 rest on the derivation seat plus the sealed numerical test. MZV basis uniqueness and
  the irreducibility of zeta(5,3) are standard conjectures.
- The towers of Appendix E are exact through order 22 only; there is no all-orders proof (the system is not Fuchsian because of
  r^2 = X^(2/n)).
- Divergence of the threshold series is strong numerical evidence, not a proof. The large-order law is supported by one sealed
  prediction set (g41..g50) and one sealed exponent fit, with no sealed null extrapolation beside them; the derived strength was
  obtained with the target window visible, and its first correction is measured. No resummation tried reaches D = 5 to the
  sealed accuracy.
- The AdS resummation is tested at 2.5 <= d <= 10 (F1; fresh only at 3.5, 4.5, 5.5) and at d = 2.25-13.3 (F2), both
  refereed internally, with the error decreasing overall with Pade order, not monotonically; no proof of convergence of the
  resummation is claimed, and on the flat side the same resummation misses the threshold at n = 3 and 5. The bridge through negative d failed as sealed. The F2 target values
  come from F1's master equation, cross-checked by separately written code but not by an independent equation.
- Process: several tests carry disclosed slips (a brief that supplied a leading form, a seat that saw its target window, scorers
  or harnesses written after data, a seal file written after the result, seal files edited after sealing). Each is stated in
  Appendix B. None changed a verdict; some reduce a test's weight.

---

## 8. Prior art and credit

Credited, not claimed. The coefficients k0..k4 are due to [EST15 eq. (4.28)] and are repeated in [ELMST18 eq. (A.1)];
k0..k2 appear in [EST13 eq. (7.34)]. The earlier analytic large-dimension expansion of the negative eigenvalue was stopped at
third order [AGHKLM07 s.3] (through g2, lambda = n - 1 + 2/n in our variable). The AdS/Ricci-flat map is due to [CCGS12] and [CGS13]; the continuation n -> -n, k -> ik applied to the 1/n
series, checked to O(n^-4), is in [EST15 s.4.2]. That the 1/D expansion is only asymptotic, with a non-perturbative scale of
about n^(-n/2), is the estimate of [EST15 eq. (5.6)], repeated in [ELMST18 s.3.4] and reviewed in [EH20]. The authors of
[ELMST18 s.3.4] invited a 5NLO calculation. The d = 4 screening mass is in [BKY07] and [BMT00], d = 6 in [BMT00].

Open to our search floor. We found no published or posted work containing (a) the exact coefficients k5..k12, with zeta(5,3)
from order 8 and zeta(3,5,3) at order 11; (b) the large-order law with its prefactor and phase (the n^(-n/2) scale alone is
taken, above), or its sealed test; (c) the Pade resummation of the series, continued to n = -d, to finite-d AdS static
sound-channel screening masses. The search floor is INSPIRE citer lists to 2026-10-05 (citers of [EST15], [CCGS12], [CGS13],
[ELMST18], [AGHKLM07] and [EH20], among others; earlier also [BKY07]; no new [EST15] citer as of 2026-11-04), INSPIRE full
text and arXiv listings to 2026-10-31, and Zenodo to 2026-10-23; full-text queries for zeta(3,5,3), for zeta(5,3) or multiple zeta values together with large D or
Gregory-Laflamme, and for large D together with screening mass and Pade returned nothing relevant. Work posted after about
2026-10-31 (Zenodo: 2026-10-23) is not covered. The factorised logarithmic form and its towers, the coefficients through g50 and lambda(n = 1) to
39 digits were not searched as separate items; we make no separate novelty claim for them.

Context. The appearance of MZVs is expected from the method: harmonic polylogarithms on the letters {0, 1} evaluated at
x = 1, and the corresponding nested sums, give multiple zeta values (Euler/Zagier sums) [RV99 s.1; MUW01 s.4.1]. Zeta values
in large-D results were seen in [EST15 eqs. (4.25), (4.27), (4.28) and the series of eq. (6.3)], [GLP23] and [Ar26]. The
negative mode itself is due to Gross, Perry and Yaffe [GPY82] (value as quoted in [LPPS17 s.2] and [AGHKLM07 s.1]). Allen
showed that in a finite cavity it persists down to a critical cavity radius [Al84], as described in [Pr00 s.1] and
[GR01 s.2]; by a double analytic continuation, the unstable mode of a critical bubble corresponds to marginally stable
stationary black-string modes [SL04]; and for static perturbations in the large-n limit the Gross-Perry-Yaffe mode is the unique
unstable mode [SS16].

Neighbours on the AdS side. A recent paper, "Black hole radial geometry from a quantum spin chain" [Kh26], derives exact
screening-mass sum rules from a solvable spin chain; it treats scalar fields only and, by a full-text scan, uses no large-d
expansion, Pade resummation or graviton sound channel, so it concerns a different object. New here, to the floor above:
resummation of the 1/n series to finite-d screening masses, blind, with the error decreasing overall with Pade order, not
monotonically.

---

## 9. Data and code availability

The data and code for this paper are archived at Zenodo from release v1.0 of https://github.com/Hashirama1337s/large-d-gregory-laflamme (the DOI is listed on that page). The deposit contains:

- data/: the derivation's result file, with the exact closed forms of k3..k12 (k0..k2 are 1, -1/2, 7/8), their decimal values
  and the 100-digit MZV values used; k0..k12 and g0..g12 evaluated to 450 digits; the fitted coefficients g13..g50 used by the
  plain-Pade test (BAR-F2) and the older coefficient file used by the first finite-d test (BAR-F1); the sealed predictions and
  the blind AdS screening masses of both finite-d tests; and the convergence table of Appendix C.
- code/: the scripts that regenerate the headline numbers: evaluation of the k-series and of g0..g12 from the closed forms, the
  plain-Pade [25/25] prediction of BAR-F2, and the scorers of BAR-F1 and BAR-F2. They are copies of the lab scripts in which
  only file paths were changed (to paths relative to the deposit).
- SEALS/: for each sealed test in Appendix B, the prediction file, the scoring script, the verdict and the SHA-256 lines
  written at sealing, with a table of hashes. Where a sealed file contained a lab-machine path or a personal name, the deposited
  copy is redacted; the table then lists both the sealed hash and the hash of the deposited copy, and only the latter can be
  checked by a reader.
- REPRODUCE.md, with the commands and their expected outputs, and MANIFEST.sha256 over all files.

Node files for lambda(n), the derivation's intermediate files and the threshold and AdS solvers are not part of this deposit.

---

## Appendix A. Methods

### A.1 Seats and sealed tests

A "seat" is one separately briefed computation or derivation, with stated access restrictions (for example, barred from
another seat's code, numbers and sealed files). An internal referee is a separately briefed seat of the same lab that
re-checks a result; this is not external peer review. Each test was written as a short file with its predictions and pass bars and
hashed (SHA-256) before the data that score it were computed or read; from 3 November the scoring script was usually hashed
with it. A blind seat then computed the target from the physics specification only. HOLDS means the prediction passed its own
bar; FAILED and VOID are reported as such, without moved goalposts. Disclosures written before results were read (addenda,
amendments) are noted with each test. Where a scorer, harness or seal file was written after the data, that is stated
(Appendix B). Bars were often far looser than the realised errors, so we quote the errors themselves.

### A.2 Numerical solvers

The threshold used two independently built solvers. Seat C solved the master equation of [AGHKLM07] eq. (2.2). Seat B,
barred from seat C's code, numbers and the sealed bar, derived its own master equation from linearised Ricci-flatness of the
black string in the gauge h_zz = h_rz = 0 and solved it with exact Taylor recurrences in fixed-point integer arithmetic,
matching to the exact far-zone Bessel solution; it computed lambda(n) at 110 digits on 124 distinct n in [100, 5969]. A second
round re-used seat B's solver with a new driver at 160 digits (n up to 16000), and a later round added 80 nodes at 240 digits
(n = 300..39496). A referee wrote a third solver from [AGHKLM07] eq. (2.2). External controls: k r0 at D = 5 and 6 agrees with
Kalisch's values [Ka18] to 7e-15 and 1.9e-14, inside their stated errors.

The AdS side used two blind solvers: one (BAR-ADS) derived the AdS master equation by its own warped-product reduction and
computed m^2(d) at 95 digits on 48 nodes d = 100..5000 for the large-d series; the other (BAR-F1, BAR-F2) solved its own master
equation for A = h_tt/(r^2 f) at finite non-integer d with boundary series in z^2 and z^d, at 45/65 digits and two matching
points, cross-checked at d = 6 against the equation of [BMT00] to 42 digits. In F2, the same solver was cross-checked to 59
digits by separately written code (different algorithm) on the same master equation.

### A.3 Analytic derivation

A separate seat, blind to all lab numbers, derived the threshold series from its own linearised Einstein equations (gauge:
sphere radius and g_zz unperturbed), written as a first-order 3x3 system whose only singular points are 0, 1 and infinity in
X = r^n. It expanded in 1/n in y = 1 - r^-n, integrated with harmonic polylogarithms on letters {0, 1}, and reduced the
resulting MZVs with its own double-shuffle tables (weights to 11; weights 12-13 by exact row reduction, dimensions 12 and 16),
without fitting or integer-relation searches. The horizon condition is regularity; the far zone is treated as beyond all
orders, which is the standard matched-asymptotic assumption of the large-D framework [EST15 s.5]. A referee checked the
linearised system, the boundary conditions and the MZV reduction, and a rerun from a clean copy reproduced k3..k10 to 4e-56. An
independent numerical check on Kol's optimal-gauge equation at 75 digits (n = 100..3200) shows the residual after k12 falling as
n^-12.5.

### A.4 Guarded identification

Before the derivation existed, coefficients were identified numerically by the PSLQ integer-relation algorithm with three
guards: find on at most about 75% of the trusted digits, hold on every remaining digit, and return no relation when the input
is perturbed above the tolerance. Bases were written in zeta values rather than powers of pi. The double zeta value
zeta(5,3) = 0.0377076729848475440113... was checked against the stuffle identity to 2e-131.

### A.5 Resummation

Large-order coefficients g13..g50 were extracted by least-squares fits in 1/n after subtracting the exact lower orders. The
headline AdS result uses plain diagonal Pade approximants of lambda(n)/n in 1/n, evaluated at n = -d (BAR-F2: [25/25], g0..g12
exact plus g13..g50 numerical). The first sealed test (BAR-F1) used a pole-subtracted Borel/Pade ensemble that also needs the
derived strength K and the measured correction function c(m).

---

## Appendix B. Scorecards and disclosures

### B.1 The series and its large-order law

| Test | Prediction (short) | Verdict | Realised numbers / disclosure |
|---|---|---|---|
| BAR-K5 C1, C2 | blind g3, g4; lambda(n = 1) vs seat C | HOLD | 2.9e-78, 5.6e-75; 5.3e-31 |
| BAR-K5 P1 | blind k5 = closed form to 1e-30 | HOLDS | 1.6e-71 (fit vs formula; implementations agree ~1e-57) |
| BAR-K5 P2, P3 | blind k6 vs seat C; lambda(n = 27), lambda(n = 47) | HOLD | 9.0e-61; 7.4e-17, 8.1e-17 (n = 47 comparator unsealed) |
| BAR-K5 N1, N2 | -37 zeta(5) variant misses; no relation without zeta(5) | HOLD | misses by 0.034; none |
| BAR-K8 C1, P1, P2, N1 | stuffle; k7 formula on new 160-digit data; k8 vs seat B | HOLD | 2.3e-131; 7.6e-92; 1.9e-74 |
| BAR-K8 P3-P5 | order-8 log structure on a 12-element basis | VOID | 84 trusted digits too few; spurious relation rejected |
| BAR-DERIV C1a, C1b, P1, P2 | derivation reproduces k3, k4; equals identified k5, k6 | HOLD | term by term, difference 0 |
| BAR-K11 P1, P2, C1 | derived k11, k12 vs sealed numerics | HOLD | 2.5e-64 (bar 1e-55), 1.9e-59 (bar 1e-50); seal file written after the result (below) |
| BAR-R2 P1-P4 | rational part, zeta(3), zeta(5) towers, no lone zeta(2), to order 30 | HOLD to j = 22; VOID j = 23-30 | exact rational equality |
| BAR-NP P1, P2 | g41..g50 within 3% (5% at j = 44, 48); exponents | HOLD | within 0.3%; a = 0.5019, Im s = 1.5716; no sealed null extrapolation |
| BAR-NP P3 | law-subtracted Borel: lambda(1) < 0.5%, lambda(2) < 1e-4 | FAILED | 1.2-8.3%; 3.1e-4-1.9e-3 |
| BAR-NP N1 | no-phase null | NOT EVALUABLE | pole on the integration ray |
| BAR-R1 P1, P2 | derived K in [0.2615, 0.2635]; a, s | HOLD | 0.2624038 (target window visible to the seat) |
| BAR-R1 P3, P4 | lambda(1) to 1e-7; lambda(2) to 1e-8 | FAILED | 7.7e-6; 1.75e-7 (error bars covering the true values) |

Disclosures. The BAR-K5 scorer was written after seat B's result (thresholds match the sealed text); seat B's blindness cannot
be verified from the files. Some round-2 output files existed when BAR-K8 was sealed (unread by the scorer and the predicting
seat), so P3-P5 were not pre-data in spirit; they were VOID anyway. The BAR-K11 seal-hash file was written at 00:22, after the
result; pre-registration rests on the file time of the sealed prediction file (00:15:14) and the lab log entry at 00:15, and
the derivation's order-11 to order-13 work files all postdate the prediction file. BAR-NP's P2 and P3 harnesses were hashed
after the results, and P3 changed the Pade orders and fit window beyond the sealed wording; every variant fails, so FAILED is
unambiguous. No null extrapolation was sealed beside BAR-NP P1. An earlier miss of k6 by seat C was caused by too tight a PSLQ
tolerance (1e-53 on 57-digit data), not by the pi^6 basis as first stated.

### B.2 The resummation

| Test | Prediction (short) | Verdict | Realised numbers / disclosure |
|---|---|---|---|
| BAR-ADS P0, P1 | static screening mode exists; c = 1 | HOLD | leading form supplied by the brief |
| BAR-ADS P2 | a1 = a2 = 0; a3..a8 = (-1)^j L_j | HOLDS | 6.8e-66 .. 2.9e-47 |
| BAR-F1 P1-P7 | seven d within 3 x ensemble bar | HOLD | 4.6e-8 .. 2.9e-19 (fresh: 3.5, 4.5, 5.5) |
| BAR-F1 P8 | d = 4.5 < 1e-9 and d = 7 < 1e-13 | HOLDS | 2.9e-12; 6.4e-16 |
| BAR-F1 N1 | flat side misses by > 10% | HOLDS (cannot fail; not a test) | 62%, 99% |
| BAR-SB P1, P2, P3 | residue signs, sizes; bridge gaps | FAILED | d = -12 no pole; -16 off 10%; gap 16.4 off 21% |
| BAR-SB P4 | no poles at d = -21, -25 | HOLDS | < 3e-27 |
| BAR-F2 P1-P4 | four new d within 3 x bar | HOLD | 2.2e-7 .. 2.6e-23 (fresh: 3.25, 6.5); margins 20x, 11x, 104x, 170x; refereed internally |
| BAR-F2 P5 | [25/25] beats [23/23] at every d | HOLDS | all four d; [23/23] is a local bump (worse than [20/20], [22/22]) |

Disclosures. BAR-F1 stated that no AdS value existed at its d; this was false for d = 7, 8, 10 (and partly 2.5), although the
predictor read none of them. The strength K used by F1 was derived with the target window visible, and c(m) was measured.
BAR-F2's "no AdS value at these d" was also too strong (neighbouring data existed for 2.25 and 13.3). The F2 blind seat found a
precision bug in the F1 solver that affects none of the scored values. The F2 target values come from F1's solver; the
cross-check is separately written code on the same master equation. Seal files for F1 and F2 were edited after sealing; the
pre-registration times rest on the lab log and file times.

---

## Appendix C. Pade-order convergence with the accurate coefficients (internal referee recompute)

Not a sealed test. Relative error, pole-subtracted, N0 = 3, recomputed by an internal referee; transcribed verbatim into the
lab data file.

| d | sealed coefficients, M = 20 / 25 | accurate coefficients, M = 20 / 24 / 25 | plain Pade (no pole law), M = 20 / 25 |
|---|---|---|---|
| 3.5 | 1.5e-10 / 2.3e-10 | 1.5e-10 / 1.8e-11 / 1.8e-11 | 4.2e-10 / 1.7e-10 |
| 4 | 1.5e-11 / 2.5e-11 | 1.5e-11 / 1.4e-12 / 1.4e-12 | 4.6e-11 / 1.6e-11 |
| 4.5 | 1.8e-12 / 3.3e-12 | 1.8e-12 / 1.3e-13 / 1.4e-13 | 6.0e-12 / 1.8e-12 |
| 7 | 3.2e-16 / 8.5e-16 | 3.2e-16 / 9.1e-18 / 9.4e-18 | 1.0e-15 / 2.3e-16 |
| 10 | 1.1e-19 / 4.8e-19 | 1.0e-19 / 1.2e-21 / 1.3e-21 | 7.9e-20 / 5.1e-20 |

With the sealed coefficient file the error stops improving after M = 20 (g38 good to 10 digits, g40 to 7); with the accurate
set the error keeps falling, though not monotonically (bump at M = 22).

---

## Appendix D. Closed forms of k10, k11, k12

Exact, as produced by the derivation (k_GL r0 = sqrt(n) sum_j k_j n^-j; z_s = zeta(s); MZV convention and basis as in
Section 2). Copied without change from the derivation's result files.

    k10 = 32515353/262144 - 602293/1024 z3 + 962941/128 z5 + 14795/64 z3^2 - 252895/4 z6
         + 1348523/8 z7 - 30972 z3 z4 + 211155/2 z3 z5 - 24002 z8 + 19000 zeta(5,3) + 354 z3^3
         - 43008 z4 z5 - 85600 z3 z6 - 336969 z9 - 1920 z3^2 z4 - 96476 z3 z7 - 43630 z5^2
         + 16768 z10 - 6016 zeta(7,3)
        = -458974.765607749456683224518811...

    k11 = -124509807/524288 + 20396371/16384 z3 - 9336937/512 z5 - 75599/128 z3^2 + 2420345/8 z6
          - 73732557/64 z7 + 328545/2 z3 z4 - 2711657/4 z3 z5 + 1314257 z8 - 125804 zeta(5,3)
          - 12545/6 z3^3 + 438816 z4 z5 + 958040 z3 z6 + 10717261/12 z9 + 20928 z3^2 z4 + 374350 z3 z7
          + 153127 z5^2 - 2143168 z10 + 21568 zeta(7,3) + 29108 z3^2 z5 - 420288 z4 z7 - 895040 z5 z6
          - 1496224 z3 z8 + 6016 z3 zeta(5,3) - 1676038 z11 + 7168 zeta(3,5,3)
        = -3969169.087163384208740858022157027434120763679197266415284429599016784188467784491912

    k12 = 1913642943/4194304 - 85848183/32768 z3 + 44270515/1024 z5 + 746067/512 z3^2 - 55794475/32 z6
          + 1040413741/128 z7 - 4018209/4 z3 z4 + 148061599/32 z3 z5 - 120509953/8 z8 + 1763487/2 zeta(5,3)
          + 132083/12 z3^3 - 3792480 z4 z5 - 8973020 z3 z6 + 206996285/24 z9 - 157968 z3^2 z4
          + 6736863/2 z3 z7 + 6985439/4 z5^2 + 17401168 z10 + 246320 zeta(7,3) - 245434 z3^2 z5
          + 4110432 z4 z7 + 8685920 z5 z6 + 14678832 z3 z8 - 54336 z3 zeta(5,3) - 4762849 z11
          - 79616 zeta(3,5,3) + 514/3 z3^4 + 1132480 z3^2 z6 + 855936 z3 z4 z5 - 26945860/3 z5 z7
          - 32102740/3 z3 z9 + 115200 z4 zeta(5,3) - 111443870320/6219 z12 - 3558080/9 zeta(9,3)
        =  1249860.146161162545968094075434265798143314562476945869311423796905593093419812686648

The 6219 = 9 x 691 in the z12 coefficient comes from converting z2^6 to zeta(12), since B_12 = -691/2730.

---

## Appendix E. Towers in the exact series

(The sealed test BAR-K8 used the logarithm of the k-series, k_GL r0/sqrt(n), which equals L/2 plus the rational part
(1/2) log((n+1)/(n+2)).) Four patterns were sealed for the exact series of Lam = lambda/n, with eps = 1/n: the zeta-free part is
(1+eps)/(1+2eps); the terms linear in zeta(3) sum to 4 eps^3 (1+eps)/(1+2eps)^2; the terms linear in zeta(5) sum to
-4 eps^5 (19+16 eps)(1+eps)/(1+2eps)^3; and zeta(2) never appears alone. All four hold exactly for j = 0..22 (BAR-R2); orders
23-30 were not reached (VOID). There is no all-orders proof. The analogous zeta(7) and zeta(9) towers are not rational
functions of this kind (their coefficient ratios grow roughly linearly, 7.7 to 15.4 over j = 9..21).

---

## Appendix F. The D = 5 value and the 2007 table

    lambda(n = 1) = 0.767657050092100429344004377681407663367   (39 independently confirmed digits)

The 39 digits are the agreement between the referee's solver on [AGHKLM07] eq. (2.2) and seat B's own equation and solver;
seat C confirms 30. Prior values: 0.76766 [AGHKLM07], 0.7677 [LPPS17], about 14 digits of k r0 [Ka18], and 25 digits of k r0
in a 2026 Zenodo record [Ba26] (not peer reviewed), k_c r = 0.8761604020338401651155990, which differs from our
sqrt(lambda(n = 1)) by a relative 1.84e-26 in k r0 (3.7e-26 in lambda). Also lambda(n = 27) = 26.0747524616712419186847962347564
(33 digits) and lambda(n = 47) = 46.04284561245624 (16 digits).

The 2007 negative-mode table (footnote-level). [AGHKLM07] Table 1 claims 5-6 digits; its authors noted a high-d drift. In that
table's own dimension label (the Schwarzschild-Tangherlini dimension, n + 3), against our values, the last printed digit is
wrong for every label >= 24, the 5th significant digit is wrong for labels >= 34 (30 and 32 still right to 5 digits), and there
are stray 1-2 unit errors at labels 10-20 (at label 50, i.e. n = 47: 46.0530 vs 46.04285). These comparisons rest mostly on one
lab solver; labels 30 and 50 were checked by a second, 30 by a referee.

---

## Appendix G. The bridge test in full (BAR-SB)

| item | prediction | blind value | deviation | verdict |
|---|---|---|---|---|
| residue d = -12 | -0.1741247 | not a pole (branch point) | - | FAILED point |
| residue d = -16 | -8.7487513e-3 | -7.8413055e-3 | 10.4% (bar 2%) | FAILED point |
| residue d = -22 | 3.56e-5 | 3.5539153e-5 | 1.7e-3 | within bar |
| residue d = -24 | -4.5777574e-6 | -4.5760863e-6 | 3.7e-4 | within bar |
| residue d = -28 | -5.8435724e-8 | -5.8428108e-8 | 1.3e-4 | within bar |
| residue d = -32 | -5.487887e-10 | -5.4874755e-10 | 7.5e-5 | within bar |
| gap n = 16.4 | -0.016762385 | -0.020347183 | 21% (bar 1%) | FAILED point |
| gap n = 28.4 | -9.9201511e-8 | -9.9189642e-8 | 1.2e-4 | within bar |
| odd null d = -21, -25 | no pole | residue < 3e-27 | - | P4 HOLDS |

On the sheet reached above the branch point near d ~ -5.14 +- 3.55i, the deviation at N = 11 is 5.3e-4 against the unrounded
law; for N <= 8 the structure is branch points or clusters.

---

## References

- [AGHKLM07] V. Asnin, D. Gorbonos, S. Hadar, B. Kol, M. Levi, U. Miyamoto, "High and low dimensions in the black hole negative
  mode", Class. Quantum Grav. 24 (2007) 5527, arXiv:0706.1555.
- [Al84] B. Allen, "Euclidean Schwarzschild negative mode", Phys. Rev. D 30 (1984) 1153-1157, doi:10.1103/PhysRevD.30.1153.

- [Ar26] P. Arnaudo, "Shear mode transport coefficients from multiple polylogarithms", Phys. Rev. D 113 (2026) 126011,
  arXiv:2602.06120, doi:10.1103/db8h-1slc.
- [Ba26] A. A. Baillargeon, "Reading a Gauge True: A Preregistered Calibration of the TAPv Stability Criterion on Black Holes",
  Zenodo record 23549946, v7 (2026-10-22), doi:10.5281/zenodo.23549946.
- [BKY07] D. Bak, A. Karch, L. G. Yaffe, "Debye screening in strongly coupled N=4 supersymmetric Yang-Mills plasma",
  JHEP 08 (2007) 049, arXiv:0705.0994, doi:10.1088/1126-6708/2007/08/049.
- [BMT00] R. C. Brower, S. D. Mathur, C.-I Tan, "Glueball spectrum for QCD from AdS supergravity duality", Nucl. Phys. B 587
  (2000) 249-276, arXiv:hep-th/0003115, doi:10.1016/S0550-3213(00)00435-1.
- [CCGS12] M. M. Caldarelli, J. Camps, B. Gouteraux, K. Skenderis, "AdS/Ricci-flat correspondence and the Gregory-Laflamme
  instability", Phys. Rev. D 87 (2013) 061502, arXiv:1211.2815.
- [CGS13] M. M. Caldarelli, J. Camps, B. Gouteraux, K. Skenderis, "AdS/Ricci-flat correspondence", JHEP 04 (2014) 071,
  arXiv:1312.7874, doi:10.1007/JHEP04(2014)071.
- [EH20] R. Emparan, C. P. Herzog, "Large D limit of Einstein's equations", Rev. Mod. Phys. 92 (2020) 045005,
  arXiv:2003.11394, doi:10.1103/RevModPhys.92.045005.
- [ELMST18] R. Emparan, R. Luna, M. Martinez, R. Suzuki, K. Tanabe, "Phases and stability of non-uniform black strings",
  JHEP 05 (2018) 104, arXiv:1802.08191, doi:10.1007/JHEP05(2018)104.
- [EST13] R. Emparan, R. Suzuki, K. Tanabe, "The large D limit of General Relativity", JHEP 06 (2013) 009, arXiv:1302.6382,
  doi:10.1007/JHEP06(2013)009.
- [EST15] R. Emparan, R. Suzuki, K. Tanabe, "Quasinormal modes of (Anti-)de Sitter black holes in the 1/D expansion",
  JHEP 04 (2015) 085, arXiv:1502.02820.
- [GL93] R. Gregory, R. Laflamme, "Black strings and p-branes are unstable", Phys. Rev. Lett. 70 (1993) 2837-2840,
  arXiv:hep-th/9301052, doi:10.1103/PhysRevLett.70.2837.
- [GLP23] S. Grozdanov, T. Lemut, J. F. Pedraza, "Reconstruction of the quasinormal spectrum from pole skipping", Phys. Rev. D
  108 (2023) L101901, arXiv:2308.01371, doi:10.1103/PhysRevD.108.L101901.
- [GPY82] D. J. Gross, M. J. Perry, L. G. Yaffe, "Instability of flat space at finite temperature", Phys. Rev. D 25 (1982) 330,
  doi:10.1103/PhysRevD.25.330.
- [GR01] J. P. Gregory, S. F. Ross, "Stability and the negative mode for Schwarzschild in a finite cavity", Phys. Rev. D 64 (2001)
  124006, arXiv:hep-th/0106220.
- [Ka18] M. Kalisch, "Numerical construction and critical behavior of Kaluza-Klein black holes", dissertation,
  arXiv:1802.06596, doi:10.22032/dbt.34074.
- [Kh26] B. A. Khanikati, "Black hole radial geometry from a quantum spin chain", arXiv:2610.10504 (2026).
- [LPPS17] H. Lu, A. Perkins, C. N. Pope, K. S. Stelle, "Lichnerowicz Modes and Black Hole Families in Ricci Quadratic Gravity",
  Phys. Rev. D 96 (2017) 046006, arXiv:1704.05493.
- [MUW01] S. Moch, P. Uwer, S. Weinzierl, "Nested sums, expansion of transcendental functions and multiscale multiloop
  integrals", J. Math. Phys. 43 (2002) 3363, arXiv:hep-ph/0110083, doi:10.1063/1.1471366.
- [Pr00] T. Prestidge, "Dynamic and thermodynamic stability and negative modes in Schwarzschild-anti-de Sitter", Phys. Rev. D 61
  (2000) 084002, arXiv:hep-th/9907163.
- [RV99] E. Remiddi, J. A. M. Vermaseren, "Harmonic polylogarithms", Int. J. Mod. Phys. A 15 (2000) 725, arXiv:hep-ph/9905237,
  doi:10.1142/S0217751X00000367.
- [SL04] O. Sarbach, L. Lehner, "Critical bubbles and implications for critical black strings", Phys. Rev. D 71 (2005) 026002,
  arXiv:hep-th/0407265.
- [SS16] A. Sadhu, V. Suneeta, "Nonspherically symmetric black string perturbations in the large dimension limit", Phys. Rev. D
  93 (2016) 124002, arXiv:1604.00595.
