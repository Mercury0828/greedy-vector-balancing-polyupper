# Literature Kill-Scan Report — `greedy-vector-balancing-polyupper`

**Date:** 2026-06-21 · **Scanner:** Claude Code (orchestrator) · **Phase:** 0
**Verdict (this report):** see §6. **Independent second opinion:** `lit/SECOND_OPINION.md`.

> Per guide §Literature. All live lookups via WebSearch/WebFetch on 2026-06-21. Every query is logged
> with hit/miss. 🔴 Honesty rail: if a load-bearing lookup had FAILED, the verdict could not be GREEN.
> All load-bearing lookups SUCCEEDED this run.

---

## 1. Mandatory query list (guide §Literature) — execution log

| # | Query | Status | Key hits |
|---|---|---|---|
| Q1 | `Czerwiński Dadush greedy vector balancing arXiv 2606.17991` | ✅ HIT | anchor abs+HTML; confirmed authors, bound, date |
| Q2 | `SODA 2027 call for papers submission deadline double blind` | ✅ HIT | SODA27 SIAM page; deadline 2026-07-09 (UTC-12) |
| Q3 | `SODA 2027 ... anonymous submission lightweight double-blind author` | ✅ HIT | lightweight double-blind confirmed; soda27.hotcrp.com |
| Q4 | `online vector balancing greedy 2026 polynomial bound delta_T tightness` | ✅ HIT | anchor only for the 2026 finite bound; older Bansal–Jiang online VB context |
| Q5 | `Bárány Lim balancing games unbounded sets Chooser Pusher arXiv 2512.03273` | ✅ HIT | confirmed V-closed model; distinct from T-absorbing |
| Q6 | `SODA 2027 accepted papers list discrepancy vector balancing` | ✅ HIT (no list) | SODA27 accepted list not yet published (future conf) — no scoop visible |
| Q7 | full-text fetch `arXiv:2606.17991` abs (version history) | ✅ HIT | **v1 only, 2026-06-16; no v2/v3** |
| Q8 | full-text fetch `arXiv:2606.17991` HTML (load-bearing claims) | ✅ HIT | δ_T def, [-1,1]T model, Thm 1.2, Lemma 1.4, tightness quote, K_T |
| Q9 | full-text fetch `arXiv:2510.20301` | ✅ HIT | bound `O(d⁴·κ_A)`, κ_A=circuit imbalance; **no κ_A↔δ_T relation** |
| Q10 | full-text fetch `arXiv:1603.00854` | ✅ HIT | Vladimirov, "Continuous products of matrices"; qualitative, not projection-specific |

**Coverage floor:** arXiv faces math.CO / math.MG / cs.DS / cs.CG indirectly via the anchor's cs.CG
listing and neighbor hits; 2026 listings reached through Q1/Q4/Q5; anchor authors' follow-ups checked
via Q7 (version history) and Q9 (Dadush 2025 companion); SODA accepted lists via Q6 (none for 2027 yet).
No paid/DB-only sources required. **No live lookup failed.**

---

## 2. Anchor — arXiv:2606.17991 (FULL-TEXT verified 2026-06-21)

"Greedy Vector Balancing" — Czerwiński, Dadush, Ergen, Ghosh, Lasota, Orlikowski. Submitted **2026-06-16
(v1; the ONLY version)**. cs.CG, 21 pp.

| Load-bearing claim | Location | Verbatim / confirmed | Status |
|---|---|---|---|
| `δ_T` definition | Definition 1.1 | `min{dist(span(U), t) : U⊂T, t∈T∖span(U)} ≥ δ` | ✅ matches guide §Notation |
| Scaled model + Thm 1.2 | Theorem 1.2 | "G(T) = max norm of any greedy sequence for **[-1,1]T := {a·t : a∈[-1,1], t∈T}**. Then G(T) ≤ (2/δ_T)^(d-1)." | ✅ **[-1,1]T scaled model confirmed** |
| Greedy rule | Thm 1.2 / abstract | s_k∈{±1} chosen so s_k·t_k has non-positive inner product with Σ_{i<k} s_i·t_i | ✅ matches |
| Lower bound | Lemma 1.4 | "For every d∈ℕ₊, δ∈(0,1) there **is** a set T⊆S^(2d-1) with δ_T=δ and G(T) ≥ √d/δ." | ✅ **EXISTENCE only**; no per-T claim; **no `G({0,1}^d)≥d^{d/2}`** |
| Tightness open | Introduction | **"We do not know if the estimate in Theorem 1.2 is tight."** | ✅ **verbatim re-confirmed** |
| `G(T) ≤ radius(K_T)` | Thm 2.4 + Lemma 2.2 | T-projective set `K_T^δ ⊆ B^m(R_d)`, `R_d=(2/δ_T)^(d-1)`; T-projective ⟹ T-absorbing (Lemma 2.2) | ✅ **P4-base IS in the paper** |
| Support-function ITERATION identity `h_{K_n}(y)=max_t(h(π_t y)+\|⟨y,t⟩\|)` | — | **NOT FOUND.** Paper uses the T-projective condition `π_t(K)+[-t,t] ⊆ K` (eq. 1, §2). | ⚠️ **OUR reconstruction, confirmed absent** |

