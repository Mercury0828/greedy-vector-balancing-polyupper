# Round-2 RESPONSE — GPT-5.5-Pro (verbatim) + orchestrator header

> **Orchestrator header.** Solver = web GPT-5.5-Pro, owner-relayed, received 2026-06-22. Verdict:
> **PARTIAL — `(★)` neither closed nor refuted; confidence 93%.** Major forward progress:
> - **NEW THEOREM (positive, polynomial).** *Theorem 1:* every realizable arrangement chamber `C_s` has a
>   margin-one dual certificate `p_s` of norm `O(r²/δ_T²)` (explicit `R_loc = √(r(r+1))(1+(r+1)κ)/δ`,
>   `κ≤1/δ`). Proof = Carathéodory + circuit-imbalance (P3′) + P1. → candidate **P7**.
> - **EXACT REFORMULATION of G1.** *Prop 2:* `(★)`/G1 ⟺ the local certificates can be patched into a
>   **bounded, cyclically monotone, 0-homogeneous selection** `p(y)∈P_{sign(Aᵀy)}` (= subgradient field of
>   one convex `F` with `F(y)≤poly·‖y‖`). Local feasibility is done (Thm 1); **integrability is the gap.**
> - **OBSTRUCTION (rank 3, constant δ).** *§3:* with `⟨t_i,t_j⟩=3/4` (δ_T=√(5/14)≈0.598), NO convex `F`
>   linear on the 8 original chambers exists → "one fixed certificate per original chamber" is DEAD; any
>   proof must refine the fan or carry history. → candidate refuted route **N2**.
> - **PRECISE REMAINING LEMMA.** *§4–5:* the **bounded dual-drift lemma** — run `p_{j+1}=Proj_{P_{s_{j+1}}}(p_j)`
>   along a reversed projection trajectory; if `sup_j‖p_j‖ ≤ poly(r,1/δ)` then (summation by parts) the TV is
>   `≤ poly·‖y_0‖` and `G(T) ≤ 2D`. This IS `(★)` now.
> - No constant-δ super-poly family found; recursive amplifiers force δ exponentially small (not a refutation).
>
> Triage: this is a normal (non-closure) reply with strong progress → audits = numeric (`code/round2_audit_checks.py`)
> + 1 fresh-context analytic agent. Classify in `docs/round2_audit.md`.

---

## VERBATIM REPLY

## Verdict first
I do **not** close or refute (★). I do prove a polynomial theorem that solves the **local** part of both G1 and G2:
> **Every arrangement chamber has a margin-one dual certificate of norm O(r²/δ_T²).**
The remaining obstruction is purely global: these bounded certificates must be patched into a cyclically monotone field, or kept bounded under a particular history-dependent projection process. A constant-δ, rank-three example proves that assigning one fixed certificate to each original chamber cannot work.

## 1. Polynomial chamber certificates
Choose one representative t_1,…,t_m from every unoriented line in T, write δ=δ_T. Let κ = circuit imbalance of A=[t_1 … t_m]. From the frozen substrate, κ ≤ 1/δ.
For every realizable sign pattern s∈{±1}^m, define v_i=s_i t_i, the closed chamber C_s={x:⟨v_i,x⟩≥0 ∀i}, and its margin-one certificate polyhedron P_s={p:⟨v_i,p⟩≥1 ∀i}.

### Theorem 1: polynomial local margin
For every realizable chamber C_s, P_s ∩ B(0,R_loc) ≠ ∅, where
  R_loc = √(r(r+1))(1+(r+1)κ)/δ ≤ (r+2)√(r(r+1))/δ² = O(r²/δ²).
Moreover, the certificate can be chosen in cone{v_1,…,v_m}.

**Proof.** Let M=[v_1 … v_m]. Since s is realizable, ∃y with ⟨v_i,y⟩>0 ∀i; consequently ker M ∩ ℝ_+^m={0}, so 0∉conv{v_i}. Let z_* be the closest point to 0 in this hull. By Carathéodory ∃ J, k:=|J|≤r+1, λ∈ℝ_+^J with 1ᵀλ=1, z_*=M_J λ.
Lower-bound dist(λ, ker M_J): take w∈ker M_J. Every kernel vector has a conformal circuit decomposition; since ker M_J ∩ ℝ_+^J={0}, every nonzero circuit has both signs. Circuit imbalance ≤κ and support ≤k give
  ‖w_+‖_1 ≤ kκ‖w_−‖_1,  ‖w_−‖_1 ≤ kκ‖w_+‖_1.   (1)
