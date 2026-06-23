# Round-8 AUDIT — rank 4 CLOSED (corrected); (32) is a REGRESS; ESCALATE TO HUMAN EXPERT

> Two independent audits of `docs/round8_response.md` (a CLAIMED CLOSURE → harshest scrutiny): (1) orchestrator
> numeric (`code/round8_audit_checks.py` → `round8_audit_results.json`); (2) fresh-context analytic agent
> (re-derived the maps, 19,607-word sweep). **Bottom line: rank 4 IS genuinely closed — but the headline
> mechanism ("Q_B=P_{K^⊥} / slope exactly 0", confidence 99%) is FALSE AS STATED; the true mechanism is
> contraction-or-neutral. Freeze P13 with the CORRECTED statement. The general crux (32) is a REGRESS (the
> Round-2/3 open core relabeled), NOT a faithful reduction. Per the pre-registered trigger → ESCALATE TO A
> HUMAN EXPERT.**

## Classification (guide §3)

### PROVEN — freeze (with corrected statement)
- **P13 — rank 4 CLOSED.** `sup_j‖p_j‖ ≤ poly(1/δ)` at `r=4` (conservative all-word `O(δ^{-13})`; the
  structural cross-section is `O(δ^{-9})`, the per-K absorbing interval `O(δ^{-7})`). 🔴 **CORRECTED mechanism
  (the attacker's "slope exactly 0 / Q_B=P_{K^⊥}" is FALSE as stated):** each K-confined return induces on
  `L=K∩J^⊥` an affine map that is **either a contraction (ratio ≤ 1−c, here ≤0.167) or the identity with ZERO
  translation** — never slope-1-with-drift. Key verified fact: **slope=1 ⟹ a_B=0** (0 violations / 19,607
  words; structural reason: all-J faces ⟹ `q_j⊥L` ⟹ every `b_B` term ⊥ L). So `|a_B|≤M_3=O(δ^{-7})`, the
  family is uniformly absorbing, common invariant cross-section `O(δ^{-9})`. Arithmetic (M_3 coeff
  6,998,400·δ^{-7}; switching `1/(1−α)≤32/δ²`; body radius 447,897,600·δ^{-9}; all-word 6.87e13·δ^{-13}) all
  exact. *Caveat NH6:* verified on ONE arrangement (the R7 example); the general rank-4 proof of
  "slope=1⟹a_B=0 and `1−slope ≥ poly(δ)`" should be written out (auditor: follows from `q_j⊥L` for J-faces;
  straightforward but not yet done) before P13 is fully load-bearing.
- *Orchestrator note:* this is the loop's value — and the orchestrator's job — to **catch the over-claim**:
  the conclusion (rank 4 closed) is right; the stated reason and the 99% were not. Frozen accordingly.

### NOT a faithful crux — REGRESS (do not treat as the new target)
- **(32) "Quantitative affine-return semigroup theorem" is a RELABELING of the open core, not progress.**
  (i) `(32)⟹(★)` is circular — `𝒜_σ` is defined over returns to a FIXED state, but `(★)` needs the
  cross-state inclusion `A_B(C_σ)⊆C_τ`, which (32) presupposes (it IS the Round-7 invariant-cylinder cocycle).
  (ii) `P_{V_σ}b_B=0` is the neutral-space version of the **already-refuted N5** point-coboundary; unproven at
  rank ≥5. (iii) The hard quantity ("translations don't accumulate along joint-neutral directions, degree
  independent of flag depth") is assumed by fiat — this is the **same open core as Round 2/3 (DA / history
  summability)**, renamed. §5's honest self-diagnosis (rank 4 is SPECIAL: 1-dim returned layer, `Q_B` a
  projector onto an original flat; does NOT template) is correct.

### THE GENUINE OPEN CORE (unchanged since Round 2/3, now sharply stated)
> The **cross-state invariant-cylinder cocycle**: construct compact convex cross-sections `C_σ⊂V_σ^⊥`,
> `sup‖c‖≤poly(r,1/δ)`, with `A_B(C_σ)⊆C_τ` for every admissible primitive block `B:σ→τ` — equivalently, a
> quantitative admissibility theorem preventing affine-translation accumulation along the joint-neutral
> directions of the return semigroup, with degree independent of flag depth. Proven for the neutral/1-dim
> cases (ranks ≤4); open for the multidimensional-survivor case (rank ≥5). Generic nonexpansiveness is NOT
> enough; the point-coboundary form is refuted (N5).

## META / escalation decision
- **Pattern:** ranks 2,3,4 each closed by a *rank-specific collapse* (no survivor / 1-dim survivor / zero-or-
  contracting reset); the general bound keeps receding; (32) is a regress. This is **mild convergence with a
  real risk of infinite regress** — the AI loop has circled the same cross-state cocycle core since Round 2.
- **DECISION (fires the pre-registered Round-8 trigger): ESCALATE TO A HUMAN EXPERT.** Round 8 DID construct
  the rank-4 interval, but it also pinned a *clean obstruction the AI rounds have not cracked in 6 rounds*.
  One more AI round most likely yields another relabeling. Hand the open core (above) to a human expert
  (oriented-matroid galleries / projection-orbit cocycles / quantitative affine IFS). → `docs/HUMAN_EXPERT_HANDOFF.md`.
  🔴 No-retreat: this is escalation (to a human), NOT a downgrade of the contribution.

## Confidence
**~73% → ~72%** (B-side / `(★)` true). Up: rank 4 genuinely closed, the feared slope-1+drift case provably
absent, arithmetic exact. Down: the headline mechanism was false-as-stated (the 99% unjustified), the general
crux is a regress, everything is one-example-verified, and the surviving set-valued cylinder is exactly where
exponential blow-up would hide if `(★)` were false. Auditor independent ~70–72%. 🔴 Nothing frozen as "proved"
beyond P11, P12, **P13 (corrected, pending NH6)**, D_exp.

## NEEDS-HUMAN
NH1–NH5 (prior); **NH6** (write the general rank-4 proof that slope=1⟹a_B=0 and `1−slope≥poly(δ)`, replacing
the one-arrangement verification); and the OPEN CORE itself = the human-expert handoff (`docs/HUMAN_EXPERT_HANDOFF.md`).
