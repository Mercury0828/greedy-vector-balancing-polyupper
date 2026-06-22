# Research-Line Ledger — `greedy-vector-balancing-polyupper`

> **APPEND-ONLY.** Format: guide §5. 🔴 Re-read this ledger + `PROJECT_STATE.md` + frozen artifacts
> before continuing any round — never work from memory. Artifacts/code in English.

---

## ▶ HEADLINE (latest status line on top)

**2026-06-22 — ROUND 3 COMPLETE (audited). STALL round #1; `(★)` ⟺ DA/PC; confidence ~72% (held).**
GPT-5.5-Pro PARTIAL (96%); both audits confirm **all mathematics SOUND**. NET: (i) **P7 sharpened to
`R_loc=r/δ`**; (ii) **P8** exact dual dynamics `p⁺=P_{H^⊥}p+q_B` (+ energy/telescoping/Bessel identities,
numerically exact); (iii) **N3** — the P6/Friedrichs-angle attack (which our R3 brief proposed) is **DEAD**
(P6 governs original flats, not the dynamically projected images `R_j H_j`, whose angles collapse to ~0.003);
(iv) `(★)` ⟺ **Dynamic affine-synthesis (DA) ⟺ Polynomial circulation (PC)** — radial part solved (`r/δ`),
only accumulated curl open; (v) **dual-drift numeric POSITIVE**: `sup_j‖p_j‖` bounded & flat in N (~r/δ),
no √N blowup ⟹ evidence DA/PC's conclusion (hence `(★)`) is TRUE. 🔴 **STALL on provability** (no new
closing lemma; natural attack died). **K_stall=2: Round 4 is the last GPT-Pro round before escalation to a
fresh-context attacker.** Confidence held ~72% (truth-evidence up, proof stuck). **NOTHING frozen as "proved".**

---

**2026-06-22 — ROUND 2 COMPLETE (audited). `(★)` reduced to ONE clean lemma; confidence ~72%.**
GPT-5.5-Pro returned PARTIAL (93%); two independent audits (numeric + analytic line-by-line) confirm **all
claims VALID**. NET: (i) **NEW PROVEN partial theorem P7** — every realizable chamber has a margin-one dual
certificate of norm `O(r²/δ_T²)`; (ii) **`(★)` ⟺ a bounded cyclically-monotone selection** (Prop 2, via
P4-upgrade) — local feasibility done (P7), **integrability is the open core**; (iii) **N2** rank-3
obstruction: no convex `F` linear on the ORIGINAL chambers (kills naive per-chamber patching); (iv) `(★)`
now = the **bounded dual-drift lemma** (`sup_j‖p_j‖≤poly` ⟹ `G(T)≤2·poly`); (v) **direct TV numerics**
(the right object via P4-upgrade) show clean **sub-linear/poly** growth tracking `√d/δ`, no exponential.
Confidence **~72%** (↑5: a proven local theorem + crux is one well-posed lemma + TV evidence). **NOTHING
frozen as "proved".** Next = Round-3 brief (attack the dual-drift lemma via P3′+P6 energy/Friedrichs-angle).

*(Round 1, 2026-06-22: refuted our "unit-vectors-WLOG" reduction; produced P6, P2′, P1-sharp, P4-upgrade,
P3′. See `docs/round1_*`.)*

---

## 1. Frozen model / notation (anchor arXiv:2606.17991, full-text confirmed 2026-06-21)

- Ambient `ℝ^d`, Euclidean `‖·‖`. Finite `T ⊆ S^{d-1}`; `r = dim span(T) ≤ d`.
- **`δ_T`** (Definition 1.1, anchor): `min{ dist(span(U), t) : U⊂T, t∈T∖span(U) }`. Regime of interest:
  `δ_T ≥ c` constant, or `δ_T ≥ 1/poly(d)`.
- **Model = `[-1,1]T` scaled** (Theorem 1.2, anchor): `[-1,1]T := {a·t : a∈[-1,1], t∈T}`; vectors arrive
  adversarially with repetition. `G(T)` = max norm of any greedy sequence. **NOT unit-step-only.**
- **Greedy rule:** at step k pick sign `s_k∈{±1}` so `s_k t_k` has **non-positive** inner product with
  `S_{k-1} = Σ_{i<k} s_i t_i`. Unit-step recursion (sanity): `‖S_k‖² = ‖S_{k-1}‖² − 2|⟨S_{k-1},t_k⟩| + 1`.
