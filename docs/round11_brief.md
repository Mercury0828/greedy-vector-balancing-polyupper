# Round-11 Brief (FRESH-CONTEXT, decisive) — to a NEW GPT-5.5-Pro chat

> **Orchestrator metadata (do NOT send).** Owner chose option A: attack the one explicit hard region. Round 10
> closed broad sub-classes (P15) and tested the pinned hard region (deficient-block PCT gap on the Hadamard
> family) — it is numerically CLEAN (γ does not collapse), so a proof is very likely chasing a TRUE statement.
> This brief targets the single remaining open step. 🔴 CLOSURE MANDATE retained: prove or refute — not another
> reduction. Archive → `docs/round11_response.md`; audit on **codex GPT-5.5-xhigh** (per owner; via the codex MCP).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO A NEW GPT-5.5-PRO CHAT ✂️

A clean, fully-specified open problem. **Solve it your way.** We want a **PROOF or a REFUTATION** — go all-out
for one; restating/reducing it to another equivalent lemma is explicitly **not** a useful outcome. End with a
definite verdict + confidence (%).

### Setup
Let `T={t_1,…,t_r}` be a unit-vector basis of `ℝ^r`, `A=[t_1…t_r]`, `G=A^⊤A` (PD, unit diagonal), separation
`δ := 1/√(max_i (G^{-1})_{ii}) = min_i dist(t_i, span(T∖t_i))`, with `δ ≥ δ_0` constant (e.g. `1/4`) or
`≥1/poly(r)`. Write `P_i = I − t_i t_i^⊤` (projection onto `t_i^⊥`).

For a finite word `w=(i_1,…,i_m)` over `[r]`, let `R_w = P_{i_m}⋯P_{i_1}`. Call `w` a **full word** if it
contains every index at least once. Define the **cycle-gap**
> `γ(w) = 1 − ‖R_w‖²` (`‖·‖` = spectral norm).

### The problem (PCT — the one open step; proving it closes everything)
> **Prove or refute:** there is a polynomial `q(r,1/δ)` such that **every full word `w`** satisfies
> `γ(w) ≥ 1/q(r,1/δ)`.

Equivalently: for any full word, the projection product `R_w` is bounded away from an isometry by at least
`1/poly`. This is a purely homogeneous statement (no signs, no translations, no orbits).

**Why this is the whole game (verified):**
- A `poly` lower bound on `γ` ⟹ the full vector-balancing target (`G(T)=poly(d,1/δ_T)`, resolving the open
  tightness of Czerwiński et al. arXiv:2606.17991, exponential `(2/δ)^{d-1}` → polynomial).
- Conversely a **super-polynomially small** `γ` on a constant-`δ` family ⟹ an explicit counterexample
  (refutation): the palindrome word `w·reverse(w)` gives `Q=R_w^⊤R_w⪰0`, `λ_max(Q)=1−γ`, and the affine
  process `p_{k+1}=P_{i_k}p_k+ε_k t_{i_k}` repeating a signed palindrome has, for some sign choice,
  `sup_k‖p_k‖² ≥ (2−γ)/γ`. So small `γ` is realizable as unbounded growth. **PCT is therefore strictly weaker
  than, and two-way bridged to, the main problem.**

### What is already PROVEN (use freely)
- **Universal gap:** `γ(w) ≥ δ^{2r}/r^{r-1}` for every full word (Bessel `I−R^⊤R=Σ_k v_k v_k^⊤`,
  `v_k=P_{i_1}⋯P_{i_{k-1}}t_{i_k}`; the first-occurrence frame is triangular with diagonal `≥δ`). Exponential —
  the target is to make this `poly`.
- **Permutation gap:** `γ ≥ δ²/r³` when `w` uses each index exactly once (`La=b`, `L+L^⊤=G+I⪰I`).
- **Round-partitioned words** (concatenations of permutations) are fully controlled. So **the difficulty is
  exactly DEFICIENT blocks: long sub-words that repeat a strict subset of indices before the last missing
  index appears.** Only deficient structure could, a priori, drive `γ` below `δ²/r³` toward super-poly small.
- **Closed regimes (no help needed there):** comparison-stable bases `ρ(|G−I|)≤1−η ⟹ γ ≥ poly`; equicorrelation
  `G_α`; sign-switchable obtuse bases. The OPEN region is **well-conditioned, non-comparison-stable bases with
  deficient blocks** — concretely the signed Sylvester–Hadamard family `G_r = I + (H_r−D_r)/(4√r)` (`δ≈0.97`
  constant, yet `ρ(|G_r−I|)=Θ(√r)`).
- **Equivalent framing:** PCT is a **quantitative, depth-independent Meshulam theorem**. Meshulam (1996) /
  arXiv:2602.00544 prove orbits of relaxed projections onto a finite affine family are *bounded*, but their
  constant is **exponential in the number of subspaces / flag depth** (`κ₊^{−2(ℓ−1)}`). PCT asks to replace
  that by `poly(r,1/δ)` — i.e. a depth-independent rate.
- **Numerics (strong prior that PCT is TRUE):** adversarially MINIMIZING `γ` over deficient-block full words —
  on the Hadamard family and random well-conditioned bases — never drives `γ` below `~1/r` (Hadamard: `γ≈0.90`
  flat to r=32; random: `~0.03` at r=10), far above the `δ²/r³` floor. No near-isometric full word found.

### Routes already ruled out (do not repeat)
- LOCAL per-step payment (a step can add fixed energy with local primal increment →0).
- POINT-valued invariants / coboundaries (the invariant must be set-valued).
- Transferring the original angle separation `sinθ≥δ/r` to *dynamically projected* images (those collapse).
- The naive potential `Σ_t|⟨t,x⟩|` (not monotone at constant δ).
- The nested-palindrome amplifier: it boosts the near-isometry but forces `δ` exponentially small — no
  constant-δ amplifier results.

### Candidate machinery (suggestions)
- A **depth-independent quantitative Meshulam / paracontraction rate** for projection-generated families.
- A global **adapted norm / Lyapunov function** for general PD `G` with `poly(r,1/δ)` distortion independent of
  word length (the set-valued invariant body).
- A direct lower bound on `λ_min(Σ_k v_k v_k^⊤)` for full words that uses the EXTRA vectors from repeated
  indices to beat the triangular first-occurrence bound (the explicit missing step).

### What we need back (priority order)
1. **A PROOF** that `γ(w) ≥ 1/poly(r,1/δ)` for all full words (with explicit degree) — OR a **REFUTATION**
   (an explicit constant-`δ` well-conditioned `G` + deficient-block full word `w` with `γ(w)` super-poly small;
   the Hadamard family is the natural candidate). One of these is the goal.
2. Only if (1) genuinely defeats a maximal attempt: the single concrete sub-fact that resists, strictly easier
   than and distinct from PCT (not a relabeling), with your best partial results toward it.
3. Confidence (%) and one-line verdict (closed / refuted / genuinely-stuck-and-why).
