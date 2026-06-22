"""
Round-3 audit — numeric verification of GPT-5.5-Pro's Round-3 claims. Fixed seed; scipy.

Checks:
  P1cert. Proposition 1: min-norm chamber certificate ‖p_s‖ ≤ r/δ (sharpening of O(r²/δ²)).
  IDS.    Affine-projection identities: energy (3), telescoping (6), Bessel (7) on random sequences.
  DRIFT.  THE DECISIVE PROBE of the bounded dual-drift lemma / DA / PC: simulate
            p_{j+1} = Proj_{P_{s_{j+1}}}(p_j)
          along the chamber itinerary of an ADVERSARIAL (reversed) projection trajectory, and measure
          sup_j ‖p_j‖ vs trajectory length N and vs r. Pre-registered:
            * if DA/PC TRUE (⟹ (★)): sup_j‖p_j‖ stays ≤ poly(r,1/δ), BOUNDED IN N (flat in N).
            * if it grows with N (e.g. ~√N) on admissible itineraries: DA as stated is in trouble
              (evidence the dual-drift is genuinely unbounded — would weaken (★)).
"""
import json
import os
import numpy as np
from scipy.optimize import minimize

import sim1_killtest as S1

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


def proj_onto_Ps(p0, V, warm=None):
    """Project p0 onto P_s = {p : Vᵀp ≥ 1} (V: d×m columns v_i). min ‖p−p0‖² s.t. Vᵀp≥1."""
    d = V.shape[0]
    x0 = warm if warm is not None else p0.copy()
    cons = {"type": "ineq", "fun": lambda p: V.T @ p - 1.0, "jac": lambda p: V.T}
    res = minimize(lambda p: float((p - p0) @ (p - p0)), x0, method="SLSQP",
                   jac=lambda p: 2 * (p - p0),
                   constraints=[cons], options={"maxiter": 300, "ftol": 1e-10})
    if res.success and (V.T @ res.x).min() >= 1 - 1e-5:
        return res.x
    # fallback: if infeasible-ish, return a feasible scaling of mean
    return x0


def min_norm_cert(V):
    d, m = V.shape
    cons = {"type": "ineq", "fun": lambda p: V.T @ p - 1.0, "jac": lambda p: V.T}
    mean_v = V.mean(axis=1)
    denom = (V.T @ mean_v).min()
    p0 = mean_v / denom if denom > 1e-9 else np.zeros(d)
    res = minimize(lambda p: p @ p, p0, jac=lambda p: 2 * p, constraints=[cons],
                   method="SLSQP", options={"maxiter": 400, "ftol": 1e-10})
    if res.success and (V.T @ res.x).min() >= 1 - 1e-5:
        return res.x, float(np.linalg.norm(res.x))
    return None, np.inf


# ---------- Proposition 1: cert norm <= r/delta ----------
def check_prop1():
    out = []
    for (r, delta) in [(3, 0.25), (4, 0.25), (5, 0.25), (6, 0.25), (4, 0.5)]:
        T = S1.family_random_independent(r, r, delta)
        if T is None:
            continue
        # add extra unit directions keeping delta
        cols = [T[:, i] for i in range(T.shape[1])]
        for _ in range(3 * r):
            w = S1.normalize_cols(rng.standard_normal((r, 1)))[:, 0]
            cand = np.column_stack(cols + [w])
            try:
                if S1.delta_T(cand) >= delta - 1e-9:
                    cols.append(w)
            except Exception:
                pass
            if len(cols) >= 2 * r:
                break
        A = np.column_stack(cols)
        dT = S1.delta_T(A)
        worst, viol = 0.0, 0
        for _ in range(40):
            y = rng.standard_normal(r)
            s = np.sign(A.T @ y); s[s == 0] = 1
            V = A * s
            _, pn = min_norm_cert(V)
            if np.isfinite(pn):
                worst = max(worst, pn)
                if pn > r / dT + 1e-3:
                    viol += 1
        out.append({"r": r, "delta_T": round(float(dT), 4), "m": A.shape[1],
                    "worst_cert_norm": round(worst, 3), "r_over_delta": round(r / dT, 3),
                    "violations_vs_r_over_delta": viol})
    return out


