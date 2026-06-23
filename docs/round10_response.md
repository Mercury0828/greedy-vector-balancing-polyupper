# Round-10 RESPONSE — GPT-5.5-Pro (targeted BST, verbatim) + orchestrator header

> **Orchestrator header.** Targeted BST attack, fresh context, owner-relayed, 2026-06-23. TWO answers
> (consistent + complementary). **Neither closes BST.** Both put BST-true at **~68–69%**. Net (to audit):
> - **NEW closed sub-classes (freezable):** (a) any **round-partitioned** schedule (each round = every
>   coordinate once) ⟹ `sup‖p‖ ≤ 4r⁴/δ³` (Fejér to the round fixed point `z_s`); (b) **Thm 1**
>   comparison-stable / sign-switchable-obtuse bases (`ρ(|G−I|)≤1−η` or `∃D: DGD` off-diag ≤0) ⟹
>   `sup‖p‖ ≤ r/η`, and for obtuse `≤ r²/δ²`; (c) **Thm 2** equicorrelation `G_α` ⟹ `c^⊤Gc ≤ 2r³/δ²+r²`
>   (explicit invariant polytope). → candidate **P15** (the closed-class package).
> - **PCT (strictly weaker target + refutation route):** `γ(R)=1−‖P_{i_m}…P_{i_1}‖² ≥ poly^{-1}(r,δ)` for
>   every full word; PALINDROME mechanism: a super-poly-small `γ` ⟹ explicit BST counterexample
>   (`sup‖p‖² ≥ (2−γ)/γ`). Proven: universal `γ ≥ δ^{2r}/r^{r-1}`; permutation `γ ≥ δ²/r³`.
> - **Hard region PINNED to a concrete explicit family:** signed Sylvester–Hadamard `G_r=I+(H_r−D_r)/(4√r)`
>   — δ≥√(5/8) (excellent, constant) yet comparison-stable fails by `Θ(√r)` and equicorrelation doesn't
>   apply. Neither solver settled it. A counterexample must use **deficient blocks** (repeated coords before
>   the last missing coordinate).
> - **More evidence BST TRUE:** the natural nested-palindrome amplifier collapses δ exponentially (depth
>   O(log r) ⟹ only poly amplification) — again no constant-δ amplifier.
> Triage: real new theorems + a clean refutation route (PCT/palindrome) + a concrete open test (Hadamard).
> Next: numeric on Hadamard/deficient-blocks/PCT-gap (the pinned hard region) + audit + Round-11 (Hadamard/PCT).

---

## ANSWER 1 (verbatim) — cycle-gap dichotomy / PCT

No proof/refutation of BST. Strictly-easier unresolved statement: the homogeneous **PCT** —
`1 − ‖P_{i_m}…P_{i_1}‖² ≥ poly^{-1}(r,δ^{-1})` for every finite word containing every index (`P_i=I−t_i t_i^⊤`).
No translations/signs/invariant bodies/orbit boundedness ⟹ genuinely weaker than BST; a super-poly failure of
PCT AUTOMATICALLY refutes BST.

**Cycle-gap dichotomy.** `R=P_{i_m}…P_{i_1}` (all r coords), `γ(R)=1−‖R‖²`.
- Universal: `γ(R) ≥ δ^{2r}/r^{r-1}` (1). Permutation (each coord once): `γ(R) ≥ δ²/r³` (2).
- Palindrome: if a poly-δ family has full words with `γ(R_r)=r^{-ω(1)}`, BST is FALSE — an explicit periodic
  sign schedule has `sup_k‖p_k‖² ≥ (2−γ)/γ` (3).
