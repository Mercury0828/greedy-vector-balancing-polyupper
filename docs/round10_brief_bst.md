# Round-10 Brief (targeted BST attack) — to a NEW GPT-5.5-Pro chat

> **Orchestrator metadata (do NOT send).** Round 9 simplified the open core to the BASIS level (BST) and
> identified BST ≡ a depth-independent (poly) Meshulam relaxed-projection boundedness theorem; BST numerics are
> clean `√r` to r=50. This brief attacks BST directly as a clean, standalone, fully-specified problem (fresh
> context). 🔴 CLOSURE MANDATE retained — we want a proof or a refutation, not another reduction. Archive →
> `docs/round10_response.md`; 3 independent audits if closure is claimed.

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO A NEW GPT-5.5-PRO CHAT ✂️

A clean, fully-specified open problem about an affine projection process. **Solve it your way.** We want a
**PROOF or a REFUTATION** — please go all-out for one of those; merely restating/reducing it to another
equivalent lemma is **not** a useful outcome (that has been done). End with a definite verdict + confidence (%).

### The problem (BST)

Let `T = {t_1,…,t_r}` be a basis of `ℝ^r` of unit vectors, `A=[t_1 … t_r]`, `G = A^⊤A` (so `G` is a positive
definite correlation matrix, unit diagonal). Its **separation** is `δ := 1/√(max_i (G^{-1})_{ii})`
(equivalently `δ = min_i dist(t_i, span(T∖{t_i}))`); assume `δ ≥ δ_0` with `δ_0` constant (e.g. `1/4`) or
`≥ 1/poly(r)`.

Consider the adversarial orbit in coordinates `c∈ℝ^r`, started at `c_0=0`: at each step the adversary picks a
coordinate `i_k∈[r]` and a sign `ε_k∈{±1}`, and updates
> `c_{k+1} = c_k + (ε_k − (G c_k)_{i_k})·e_{i_k}`.

Equivalently, with `p = A c` (so `‖p‖² = c^⊤ G c`), this is the metric-projection process
`p_{k+1} = π_{t_{i_k}} p_k + ε_k t_{i_k}` (`π_t = I − tt^⊤`); the post-step residual is `(G c_{k+1})_{i_k} = ε_k`,
and the energy obeys
> `‖p_{k+1}‖² = ‖p_k‖² + 1 − (G c_k)_{i_k}²`   (so energy is non-decreasing exactly at productive coords
> `|(Gc)_i| < 1`).

> **Prove or refute (BST):** `sup_k c_k^⊤ G c_k ≤ poly(r, 1/δ)` for every adversarial choice of
> `(i_k, ε_k)_k`. (A bound of any polynomial degree suffices.)

**Why it matters / equivalences (optional context):**
- BST is *equivalent* to the open tightness question for greedy Euclidean vector balancing
  (Czerwiński et al., arXiv:2606.17991): a `poly(r,1/δ)` bound here ⟹ the greedy worst-case norm is
  `poly` (improving their exponential `(2/δ)^{r-1}`), resolving a stated open problem.
- Equivalently it is a **quantitative, depth-independent Meshulam theorem**: Meshulam (1996) and its modern
  extension (arXiv:2602.00544) prove orbits of relaxed projections onto a finite family of affine subspaces
  are *bounded* even with empty intersection — but the known constant is
  `(τ+D)/(1 − √(1 − λ(2−λ)·κ₊^{−2(ℓ−1)}))`, **exponential in the number of subspaces / flag depth `ℓ`**. BST
  asks for a bound polynomial in `(r, 1/δ)` (hence depth-independent). That improvement is exactly the gap.

### What is already known (use freely)
- **Energy/Bessel.** With `v_j = π_{t_1}…π_{t_{j-1}} t_j`, `‖p_n‖`-type sums equal `max_{ε}‖Σ_j ε_j v_j‖`, and
  `Σ_j v_j v_j^⊤ = I − (π_{t_n}…π_{t_1})^⊤(π_{t_n}…π_{t_1}) ⪯ I` (a Bessel system). So BST ⟺ a polynomial
  **unconditionality** bound for these projection-generated Bessel sequences. (`Σ v_j v_j^⊤ ⪯ I` alone is not
  enough — a generic Bessel sequence gives signed sums of order `√n`; the projection structure must do the work.)
