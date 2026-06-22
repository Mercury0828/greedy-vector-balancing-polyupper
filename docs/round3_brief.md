# Round-3 Brief — to GPT-5.5-Pro (the bounded dual-drift lemma = close `(★)`)

> **Orchestrator metadata (do NOT send).** Round 3. Your Round-2 reply was independently re-verified
> (numeric + line-by-line analytic) — **all claims VALID**: Theorem 1 (frozen as P7), Prop 2, the rank-3
> obstruction (frozen as refuted route N2), and the dual-drift reduction. Direct projection-TV numerics
> show clean sub-linear/polynomial growth (tracking √d/δ, no exponential). The whole problem now sits on
> ONE lemma. This brief states it cleanly with the full substrate and the most promising attack; methods
> free. Archive reply → `docs/round3_response.md`; then independent audits (3 if you claim closure).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

Round 3. Your Round-2 results were independently verified and are correct; Theorem 1 and the dual-drift
reduction are frozen. The entire problem `(★)` now reduces to ONE lemma below. **Solve it your way** —
prove it, refute it, or pinpoint the exact missing ingredient. End with a definite verdict and confidence (%).

### Setting (recap)
`ℝ^d`, Euclidean norm. Finite `T ⊆ S^{d-1}`, `r = dim span(T)`. `δ := δ_T = min{dist(t,span(U)) : U⊆T,
t∈T, t∉span(U)}`, regime `δ ≥ 1/poly(d)` (e.g. constant `1/4`). Greedy in the scaled model `[-1,1]T`;
`G(T)=sup‖S_k‖`. Goal `(★)`: prove `G(T) ≤ poly(d,1/δ)` (anchor has only `(2/δ)^{d-1}` upper / `√d/δ`
lower; tightness open).

### Frozen, verified substrate — use freely
- **P1.** Independent `B⊆T` (cols): `σ_min(B) ≥ δ/√|B|`.
- **P3′ (few directions).** `T` has `≤ 2πr⁴/δ` distinct directions (circuit imbalance `κ≤1/δ` +
  column-number theorem). So only **polynomially many** projection directions `{π_t}`.
- **P6 (angle separation).** Any two flats `H,K` spanned by subsets of `T` have smallest positive principal
  angle with `sin θ(H,K) ≥ δ/r`.
- **P4 (projective-body identity, rigorous).** `K_0={0}`, `K_{n+1}=conv ∪_t (π_t K_n+[-t,t])`. Then
  `h_{K_n}(y)=max over chains Σ_j ‖y_j−y_{j-1}‖` (`y_j=π_{t_j}y_{j-1}`), and `G(T) ≤ radius(K_∞)`. So
  bounding the projection-trajectory total variation by `poly·‖y_0‖` proves `(★)`.
- **P7 (Theorem 1, your result — chamber certificate).** For one rep `t_i` per line and any realizable sign
  pattern `s` (`v_i=s_i t_i`, chamber `C_s={x:⟨v_i,x⟩≥0}`, `P_s={p:⟨v_i,p⟩≥1}`): the min-norm point
  `z_*` of `conv{v_i}` gives `p_s=z_*/‖z_*‖² ∈ P_s ∩ cone{v_i}` with `‖p_s‖ ≤ R_loc = O(r²/δ²)`.

### Refuted routes — do NOT attempt
- **N1.** A fixed-`O(1)`-rank multiplicative amplifier `R↦(1+c)R` (additive by P5, not multiplicative).
- **N2 (your rank-3 obstruction).** Assigning ONE fixed certificate per ORIGINAL chamber to form a convex
  `F` linear on those chambers — impossible already at rank 3, constant `δ` (`⟨t_i,t_j⟩=¾`): the margins
  force `−½Σw≥3`. ⇒ **any proof must refine the chamber fan, vary the gradient inside chambers, or carry
  genuine history.** (This does not refute `(★)`.)

### THE LEMMA (prove this ⟹ `(★)` closed; the reduction is already verified)

Reverse a finite projection trajectory: `x_j = x_{j-1} + α_j t_j` with `⟨x_{j-1},t_j⟩=0`; split at every
arrangement-wall crossing so each segment lies in one chamber `C_{s_j}`. Initialize `p_1 ∈ P_{s_1}` with
`‖p_1‖ ≤ R_loc` (P7) and update by metric projection
> `p_{j+1} = Proj_{P_{s_{j+1}}}(p_j)`.

Because `rec(P_s)=C_s` and `x_j∈C_{s_{j+1}}`, projection optimality gives `⟨p_j−p_{j+1},x_j⟩≤0`, and with
`⟨p_j,d_j⟩≥‖d_j‖` (`d_j=x_j−x_{j-1}`) summation by parts yields
`Σ_j‖d_j‖ ≤ ‖p_N‖‖x_N‖ + ‖p_1‖‖x_0‖`. Since projections are non-expansive, **if**

> **Bounded dual-drift lemma.** `sup_j ‖p_j‖ ≤ D = poly(r, 1/δ)`,

**then** `Σ_k ‖y_k−y_{k-1}‖ ≤ 2D‖y_0‖`, hence `G(T) ≤ 2D`, closing `(★)`.

Equivalently (static form): build an even convex positively-homogeneous `F` with `∂F(x)∩P_s≠∅` for `x∈C_s`
and `F(x) ≤ poly(r,1/δ)·‖x‖` (a bounded, cyclically-monotone selection `p(x)∈P_{sign(Aᵀx)}`). P7 gives
pointwise feasibility; the open part is doing it **globally / integrably**.

### The most promising attack (from our internal audit — use, adapt, or discard)
Bound `sup_j‖p_j‖` by a **history-dependent energy/potential** on the projection sequence that **exploits
P3′ and P6** — exactly the two facts the general bounded-variation theory (Güntürk–Thao arXiv:1901.07516,
and 2026 follow-ups arXiv:2601.07002, arXiv:2602.00544) does NOT assume, which is why it gives only a
geometry-dependent / non-polynomial constant. KKT: each step `Proj_{P_{s_{j+1}}}` lands on an active affine
face whose normals are signed members of `T`. The drift `‖p_j‖` can only increase when the projection moves
`p` along a recession direction of the new polyhedron, i.e. at a REORIENTATION of the active face. Charge
each such increase to the angle between the old and new active faces — bounded below by `δ/r` (P6) — and use
that there are only `O(r⁴/δ)` possible face normals (P3′), so the worst-case per-step factor `O(r/δ)` (which
compounds to exponential if naive) becomes an ADDITIVE polynomial total. This is a Friedrichs-angle /
contraction estimate for the "project onto polyhedra `{P_s}`" semigroup, specialized to angle-separated,
polynomially-many faces. It must be **history-dependent** (the static switch lemma is false; N2).

### What we need back
1. A proof of the **bounded dual-drift lemma** (or the equivalent bounded cyclic-monotone selector), with an
   explicit `D=poly(r,1/δ)` and its degree — hence `(★)` and `G(T)≤2D`. OR a precise break-point. OR a
   refutation (a constant-`δ` itinerary forcing `sup_j‖p_j‖` super-polynomial — which, if it corresponds to a
   realizable projection trajectory, is evidence for the exponential side).
2. If partial: the exact remaining sub-lemma, stated cleanly.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

Use any method; the energy/Friedrichs-angle attack above is a suggestion, not a constraint.
