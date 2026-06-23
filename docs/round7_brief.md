# Round-7 Brief — to GPT-5.5-Pro (continue fresh thread) — the PIVOTAL rank-4 flag-holonomy core

> **Orchestrator metadata (do NOT send).** Continue the FRESH thread. Round 6 (rank 3 closed; obstruction at
> rank 4) was independently re-verified (rank-3 proof 8/8 valid, numerically `sup≤√53/δ²`; the rank-4 survivor
> obstruction `P_L z=0` confirmed). This brief asks for the ONE case the audit flagged as isolating the whole
> remaining difficulty: the rank-4 closed-excursion holonomy. Closing it likely templates the general
> induction. If it resists, that pinpoints exactly what a human expert must supply. Archive → `docs/round7_response.md`;
> independent audits (3 if closure). 🔴 If this pivotal case resists a focused round, we escalate to a human expert.

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

Continuing. Your rank-3 closure (`sup_j‖p_j‖ ≤ √53/δ² < 8/δ²`) is verified and correct, and your diagnosis is
verified too: rank 3 is special (a 2-plane `J` plus any `t∉J` spans `E`, so the survivor cannot hide), and the
real difficulty — the **multidimensional survivor** hiding in `(J+L)^⊥` — first appears at rank 4. The whole
remaining theorem now sits on ONE case. **Solve it your way.** End with a definite verdict and confidence (%).

### Setting (verified substrate, use freely)
- Dual process `p_{j+1}=P_{H_j^⊥}p_j+q_j`, `H_j`=span of active-face normals (subsets of `T`), `q_j∈H_j`,
  `‖q_j‖≤h/δ` where `h=dim H_j`. `δ=δ_T≥1/poly`, `δ≤1`. Goal `(★)`: `sup_j‖p_j‖≤poly(r,1/δ)`.
- **(A1)** `dist(t, span U)≥δ` for `t∉span U`; **(P1)** `σ_min(B)≥δ/√|B|`; **(B3)** `T`-spanned flats have
  `sinθ≥δ/r`; **(P9)** a positive switch (`Δ=‖p⁺‖²−‖p⁻‖²>0`) needs a constraint active on both sides ⟹
  `dim H_j≥2`; **exact-J:** if all `H_k⊆J` and `q_k∈J` then `P_{J^⊥}p_k` is invariant and `P_J p_k` runs the
  lower-rank dual process inside `J`.
- **Induction hypothesis (assume):** the polynomial bound holds at every rank `≤3` (proved: rank ≤2 = `r/δ`;
  rank 3 = `√53/δ²`). So any sub-run confined to a proper `T`-spanned flat `J` (`dim J≤3`) has `‖P_J p‖≤poly(1/δ)`.

### The mechanism you established (recap)
A "promotion" `J→K` (entering a strictly larger `T`-spanned flat `K⊃J`) can push the survivor component into
`(J+?)^⊥`. The danger (why naive flags give `D_exp`): each promotion can pay a factor `1/sinθ(J,K)` and these
multiply across a flag `J_0⊊J_1⊊⋯`, giving rank-dependent degree. Polynomiality requires that the accumulated
affine displacement **coboundary-cancels** on the matching return, paying each flag layer at most once.

### THE PIVOTAL CASE — prove the rank-4 closed-excursion holonomy
Work at ambient rank 4 (or general `r`, but rank 4 is the first nontrivial instance). Let `J` be a `T`-spanned
**rank-2** flat in a stabilized cluster state, and let `B` be a complete admissible excursion that:
- starts in the `J`-cluster (so `p = z + y`, `z∈J^⊥`, `y∈J`, `‖y‖≤poly` by the rank-2 hypothesis),
- promotes through **rank-3 superflats** `K` with `J⊂K⊂E` (the survivor may now hide in `(J+L)^⊥`),
- and **returns to the same refined `J`-state**.

Let the excursion's affine map (on the dual iterate) be `A_B(p)=Q_B p + b_B` (`‖Q_B‖≤1`, a product of
projectors). Prove:
> **Rank-4 closed-excursion holonomy:** `b_B = (I − Q_B)·c_{J,ω}` for a single memory vector `c_{J,ω}` with
> `‖c_{J,ω}‖ ≤ poly(1/δ)`, depending only on the `J`-state and the oriented-matroid entry data `ω` (NOT on the
> internal length of the excursion, and the SAME `c_{J,ω}` for every excursion from this state).

Then `A_B(p) − c_{J,ω} = Q_B(p − c_{J,ω})`, so the excursion is a contraction toward `c_{J,ω}`; chaining
excursions telescopes and gives `sup_j‖p_j‖ ≤ poly(1/δ)`. This closes rank 4, and the same scheme (flag-indexed
`c_σ`, one layer paid once) should template general `r`.

The structure to exploit (the audit's read): at the promotion `J→K`, decompose `z=z_0+z_1`, `z_0∈(J+L)^⊥`,
`z_1∈K∩J^⊥`; `z_1` is detected (`|P_L z_1|≥(δ/r)|z_1|`) but `z_0` is carried untouched. The memory `c_{J,ω}`
must "remember" `z_0` so that, on the matched return, the displacement it caused cancels as `(I−Q_B)c_{J,ω}`
WITHOUT re-paying `1/sinθ(J,K)`. Admissibility you may use: consecutive active faces share the trajectory
point `x_j`; `ρ=‖x_j‖` is monotone; the itinerary is an ordered oriented-matroid gallery (so promotions and
their matched pops are properly nested).

### What we need back
1. A proof of the **rank-4 closed-excursion holonomy** (hence rank 4, and ideally the general `r→r+1` step) —
   with an explicit `poly(1/δ)` bound on `‖c_{J,ω}‖` and the resulting `sup_j‖p_j‖`. OR a precise break-point
   (the exact obstruction to constructing `c_{J,ω}`). OR a refutation: an admissible rank-4 reversed-projection
   itinerary (constant `δ`) with super-polynomial `sup_j‖p_j‖` — equivalently a repeatable closed excursion `B`
   with `‖(I−Q_B)^† b_B‖` super-poly.
2. If partial: the exact remaining sub-lemma, cleanly stated.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

Use any machinery (oriented-matroid gallery nesting, projection-orbit cocycles/coboundaries, holonomy of the
flag bundle). If closing `c_{J,ω}` needs a tool not present here or in the standard literature, say exactly
what is missing — that pinpoints the hand-off to a human expert.
