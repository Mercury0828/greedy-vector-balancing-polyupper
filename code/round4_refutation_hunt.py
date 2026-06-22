"""
Round-4 REFUTATION HUNT (the decisive de-risk; guide §Evaluation, adversarial input only).

The Round-4 audit flagged: §6 confines all UNPAID dual drift to codim-≥2 wall CLUSTERS but does NOT bound
the NUMBER of clustered switches. The danger (would refute DA, hence (★)): a chain of §3-type switches near
a codim-≥2 stratum, each adding Θ(1) dual energy with vanishing radial cost, accumulating to make
sup_j ‖p_j‖ super-polynomial. The flat-in-N sims so far used GENERIC (mostly transverse) crossings; here we
specifically STRESS the codim-≥2 cluster.

Construction of a codim-≥2 cluster: walls t^⊥ all containing a common (r-2)-flat ⟺ the t_i lie in a common
2-plane (L^⊥). So: put n_plane unit vectors in the e1–e2 plane (well separated, to keep δ_T≥~1/4 — only
O(1/δ) fit) PLUS e3,…,er to span. Trajectories that oscillate IN the plane cross these clustered walls
repeatedly — exactly the §6 danger zone.

PRE-REGISTERED:
  * DA TRUE ⟹ sup_j‖p_j‖ stays ≤ poly(r,1/δ), BOUNDED/flat in trajectory length N even under clustered stress.
  * REFUTATION ⟹ sup_j‖p_j‖ grows with N (e.g. ~√N or faster) on an admissible clustered itinerary
    ⟹ DA false ⟹ (★) likely false ⟹ pivot-to-A human gate (death-EVIDENCE, not a formal proof).
"""
import json
import os
import numpy as np
from scipy.optimize import minimize

import sim1_killtest as S1

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


def proj_onto_Ps(p0, V):
    cons = {"type": "ineq", "fun": lambda p: V.T @ p - 1.0, "jac": lambda p: V.T}
    res = minimize(lambda p: float((p - p0) @ (p - p0)), p0, method="SLSQP",
                   jac=lambda p: 2 * (p - p0), constraints=[cons],
                   options={"maxiter": 500, "ftol": 1e-12})
    return res.x


def min_norm_cert(V):
    cons = {"type": "ineq", "fun": lambda p: V.T @ p - 1.0, "jac": lambda p: V.T}
    mv = V.mean(axis=1); den = (V.T @ mv).min()
    p0 = mv / den if den > 1e-9 else V[:, 0].copy()
    res = minimize(lambda p: p @ p, p0, jac=lambda p: 2 * p, constraints=[cons],
                   method="SLSQP", options={"maxiter": 500, "ftol": 1e-12})
    return res.x


def build_cluster_T(r, n_plane, ang_gap_deg):
    """n_plane unit vectors in the e1-e2 plane spaced ang_gap_deg apart (codim-2 cluster) + e3..er."""
    cols = []
    for k in range(n_plane):
        a = np.deg2rad(k * ang_gap_deg)
        v = np.zeros(r); v[0] = np.cos(a); v[1] = np.sin(a)
        cols.append(v)
    for j in range(2, r):
        e = np.zeros(r); e[j] = 1.0
        cols.append(e)
    return np.column_stack(cols)


