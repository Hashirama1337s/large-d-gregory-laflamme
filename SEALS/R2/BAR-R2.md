# BAR-R2 - all-orders structure, tested at far orders (sealed 2026-11-03 before the ring-map runs)

## In plain words
Through order 12 the exact series shows three patterns: the rational part of lambda/n is exactly (n+1)/(n+2); every zeta(3)
term sums to one fraction; every zeta(5) term sums to another; and zeta(2) never appears on its own. Patterns seen on 10-12 terms
can break later ([owner] 11-03: test where it could break). The derivation engine, with simplified zeta algebra (ring maps), can now
run to order 25-30 in minutes. We predict, now, that all four patterns hold to order 30. Any miss is a FAILED and a discovery.

## Normalisation
Lam(n) = lambda/n = k_GL^2 / n = sum_j Lam_j n^-j (deriv/RESULT.json conventions), eps = 1/n.

## Predictions (scored by verdict_r2.py, hashed with this file)
- P1 rational part: the zeta-free part of Lam has coefficients exactly those of (1+eps)/(1+2eps): 1, then -(-2)^(j-1), for all j <= 30.
- P2 zeta3 tower: the coefficient of zeta3 (terms linear in zeta3, no other MZV factor) equals that of 4 eps^3 (1+eps)/(1+2eps)^2, j <= 30.
- P3 zeta5 tower: the coefficient of zeta5 (linear, no other factor) equals that of -4 eps^5 (19+16 eps)(1+eps)/(1+2eps)^3, j <= 30.
- P4 no single zeta2: the coefficient of zeta2 (linear in zeta2, no other MZV factor) is exactly 0 for all j <= 30.
- Each prediction: HOLDS iff exact rational equality for every j up to the highest order the seat reaches (>= 25 required; else
  VOID for orders not reached, reported). Any mismatch: FAILED at the first j that misses.
- Descriptive: zeta7, zeta9 towers to order 30 and any closed form found; proof sketches for P1-P4.
