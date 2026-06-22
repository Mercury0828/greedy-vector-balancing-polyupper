"""
Round-2 audit — numeric verification of GPT-5.5-Pro's Round-2 claims. Fixed seed; scipy QP/LP.

Checks:
  T1. Theorem 1: min-norm margin-1 chamber certificate ‖p_s‖ ≤ R_loc = O(r²/δ²). Solve the QP
      min‖p‖ s.t. Mᵀp≥1 over many realizable chambers; compare to R_loc and to r²/δ².
  R3. Rank-3 obstruction: δ_T of the equiangular-3/4 config (claim √(5/14)≈0.598) and LP-infeasibility
      of the "odd-one-out" margin system (9) ⇒ no convex F linear on the 8 original chambers.
  TV. The DIRECT probe of (★) (via P4-upgrade: h_K(y)=max chain Σ‖y_j−y_{j-1}‖): adversarially maximize
      the projection-trajectory total variation Σ_j|⟨y_{j-1},t_j⟩| over chains, vs r at δ_T≥1/4.
      Pre-registered: poly growth ⟹ (★)-consistent; clear super-poly ⟹ refutation evidence.
"""
import itertools
import json
import os
import numpy as np
from scipy.optimize import minimize, linprog

import sim1_killtest as S1
from round1_audit_checks import circuit_imbalance

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


# ---------- T1. Theorem 1 certificate ----------
def min_norm_certificate(M):
    """min ‖p‖ s.t. Mᵀp ≥ 1 (M: d×m columns v_i). Returns (p, ‖p‖) or (None, inf) if infeasible."""
    d, m = M.shape
    # feasible start: p0 = c * mean(v_i) scaled so margins ~>=1 if realizable
    mean_v = M.mean(axis=1)
    p0 = mean_v * (1.0 / max(1e-6, (M.T @ mean_v).min())) if (M.T @ mean_v).min() > 1e-9 else np.zeros(d)
    cons = {"type": "ineq", "fun": lambda p: M.T @ p - 1.0, "jac": lambda p: M.T}
    res = minimize(lambda p: p @ p, p0, jac=lambda p: 2 * p, constraints=[cons],
                   method="SLSQP", options={"maxiter": 500, "ftol": 1e-10})
    if res.success and (M.T @ res.x).min() >= 1 - 1e-6:
        return res.x, float(np.linalg.norm(res.x))
    return None, np.inf


def check_T1():
    out = []
    for (r, delta) in [(2, 0.25), (3, 0.25), (4, 0.25), (5, 0.25), (6, 0.25), (4, 0.5), (5, 0.1)]:
        # adversarial T (representatives, unit cols); use rand-indep + a few extra directions
        T = S1.family_random_independent(r, r, delta)
        if T is None:
            continue
        # add a couple extra non-collinear unit directions to make chambers nontrivial (keep delta)
        extra = []
        for _ in range(2 * r):
            w = S1.normalize_cols(rng.standard_normal((r, 1)))[:, 0]
            cand = np.column_stack([T] + extra + [w])
            try:
                if S1.delta_T(cand) >= delta - 1e-9:
                    extra.append(w)
            except Exception:
                pass
            if len(extra) >= r:
                break
        Tm = np.column_stack([T] + extra) if extra else T
        kappa, _ = circuit_imbalance(Tm) if Tm.shape[1] > Tm.shape[0] else (1.0 / S1.delta_T(Tm), 0)
        dT = S1.delta_T(Tm)
        R_loc = np.sqrt(r * (r + 1)) * (1 + (r + 1) * kappa) / dT
        worst_norm = 0.0
        viol = 0
        for _ in range(40):
            y = rng.standard_normal(r)
            s = np.sign(Tm.T @ y)
            s[s == 0] = 1
            M = Tm * s  # columns v_i = s_i t_i
            p, pn = min_norm_certificate(M)
            if p is None:
                continue
            worst_norm = max(worst_norm, pn)
            if pn > R_loc + 1e-4:
                viol += 1
        out.append({"r": r, "delta": delta, "m": int(Tm.shape[1]), "delta_T": round(float(dT), 4),
                    "kappa": round(float(kappa), 4), "R_loc": round(float(R_loc), 2),
                    "worst_cert_norm": round(float(worst_norm), 3),
                    "r2_over_delta2": round(r**2 / dT**2, 2), "violations_vs_Rloc": int(viol)})
    return out


# ---------- R3. rank-3 obstruction ----------
def check_R3():
    c = 0.75
    G = (1 - c) * np.eye(3) + c * np.ones((3, 3))
    L = np.linalg.cholesky(G)
    T = L.T  # columns have the prescribed Gram
    T = S1.normalize_cols(T)
    dT = S1.delta_T(T)
    Ginv_diag = np.diag(np.linalg.inv(G))
    # LP: find w>=0 with w_j - c*sum_{i!=j} w_i >= 1 for j=1,2,3  (odd-one-out chambers)
    # linprog minimizes c^T x s.t. A_ub x <= b_ub; encode -(w_j - c*sum_{i!=j}w_i) <= -1
    A = np.zeros((3, 3))
    for j in range(3):
        for i in range(3):
            A[j, i] = -(1.0 if i == j else -c)
    b = -np.ones(3)
    res = linprog(c=np.zeros(3), A_ub=A, b_ub=b, bounds=[(0, None)] * 3, method="highs")
    return {"delta_T": round(float(dT), 4), "claimed_sqrt(5/14)": round(float(np.sqrt(5/14)), 4),
            "Ginv_diag": [round(float(x), 4) for x in Ginv_diag], "claimed_Ginv_ii": 14/5,
            "margin_LP_feasible": bool(res.success),
            "VERDICT": "obstruction holds (no convex F linear on 8 chambers)" if not res.success
            else "FEASIBLE — obstruction FAILS"}


