# Round-7 RESPONSE — GPT-5.5-Pro (fresh thread, verbatim) + orchestrator header

> **Orchestrator header.** Solver = web GPT-5.5-Pro (fresh thread), owner-relayed, 2026-06-22. Verdict:
> **PARTIAL+WHERE — the point-valued holonomy (OUR Round-7 ask) is REFUTED; `(★)`/bounded dual-drift is NOT
> refuted; confidence 98%.** Net (to be audited):
> - **REFUTES the point-cocycle `b_B=(I−Q_B)c_{J,ω}`:** two exact constant-δ (δ_T≈0.359) rank-4 admissible
>   excursions A,B from the SAME combinatorial J-state, SAME linear part `Q`, but **`b_A ≠ b_B`** ⟹ no single
>   common `c_{J,ω}`. Their fixed-point lines are parallel & disjoint (bounded nonzero holonomy = hysteresis).
> - **NOT a refutation of `(★)`:** both `A_A, A_B` keep a bounded **invariant cylinder** `C` invariant (each
>   maps `C` onto one of its two boundary lines), so arbitrary alternation stays bounded — no drift. Holonomy
>   is BOUNDED. (Positive structural finding, consistent with `(★)` TRUE.)
> - **Replacement crux (set-valued):** the **Polynomial invariant-cylinder theorem** — for each cluster state
>   σ (hidden survivor flat `V_σ`) a compact convex cross-section `C_σ⊂V_σ^⊥`, `sup‖c‖≤poly(r,1/δ)`, with
>   `A_B(C_σ+V_σ)⊆C_τ+V_τ`. Rank-4 form: an **invariant-strip sublemma** (common invariant interval of radius
>   poly(1/δ) on `K∩J^⊥`). Crux = polynomial bounded holonomy of the return semigroup (NOT zero/point-cocycle).
> Triage: this REFUTES our brief's ask (freeze N5), advances structure (bounded hysteresis), gives the exact
> replacement sublemma. Genuine progress, not a stall, not a refutation of `(★)`. → audit + Round-8 (or human expert).

---

## VERBATIM REPLY

## The requested point-valued holonomy is false
This does NOT refute bounded dual drift. It refutes the reduction to one common vector c_{J,ω}. Rank 4 already
exhibits genuine bounded hysteresis: different closed excursions from the same combinatorial J-state have
disjoint fixed-point lines.

### 1. A constant-δ rank-4 arrangement
Coordinates (a,b,c,d,e): a=(1,0,0,0), b=(0,1,0,0), c=(3,1,4,0)/√26, d=(1,3,−2,4)/√30, e=(−2,1,−3,−4)/√30.
Unit, span ℝ⁴. Exact Gram-determinant over all independent subsets: δ_T²=242/1875, δ_T≈0.359258>1/3, minimum
at dist(e, span{b,c,d})²=242/1875. Set J=span{a,b} (rank 2), K=span{a,b,e} (rank 3), J⊂K⊊E.
Chamber s_0=(+,+,+,−,−), certificate p_0=(1,1,6,0): signed values 1,1,28/√26,8/√30,19/√30 ⟹ p_0∈P_{s0}, active
face span = J, ‖p_0‖=√38<4/δ_T.

### 2. Two exact admissible closed excursions
For wall word W=(w_0,…,w_L), x_0∈w_0^⊥, α_k=−⟨x_k,w_{k+1}⟩/⟨w_k,w_{k+1}⟩, x_{k+1}=x_k+α_k w_k (1). Then
x_k⊥w_k, x_{k+1}⊥w_{k+1}, ‖x_{k+1}‖²=‖x_k‖²+α_k². So each word below IS a reversed projection trajectory.
**Excursion A:** x_0^A=(37/10,61/10,33/5,−11/5)∈d^⊥, W_A=(d,b,e,d,a,c,e,c,b,d,e); itinerary (2):
(+,+,+,−,−)→(+,+,+,−,+)→(+,−,+,−,+)→(+,−,+,−,−)→(−,−,+,−,−)→(−,−,+,−,+)→(−,−,+,−,−)→(+,−,+,−,−)→(+,+,+,−,−).
**Excursion B:** x_0^B=(49/30,59/10,101/15,−22/15)∈d^⊥, W_B=(d,b,e,c,a,c,a,e,b,c,b,c,b,d); itinerary (3):
(+,+,+,−,−)→(+,+,+,−,+)→(−,+,+,−,+)→(−,−,+,−,+)→(−,+,+,−,+)→(−,+,+,−,−)→(−,−,+,−,−)→(+,−,+,−,−)→(+,+,+,−,−).
Both: start & finish same chamber; same J-face state; same first transition e:−→+; same final transition
b:−→+; same incoming wall flag d→b→e; all active-face spans ⊆ the single rank-3 superflat K. So the nested
flag, entry side, return order (the ω data) are IDENTICAL; only the internal excursion differs.

