# Human-Expert Handoff — `greedy-vector-balancing-polyupper`

**Date:** 2026-06-22 · **Status:** AI attack loop (8 rounds, GPT-5.5-Pro + independent audits) has produced a
strong partial result and isolated a single open core. Per the project's escalation ladder, the core is now
handed to a human expert. 🔴 **"AI-verified ≠ proved":** the results below are AI-produced and
independently AI-audited (analytic + numeric), NOT yet human-verified. Treat as conditional.

---

## 1. The problem (and why it matters)

Czerwiński–Dadush–Ergen–Ghosh–Lasota–Orlikowski, *Greedy Vector Balancing* (arXiv:2606.17991, 2026) study
the deterministic greedy Euclidean vector-balancing algorithm in the scaled model: finite `T⊆S^{d-1}`,
vectors arrive adversarially from `[-1,1]T`, greedy picks signs so the running sum has non-positive inner
product with each arrival; `G(T)=sup_k‖S_k‖`. They prove `G(T) ≤ (2/δ_T)^{d-1}` (exponential) and a lower
bound `Ω(√d/δ_T)`, where `δ_T = min{dist(t, span U) : U⊆T, t∈T, t∉span U}`, and **explicitly leave the
tightness open** ("We do not know if the estimate in Theorem 1.2 is tight").

> **TARGET `(★)` (this project, would resolve the open problem on the polynomial side ⟹ SODA):**
> for `δ_T ≥ 1/poly(d)` (e.g. constant `1/4`), `G(T) = poly(d, 1/δ_T)` — improving the exponential upper
> bound to polynomial.

---

## 2. The reduction (verified) — `(★)` ⟺ a bounded dual-drift / invariant-cylinder statement

Work in `E=span(T)`, `r=dim E`. Let `π_t` = orthogonal projection onto `t^⊥`.
- **Projective-body identity (verified):** with `K_0={0}`, `K_{n+1}=conv ⋃_{t∈T}(π_t K_n+[-t,t])`, the support
  function satisfies `h_{K_n}(y)=max_{chains} Σ_j‖y_j−y_{j-1}‖` (`y_j=π_{t_j}y_{j-1}`), and `G(T) ≤ radius(K_∞)`.
- **Dual process:** along a reversed projection trajectory (`x_j=x_{j-1}+α_j t_j`, `⟨x_{j-1},t_j⟩=0`; chambers
  `C_{s_j}`), define `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)` where `P_s={p∈E:⟨s_i t_i,p⟩≥1 ∀i}`. Then
  `p_{j+1}=P_{H_j^⊥}p_j+q_j` (`H_j`=span of active-face normals, `q_j∈H_j`, `‖q_j‖≤(dim H_j)/δ_T`).
- **Verified consequence:** `G(T) ≤ 2·sup_j‖p_j‖`. So `(★)` ⟺ `sup_j‖p_j‖ ≤ poly(r,1/δ_T)` for every
  admissible itinerary.

Inversive form (verified): `I(p)=p/‖p‖²` maps chambers to mutually-tangent lobes `L_s=⋂_i B(s_i t_i/2, ½)`;
`(★)` ⟺ the orbit never "cusps" into the common tangency point `0` (`inf_j‖I(p_j)‖ ≥ 1/poly`).

---

## 3. What is PROVEN (AI-produced, AI-audited; "use freely" pending human check)

| ID | Statement | Status |
|---|---|---|
| P1 | independent `B⊆T`: `σ_min(B) ≥ δ_T/√|B|` | numeric+analytic ✓ |
| P2/P2′ | `‖x‖>r/(2δ_T) ⟹ span N(x) proper`; `‖P_{H(x)}x‖≤q/(2δ_T)` | ✓ |
| P3′ | `|T| ≤ 2π r⁴/δ_T` (poly-many directions; via circuit imbalance `κ_A≤1/δ_A`, arXiv:2510.20301) | ✓ (NH1: eyeball the κ_A≤1/δ_A proof) |
| P4 | `G(T)≤radius(K_T)` + the support-function ITERATION identity (derived) | ✓ |
| P6 | `T`-spanned flats: `sinθ ≥ δ_T/r` (principal-angle separation) | ✓ |
| P7 | every realizable chamber has a margin-1 certificate of norm `≤ r/δ_T` | ✓ |
| P8 | exact dual dynamics + energy/telescoping/Bessel (`‖Σ R_j q_j‖ ≤ (r/δ)√N`) | ✓ |
| P9 | KKT localization: positive dual jump only from constraints active both sides; no-common ⟹ Δ≤0 | ✓ |
| P10 | all UNPAID dual drift confined to a codim-≥2 wall cluster | ✓ |
| **P11** | **rank ≤2 closed:** `sup_j‖p_j‖ ≤ r/δ_T` (saturated) | ✓ |
| **P12** | **rank 3 closed:** `sup_j‖p_j‖ ≤ √53/δ_T² < 8/δ_T²` (degree 2) | ✓ |
| **P13** | **rank 4 closed:** `sup_j‖p_j‖ = poly(1/δ_T)` (all-word `O(δ^{-13})`; structural cross-section `O(δ^{-9})`). Mechanism: each K-confined return induces on `L=K∩J^⊥` a map that is a contraction (ratio ≤1−poly(δ)) OR an identity with ZERO translation (slope=1 ⟹ `a_B=0`); uniformly absorbing. | ✓ (NH6: one-arrangement→general write-up) |
| D_exp | all-word bound `2(r/δ)·5^{r-1}·(2r/δ)^{r(r-1)}` (exp in r; avoids the dead angle route) | ✓ |

**Numerics:** across all probes (adversarial projection-TV, dual-drift `sup_j‖p_j‖` flat in trajectory
length N, targeted codim-≥2 cluster stress, cocycle fixed-cycle probe) the dual drift stays **bounded and
≈`poly(r,1/δ)`** with NO super-polynomial growth found — consistent with `(★)` being TRUE.

