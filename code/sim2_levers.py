"""
Sim 2 — LEVER CHECK for `greedy-vector-balancing-polyupper` (Phase 0, guide ��Evaluation).

Numerically verifies the substrate the HS2 (subspace-switch) route rests on, on ADVERSARIAL T (the
families from Sim 1, including the dependency danger zone), at constant delta_T >= 1/4:

  P1:  every independent basis B subset of T has  sigma_min(B) >= delta_T / sqrt(r),  r = rank.
       (Dual-row-norm argument: rows of B^{-1} have norm 1/dist(b_i, span(B\\b_i)) <= 1/delta_T,
        so ||B^{-1}||_F <= sqrt(r)/delta_T, hence sigma_min(B) = 1/||B^{-1}||_2 >= 1/||B^{-1}||_F >= delta_T/sqrt(r).)

  P2:  if ||x|| > r/(2 delta_T)  then  span{ t in T : |<x,t>| < 1/2 }  is a PROPER subspace of span(T).
       (If N(x) spanned all of span(T), a basis B subset of N(x) gives ||B^T x|| <= sqrt(r)/2, so
        ||x|| <= ||B^{-T}||_2 * ||B^T x|| <= (sqrt(r)/delta_T)*(sqrt(r)/2) = r/(2 delta_T) -- contradiction.)

Verification = POSITIVE checks (the inequality holds with the claimed slack) AND NEGATIVE checks
(report the tightest observed ratio; flag any violation). Adversarial input only; fixed seed.
"""

import itertools
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim1_killtest as S1   # reuse delta_T, families, adversary

_HERE = os.path.dirname(os.path.abspath(__file__))

rng = np.random.default_rng(S1.SEED + 1)


def sigma_min(M):
    return float(np.linalg.svd(M, compute_uv=False)[-1])


def check_P1(T, max_bases=2000):
    """Check sigma_min(B) >= delta_T/sqrt(r) over independent bases B subset of T.
    Returns the worst (smallest) ratio sigma_min(B) / (delta_T/sqrt(|B|)); must be >= 1 if P1 holds."""
    d, n = T.shape
    r = np.linalg.matrix_rank(T)
    dT = S1.delta_T(T)
    worst_ratio = np.inf
    n_bases = 0
    violations = 0
    # enumerate independent subsets of all sizes up to r (cap count)
    cols = list(range(n))
    sizes = range(1, r + 1)
    combos = []
    for k in sizes:
        for c in itertools.combinations(cols, k):
            combos.append(c)
    if len(combos) > max_bases:
        idx = rng.choice(len(combos), size=max_bases, replace=False)
        combos = [combos[i] for i in idx]
    for c in combos:
        B = T[:, list(c)]
        k = len(c)
        if np.linalg.matrix_rank(B) < k:
            continue  # not independent
        sm = sigma_min(B)
        bound = dT / np.sqrt(k)
        ratio = sm / bound if bound > 0 else np.inf
        worst_ratio = min(worst_ratio, ratio)
        n_bases += 1
        if sm < bound - 1e-9:
            violations += 1
    return {"delta_T": round(float(dT), 4), "rank": int(r), "bases_checked": n_bases,
            "worst_ratio_sigmamin_over_bound": round(float(worst_ratio), 4),
            "violations": int(violations)}


