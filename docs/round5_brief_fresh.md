# Round-5 Brief (ESCALATION — FRESH-CONTEXT attacker) — to a NEW GPT-5.5-Pro session

> **Orchestrator metadata (do NOT send).** Escalation per the attack ladder: four rounds with one solver
> have reduced the problem to a single crisp lemma but not closed it, and each *local* attack provably died.
> This brief is for a **FRESH GPT-5.5-Pro conversation** (no prior thread) — a clean, mostly self-contained
> statement of the open lemma, framed to invite machinery the thread hasn't used (oriented-matroid galleries,
> projection-orbit / Coxeter-arrangement theory). It states what is already proven (so the attacker doesn't
> redo it) and which local routes are dead (so it doesn't repeat them), then asks for the one missing
> theorem. Archive reply → `docs/round5_response.md`; independent audits (3 if closure claimed).

---

## ✂️ COPY-PASTE EVERYTHING BELOW THIS LINE TO A NEW GPT-5.5-PRO CHAT ✂️

I have reduced an open problem in discrepancy theory to a single, clean lemma about a **metric-projection
orbit through a hyperplane arrangement**. Everything below the "PROVEN" line is rigorously established
(independently verified). I need the one missing theorem (or a refutation). **Solve it your way** — please
bring whatever machinery fits (oriented matroids, projection-orbit / Friedrichs-angle theory, arrangement
combinatorics). End with a definite verdict and confidence (%).

### Objects
- `ℝ^d`, Euclidean norm. A finite set of unit vectors `T={t_1,…,t_m}⊂S^{d-1}`, `r=dim span(T)`. Work in
  `E=span(T)`.
- **Separation parameter** `δ := min{ dist(t, span(U)) : U⊆T, t∈T, t∉span(U) } ≥ 1/poly(d)` (e.g. constant
  `1/4`). Equivalently: every independent subset `B⊆T` has `σ_min(B) ≥ δ/√|B|`. **(A1)**
- For a sign vector `s∈{±1}^m`, set `v_i=s_i t_i`; **chamber** `C_s={x∈E:⟨v_i,x⟩≥0 ∀i}`; **certificate
  polyhedron** `P_s={p∈E:⟨v_i,p⟩≥1 ∀i}`. A chamber is *realizable* if it has nonempty interior.
- A **reversed projection trajectory**: a polygonal path `x_0,x_1,…` with `x_j=x_{j-1}+α_j t_j` and
  `⟨x_{j-1},t_j⟩=0` (each step moves orthogonally off the current point along some `t_j`; `ρ=‖x_j‖` is
  nondecreasing). Splitting at arrangement walls, each open segment lies in one chamber `C_{s_j}`; this
  yields an **admissible chamber itinerary** `s_1,s_2,…`.

### The dual process
Start with any `p_1∈P_{s_1}` of norm `≤ r/δ`, and update by **metric projection**
> `p_{j+1} = Proj_{P_{s_{j+1}}}(p_j)`.

### PROVEN (verified — use freely, do NOT re-derive)
- **(B1)** Each `P_s` is nonempty and `min_{p∈P_s}‖p‖ ≤ r/δ`; in fact `P_s ⊆ C_s + (r/δ)B_2` (within `E`).
- **(B2)** `|T|` (distinct directions) `≤ 2π r⁴/δ` (only polynomially many walls).
- **(B3) Angle separation of ORIGINAL flats:** any two subspaces spanned by subsets of `T` have smallest
  positive principal angle with `sinθ ≥ δ/r`. *(Warning: this does NOT extend to images of these flats under
  products of projections — see "dead routes".)*
- **(B4) Exact dynamics.** `p_{j+1}=P_{H_j^⊥}p_j+q_j`, `H_j`=span of the active-face normals (signed members
  of `T`) at `p_{j+1}`, `q_j∈H_j` with `‖q_j‖≤r/δ`; energy `‖p_{j+1}‖²−‖p_j‖²=‖q_j‖²−‖P_{H_j}p_j‖²`.
  Unrolling: `p_N=Q_N p_0+Σ_j R_j q_j`, `R_j=P_{H_N^⊥}⋯P_{H_{j+1}^⊥}`; telescoping+Bessel give
  `‖Σ_j R_j q_j‖ ≤ (r/δ)√N`.
- **(B5) KKT localization.** For one adjacent transition (flipped normal `b_0`, common active normals
  `b_1..b_k`), the energy jump `Δ=‖p_{j+1}‖²−‖p_j‖² ≤ 4Σ_{i≥1}λ_i` (KKT multipliers); and **if no common
  constraint is active, `Δ≤0`**. With `u=x_j/‖x_j‖` (`⟨b_0,u⟩=0`, `⟨b_i,u⟩≥0`): the unpaid part of `Δ` forces
  `dist(u,J^⊥)≤rη/δ` for a `dim≥2` flat `J` — i.e. **all uncharged dual-energy growth happens only near a
  codimension-≥2 stratum of the arrangement (a multiwall cluster).**

### THE OPEN LEMMA (prove this — it closes the whole problem)
> **Bounded dual-drift.** There is `D=poly(r,1/δ)` such that for EVERY admissible chamber itinerary (one
> arising from a reversed projection trajectory as above), `sup_j ‖p_j‖ ≤ D`.

Equivalent clean reformulation by inversion `I(p)=p/‖p‖²` (use whichever you prefer): the chambers map to
**tangent lobes** `L_s=⋂_i B(v_i/2, ½)` (`I(P_s)=L_s∖{0}`; distinct lobes are mutually tangent only at `0`;
inversion is a Möbius map with `‖I(z)−I(w)‖=‖z−w‖/(‖z‖‖w‖)`), and the update becomes the relative-nearest
point `z_{j+1}=argmin_{w∈L_{s_{j+1}}∖0}‖w−z_j‖/‖w‖`, with `‖z_j‖=1/‖p_j‖`. The lemma is then:
> **No-cusp.** `inf_j ‖z_j‖ ≥ 1/poly(r,1/δ)` — the orbit never cusps into the common tangency point `0`.

If proven, `G(T)≤2D` and the original discrepancy bound `G(T)=poly` follows.

### What is REALLY missing (and what is dead)
- **Dead route 1 — pure energy/Bessel:** gives only `(r/δ)√N` (B4), not `N`-independent. The `√N` is the
  ceiling of any estimate that bounds `(Σ‖q_j‖²)^{1/2}` termwise.
- **Dead route 2 — angle-charging via (B3):** the drift is governed by the *dynamically projected* images
  `R_jH_j=P_{H_N^⊥}⋯P_{H_{j+1}^⊥}H_j`, which are NOT `T`-spanned; their mutual angles can collapse to ~0
  after a single projector, so (B3)/(B2) do not apply to them. Do not try to transfer (B3) to `R_jH_j`.
- **Dead route 3 — local per-switch payment:** a single adjacent switch on a GENUINE constant-δ itinerary can
  raise `‖p‖²` by a fixed amount (e.g. 48/7) while the local radial increment `⟨p_{j+1}−p_j, x_j⟩/‖x_j‖→0`.
  So no bound "energy jump ≤ poly·(local radial/transition budget)" can hold. The cancellation must be
  **cluster-level and history-dependent**, not per-switch.
- **The exact missing ingredient:** a **polynomial multiwall-cluster RETURN-POINT / no-cusp theorem.** A
  cluster of near-simultaneous wall crossings near a codim-≥2 stratum may create a large intermediate dual
  excursion, but the ADMISSIBILITY of the itinerary (consecutive active faces share the trajectory point
  `x_j`; `ρ` is monotone; the gallery is an ordered oriented-matroid walk) should force those excursions to
  CANCEL after the cluster and any later revisits — without re-paying a rank or angle factor each time.

Likely-relevant machinery (suggestions, not constraints): oriented-matroid galleries / tope graphs of the
arrangement; the combinatorics of reversed-projection walks; projection-orbit regularity (Güntürk–Thao-type
absolute convergence, Meshulam/Bauschke–Tung boundedness) made *quantitative and polynomial* using (A1)+(B2);
a return-time / hysteresis potential keyed to the monotone radial coordinate.

**Strong numerical evidence the lemma is TRUE:** simulating the dual process on adversarial itineraries —
INCLUDING targeted codim-≥2 cluster stress — `sup_j‖p_j‖` stays bounded and FLAT in `N` (saturates at ~`r/δ`,
no `√N` growth) for `r` up to 6 and trajectories of length up to ~350. So a refutation is unlikely but not
excluded.

### What we need back
1. A proof of **bounded dual-drift / no-cusp** with explicit `D=poly(r,1/δ)` and its degree — OR a precise
   break-point — OR a refutation: an explicit **admissible** itinerary (realizable by a reversed projection
   trajectory at constant `δ`) on which `sup_j‖p_j‖` is super-polynomial. (Super-poly for ARBITRARY chamber
   words is NOT enough — admissibility/realizability is essential.)
2. If partial: the exact remaining sub-lemma, cleanly stated.
3. Your **confidence (%)** and a one-line **verdict** (closed / partial+where / refuted).