# ---------- TV. adversarial projection-trajectory total variation ----------
def adversary_TV(T, beam_width=48, restarts=20, max_steps=None):
    """Maximize Σ_j |⟨y_{j-1}, t_j⟩| over chains y_j = y_{j-1} - ⟨y_{j-1},t_j⟩ t_j. Returns max TV / ‖y0‖."""
    d, n = T.shape
    if max_steps is None:
        max_steps = max(60, 25 * d)
    best = 0.0
    # beam over (y, accumulated_TV); seed several y0
    seeds = [S1.normalize_cols(rng.standard_normal((d, 1)))[:, 0] for _ in range(6)]
    for y0 in seeds:
        beam = [(y0.copy(), 0.0)]
        for _ in range(max_steps):
            cand = []
            for y, tv in beam:
                if np.linalg.norm(y) < 1e-6:
                    continue
                ips = T.T @ y
                # try the top directions by |ip| AND a few near-orthogonal (small |ip|) to prolong
                order = np.argsort(-np.abs(ips))
                pick = list(order[:6]) + list(order[-3:])
                for i in set(pick):
                    step = abs(ips[i])
                    if step < 1e-9:
                        continue
                    ynew = y - ips[i] * T[:, i]
                    cand.append((ynew, tv + step))
            if not cand:
                break
            cand.sort(key=lambda z: -z[1])
            best = max(best, cand[0][1])
            # dedup-ish keep top beam_width
            beam = cand[:beam_width]
        # stochastic restarts
    for _ in range(restarts):
        y = S1.normalize_cols(rng.standard_normal((d, 1)))[:, 0]
        tv = 0.0
        for _ in range(max_steps):
            if np.linalg.norm(y) < 1e-6:
                break
            ips = T.T @ y
            a = np.abs(ips)
            if a.max() < 1e-9:
                break
            # bias toward moderate steps (prolong trajectory)
            w = a / a.sum()
            i = rng.choice(n, p=w)
            tv += a[i]
            y = y - ips[i] * T[:, i]
        best = max(best, tv)
    return best  # ‖y0‖=1


def check_TV():
    theta = np.arcsin(0.25)
    rows = []
    for d in range(2, 9):
        cands = {}
        dp = max(1, d // 2)
        cands["gadgets"] = S1.family_orthogonal_gadgets(dp, theta)
        Ti = S1.family_random_independent(d, d, 0.25)
        if Ti is not None:
            cands["rand_indep"] = Ti
        cands["dep_pairs"] = S1.family_dependent_pairs(d, min(2, d // 2))
        best, who, dTbest = 0.0, None, None
        for name, T in cands.items():
            try:
                dT = S1.delta_T(T)
            except Exception:
                continue
            tv = adversary_TV(T)
            if tv > best:
                best, who, dTbest = tv, name, dT
        rows.append({"d": d, "max_TV_over_y0": round(float(best), 3), "winner": who,
                     "delta_T": round(float(dTbest), 4), "sqrt_d_over_delta": round(np.sqrt(d)/0.25, 2),
                     "exp_bound": round((2/0.25)**(d-1), 1)})
    ds = np.array([x["d"] for x in rows], float)
    ys = np.array([max(x["max_TV_over_y0"], 1e-9) for x in rows], float)
    poly_slope = float(np.polyfit(np.log(ds), np.log(ys), 1)[0])
    exp_slope = float(np.polyfit(ds, np.log(ys), 1)[0])
    return {"rows": rows, "loglog_poly_slope": round(poly_slope, 3), "semilog_exp_slope": round(exp_slope, 3)}


def run():
    print("=== Round-2 audit numeric checks ===\n")
    T1 = check_T1()
    print("T1 (Theorem 1 certificate ‖p_s‖ vs R_loc and r^2/delta^2):")
    for row in T1:
        print("   ", row)
    R3 = check_R3()
    print("\nR3 (rank-3 obstruction):", R3)
    TV = check_TV()
    print("\nTV (adversarial projection-trajectory total variation, the direct (star) probe):")
    for row in TV["rows"]:
        print("   ", row)
    print(f"   growth: log-log poly slope={TV['loglog_poly_slope']}  semilog exp slope={TV['semilog_exp_slope']}")
    with open(os.path.join(_HERE, "round2_audit_results.json"), "w") as f:
        json.dump({"T1": T1, "R3": R3, "TV": TV}, f, indent=2)
    print("\nFrozen -> code/round2_audit_results.json")


if __name__ == "__main__":
    run()
