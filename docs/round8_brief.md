# Round-8 Brief — to GPT-5.5-Pro (continue fresh thread) — the rank-4 INVARIANT-STRIP sublemma

> **Orchestrator metadata (do NOT send).** Continue the FRESH thread. Round 7 correctly REFUTED our
> point-valued holonomy conjecture and replaced it with a SET-VALUED target (verified exactly: the holonomy is
> bounded but nonzero; the example keeps a bounded invariant cylinder, so `(★)` is NOT refuted). 🔴 **This is the
> LAST AI attacker round on the rank-4 pivot.** If it neither constructs the poly-radius invariant interval nor
> pins a clean obstruction, we escalate to a human expert (oriented-matroid galleries / projection-orbit
> cocycles). Archive → `docs/round8_response.md`; independent audits (3 if closure).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO GPT-5.5-PRO ✂️

Continuing. Your refutation of the point-valued holonomy is verified (exact): two admissible closed excursions
from the same combinatorial `(J,ω)` state with the same linear part `Q` but `b_A≠b_B`, so no single fixed
vector works — the return holonomy is bounded but NONZERO, a hysteresis strip. Crucially, both maps keep a
bounded invariant cylinder, so `(★)` is not refuted. You proposed the right replacement; this brief asks you to
prove it (the rank-4 instance). **Solve it your way.** End with a definite verdict and confidence (%).

### Verified substrate (use freely)
- Dual process `p_{j+1}=P_{H_j^⊥}p_j+q_j`, `H_j`=span of active-face normals (subsets of `T`), `q_j∈H_j`,
  `‖q_j‖≤(dim H_j)/δ`. `δ=δ_T≤1`. Goal `(★)`: `sup_j‖p_j‖≤poly(r,1/δ)`.
- **(A1)** `dist(t, span U)≥δ`; **(P1)** `σ_min(B)≥δ/√|B|`; **(B3)** `T`-spanned flats: `sinθ≥δ/r`;
  **exact-J:** all `H_k⊆J`, `q_k∈J` ⟹ `P_{J^⊥}p_k` invariant, `P_J p_k` runs the lower-rank dual process.
- **Proven:** rank ≤2 bound `r/δ`; rank 3 bound `√53/δ²`. So any sub-run confined to a proper `T`-flat
  `J` (`dim J≤3`) keeps `‖P_J p‖≤poly(1/δ)`.
- **Round-7 structure (use it):** for a fixed `J⊂K` (ranks 2, 3) and excursions confined to `K` returning to a
  refined `J`-state, the affine return map is `A_B(p)=Q_B p+b_B` with `Q_B` = orthogonal projector onto `K^⊥`
  (so `‖Q_B‖=1`, nonexpansive) and `b_B` varying with the excursion but lying in the 1-dim line
  `K∩J^⊥` (mod the invariant `K^⊥` direction). Different excursions give different `b_B` but a BOUNDED spread.

### THE TARGET — the rank-4 invariant-strip sublemma
> Let `J⊂K⊂E` with `dim J=2`, `dim K=3`, ambient rank 4. Consider all composable admissible `K`-confined
> excursions from one refined `J`-cluster state. Each induces a scalar affine return map on the 1-dimensional
> space `K∩J^⊥`. **Prove these maps admit a common invariant interval `I⊂K∩J^⊥` of radius `poly(1/δ)`** (i.e.
> a compact interval mapped into itself by every such excursion's return map, with `|I|≤poly(1/δ)`).

Then (you indicated): these intervals produce bounded strips in the 2-dim survivor plane `J^⊥`; different
`K^⊥`-directions have sine-separation `≥δ/4` (B3-type); the full-span block contraction (`‖Q‖≤β_{r}<1`) bounds
switching among the strips polynomially. Chaining (each `A_B` nonexpansive toward the strip) telescopes to
`sup_j‖p_j‖≤poly(1/δ)` at rank 4 — and the same set-valued scheme should lift to general `r` (the
**Polynomial invariant-cylinder theorem**: compact convex cross-section `C_σ⊂V_σ^⊥`, `sup‖c‖≤poly`,
`A_B(C_σ+V_σ)⊆C_τ+V_τ`; at top rank `V_σ={0}` ⟹ `(★)`).

### Why the strip should exist (heuristics to confirm or break)
- Each return map on `K∩J^⊥` is affine with linear part a contraction or identity on that line (it is a
  composition of projections; the `K^⊥` part is killed, the `J`-part is poly-bounded by the rank-2 hypothesis).
- The translation amounts `b_B` are bounded because: at the promotion `J→K`, the survivor entering `(K∩J^⊥)`
  is detected with margin `≥δ/r` (B3), and the rank-2/rank-3 proven bounds cap the in-flat parts. The question
  is whether the FAMILY of these affine maps (over all excursions) has a common invariant compact interval —
  equivalently, whether the semigroup they generate has bounded orbits with a poly-radius attractor on the line.
- Admissibility you may use: consecutive active faces share the trajectory point `x_j`; `ρ=‖x_j‖` monotone;
  oriented-matroid gallery nesting of promotions/pops.

### What we need back
1. A proof of the **rank-4 invariant-strip sublemma** (a common invariant interval of radius `poly(1/δ)`),
   hence rank 4 and ideally the general invariant-cylinder theorem ⟹ `(★)` with explicit degree. OR a precise
   break-point (the exact obstruction to a common invariant interval). OR a refutation: an admissible
   `K`-confined excursion FAMILY whose return maps on `K∩J^⊥` have NO common invariant interval of poly radius
   (i.e. force the line-orbit to escape super-polynomially) — that would refute `(★)`.
2. If partial: the exact remaining sub-lemma, cleanly stated, and what tool is missing (this pinpoints the
   hand-off to a human expert).
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).

Any machinery welcome (1-dim affine IFS / contraction semigroups, oriented-matroid gallery nesting,
projection-orbit attractors). If a common invariant interval provably cannot have poly radius by elementary
means, say exactly which deeper structure is required.
