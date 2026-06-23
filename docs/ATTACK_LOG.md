# External-Solver Attack Loop — Index / Log

> Append-only index of the `(★)` attack loop (guide §External-solver). Solver = **web GPT-5.5-Pro**
> (owner-relayed). One file per artifact in `docs/`: `round{n}_brief.md` (to solver),
> `round{n}_response.md` (solver reply, verbatim/summary), `round{n}_audit.md` (independent adversarial
> audit verdict: FATAL / GAP / MINOR). 🔴 Confidence trend mirrored into `LEDGER_polyupper.md`.

| Round | Date | Artifact | Status | Verdict / notes |
|---|---|---|---|---|
| 1 | 2026-06-21 | `docs/round1_brief.md` | dispatched | Crux `(★)`, HS2 primary. P1,P2 "use freely"; P3 omitted; HS1 fallback. |
| 1 | 2026-06-22 | `docs/round1_response.md` | **PARTIAL** (GPT-5.5-Pro, conf 95% in analysis) | `(★)` not closed/refuted. Refuted our unit-WLOG reduction; derived HS1 identity; new lemmas P6, P2′, P3′. |
| 1 | 2026-06-22 | `docs/round1_audit.md` + `code/round1_audit_checks.py` | **AUDITED — all claims VALID** | 2 independent audits (numeric + fresh-agent). FATAL-to-brief: unit-WLOG false. New substrate promoted. GAPs G1 (poly-TV)/G2 (history invariant). No FATAL vs `(★)`. Conf 65→67%. |
| 2 | 2026-06-22 | `docs/round2_brief.md` | dispatched | Targets G1/G2; ships P1-sharp/P2′/P6/P3′/P4-upgrade; methods free. |
| 2 | 2026-06-22 | `docs/round2_response.md` | **PARTIAL** (GPT-5.5-Pro, conf 93%) | NEW Theorem 1 (chamber certificate `O(r²/δ²)`); `(★)`⟺bounded cyclic-monotone selection; rank-3 obstruction; bounded dual-drift lemma = the remaining crux. |
| 2 | 2026-06-22 | `docs/round2_audit.md` + `code/round2_audit_checks.py` | **AUDITED — all claims VALID** | Numeric + analytic (line-by-line). Freeze **P7** (Theorem 1), **N2** (rank-3 obstruction). Direct TV probe: sub-linear/poly growth tracking √d/δ. No FATAL vs `(★)`. Conf 67→72%. |
| 3 | 2026-06-22 | `docs/round3_brief.md` | dispatched | Targets bounded dual-drift lemma; P3′+P6 Friedrichs-angle attack suggested. |
| 3 | 2026-06-22 | `docs/round3_response.md` | **PARTIAL** (GPT-5.5-Pro, conf 96%) | P7→`r/δ`; exact dual dynamics (P8); **P6-attack DEAD** (projected images not T-spanned); `(★)`⟺DA/PC. |
| 3 | 2026-06-22 | `docs/round3_audit.md` + `code/round3_audit_checks.py` | **AUDITED — all math SOUND; STALL #1** | Numeric + analytic. Update **P7→r/δ**, freeze **P8** (dynamics), **N3** (dead P6-attack). Dual-drift numeric POSITIVE (sup_j‖p_j‖ bounded in N). No FATAL. Conf held 72%. NH3 (Betke-797 attribution). |
| 4 | 2026-06-22 | `docs/round4_brief.md` | dispatched | Targets DA/PC via itinerary-admissibility / radial-budget Lyapunov. |
| 4 | 2026-06-22 | `docs/round4_response.md` | **PARTIAL** (GPT-5.5-Pro, conf 97%) | Localized obstruction: P9 KKT-localization, P10 codim-≥2 confinement, NC inversive reformulation; killed radial-budget Lyapunov (N4). |
| 4 | 2026-06-22 | `docs/round4_audit.md` + `code/round4_audit_checks.py` + `round4_refutation_hunt.py` | **AUDITED — all math CORRECT; genuine progress** | Numeric + analytic + **decisive refutation hunt NEGATIVE** (`sup_j‖p_j‖` flat in N under codim-≥2 stress ⟹ DA conclusion likely TRUE). Freeze P9/P10/NC, N4. Conf 72→75%. |
| 5 | 2026-06-22 | `docs/round5_brief_fresh.md` | dispatched (ESCALATION, fresh context) | Clean NC / multiwall-cluster return-point theorem. |
| 5 | 2026-06-22 | `docs/round5_response.md` | **PARTIAL+WHERE** (fresh GPT-5.5-Pro; 97% rank-exp thm, 72% full lemma) | rank≤2 CLOSED; all-word D_exp bound; `(★)`⟺ cocycle identity `b_B=c_τ−Q_B c_σ`. |
| 5 | 2026-06-22 | `docs/round5_audit.md` + `code/round5_audit_checks.py` | **AUDITED — all 5 claims VALID; genuine progress** | Numeric + analytic. Freeze **P11** (rank≤2, saturated) + **D_exp**. Cocycle = sharp crux. Conf held 75%. Best path: rank induction r→r+1. |
| 6 | 2026-06-22 | `docs/round6_brief.md` | dispatched (fresh thread) | Rank induction r→r+1 (start rank 3). |
| 6 | 2026-06-22 | `docs/round6_response.md` | **PARTIAL+WHERE** (GPT-5.5-Pro, conf 97%) | rank 3 CLOSED `sup<8/δ²`; argument first fails at rank 4 (multidimensional survivor); crux = flag-holonomy lemma. |
| 6 | 2026-06-22 | `docs/round6_audit.md` + `code/round6_audit_checks.py` | **AUDITED — rank 3 CLOSED (8/8 VALID); rank-4 obstruction GENUINE** | Numeric + analytic. Freeze **P12** (rank 3, `√53/δ²`). Rank 3 special (no template). NH5 (gallery refinement). Conf held 75%. |
| 7 | 2026-06-22 | `docs/round7_brief.md` | dispatched (fresh thread) | Pivotal rank-4 flag-holonomy core: point-valued `b_B=(I−Q_B)c_{J,ω}`. |
| 7 | 2026-06-22 | `docs/round7_response.md` | **PARTIAL+WHERE** (GPT-5.5-Pro, conf 98%) | REFUTES the point-cocycle (our ask): explicit rank-4 example, 2 excursions, same Q, `b_A≠b_B`. `(★)` NOT refuted (bounded invariant cylinder). Crux → set-valued invariant-cylinder. |
| 7 | 2026-06-22 | `docs/round7_audit.md` + `code/round7_audit_checks.py` | **AUDITED — refutation CORRECT (exact)** | Numeric + analytic, sympy-confirmed. Freeze **N5** (point-cocycle dead = our own conjecture). Bounded hysteresis = mild positive. Conf 75→73%. ONE more AI round then human expert. |
| 8 | 2026-06-22 | `docs/round8_brief.md` | dispatched (fresh thread; last AI round on pivot) | rank-4 invariant-strip sublemma. |
| 8 | 2026-06-22 | `docs/round8_response.md` | **CLOSED rank 4** (GPT-5.5-Pro, conf 99%) | Zero-slope reset; rank 4 closed; general crux proposed as (32). |
| 8 | 2026-06-22 | `docs/round8_audit.md` + `code/round8_audit_checks.py` | **AUDITED — rank 4 genuinely closed (P13, CORRECTED); (32) = REGRESS; ESCALATE** | Numeric (0/19607 slope=1⟹a_B=0) + analytic. "slope exactly 0 / 99%" FALSE-as-stated (caught). (★) NOT reduced to (32). Conf 73→72%. |
| — | 2026-06-22 | **`docs/HUMAN_EXPERT_HANDOFF.md`** | **HANDOFF READY (human gate b)** | Standalone open-core statement (cross-state invariant-cylinder cocycle, rank ≥5) + proven P1–P13/D_exp + dead routes N1–N5 + candidate machinery. **AI attack loop concluded.** |

## Stop criteria (guide §4) — AI convergence only when ALL hold
1. solver explicitly claims closure of `(★)` + assembly, no further conditions;
2. ≥ `K_audit = 3` independent adversarial audits find no FATAL / no counterexample;
3. every residual is verification debt (write-out / wording), not a new GAP/obstruction.
→ then STOP the AI loop → human gate (b). 🔴 "AI-verified ≠ proved."

## Stall / escalation (guide §1)
`K_stall = 2` consecutive rounds with no new VERIFIED lemma, OR circular reasoning, OR re-tread of a
refuted route, OR sustained confidence drop ⇒ escalate (fresh-context attacker with a method-free brief).
No-retreat red line: difficulty never downgrades the contribution; only proof-of-death → human gate.
