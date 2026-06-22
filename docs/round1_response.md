# Round-1 RESPONSE — GPT-5.5-Pro (verbatim) + orchestrator header

> **Orchestrator header.** Solver = web GPT-5.5-Pro, owner-relayed, received 2026-06-22. Verdict:
> **PARTIAL — `(★)` neither closed nor refuted; confidence 95% (in the analysis).** This is a
> normal (non-closure) reply with substantial forward progress → ≥1 independent adversarial audit
> (`docs/round1_audit.md`). Headline findings (orchestrator triage, to be audited):
> - **FATAL-to-brief:** the "full unit vectors WLOG" reduction I shipped in `round1_brief.md` is **FALSE**
>   (explicit δ=1/4 counterexample; scaled "steering" moves matter). Also invalidates Sim 1's unit-only adversary.
> - **PROGRESS (new substrate, pending audit):** (i) the HS1 support-function ITERATION identity is **DERIVED**
>   for the recursive projective closure ⇒ HS1 reduction now rigorous; (ii) **principal-angle lemma**
>   `sinθ(H,K) ≥ δ_T/r` for T-spanned flats (candidate P6); (iii) refined P2 `‖P_{H(x)}x‖ ≤ q/(2δ_T)`;
>   (iv) **P3 possibly REVIVED**: claims `κ_A ≤ 1/δ_A ≤ 1/δ_T` for unit columns ⇒ `|T| ≤ 2πr⁴/δ_T`.
> - **GAPs (precise break-points):** HS2 needs a *history-dependent summability invariant* (static switch
>   lemma disproved by a `B↦B/δ` example); HS1 needs a *polynomial total-variation theorem* (cited BV
>   result arXiv:1901.07516 gives only a geometry-dependent/exponential constant).
> - **Lit note:** GPT cites **arXiv:1901.07516** for projection-product BV (NOT our 1603.00854).

---

## VERBATIM REPLY

## Verdict

I do **not** obtain a proof or refutation of (★). I do obtain a precise failure point for HS2, plus a correction to one claimed reduction that materially changes the problem.

### 1. The "full unit vectors WLOG" reduction is false

One-step convexity does not imply dynamic endpoint reduction. It maximizes the *next norm* while changing the state from which all future choices are made. Convexity has, rather predictably, impersonated dynamic programming without the required qualifications.

Here is an explicit counterexample at the requested constant δ=1/4. Put
  c = √15/4,  u = e_2,  v = (1/4)e_1 − c e_2,  T = {u,v} ⊂ S^1.
Then δ_T = dist(u, span v) = dist(v, span u) = 1/4.

#### Full-unit arrivals have norm at most 1
Starting at zero, every full-unit greedy state belongs to R = {0, ±u, ±v, ±(u+v)}.
Indeed:
* From u, an arrival u must be subtracted, returning to 0.
* Since ⟨u,v⟩ = −c < 0, an arrival v is added, reaching u+v.
* At u+v, ⟨u,u+v⟩ = ⟨v,u+v⟩ = 1−c > 0, so the arriving vector must be subtracted, reaching either u or v.
* The negative states behave symmetrically.
Moreover, |u+v|² = 2−2c < 1. Thus the full-unit model has maximum norm exactly 1.

#### Scaled arrivals reach norm 4
For m = 0,…,16, define x_m = (m/4) e_1. From x_m, for 0≤m≤15, first send the scaled vector cu. It is orthogonal to x_m, so the positive sign is greedy. This gives y_m = x_m + cu. Next send the full vector v. We have ⟨y_m, v⟩ = m/16 − 15/16 ≤ 0. Hence adding v is greedy, and y_m + v = ((m+1)/4) e_1 = x_{m+1}. After sixteen pairs, x_16 = 4 e_1.
Therefore G_{[-1,1]T}(T) ≥ 4,  G_unit-only(T) = 1.