Set d=‖λ−w‖_1. Since λ≥0, ‖w_−‖_1≤d. Also Σ_i w_i ≥ Σ_i λ_i − ‖λ−w‖_1 = 1−d, so ‖w_+‖_1≥1−d. Using (1): 1−d ≤ ‖w_+‖_1 ≤ kκ‖w_−‖_1 ≤ kκ d. Thus d ≥ 1/(1+kκ). Since ‖u‖_1≤√k‖u‖_2,
  dist_2(λ, ker M_J) ≥ 1/(√k(1+kκ)).   (2)
Let q=rank M_J ≤ r, choose q independent columns B of M_J spanning its column space. Since M_J M_Jᵀ ⪰ BBᵀ on that space, P1 gives
  σ_q(M_J) ≥ σ_min(B) ≥ δ/√q.   (3)
Combining (2),(3): ‖z_*‖ = ‖M_J λ‖ ≥ σ_q(M_J)·dist_2(λ,ker M_J) ≥ δ/(√(qk)(1+kκ)) ≥ δ/(√(r(r+1))(1+(r+1)κ)).   (4)
Closest-point optimality: ⟨z_*, v_i−z_*⟩≥0 ∀i, so ⟨z_*,v_i⟩≥‖z_*‖². Therefore p_s:=z_*/‖z_*‖² satisfies ⟨p_s,v_i⟩≥1 ∀i, lies in cone{v_i}, and ‖p_s‖=1/‖z_*‖ ≤ R_loc by (4). ∎
(Incidentally p_s is the minimum-norm point of P_s: every p∈P_s has 1≤⟨p,z_*⟩≤‖p‖‖z_*‖.)

## 2. Exact convex-analytic form of G1
Let F be finite convex even positively homogeneous = support function of a symmetric convex body; F(y)≤R‖y‖ ⟺ that body has radius ≤R. For generic y∈int C_s consider
  ∇F(y)∈P_s,  i.e.  s_i⟨t_i,∇F(y)⟩≥1 ∀i.   (5)

### Proposition 2: gradient margins ⟺ projectivity
Equivalent (a.e. gradient sense): F(y) ≥ F(π_t y)+|⟨t,y⟩| ∀t∈T,y   (6), and condition (5) in every chamber.
**Proof.** Fix t, z=π_t y, y=z+at, z⊥t, φ(a)=F(z+at). If (6) and a>0: φ'(a) ≥ (φ(a)−φ(0))/a ≥1; for a<0, φ'(a)≤−1 — exactly (5). Conversely if (5) a.e.: along z+at the sign of ⟨t,z+at⟩ stays positive even crossing other walls, so φ'(a)≥1 a.e. for a>0, integrate ⇒ F(z+at)−F(z)≥a; negative side identical ⇒ (6). ∎
Therefore G1 ⟺ finding a bounded, cyclically monotone, zero-homogeneous selection p(y)∈P_{sign(Aᵀy)}. Theorem 1 proves the multifunction has bounded values locally (P_s∩R_loc B_2≠∅). It does NOT prove these can be selected cyclically monotonically (as the subgradient field of one convex function). Local feasibility is cheap. Integrability is where geometry sends the invoice. If the local points could be patched without increasing norm, P4 would give
  G(T) ≤ (r+2)√(r(r+1))/δ_T² = O(r²/δ_T²).   (7)

## 3. Why one fixed certificate per chamber cannot work
Rank three, constant δ_T. Let t_1,t_2,t_3 unit with ⟨t_i,t_j⟩=c=3/4 (i≠j). Gram G=(1−c)I+c·11ᵀ, (G^{-1})_{ii}=(1+c)/((1−c)(1+2c))=14/5. Therefore δ_T=√(5/14)≈0.598.
Suppose F even convex positively homogeneous, linear on each of the 8 original chambers, chamber gradient p_s. Continuity across wall t_i^⊥ forces the gradient jump across that wall ∥ t_i; codim-2 compatibility forces jump size independent of the other two signs; convexity makes it ≥0; evenness gives
  p_s = Σ_{i=1}^3 w_i s_i t_i  (w_i≥0).   (8)
