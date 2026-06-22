# Round-3 AUDIT — independent verdict + classification + STALL log

> Two independent audits of `docs/round3_response.md`, blind to each other:
> (1) orchestrator numeric (`code/round3_audit_checks.py` → `code/round3_audit_results.json`, seed 20260622);
> (2) fresh-context analytic agent (by hand + numeric spot-checks + literature).
> **Bottom line: all of Round 3's mathematics is SOUND (Claims 1–5 VALID; Claim 6 split). No FATAL, no
> refutation of `(★)`. But the round is a STALL on the closure objective** — one small sharpening (`r/δ`),
> a KILLED attack (the P6/Friedrichs route is dead), and a faithful reformulation (DA ⟺ PC). Counterweight:
> the **dual-drift numeric is POSITIVE** — `sup_j‖p_j‖` stays bounded in N (evidence DA/PC's conclusion is true).

## Classification (guide §3)

### PROGRESS — verified, update/freeze
- **P7-SHARPENED → `R_loc = r/δ`** (Prop 1). Every realizable `P_s` has a vertex; `r` independent active
  normals `B` with `Bᵀp=1`, `σ_min(B)≥δ/√r` (P1) ⟹ `‖p‖≤r/δ`. *Analytic VALID; numeric: cert norms 4–6,
  0 violations vs `r/δ`.* Replaces the `O(r²/δ²)` constant. **The one concrete new quantitative gain.**
- **P8 (NEW machinery) — exact dual dynamics.** Each update `p⁺=Proj_{P_s}(p)=P_{H^⊥}p+q_B`, `q_B∈H` the
  min-norm point of the active-face affine hull, `‖q_B‖≤r/δ`; **energy identity** `‖p⁺‖²−‖p‖²=‖q_B‖²−‖P_H p‖²`;
  **telescoping** `I−Q_N Q_Nᵀ=Σ_j R_j P_{H_j} R_jᵀ`; **Bessel** `Σ_j‖P_{H_j}R_jᵀu‖²≤‖u‖²`. *Analytic VALID;
  numeric: telescoping max-abs-err 0.0.* ⚠️ Exposition caveat: "Proj onto `P_s` = Proj onto active-face
  affine hull" needs the **non-degenerate face** justification (independent active normals) — generically
  true (519/519), fails in degenerate cases (measure zero); state via face theory, not bare "optimality".

### NEW REFUTED APPROACH — freeze
- **N3 — the P6/Friedrichs-angle charging attack is DEAD** (the route the Round-3 brief proposed). The drift
  in Bessel (8) is governed by the **dynamically projected images** `R_j H_j = P_{H_N^⊥}⋯P_{H_{j+1}^⊥} H_j`,
  NOT the original `T`-spanned flats. These images (i) are not `T`-spanned (P6 inapplicable), (ii) form an
  infinite time-ordered family (P3′ count inapplicable), (iii) **can have mutual `sinθ` collapse to ~0.003
  after a single projector** (numerically confirmed by the auditor). So P1/P3′/P6 give no transformed-frame
  estimate; the pure energy method stops at `√N`, not uniform. **Fundamental, not a hand-wave.**

### THE OPEN CRUX — `(★)` ⟺ DA ⟺ PC (faithful, slack-free)
- **DA (dynamic affine-synthesis):** `sup_N‖Σ_j P_{H_N^⊥}⋯P_{H_{j+1}^⊥} q_j‖ ≤ poly(r,1/δ)`, over admissible
  `(H_j,q_j)` (`q_j∈H_j`, `‖q_j‖≤r/δ`).  ⟺ **PC (polynomial circulation):** the curl term
  `C(Γ)=Σ∫ρ d⟨a_s,u⟩ ≤ poly·‖y_0‖`. Then `G(T) ≤ 2(r/δ + C)`. Radial/feasibility part fully handled
  (radius `r/δ`); **only accumulated curl/cancellation is open.** Must be history-dependent (N2/N3).

### DIRECT NUMERIC EVIDENCE (positive — the decisive probe)
- **Dual-drift sim** (`p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)` along adversarial reversed-projection itineraries):
  `sup_j‖p_j‖` is **bounded and ~flat in trajectory length N** and tracks the `r/δ` scale — e.g. r=3:
  4.13→4.34, r=4: 11.4→13.3, as N goes 10→90. **No `√N` blowup.** ⟹ on admissible itineraries the
  cancellation DA/PC needs APPEARS REAL; the lemma's *conclusion* holds empirically. Evidence for `(★)`,
  not a proof (heuristic adversary, not worst-case-over-admissible-itineraries).

### Literature (Claim 6)
- arXiv:2506.22553 = **Bauschke–Tung, "On a result by Meshulam" (2025)** — extends Meshulam boundedness for
  orbits of projections onto finitely many affine/polyhedral sets; **qualitative only, no poly constant**
  (solver's reading VALID-as-inference).
- optimization-online/797 = **Betke (2004), "Relaxation… Linear Feasibility"** — the δ-algebra
  `vol(B)≥δ^{|B|−1} ⟹ κ(A)≤δ^{-(r-1)}` (exponential at constant δ) is VALID, **but the specific
  "`κ(A)·2^{3r/2}`" factor + κ(A) definition are the solver's paraphrase, NOT sourced** → **NH3** (human
  confirm against the DCG text). No source gives a poly-in-(r,1/δ) bound for DA/PC.

## STALL LOG (guide §1)
- **Round 3 = STALL round #1 on the closure objective.** Rationale: Rounds 1–2 each froze new positive
  substrate (P6/P2′/P4-upgrade/P3′; P7/N2); Round 3 froze one sharpened constant (`r/δ`), killed the
  recommended attack (N3), and reformulated (DA⟺PC) — **no new lemma toward closing.** Confidence in
  `(★)` being TRUE is unchanged-to-up (numeric positive), but the PROOF did not advance.
- **K_stall = 2.** Round 4 is the **last GPT-Pro round before escalation**: if it also yields no new closing
  lemma → escalate per the ladder (spawn a FRESH-context attacker with a method-free brief; the fresh-agent
  move is first-class). 🔴 No-retreat: escalation = attack harder, never downgrade.

## Most promising NEXT attack (auditor; for Round 4) — NOT angle-transfer (dead)
Exploit the **admissibility structure of itineraries from reversed projection trajectories** (the `(H_j,q_j)`
are NOT an arbitrary word). A **monotonicity/Lyapunov argument along sub-runs**: ρ is monotone (PC) and
`‖p_j‖` is non-increasing on a maximal sub-run with a fixed active face; norm growth occurs ONLY at face
reorientations, which are itinerary-constrained (successive active faces share the trajectory point `x_j`,
coupling `q_{j+1}` to `q_j`). Build a potential `Φ_j=‖p_j‖²+`(correction from the trajectory-induced overlap,
not P6) and show increments telescope because each reorientation consumes a quantum of the bounded radial
budget `(r/δ)‖y_0‖` that PC already controls. Equivalently: choose `a_s` history-dependently so `d⟨a_s,u⟩`
has a sign/summability tied to ρ-monotonicity, bounding `C(Γ)`. Routes through verified PC/radial structure +
itinerary admissibility, never through angle-transfer.

## Confidence
**~72% (held).** Two-sided: the dual-drift numeric (bounded in N) is genuine positive evidence the lemma's
conclusion — hence `(★)` — is TRUE; but Round 3 is a stall on provability, the natural attack died, and the
proof needs an admissibility-cancellation no current tool supplies. Net hold. 🔴 Honesty rail: not a proof.

## NEEDS-HUMAN
NH1 (κ_A≤1/δ_A proof in 2510.20301); NH2 (BV constants non-poly — confirmed); **NH3 (Betke-797 `κ·2^{3r/2}`
attribution)**; P5 hand-proof audit.
