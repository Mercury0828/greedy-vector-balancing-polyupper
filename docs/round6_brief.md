# Round-6 Brief — to GPT-5.5-Pro (continue fresh thread) — rank induction r→r+1

> **Orchestrator metadata (do NOT send).** Continue the FRESH thread from Round 5. Its results were
> independently re-verified (numeric + analytic): **rank ≤2 closure (P11)** is rigorous and numerically
> saturates `r/δ`; the **all-word bound D_exp** is correct (and uniquely avoids the dead angle route); the
> **return-cocycle reduction** is a faithful sharpening. This brief asks for the next concrete step the
> auditor flagged as most promising: a **rank induction r→r+1**, with the cocycle identity as the inductive
> step on top-rank blocks. Archive reply → `docs/round6_response.md`; independent audits (3 if closure).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

Continuing from your last analysis (rank ≤2 closed; the all-word bound `D_exp`; the return-cocycle
reduction). All three were independently verified and are correct. The goal now is to **turn rank ≤2 into a
full rank induction**. **Solve it your way.** End with a definite verdict and confidence (%).

### Recap of the state (all verified, use freely)
- Setting: `ℝ^d`, `E=span(T)`, unit `T`, `r=dim E`, `δ=δ_T≥1/poly`. Dual process along an admissible reversed
  projection itinerary: `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)=P_{H_j^⊥}p_j+q_j`, `H_j`=span of active-face normals
  (subsets of `T`), `q_j∈H_j`, `‖q_j‖≤R_0:=r/δ`. Goal `(★)`: `sup_j‖p_j‖≤poly(r,1/δ)` ⟹ `G(T)=poly`.
- **(P1)** `σ_min(B)≥δ/√|B|`; **(B3)** `T`-spanned flats have `sinθ≥δ/r`; **(P9)** a switch with no common
  active constraint has `Δ=‖p⁺‖²−‖p⁻‖²≤0`; positive `Δ` only from constraints active on both sides; **(P10)**
  all unpaid drift sits near a codim-≥2 wall cluster.
- **(P11) rank ≤2 closed:** `sup_j‖p_j‖ ≤ r/δ` (proved; numerically saturated).
- **(D_exp) all-word bound:** `sup_j‖p_j‖ ≤ 2(r/δ)·5^{r-1}·(2r/δ)^{r(r-1)}` via full-rank block contraction
  `‖Q_block‖≤β_k=1/√(1+(2r/δ)^{-2(k-1)})` (uses ONLY cumulative-original-flat→next-original-flat angles).
- **Exact-J-cluster structure (your observation):** if a sub-run uses only `H_j⊆J` and `q_j∈J` for a fixed
  `T`-spanned `J`, then `P_{J^⊥}p_j` is invariant and `P_J p_j` runs the SAME dual process inside `J` (lower
  rank). So a "pure `J`-cluster" is governed by the rank-`dim J` instance.
- **Reduction target — the return-cocycle:** decomposing the unpaid transitions into nested cluster blocks
  `B:σ→τ` with affine maps `A_B(p)=Q_B p+b_B`, the poly bound is equivalent to memory vectors `c_σ`,
  `‖c_σ‖≤poly(r,1/δ)`, with `b_B=c_τ−Q_B c_σ` (closed block: `b_B=(I−Q_B)c_σ`). Then `p_N−c_{σ_N}=
  Q_{B_N}⋯Q_{B_1}(p_0−c_{σ_0})` telescopes ⟹ `‖p_N‖≤R_0+2C`.

### THE ASK — a rank induction r→r+1 (start with r=3)
Assume the polynomial bounded-dual-drift bound holds at every rank `≤ r` (base `r=2` = P11). Prove it at rank
`r+1`. The natural program (use, adapt, or replace):
1. **Decompose** an admissible rank-`(r+1)` itinerary into (a) maximal sub-runs confined to a PROPER
   `T`-spanned flat `J` (`dim J ≤ r`) — handled by the induction hypothesis inside `J` via the exact-J-cluster
   structure — and (b) genuinely **top-rank ("full-span") blocks** that touch all of `E`.
2. For the top-rank blocks, the linear parts contract (`‖Q_B‖≤β_{r+1}<1`, from D_exp Step 2). So the ONLY way
   `‖p_j‖` can fail to be poly is if the block translations `b_B` ACCUMULATE rather than coboundary-cancel.
3. **Prove the return-cocycle identity** `b_B=c_τ−Q_B c_σ` (equivalently the closed-block `b_B=(I−Q_B)c_σ`)
   for top-rank blocks, with `‖c_σ‖≤poly` — i.e. construct the history/memory vectors `c_σ` (indexed by the
   nested-cluster entry/exit state). This is the one deep step. It MUST be history-dependent (a single fixed
   certificate per original chamber provably fails — rank-3 obstruction: at `⟨t_i,t_j⟩=¾` no convex `F`
   linear on the 8 chambers exists). The admissibility you may exploit: consecutive active faces share the
   trajectory point `x_j`; `ρ=‖x_j‖` is monotone along the trajectory; the itinerary is an ordered
   oriented-matroid gallery walk.

Equivalent sufficient target: bound the affine-synthesis sum `‖Σ_j R_j q_j‖` (`R_j=P_{H_N^⊥}⋯P_{H_{j+1}^⊥}`)
by `poly(r,1/δ)` — the `√N` Bessel ceiling must be beaten using the itinerary admissibility (NOT termwise).

### Concretely, the most valuable single deliverable
**Close rank 3** with an explicit `poly(1/δ)` bound (any degree), by proving the cocycle identity / bounding
the affine-synthesis sum for rank-3 top-span blocks. A clean rank-3 proof almost certainly templates the
general `r→r+1` step. (If rank 3 already needs a genuinely new idea, that idea is the whole theorem.)

### What we need back
1. A proof of the rank `r→r+1` step (or at least **rank 3 closed**) ⟹ `(★)`, with explicit degree — OR a
   precise break-point (the exact sub-lemma that resists) — OR a refutation (an admissible rank-3 itinerary,
   realizable by a reversed projection trajectory at constant `δ`, with super-polynomial `sup_j‖p_j‖`; note a
   repeatable closed cluster block with `‖(I−Q_B)^†b_B‖` super-poly would do it).
2. If partial: the exact remaining sub-lemma, cleanly stated.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

Use any machinery (oriented-matroid galleries, projection-orbit cocycles, arrangement induction). The
cocycle / J-cluster program above is a suggestion, not a constraint.
