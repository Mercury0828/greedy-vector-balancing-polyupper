# Round-9 Brief (FINAL, FRESH-CONTEXT decisive attack) — to a NEW GPT-5.5-Pro session

> **Orchestrator metadata (do NOT send).** This is the FINAL decisive attack, in a brand-new GPT-5.5-Pro
> conversation (no prior thread). 8 prior rounds (one solver lineage) reduced the problem to a single core but
> circled it; the owner is invoking the fresh-context lever for a last full-strength attempt. DESIGN: present
> the ORIGINAL problem cleanly and invite a genuinely NEW route — the accumulated dual-cylinder framework is
> given only as an OPTIONAL appendix the attacker may discard.
> 🔴 OWNER STEERING (2026-06-22): the brief carries an explicit CLOSURE MANDATE — extracting/relabeling
> another "core" or "break-point" is declared NOT a useful outcome (8 rounds already did that); the solver is
> pushed to actually PROVE or REFUTE. Rationale: framing the task as "reduce / extract a break-point" lets the
> solver settle for a partial instead of going all-out. Archive reply → `docs/round9_response.md`;
> independent audits (3 if closure). If this does not close or refute, the project goes to the owner gate.

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO A NEW GPT-5.5-PRO CHAT ✂️

You are attacking, at full strength, a concrete open problem in discrepancy theory. **Solve it your way** —
bring whatever machinery fits, and feel free to ignore the optional appendix entirely if you see a cleaner
route. End with a definite verdict and a confidence (%).

🔴 **MANDATE — read before you start.** We want a **PROOF of `(★)`** (or a genuine **REFUTATION**). We do
**NOT** want another reduction. Over many prior expert attempts this problem has repeatedly been "reduced to
a cleaner equivalent sub-lemma" or had "a precise break-point extracted" — **that has not helped, and it is
not what we need.** So:
- Do **not** treat "isolate/restate a cleaner core" or "hand back a precise break-point" as a successful
  outcome. Restating the obstruction in new language (a semigroup bound, a cocycle, an invariant-set lemma,
  etc.) is **explicitly not progress here** — it has been done.
- Commit your full effort to **actually closing it**: either prove the polynomial bound, or build an explicit
  super-polynomial counterexample. Push each idea to the end; combine techniques; do the hard estimates.
- A break-point is acceptable **only as a true last resort**, only **after** a maximal genuine attempt, and
  only if it is a *concrete, fully-specified, independently-checkable* statement that is **strictly easier
  than and provably different from** the open core below (not a relabeling of it) — and even then, try hard
  to settle that statement yourself before reporting it. Default expectation: you return a proof or a
  refutation.

### The problem `(★)`

Czerwiński–Dadush–Ergen–Ghosh–Lasota–Orlikowski (arXiv:2606.17991, 2026) analyze deterministic greedy
Euclidean vector balancing. Finite `T ⊆ S^{d-1}`; vectors arrive online and adversarially from the scaled set
`[-1,1]T = {a·t : a∈[-1,1], t∈T}`; the algorithm keeps `S_k = Σ_{i≤k} s_i v_i` and at each step picks the sign
`s_k∈{±1}` so that `s_k v_k` has non-positive inner product with `S_{k-1}`. Let `G(T) = sup_k ‖S_k‖`.