This is the two-vector mechanism underlying the paper's lower-bound construction. The source extends its upper bound to scaled vectors using convexity of an already constructed absorbing body, not by replacing scaled adversarial moves with unit moves. [arXiv 2606.17991]

Consequently, P2 still applies to an individual norm-increasing scaled move, because
  a² − 2a|⟨t,x⟩| > 0  ⟹  |⟨t,x⟩| < a/2 ≤ 1/2,
but a maximizing trajectory may contain essential norm-decreasing or norm-neutral steering moves outside N(x). HS2 must account for those moves.

### 2. Two useful consequences of P1 and P2
Let N(x) = {t∈T : |⟨t,x⟩|<1/2}, H(x) = span N(x), q = dim H(x).

#### Refined P2
  ‖P_{H(x)} x‖ ≤ q/(2δ_T).
Choose a basis B ⊆ N(x) of H(x). Since B^⊤ P_{H(x)} x = B^⊤ x, we have ‖B^⊤ P_{H(x)} x‖₂ ≤ √q/2. The inverse of B^⊤: H(x)→ℝ^q has operator norm 1/σ_min(B), so P1 gives ‖P_{H(x)} x‖ ≤ (√q/δ_T)(√q/2) = q/(2δ_T).
Thus above r/(2δ_T), the active flat is proper, exactly as desired.

#### Polynomial separation of all T-spanned flats
Let H,K be spans of subsets of T, and let θ(H,K) denote their smallest positive principal angle. Then
  sin θ(H,K) ≥ δ_T / r.
To see this, choose T-bases A,B for H,K, and put M = [A, −B]. Choose independent columns C of M spanning H+K. By P1, σ_min(C) ≥ δ_T/√r. Since MM^⊤ ⪰ CC^⊤ on H+K, the reduced minimum singular value satisfies γ(M) ≥ δ_T/√r.
Write thin QR: A = Q_H R_H, B = Q_K R_K, and let N = [Q_H, −Q_K], D = diag(R_H, R_K). Then M = ND, while ‖D‖ ≤ √r. Hence γ(N) ≥ γ(M)/√r ≥ δ_T/r. The relevant singular value of N is √(1−cosθ) = √2 sin(θ/2). It follows that sin θ ≥ δ_T/r.
So active flats cannot meet at exponentially tiny angles when δ_T is polynomially bounded. This is genuine progress for HS2, but it does not by itself control how often the trajectory can change flats.

### 3. Exact HS2 break-point
The unsupported step is the proposed conversion
  "proper active flat + separated switch" ⟹ "additive or summably charged norm growth."
P1 and P2 alone do not imply such an additive transition estimate.

Let J = span(e_1), t = √(1−δ²) e_1 + δ e_2, and, for arbitrary B>0, let x = B e_1 − (√(1−δ²)/δ) B e_2. Then ‖P_J x‖ = B, ⟨t,x⟩ = 0, so t is maximally active. Nevertheless, J + span(t) = ℝ² and ‖P_{J+span(t)} x‖ = ‖x‖ = B/δ. Also δ_{{e_1,t}} = δ.
Thus, knowing only ‖P_J x‖ ≤ B, |⟨t,x⟩| < 1/2 allows a factor 1/δ increase when the tracked flat is enlarged. An estimate of the form ‖P_{J+⟨t⟩} x‖ ≤ ‖P_J x‖ + poly(r,1/δ) is statically false.

This example is not itself a dynamically reachable repeated amplifier, so it does not refute (★). It pinpoints what HS2 lacks: a **history-dependent reachability invariant** controlling the hidden component of x, not merely the current active flat and its projection.

The principal-angle lemma bounds the loss at one transition by a polynomial factor, roughly r/δ. Multiplying that factor along a rank recursion reproduces an exponential bound. To obtain a polynomial result, one needs a theorem showing that these factors are summable, square-summable, or globally coupled by P1. P1 and P2 currently provide no such coupling.
In particular, simply counting active-flat switches cannot work. Scaled steering permits switches with arbitrarily small local changes, and even unit trajectories can cycle between active-set configurations. Any successful charging argument must charge a quantitative geometric quantity, not the occurrence of a switch.

