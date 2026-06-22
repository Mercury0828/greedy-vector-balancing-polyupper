# Round-1 Brief — to GPT-5.5-Pro (crux `(★)`, HS2 primary)

> **Orchestrator metadata (do NOT send this block).** Round 1 of the external-solver attack loop.
> Solver = web GPT-5.5-Pro, owner-relayed. Freeze-FACTS / free-METHODS. P1,P2 are numerically confirmed
> (Sim 2) → "use freely"; P3 is OMITTED (no source bridge); the support-function iteration identity is NOT
> in the anchor (our reconstruction) → HS1 is fallback only, **HS2 is the designated primary route**.
> When the reply comes back, archive it verbatim/summarized to `docs/round1_response.md`, then run ≥1
> independent adversarial audit → `docs/round1_audit.md`, and update `LEDGER_polyupper.md` confidence trend.

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

You are attacking an open problem in discrepancy theory / online algorithms. **Solve it your way.** Below
is a self-contained statement, the regime, an OPTIONAL appendix of facts we have already verified
(numerically or against the source paper), and two candidate routes. Treat the appendix as context, not
instruction — reuse it, ignore it, or overturn it. Use your full strength. End with a definite verdict
and your confidence (%).

### The setting (deterministic greedy Euclidean vector balancing)

Work in `ℝ^d` with the Euclidean norm `‖·‖`. Let `T ⊆ S^{d-1}` be a **finite** set of unit vectors;
let `r = dim span(T) ≤ d`. Define the **distance property**
> `δ_T := min { dist(t, span(U)) : U ⊆ T, t ∈ T, t ∉ span(U) }`

(the minimum nonzero distance from a vector of `T` to the linear span of any subset of the others).

**Greedy algorithm, scaled model.** Vectors `v_1, v_2, …` arrive online and adversarially (with
repetition) from the scaled universe `[-1,1]T := { a·t : a ∈ [-1,1], t ∈ T }`. The algorithm maintains
`S_k = Σ_{i≤k} s_i v_i` and, at step `k`, picks a sign `s_k ∈ {+1,-1}` so that `s_k v_k` has
**non-positive** inner product with `S_{k-1}`. Define the worst-case greedy norm
> `G(T) := sup over all such arrival sequences and greedy runs of  max_k ‖S_k‖`.

**Known (Czerwiński–Dadush–Ergen–Ghosh–Lasota–Orlikowski, arXiv:2606.17991, 2026):**
- Upper bound: `G(T) ≤ (2/δ_T)^{d-1}` (their Theorem 1.2). **Exponential in `d`.**
- Lower bound: there EXISTS `T` (on `S^{2d-1}`) with `δ_T = δ` and `G(T) ≥ √d/δ` (their Lemma 1.4). This
  is the only lower bound; it is **polynomial**.
- They explicitly leave tightness open: *"We do not know if the estimate in Theorem 1.2 is tight."*

### THE TARGET — prove or refute `(★)`

> **`(★)`:** For every finite `T ⊆ S^{d-1}` with `δ_T ≥ δ` — where `δ` is a constant (e.g. `δ = 1/4`),
> or more generally `δ ≥ 1/poly(d)` — prove `G(T) ≤ poly(d, 1/δ)`.

That is: improve the upper bound from **exponential** `(2/δ_T)^{d-1}` to **polynomial** in the
constant/`1/poly(d)` `δ_T` regime — resolving the tightness question on the polynomial side. "Done" = an
explicit `poly(d, 1/δ)` bound (any degree), OR a precise statement of where it provably fails (e.g. a
constant-`δ` family with super-polynomial `G(T)` — which would be evidence the truth is exponential).

A useful **reduction** (you may use freely): for an arriving `v = a·t`, the greedy rule gives
`‖S + s v‖² = ‖S‖² + a² − 2|a|·|⟨t,S⟩|`, which as a function of `|a|∈[0,1]` is convex, hence maximized at
an endpoint. So a norm-maximizing adversary WLOG sends **full unit vectors** `t ∈ T` with `|⟨t,S⟩| < 1/2`
(the "productive" set), each step doing `‖S‖² ← ‖S‖² + 1 − 2|⟨t,S⟩|`.

---

### OPTIONAL appendix — facts we have verified (reuse / ignore / overturn)

**Substrate — use freely (each independently checked):**

- **P1.** Every linearly independent subset `B ⊆ T` (as columns) has `σ_min(B) ≥ δ_T / √r`.
  *Reason:* the dual basis vector of `b_i` in `span(B)` has norm `1/dist(b_i, span(B∖{b_i})) ≤ 1/δ_T`, so
  the pseudoinverse satisfies `‖B^+‖_F ≤ √r/δ_T`, hence `σ_min(B) = 1/‖B^+‖_2 ≥ 1/‖B^+‖_F ≥ δ_T/√r`.
  *(Numerically confirmed on adversarial `T` at `δ_T ≥ 1/4`; worst observed ratio to the bound = 1.008.)*

