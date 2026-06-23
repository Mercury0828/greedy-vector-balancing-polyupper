# PROJECT_STATE — `greedy-vector-balancing-polyupper`

**Last updated:** 2026-06-23 · **Current phase:** ATTACK LOOP — Round 10 COMPLETE & audited (**P15** closed-class
package frozen; hard region pinned to deficient-block/Hadamard and tested **CLEAN** — γ no collapse ⟹ no
refutation; BST `√r` to r=64). **Round-11 brief READY** (`docs/round11_brief.md`: prove the open step = a poly
PCT-gap lower bound ≡ depth-independent Meshulam). Proven: P11–P15, D_exp. Target = SODA 2027. Confidence ~76%.
**Role:** Claude = orchestrator/referee/archivist (NOT prover). Target: **SODA 2027** (deadline
**2026-07-09 AoE**, lightweight double-blind — confirmed live 2026-06-21).

---

## ▶ COLD-START (read this first to resume)

**One-liner:** Phase 0 GREEN; external-solver attack loop (GPT-5.5-Pro + independent audits), now 10 rounds.
**Proven:** ranks ≤4 of `(★)` (P11–P13), root-system/graphical (P14), and a BST closed-class package (P15:
round-schedule, comparison-stable/obtuse, equicorrelation + PCT bounds + palindrome refutation bridge). The
open core is **BST ⟺ a depth-independent (poly) Meshulam constant**; the hard region (deficient-block/Hadamard)
was tested decisively and is **CLEAN** (PCT gap γ no collapse ⟹ no refutation); BST `√r` to r=64. **Round-11
brief (prove the PCT-gap lower bound) is written and waiting.** Confidence `(★)` true ~76%.

**Read in this order to rebuild context:** `guide.md` (read-only constitution) → this file →
`LEDGER_polyupper.md` (frozen model/substrate/`(★)`/confidence) → `docs/ATTACK_LOG.md` (round index) →
latest `docs/round{n}_*.md`. 🔴 Never work from memory; re-read these first.

