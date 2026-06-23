# Round-9 RESPONSE — GPT-5.5-Pro (FINAL fresh-context, verbatim) + orchestrator header

> **Orchestrator header.** FINAL fresh-context decisive round, owner-relayed, 2026-06-22/23. TWO answers
> (complementary; Response 2 generalizes Response 1 + adds a basis-level reduction). **Neither closes `(★)`**
> (the MANDATE's primary ask), but BOTH deliver genuinely NEW content (not the prior "relabeling"):
> - **NEW PROVEN THEOREM (positive):** `(★)` holds for **root-system / reflection-closed `T`** (incl. all
>   GRAPHICAL `t=(e_u−e_v)/√2`), via a global potential `Φ(x)=½Σ_{u∈R}|⟨u,x⟩|` (pair `u` with `R_t u`,
>   `P_t=(I+R_t)/2` + convexity) ⟹ `G(T) ≤ |R|/2` (graphical: `≤ r(r+1)/2`), even at `δ≈r^{-1/2}`. First clean
>   global-potential closure of an infinite subclass at small δ → candidate **P14**.
> - **NEW SIMPLIFICATION of the open core:** the difficulty is ALREADY present for a SINGLE WELL-CONDITIONED
>   BASIS — the **Basis Switching Theorem (BST)**: adversarial coordinate descent on `½c^T G c` with switched
>   residual targets, `(G^{-1})_{ii}≤δ^{-2}`, claim `sup_k c_k^T G c_k ≤ poly(r,δ^{-1})`. NO chambers /
>   circuits / oriented matroids needed (the 8-round edifice was over-complicated). Equivalent Bessel form:
>   `(★) ⟺ max_ε‖Σ ε_j v_j‖ ≤ poly` for projection-generated Bessel sequences (`Σ v_j v_j^T ⪯ I`).
> - **Refutation program (open):** encode relaxed/contraction projections via exact projections (dilation);
>   a constant-δ lift of an exponential contraction orbit would refute `(★)`. Not achieved.
> - **Confidence DOWN:** both put `(★)`-true at **~65–66%** (was ~72%) — honest sobering update.
> Triage: a real new theorem (root systems) + a genuine simplification (BST, basis-level) + a clean new
> kill-test (BST is directly simulable at large r). Audit + the BST adversarial numeric are the next actions.

---

## RESPONSE 1 (verbatim) — graphical root systems have a quadratic bound

**Verdict:** no valid proof/refutation of full `(★)`; closed a distinct infinite subclass in the
inverse-poly-δ regime.

**Theorem.** `G=(V,E)` connected on `n` vertices, `T_G={(e_u−e_v)/√2 : {u,v}∈E} ⊂ 1^⊥ ⊂ ℝ^n`,
`r=dim span T_G=n−1`. Then `δ_{T_G} ≥ √(2/n)`, and every projection trajectory `x_k=P_{t_k^⊥}x_{k-1}` has
`Σ_{k≥1}‖x_k−x_{k-1}‖ ≤ C(n,2)·‖x_0‖`, hence (F5) `G(T_G) ≤ C(n,2) = r(r+1)/2`. So `(★)` holds, quadratically,
for every graphical config even though `δ_{T_G} ≍ r^{-1/2}`.

*Proof of TV bound.* Dispersion potential `Φ(x)=Σ_{p<q}|x_p−x_q|`. Projection on edge {u,v} replaces
`(x_u,x_v)` by `(m,m)`, `m=(x_u+x_v)/2`. The {u,v} term drops by `|x_u−x_v|`; for `w∉{u,v}`, convexity
`|a−x_w|+|b−x_w| ≥ 2|m−x_w|` ⟹ no other term increases ⟹ `Φ(x)−Φ(P_t x) ≥ |x_u−x_v|`. Since
`‖x−P_t x‖=|⟨t,x⟩|=|x_u−x_v|/√2`, `Φ(x)−Φ(P_t x) ≥ √2·‖x−P_t x‖`. Telescoping ⟹ `Σ‖x_k−x_{k-1}‖ ≤
Φ(x_0)/√2 ≤ C(n,2)‖x_0‖`. ∎
*Proof of δ bound.* For `U⊆T_G` = edges of subgraph `H`, components span the zero-sum spaces. If
`t_{uv}∉span U`, `u∈A`, `v∈B` (distinct components); the ⊥ component is `(1_A/|A| − 1_B/|B|)/√2`, so
`dist²=½(1/|A|+1/|B|) ≥ ½·4/n = 2/n`. ∎

*Why it does not extend:* every projection is literally 2-coordinate averaging; the majorization
`|a−c|+|b−c|≥2|m−c|` is special. General projections lack this. Even `Φ_T(x)=Σ_t|⟨t,x⟩|` FAILS at constant δ:
in ℝ², directions at 0°,30°,60° (δ=1/2), `x=(−ε,M)`, `M≫ε>0`: project onto `e_1^⊥` ⟹ `x'=(0,M)`, but
`Φ_T(x)−Φ_T(x') = ε(1−cos30°−cos60°) < 0`. So no generic triangle-inequality argument hides here.

Also pushed: recursive multiplicative constructions need exp-small Gram–Schmidt residuals (δ collapses
exponentially); circuit-imbalance controls lifts but not temporal splitting/cancellation; random-flag/volume
potentials incur a per-rank conditioning factor (exp depth); complete independent sweeps contract poly but an
arbitrary itinerary can spend unbounded time in changing proper flats. Known unrestricted finite-variation
results (Güntürk–Thao 1901.07516) give configuration-dependent constants, not poly-(r,1/δ).
**Verdict:** genuinely stuck; graphical case `G(T)≤r(r+1)/2`; no general replacement for the majorization
potential, no constant-δ amplifier. **Confidence: 99% in the theorem; 66% that full `(★)` is true.**

---

## RESPONSE 2 (verbatim) — the breakpoint is already a single well-conditioned basis

No valid proof/refutation of `(★)`. Precise earlier breakpoint: the unresolved phenomenon already occurs when
`T` is merely a single well-conditioned basis. Circuits, large arrangements, oriented-matroid complexity are
NOT required.

**§1 Homogeneous reformulation.** `P_t=I−tt^⊤`, `R_j=P_{t_j}…P_{t_1}`, `y_j=R_j y_0`; `v_j=R_{j-1}^⊤ t_j=
P_{t_1}…P_{t_{j-1}}t_j`. Then `‖y_j−y_{j-1}‖=|⟨v_j,y_0⟩|`, so
`sup_{‖y_0‖≤1} Σ_j‖y_j−y_{j-1}‖ = max_{ε∈{±1}^n} ‖Σ_j ε_j v_j‖` (1). Exact Bessel
`Σ_j v_j v_j^⊤ = I − R_n^⊤ R_n ⪯ I` (2) (since `R_{j-1}^⊤R_{j-1}−R_j^⊤R_j = v_j v_j^⊤`). So F5 ⟺ a polynomial
**unconditionality** bound `max_ε‖Σ ε_j v_j‖ ≤ poly(r,δ^{-1})` (3) for these special projection-generated
Bessel sequences. (2) alone is insufficient: a generic Bessel sequence has signed sums of order `√n`.

**§2 The obstruction for a basis.** `T={t_1..t_r}`, `A=[t_i]`, `G=A^⊤A`; `dist(t_i,span(T∖t_i))²=1/(G^{-1})_{ii}`
so `(G^{-1})_{ii}≤δ^{-2}` (4). Reading the signed sum backwards ⟹ affine maps `p↦P_{t_i}p+ε t_i`; in
coordinates `p=Ac`: `c_{k+1}=c_k+(ε_k−(Gc_k)_{i_k})e_{i_k}`, `ε_k∈{±1}` (5) — adversarial exact coordinate
descent on `f(c)=½c^⊤Gc` with the selected residual coordinate switched ±1. Energy
`‖Ac_{k+1}‖²=‖Ac_k‖²+1−(Gc_k)_{i_k}²` (6).
> **Basis Switching Theorem (BST).** For every PD correlation `G` with `(G^{-1})_{ii}≤δ^{-2}`, every orbit (5)
> from `0` has `sup_k c_k^⊤ G c_k ≤ poly(r,δ^{-1})`.
A counterexample to BST already destroys the projection-trajectory claim, no circuits. None of F1–F4 currently
proves BST.

**§3 What conditioning proves.** One independent sweep (`t_1..t_s` each once): `L` unit-lower-triangular with
`L+L^⊤=H+I⪰I` ⟹ `‖L^{-1}‖₂≤2` (7); `‖Aα‖²=α^⊤Hα=2α^⊤ε−‖α‖²=s−‖α−ε‖²≤s` (8) — ends inside radius `√s` (no δ
needed). Homogeneous sweep contracts: `Σ_{sweep}‖x_j−x_{j-1}‖² ≥ δ²/s³·‖x_0‖²` (9). General block of length L
containing a spanning s-set: `E:=Σ_block‖x_j−x_{j-1}‖² ≥ δ²/(4s²L)·‖P_{span T_block}x_0‖²` (10). So a
polynomial bound on full-rank RETURN TIME `L` ⟹ poly contraction ⟹ done. But `L` is adversarially unbounded;
applying (10) rank-by-rank multiplies losses → exponential. **That is the precise temporal obstruction.**

**§4 Why static angle info doesn't bridge it.** For `I⊆T`, `‖P_{H_I}x‖≤(|I|/δ)max_{t∈I}|⟨t,x⟩|` (11) — but
along a trajectory each residual is at a different iterate; replacing by start-of-block residuals costs
`‖x_k−x_0‖≤√k(Σ‖x_j−x_{j-1}‖²)^{1/2}` = the `√L` in (10). Known unrestricted-product proofs propagate residual
bounds through subspace intersections, raising a transversality parameter to the #subspaces / flag depth — F4
gives a poly angle at one level but the machinery exponentiates it.

**§5 Basis-level survivor obstruction.** Partition coords into active `J`, survivors `K`;
`h_J(c_K)=−G_{JJ}^{-1}G_{JK}c_K`, `u_J=c_J−h_J(c_K)` ⟹ `(Gc)_J=G_{JJ}u_J` (12). While only `J` updates, `c_K`
fixed and `u_J` runs the lower-dim process with Gram `G_{JJ}`. Accumulation comes only from CHANGING `J`, which
changes the Schur complement of the survivor; from rank 5 the survivor can be multidim and the return maps need
not share a point coboundary.
> **Quantitative switched-survivor lemma:** arbitrary switching among the principal-submatrix processes in (12)
> has a common invariant family of convex cross-sections of `G`-radius `poly(r,δ^{-1})`.
This is the basis specialization of CORE (not an artifact of chambers/circuits).

**§6 A class where `(★)` DOES hold (generalizes Response 1).** If `R⊂S^{r-1}` is finite, centrally symmetric,
`⊇T`, invariant under every reflection `R_t=I−2tt^⊤` (`t∈T`), then `Φ(x)=½Σ_{u∈R}|⟨u,x⟩|`: since `P_t=(I+R_t)/2`,
pair `u,R_t u`; convexity ⟹ all pairs but `±t` don't increase, `±t` drops by `|⟨t,x⟩|` ⟹
`Φ(x)−Φ(P_t x)≥|⟨t,x⟩|=‖x−P_t x‖` (13) ⟹ `Σ‖x_j−x_{j-1}‖≤Φ(x_0)≤(|R|/2)‖x_0‖` (14) ⟹ `G(T)≤|R|/2`. Proves
`(★)` for every `T` embedded in a reflection (root) system of polynomial size. Graphical/incidence case
sharper via `D(x)=Σ_{i<j}|x_i−x_j|` ⟹ `Σ‖x_k−x_{k-1}‖ ≤ (n−1)√n/√2·‖x_0‖` (15).

**§7 A concrete (open) refutation program.** Relaxed projections via exact ones: `n_t=√λ t+√(1−λ)e` ⟹
`P_e P_{n_t}(x,0)=((I−λtt^⊤)x,0)` (16); every `0⪯M⪯I` is a compression of an orthogonal projector `Π_M` (17).
So an exponential time-varying positive-contraction orbit, IF liftable to exact projections with
`δ_T≥d^{-O(1)}` (18), would refute `(★)`. Known recursive-averaging lower bounds don't yet verify (18) (their
dilation normal families have uncontrolled distance property). A narrower certificate: a periodic affine word
`F_W(z)=Q_W z+b_W` with `‖(I−Q_W)^† b_W‖` super-poly at constant δ. None emerged.

**Missing theorem (no discrepancy language):**
> **QBV — Quantitative bounded-variation for well-separated projections.** If `T⊂S^{r-1}` has `δ_T≥δ`, then
> `sup_{n,(t_j)} sup_{‖x‖≤1} Σ_j ‖P_{t_j}…P_{t_1}x − P_{t_{j-1}}…P_{t_1}x‖ ≤ poly(r,δ^{-1})`.
Qualitative BV / bounded-orbit results are known; existing proofs build an adapted norm via recursive
intersection geometry with exponentially-compounded Euclidean distortion. Missing = a QUANTITATIVE adapted norm
(≡ the set-valued survivor cross-sections of CORE) with distortion degree independent of flag depth.

**Verdict: PARTIAL + PRECISE BREAKPOINT.** `(★)` open; first unresolved case = adversarial affine coordinate
descent for one well-conditioned basis (BST). **Confidence: 95% in the reductions/breakpoint; 65% that `(★)`
is ultimately true.**

Refs: 2606.17991 (anchor); 1901.07516 / Güntürk–Thao PAFA; 2602.00544 (affine orbits).
