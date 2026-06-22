# Round-2 AUDIT — independent verdict + classification

> Two independent audits of `docs/round2_response.md`, blind to each other:
> (1) orchestrator numeric (`code/round2_audit_checks.py` → `code/round2_audit_results.json`, seed 20260622);
> (2) fresh-context analytic agent (line-by-line by hand + literature).
> **Bottom line: ALL claims VALID. No FATAL, no counterexample to `(★)`. A NEW proven polynomial partial
> result (Theorem 1 → freeze P7) + a valid obstruction (→ freeze N2) + an exact reduction of `(★)` to ONE
> clean open lemma (bounded dual-drift). Direct TV numerics show clean polynomial growth.**

## Classification (guide §3)

### PROGRESS — proven, freeze as substrate
- **P7 (NEW, Theorem 1) — polynomial chamber certificate.** Every realizable chamber `C_s` has a margin-one
  dual certificate `p_s = z_*/‖z_*‖²` (z_* = min-norm point of `conv{v_i}`) in `cone{v_i}` with
  `‖p_s‖ ≤ R_loc = √(r(r+1))(1+(r+1)κ)/δ_T ≤ (r+2)√(r(r+1))/δ_T² = O(r²/δ_T²)`.
  - *Analytic audit:* every step VALID — (a) realizability ⟹ 0∉conv{v_i}; (b) Carathéodory k≤r+1; **(c)
    the `kκ` circuit-imbalance factor is correct** (conformal decomposition; per circuit ≤(k−1)κ; κ
    sign-flip-invariant so κ(M)=κ(A)); (d) `dist₂(λ,ker)≥1/(√k(1+kκ))`; (e) `σ_q(M_J)≥σ_min(B)≥δ/√q` via
    P1; (f) `‖z_*‖≥σ_q·dist₂`; (g) certificate construction. Order `O(r²/δ²)` confirmed (uses κ≤1/δ, δ≤1).
  - *Numeric audit:* over realizable chambers (r=2..6, δ=0.1–0.5), min-norm certificate `‖p_s‖` **always
    ≤ R_loc, 0 violations**; actual norms tiny (4–9, ≪ R_loc and ≪ r²/δ²). ✅
  - *Dependency:* P1 (frozen) + P3′ (κ≤1/δ, inherits **NH1** — one-line proof in 2510.20301 not yet
    human-eyeballed). Freeze P7 conditional on NH1.
- **P4-link (Prop 2) VALID.** `G1/(★)` ⟺ a bounded, cyclically-monotone, 0-homogeneous selection
  `p(y)∈P_{sign(Aᵀy)}` (= subgradient field of one convex `F`, `F(y)≤poly·‖y‖`). The "(5)⟹(6)" worry is
  benign (`⟨t,z+at⟩=a` is wall-independent). Local feasibility = P7; **integrability is the open core.**
- **Dual-drift reduction (§4) VALID** (the reduction; the lemma is open). `rec(P_s)=C_s` ✓; projection
  variational inequality ✓; summation-by-parts `Σ‖d_j‖ ≤ ‖p_N‖‖x_N‖+‖p_1‖‖x_0‖ ≤ 2D‖y_0‖` ✓ (projections
  non-expansive); **`⟨p_j,d_j⟩≥‖d_j‖` is load-bearing on orthogonality (10)** `⟨x_{j-1},t_j⟩=0`. So
  `sup_j‖p_j‖≤D=poly ⟹ G(T)≤2D`.

### REFUTED ROUTE — freeze
- **N2 (NEW) — rank-3 obstruction.** With `⟨t_i,t_j⟩=3/4` (δ_T=√(5/14)≈0.598, constant): NO convex `F`
  linear on the 8 ORIGINAL chambers exists (forced rep `p_s=Σw_i s_i t_i`, w≥0; odd-one-out gives
  `w_j−¾Σ_{i≠j}w_i≥1`; sum ⟹ `−½Σw≥3`, impossible).
  - *Numeric:* δ_T=0.5976=√(5/14) ✓, (G⁻¹)ᵢᵢ=2.8=14/5 ✓, margin LP **infeasible** ✓. *Analytic:* forcing
    of (8) + arithmetic VALID. **Scope (do not over-read):** kills "one fixed certificate per ORIGINAL
    chamber"; does NOT forbid refined fans, intra-chamber gradient variation, or history.