Define the **distance property** `δ_T = min{ dist(t, span U) : U⊆T, t∈T, t∉span U }` (the min nonzero distance
from a `T`-vector to the span of others). They prove `G(T) ≤ (2/δ_T)^{d-1}` (exponential) and an existence
lower bound `Ω(√d/δ_T)`, and **explicitly leave the tightness open** ("We do not know if the estimate in
Theorem 1.2 is tight").

> **Prove or refute `(★)`:** for `δ_T ≥ δ` with `δ` constant (e.g. `1/4`) or `δ ≥ 1/poly(d)`,
> `G(T) ≤ poly(d, 1/δ)`. I.e. improve the exponential upper bound to polynomial in the well-separated regime.
> "Done" = an explicit `poly(d,1/δ)` bound (any degree), OR a precise statement of where it provably fails,
> OR a refutation: a constant-`δ` family of finite `T` (realizable by the greedy process) with `G(T)`
> super-polynomial in `d` (which would mean the truth is the exponential side).

A few reliable facts you may use freely (all independently verified):
- **(F1)** any independent `B⊆T` has `σ_min(B) ≥ δ_T/√|B|` (so no exponential ill-conditioning among
  independent directions).
- **(F2)** at high radius growth is confined: only directions `t` with `|⟨t,x⟩|<½` can increase `‖x‖` (unit
  step), and `‖x‖ > r/(2δ_T)` forces `span{t:|⟨t,x⟩|<½}` to be a proper subspace of `span T` (`r=dim span T`).
- **(F3)** `T` has only polynomially many distinct directions: `|T| ≤ 2π r⁴/δ_T` (circuit-imbalance column
  bound; for unit columns `κ_A ≤ 1/δ_T`).
- **(F4)** `T`-spanned flats are angle-separated: any two subspaces spanned by subsets of `T` have smallest
  positive principal angle with `sin θ ≥ δ_T/r`.
- **(F5)** `G(T) ≤ radius(K_T)` where `K_T` is the minimal convex `T`-absorbing body; equivalently
  `G(T) ≤ max over chains Σ_j ‖y_j − y_{j-1}‖`, `y_j = π_{t_j} y_{j-1}` (`π_t` = projection onto `t^⊥`). So a
  polynomial bound on this projection-trajectory total variation would prove `(★)`.

**Numerical evidence (ours):** extensive adversarial search (projection-trajectory total variation; a dual
process described in the appendix; targeted near-degenerate stress; trajectories of length up to ~350) finds
`G(T)`-type quantities consistently BOUNDED and polynomial in `d` at constant `δ`, with NO super-polynomial
growth — so we believe `(★)` is TRUE (~72% confidence), but a proof has resisted.

### What we need back (in priority order)
1. **A PROOF of `(★)`** (any route — a fresh one is very welcome), with an explicit `poly(d,1/δ)` bound; OR a
   **REFUTATION** (a constant-`δ`, greedy-realizable family with super-polynomial `G(T)`). One of these is the
   goal — please aim squarely at it and use your full strength.
2. Only if (1) genuinely defeats a maximal attempt: a single concrete obstruction that is **strictly easier
   than and provably distinct from** the open core (NOT a restatement) — with your best partial results toward
   settling it. (Reminder: merely reducing `(★)` to another clean lemma is *not* a useful deliverable here.)
3. Your confidence (%) and a one-line verdict (closed / refuted / genuinely-stuck-and-why).

---

## OPTIONAL APPENDIX — one route that reached rank 4 and stalled (reuse, or discard entirely)

We reduced `(★)` to a dual projection-orbit problem and CLOSED it for `span T` of rank `r ≤ 4`, but the
general case stalls at one set-valued lemma. **If you see a cleaner approach to `(★)`, ignore all of this.**

**The dual process.** Along a reversed projection trajectory (`x_j = x_{j-1}+α_j t_j`, `⟨x_{j-1},t_j⟩=0`),
which visits arrangement chambers `C_{s_j}` (`s∈{±1}^{|T|}`), define certificate polyhedra
`P_s = {p : ⟨s_i t_i, p⟩ ≥ 1 ∀i}` and the metric-projection orbit `p_{j+1} = Proj_{P_{s_{j+1}}}(p_j)`, init
`p_1∈P_{s_1}`, `‖p_1‖≤r/δ`. Then `p_{j+1} = P_{H_j^⊥}p_j + q_j` (`H_j` = span of the active-face normals
⊆ `T`, `q_j∈H_j`, `‖q_j‖≤(dim H_j)/δ`). VERIFIED: `G(T) ≤ 2·sup_j‖p_j‖`. So `(★)` ⟺ `sup_j‖p_j‖ ≤ poly`.

**What is proven (rank = `dim span T`):**
- rank ≤2: `sup_j‖p_j‖ ≤ r/δ`.  rank 3: `≤ √53/δ²`.  rank 4: `= poly(1/δ)` (`O(δ^{-13})` explicit).
- Each closes by a "survivor reset": decomposing the iterate along a flag `J⊂K`, the return map on the
  newly-exposed survivor direction `K∩J^⊥` is either a contraction or a zero-translation identity, giving a
  bounded absorbing interval / invariant convex "cylinder".

**The exact open core (general rank ≥5).** Cluster the unpaid transitions into "blocks" `B` with affine
return maps `A_B(p)=Q_B p+b_B` (`‖Q_B‖≤1`, products of `T`-flat projections), indexed by a refined flag state
`σ` (the nested promoted survivor flats + oriented-matroid entry data). We need:
> **(CORE)** compact convex cross-sections `C_σ ⊂ V_σ^⊥` (`V_σ` = joint-neutral survivor space of the return
> semigroup at `σ`), with `sup_{c∈C_σ}‖c‖ ≤ poly(r,1/δ)`, such that `A_B(C_σ) ⊆ C_τ` for every admissible
> block `B:σ→τ`. Equivalently: a quantitative theorem that the affine translations `b_B` do NOT accumulate
> along the joint-neutral directions of the return semigroup, with **degree independent of flag depth**.

Then nonexpansiveness gives `dist(A_B p, C_τ) ≤ dist(p, C_σ)`; at a top-rank state (`V_σ={0}`) a poly
cross-section radius yields `sup_j‖p_j‖ ≤ poly`, hence `(★)`. Ranks ≤4 are the cases where `V_σ` is `≤1`-dim
and `Q_B` is a projector onto an original flat; rank ≥5 has multidimensional survivors and `Q_B` need not be
such a projector — that is the whole open difficulty.

**Routes already RULED OUT (do not repeat):**
- **N1** a fixed-`O(1)`-rank multiplicative amplifier (it is additive, not multiplicative).
- **N2** one fixed certificate per ORIGINAL chamber (rank-3 obstruction: `⟨t_i,t_j⟩=¾` ⟹ no convex `F`
  linear on the 8 chambers).
- **N3** charging via the angle bound (F4) on the *dynamically projected images* `R_jH_j` — those are NOT
  `T`-spanned and their angles collapse to ~0; (F4) does not transfer to them.
- **N4** any LOCAL per-switch payment (`r/δ`-ball is not projection-invariant; a genuine constant-δ itinerary
  raises `‖p‖²` by a fixed amount while the local radial increment → 0).
- **N5** a POINT-valued holonomy `b_B = (I−Q_B)c_σ` (one common memory vector per state) — refuted by an
  explicit constant-δ rank-4 example (two excursions, same `Q_B`, different `b_B`); the holonomy is bounded
  but genuinely SET-VALUED. Its "neutral-space" point form `P_{V_σ}b_B=0` is the same dead idea at rank ≥5.

So the surviving target is genuinely **set-valued** (invariant cross-sections / cylinders),
**history-dependent**, and cannot come from local estimates, point coboundaries, or transferring
original-flat angles to projected images. Candidate machinery we did not fully exploit: oriented-matroid
gallery nesting of promotions/pops; quantitative orbit theory for products of metric projections onto a
finite family of polyhedra (Meshulam / Bauschke–Tung give only geometry-dependent constants — the gap is a
polynomial-in-`(r,1/δ)` constant); common invariant compact sets of nonexpansive affine IFS.

If closing `(CORE)` needs a tool absent here and in the standard literature, say exactly what is missing.
