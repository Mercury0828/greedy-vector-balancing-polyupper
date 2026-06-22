# Round-2 Brief — to GPT-5.5-Pro (close G1 or G2)

> **Orchestrator metadata (do NOT send).** Round 2. Your Round-1 reply was independently audited
> (numeric + fresh-context) — **all your claims checked out VALID**: the unit-WLOG refutation, refined P2,
> the principal-angle lemma, the support-function iteration identity, and the κ_A ≤ 1/δ_A ⇒ |T| ≤ 2πr⁴/δ_T
> revival. Those are now frozen substrate. This brief feeds them back consolidated and asks you to close
> the crux. Methods free (HS1 and HS2 both on the table; HS1's reduction is now rigorous thanks to your
> identity). Archive reply → `docs/round2_response.md`; then ≥1 independent audit (3 if you claim closure).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

This is round 2. Your round-1 analysis was independently verified and is correct; we have frozen it as
substrate below. **Solve it your way.** The problem has now reduced to one of two crisp missing theorems
(G1, G2) — close either and you close the whole problem. End with a definite verdict and confidence (%).

### Setting (recap)

`ℝ^d`, Euclidean norm. Finite `T ⊆ S^{d-1}`, `r = dim span(T) ≤ d`.
`δ_T := min { dist(t, span(U)) : U ⊆ T, t ∈ T, t ∉ span(U) }`. Greedy in the scaled model `[-1,1]T`:
arrivals `v_k ∈ {a t : a∈[-1,1], t∈T}` adversarial; greedy picks `s_k∈{±1}` with `⟨s_k v_k, S_{k-1}⟩ ≤ 0`;
`G(T) = sup_k ‖S_k‖`. Known (arXiv:2606.17991): `G(T) ≤ (2/δ_T)^{d-1}`; existence lower bound `√d/δ`;
tightness open.

> **TARGET `(★)`:** prove `G(T) ≤ poly(d, 1/δ_T)` for `δ_T ≥ δ` (`δ` constant e.g. 1/4, or `≥1/poly(d)`).
> "Done" = an explicit `poly(d,1/δ)` bound, OR a refutation (a constant-`δ` family with super-poly `G(T)`,
> which would be evidence the truth is exponential — report it as such).

⚠️ **Correction carried from round 1:** there is NO "send full unit vectors WLOG" reduction. The adversary
may use scaled, norm-neutral/decreasing **steering** moves (your `T={u,v}` example: unit-only `G=1`, scaled
`G≥4`). Any argument must allow steering moves outside the productive set `N(x)={t:|⟨t,x⟩|<1/2}`.

### Frozen substrate — verified, use freely

- **P1 (sharpened).** Independent `B⊆T` (columns) has `σ_min(B) ≥ δ_T/√|B|`.
- **P2 / P2′.** `N(x)={t∈T:|⟨t,x⟩|<1/2}`, `H(x)=span N(x)`, `q=dim H(x)`. Then `‖x‖>r/(2δ_T) ⟹ H(x)⊊span T`,
  and more precisely `‖P_{H(x)} x‖ ≤ q/(2δ_T)`.
- **P6 (principal-angle separation).** For flats `H,K` spanned by subsets of `T`, the smallest positive
  principal angle satisfies `sin θ(H,K) ≥ δ_T/r`. (Likely loose in `r`.)
- **P3′ (few directions).** `T` has at most `2πr⁴/δ_T` distinct directions (one rep per antipodal line ⇒
  unit-column matrix with `κ_A ≤ 1/δ_A ≤ 1/δ_T`; column-number theorem `n ≤ πr⁴κ_A`, arXiv:2510.20301).
  So at constant `δ`, `|T| = O(r⁴/δ_T)` — only POLYNOMIALLY many projection directions.
- **P4 (reduction, now rigorous).** Define `K_0={0}`, `K_{n+1}=conv ∪_{t∈T}(π_t K_n+[-t,t])` (`π_t` =
  projection onto `t^⊥`). Then `h_{K_{n+1}}(y)=max_t(h_{K_n}(π_t y)+|⟨y,t⟩|)`, which unrolls to
  `h_{K_n}(y) = max over chains (t_1,…,t_n) of Σ_{j} ‖y_j − y_{j-1}‖`, where `y_0=y`, `y_j=π_{t_j}y_{j-1}`.
  Since `G(T) ≤ radius(K_∞)`, **a polynomial total-variation bound (G1 below) immediately gives `(★)`.**
- **P5 (helper).** Fixed convex `H`-absorbing `K⊆B(0,R_H)` ⟹ `K+ρB₂` is `H`-absorbing ⟹ a fixed-rank-`q`
  phase grows ADDITIVELY. (Rules out a fixed-rank multiplicative amplifier — see N1.)

**Refuted route N1 (do not attempt):** a fixed-`O(1)`-rank recursive amplifier `R↦(1+c)R` (exponential) —
refuted by P5 (fixed-rank phases are additive).

### THE CRUX — close either G1 or G2

**G1 (HS1, total-variation route — reduction is rigorous via P4).**
> Prove: for products of the hyperplane projections `{π_t : t∈T}` — where there are only `O(r⁴/δ_T)`
> distinct `t` (P3′) and any two `T`-spanned flats are angle-separated with `sin θ ≥ δ_T/r` (P6) — every
> trajectory `y_j = π_{t_j} y_{j-1}` has `Σ_j ‖y_j − y_{j-1}‖ ≤ poly(r, 1/δ_T)·‖y_0‖`.

Status of the obstacle (your round-1 finding, confirmed): the general unrestricted-projection
bounded-variation results (e.g. Güntürk–Thao, arXiv:1901.07516) give only a **geometry-dependent /
non-polynomial** constant; the naive bound multiplies a per-transition factor `O(r/δ)` along a rank
recursion and is exponential in the number of steps. **A genuinely new quantitative argument is needed**,
and it should EXPLOIT the two new structural facts that the general theory does not assume: only
poly-many distinct projectors (P3′) and uniform poly angle-separation (P6). (Candidate angles: an
energy/potential `Σ‖y_j‖²`-type argument with a `δ`-quantified contraction-or-charge per step; a spectral
/ Friedrichs-angle estimate for the projector semigroup using P6; a charging scheme over the `O(r⁴/δ)`
directions. Use anything.)

**G2 (HS2, subspace-switch charging route).**
> Above radius `r/(2δ_T)` the active flat `H(x)=span N(x)` is proper (P2). Prove a **history-dependent
> summability invariant**: a potential `Φ(x, history)` that bounds the cumulative growth across changes of
> the active flat, giving `poly(r,1/δ_T)` total. 

Status of the obstacle (your round-1 finding, confirmed): the **static** switch lemma is FALSE — knowing
only `‖P_J x‖≤B` and `⟨t,x⟩=0` allows `‖P_{J+⟨t⟩}x‖=B/δ` (a `1/δ` jump). And switch-counting fails
(scaled steering allows arbitrarily small switches; trajectories can cycle). So the invariant must charge
a quantitative geometric quantity and exploit GLOBAL basis conditioning (P1/P6), not just the current flat.

### What we need back
1. A proof of **G1 or G2** (hence `(★)`), with an explicit `poly(r,1/δ_T)` bound and its degree — OR a
   precise break-point — OR a refutation (constant-`δ` super-poly family).
2. If you make partial progress: the exact remaining lemma, stated cleanly.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

You may use either route or a new one; do not feel bound to G1/G2 framing. If closure needs a technique
absent from this sketch and the standard literature, say so and pinpoint exactly what is missing.
