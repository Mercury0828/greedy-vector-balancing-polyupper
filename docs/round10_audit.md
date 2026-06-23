# Round-10 AUDIT — freeze P15 (closed sub-classes); hard region tested CLEAN; confidence ~76%

> Independent audits of `docs/round10_response.md`: (1) orchestrator numeric (`code/round10_audit_checks.py`,
> `round10_deficient_pct.py`); (2) fresh-context theorem auditor (re-derived all algebra + fresh numerics).
> **Bottom line: all Round-10 claims CORRECT (no errors) — freeze the P15 closed-class package. The pinned
> hard region (deficient-block PCT gap on the Hadamard family) was tested decisively and is CLEAN (γ does NOT
> collapse). Converging; confidence ~76%.**

## Classification

### PROVEN — freeze as the P15 package (all VALID per both audits)
- **P15a — round-partitioned schedules.** Any schedule that is a sequence of full permutations (each round
  uses every coordinate once) ⟹ `sup‖p‖ ≤ 4r⁴/δ³ + 2r/δ` (Fejér-monotone to the round fixed point). Closed.
- **P15b — Theorem 1 (comparison-stable).** `B=|G−I|`; `ρ(B)≤1−η` ⟹ `sup‖p‖≤r/η`, `c^⊤Gc≤r²/η²`
  (per-coordinate total variation `V≤b+BV`, `(I−B)^{-1}≥0`, transferred to the affine orbit). **Corollary
  (sign-switchable obtuse):** `∃D` diag-sign with `DGD` off-diag ≤0 ⟹ `η≥λ_min(G)≥δ²/r` ⟹ `sup‖p‖≤r²/δ²`.
- **P15c — Theorem 2 (equicorrelation).** `G_α=(1−α)I+α11^⊤` ⟹ `c^⊤Gc ≤ 2r³/δ²+r²` (explicit invariant
  polytope `|Σ_{S}c_j|≤F_{|S|}`, exact recursion `F_s=1+(1−α)F_{s-1}+αF_{r-s}`).
- **P15d — PCT cycle-gap bounds + palindrome reduction.** `γ(R)=1−‖P_{i_m}…P_{i_1}‖²`: universal
  `γ≥δ^{2r}/r^{r-1}`, permutation `γ≥δ²/r³`. **Palindrome bridge (verified exact, incl. `BB^⊤=I−Q²`):** a
  constant-δ family with `γ→r^{-ω(1)}` ⟹ explicit BST counterexample (`sup‖p‖²≥(2−γ)/γ`, realizable by a
  directed sign schedule). So PCT is strictly weaker than BST AND a valid refutation route.
- *Auditor:* all correct; only looseness (the `‖W‖_F^{r-1}` and `4r⁴/δ³` constants), nothing load-bearing.
  Genuine new closed sub-classes + a valid two-way bridge — real progress, not relabeling.

### DECISIVE de-risk — the pinned hard region tested CLEAN
- The one genuinely-open quantity (auditor's rec (e)): can **DEFICIENT-block** full words drive `γ`
  super-poly small on the well-conditioned hard family? Numeric (`code/round10_deficient_pct.py`, a
  deficient-block-aware adversary maximizing `‖product‖`):
  - **signed-Hadamard family** (δ≈0.97, comparison fails Θ(√r)): min γ(deficient) ≈ **0.90, FLAT in r**
    (r=4..32, log-log slope −0.009) — Ω(1), ≫ δ²/r³ (1e-2..1e-5).
  - random well-conditioned (δ 0.25–0.51): min γ = 0.19→0.027 (~1/r, polynomial), still ≫ δ²/r³.
  - **VERDICT: γ stays ≥ 1/poly, no super-poly collapse ⟹ NO refutation; via the palindrome bound
    `sup‖p‖²≈2/γ` stays poly ⟹ BST holds on the pinned hard region.**
- Plus (Round-10 main numeric): BST adversary on the Hadamard family `sup‖p‖ ~ √r` to **r=64**; the natural
  nested-palindrome amplifier provably collapses δ (`δ≈a^m`). All point to BST TRUE.

### Status / convergence
- Easy regions CLOSED (comparison-stable, equicorrelation, permutation/round schedules); the natural amplifier
  self-defeats; the danger was concentrated on deficient-block/Hadamard — and that tested clean. This is real
  triangulation. **Still no PROOF of general BST** — the missing step (Answer-1 §5) is a γ lower bound for
  arbitrary deficient blocks (≡ a depth-independent Meshulam constant). The numerics now strongly suggest it
  holds; a proof is what remains.

## Confidence
**~74% → ~76%** (B-side / `(★)` true). The decisive deficient-block test on the exact hard family came back
clean (γ flat/poly, no collapse); BST `√r` to r=64; every refutation route across 10 rounds dead; amplifiers
collapse δ. Tempered: still a heuristic search (not a proof), BST/PCT-γ unproven. Auditor independent ~73%;
I weight the hard-region-clean evidence slightly higher → ~76%. 🔴 Nothing frozen as "proved" beyond P11–P15,
D_exp. No matching lower bound — do NOT claim "tight/optimal".

## Next (recommended)
**Round 11 = prove BST on the now-strongly-supported hard region** — specifically a `poly(r,1/δ)` LOWER BOUND
on the PCT gap `γ` for arbitrary (deficient-block) full words on a well-conditioned `G` (≡ a depth-independent
Meshulam/paracontraction constant). Closure mandate stands; the numerics give a strong prior that it is true
and that any proof attempt is not chasing a false statement. Pair with a dedicated lit pass on
quantitative/poly-depth Meshulam & paracontraction rates. Brief: `docs/round11_brief.md`.

## NEEDS-HUMAN
NH1–NH6; the deep step = a depth-independent (poly) lower bound on the PCT gap for deficient-block words on
well-conditioned `G` (≡ quantitative Meshulam) — numerically supported, proof open.