- **P2.** Let `N(x) := { t ∈ T : |⟨t,x⟩| < 1/2 }` (the only directions whose unit step can increase `‖x‖`).
  Then `‖x‖ > r/(2δ_T)  ⟹  span N(x) ⊊ span T` (the growth directions live in a PROPER subspace).
  *Reason:* if `span N(x) = span T`, take a basis `B ⊆ N(x)`; then `‖B^⊤ x‖ ≤ √r/2`, and since
  `x ∈ span(B)`, `‖x‖ ≤ ‖x‖/σ_min(B)·… ≤ (√r/δ_T)(√r/2) = r/(2δ_T)`, contradiction.
  *(Numerically confirmed on adversarial `T` and on actual greedy iterates: zero violations above the
  threshold.)*

- **P4 (base).** `G(T) ≤ radius(K_T)`, where `K_T` is the minimal convex **`T`-absorbing** body; the
  anchor builds a `T`-projective body satisfying `π_t(K) + [-t, t] ⊆ K` for all `t ∈ T` (`π_t` = orthogonal
  projection onto `t^⊥`) and bounds its radius by `(2/δ_T)^{d-1}`. *This `G(T) ≤ radius(K_T)` reduction is
  in the paper.* (⚠️ A support-function ITERATION identity
  `h_{K_n}(y) = max_{t}( h_{K_{n-1}}(π_t y) + |⟨y,t⟩| )` is **NOT** in the paper — it is our own
  reconstruction; use it only if you can derive it. See route HS1 below.)

- **P5 (helper, not yet independently audited).** For a fixed convex `H`-absorbing `K ⊆ B(0, R_H)`, the
  set `K + ρB₂` is again `H`-absorbing; consequently a greedy "phase" that only uses directions from a
  fixed rank-`q` subspace grows **additively**: `‖x_out‖ ≤ R_H + ‖x_in‖` with `R_H ≤ (2/δ_T)^{q-1}`.

**Refuted route — do NOT attempt:**
- **N1.** A fixed-`O(1)`-rank recursive "amplifier" that MULTIPLIES the norm (`R ↦ (1+c)R` per level,
  giving exponential growth). Refuted by P5: fixed-rank phases are **additive**, not multiplicative. Do
  not assume such an amplifier exists.

**Barriers / flags:**
- **B1 (optional).** The qualitative boundedness/convergence of products of orthogonal projections is
  known in general (e.g. products of matrices from a finite set), but only QUALITATIVELY — the open part
  is a `poly(d, 1/δ)` QUANTITATIVE bound. Route HS2 does not need this.
- **B2.** If you find a constant-`δ` family with **super-polynomial** `G(T)` (or super-poly projection
  total variation), that is evidence the truth is the EXPONENTIAL side — please report it as a
  **refutation of `(★)`**, not a failure, with the explicit construction.

**Numeric de-risk (context):** an adversarial search over `T` with `δ_T ≥ 1/4` for `d ≤ 10` found **no
super-polynomial growth** (`max ‖S_k‖ ≤ ~5.2`, far below `√d/δ` and astronomically below `(2/δ)^{d-1}`);
the search did not reach the proven `√d/δ` worst case, so this is evidence AGAINST an exponential, not a
proof of polynomial.

---

### Two candidate routes (use either, both, or neither)

- **HS2 — subspace-switch charging (we believe this is the cleaner/safer route; rests only on P1, P2).**
  Above radius `r/(2δ_T)` the growth-subspace `span N(x)` is a PROPER subspace of `span T` (P2). Intuition:
  the iterate can only grow inside a proper "active" subspace; to grow further it must SWITCH the active
  subspace, and a switch should cost a quantifiable norm drop. Prove that the number of growth-subspace
  switches — and hence `G(T)` — is `poly(d, 1/δ)`. (Define a subspace potential; show monotone/summable
  charging.) This route uses no unverified anchor machinery.

- **HS1 — projection-trajectory total variation (fallback; needs the iteration identity derived).** For
  the family of hyperplane projections `{π_t : t ∈ T}` with `δ_T ≥ δ`, prove every orthogonal-projection
  product trajectory `y_j = π_{t_j} y_{j-1}` has total variation `Σ_j ‖y_j − y_{j-1}‖ ≤ poly(d, 1/δ)·‖y_0‖`.
  If combined with a (derived) support-function iteration this bounds `G(T)`. Candidate angles: an
  energy/potential argument on `‖y_j‖²` with a `δ`-quantified contraction-or-charge per step; a spectral
  gap of the projection semigroup; combinatorial charging via P2.

### What we need back
1. The **full argument** closing `(★)` (any method) — OR a **precise break-point** (the exact step that
   fails and why), OR a **refutation** (a constant-`δ` super-poly family, per B2).
2. An explicit `poly(d, 1/δ)` bound with its degree, if you close it.
3. Your **confidence (%)** and a one-line **verdict**: closed / partial (+where) / refuted.

If `(★)` needs a technique that neither this sketch nor the standard literature provides, say so and
pinpoint exactly what is missing.