*Proof of (1):* Bessel `I−R^⊤R=Σ_k v_k v_k^⊤`, `v_k=P_{i_1}…P_{i_{k-1}}t_{i_k}` (4). First-occurrence vectors
`w_1..w_r`; Gram–Schmidt `u_j` of `t_{π_1}..t_{π_r}`; `⟨u_j,w_j⟩=dist(t_{π_j},span{earlier})≥δ` (5); `W=[w_j]`
triangular in the `u`-basis, diag ≥δ ⟹ `|det W|≥δ^r` (6), `‖W‖_F≤√r` ⟹ `σ_min(W)≥δ^r/r^{(r-1)/2}` (7);
`I−R^⊤R⪰WW^⊤` ⟹ `1−‖R‖²≥σ_min(W)²≥δ^{2r}/r^{r-1}`. (Loss localized: triangular first-occurrence frame can be
exp ill-conditioned.) *Proof of (2):* permutation, `La=b` (`L` unit-lower-tri, `L+L^⊤=G+I⪰I`, `‖L‖≤r`) ⟹
`‖a‖≥δ/r^{3/2}‖x_0‖`; loss `=Σa_j²≥δ²/r³‖x_0‖²`.
**§2 PCT-failure ⟹ BST-false:** append reversal ⟹ palindrome `Q=R^⊤R⪰0`, `λ_max(Q)=‖R‖²=1−γ` (9);
`F_η(x)=Qx+Bη`, `BB^⊤=I−Q²` (10); repeating signed palindrome → `x_η=(I−Q)^{-1}Bη`;
`E_η‖x_η‖²=tr[(I+Q)(I−Q)^{-1}]≥(2−γ)/γ` (11)-(12). So super-poly-small γ ⟹ super-poly BST orbit. (PCT not
sufficient for BST: poly contraction per block doesn't control cross-block translations.)
**§3 polynomial schedule class:** round-partitioned schedules (each round uses every coord once, any
order/signs): `q=√(1−δ²/r³)`, round fixed point `z_s=A^{-⊤}s`, `‖z_s‖²≤r²/δ²` (13); `|F(x)|≤q|x|+(1+q)r/δ`
(14); iterating ⟹ `sup_k‖p_k‖ ≤ 4r⁴/δ³ + 2r/δ` (16) (Fejér-monotone within rounds). So repeated permutations
are harmless; any counterexample needs unboundedly long DEFICIENT blocks.
**§4 walk-summable:** `B=|offdiag(G)|`, if `max_i Σ_{j≠i}|G_{ij}|≤1−α` then box `|c_i|≤1/α` invariant ⟹
`c^⊤Gc≤r²/α²` (18); more generally `ρ(B)<1` ⟹ box `m=(I−B)^{-1}1` invariant. (Not implied by constant δ.)
**§5 exact unresolved step:** `γ(R)=λ_min(Σ_k v_k v_k^⊤)` (19); first occurrences give only (1); MISSING = the
extra vectors from REPEATED coords compensate the exp conditioning of the triangular first-occurrence frame —
a finite homogeneous frame bound, not an affine invariant body, NOT equivalent to BST.
**Verdict: GENUINELY STUCK.** Confidence: 97% derivations; **69% BST true.** (refs 2602.00544)

---

## ANSWER 2 (verbatim) — comparison-stable + equicorrelation theorems

No proof/refutation of BST. Two complete polynomial results + the natural amplifier fails.
**Theorem 1 (comparison-stable).** `B=|G−I|` entrywise; if `ρ(B)≤1−η` then `sup_k‖p_k‖≤r/η`, `c^⊤Gc≤r²/η²` (2).
*Proof:* homogeneous step `d^{m+1}=d^m−y^m_{i_m}e_{i_m}`, step length `|y^m_{i_m}|` (3)-(4); per-coord total
variation `V≤b+BV` (5) ⟹ `V≤(I−B)^{-1}b`, `‖(I−B)^{-1}‖₂≤1/η`, `‖b‖≤√r‖x_0‖` ⟹ `Σ‖steps‖≤r/η‖x_0‖` (6);
transfer to affine via reversed-word path length (7). ∎
**Corollary (sign-switchable obtuse):** if `∃D` diagonal sign with `G'=DGD` off-diag ≤0, then `‖G'−I‖=I−G'`,
`ρ=1−λ_min(G')`, `λ_min(G)≥δ²/r` ⟹ `η≥δ²/r` ⟹ `sup‖p‖≤r²/δ²`, `c^⊤Gc≤r⁴/δ⁴` (8).
**Theorem 2 (equicorrelation).** `G_α=(1−α)I+α11^⊤` ⟹ `c^⊤G_α c ≤ r³/(1−α)+αr² ≤ 2r³/δ²+r²` (10). *Proof:*
invariant polytope `K={c: |Σ_{j∈S}c_j|≤F_{|S|} ∀S}`, `F_s=s(1+α(r−1−s))/(1−α)` (11), exact recursion
`F_s=1+(1−α)F_{s-1}+αF_{r-s}` (16) ⟹ closure; `|c_i|≤F_1≤r/(1−α)`, `|Σc_i|≤F_r=r` ⟹ (19). `δ²≤2(1−α)` (20).
Outside Thm 1 (here `ρ(|G_α−I|)=α(r−1)≫1`).
**§3 amplifier fails:** nested palindrome `S_+=(S⊕I)P_t(S⊕I)`, eigenvalue `λ_+=1−a²(1−λ²)` (21) — multiplies
gap by ~2a²/level, but basis becomes exp ill-conditioned (`A^{-1}` rows ~`a^{-m}` ⟹ `δ≲a^m`); balancing ⟹
depth O(log r) ⟹ only poly amplification. Does NOT refute BST.
**§4 concrete open family:** signed Sylvester–Hadamard `G_r=I+(H_r−D_r)/(4√r)` (22): unit diag, `λ_min≥5/8`,
`δ≥√(5/8)` (23) — exceptionally well-conditioned constant δ — yet `ρ(|G_r−I|)=(r−1)/(4√r)=Θ(√r)` (comparison
fails by `Θ(√r)`), equicorrelation invariant lost (Hadamard signs break the 2-class recursion). Partial:
schedules on ≤`2√r` coords obey Thm 1 with η≥1/2. A super-poly orbit must use `>2√r` directions recurrently.
**NOT settled.**
**Verdict: genuinely stuck.** Confidence: 99% Thms 1&2; **68% BST true.** (refs 2606.17991)
