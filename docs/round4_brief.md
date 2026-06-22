# Round-4 Brief — to GPT-5.5-Pro (close DA/PC via itinerary admissibility)

> **Orchestrator metadata (do NOT send).** Round 4. Your Round-3 reply was independently re-verified
> (numeric + line-by-line analytic): Prop 1 (`r/δ`), the affine-projection dynamics + energy/telescoping/
> Bessel identities, and the obstruction (P6 does not transfer to projected images) are ALL confirmed; the
> P6/Friedrichs-angle attack is dead (frozen as refuted route N3). Our own simulation of the dual process
> shows `sup_j‖p_j‖` stays **bounded and flat in trajectory length N** (~`r/δ`) — i.e. the lemma's
> conclusion appears TRUE; only the proof is missing. This brief ships that and points squarely at the one
> avenue the obstruction leaves open. 🔴 Internal note: this is the **last GPT-Pro round before we escalate
> to a fresh-context attacker** (the natural attack stalled). Archive reply → `docs/round4_response.md`;
> then independent audits (3 if closure claimed).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

Round 4. Your Round-3 analysis was independently verified and is correct: `R_loc=r/δ`, the exact affine
dual dynamics, and the obstruction (the Friedrichs-angle idea fails because P6 controls the original flats
`H_j`, not the dynamically projected images `R_jH_j`). That angle-transfer route is closed — please do not
revisit it. The whole problem is now ONE lemma, and we have numerical evidence its conclusion is TRUE.
**Solve it your way.** End with a definite verdict and confidence (%).

### Setting (recap)
`ℝ^d`, `E=span T`, unit `T⊆S^{d-1}`, `r=dim E`, `δ=δ_T≥1/poly(d)`. Greedy scaled model; goal `(★)`:
`G(T)≤poly(d,1/δ)`. Reduction (verified): `G(T) ≤ 2·sup_j‖p_j‖` for the dual process below.

### Frozen, verified substrate — use freely
- **P1** `σ_min(B)≥δ/√|B|` (independent `B⊆T`).  **P3′** `T` has `≤2πr⁴/δ` distinct directions.
- **P6** `sinθ(H,K)≥δ/r` for `T`-spanned flats `H,K`. *(Caveat from R3: this does NOT extend to projected
  images `R_jH_j` — those are not `T`-spanned and their angles can collapse to ~0. Do not use P6 on them.)*
- **P7** every realizable chamber `C_s` (`v_i=s_i t_i`, `P_s={p:⟨v_i,p⟩≥1}`) has `min_{p∈P_s}‖p‖ ≤ r/δ`.
- **P8 (exact dual dynamics).** `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)=P_{H_j^⊥}p_j+q_j`, where `H_j`=span of the
  active-face normals (signed members of `T`), `q_j∈H_j` the min-norm point of the active affine hull,
  `‖q_j‖≤r/δ`. Energy `‖p_{j+1}‖²−‖p_j‖²=‖q_j‖²−‖P_{H_j}p_j‖²`. Unrolling: `p_N=Q_N p_0+Σ_j R_j q_j`
  (`Q_N=P_{H_N^⊥}⋯P_{H_1^⊥}`, `R_j=P_{H_N^⊥}⋯P_{H_{j+1}^⊥}`). Telescoping+Bessel give
  `‖Σ_j R_j q_j‖ ≤ (r/δ)√N` — the `√N` is the ceiling of the pure energy method.

### Refuted — do NOT attempt
- **N1** fixed-rank multiplicative amplifier.  **N2** one fixed dual certificate per ORIGINAL chamber (rank-3
  obstruction; the field must carry history).  **N3** the P6/Friedrichs-angle charging of dual-drift
  reorientations (P6 does not transfer to `R_jH_j`).

### THE LEMMA (prove ⟹ `(★)` closed; reduction verified)
> **Bounded dual-drift ⟺ DA ⟺ PC.** Along any reversed orthogonal-projection trajectory
> (`x_j=x_{j-1}+α_j t_j`, `⟨x_{j-1},t_j⟩=0`, split at arrangement walls so each piece lies in a chamber
> `C_{s_j}`), with `p_1∈P_{s_1}`, `‖p_1‖≤r/δ` and `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)`:
> **(DA)** `sup_N ‖Σ_{j} R_j q_j‖ ≤ poly(r,1/δ)`,  equivalently
> **(PC)** the circulation `C(Γ)=Σ_{pieces} ∫ ρ\,d⟨a_s,u⟩ ≤ poly(r,1/δ)·‖y_0‖`
> (with the uniform feasible field `q_s(x)=a_s+(r/δ−⟨a_s,u⟩)u`, `‖q_s‖≤√2·r/δ`, `⟨q_s,x⟩=(r/δ)‖x‖`).
> Then `G(T) ≤ 2(r/δ + poly)`.

**Numerical evidence (ours):** simulating the dual process along adversarial reversed-projection itineraries,
`sup_j‖p_j‖` stays bounded and essentially FLAT in `N` (e.g. ~4 for r=3, ~13 for r=4, up to N=90), tracking
`r/δ` — NOT `√N`. So the cancellation DA/PC needs really does occur on admissible itineraries; the lemma's
conclusion looks true. The task is to PROVE the `N`-independent bound.

### The one open avenue (the obstruction leaves exactly this) — suggestion, not a constraint
The `(H_j,q_j)` are NOT an arbitrary word: they come from a reversed projection trajectory, so successive
active faces are **coupled through the shared trajectory point** `x_j` (and `ρ=‖x_j‖` is monotone along the
trajectory). Promising directions:
1. **Radial-budget Lyapunov.** `‖p_j‖` is non-increasing on any maximal sub-run with a fixed active face
   (energy identity with `q_j` fixed); norm can only grow at face REORIENTATIONS. Show each reorientation
   consumes a quantum of the monotone radial budget `(r/δ)‖y_0‖` (which PC already controls), so only
   `poly` reorientations contribute — a potential `Φ_j=‖p_j‖²+`(trajectory-coupling correction) that
   telescopes.
2. **Bound the circulation `C(Γ)` directly** by choosing `a_s` history-dependently so that `d⟨a_s,u⟩` has a
   definite sign / is summable against the monotone `ρ`.
3. **Use the admissibility relation** (consecutive faces share `x_j`, with `⟨x_j,·⟩` constraints) to get the
   cross-term cancellation in Bessel `(8)` that turns `(r/δ)√N` into `poly` — replacing the discarded
   `(Σ‖q_j‖²)^{1/2}` factor by something `N`-independent.
None of these uses angle-transfer to projected images (N3).

### What we need back
1. A proof of **DA/PC** (hence `(★)`, `G(T)≤poly(r,1/δ)`) with explicit degree — OR a precise break-point —
   OR a refutation: a constant-`δ` ADMISSIBLE itinerary (from a genuine reversed projection trajectory)
   forcing `sup_j‖p_j‖` super-polynomial. (A super-poly bound for ARBITRARY words is not enough — it must be
   realizable by a projection trajectory, per the obstruction.)
2. If partial: the exact remaining sub-lemma, cleanly stated.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

Use any method; the three directions above are suggestions. If closure needs a tool absent here and from the
literature (Meshulam / Bauschke–Tung qualitative boundedness; Güntürk–Thao BV), say so and pinpoint it.