def cluster_traj(T, max_steps, plane_bias=0.85):
    """Reversed-projection-style forward trajectory biased to use the IN-PLANE (clustered) walls, so the
    chamber itinerary repeatedly crosses the codim-2 cluster. Returns the list of points."""
    d, n = T.shape
    # plane walls = columns with support in {0,1}
    in_plane = [i for i in range(n) if abs(T[2:, i]).max() < 1e-9] if d > 2 else list(range(n))
    y = S1.normalize_cols(rng.standard_normal((d, 1)))[:, 0]
    pts = [y.copy()]
    for _ in range(max_steps):
        if np.linalg.norm(y) < 1e-4:
            break
        ips = T.T @ y
        a = np.abs(ips)
        if a.max() < 1e-9:
            break
        # bias toward in-plane walls to stress the cluster
        if in_plane and rng.random() < plane_bias:
            cand = in_plane
        else:
            cand = list(range(n))
        # among chosen, pick a moderate-projection wall (prolong; keep crossing the cluster)
        sub = sorted(cand, key=lambda i: a[i])
        i = sub[len(sub) // 2]
        if a[i] < 1e-9:
            i = int(np.argmax(a))
        y = y - ips[i] * T[:, i]
        pts.append(y.copy())
    return pts


def dual_sup(T, pts):
    A = T
    seq = []
    for y in pts:
        s = np.sign(A.T @ y); s[s == 0] = 1
        seq.append(s)
    seq = seq[::-1]
    p = min_norm_cert(A * seq[0])
    sup = float(np.linalg.norm(p))
    norms = [sup]
    for s in seq[1:]:
        V = A * s
        if (V.T @ p).min() < 1 - 1e-6:
            p = proj_onto_Ps(p, V)
        nn = float(np.linalg.norm(p))
        sup = max(sup, nn)
        norms.append(nn)
    return sup, norms


def run():
    print("=== Round-4 REFUTATION HUNT (codim-≥2 cluster stress) ===\n")
    results = []
    # r=3: plane cluster + e3. Try several cluster sizes / angular gaps (keep delta_T up).
    configs = [
        (3, 6, 30.0), (3, 7, 26.0), (3, 9, 20.0),   # more walls => smaller delta_T
        (4, 6, 30.0), (4, 8, 24.0),
    ]
    for (r, n_plane, gap) in configs:
        T = build_cluster_T(r, n_plane, gap)
        try:
            dT = S1.delta_T(T)
        except Exception:
            dT = float("nan")
        per_len = []
        for N in [25, 50, 100, 200, 350]:
            best = 0.0
            for _ in range(5):
                pts = cluster_traj(T, N)
                sup, _ = dual_sup(T, pts)
                best = max(best, sup)
            per_len.append((N, round(best, 3)))
        # growth fit on sup vs N
        Ns = np.array([x[0] for x in per_len], float)
        ys = np.array([x[1] for x in per_len], float)
        sqrtN_slope = float(np.polyfit(np.sqrt(Ns), ys, 1)[0])  # ys ~ slope*sqrt(N)?
        loglog = float(np.polyfit(np.log(Ns), np.log(np.maximum(ys, 1e-9)), 1)[0])
        results.append({"r": r, "n_plane": n_plane, "ang_gap_deg": gap,
                        "delta_T": round(float(dT), 4), "r_over_delta": round(r / dT, 2),
                        "sup_by_N": per_len, "fit_vs_sqrtN_slope": round(sqrtN_slope, 4),
                        "fit_loglogN_slope": round(loglog, 4)})
        print(f"r={r} n_plane={n_plane} gap={gap}° δ_T={dT:.3f} r/δ={r/dT:.1f}: {per_len}")
        print(f"    fit: sup~{sqrtN_slope:.3f}·√N  | log-log(N) slope {loglog:.3f}")

    # verdict heuristic
    max_loglog = max(r["fit_loglogN_slope"] for r in results)
    verdict = ("BOUNDED-in-N (DA-consistent; no refutation found)"
               if max_loglog < 0.25 else
               "GROWS with N — possible refutation, INVESTIGATE")
    print(f"\nVERDICT: {verdict}  (max log-log(N) slope = {max_loglog:.3f}; "
          f"~0 ⟹ flat/bounded, ~0.5 ⟹ √N growth)")
    with open(os.path.join(_HERE, "round4_refutation_results.json"), "w") as f:
        json.dump({"results": results, "verdict": verdict, "max_loglogN_slope": max_loglog}, f, indent=2)
    print("Frozen -> code/round4_refutation_results.json")


if __name__ == "__main__":
    run()