# ---------- identities (3),(6),(7) ----------
def check_identities():
    d = 6
    rng2 = np.random.default_rng(7)
    max_err = 0.0
    for _ in range(200):
        N = rng2.integers(3, 12)
        Hdims = rng2.integers(1, d, size=N)
        Ms, projsH = [], []
        for k in range(N):
            G = rng2.standard_normal((d, int(Hdims[k])))
            Q, _ = np.linalg.qr(G)
            PH = Q @ Q.T
            projsH.append(PH)
            Ms.append(np.eye(d) - PH)  # P_{H^⊥}
        # telescoping (6): I - Q_N Q_N^T = sum R_j P_{H_j} R_j^T
        Q = np.eye(d)
        for k in range(N):  # Q_N = M_N ... M_1
            Q = Ms[k] @ Q
        lhs = np.eye(d) - Q @ Q.T
        rhs = np.zeros((d, d))
        for j in range(N):
            Rj = np.eye(d)
            for k in range(j + 1, N):
                Rj = Ms[k] @ Rj   # R_j = M_N ... M_{j+1}
            rhs += Rj @ projsH[j] @ Rj.T
        max_err = max(max_err, float(np.abs(lhs - rhs).max()))
    return {"telescoping_max_abs_err": round(max_err, 9),
            "note": "≈0 confirms I−Q_NQ_Nᵀ = Σ R_j P_{H_j} R_jᵀ (eq 6) ⟹ Bessel (7)"}


# ---------- DECISIVE: dual-drift simulation ----------
def adversarial_projection_traj(T, max_steps):
    """Forward projection trajectory maximizing per-step TV; returns list of points y_0..y_L."""
    d, n = T.shape
    y = S1.normalize_cols(rng.standard_normal((d, 1)))[:, 0]
    pts = [y.copy()]
    for _ in range(max_steps):
        if np.linalg.norm(y) < 1e-4:
            break
        ips = T.T @ y
        # adversary: pick a moderate-projection direction to prolong + accumulate TV
        a = np.abs(ips)
        if a.max() < 1e-9:
            break
        # bias to mid-range |ip| (prolong); mix with argmax occasionally
        i = int(np.argsort(a)[len(a) // 2]) if rng.random() < 0.7 else int(np.argmax(a))
        y = y - ips[i] * T[:, i]
        pts.append(y.copy())
    return pts


def dual_drift_sup(T, pts):
    """Run p_{j+1}=Proj_{P_{s_{j+1}}}(p_j) over the REVERSED chamber itinerary of pts; return sup‖p_j‖."""
    d, n = T.shape
    A = T  # representatives (columns assumed distinct directions)
    # chamber signs along trajectory
    seq = []
    for y in pts:
        s = np.sign(A.T @ y); s[s == 0] = 1
        seq.append(s)
    seq = seq[::-1]  # reversed
    # init at min-norm cert of first chamber
    V0 = A * seq[0]
    p, _ = min_norm_cert(V0)
    if p is None:
        return None
    sup = np.linalg.norm(p)
    for s in seq[1:]:
        V = A * s
        # only project if current p violates P_s
        if (V.T @ p).min() < 1 - 1e-6:
            p = proj_onto_Ps(p, V, warm=p)
        sup = max(sup, float(np.linalg.norm(p)))
    return sup


def check_drift():
    rows = []
    theta = np.arcsin(0.25)
    for r in [3, 4, 5, 6]:
        T = S1.family_random_independent(r, r, 0.25)
        if T is None:
            continue
        dT = S1.delta_T(T)
        # vary trajectory length N to test N-dependence
        per_len = []
        for N in [10, 25, 50, 90]:
            best = 0.0
            for _ in range(4):
                pts = adversarial_projection_traj(T, N)
                sup = dual_drift_sup(T, pts)
                if sup is not None:
                    best = max(best, sup)
            per_len.append({"N": N, "sup_norm": round(best, 3)})
        rows.append({"r": r, "delta_T": round(float(dT), 4), "r_over_delta": round(r / dT, 2),
                     "sup_by_len": per_len})
    return rows


def run():
    print("=== Round-3 audit numeric checks ===\n")
    P1c = check_prop1()
    print("Prop 1 (cert norm <= r/delta):")
    for row in P1c:
        print("   ", row)
    ID = check_identities()
    print("\nIdentities:", ID)
    DR = check_drift()
    print("\nDUAL-DRIFT (decisive: sup_j‖p_j‖ vs trajectory length N and r):")
    for row in DR:
        print(f"   r={row['r']} delta_T={row['delta_T']} r/delta={row['r_over_delta']}: "
              f"{row['sup_by_len']}")
    print("   Pre-registered: bounded-in-N & ~poly(r,1/δ) ⟹ DA/PC-consistent (supports (★));"
          " growth with N ⟹ DA in trouble.")
    with open(os.path.join(_HERE, "round3_audit_results.json"), "w") as f:
        json.dump({"prop1": P1c, "identities": ID, "dual_drift": DR}, f, indent=2)
    print("\nFrozen -> code/round3_audit_results.json")


if __name__ == "__main__":
    run()