- `π_t` = orthogonal projection onto `t^⊥`. Trajectory `y_j = π_{t_j} y_{j-1}`.
- `K_T` = minimal convex `T`-absorbing body; T-projective condition (anchor eq.1, §2):
  `π_t(K)+[-t,t] ⊆ K`. **`G(T) ≤ radius(K_T)`** (anchor Thm 2.4 + Lemma 2.2).
- **Anchor results (confirmed):** upper `G(T) ≤ (2/δ_T)^{d-1}` (Thm 1.2); lower **existence** `∃T: δ_T=δ,
  G(T) ≥ √d/δ` (Lemma 1.4). Tightness **open** (verbatim: "We do not know if the estimate in Theorem 1.2
  is tight.").

## 2. Proven `P*` — "use freely, do NOT re-derive"  (status as of 2026-06-21)

> 🔴 None are yet promoted to unconditional "use freely". Promotion rule (guide §0): P1/P2/P5 → "use
> freely" only AFTER Sim 2 confirms; P4 → only after Phase-0 source-verification (now done for the base).

- `P1` (SHARPENED 2026-06-22) `σ_min(B) ≥ δ_T/√|B|` for independent `B⊆T` (subset-size `|B|`, stronger than
  `√r`). *Source:* dual-row-norm; sharpening confirmed by Round-1 audit (min ratio 1.02). *Status:* **✅
  CONFIRMED — "use freely".** (Sim 2 used the `√r` form: worst ratio 1.008.)
- `P2` `‖x‖ > r/(2δ_T) ⟹ span N(x) ⊊ span T`, `N(x)={t∈T:|⟨x,t⟩|<1/2}`. *Status:* **✅ CONFIRMED (Sim 2) —
  "use freely"** (0 violations, ~2700+ adversarial x/case).
  - `P2′` (REFINED 2026-06-22, Round-1) `‖P_{H(x)} x‖ ≤ q/(2δ_T)`, `H(x)=span N(x)`, `q=dim H(x)`.
    *Status:* **✅ CONFIRMED** (numeric audit ratio 0.71, 0 viol; agent VALID).
- `P6` (NEW 2026-06-22, Round-1) **principal-angle lemma:** for flats `H,K` = spans of subsets of `T`,
  `sin θ(H,K) ≥ δ_T/r` (smallest positive principal angle). *Status:* **✅ CONFIRMED** (numeric: 3768
  pairs, 0 viol, ~3–5× slack — loose, `r` may improve; agent VALID). *Use:* active flats never meet at
  exp-small angles.
- `P3′` (REVIVED 2026-06-22; supersedes the Phase-0 DROP) for unit columns `κ_A ≤ 1/δ_A` (**stated in
  arXiv:2510.20301**), `κ_A` = circuit-imbalance; with Thm 1.1 `n ≤ π d⁴ κ_A` (`d≥4`, non-collinear) ⇒
  one rep per antipodal line gives **`|T| ≤ 2π r⁴/δ_T`** (poly-many directions at constant δ). *Status:*
  **✅ CONFIRMED** (numeric: `κ_A≤1/δ_A` all cases, dep_pairs equality √2; agent VALID, source-backed).
  🔴 NEEDS-HUMAN NH1: eyeball the one-line `κ_A≤1/δ_A` proof in the paper before fully load-bearing.
- `P7` (Round-2 Theorem 1; **SHARPENED 2026-06-22 Round-3 Prop 1**) **polynomial chamber certificate:**
  every realizable chamber `C_s={x:⟨s_i t_i,x⟩≥0}` has a margin-one dual certificate in `cone{s_i t_i}` with
  **`‖p_s‖ ≤ r/δ_T`** (vertex of `P_s` + `r` independent active normals + P1; was `O(r²/δ²)` via
  Carathéodory). *Status:* **✅ proven (analytic VALID both forms) + numerically confirmed** (cert norms 4–6,
  0 violations vs `r/δ`). Inherits NH1 via P3′. *Use:* LOCAL feasibility; integrability open (see `(★)`).
- `P8` (NEW 2026-06-22, Round-3) **exact dual-drift dynamics:** the dual update is an affine projection
  `p⁺=Proj_{P_s}(p)=P_{H^⊥}p+q_B`, `H`=active-face normal span, `q_B`=its affine hull's min-norm point,
  `‖q_B‖≤r/δ_T`; with **energy identity** `‖p⁺‖²−‖p‖²=‖q_B‖²−‖P_H p‖²`, **telescoping**
  `I−Q_NQ_Nᵀ=Σ_j R_j P_{H_j}R_jᵀ`, **Bessel** `Σ_j‖P_{H_j}R_jᵀu‖²≤‖u‖²`. *Status:* **✅ analytic VALID +
  numeric (telescoping err 0.0).** Caveat: the "Proj onto P_s = Proj onto active-face affine hull" step needs
  the non-degenerate-face justification (generic). *Use:* machinery for the dual-drift/DA analysis.
- `P4` `G(T) ≤ radius(K_T)`. *Status:* **base CONFIRMED full-text (anchor Thm 2.4 + Lemma 2.2)** — citable.
  **P4-UPGRADE (2026-06-22, Round-1): the support-function ITERATION identity is now DERIVED & VALID** for
  the recursive projective closure `K_{n+1}=conv ∪_t(π_t K_n+[-t,t])`: `h_{K_{n+1}}(y)=max_t(h_{K_n}(π_t y)
  +|⟨y,t⟩|)` ⇒ `h_{K_n}(y)=max_chains Σ_j‖y_j−y_{j-1}‖`. **Phase-0 caveat (a) RESOLVED — HS1's reduction is
  rigorous; a poly-TV bound (G1) ⟹ `(★)`.** (agent VALID.)
- `P5` absorbing-neighborhood lemma (GPT-Pro): fixed convex `H`-absorbing `K⊆B(0,R_H)` ⟹ `K+rB₂` is
  `H`-absorbing ⟹ a rank-`q` phase grows **additively** (`‖x_out‖ ≤ R_H + ‖x_in‖`, `R_H ≤ (2/δ_T)^{q-1}`).
  *Status:* **candidate — needs a full hand-written proof audit logged here before "use freely"** (do NOT
  treat the external GPT-Pro verdict as a literature fact). One-directional helper; rules out N1.

## 3. DROPPED / refuted

- `P3` DROP (2026-06-21) — **REVERSED 2026-06-22.** The Phase-0 drop was on an incomplete read:
  arXiv:2510.20301 DOES state `κ_A ≤ 1/δ_A` for unit-norm columns. See `P3′` above (REVIVED). 🔴 lesson:
  Phase-0 lit pass + second opinion both missed the unit-column bridge — re-read primary proofs, not summaries.
- **RETRACTED REDUCTION (2026-06-22):** "a norm-maximizing greedy adversary WLOG sends full unit vectors"
  (shipped in `round1_brief.md`, used in `Sim 1`) is **FALSE** (δ=1/4 counterexample, unit-only `G=1` vs
  scaled `G≥4`; numeric A + agent). One-step convexity ≠ dynamic optimality. ⇒ Sim 1's unit-only adversary
  is an incomplete model (scaled steering moves matter); its "no super-poly" stands only as weak negative
  evidence. Not a refutation of `(★)`.
- `N1` (refuted route — do NOT attempt): a fixed-`O(1)`-rank recursive "amplifier" multiplying the norm
  `R ↦ (1+c)R`. Refuted by `P5` (fixed-rank phases are **additive**, not multiplicative). This is the
  sibling A-side's dead gadget — do not assume it amplifies.
- `N2` (refuted route 2026-06-22, Round-2 §3): assigning **one fixed dual certificate per ORIGINAL chamber**
  to build a convex potential `F` linear on those chambers. Refuted at rank 3, constant δ (⟨t_i,t_j⟩=¾,
  δ_T=√(5/14)): margins force `(1−2c)Σw≥3` ⟹ `−½Σw≥3`, impossible (numeric LP infeasible + analytic VALID).
  ⇒ any HS1/HS2 proof MUST refine the chamber fan, vary the gradient inside chambers, or carry HISTORY. Does
  NOT refute `(★)`.
- `N3` (refuted approach 2026-06-22, Round-3): the **P6/Friedrichs-angle charging attack** (charge dual-drift
  reorientations using `sinθ≥δ/r`). DEAD: the interacting spaces are the dynamically projected images
  `R_j H_j=P_{H_N^⊥}⋯P_{H_{j+1}^⊥}H_j`, NOT `T`-spanned — P6 inapplicable; they form an infinite family
  (P3′ count inapplicable) and angles collapse to ~0.003 after one projector (numerically confirmed). The
  energy method stops at `√N`. ⇒ Round-4 must use itinerary-admissibility, NOT angle-transfer. Not a refutation of `(★)`.

## 4. Barriers `B*`

- `B1` (citation corrected 2026-06-22) the right projection-BV reference is **arXiv:1901.07516**
  (Güntürk–Thao, "Unrestricted iterations of relaxed projections… absolute convergence"), NOT 1603.00854
  (Vladimirov, a different object). 1901.07516 gives `Σ‖y_{j+1}−y_j‖^γ ≤ C(geometry)·‖y_0‖^γ` but the
  constant is **geometry-dependent / non-polynomial (root-exponential)** — so it does NOT supply the poly
  bound G1 needs. The poly QUANTITATIVE bound is the open part (G1). **2026 follow-ups confirmed (Round-2
  audit):** arXiv:2601.07002 (polyhedral cones; limiting counterexamples), arXiv:2602.00544 (affine
  subspaces, empty intersection; qualitative boundedness only) — **neither gives poly-in-(r,1/δ).**
- `B2` any construction giving **exponential TV at constant δ** is evidence the truth is the **exponential
  (A) side** — if found, report as a refutation of `(★)`, not a failure (→ human gate, pivot-to-A).

## 5. THE EXACT REDUCED OPEN PROBLEM `(★)` (currently posed)

> `(★)` = "**G(T) = poly(d, 1/δ_T)**" in the anchor's `[-1,1]T` scaled model, for `δ_T ≥ δ` (δ const e.g.
> 1/4, or `≥ 1/poly(d)`). After Round 1, `(★)` reduces to ONE of two crisp missing theorems:
>
> - **G1 (HS1 — poly total-variation, reduction now RIGOROUS via P4-upgrade):** for products of the
>   (`≤2πr⁴/δ_T`, by P3′) hyperplane projections `{π_t}`, whose flats are pairwise angle-separated by
>   `sinθ≥δ_T/r` (P6), prove `sup Σ_j‖y_j−y_{j-1}‖ ≤ poly(r,1/δ_T)·‖y_0‖`. Then P4-upgrade ⟹ `(★)`.
>   Obstacle: BV literature (1901.07516) gives only a non-poly/geometry-dependent constant; the naive
>   per-transition factor `O(r/δ)` × rank-recursion = exponential. Needs a NEW quantitative argument
>   (exploit P3′ poly-many directions + P6 angle separation).
> - **G2 (HS2 — history-dependent summability invariant):** a potential bounding cumulative hidden-component
>   transfer across active-flat switches. The **static** switch lemma is FALSE (`B↦B/δ` example, verified)
>   and switch-counting fails (scaled steering ⇒ arbitrarily small switches). Must charge a quantitative
>   geometric quantity, history-dependently.
> - **HS3 (assemble):** G1 or G2 + substrate ⟹ `G(T) ≤ poly(d,1/δ_T)`.
>
> **OPERATIVE FORM after Round 2 — the single remaining lemma:**
> > **Bounded dual-drift lemma.** `∃ D=poly(r,1/δ_T)` s.t. along any reversed orthogonal-projection
> > trajectory, the dual sequence `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)` (init `‖p_1‖≤R_loc=O(r²/δ²)` via P7,
> > `P_s={p:⟨s_i t_i,p⟩≥1}`) satisfies `sup_j‖p_j‖≤D`. **Then `G(T) ≤ 2D` (reduction VALID, audited).**
> > Equivalently (static): a bounded cyclic-monotone selector `p(y)∈P_{sign(Aᵀy)}` = subgradient field of a
> > convex `F` with `F(y)≤poly·‖y‖`. Local feasibility = P7 (`r/δ`); **global integrability is the open core.**
> > **Round-3 sharpening (P8): `(★)` ⟺ DA ⟺ PC** — `DA: sup_N‖Σ_j P_{H_N^⊥}⋯P_{H_{j+1}^⊥}q_j‖≤poly`
> > (`q_j∈H_j`, `‖q_j‖≤r/δ`); `PC: C(Γ)=Σ∫ρ d⟨a_s,u⟩ ≤ poly·‖y_0‖`. Radial part solved; only accumulated
> > curl open. **Dual-drift numeric (Round-3): `sup_j‖p_j‖` bounded & flat in N ~`r/δ` ⟹ conclusion holds
> > empirically.** ❌ Dead attack `N3`: P6/Friedrichs-angle (P6 doesn't transfer to projected images).
> > ✅ Round-4 attack: itinerary-admissibility / radial-budget Lyapunov — `‖p_j‖` non-increasing on fixed-face
> > sub-runs; growth only at reorientations, which are itinerary-coupled (successive faces share `x_j`); make
> > `C(Γ)` summable via history-dependent `a_s` tied to ρ-monotonicity. NOT angle-transfer.
>
> 🔴 `(★)` is ATTACKER-originated (web GPT-5.5-Pro), NOT Claude. Pivot trigger if refuted (TV provably
> exponential at constant δ ⟹ truth is A-side). **Routing:** HS1 reduction rigorous (P4-upgrade) + Theorem 1
> ⇒ HS1/dual-drift is the live route; HS2 folded into the same dual-drift object.

## 6. Confidence trend (% that the B-side / `(★)` is TRUE; dated)

| Date | Conf. | Basis |
|---|---|---|
| 2026-06-22 (seed) | ~65% | GPT-5 Pro external adjudication; P5 rigorously kills the sibling's literal amplifier route. NOT panel-validated. |
| 2026-06-21 (lit scan) | ~65% (held) | No scoop; anchor machinery confirmed; P3 dropped (cost-free); support-fn iteration absent (HS1 needs derivation, HS2 intact). Awaiting Sim 1. |
| 2026-06-21 (de-risk) | ~65% (held) | Sim 1 found **no super-poly growth** (falsifier not triggered) → no death-evidence against B; but the heuristic adversary under-explores amplitude (did not reach √d/δ), so this is **negative evidence, not a poly proof**. Sim 2 confirmed P1,P2. Net: crux still genuinely open; confidence unchanged, not raised (honesty rail: de-risk ≠ proof). |
| 2026-06-22 (Round 1) | ~67% (↑2) | GPT-Pro PARTIAL, both audits VALID. New verified substrate (P6 angle-sep, P2′, P1-sharp, P4-upgrade ⇒ HS1 rigorous, P3′ ⇒ poly-many directions) makes an exponential construction structurally harder and turns the crux into a clean finitary geometry problem (G1). BUT the core poly-TV/summability question is untouched and BV-lit gives exponential — progress is reduction-clarity, not proof. Modest uptick only. |
| 2026-06-22 (Round 2) | ~72% (↑5) | GPT-Pro PARTIAL (93%), both audits VALID. Proven NEW local theorem P7 (`O(r²/δ²)` certificate); `(★)` ⟺ bounded dual-drift lemma (one clean well-posed lemma) with a concrete P3′+P6 attack; direct TV numerics show sub-linear/poly growth tracking `√d/δ`, no exponential. Tempered: global integrability unproven, N2 + 2026 BV counterexamples show real subtlety, TV is a lower-bound search. Not a proof. |
| 2026-06-22 (Round 3) | ~72% (held) | GPT-Pro PARTIAL (96%), all math SOUND. **STALL #1:** P7 sharpened to `r/δ` + P8 dynamics, but the P3′+P6 attack DIED (N3: P6 doesn't transfer to projected images) and the round is net refutation+reformulation (`(★)`⟺DA/PC). Counterweight: dual-drift numeric `sup_j‖p_j‖` bounded & flat in N ~`r/δ` ⟹ conclusion likely TRUE. Two-sided ⟹ held. K_stall=2: Round 4 = last before escalation. |

---

## 7. Phase-0 de-risk results (frozen 2026-06-21)

**Sim 1 — kill test** (`code/sim1_killtest.py`, seed=20260621, δ≥0.25, `code/sim1_results.json`):
adversarial `max‖S_k‖` vs d (best over families: gadgets / rand-indep+opt / dep-pairs / near-dep-chain):

| d | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| best `max‖S_k‖` | 1.41 | 2.00 | 2.44 | 2.99 | 3.62 | 4.90 | 5.24 | 5.05 | 4.09 |
| `√d/δ` (anchor lower) | 5.66 | 6.93 | 8.0 | 8.94 | 9.80 | 10.58 | 11.31 | 12.0 | 12.65 |
| `(2/δ)^{d-1}` (anchor upper) | 8 | 64 | 512 | 4096 | 3·10⁴ | 3·10⁵ | 2·10⁶ | 2·10⁷ | 1·10⁸ |

- Growth fit: log-log slope ≈ **0.82** (sub-linear polynomial); semilog slope ≈ 0.15. **Clearly polynomial;
  no exponential signature.** FALSIFIER (constant-δ super-poly family) **NOT triggered.**
- **Simulator validated:** on orthonormal `T` (δ_T=1) the adversary reaches **exactly √d** (optimal) for
  d∈{2,4,8,16,25} → greedy/adversary mechanics correct.
- 🔴 **Honest limitation:** the generic search did NOT reach the anchor's proven `√d/δ` worst case (the
  `1/δ` amplification of the S^{2d-1} gadget was not constructed by random/structured search). So Sim 1 is
  decisive on the **qualitative** poly-vs-exp question (poly, no exp) but **does not certify the exponent**;
  it is **negative evidence against the exponential A-side, not a proof of the polynomial B-side.**

**Sim 2 — lever check** (`code/sim2_levers.py`, seed=20260622, `code/sim2_results.json`):
**P1 holds** (worst σ_min/bound ratio = 1.008 ≥ 1; 0 violations) and **P2 holds** (0 violations above the
`r/(2δ_T)` threshold; ~2700+ adversarial `x` per case) across all families and d∈{2,4,6,8}. → P1,P2 "use freely".