---

## 4. THE OPEN CORE (what the human expert is asked to prove or refute)

The whole problem reduces to ONE statement (open for the **multidimensional-survivor case, rank ≥5**; proven
for ranks ≤4 by rank-specific collapses):

> **Cross-state invariant-cylinder cocycle.** For each refined cluster state `σ` (a nested flag of "promoted"
> survivor flats, with oriented-matroid entry data), construct a compact convex cross-section `C_σ ⊂ V_σ^⊥`
> (`V_σ` = the joint-neutral survivor space of the return semigroup at `σ`) with `sup_{c∈C_σ}‖c‖ ≤
> poly(r,1/δ_T)`, such that for every admissible primitive cluster block `B:σ→τ` with affine return map
> `A_B(p)=Q_B p + b_B` (`‖Q_B‖≤1`, product of orthogonal projections onto `T`-flats),
> `A_B(C_σ) ⊆ C_τ`.
> Then nonexpansiveness gives `dist(A_B p, C_τ) ≤ dist(p, C_σ)`; at a top-rank state (`V_σ={0}`) a poly
> cross-section radius yields `sup_j‖p_j‖ ≤ poly`, hence `(★)` and `G(T)=poly(d,1/δ_T)`.

**Equivalently** (the hard analytic kernel): a *quantitative admissibility theorem* showing that the affine
translations `b_B` do not accumulate along the **joint-neutral directions** of the return semigroup — with a
bound of degree **independent of the flag depth**. (Generic nonexpansiveness/boundedness gives only a
geometry-dependent constant; the project needs `poly(r,1/δ)`.)

**Why ranks ≤4 don't template it:** rank 2 has no survivor; rank 3's survivor cannot hide (`J+L=E`); rank 4's
returned layer is 1-dimensional and the return linear part is a projector onto an *original* flat, so the
survivor is reset (contraction-or-neutral). At rank ≥5 the returned layer can be multidimensional and `Q_B`
is **not** a projector onto an original flat — the "dangerous dynamically-projected directions" return, and
this is exactly where the argument has been stuck since Round 2.

---

## 5. Dead routes (do NOT re-attempt — each has an explicit refutation)

- **N1** fixed-`O(1)`-rank multiplicative amplifier (additive, not multiplicative).
- **N2** one fixed certificate per ORIGINAL chamber (rank-3 obstruction: `⟨t_i,t_j⟩=¾` ⟹ no convex `F`
  linear on the 8 chambers).
- **N3** the P6/Friedrichs-angle charging (P6 does NOT transfer to the dynamically-projected images `R_jH_j`;
  their angles collapse to ~0).
- **N4** any LOCAL per-switch payment (`r/δ` ball not projection-invariant; genuine itinerary with `Δ=48/7`
  while local radial increment →0).
- **N5** the POINT-valued holonomy `b_B=(I−Q_B)c_{J,ω}` (explicit constant-δ rank-4 example: two excursions,
  same `Q`, `b_A≠b_B` ⟹ no common memory vector; the holonomy is bounded but **set-valued**, not a point
  coboundary). *Caution:* the "neutral-space" point form `P_{V_σ}b_B=0` (proposed in Round 8's (32)) is the
  same dead idea at rank ≥5 — the cocycle must be **set-valued**.

So the surviving target is genuinely **set-valued** (invariant cylinders/cross-sections), history-dependent
(N2), and cannot be obtained by transferring original-flat angle bounds to projected images (N3) or by any
local/per-switch estimate (N4) or point coboundary (N5).

---

## 6. Candidate machinery (suggestions for the expert)

- Oriented-matroid galleries / tope graphs of the hyperplane arrangement `{t^⊥}`; nesting of promotions and
  matched pops as a properly-nested gallery walk.
- Quantitative theory of **products/orbits of metric projections onto a finite family of polyhedra**
  (Meshulam 1996; Bauschke–Tung arXiv:2506.22553 cover polyhedra but give only geometry-dependent, non-poly
  constants; Güntürk–Thao arXiv:1901.07516 absolute convergence; arXiv:2601.07002, 2602.00544) — the gap is a
  **polynomial-in-(r,1/δ)** constant, which none of these supply.
- Affine IFS / contraction semigroups with a common invariant compact set (here the maps are nonexpansive
  with `T`-flat-projection linear parts and poly-bounded translations).
- The project's own substrate P1–P13 + D_exp (use freely).

---

## 7. Honest status for the decider

- **Proven (AI, audited):** ranks ≤4 of `(★)`; the full reduction chain; the precise open core; all dead
  routes. **Not proven:** general-`r` `(★)` (the SODA-necessary headline).
- **Confidence `(★)` is TRUE: ~72%** (numerics consistently bounded; no refutation found in 8 rounds; but the
  general core is genuinely hard and the surviving set-valued cylinder is where an exponential would hide if
  `(★)` were false).
- **No matching lower bound** has been attempted — do NOT claim "tight/optimal"; the anchor's `Ω(√d/δ_T)`
  stands. (Closing the poly-degree-vs-`√d` gap is a separate, nice-to-have item.)
- **Decision for the owner (human gate):** (a) hand the open core (§4) to a human expert and, if proven,
  submit the full resolution to SODA; (b) any change of scope/venue (e.g. a weaker "partial-progress + new
  framework" paper) is the owner's call — the AI loop does NOT downgrade by default (no-retreat).

*Pointers:* full per-round record in `docs/round{1..8}_{brief,response,audit}.md` + `docs/ATTACK_LOG.md`;
frozen model/substrate/confidence in `LEDGER_polyupper.md`; reproducible numerics in `code/`.
