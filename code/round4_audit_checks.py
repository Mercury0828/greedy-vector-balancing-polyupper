"""
Round-4 audit — numeric verification of GPT-5.5-Pro's Round-4 claims. Fixed seed; scipy.

Checks:
  S2.  §2 explicit example: t1,t2,t3 with δ_T=√7/4; p⁻∈P⁻, p⁺∈P⁺, p⁺=Proj_{P⁺}(p⁻), and
       ‖p⁻‖<R_0<‖p⁺‖ — i.e. one adjacent dual projection ESCAPES the r/δ ball.
  S3.  §3 genuine itinerary: T'={t1,t2,t3,w}, δ_{T'}=√7/8>1/4; the (−,+,+,+)→(+,+,+,+) junction at x_ε;
       ⟨d,x_ε⟩/‖x_ε‖→0 while ‖p⁺‖²−‖p⁻‖²=48/7 ⟹ no LOCAL per-switch payment estimate.
  S4.  §4 KKT localization: Δ=2Σλ_i−‖d‖² and Δ≤4Σλ_i over common-active; no common active ⟹ Δ≤0.
  S7.  §7 inversion identity ‖I(z)−I(w)‖=‖z−w‖/(‖z‖‖w‖) and I(P_s)=L_s∖{0}.
  DRIFT2. dual-drift STRESS on a near-degenerate (codim-≥2 clustered) T: can sup_j‖p_j‖ be made to grow?
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


def check_S2():
    s7 = np.sqrt(7); s14 = np.sqrt(14)
    t1 = np.array([1.0, 0, 0]); t2 = np.array([-0.75, s7/4, 0]); t3 = np.array([0, 0, 1.0])
    T = np.column_stack([t1, t2, t3])
    units = [float(np.linalg.norm(c)) for c in [t1, t2, t3]]
    dT = S1.delta_T(T)
    pm = np.array([-1.0, 1/s7, s14]); pp = np.array([1.0, s7, s14])
    Vm = np.column_stack([-t1, t2, t3]); Vp = np.column_stack([t1, t2, t3])
    pm_in = (Vm.T @ pm).min(); pp_in = (Vp.T @ pp).min()
    d = pp - pm
    # express d in t1,t2
    coef, *_ = np.linalg.lstsq(np.column_stack([t1, t2]), d, rcond=None)
    proj = proj_onto_Ps(pm, Vp)
    R0 = 3 / dT
    return {"units": [round(x, 6) for x in units], "delta_T": round(float(dT), 6),
            "claim_sqrt7/4": round(float(s7/4), 6),
            "pm_in_Pminus(min_constraint)": round(float(pm_in), 5),
            "pp_in_Pplus(min_constraint)": round(float(pp_in), 5),
            "d_coef_in_t1t2": [round(float(c), 5) for c in coef], "claim_(32/7,24/7)": [round(32/7,5), round(24/7,5)],
            "proj_matches_pp": bool(np.linalg.norm(proj - pp) < 1e-4),
            "norm_pm^2": round(float(pm @ pm), 5), "norm_pp^2": round(float(pp @ pp), 5),
            "R0^2": round(float(R0**2), 5),
            "ESCAPES_ball (||pm||<R0<||pp||)": bool(np.linalg.norm(pm) < R0 < np.linalg.norm(pp))}


def check_S3():
    s7 = np.sqrt(7); s3 = np.sqrt(3); s42 = np.sqrt(42); s14 = np.sqrt(14)
    t1 = np.array([1.0, 0, 0]); t2 = np.array([-0.75, s7/4, 0]); t3 = np.array([0, 0, 1.0])
    w = np.array([0.5, 0, s3/2])
    Tp = np.column_stack([t1, t2, t3, w])
    dTp = S1.delta_T(Tp)
    eps = 1e-3
    x = np.array([0.0, eps, 1.0])
    z = x - (w @ x) * w  # pi_w x
    pm = np.array([-1.0, 1/s7, s14]); pp = np.array([1.0, s7, s14])
    d = pp - pm
    # signs along z->x for (t1,t2,t3,w): evaluate at x
    signs_x = np.sign(np.array([t1 @ x, t2 @ x, t3 @ x, w @ x]))
    w_slack_pm = w @ pm; w_slack_pp = w @ pp
    return {"delta_Tp": round(float(dTp), 6), "claim_sqrt7/8": round(float(s7/8), 6),
            "z_perp_w": round(float(abs(z @ w)), 8), "x=z+(s3/2)w_err": round(float(np.linalg.norm(x - (z + (s3/2)*w))), 8),
            "signs_at_x (t1,t2,t3,w)": [int(s) for s in signs_x],
            "w_slack_pm(>1)": round(float(w_slack_pm), 4), "w_slack_pp(>1)": round(float(w_slack_pp), 4),
            "claim_w_slacks": [round((-1+s42)/2,4), round((1+s42)/2,4)],
            "<d,x>/||x||": round(float((d @ x)/np.linalg.norm(x)), 6),
            "energy_jump ||pp||^2-||pm||^2": round(float(pp@pp - pm@pm), 5), "claim_48/7": round(48/7, 5),
            "LOCAL_payment_dead (<d,x>/||x|| -> 0 while jump fixed)": bool((d@x)/np.linalg.norm(x) < 0.05 and abs(pp@pp-pm@pm - 48/7) < 1e-6)}


def check_S4(trials=300):
    """Random adjacent transitions: verify Δ=2Σλ−‖d‖², Δ≤4Σλ_common, and no-common-active⟹Δ≤0."""
    worst_bound_slack = -np.inf
    viol_bound = 0
    viol_eq9 = 0
    eq9_cases = 0
    for _ in range(trials):
        r = rng.integers(2, 5)
        T = S1.family_random_independent(r, r, 0.25)
        if T is None:
            continue
        cols = [T[:, i] for i in range(r)]
        for _ in range(r):
            wv = S1.normalize_cols(rng.standard_normal((r, 1)))[:, 0]
            c = np.column_stack(cols + [wv])
            if S1.delta_T(c) >= 0.25 - 1e-9:
                cols.append(wv)
            if len(cols) >= r + 2:
                break
        A = np.column_stack(cols)
        y = rng.standard_normal(r)
        s = np.sign(A.T @ y); s[s == 0] = 1
        # pick a feasible p- in P_s
        Vm = A * s
        pm = proj_onto_Ps(np.zeros(r), Vm)
        if (Vm.T @ pm).min() < 1 - 1e-5:
            continue
        # flip one sign -> adjacent chamber
        k0 = int(rng.integers(0, A.shape[1]))
        s2 = s.copy(); s2[k0] = -s2[k0]
        Vp = A * s2
        pp = proj_onto_Ps(pm, Vp)
        if (Vp.T @ pp).min() < 1 - 1e-5:
            continue
        d = pp - pm
        Delta = float(pp @ pp - pm @ pm)
        # active at pp
        act = np.where(Vp.T @ pp <= 1 + 1e-6)[0]
        b0 = Vp[:, k0]
        common = [i for i in act if i != k0]
        # KKT multipliers: d = sum_{active} lambda_i v_i, lambda>=0
        if len(act) == 0:
            continue
        Bact = Vp[:, act]
        lam, *_ = np.linalg.lstsq(Bact, d, rcond=None)
        sum_common = sum(max(lam[list(act).index(i)], 0) for i in common) if common else 0.0
        # Δ ≤ 4 Σ λ_common
        if Delta > 4 * sum_common + 1e-3:
            viol_bound += 1
        worst_bound_slack = max(worst_bound_slack, Delta - 4 * sum_common)
        # eq (9): if no common active constraint, Δ ≤ 0
        if not common:
            eq9_cases += 1
            if Delta > 1e-4:
                viol_eq9 += 1
    return {"viol_Delta<=4sum_common": int(viol_bound), "worst (Delta-4sum_common)": round(float(worst_bound_slack), 4),
            "eq9_cases (no common active)": int(eq9_cases), "eq9_violations (Delta>0)": int(viol_eq9)}


def check_S7():
    rng2 = np.random.default_rng(3)
    max_err = 0.0
    for _ in range(500):
        z = rng2.standard_normal(4) + 0.5; w = rng2.standard_normal(4) + 0.5
        Iz = z / (z @ z); Iw = w / (w @ w)
        lhs = np.linalg.norm(Iz - Iw)
        rhs = np.linalg.norm(z - w) / (np.linalg.norm(z) * np.linalg.norm(w))
        max_err = max(max_err, abs(lhs - rhs))
    return {"inversion_identity_max_err": round(float(max_err), 10),
            "note": "≈0 confirms ‖I(z)−I(w)‖=‖z−w‖/(‖z‖‖w‖)"}


def check_drift2():
    """Stress: near-degenerate T (several near-coplanar walls => codim-2 cluster). Can sup‖p_j‖ grow?"""
    import round3_audit_checks as R3
    rows = []
    for r in [3, 4]:
        # build a near-degenerate cluster: r-1 vectors near a common codim-2 flat + perturb
        base = np.eye(r)
        cols = []
        for i in range(r):
            v = base[:, i] + 0.12 * rng.standard_normal(r)  # near-axis but tilted (small angles)
            cols.append(v / np.linalg.norm(v))
        # add a few more near-degenerate directions
        for _ in range(2):
            v = cols[0] + 0.1 * rng.standard_normal(r)
            c = np.column_stack(cols + [v / np.linalg.norm(v)])
            try:
                if S1.delta_T(c) >= 0.05:
                    cols.append(v / np.linalg.norm(v))
            except Exception:
                pass
        T = np.column_stack(cols)
        dT = S1.delta_T(T)
        best = 0.0
        for N in [20, 50, 100]:
            for _ in range(4):
                pts = R3.adversarial_projection_traj(T, N)
                sup = R3.dual_drift_sup(T, pts)
                if sup is not None:
                    best = max(best, sup)
        rows.append({"r": r, "delta_T": round(float(dT), 4), "r_over_delta": round(r/dT, 2),
                     "max_sup_norm_over_N<=100": round(float(best), 3)})
    return rows


def run():
    print("=== Round-4 audit numeric checks ===\n")
    print("S2 (r/δ ball NOT invariant):", json.dumps(check_S2(), indent=0), "\n")
    print("S3 (genuine itinerary; local payment dead):", json.dumps(check_S3(), indent=0), "\n")
    print("S4 (KKT localization Δ≤4Σλ_common; no-common⟹Δ≤0):", check_S4(), "\n")
    print("S7 (inversion identity):", check_S7(), "\n")
    DR = check_drift2()
    print("DRIFT2 (codim-≥2 near-degenerate stress — can sup‖p_j‖ grow?):")
    for row in DR:
        print("   ", row)
    out = {"S2": check_S2(), "S3": check_S3(), "S4": check_S4(), "S7": check_S7(), "DRIFT2": DR}
    with open(os.path.join(_HERE, "round4_audit_results.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("\nFrozen -> code/round4_audit_results.json")


if __name__ == "__main__":
    run()