### 4. HS1 can be made exact, but its quantitative theorem is still missing
Define K_0 = {0}, K_{n+1} = conv ∪_{t∈T} (π_t K_n + [−t,t]). Then support functions satisfy
  h_{K_{n+1}}(y) = max_{t∈T} h_{π_t K_n + [−t,t]}(y) = max_{t∈T} ( h_{K_n}(π_t y) + |⟨y,t⟩| ).
Thus the proposed iteration identity is valid for this recursively defined projective closure.
Unrolling it, set y_0 = y, y_j = π_{t_j} y_{j−1}. Since y_{j−1} − y_j = ⟨y_{j−1}, t_j⟩ t_j, we obtain
  h_{K_n}(y) = max_{t_1,…,t_n∈T} Σ_{j=1}^n |y_j − y_{j−1}|.
Consequently, a uniform estimate Σ_{j≥1} |y_j − y_{j−1}| ≤ P(r,1/δ_T) |y_0| would produce a bounded T-projective body of radius P(r,1/δ_T), and hence prove (★).

For a finite family of finite-dimensional subspaces, unrestricted projection trajectories are indeed known to have bounded total variation. However, the result supplies a geometry-dependent constant rather than a polynomial one. [arXiv 1901.07516]
Moreover, the displayed quantitative proof in that work uses ε_* = ½ κ_*^{−N} and then a recurrence whose denominator contains 1 − √(1−ε_*²). Even after the principal-angle lemma gives κ_* = O(r/δ_T), the resulting bound is exponential, or worse, in the number N of projections. [arXiv 1901.07516]

So HS1 has a clean and rigorous reduction, but it stops precisely at:
> **Missing projection theorem.** Prove polynomial total variation for products of the hyperplane projections {π_t : t∈T}, assuming every nonzero principal angle between T-spanned flats has sine at least δ_T/r.
No existing argument cited above gives that polynomial dependence.

### 5. A useful additional structural reduction
There cannot be exponentially many distinct directions hidden inside T.
Take one representative from every antipodal line of T, and put these representatives into a matrix A. Then δ_A ≥ δ_T. For unit columns, the circuit imbalance satisfies κ_A ≤ 1/δ_A ≤ 1/δ_T. A recent column-number theorem states that a rank-r real matrix with pairwise non-collinear columns has, for r≥4, m ≤ π r⁴ κ_A. Therefore the number m of unoriented directions in T satisfies
  m ≤ π r⁴ / δ_T,  and hence |T| ≤ 2π r⁴ / δ_T. [arXiv 2510.20301]
This is a worthwhile reduction: constant-δ instances contain only polynomially many projective directions. Unfortunately, current unrestricted-projection bounds are exponential in that polynomial number, so counting alone does not close the gap.

### What is actually missing
A closure now appears to require one of the following genuinely new statements:
1. A history-dependent HS2 potential that bounds the cumulative hidden-component transfer across active-flat changes. It must exploit global basis conditioning, because any static additive switch lemma is disproved by the B↦B/δ example.
2. A polynomial bounded-variation theorem for arbitrary products of these specially conditioned hyperplane projections:
   sup_{(t_j)} Σ_j |π_{t_j} y_{j−1} − y_{j−1}| ≤ poly(r,1/δ_T) |y_0|.
The second statement, combined with the derived support-function identity, would close (★) immediately. I found no argument deriving either statement from P1 and P2 alone.

**Verdict: PARTIAL, not closed or refuted. The endpoint reduction is false; HS2 fails at the first active-flat transition without a new history-dependent summability invariant, while HS1 stops at the missing polynomial total-variation theorem. Confidence: 95%.**

Refs cited by GPT: [1] arXiv:2606.17991 (anchor); [2] arXiv:1901.07516 (projection-product BV); [3] arXiv:2510.20301 (column number).
