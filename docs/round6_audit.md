# Round-6 AUDIT — verdict + classification (rank-3 closure)

> Two independent audits of `docs/round6_response.md`, blind to each other: (1) orchestrator numeric
> (`code/round6_audit_checks.py` → `round6_audit_results.json`); (2) fresh-context analytic agent (line-by-line).
> **Bottom line: rank 3 is genuinely CLOSED (all 8 steps VALID) — freeze P12. The rank-4 obstruction is
> GENUINE (not an artifact); rank 3 does NOT template r→r+1. The crux is now the rank-4 flag-holonomy core case.**

## Classification (guide §3)

### PROGRESS — proven, freeze
- **P12 (NEW) — rank 3 CLOSED.** For `r=dim span(T)=3` and ADMISSIBLE itineraries (δ_T≤1, always true):
  `sup_j‖p_j‖ ≤ √53/δ² < 8/δ²` (degree 2 in 1/δ), hence `‖Σ_{j<N}R_j q_j‖ < 11/δ²` and `(★)` at rank 3.
  - *Proof (uses P1,P9,P11,B4,exact-J; NOT the full cocycle):* active-rank `‖q_j‖≤h/δ`; positive transition
    (P9) ⟹ `dim H_j≥2` ⟹ reset (`H_j=E`, `‖p‖≤3/δ`) or a **plane cluster** `J` (dim 2) with `p=a·e+y`,
    `a` constant (exact-J), `‖y‖≤2/δ` (P11 inside `J`); **leaving the plane DETECTS the survivor** (`|P_L e|≥δ`,
    A1) ⟹ cluster recurrence `(a')²≤a²+2C²−(ℓ(a)−C²)₊` ⟹ trapping `|a|≤7/δ²`; combine ⟹ `√53/δ²`.
  - *Analytic:* all 8 claims VALID (q-bound, reset, cluster `a`-constant + `‖y‖≤2/δ`, exit detection, recurrence
    invariant `a²≤49/δ⁴` preserved on `[0,7/δ²]`, global coverage). *Numeric:* `sup ≤ √53/δ²`, 0 violations,
    worst ratio 0.22 (loose — actual drift far smaller).
  - 🔴 **Caveats:** (i) ADMISSIBILITY is load-bearing (all-word sim hit 67.76 > √53/δ²; that's D_exp territory,
    not a refutation). (ii) δ≤1 is a standing hypothesis (true for unit vectors). (iii) **Soft spot NH5:** the
    "adjacent refinement of simultaneous/non-adjacent crossings" (oriented-matroid gallery reduction to
    adjacent P9-switches) is asserted, standard, but the least-written step — write explicitly at formalization.

### THE OBSTRUCTION — genuine, pinpoints the crux
- Rank 3 closes because `J` (2-dim) `+` any `t∉J` `= E` ⟹ the survivor `z_0∈(J+L)^⊥=0` (no place to hide).
  **At rank ≥4 this fails:** explicit `δ=1` example `J=⟨e1,e2⟩`, `L=⟨e1,e3⟩`, `z=e4` ⟹ `P_L z=0` (numerically
  confirmed; survivor in `(J+L)^⊥` has norm 1). The naive flag pays `n/δ` per promotion ⟹ rank-dependent degree
  (= D_exp's `K^{Θ(r²)}`). **So rank 3 does NOT template r→r+1; the real difficulty is the multidimensional
  survivor, first visible at rank 4.**

### THE OPEN CRUX (sharpest form) — flag-holonomy cocycle
- **`(★)` ⟺ the polynomial FLAG-HOLONOMY lemma (17):** `b_B=c_τ−Q_B c_σ` with `c_σ` indexed by the nested-flag
  cluster state, `‖c_σ‖≤C r^a δ^{-b}` (fixed degree, flag-depth-independent), reused on every revisit. A
  faithful flag-refinement of the Round-5 return-cocycle. **First unresolved (pivotal) case:** the **rank-4
  core** — every complete admissible excursion from a rank-2 `J`-cluster through rank-3 superflats `K⊃J` back
  to the same `J`-state has holonomy `b_B=(I−Q_B)c_{J,ω}`, `‖c_{J,ω}‖≤poly(1/δ)`, one common `c_{J,ω}`.
  Closing this almost certainly templates the general induction (it's where the holonomy stack first forms).

### Numeric (context, not refutation)
- Rank-4 dual-drift stays small/bounded (sup 6–24, ≪ D_exp) — empirically `(★)` holds at rank 4 too; the
  issue is purely the missing PROOF (the holonomy cancellation), not evidence of failure.

## Confidence
**~75% (held).** Rank ≤3 now closed (clean degree-2 bounds), all refutation/cocycle/rank-4 probes negative,
qualitative boundedness known. Tempered: rank 3 is a special case that does NOT prove the general mechanism;
the rank-dependent `K^{Θ(r²)}` factor is real and only conjecturally cancels (flag-holonomy unproven); N2
forces history-dependence. 🔴 Nothing frozen as "proved" beyond P11, P12, D_exp.

## NEEDS-HUMAN
NH1–NH4 (prior); **NH5** (write the simultaneous-crossing→adjacent-switch gallery refinement explicitly).

## Next
**Round 7 = the rank-4 flag-holonomy core case** (pivotal — isolates the whole difficulty). Continue the fresh
thread. If rank 4 resists a focused round, escalate to a human expert (oriented-matroid gallery / projection
cocycles) — per no-retreat, escalation not downgrade.