**Conclusions:** (a) **No scoop** — single version, abstract claims only `(2/δ_T)^{d-1}` upper and
`Ω(√d/δ_T)` lower, explicitly leaves the gap open. (b) The model/notation/`δ_T`/`G(T)≤radius(K_T)`
substrate is confirmed → **P4-base citable**. (c) The support-function iteration is **our
reconstruction, not in the paper** → HS1 needs an explicit derivation from the `π_t(K)+[-t,t]⊆K`
machinery, OR run HS2 (which does not use it). This is exactly the start_up-flagged caveat (a).

---

## 3. arXiv:2510.20301 — column-number / circuit-imbalance (FULL-TEXT verified 2026-06-21)

"Excluding a Line Minor via Design Matrices and Column Number Bounds for the Circuit Imbalance Measure"
— Dadush, Eisenbrand, Pinchasi, Rothvoss, Singer. Submitted **2025-10-23**.
- Bound: **`n ≤ O(d⁴·κ_A)`** for pairwise non-collinear columns.
- `κ_A` = **circuit-imbalance measure** of `A` (real analogue of Δ-modularity; `κ_A ≤ Δ_A` for integer `A`).
- **The paper gives NO relation between `κ_A` and a min-distance-to-span parameter (`δ_T`).**

➡️ **P3 is DROPPED.** There is no source relation letting `κ_A ≤ 1/poly(δ_T)` for our `T`. Fact-3 does
not apply. (Per guide §Theory this costs the main result nothing: HS1/HS2 do not depend on P3.) Note:
Dadush co-authors both this and the anchor — checked, it is a *companion* tool paper, **not** a follow-up
resolving greedy-VB tightness. No scoop.

---

## 4. arXiv:1603.00854 — products of matrices (FULL-TEXT verified 2026-06-21)

"Continuous products of matrices" — A. Vladimirov. Submitted **2016-03-02**. Establishes convergence
conditions (LCP/RCP) for products `M₁M₂…M_k`, `M_i` from a finite set Σ. **Qualitative** (convergence),
**not** a quantitative polynomial rate, and **not specifically about orthogonal projections** onto
hyperplanes / trajectory total variation.

➡️ **B1 is at best weakly supportive.** It does NOT directly supply "qualitative bounded variation of
finite orthogonal-projection trajectories" in the form HS1 wanted, and it is qualitative only. This is
exactly start_up-flagged caveat (b). **HS1 does not strictly require B1; HS2 does not use it at all.** A
dedicated source for projection-trajectory BV (if any) remains an open lit item — flag, not a blocker.

---

## 5. Neighbor / scoop check

| Work | Confirmed | Bearing |
|---|---|---|
| Bárány–Lim 2512.03273 "Balancing games on unbounded sets" | V-closed set: `t∈T, v∈V ⟹ t+v∈T or t−v∈T`; Pusher/Chooser threshold | **V-closed ≠ greedy T-absorbing** (either-sign-may-stay vs inner-product-chosen-sign). Different model; does not bear on our δ_T-Euclidean bound. Cite + distinguish. GREEN. |
| Bansal–Jiang "Online VB & geometric discrepancy" (1912.03350) | older randomized/stochastic online VB | different (non-greedy/stochastic) regime; cite as lineage. GREEN. |
| SODA 2027 accepted list | not yet published (future conf) | re-scan at convergence + submission. |

**No paper (anchor v2/v3 or 2026 follow-up) resolves the tightness in either direction.** No scoop.

---

## 6. VERDICT (pre-frozen kill criteria, guide §Literature)

**Literature axis: NOT RED — no scoop, load-bearing anchor machinery confirmed.**

- **RED criterion (i) scoop:** NOT triggered — anchor is v1-only and explicitly open; no follow-up.
- **YELLOW flags (load-bearing, carried forward):**
  - `(Y1)` Support-function **iteration identity is OUR reconstruction, confirmed absent** from the
    anchor → HS1 must derive it from `π_t(K)+[-t,t]⊆K`, or use **HS2** (primary, safer route).
  - `(Y2)` **P3 dropped** — no `κ_A↔δ_T` relation in 2510.20301.
  - `(Y3)` **B1 weak** — 1603.00854 does not cleanly supply the projection-trajectory BV; HS2 unaffected.
- **GREEN preconditions met on the literature axis:** model/`δ_T`/`G(T)≤radius(K_T)` confirmed; no scoop.

**The overall Phase-0 GREEN/YELLOW/RED verdict is gated on Sim 1** (the kill test): literature alone
cannot turn the project GREEN — the de-risk sims decide. The YELLOW flags Y1–Y3 do **not** kill the
project because HS2 (resting only on the numerically-checkable P1/P2) is intact and was pre-designated
co-primary. → Proceed to Sim 1 / Sim 2; final verdict folds in their results + the second opinion.

---

## Sources
- Anchor: https://arxiv.org/abs/2606.17991 · https://arxiv.org/html/2606.17991
- Column number: https://arxiv.org/abs/2510.20301
- Products of matrices: https://arxiv.org/abs/1603.00854
- Bárány–Lim: https://arxiv.org/abs/2512.03273
- SODA27: https://www.siam.org/conferences-events/siam-conferences/soda27/ · https://soda27.hotcrp.com/