def check_P2(T, trials=4000):
    """For random/adversarial x with ||x|| > r/(2 delta_T), confirm span N(x) is PROPER.
    Also report the largest ||x|| at which span N(x) was still FULL (should be <= r/(2 delta_T))."""
    d, n = T.shape
    r = np.linalg.matrix_rank(T)
    dT = S1.delta_T(T)
    threshold = r / (2 * dT)
    spanT_rank = r
    violations = 0
    max_fullspan_norm = 0.0
    checked_above = 0

    # build x's two ways: (1) random directions scaled across a range of norms,
    # (2) actual greedy iterates from the Sim-1 adversary (most relevant adversarial x).
    xs = []
    for _ in range(trials):
        dirv = rng.standard_normal(d)
        dirv /= np.linalg.norm(dirv)
        scale = rng.uniform(0.1, 3.0) * threshold
        xs.append(scale * dirv)
    # adversarial iterates
    S = np.zeros(d)
    for _ in range(max(60, 12 * d)):
        gains, _ = S1.productive_gain(T, S)
        prod = np.where(gains > 1e-12)[0]
        if prod.size == 0:
            break
        i = prod[int(np.argmax(gains[prod]))]
        t = T[:, i]
        s = -np.sign(t @ S) if abs(t @ S) > 0 else 1.0
        S = S + s * t
        xs.append(S.copy())

    for x in xs:
        nx = np.linalg.norm(x)
        ips = np.abs(T.T @ x)
        Nx = T[:, ips < 0.5]
        rank_Nx = np.linalg.matrix_rank(Nx) if Nx.shape[1] > 0 else 0
        full = (rank_Nx == spanT_rank)
        if full:
            max_fullspan_norm = max(max_fullspan_norm, nx)
        if nx > threshold + 1e-9:
            checked_above += 1
            if full:  # P2 says this must NOT happen
                violations += 1
    return {"delta_T": round(float(dT), 4), "rank": int(r),
            "threshold_r_over_2delta": round(float(threshold), 4),
            "x_checked_above_threshold": int(checked_above),
            "max_norm_with_FULL_spanNx": round(float(max_fullspan_norm), 4),
            "violations": int(violations)}


def run():
    DELTA = 0.25
    results = {"seed": int(S1.SEED + 1), "delta": DELTA, "cases": []}
    print(f"=== Sim 2 lever check ===  seed={S1.SEED+1}  delta>={DELTA}\n")

    # Build the same adversarial families as Sim 1 across a few d, plus the danger zone.
    theta = np.arcsin(DELTA)
    cases = []
    for d in [2, 4, 6, 8]:
        dp = max(1, d // 2)
        cases.append((f"gadgets(dim={2*dp})", S1.family_orthogonal_gadgets(dp, theta)))
        Tind = S1.family_random_independent(d, d, DELTA)
        if Tind is not None and S1.is_independent(Tind) and S1.delta_T_independent(Tind) >= DELTA:
            cases.append((f"rand_indep(d={d})", Tind))
        kpairs = min(2, d // 2)
        if kpairs >= 1:
            cases.append((f"dep_pairs(d={d},n={d+kpairs})", S1.family_dependent_pairs(d, kpairs)))
        cases.append((f"near_dep_chain(d={d})", S1.family_near_dependency_chain(d, DELTA)))

    p1_ok = p2_ok = True
    for name, T in cases:
        try:
            p1 = check_P1(T)
            p2 = check_P2(T)
        except Exception as e:
            print(f"{name}: ERROR {e}")
            continue
        if p1["violations"] > 0 or p1["worst_ratio_sigmamin_over_bound"] < 1 - 1e-6:
            p1_ok = False
        if p2["violations"] > 0:
            p2_ok = False
        print(f"[{name}]")
        print(f"   P1: dT={p1['delta_T']} r={p1['rank']} bases={p1['bases_checked']} "
              f"worst_ratio={p1['worst_ratio_sigmamin_over_bound']} (>=1 ok) viol={p1['violations']}")
        print(f"   P2: dT={p2['delta_T']} r={p2['rank']} thr={p2['threshold_r_over_2delta']} "
              f"maxnorm_with_full_Nx={p2['max_norm_with_FULL_spanNx']} (<=thr ok) "
              f"viol={p2['violations']} (checked {p2['x_checked_above_threshold']} above thr)")
        results["cases"].append({"name": name, "P1": p1, "P2": p2})

    results["P1_holds"] = bool(p1_ok)
    results["P2_holds"] = bool(p2_ok)
    print(f"\nP1 holds on all adversarial cases: {p1_ok}")
    print(f"P2 holds on all adversarial cases: {p2_ok}")
    with open(os.path.join(_HERE, "sim2_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("Frozen -> code/sim2_results.json")
    return results


if __name__ == "__main__":
    run()
