# Round-4 AUDIT — verdict + classification + refutation hunt + escalation decision

> Independent audits of `docs/round4_response.md`: (1) orchestrator numeric
> (`code/round4_audit_checks.py` → `round4_audit_results.json`); (2) fresh-context analytic agent;
> (3) **decisive refutation hunt** (`code/round4_refutation_hunt.py` → `round4_refutation_results.json`).
> **Bottom line: all of Round 4's mathematics is CORRECT (genuine progress, not a stall). The obstruction
> is now localized to a single precise mechanism (codim-≥2 wall clusters), and a TARGETED refutation hunt
> shows that mechanism does NOT accumulate — `sup_j‖p_j‖` is flat in N. Evidence `(★)` is TRUE strengthens.**

## Classification (guide §3)

### PROGRESS — verified, freeze as substrate
- **P9 (NEW, §4 KKT localization).** For an adjacent dual transition with flipped normal `b_0` and common
  active normals `b_1..b_k` at `p⁺`: `Δ=‖p⁺‖²−‖p⁻‖²=2Σλ_i−‖d‖² ≤ 2Σ_{i≥1}λ_i(1−⟨b_0,b_i⟩) ≤ 4Σλ_i`, and
  **NO common active constraint ⟹ Δ≤0** (dual norm cannot increase). *Analytic VALID (load-bearing step
  `β≥2` proven and confirmed essential); numeric: 0 violations of `Δ≤4Σλ_common`, 0 violations of eq(9)
  over 54 no-common cases.* ⟹ all positive drift comes from constraints active on BOTH sides of a switch.
- **P10 (NEW, §5–6 codim-≥2 confinement).** With `u=x/‖x‖`: `Δ_+ ≤ (4/η)⟨d,u⟩ + 4Σ_{i∈Z}λ_i`, and the
  unpaid part `Z≠∅ ⟹ dist(u,J^⊥)≤rη/δ` with `dim J≥2`. *Analytic + numeric VALID.* ⟹ all UNPAID dual
  drift is confined to a poly-thin tube around a **codim-≥2 arrangement stratum** (clustered multiwall).
- **P7-corollary (§1).** `P_s ⊆ C_s + (r/δ)B_2` (every vertex ≤ r/δ; Minkowski–Weyl) — **valid WITHIN
  E=span(T)** (caveat: in ambient ℝ^d, `P_s` is not pointed; restrict to E). `dist(p,C_s)≤r/δ`.
- **NC (NEW, §7 inversive no-cusp reformulation).** `I(p)=p/‖p‖²`, lobes `L_s=∩B(v_i/2,½)`, `I(P_s)=L_s∖{0}`
  (verified exactly), inversion identity `‖I(z)−I(w)‖=‖z−w‖/(‖z‖‖w‖)` (err 7e-15), lobes meet only at 0.
  **DA ⟺ NC:** `inf_j‖z_j‖ ≥ 1/poly(r,1/δ)` — the relative-nearest-point process never cusps into the
  common tangency point 0. Cleanest standalone restatement of the crux.

### REFUTED LOCAL APPROACH (already in N-list, reinforced)
- **N4 (≈ extends N3/§3): no LOCAL per-switch payment estimate exists.** Verified (S2/S3): the `r/δ` ball is
  NOT projection-invariant (one adjacent projection escapes: `‖p⁻‖²=106/7 < R_0²=144/7 < ‖p⁺‖²=154/7`), and
  on a GENUINE constant-δ itinerary a switch adds `Δ=48/7` while `⟨d,x⟩/‖x‖→0` ⟹ the radial-budget Lyapunov
  (our R4 direction 1) is dead. Cancellation must be CLUSTER-level / history-dependent, not per-switch.

### THE OPEN CRUX (unchanged target, sharper form)
- `(★)` ⟺ DA ⟺ PC ⟺ **NC** ⟺ a **polynomial multiwall-cluster return-point / no-cusp theorem**: a cluster
  of near-simultaneous wall switches may create a large intermediate dual excursion, but after the admissible
  cluster (+ later revisits) is processed the excursions must cancel without re-paying the rank/angle factor.
  Needs the **ordered oriented-matroid gallery** of the itinerary. No literature source supplies it.

### DECISIVE REFUTATION HUNT (the auditor's point (c): could DA be FALSE?)
- **Setup:** built genuine **codim-≥2 wall clusters** (n_plane unit vectors in a common 2-plane + axes),
  trajectories biased to repeatedly cross the clustered walls — exactly the §6 danger zone the localization
  leaves open. Measured `sup_j‖p_j‖` vs trajectory length N∈{25..350}.
- **Result:** `sup_j‖p_j‖` is **EXACTLY FLAT in N** (constant across all N) and stays below `r/δ` in every
  config (r=3,4; n_plane up to 9; δ_T 0.21–0.50). **log-log(N) slope = 0.000; √N slope = 0.000. NO
  accumulation, NO √N growth.** The feared §3-chain super-poly mechanism does NOT materialize on admissible
  clustered itineraries. → **No refutation found; DA's conclusion holds even in the danger zone.**
- *Caveat:* still a heuristic adversary (cluster-biased), not provably worst-case-over-admissible — evidence,
  not proof. But it is specifically engineered for the §6 mechanism and shows perfect saturation at ~r/δ.

## Stall / escalation
- **Round 4 = genuine progress (NOT stall #2).** New verified lemmas P9, P10, NC. So K_stall is NOT
  triggered (Round-3 stall #1 did not recur). 🔴 BUT — independent recommendation (auditor) + orchestrator
  judgment: the problem has now reduced to ONE crisp, well-isolated object (NC / multiwall-cluster
  return-point), the same GPT-Pro thread keeps localizing-without-closing, and each orchestrator-suggested
  local attack dies. **This is the right point to ESCALATE to a fresh-context attacker** (first-class lever,
  guide §1): a NEW GPT-Pro session given the clean NC framing + frozen substrate, asked specifically for the
  multiwall-cluster return-point theorem, inviting machinery the thread hasn't used (oriented-matroid
  galleries, projection-orbit / Coxeter-arrangement theory). → `docs/round5_brief_fresh.md`.

## Confidence
**~72% → ~75%** (B-side / `(★)` true). Rationale: Round 4 confined the obstruction to a single precise
mechanism (codim-≥2 clusters), and the targeted refutation hunt shows that mechanism does NOT accumulate
(`sup` flat in N) — both push toward TRUE; plus P9/P10 are real new structure. Tempered by: the proof
genuinely does not exist (the no-cusp theorem is deep), and all numerics are heuristic lower bounds. 🔴 Not
a proof; nothing frozen as proved.

## NEEDS-HUMAN
NH1 (κ_A≤1/δ_A proof); NH2 (BV constants non-poly, confirmed); NH3 (Betke-797 attribution); **NH4** (§1
inclusion is within E=span(T) only — keep ambient-vs-E bookkeeping clean in any writeup); P5 hand-proof audit.