### 3. Exact active faces
Unsigned active-normal sets per destination chamber (steps 1..8):
A: {a,e},{a,b,e},{e},{a,e},{e},{a,e},{a},{a,b}. B: {a,e},{a},{a,b},{a,b},{a,b,e},{a,b},{a,b},{a,b}.
Every H_j⊆K, none =E (not a disguised full-rank reset). Face projector for independent signed-active M:
Π_M(p)=(I−Mᵀ(MMᵀ)^{-1}M)p+Mᵀ(MMᵀ)^{-1}1 (5). Substituting gives nonnegative KKT multipliers and strictly
positive slack on every nonactive constraint (smallest nonzero slack >0.19) — not a numerical accident.

### 4. The two closed affine maps
A_A(p)=Qp+b_A, A_B(p)=Qp+b_B with the SAME linear part
  Q = diag-block [[16/25,−12/25],[−12/25,9/25]] on coords (c,d), 0 on (a,b).   (6)
m=(0,0,3,4), n=(0,0,4,−3): Q = orthogonal projector onto ℝn=K^⊥; I−Q projects onto J+ℝm. Translations:
  b_A=(1,1,0,0)+((11+12√30)/325)·m,   b_B=(1,1,0,0)+((3+√30)/25)·m.   (7)
Different because (3+√30)/25 − (11+12√30)/325 = (28+√30)/325 > 0.   (8)  Both return to the J-face (first two
coords =1, other three signed constraints of s_0 strictly >1).

### 5. No common memory vector exists
If c_{J,ω} existed, same (J,ω) ⟹ b_A=(I−Q)c_{J,ω}=b_B, contradicting (8). So **there is no single c_{J,ω}
fixed by all closed excursions from this state.** Geometrically each map is the orthogonal projection onto an
affine line: Fix(A_A)=(1,1,0,0)+((11+12√30)/325)m+ℝn, Fix(A_B)=(1,1,0,0)+((3+√30)/25)m+ℝn (9) — parallel,
disjoint. Affine holonomy BOUNDED but nonzero. Distinguishing A,B would require recording the internal word /
metric history — exactly what the state-independent return vector was meant to avoid.

### 6. Why this does NOT produce drift
Cylinder C=(1,1,0,0)+[ (11+12√30)/325, (3+√30)/25 ]·m + ℝn   (10). Then A_A(C)⊆C and A_B(C)⊆C (A_A maps the
whole cylinder to its first boundary line, A_B to the other). Arbitrary alternation is bounded transversely —
a hysteresis strip where the proof requested a fixed point.

### 7. Exact replacement sublemma
> **Polynomial invariant-cylinder theorem.** For each refined cluster state σ with hidden survivor flat V_σ,
> there is a compact convex cross-section C_σ⊂V_σ^⊥ with sup_{c∈C_σ}‖c‖≤poly(r,1/δ) such that the cylinder
> C_σ=C_σ+V_σ obeys A_B(C_σ)⊆C_τ (11) for every admissible primitive block B:σ→τ.
Since each A_B is nonexpansive, dist(A_B p, C_τ) ≤ dist(p, C_σ) (12). At a top-rank state V_σ={0}, a poly
cross-section radius gives the dual bound. Rank-4 handoff:
> **Rank-4 invariant-strip sublemma.** For every J⊂K of ranks 2,3, the scalar affine return maps induced on
> K∩J^⊥ by all composable K-confined excursions from one refined J-state admit a common invariant interval of
> radius poly(1/δ).
Those intervals produce strips in the 2-dim survivor plane J^⊥; different K^⊥-directions have sine separation
≥δ/4; the full-span block contraction then bounds switching among strips polynomially. No common fixed point
required. The unresolved issue: **polynomial bounded holonomy of the return semigroup** (construct invariant
intervals/cross-sections) — not zero holonomy, not a point-valued coboundary.

**Verdict: PARTIAL + WHERE. The rank-4 common-vector holonomy theorem is refuted by two exact constant-δ
admissible excursions; bounded dual drift remains open and now requires a polynomial invariant-cylinder /
set-valued return theorem. Confidence: 98%.**