- **One independent sweep is harmless.** If `t_1,…,t_r` are each used once (any signs), the orbit ends inside
  the radius-`√r` ball — with NO dependence on δ. (`L+L^⊤=H+I⪰I` ⟹ `‖L^{-1}‖₂≤2`; `‖Ac‖²=r−‖α−ε‖²≤r`.)
- **Return-time reduction.** For a block of length `L` containing a full-rank sub-sweep,
  `Σ_block ‖p_j−p_{j-1}‖² ≥ (δ²/(4r²L))·‖p_start‖²`. So a **polynomial bound on the full-rank return time `L`
  ⟹ BST.** The difficulty is that `L` is adversarially unbounded, and applying this rank-by-rank compounds to
  exponential — this is the precise temporal obstruction.
- **A solved structured case (sanity).** If `T` sits inside a centrally-symmetric reflection (root) system
  `R` of size `poly(r)` closed under all `R_t = I−2tt^⊤`, then `Φ(x)=½Σ_{u∈R}|⟨u,x⟩|` is a global Lyapunov
  potential dropping by `≥ ‖step‖` per projection, giving `sup_k‖p_k‖ ≤ |R|/2`. (This handles e.g. all
  graphical `t=(e_u−e_v)/√2` at `δ≈r^{-1/2}`.) The open problem is a Lyapunov/adapted-norm that works for a
  GENERAL well-conditioned `G`, where no such finite reflection orbit exists.
- **Numerics.** Adversarial search over `(i_k,ε_k)` (beam + restarts) at constant δ, to `r=50` (random and
  structured/near-collinear bases), finds `sup_k‖p_k‖ ≍ √r` (clean polynomial, no super-polynomial growth).
  So we believe BST is TRUE (~74%), but a proof has resisted; a refutation is not excluded.

### Routes already ruled out (do not repeat)
- A LOCAL per-step payment ("energy jump ≤ poly·local progress") is impossible: a step can raise `‖p‖²` by a
  fixed amount while the local primal increment → 0.
- A POINT-valued invariant ("all returns share one fixed point/coboundary `b_B=(I−Q_B)c`") is false: distinct
  returns from the same state have different translations; the invariant must be **set-valued** (an invariant
  convex body / adapted norm).
- Transferring the original-vectors' angle separation (`sin θ ≥ δ/r` between `T`-spanned flats) to the
  *dynamically projected* images fails — those images can become arbitrarily ill-separated.
- The naive potential `Σ_t |⟨t,x⟩|` is not monotone at constant δ.

### Candidate machinery (suggestions, not constraints)
- A **quantitative / depth-independent Meshulam (paracontraction) boundedness theorem** for projection-generated
  affine families — the literature constant is exp-in-depth; the task is to remove that.
- A global **adapted norm / Lyapunov function** for a general PD `G` whose Euclidean distortion is `poly(r,1/δ)`
  (degree independent of orbit length / flag depth) — the set-valued invariant body.
- de Pierro / Bauschke POCS and paracontraction rate theory; signed-residual coordinate-descent on a quadratic.

### Refutation route (if BST is false)
Relaxed/contractive projections embed in exact ones: `I − λ tt^⊤` is the compression of an orthogonal
projector (dilation). A constant-δ family of well-conditioned bases on which an exponential time-varying
contraction orbit lifts to this process (keeping `δ ≥ r^{-O(1)}`) would refute BST (and `(★)`). We did not find
one; the lifted normals' separation was uncontrolled — but it is a concrete target.

### What we need back (priority order)
1. **A PROOF of BST** with an explicit `poly(r,1/δ)` bound and degree; OR a **REFUTATION** (an explicit
   constant-δ well-conditioned `G` + adversarial schedule with `sup_k c_k^⊤Gc_k` super-polynomial in `r`).
2. Only if (1) defeats a maximal attempt: the single concrete sub-fact that resists, *strictly easier than and
   distinct from* BST (not a relabeling), with your best partial results toward it.
3. Confidence (%) and one-line verdict (closed / refuted / genuinely-stuck-and-why).
