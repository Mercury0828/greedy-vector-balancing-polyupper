# Round-5 AUDIT — independent fresh-context adversarial verdict

> Independent line-by-line audit of `docs/round5_response.md` (fresh GPT-5.5-Pro escalation).
> Numeric: `code/round5_audit_checks.py` → `code/round5_audit_results.json` (seed 20260622) + ad-hoc
> arithmetic/energy checks. Literature: live WebFetch of arXiv:2506.22553 (HTML v2) + 2602.00544 (HTML).
> **Bottom line: all five claims VALID. CLAIM 3 (rank≤2) is a genuine new VERIFIED base case worth
> freezing. CLAIM 2 (D_exp) is a correct all-word bound. CLAIM 4 (cocycle) is a faithful, real
> sharpening. CLAIM 1's literature citation is accurate AND newly relevant (the paper DOES cover
> polyhedra in finite dim), but the qualitative inference must be stated carefully (see below).**

## CLAIM 1 — Bauschke–Tung (§1 qualitative all-word boundedness) — VALID, with one scoping note

- **(a) Do the papers establish boundedness of arbitrary projection orbits?** YES.
  arXiv:2506.22553 (Bauschke–Tung, "On a result by Meshulam", subm. 2025-06-27) extends Meshulam's 1996
  theorem. **Meshulam 1996:** every sequence of projections onto affine subspaces drawn from a finite
  collection in Euclidean space is bounded. Confirmed verbatim from the abstract.
