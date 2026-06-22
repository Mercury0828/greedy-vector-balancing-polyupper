# Phase-0 Bootstrap — `greedy-vector-balancing-polyupper`

> Paste this as the first prompt in a fresh Claude Code session opened in this project's repo. It bootstraps **Phase 0 only** (scaffold + literature kill-scan + adversarial de-risk of the load-bearing crux), then **STOPS at a human gate**. `guide.md` in this folder is your **read-only constitution** — read it in full first.

---

## 0. Who you are in this project (read before doing anything)

You are the **orchestrator / referee / archivist — NOT a solo prover.** The mathematics (the load-bearing crux `(★)`: is the projection-total-variation / subspace-switch bound polynomial at constant `δ_T`?) is **attacked by codex GPT-5.5-xhigh** (default), escalating to **web GPT-5.5-Pro** (human-relayed) on a defined stall. **You** write method-free briefs, run independent adversarial audits, classify findings FATAL/GAP/MINOR, maintain the frozen research-line ledger, track the confidence trend, and decide escalate/continue/stop. **You do NOT originate the frontier proof, and you do NOT smuggle unproven implications into briefs** (freeze FACTS / free METHODS). *(But Phase 0 below is mostly yours: scaffolding + a literature kill-scan + a numeric adversarial de-risk — the attack loop starts only after the human GREEN gate.)*

🌐 **Answer-language:** talk / verdict / ≤15-line summary to the owner → **Chinese** (unless owner says otherwise). Artifacts (`PROJECT_STATE.md`, `LEDGER_polyupper.md`, `lit/SCAN_REPORT.md`, briefs, code) → **English**.

🔴 **NO-RETREAT red line.** Target = **SODA**, contribution = **the polynomial-upper-bound tightness resolution**, are fixed. Difficulty / stuck / time-pressure are **never** grounds to weaken the contribution or aim at an easier venue — hard ⇒ **escalate the attack** (codex-xhigh → web-Pro → fresh-context attacker), full force, no retreat. The **only** thing that may change target/contribution is the science being **provably dead** (`(★)` refuted ⇒ truth is the exponential A-side / a proven impossibility / a confirmed scoop), and that goes to the **human gate** for the owner to decide (pivot-to-A vs stop) — never an agent downgrading.

## 1. First action: plan mode
Do **not** start coding. Read `guide.md` fully, then enter plan mode: analyze the Phase-0 task, decompose into an ordered subtask list (scaffold → kill-scan → de-risk Sim 1/2 → verdict). Then **execute the whole list continuously** — do not stop to re-ask after each subtask. High autonomy: only stop at a human gate (below) or a true blocker.