### THE OPEN CRUX — `(★)` now = ONE lemma
- **Bounded dual-drift lemma (≡ bounded cyclic-monotone selector).** `∃ D=poly(r,1/δ_T)` s.t. the
  projection sequence `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)` along any reversed projection trajectory (init
  `‖p_1‖≤R_loc`) has `sup_j‖p_j‖≤D`. ⟹ `G(T)≤2D`.

### DIRECT NUMERIC EVIDENCE for `(★)` (the right object now)
- **TV probe** (`max chain Σ‖y_j−y_{j-1}‖ = h_K(y) ≈ G(T)` by P4-upgrade): adversarial search at δ_T≥1/4
  gives TV/‖y₀‖ = **6.8, 6.8, 8.6, 8.7, 10.2, 10.0, 11.5** for d=2..8 — **log-log slope 0.39** (sub-linear
  poly), tracking `√d/δ` (≈11.3 at d=8) and astronomically below `(2/δ)^{d-1}`. **No exponential signature.**
  Unlike the retracted unit-only Sim 1, this is the CORRECT object (the projection TV that bounds G(T)),
  and the adversary now reaches the `√d/δ` scale — credible. Strong `(★)`-consistent evidence (still a
  lower-bound search, not a proof).

### MINOR / lit
- **M1.** Response §3 phrasing fine; all arithmetic exact.
- **B1 update.** Projection-BV literature confirmed to give only **geometry-dependent / non-polynomial**
  constants: Güntürk–Thao (arXiv:1901.07516) `C(V,η,γ)`; 2026 follow-ups **arXiv:2601.07002** (polyhedral
  cones; limiting counterexamples) and **arXiv:2602.00544** (affine subspaces, empty intersection;
  qualitative boundedness only). **None gives poly-in-(r,1/δ).** The poly bound is genuinely open.

## Most promising next attack (auditor's recommendation, for Round 3)
Bound `sup_j‖p_j‖` by a **history-dependent energy/potential** on `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)` that
**exploits P3′ (only `O(r⁴/δ)` distinct walls) + P6 (`sin θ ≥ δ_T/r` angle separation)** — the two facts
the general BV theory does NOT assume. Charge each norm increase to the angle between the old and new active
faces (KKT: each projection lands on an active face with signed-`T` normals; angle `≥ δ_T/r` by P6), so the
per-step worst case `O(r/δ)` (which compounds to exponential) becomes an ADDITIVE poly bound over the
`O(r⁴/δ)` possible reorientations. Equivalently a Friedrichs-angle/contraction estimate for the
projector-onto-polyhedra semigroup specialized to angle-separated, poly-many faces. Must be
history-dependent (static switch lemma is false; N2 + the `B↦B/δ` example).

## Stall check
**NOT a stall.** Round 2 produced a proven new theorem (P7), an obstruction (N2), an exact reduction, and a
concrete attack. Continue → Round 3.

## Confidence
**~67% → ~72%** (B-side / `(★)` true). Rationale: a proven polynomial *local* theorem (P7); the crux is now
ONE clean, well-posed lemma with a concrete P3′+P6-powered attack; the direct TV numerics show clean
polynomial growth tracking `√d/δ`. Tempered by: the global patching is unproven, the rank-3 obstruction +
2026 BV counterexamples show real subtlety, and TV is still a lower-bound search. 🔴 Honesty rail: not a proof.

## NEEDS-HUMAN (carry to handoff)
NH1 (eyeball κ_A≤1/δ_A proof in 2510.20301 — now also under P7); NH2 (BV constant non-poly — confirmed, so
G1 needs the new argument); P5 still needs a hand proof audit.
