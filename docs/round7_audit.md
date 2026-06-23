# Round-7 AUDIT — verdict + classification (point-cocycle refuted; invariant-cylinder crux)

> Two independent audits of `docs/round7_response.md`: (1) orchestrator numeric
> (`code/round7_audit_checks.py` → `round7_audit_results.json`); (2) fresh-context analytic agent (exact
> arithmetic + sympy). **Bottom line: the refutation is CORRECT and rigorous. What died is the ORCHESTRATOR's
> own Round-7 conjecture (the point-valued holonomy) — freeze N5 — NOT a prior result. `(★)` stays genuinely
> OPEN; the example shows BOUNDED hysteresis (mild positive evidence). The crux becomes the set-valued
> invariant-cylinder theorem. This is the LAST AI attacker round on the rank-4 pivot before human escalation.**

## Classification (guide §3)

### REFUTED — the orchestrator's own conjecture (freeze)
- **N5 — the point-valued holonomy is FALSE.** The Round-7 brief conjectured `b_B=(I−Q_B)c_{J,ω}` with ONE
  common memory vector per `(J,ω)`. Refuted by an explicit constant-δ (δ_T=√(242/1875)≈0.359) rank-4
  arrangement with two admissible closed excursions A,B from the SAME combinatorial `(J,ω)` state, SAME linear
  part `Q` (projector onto `K^⊥=ℝn`), but **`b_A ≠ b_B`** (`‖b_A−b_B‖=0.515`, exact `(28+√30)/325·m`). Same `Q`
  + different `b` ⟹ no common `c_{J,ω}`; fix-lines parallel & disjoint.
  - *Numeric (exact):* all 5 unit; δ_T=√(242/1875) ✓; ranks J/K/E=2/3/4; `p_0` active face = J, `‖p_0‖=√38`;
    itineraries (2)/(3) reproduced 8/8 from `p_0`; `Q_A=Q_B`=proj onto `n` (exact 0.0); `b_A,b_B` match eq(7)
    exactly; cylinder invariant under both. *Analytic:* all VALID, sympy-confirmed.
  - 🔴 **Convention note:** the refutation REQUIRES the signed-normal face projector (RHS `+1`); with UNSIGNED
    normals one spuriously gets `b_A=b_B`. The response uses the correct (signed) convention. (KKT-multiplier
    "nonnegativity" is a sign artifact of the reversed-dual orientation — not load-bearing; the positive-slack
    condition, min 0.193, is what validates active-face = metric-projection.)
  - **Healthy outcome:** the loop self-corrected — the attacker killed a false reduction the orchestrator was
    about to chase, and replaced it with a sharper target. (Frozen as N5; P11/P12/N1–N4 untouched.)

### `(★)` NOT refuted — bounded hysteresis (mild positive)
- Both `A_A, A_B` are nonexpansive (`‖Q‖₂=1`) and keep a bounded **invariant cylinder**
  `C=(1,1,0,0)+[c_A,c_B]·m+ℝn` invariant (each maps `C` onto one boundary line; verified, excursion 0.0).
  Arbitrary A/B alternation stays in `C` ⟹ **bounded hysteresis, NOT drift** ⟹ the example does NOT refute
  `(★)`. Holonomy is "bounded but nonzero". *Mild positive evidence* `(★)` true — but it is ONE symmetric
  example with an explicit invariant cylinder, not a general construction; do not over-weight.

### THE OPEN CRUX (set-valued replacement)
- **Polynomial invariant-cylinder theorem:** for each cluster state σ (hidden survivor flat `V_σ`) a compact
  convex cross-section `C_σ⊂V_σ^⊥`, `sup‖c‖≤poly(r,1/δ)`, with `A_B(C_σ+V_σ)⊆C_τ+V_τ` for every admissible
  primitive block. Nonexpansiveness ⟹ `dist(A_B p,C_τ)≤dist(p,C_σ)`; top-rank `V_σ={0}` ⟹ `(★)`. *Faithful
  replacement (reduction, not yet proof).*
- **Rank-4 invariant-strip sublemma (the next concrete target):** for every `J⊂K` of ranks 2,3, the scalar
  affine return maps on `K∩J^⊥` induced by all composable `K`-confined excursions from one refined `J`-state
  admit a **common invariant interval of radius poly(1/δ)**. (Then strips in the 2-dim survivor plane `J^⊥`;
  `K^⊥`-directions have sine-separation ≥δ/4; full-span contraction bounds switching polynomially.)

## Stall / escalation
- **NOT a stall** (refuted a false reduction + produced the first explicit rank-4 bounded-hysteresis structure
  + handed over a sharper well-posed target). Per the auditor + pre-stated trigger: the rank-4 pivot did not
  merely resist — it was **replaced by a markedly more tractable problem** (a 1-dim invariant interval with
  explicit sine-separation), which **deserves exactly ONE more attacker round**. **Round 8 = the invariant-strip
  sublemma; if it neither builds the interval nor pins a clean obstruction → ESCALATE TO A HUMAN EXPERT**
  (oriented-matroid galleries / projection-orbit cocycles). Do not loop further. No-retreat: escalate, not downgrade.

## Confidence
**~75% → ~73%** (B-side / `(★)` true). Two-sided: bounded hysteresis is mild positive; BUT the *clean*
mechanism (zero holonomy / point cocycle) is now definitively dead, and the surviving set-valued cylinder
(poly radius surviving a multiplicative `1/sinθ` across a flag) is **exactly where an exponential blow-up
would hide if `(★)` were false**. Truth now hinges on whether bounded hysteresis is GENERIC or an artifact of
this symmetric example. Small downward nudge; auditor independently puts it ~70%. 🔴 Nothing frozen as
"proved" beyond P11, P12, D_exp.

## NEEDS-HUMAN
NH1–NH5 (prior); the deep step is now the invariant-cylinder/strip theorem (human-expert candidate if Round 8 resists).
