# Round-9 AUDIT — new theorem P14 (freeze); core simplified to BST; BST ≡ quantitative Meshulam

> Two independent audits of `docs/round9_response.md`: (1) orchestrator numeric (`code/round9_bst_killtest.py`
> → `round9_results.json`); (2) fresh-context analytic agent (re-derived all identities; reran BST to r=50
> with structured stress; ran down the literature pointer). **Bottom line: all five claims' math is CORRECT.
> Neither closes `(★)`, but the round delivers (i) a freezable NEW theorem (P14, root systems), (ii) a genuine
> SIMPLIFICATION of the core to the basis level (BST), and (iii) the decisive literature framing — BST ≡ a
> quantitative (depth-independent) Meshulam boundedness theorem. Confidence ↑ to ~74%.**

## Classification

### PROVEN — freeze
- **P14 (NEW) — root-system / reflection-closed `(★)`.** If `R⊂S^{r-1}` is finite, centrally symmetric, `⊇T`,
  invariant under every reflection `R_t=I−2tt^⊤` (`t∈T`), then `Φ(x)=½Σ_{u∈R}|⟨u,x⟩|` satisfies
  `Φ(x)−Φ(π_t x) ≥ ‖x−π_t x‖` (pair `u` with `R_t u`; `π_t(R_t u)=π_t u` so `|⟨u,x⟩|+|⟨R_t u,x⟩| ↦ |⟨u+R_t u,x⟩|`
  never increases; `±t` drops by `|⟨t,x⟩|`) ⟹ `Σ‖steps‖ ≤ Φ(x_0) ≤ (|R|/2)‖x_0‖` ⟹ **`G(T) ≤ |R|/2`**.
  Specializes to GRAPHICAL `T_G={(e_u−e_v)/√2}`: `δ_{T_G} ≥ √(2/n) ≍ r^{-1/2}`, `G(T_G) ≤ r(r+1)/2` (via the
  dispersion potential `D(x)=Σ_{i<j}|x_i−x_j|`). *Status:* **✅ analytic VALID (both forms, line-by-line) +
  numeric (TV ≤ C(n,2), 0 violations).** First clean global-potential closure of an infinite subclass at small
  δ. 🔴 Caveat: closes `(★)` only for `T` inside a **polynomial-size** root system; the value is the TECHNIQUE
  (a working global potential at small δ), not general coverage. Non-extension confirmed: the naive `Σ_t|⟨t,x⟩|`
  strictly increases under a projection (R² 0°/30°/60° example).

### THE CORE — SIMPLIFIED (real progress, not relabeling)
- **BST (Basis Switching Theorem) is the genuine, basis-level core.** For a basis `T={t_1..t_r}`, `G=A^⊤A`,
  `(G^{-1})_{ii}≤δ^{-2}`: the orbit `c_{k+1}=c_k+(ε_k−(Gc_k)_{i_k})e_{i_k}` (ε_k∈{±1}) has
  `‖p_k‖²=c_k^⊤Gc_k`, `‖p_{k+1}‖²=‖p_k‖²+1−(Gc_k)_{i_k}²`; **BST:** `sup_k c_k^⊤Gc_k ≤ poly(r,1/δ)`. **`(★)`
  (projection-trajectory TV) ⟺ BST** (analytic VALID: identities (i)–(ii), the Bessel form
  `Σ v_j v_j^⊤=I−R_n^⊤R_n⪯I`, `sup-TV=max_ε‖Σε_j v_j‖`). 🔴 **This SUPERSEDES the chamber/CORE framing as the
  working statement** — strictly lower complexity (one r×r PD matrix + a scalar recursion, NO chambers/
  circuits/oriented-matroids), and the obstruction SURVIVES (still open, still the temporal/return-time
  difficulty). Satisfies the no-relabeling mandate (it is simpler, not just renamed).
- **§3 sub-results VALID (open reductions):** one independent sweep ends inside radius `√s` (no δ needed);
  a **polynomial full-rank RETURN-TIME bound ⟹ `(★)`** (eq 10), but the return time `L` is adversarially
  unbounded and rank-by-rank application compounds to exponential — the precise temporal obstruction.

### DECISIVE LITERATURE FIND — BST ≡ quantitative Meshulam
- **BST is exactly a QUANTITATIVE, depth-independent version of Meshulam's relaxed-projection boundedness
  theorem.** arXiv:2602.00544 (Meshulam-lineage, 2026) proves the QUALITATIVE result — orbits of relaxed
  projections `(I−λP)` onto a finite family of affine subspaces are BOUNDED even with empty intersection — but
  its constant `C=(τ+D)/(1−√(1−λ(2−λ)·κ₊^{−2(ℓ−1)}))` is **EXPONENTIAL in the number of subspaces ℓ (= flag
  depth)**. So the literature supplies the framework + the exact gap: **make Meshulam's constant
  poly-in-depth.** (Kaczmarz/POCS/coordinate-descent convergence theory is about decay TO the solution, not the
  adversarial driven-away boundedness BST needs — not directly applicable.)

### Refutation program (open, not evidence of falsity)
- §7 dilation (relaxed/contractive projections as compressions of exact projectors) — algebra VALID; a
  constant-δ lift of an exponential contraction orbit would refute `(★)`, but the binding condition (`δ_T ≥
  d^{-O(1)}` for the lifted normals) is unmet and δ inflates uncontrollably. Genuine open route; NOT current
  evidence `(★)` is false.

## Numerics (strongest `(★)`-evidence to date)
- **BST kill-test** (`code/round9_bst_killtest.py`): adversarial coordinate descent at constant δ≈0.25,
  `sup‖p‖` vs r=4…30 grows as **√r** (log-log slope **0.454**, semilog 0.030); ≪ r/δ, ≪ r²/δ², ≪ `(2/δ)^{r-1}`.
  Auditor independently reran to **r=50** + structured staircase stress at δ=0.25: same clean √r (slope 0.453),
  **no super-poly anywhere.** This is the cleanest, highest-rank probe yet (prior chamber sims stalled at d≤10),
  on the solver-identified true core ⟹ strong support for BST/`(★)`.
- Root-system theorem numerically confirmed (TV ≤ C(n,2), 0 violations).

## Confidence
**~72% → ~74%** (B-side / `(★)` true). The BST-to-r=50 √r evidence (clean, robust to structured stress, on the
true core, with a structural reason — energy gain `1−⟨t,p⟩²`) outweighs the solvers' deeper-understanding
pessimism (65–66%, a prior not evidence). Auditor independently lands ~75–78%. Tempered: BST poly-rate is
unproven; the dilation refutation route is open (not closed off). Modest uptick. 🔴 Nothing newly frozen as
"proved" beyond **P14**.

## Next (recommended; owner-preferred direction, audit-endorsed)
**Round 10 = a targeted fresh-context attack on BST** — the cleanest target we have: a fully-specified r×r
problem, large-r-simulable, with an EXACT literature precedent (make Meshulam's constant depth-independent).
Ask: prove `poly(r,1/δ)`-in-depth boundedness for the affine IFS `c_{k+1}=c_k+(ε−(Gc)_i)e_i`, i.e. a
depth-independent Meshulam/paracontraction constant for projection-generated families — or refute via the
dilation program. Closure mandate stands. Brief: `docs/round10_brief_bst.md`. Also: a dedicated lit pass on
"quantitative/polynomial Meshulam", paracontraction rates, de Pierro/Bauschke POCS depth dependence.

## NEEDS-HUMAN
NH1–NH6 (prior); the deep step now = a depth-independent (poly) Meshulam boundedness constant for
projection-generated affine families (= BST).
