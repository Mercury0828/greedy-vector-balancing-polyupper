# Independent Second-Opinion — Literature Kill-Scan Verdict

**Date:** 2026-06-21 · **Reviewer:** independent fresh-context subagent (general-purpose, web-enabled),
adversarially tasked to BREAK the verdict, verifying from primary sources (arxiv.org). Archived per guide
§Workflow (never skip the independent check).

## Verdict: **Literature axis NOT RED — upheld.** No scoop; no load-bearing misstatement blocking GREEN.

### Item-by-item (CONFIRMED unless noted)
1. **Scoop check — CONFIRMED (no scoop).** 2606.17991 is **v1 only** (2026-06-16 14:42:12 UTC); no v2/v3.
   Authors' 2025–26 output checked via DBLP (Orlikowski → VASS/reachability; Dadush → 2510.20301
   circuit-imbalance) — no follow-up on greedy-VB tightness. June-2026 cs.CG listing has only 2606.17991
   on-topic. No competing paper in EITHER direction. Target (polynomial side) genuinely open.
2. **Anchor machinery — CONFIRMED** (a) δ_T def, (b) [-1,1]T model, (c) Lemma 1.4 existence-only `√d/δ`,
   (d) tightness quote verbatim, (e) `G(T) ≤ (2/δ_T)^{d-1}` via T-absorbing/T-projective `K_T` (chains of
   subspaces + Minkowski sums + inductive radius). **Support-function iteration identity confirmed ABSENT**
   (proof uses T-projective definitions, not a support-function recursion) — favorable: the iteration would
   be OUR contribution, not a restatement.
3. **2510.20301 — CONFIRMED**: `n ≤ O(d⁴·κ_A)`, κ_A = circuit imbalance, **no κ_A↔δ_T relation**.
   Dropping P3 was correct.
4. **1603.00854 — CONFIRMED**: qualitative convergence (LCP/RCP, joint spectral radius); no quantitative
   projection-trajectory TV bound.
5. **SODA 2027 — CONFIRMED in substance.** Deadline **2026-07-09 AoE (UTC-12)** (PaperPilot + aggregators);
   lightweight double-blind = SODA standing policy (anonymized, third-person self-ref).

### Non-blocking caveats (carried to PROJECT_STATE / human gate)
- **(C1)** The reviewer's fetch of the **SODA27 SIAM CFP page returned HTTP 403**; deadline/double-blind
  were confirmed via aggregators + the SODA26/25 SIAM submission pages, not the live SODA27 page by the
  reviewer. *(The orchestrator's own WebSearch on 2026-06-21 did surface the SODA27 SIAM page + soda27.hotcrp.com
  with the 2026-07-09 deadline and lightweight-double-blind text.)* → **Recommend a human re-confirm the exact
  SODA27 anonymity wording on the live CFP before submission.**
- **(C2)** Lemma 1.4's ambient sphere is **S^{2d-1}, not S^{d-1}** — track this dimension bookkeeping so the
  paper's lower-bound comparison (`Ω(√d/δ_T)`) uses the right `d`.

### URLs fetched by the reviewer
2606.17991 (abs+html), 2510.20301, 1603.00854, dblp.org/pid/291/4569.html, arxiv.org/list/cs.CG/2026-06,
getpaperpilot.com/deadlines/soda-2027.html, siam.org SODA27 page (403).