For each j take the chamber with s_j opposite the other two signs; margin gives
  w_j − c Σ_{i≠j} w_i ≥ 1.   (9)
Summing over j: (1−2c)Σ_i w_i ≥ 3. But c=3/4 ⇒ LHS = −½ Σ w_i ≤ 0, contradiction.
Thus even at constant δ_T, no convex potential linear on the original chambers need exist. Any successful construction must refine the chamber fan, use gradients varying inside a chamber, or carry genuine history.

## 4. A precise history-dependent G2 formulation
Reverse a finite projection trajectory; reversed vertices satisfy x_j=x_{j−1}+α_j t_j, ⟨x_{j−1},t_j⟩=0   (10). Split every segment at every arrangement-wall crossing → smaller segments d_j=x_j−x_{j−1}, each open segment in one chamber C_{s_j}. For any p_j∈P_{s_j}, the movement direction agrees with the chamber sign, so
  ⟨p_j,d_j⟩ ≥ ‖d_j‖.   (11)
Initialize p_1∈P_{s_1}∩R_loc B_2 and update
  p_{j+1} = Proj_{P_{s_{j+1}}}(p_j).   (12)
At a transition x_j∈C_{s_{j+1}}. But rec(P_s)={q:⟨s_i t_i,q⟩≥0 ∀i}=C_s. Hence p_{j+1}+λ x_j∈P_{s_{j+1}} ∀λ≥0. Metric-projection optimality on this ray gives
  ⟨p_j−p_{j+1}, x_j⟩ ≤ 0.   (13)
Using (11) and summation by parts:
  Σ_{j=1}^N ‖d_j‖ ≤ Σ_j ⟨p_j, x_j−x_{j−1}⟩ = ⟨p_N,x_N⟩ − ⟨p_1,x_0⟩ + Σ_{j=1}^{N−1}⟨p_j−p_{j+1},x_j⟩ ≤ ‖p_N‖‖x_N‖+‖p_1‖‖x_0‖.   (14)
Both endpoint norms ≤ initial norm of the forward trajectory. Consequently:

### Bounded dual-drift lemma (the exact remaining lemma)
> There is D=poly(r,1/δ_T) such that, for every chamber itinerary induced by a reversed orthogonal-projection trajectory, the sequence (12) initialized with ‖p_1‖≤R_loc satisfies sup_j‖p_j‖≤D.
By (14) this implies Σ_k‖y_k−y_{k−1}‖ ≤ 2D‖y_0‖, hence G(T) ≤ 2D.
This is genuinely history-dependent: p_j remembers how the chamber was entered. It pinpoints why Theorem 1 alone is insufficient — every P_s meets a polynomial ball, but successive projections onto these unbounded polyhedra could drift along recession directions. KKT decomposes (12) into projection onto an active affine face whose normals are signed members of T; this falls into the same hierarchy as quantitative affine-projection orbit problems. Known general bounded-variation + recent innate-regularity results for affine projection orbits give only qualitative boundedness, not the polynomial dependence needed.

## 5. The remaining lemma in its cleanest static form
> **Bounded cyclic-monotone selector lemma.** For the arrangement generated by T, there exists an even convex positively homogeneous F with ∂F(x)∩P_s≠∅ for x∈C_s, and F(x)≤poly(r,1/δ_T)‖x‖.
Equivalently at differentiability points: sign⟨t_i,x⟩·⟨t_i,∇F(x)⟩≥1 ∀i.
Theorem 1 proves pointwise feasibility with norm O(r²/δ_T²). The rank-three example proves cyclic monotonicity cannot generally be achieved without refining the original chamber fan or adding history.
I found no constant-δ super-polynomial family, and the standard recursive projection amplifiers continue to create an exponentially small δ_T, rather than refuting (★).

**Verdict: PARTIAL. Polynomial local certificates established with radius O(r²/δ_T²); (★) remains open exactly at bounded cyclic-monotone patching, equivalently the dual-drift lemma above. Confidence: 93%.**