**THE NEXT ACTION (resume here):** owner relays **`docs/round11_brief.md`** (the `✂️` block) to a NEW
GPT-5.5-Pro conversation — prove the open step: a `poly(r,1/δ)` LOWER BOUND on the PCT gap `γ` for arbitrary
(deficient-block) full words on a well-conditioned `G` (≡ a depth-independent Meshulam constant), which closes
BST hence `(★)`. The numerics give a strong TRUE prior (γ doesn't collapse on the hard family). Paste the
reply back → archive `docs/round11_response.md`, 3 audits if closure claimed, classify, update confidence. If
PROVEN → `(★)` closed ⟹ human-gate verification + writing pipeline (`venue-prompts/soda/`) + scoop re-scan.
No-retreat: escalate, never downgrade. *(Owner's standing A/B/C question: A = keep attacking (this); the
decisive hard-region test now strengthens A.)*
🔧 **AUDIT ROUTING (2026-06-23):** the `codex` MCP server (codex-cli, model=gpt-5.5, reasoning_effort=xhigh) is
now added to this project. **All future audits run on codex GPT-5.5-xhigh, NOT Claude subagents** — but MCP
tools load at session start, so a **Claude Code restart in this project** is required to activate the codex
tool. After restart, audit the Round-11 response by calling the codex MCP tool with the audit brief. (Owner:
no re-audit of Rounds 0–10.)

**Where the math stands (after Round 10):** `(★)` ⟺ **BST** ⟺ a **depth-independent (poly) Meshulam** constant.
The remaining open step (everything else closed): a `poly(r,1/δ)` LOWER BOUND on the PCT cycle-gap
`γ(R)=1−‖P_{i_m}…P_{i_1}‖²` for arbitrary DEFICIENT-block full words on a well-conditioned `G` (a super-poly
collapse ⟹ refutation via the palindrome; a poly lower bound ⟹ BST/`(★)`). **PROVEN (AI, audited):** rank ≤2
(**P11**), rank 3 (**P12**), rank 4 (**P13**), root-system/graphical (**P14**), the **P15** closed-class package
(round-schedule, comparison-stable/obtuse, equicorrelation, PCT bounds, palindrome bridge), all-word `D_exp`,
substrate P1–P10. **Numerics:** BST `sup‖p‖~√r` to r=64; **decisive deficient-block γ test on the Hadamard hard
family CLEAN** (γ≈0.90 flat, no collapse ⟹ no refutation); amplifier collapses δ. **Open:** the PCT-gap lower
bound (numerically supported). Refuted: N1–N5. Retracted: unit-WLOG. **Confidence (B-side true): ~76%.**
🔴 No matching lower bound — do NOT claim "tight/optimal".

**Pending human items:** NH1 (κ_A≤1/δ_A proof in 2510.20301); NH2 (BV constants non-poly, confirmed); **NH3**
(Betke-797 attribution); **NH4** (§1 `P_s⊆C_s+(r/δ)B_2` holds within `E=span T` only); P5 hand-proof audit.
🔴 Nothing is frozen as "proved".

**Repro:** `python code/sim1_killtest.py` · `sim2_levers.py` · `round{1,2,3,4}_audit_checks.py` ·
`round4_refutation_hunt.py` (Python 3.11 + numpy + scipy; seeds in-file; JSON outputs alongside).

---

## Current progress

- [x] Scaffold day-0 artifacts (this file, `DESIGN_DECISIONS.md`, `LEDGER_polyupper.md`,
      `docs/guide_amendments.md`, `lit/SCAN_REPORT.md`, `code/`).
- [x] Literature kill-scan (full-text anchor + 2510.20301 + 1603.00854 + SODA27 CFP) → `lit/SCAN_REPORT.md`.
      **Literature axis: NOT RED (no scoop).**
- [x] Independent second-opinion subagent on verdict → `lit/SECOND_OPINION.md`. **Verdict upheld.**
- [x] Sim 1 (kill test) → `code/sim1_killtest.py` + `code/sim1_results.json`. **No super-poly growth.**
- [x] Sim 2 (lever check P1/P2) → `code/sim2_levers.py` + `code/sim2_results.json`. **P1,P2 confirmed.**
- [ ] Paper-orientation health-check subagent.
- [ ] Phase-0 verdict + STOP at human gate (in progress).

## Frozen results + numbers (with artifact paths)

> 🔴 APPEND-ONLY discipline. Each figure/number regenerated by ONE named script with a fixed seed; the
> adversarial **maximum** (not mean) is reported.

### Literature (frozen 2026-06-21, `lit/SCAN_REPORT.md`)
- Anchor arXiv:2606.17991 = **v1 only (2026-06-16); no scoop.** `δ_T` def (Def 1.1), `[-1,1]T` model +
  `G(T)≤(2/δ_T)^{d-1}` (Thm 1.2), Lemma 1.4 **existence-only** lower `√d/δ`, tightness-open quote, and
  `G(T)≤radius(K_T)` (Thm 2.4 + Lemma 2.2) all **confirmed full-text**. Support-function **iteration
  identity ABSENT** (our reconstruction). **P3 DROPPED** (2510.20301 gives `O(d⁴·κ_A)`, no `κ_A↔δ_T`).
  **B1 weak** (1603.00854 qualitative, not projection-specific).

### Sim 1 (kill test) — FROZEN 2026-06-21
`code/sim1_killtest.py` · seed=20260621 · δ≥0.25 · out `code/sim1_results.json`.
- Adversarial `max‖S_k‖` for d=2..10: **1.41, 2.00, 2.44, 2.99, 3.62, 4.90, 5.24, 5.05, 4.09** — vs
  `√d/δ` (5.7→12.6) and `(2/δ)^{d-1}` (8→1.3·10⁸). Growth fit log-log slope **0.82** (poly), semilog 0.15.
- **No super-polynomial growth → kill-test FALSIFIER NOT triggered.** Simulator validated: hits exactly
  **√d** on orthonormal T (δ=1). 🔴 Limitation: search did not reach the anchor's `√d/δ` worst case →
  this is **negative evidence vs the exponential A-side, NOT a proof of the polynomial B-side**.

### Sim 2 (lever check) — FROZEN 2026-06-21
`code/sim2_levers.py` · seed=20260622 · out `code/sim2_results.json`.
- **P1** `σ_min(B) ≥ δ_T/√r`: worst ratio **1.008 ≥ 1**, 0 violations, all families, d∈{2,4,6,8}. ✅
- **P2** `‖x‖>r/(2δ_T) ⟹ span N(x) proper`: **0 violations** over ~2700+ adversarial x per case. ✅
- → P1, P2 promoted to "use freely" for the round-1 attacker brief.

## Paper-orientation health-check (independent subagent, 2026-06-21)

**Recommendation: GREEN with guardrails.** ① On track / SODA-altitude IF (★) proved; boundary has NOT
collapsed (anchor bound is `2^{d-1}` even at δ=1, so poly is a genuine exp→poly win in-regime). ② No
material drift; P3-drop / weak-B1 / HS1-missing-identity correctly contained (HS2 intact, single point of
failure is only (★) itself). ③ Claims respect provability; Sim-1 weak-adversary limitation correctly
handled (GREEN = "no death-evidence, attempt the proof", NOT "(★) likely true").
- **Biggest risk:** RUNWAY — (★) unproved with ~18 days to the 2026-07-09 deadline (solve+audit+assemble
  +full ~50–60pp THEORY writeup). One-theorem paper; thin margin.
- **Most important missing piece:** HS3 = the HS2 end-to-end assembly (closed-form subspace-switch
  charging turning P1/P2 into an explicit `G(T) ≤ poly(d,1/δ_T)` with a stated degree).
- **Guardrails:** (G1) **HS2 = sole primary route** [owner-confirmed]. (G2 RETIRED by owner: target SODA
  2027, ignore time — no runway downgrade; no-retreat red line stands.)

## TODO + pending human decisions

- ✅ Owner rulings (2026-06-21): (1) GREEN — start attack loop, solver = **GPT-5.5-Pro** (relayed);
  (2) target **SODA 2027**, ignore time; (3) **HS2 = sole primary route**.
- ✅ Rounds 1–9 done: archived `docs/round{1..9}_response.md`; all audited `docs/round{1..9}_audit.md`.
- 🔴 **AWAITING OWNER:** relay `docs/round10_brief_bst.md` to a NEW GPT-5.5-Pro chat (targeted BST attack).
  Paste reply back. (`docs/HUMAN_EXPERT_HANDOFF.md` retained as reference.)
- Attack-loop state in `docs/ATTACK_LOG.md`. NEEDS-HUMAN: NH1–NH6; the OPEN CORE = BST ≡ a depth-independent
  Meshulam constant. P5 hand-proof audit.
- **Substrate gains (frozen):** R1 — P1-sharp, P2′, P6, P4-upgrade, P3′; R2 — **P7**; R3 — **P8**; R4 — **P9**,
  **P10**, **NC**; R5 — **P11** (rank ≤2), **D_exp**; R6 — **P12** (rank 3); R8 — **P13** (rank 4); R9 — **P14**
  (root-system/graphical). **Open core:** **BST** (basis-level) ≡ depth-independent Meshulam. Refuted: N1–N5.
  Retracted: unit-WLOG.
- Re-confirm at submission / at convergence: SODA27 anonymity wording on live CFP (caveat C1); Lemma 1.4
  dimension bookkeeping S^{2d-1} (caveat C2); anchor v2/scoop re-scan.

## Confidence trend
| Date | Conf (B-side true) | Note |
|---|---|---|
| 2026-06-22 (seed) | ~65% | GPT-Pro external; not panel-validated |
| 2026-06-21 (lit) | ~65% (held) | lit scan: no scoop, machinery confirmed; awaiting Sim 1 |
| 2026-06-21 (de-risk) | ~65% (held) | Sim 1 no super-poly (no death-evidence) but weak adversary (not a proof); Sim 2 confirms P1,P2. Crux still open; honesty rail — de-risk ≠ proof, so confidence not raised. |
| 2026-06-22 (Round 1) | ~67% (↑2) | GPT-Pro PARTIAL, both audits VALID. New substrate (P6/P2′/P1-sharp/P4-upgrade/P3′) → crux is now a clean finitary geometry problem; exponential structurally harder. But poly-TV/summability untouched, BV-lit exponential → reduction-clarity, not proof. Modest uptick. |
| 2026-06-22 (Round 2) | ~72% (↑5) | GPT-Pro PARTIAL (93%), both audits VALID. Proven local theorem P7 (`O(r²/δ²)` certificate); `(★)`⟺bounded dual-drift lemma (one clean lemma) + concrete P3′+P6 attack; direct TV numerics sub-linear/poly tracking √d/δ. Tempered: global integrability unproven, N2 + 2026 BV counterexamples show subtlety; TV is lower-bound search. Not a proof. |
| 2026-06-22 (Round 3) | ~72% (held) | GPT-Pro PARTIAL (96%), all math sound. STALL #1: P7→`r/δ` + P8 dynamics, but P3′+P6 attack DIED (N3) and net = refutation+reformulation (`(★)`⟺DA/PC). Counterweight: dual-drift numeric bounded & flat in N ⟹ conclusion likely TRUE. Two-sided → held. Round 4 = last before escalation. |
| 2026-06-22 (Round 4) | ~75% (↑3) | GPT-Pro PARTIAL (97%), all math correct (genuine progress). Obstruction localized to codim-≥2 clusters (P9/P10); local payment dead (N4); NC reformulation. **Refutation hunt NEGATIVE** — `sup_j‖p_j‖` flat in N under cluster stress ⟹ §3-chain accumulation does NOT happen ⟹ evidence `(★)` TRUE. Tempered: deep no-cusp proof absent, numerics heuristic. Escalating to fresh attacker. |
| 2026-06-22 (Round 5) | ~75% (held) | Fresh-context escalation paid off: rank ≤2 CLOSED (P11, saturated) + all-word exp bound (D_exp) + `(★)`⟺cocycle identity. Both audits VALID; cocycle probe NEGATIVE. Base case + sharp algebraic crux + clear path (rank induction). Held: positive structure vs deep coboundary step unproven (N2 ⟹ history-dependent). |
| 2026-06-22 (Round 6) | ~75% (held) | rank 3 CLOSED (P12, `√53/δ²`, degree 2) via survivor recurrence; both audits VALID. But rank 3 is SPECIAL — general first fails at rank 4 (multidimensional survivor); crux = rank-4 flag-holonomy core. Rank-4 drift still bounded numerically. Held: another base case + obstruction pinpointed, deep holonomy step now known rank-4-new and unproven. |
| 2026-06-22 (Round 7) | ~73% (↓2) | Both audits VALID (exact). Our point-cocycle conjecture REFUTED (N5); `(★)` NOT refuted (bounded invariant cylinder = mild positive). Two-sided: clean mechanism (zero holonomy) dead, surviving set-valued cylinder is where exp blow-up hides if `(★)` false ⟹ small downward nudge (auditor ~70%). Round 8 = invariant-strip, LAST AI round before human expert. |
| 2026-06-22 (Round 8) | ~72% (↓1) | rank 4 CLOSED (P13, corrected) but the "slope exactly 0 / 99%" was FALSE-as-stated (orchestrator caught it); general (32) is a REGRESS. Pattern = rank-specific collapses, general bound receding ⟹ ESCALATE TO HUMAN EXPERT (gate b). AI attack loop concluded. Up: base case closed; down: regress, one-example-verified. |
| 2026-06-23 (Round 9) | ~74% (↑2) | FINAL fresh-context, both audits VALID. NEW theorem P14 (root systems); core SIMPLIFIED to BST (basis-level, real progress); BST≡quantitative Meshulam (gap = poly-in-depth). BST numerics √r to r=50 (auditor-reproduced + structured stress) = strongest `(★)`-evidence on the true core; auditor ~75–78%. Tempered: BST unproven, dilation refutation route open. |