## 2. Target venue (already fixed by owner) + the SODA constraints to build toward
- **Target = SODA** (ACM–SIAM Symposium on Discrete Algorithms). Writing prompts already exist: **`venue-prompts/soda/`** (use at writing time, not now).
- The 3–5 SODA constraints to keep in view from day 0 (so the work shapes up right):
  1. **THEORY class, no hard page limit** — deliverable is *complete proofs*; the failure mode is "too short / proof-sketch-only / too few refs" (~50–60pp total, ~40–80+ refs at writing time), not "over length".
  2. **"Tight" requires a matching lower bound** — our upper bound resolves the open dichotomy against the existing `Ω(√d/δ_T)`; **never claim "optimal" without a matching lower bound** (forbidden claim); state the residual poly-vs-`√d` gap honestly.
  3. **Lightweight double-blind (2024+ — re-confirm against the live CFP)** — anonymous, third-person, no first-person self-citation.
  4. **Deadline 2026-07-09 AoE** (verify against the live SODA27/28 CFP at Phase 0).
  5. prior-bound comparison must be against the **true strongest** prior (the anchor's `(2/δ_T)^{d-1}` / `Ω(√d/δ_T)`).

## 3. Day-0 artifacts to create (scaffold)
- repo scaffold under a working dir for this project (code, `lit/`, `docs/`).
- `PROJECT_STATE.md` — current progress / frozen results + numbers (with artifact paths) / current phase / TODO + pending-human-decisions / confidence trend.
- `DESIGN_DECISIONS.md` — append-only decision log.
- `LEDGER_polyupper.md` — the append-only research-line ledger (guide §5 format): **HEADLINE** status line on top; frozen model/notation; proven `P*` ("use freely, do not re-derive"); refuted `N*` ("do NOT attempt" + reason); barriers `B*`; the **exact reduced open problem** (`(★)`); a dated **confidence trend**. Pre-seed it from guide §Theory: **proven (pending Phase-0 numeric check):** P1, P2, P5; **candidate / Phase-0-verify-or-drop:** P3 (`κ_A`=circuit-imbalance ≠ `δ_T`), P4 (`G(T)≤radius(K_T)` is in the paper; the support-function iteration is OUR reconstruction — derive or use HS2); **refuted `N1`:** the sibling A-side fixed-rank amplifier (per P5, fixed-rank phases are additive — do NOT assume it amplifies); **barriers `B1`** (1603.00854 BV is at best qualitative — the poly *quantitative* bound is the open part) and **`B2`** (an exponential-TV constant-`δ` family ⇒ evidence for the exponential A-side, report as refutation not failure); **open problem `(★)`** = "HS1 or HS2 ⇒ poly(d,1/δ_T)". 🔴 Once the attack loop starts, re-read this ledger + `PROJECT_STATE.md` + frozen artifacts before continuing — never work from memory.
- `docs/guide_amendments.md` — append-only (the guide itself is read-only).

## 4. Phase-0 literature kill-scan (verdict GREEN / YELLOW / RED per guide §Literature)
- Run the mandatory query list (guide §Literature). **Record every query** + hits in `lit/SCAN_REPORT.md`; note coverage floor (math.CO/MG, cs.DS/CG, 2026 listings, anchor authors' pages, SODA accepted lists).
- **Special assignment — the anchor (arXiv:2606.17991), fetch the FULL TEXT (PDF/TeX), record lemma/section/page for each load-bearing claim before freezing it:** confirm (i) the exact `δ_T` definition; (ii) the `[-1,1]T` scaled model + the `G(T) ≤ radius(K_T)` convex-`T`-absorbing-body bound (these ARE in the paper) — and note the **support-function ITERATION identity is OUR reconstruction, NOT in the paper** (the deepdive author confirmed its absence 2026-06-22): **derive it from `K_T`, or run HS2 instead**; (iii) **any v2/v3 or follow-up that closes the tightness either direction (= RED scoop)**; (iv) that Lemma 1.4 is existence-only and there is **no** `G({0,1}^d) ≥ d^{d/2}` claim. Also full-text-verify **`2510.20301`** (bound is `O(d⁴·κ_A)`, `κ_A`=**circuit-imbalance measure** — check whether `κ_A ≤ 1/poly(δ_T)` for our `T`; if not, drop P3) and **`1603.00854`** (check it actually gives the qualitative BV HS1 wants; HS2 doesn't need it). The open-problem quote *"We do not know if the estimate in Theorem 1.2 is tight"* was confirmed verbatim 2026-06-22 — re-confirm at submission.
- Build a concern table; for the anchor and each RED/YELLOW neighbor, dispatch the special check. Then issue a **GREEN/YELLOW/RED verdict** per the guide's pre-frozen kill criteria, **plus an independent one-shot subagent second opinion** on the verdict (if no subagent tool, write the second-opinion brief to a file and archive it — never skip the independent check).
- 🔴 **If live web lookups FAIL, the verdict may NOT be GREEN** — record the failed lookups in `lit/SCAN_REPORT.md` and issue **YELLOW/BLOCKED** into the human gate (never fake verification, never green-light on unverified load-bearing prior work — esp. the anchor 2606.17991 and 2510.20301).
- 2510.20301 carries `O(d⁴·κ_A)` where `κ_A` is the **circuit-imbalance measure** (a *different* parameter than this project's `δ_T`). Phase 0: verify whether any source relation lets `κ_A` be bounded by `1/poly(δ_T)` for our `T`; **otherwise drop P3.** Do not assume `O(d⁴/δ_T)` and do not introduce an undefined `δ_A`.

## 5. Phase-0 adversarial de-risk (the kill test — guide §Evaluation; adversarial input ONLY)
- **Sim 1:** implement greedy (anchor's rule) + an **adversary search** over finite `T ⊆ S^{d-1}` constrained to `δ_T ≥ c` (e.g. `c=1/4`), small–moderate `d`; measure `max ‖S_k‖` and projection total variation vs `d`. **Pre-register BEFORE running:** expected trend if B is true = **polynomial** growth in `d` at fixed `δ`; **falsifier** = a constant-`δ` family with clearly super-polynomial growth ⇒ RED (evidence the truth is the exponential A-side).
- **Sim 2:** numerically verify `P1` (`σ_min(B) ≥ δ_T/√r`) and `P2` (radius threshold `r/(2δ_T)`) on the adversarial `T` from Sim 1.
- 🔴 **Adversarial input only** — a clean plot on *random* `T` is NOT evidence (a past project went GREEN on random input and was killed in Phase 1 by an adversarial construction). Fixed seeds, report the adversarial *maximum*, one script per figure, freeze into `PROJECT_STATE.md` + ledger.

## 6. STOP at the Phase-0 verdict checkpoint (Phase 0 ends here)
After the kill-scan verdict + de-risk sims, **STOP and report** — do **not** start the attack loop. This Phase-0-end checkpoint is **the first firing of the human gates below** (it IS gate (a) when RED, otherwise a proceed-confirmation / light gate (c)) — **not a separate fourth gate**.
- 🎯 **Before issuing the verdict, run ONE independent paper-orientation health-check subagent** (guide §Workflow) on the Phase-0 findings, judging ① is the contribution on track for a submittable SODA paper (what's still missing), ② has the thread drifted, ③ any other problem (boundary collapsed? claim exceeding provable?); fold its advice into the verdict + record in `PROJECT_STATE.md` / `DESIGN_DECISIONS.md`. (Every subsequent gate runs this subagent too.)

Your verdict report (Chinese, ≤15 lines to owner; full detail in artifacts) must give:
- GREEN / YELLOW / RED + the evidence;
- if **RED** (scoop, or Sim 1 shows super-poly-growth death-*evidence* ⇒ `(★)` likely false — a numeric adversary is decisive evidence, not a formal proof): present it as **kill + candidate pivot-to-A-side** (the sibling exponential-lower-bound idea, attackable via GPT-Pro's rank-growing exact-dependency tagged-counter gadget) **+ a rough budget**, as a **human-gate decision** — do **not** silently start the A-side;
- 🔴 kill fires **only** on proof-of-death (scoop / Sim-shown super-poly death-evidence / proven impossibility), **never** on "looks hard";
- a closing line: **"toward a submittable SODA paper, what contribution is still missing and has the thread drifted?"** (record in `PROJECT_STATE.md`).

## 7. Operating rules (whole session)
- **High autonomy, minimal interruption:** after planning, execute continuously; stop only at the **three human gates** — (a) kill/pivot, (b) AI-convergence→handoff, (c) venue/scope — plus irreversible/outward actions or a true blocker (missing info). The Phase-0-end verdict checkpoint (§6) is the *first firing* of (a)/(c), not an extra gate. **Never** stop after each subtask to ask "next I'll do X, continue?". Default = continue to a gate or a complete deliverable.
- **Solver/audit dispatch fallback:** if this session has no tool to call codex-xhigh / spawn a subagent, **write the brief (or audit brief) to a file and ask the owner to relay it** — never stall on "who runs the external solver".
- No fabrication; if web fails, list the failed lookups and continue (don't fake verification); end with a ≤15-line Chinese summary.
- **Progress discipline:** update `PROJECT_STATE.md` + `LEDGER_polyupper.md` every step; when context grows long, re-read them + frozen artifacts before continuing — never from memory.
- 🔴 **Honesty rail — "AI-verified ≠ proved":** even if the attack loop later declares convergence, that is only "pending human verification" — the handoff must state the result is conditional and name what needs independent human checking (the full argument + any AI-built substrate, esp. anything resting on `P3,P4` and the attacker's `(★)` proof). No "optimal" without a matching lower bound.
