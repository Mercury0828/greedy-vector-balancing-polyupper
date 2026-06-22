# Round-1 AUDIT — independent adversarial verdict + classification

> Two independent audits of `docs/round1_response.md`: (1) orchestrator numeric checks
> (`code/round1_audit_checks.py` → `code/round1_audit_results.json`, seed 20260622); (2) fresh-context
> adversarial audit agent (web-enabled, primary sources). Both ran blind to each other.
> **Bottom line: every load-bearing claim VALID. No FATAL against `(★)` (no counterexample to the
> conjecture). One reduction in our own brief is refuted (correction, not kill). Real forward progress:
> 4 new/upgraded substrate lemmas + P3 revived.**

## Classification (guide §3: FATAL / GAP / MINOR)

### FATAL — but to OUR BRIEF / method, not to `(★)`
- **F1. The "full unit vectors WLOG" reduction is FALSE.** [numeric A ✓ + agent VALID] Explicit δ=1/4
  counterexample `T={u,v}`, `u=e₂`, `v=¼e₁−(√15/4)e₂`: unit-only `G=1`, scaled `G≥4`. One-step convexity
  ≠ dynamic optimality; scaled norm-neutral/decreasing "steering" moves matter.
  - **Consequences:** (a) **retract** that reduction from the brief; (b) **Sim 1 is an incomplete model**
    — its adversary sent only full unit vectors, so it under-explored (missed scaled steering). Sim 1's
    "no super-poly" stays as *weak negative evidence*; a corrected scaled-adversary Sim is future work.
    (c) HS2 must account for steering moves outside `N(x)`. **`(★)` is NOT refuted by this.**

### NEW / UPGRADED SUBSTRATE — VERIFIED, promote to "use freely"
- **P1-sharpened.** [agent B] P1 actually gives `σ_min(B) ≥ δ_T/√|B|` (subset size), STRONGER than
  `δ_T/√r`. Numerically reconfirmed (min ratio 1.02).
- **P2-refined.** [numeric B ✓ + agent VALID] `‖P_{H(x)}x‖ ≤ q/(2δ_T)`, `q=dim span N(x)` (projection
  onto the active flat; tighter than the scalar P2).
- **P6 (NEW) — principal-angle lemma.** [numeric C ✓ (3768 pairs, 0 viol, ~3–5× slack) + agent VALID]
  For flats `H,K` = spans of subsets of `T`, the smallest positive principal angle obeys
  `sin θ(H,K) ≥ δ_T/r`. (Loose; the `r` may be improvable.) ⇒ active flats never meet at exponentially
  small angles when `δ_T ≥ 1/poly`.
- **P4-upgrade — support-function ITERATION identity DERIVED & VALID.** [agent VALID] For the recursive
  projective closure `K_{n+1}=conv ∪_t (π_t K_n+[-t,t])`: `h_{K_{n+1}}(y)=max_t(h_{K_n}(π_t y)+|⟨y,t⟩|)`,
  unrolling to `h_{K_n}(y)=max_chains Σ_j‖y_j−y_{j-1}‖`. **This was the missing piece (Phase-0 caveat (a)):
  HS1's reduction is now rigorous** — a poly-TV bound ⟹ `(★)`.
- **P3-REVIVED (now `P3′`).** [numeric D ✓ (κ_A≤1/δ_A holds all cases; dep_pairs hits equality √2) +
  agent VALID, source-backed] arXiv:2510.20301 **explicitly states** "for unit-norm columns `κ_A ≤ 1/δ_A`"
  and **Theorem 1.1: `n ≤ π d⁴ κ_A` for `d≥4`**, non-collinear columns. Taking one rep per antipodal line
  of `T` (`δ_A ≥ δ_T`, `κ_A ≤ 1/δ_T`) ⇒ **`|T| ≤ 2π r⁴/δ_T`** — only POLYNOMIALLY many directions at
  constant `δ`. 🔴 *Phase-0 dropped P3 on an incomplete read; the bridge exists. Corrected.*

### GAP — the actual open frontier of `(★)` (no proof from P1/P2 alone)
- **G1 (HS1).** A **polynomial total-variation theorem**: for products of the (≤`2πr⁴/δ_T`) hyperplane
  projections `{π_t}` whose flats are pairwise `sin`-angle-separated by `≥ δ_T/r`, prove
  `sup Σ_j‖y_j−y_{j-1}‖ ≤ poly(r,1/δ_T)·‖y_0‖`. The known unrestricted-projection BV result
  (arXiv:1901.07516, Güntürk–Thao — see MINOR) gives only a **geometry-dependent / non-polynomial**
  constant; multiplying the per-transition factor `O(r/δ)` along a rank recursion reproduces exponential.
- **G2 (HS2).** A **history-dependent summability invariant** controlling cumulative hidden-component
  transfer across active-flat switches. [numeric E ✓ + agent] The **static** switch lemma is FALSE:
  `‖P_J x‖=B`, `⟨t,x⟩=0` yet `‖P_{J+⟨t⟩}x‖=B/δ` (verified 10→40). Counting switches cannot work
  (scaled steering allows arbitrarily small switches). Must charge a quantitative geometric quantity.

### MINOR
- **M1.** Response §1 parenthetical "(since `|u+v|²=2−2c`)" is a muddled justification — `|u+v|≈0.25` is
  *small*; the max norm 1 is attained at singletons `±u,±v`. Conclusion correct; reasoning cosmetic.
- **M2 (lit).** The projection-BV reference is **arXiv:1901.07516** (Güntürk–Thao, "Unrestricted
  iterations of relaxed projections… absolute convergence…") — a better match than our `1603.00854`
  (Vladimirov), which is a different object. Update B1's citation. Neither gives a polynomial constant.

## NEEDS-HUMAN (carry to convergence/handoff)
- **NH1.** Eyeball the one-line proof of `κ_A ≤ 1/δ_A` (unit columns) in arXiv:2510.20301 (agent confirmed
  the paper *states* it; read the proof for final certainty before P3′ is load-bearing).
- **NH2.** Decide whether HS1 can tolerate the non-polynomial constant of 1901.07516 — it cannot for a
  poly bound, so G1 requires a genuinely NEW quantitative argument (exploiting P3′ + P6).

## Stall check (guide §1)
**NOT a stall.** Round 1 produced multiple NEW verified lemmas (P6, P2-refined, P1-sharpened, P4-upgrade
identity, P3′ revival) and sharpened `(★)` to two crisp missing theorems. Continue the loop → Round 2.

## Confidence
Held-with-slight-uptick: **~65% → ~67%** (B-side / `(★)` true). Rationale: structural assets strengthened
(poly-many directions P3′; poly angle-separation P6; HS1 reduction now rigorous) make an exponential
construction harder and turn the crux into a clean finitary geometry problem; BUT the core poly-TV /
summability question is untouched and the BV literature gives exponential — so no evidence the answer is
*yes*, only a better-posed problem. 🔴 Honesty rail: progress is in reduction clarity, not in proof.