- **(b) Does it cover POLYHEDRA, not just affine subspaces?** YES — this is exactly the paper's
  contribution. Abstract (verbatim): *"we extend his result not only from affine subspaces to convex
  polyhedral subsets, but also from Euclidean to general Hilbert space."* **Theorem 2.5** (finite-dim) gives
  boundedness for arbitrary sequences of (relaxed) projections onto a finite collection of nonempty
  polyhedral sets, λ∈[0,2[. The mechanism is exactly as the solver states: **Corollary 2.3** establishes
  `P_C x = P_{aff F} x` for the reached face F, reducing the polyhedron orbit to a finite-affine-family
  orbit and invoking Meshulam (Fact 1.1). So the solver's "projection onto the affine hull of the reached
  face" is the paper's actual proof strategy, not an over-reading. **Our P_s are exactly polyhedra ⟹
  legitimately covered.**
- **(c) Is the inference "fixed arrangement cannot cusp; any refutation must be a FAMILY T_r"
  valid?** YES, and it is the correct logical reading. For each FIXED T the sup over all chamber words is a
  finite constant `D(T)<∞` (Meshulam/B–T). Hence no single fixed arrangement can produce z_j→0; a
  super-poly refutation must come from a FAMILY where `D(T_r)` grows super-polynomially in (r,1/δ). This
  re-frames the open problem without resolving it — fair.
- **Constant is NOT polynomial.** CONFIRMED. 2506.22553 gives only a qualitative existence statement
  ("the sequence is bounded"), no explicit constant; the "sharpness examples" characterize when bounds
  FAIL, not a rate. 2602.00544 (Bauschke–Tung, infinite-dim, affine subspaces only) is explicit that the
  constant `C_{A,λ}<+∞` exists non-constructively (Corollary 4.4: `‖x_n‖≤‖x_0‖+λC_{A,λ}`), no formula, and
  requires "innate regularity" (automatic in finite dim). So the cited results give NO polynomial-in-(r,1/δ)
  control — exactly why they cannot close the lemma and the project's whole effort is needed.
- **Scoping note (not a defect, a precision):** 2602.00544 is affine-subspaces-only; the POLYHEDRA
  extension lives in 2506.22553. The solver cites both for §1; only 2506.22553 carries the polyhedral
  claim. Minor — the load-bearing citation (2506.22553) is correct.

**Verdict CLAIM 1: VALID.** Citations accurate, scope correct (polyhedra ARE covered in finite dim),
inference valid, constants confirmed non-polynomial.

## CLAIM 2 — all-word bound D_exp (§2) — VALID (correct, exponential-in-r)

- **Step 1 (two-flat regularity, eq 1).** The inequality `d_{M∩N}(x)² ≤ (d_M²+d_N²)/(1−cos φ)` with φ the
  Friedrichs angle is the standard estimate. `1−cos φ ≥ ½ sin²φ` holds for ALL angles (⟺ cos φ≤1; verified
  algebraically: `1−c ≥ ½(1−c²)=½(1−c)(1+c) ⟺ 2≥1+c`). With `sin φ ≥ δ/r` (B3) this gives
  `d_{M∩N} ≤ √(2/((½)(δ/r)²))·max = 2(r/δ)·max`. **So K = 2r/δ is EXACTLY right** (computed: K_implied =
  2r/δ to machine precision for several (δ,r)). Numeric: `d_{A^⊥∩B^⊥}/(K·max) ≤ 0.354` over 400 random
  T-spanned pairs, 0 violations, and the underlying `d_{M∩N}²≤(d_M²+d_N²)/(1−cos)` held with 0 violations
  over 20000 random subspace pairs.
- **Step 2 (block contraction, eq 3).** The W_i flag argument is sound: σ_{W_i} can only be raised when the
  cumulative intersection strictly drops, which happens ≤ k−1 times; W_n={0} forces a definite energy loss.
  The conclusion `‖Q‖ ≤ β_k = 1/√(1+K^{−2(k−1)})` follows from the energy identity
  `‖x_0‖²−‖x_n‖² ≥ K^{−2(k−1)}‖x_n‖²`. **DIRECTLY VERIFIED** by independent simulation: over 3996 random
  full-rank blocks (intersection exactly {0}), the energy inequality held with 0 violations (min margin
  +1.6e−3), where K was derived purely from CUMULATIVE-ORIGINAL-FLAT angles `angle(W_{i−1},V_i)`. And the
  end bound `‖Q‖≤β_k` held with 0 violations (worst `‖Q‖−β_k = −0.031`). **CRUCIAL POINT CONFIRMED:** the
  argument uses ONLY angles between the cumulative original flat `span(H_1..H_{i−1})` and the next ORIGINAL
  `H_i` — never the dynamically-projected images `R_jH_j`. This genuinely sidesteps dead route 2 (the angle
  collapse of projected images), which was the central failure of Round 3.
- **Step 3 (recursion, eq 4).** All arithmetic verified exactly:
  `1/(1−β_k) = √(1+a²)(√(1+a²)+1)/a²` (a=K^{−(k−1)}) — exact; `< 4K^{2(k−1)}` — holds (checked across
  K∈[1,50], k∈[2,7], 100k samples, 0 failures). `G_k ≤ 5K^{2(k−1)}G_{k−1}` with `G_1≤2R_0` telescopes to
  `G_r ≤ 2R_0·5^{r−1}·K^{r(r−1)}`; the exponent `Σ_{k=2}^r 2(k−1) = r(r−1)` confirmed symbolically (sympy).
- **Caveat (honest, already stated by solver):** D_exp is polynomial in 1/δ at FIXED r (degree r(r−1)+1)
  but EXPONENTIAL in r (the 5^{r−1}·K^{r(r−1)} factor). It is NOT the target poly(r,1/δ) bound. It is a
  correct, clean, no-admissibility all-word ceiling — useful as the inductive scaffold, not the goal.

**Verdict CLAIM 2: VALID.** Correct all-word bound. The "avoids dead route 2" property is real and verified.

## CLAIM 3 — rank ≤2 CLOSED (§3) — VALID, RIGOROUS, NEW base case (freeze)

- **(i) Case split exhaustive?** YES. r=1 is immediate (E is a line; `P_{H^⊥}` kills it; `p_{j+1}=q_j`,
  `‖q_j‖≤r/δ`). r=2 adjacent transition splits on whether a common constraint is active:
  (A) **no common active** ⟹ B5 (frozen P9) gives `Δ≤0` (norm non-increasing) — done.
  (B) **common b_1 active AND Δ>0** ⟹ the flipped b_0 and the common b_1 are two distinct active
  T-members; in rank 2 two independent T-vectors span E, so `H_j=span(b_0,b_1)=E`, whence
  `P_{E^⊥}=0` (within E) and (B4/P8) `p_{j+1}=q_j`, `‖q_j‖≤r/δ`.
  The only escape from (A)∪(B) is "common b_1 active, b_1 ∥ b_0" — but parallel walls are merged at the
  outset ("after merging parallel copies of the same wall"), so b_0,b_1 distinct ⟹ independent in rank 2.
  Split is exhaustive given the merge convention.
- **(ii) Does `p_{j+1}=q_j` really hold when H_j=E?** YES. By the frozen exact dynamics P8/B4
  `p_{j+1}=P_{H_j^⊥}p_j+q_j`; if `H_j=E` then within E `P_{E^⊥}=0`, so `p_{j+1}=q_j` with `q_j∈H_j=E`,
  `‖q_j‖≤r/δ`. Correct.
- **(iii) "two distinct central walls cross only at 0":** in rank 2, two distinct lines (1-dim flats =
  walls through origin) meet only at {0}. A simultaneous active-crossing of both at a point x≠0 is therefore
  impossible. On a norm-MONOTONE reversed trajectory with `‖x_j‖` nondecreasing and x_0≠0, every later point
  has `‖x_j‖>0`, so the degenerate double-crossing cannot occur at any later j. This correctly rules out the
  one remaining problematic configuration for ALL j. No gap found.
- **NUMERIC corroboration (decisive for tightness):** simulated the r=2 dual process (direct metric
  projection onto `P_s`) over random rank-2 T and random feasible itineraries, length 60. `sup_j‖p_j‖`
  stayed ≤ `2/δ` in EVERY case (0 violations), and the worst ratio sup/bound = **0.9971** — i.e. the bound
  `r/δ` is essentially SATURATED, confirming both correctness and sharpness.

**Verdict CLAIM 3: VALID & RIGOROUS.** This is a genuinely new closed base case (prior frozen results
only had the r/δ *certificate* P7, not a closed *orbit* bound at any rank). Freeze as **P11 (rank≤2
closure, sup_j‖p_j‖ ≤ r/δ)**. Depends on P8 (dynamics) + P9 (B5/Δ≤0) — both already frozen-valid.

## CLAIM 4 — cocycle reduction (§5) — VALID, faithful sharpening

- **Telescoping algebra.** If `b_B = c_τ − Q_B c_σ` for each block, then `A_B(p)−c_τ = Q_B(p−c_σ)`, and
  composing consecutive blocks gives `p_N − c_{σ_N} = Q_{B_N}⋯Q_{B_1}(p_0 − c_{σ_0})`. Since each Q_B is a
  product of projectors (`‖Q_B‖≤1`), `‖p_N−c_{σ_N}‖ ≤ ‖p_0−c_{σ_0}‖`, hence `‖p_N‖ ≤ R_0 + 2C` with
  `‖c_σ‖≤C`. **VERIFIED numerically exact** (max residual `‖p_N − (c_{σ_N}+Q_{prod}(p_0−c_{σ_0}))‖ ≈ 1e−14`
  over 2000 random instances). Closed-block form `b_B=(I−Q_B)c_σ` is the σ=τ specialization — correct, and
  it does remove the dangerous inverse spectral gap (b_B already carries the I−Q_B factor).
- **Is it a FAITHFUL reduction?** The forward direction (cocycle (5) ⟹ poly bound, given ‖c_σ‖≤poly AND
  finitely-many memory states σ) is rigorous as above. The reverse/necessity ("poly bound ⟹ such c_σ
  exist") is the *natural* cohomological converse (a bounded cocycle is a coboundary) but is stated, not
  re-proved in detail here; it is plausible and standard in spirit. So **"(★) ⟺ cocycle (5)"** is fair as a
  *route-equivalence* — slightly stronger than what is fully written (the ⟸ is airtight; the ⟹ relies on
  the unstated coboundary/finiteness argument). Not overstated in any harmful way: it correctly identifies
  the precise algebraic obstruction (relate b_B to the near-invariant directions of Q_B, not merely bound
  ‖b_B‖ — matching the §4 break-point that repeated ‖b_B‖ bounding costs `(1−‖Q_B‖)^{−1}≍K^{Θ(r²)}`).
- **Exact-J-cluster supporting structure.** Correct: if every `H_j⊆J` and `q_j∈J`, then `P_{J^⊥}p_j` is
  invariant (projectors and translations act inside J) while `P_J p_j` runs the lower-rank dual process
  inside J. This is a clean inductive hook. The genuinely unresolved piece (solver is honest about it) is
  the entry/exit memory state across *approximate* clusters and repeated revisits.
- **Cocycle-refutation probe.** Over closed cyclic chamber blocks, the would-be super-poly affine fixed
  cycle `‖(I−Q_B)^† b_B‖` stayed at the `r/δ` scale (r=2: 1.96 vs r/δ=2.28; r=3: 6.45 vs r/δ=8.28) — no
  super-poly blowup found, consistent with (★) TRUE.

**Verdict CLAIM 4: VALID.** Faithful, and a real sharpening: it converts the open lemma into a concrete
algebraic identity with a clear refutation target (a repeatable admissible closed cluster with
`‖(I−Q_B)^† b_B‖` super-poly).

## FINAL ASSESSMENT

**(a) Is Round 5 genuine progress?** YES.
  - **rank≤2 closure (CLAIM 3): NEW VERIFIED base case** — freeze as P11. The first closed *orbit* bound
    (not just a certificate) at any rank; rigorous, exhaustive, and numerically saturates r/δ.
  - **D_exp (CLAIM 2): correct all-word bound** — verified end to end, and crucially it is the FIRST
    estimate in the project that legitimately avoids dead route 2 (uses original-flat angles only). Not the
    target (exponential in r), but a sound scaffold.
  - **Cocycle reduction (CLAIM 4): real sharpening** — pins the obstruction to one algebraic cocycle
    identity with an explicit refutation target.
  The escalation to fresh context paid off (consistent with the round-4 audit's escalation rationale).

**(b) Does this suggest a viable RANK INDUCTION?** Plausibly. The exact-J-cluster structure (P_{J^⊥}p
invariant, P_J p runs the lower-rank process) plus the closed rank≤2 base is exactly the shape of an
r→r+1 induction. **Single most promising path: (ii) a rank induction building on §3 + the J-cluster
structure**, with the inductive step *being* the cocycle identity (i) restricted to the new top stratum.
I.e. (i) and (ii) are not really competitors — the cleanest program is: assume the poly bound at rank ≤ r
(base r=2 = P11), then for rank r+1 use the J-cluster decomposition to run the rank-r bound inside each
proper J, and prove the cocycle identity (5) ONLY for the genuinely-top-rank ("full-span") blocks, where
the memory state σ is the nested cluster flag. The crux is unchanged from round 4 (entry/exit memory
across approximate clusters / revisits), now stated as the cocycle coboundary condition — that IS the
deep step and remains unproved. The §2 block-contraction shows full-span blocks contract by β_k; what's
missing is that the per-block translations b_B coboundary-cancel rather than accumulate the
`(1−β_k)^{−1}≍K^{2(k−1)}` factor.

**(c) Confidence the full polynomial lemma is TRUE.** I concur with the project's ~75% (solver's 72% is
also reasonable). Pushing toward TRUE: rank≤2 now genuinely closed; D_exp confirms a clean (if
exponential) ceiling via the previously-dead angle route; the cocycle/fixed-cycle probe and the round-4
refutation hunt both fail to find any super-poly accumulation; numerics saturate exactly at r/δ. Tempering:
the deep step (cocycle identity / cluster return-point) genuinely does not exist yet, the rank-3
obstruction N2 shows static one-certificate-per-chamber is impossible (so the induction MUST be
history-dependent), and all positive evidence is heuristic/lower-bound. **Independent recommendation: 75%.**
Not a proof; nothing here should be frozen as "proved" beyond P11 (rank≤2) and the D_exp all-word bound.

### URLs fetched
- https://arxiv.org/abs/2506.22553 (Bauschke–Tung, "On a result by Meshulam")
- https://arxiv.org/html/2506.22553v2
- https://arxiv.org/pdf/2506.22553
- https://arxiv.org/html/2602.00544 (Bauschke–Tung, infinite-dim affine extension)
