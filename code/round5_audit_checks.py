"""
Round-5 audit — numeric verification of the FRESH attacker's claims. Fixed seed; scipy.

Checks:
  RANK2.  §3 closure: r=2 ⟹ sup_j‖p_j‖ ≤ r/δ on admissible itineraries (the new base case).
  CONTRACT. §2 Step 2: full-rank spanning block linear part Q=∏ P_{H_i^⊥} has ‖Q‖ ≤ β_k=1/√(1+K^{−2(k−1)}),
            K=2r/δ. (Verify the contraction the all-word bound rests on.)
  TWOFLAT. §2 Step 1: d_{A^⊥∩B^⊥}(x) ≤ K·max{d_{A^⊥}(x), d_{B^⊥}(x)} for T-spanned A,B.
  COCYCLE. §5 probe: over closed (cyclic) chamber blocks, compute the affine map A_B(p)=Q_B p+b_B and
           ‖(I−Q_B)^† b_B‖ (the would-be super-poly fixed cycle). Does it stay ≤ poly(r,1/δ)?
"""
import json
import os
import numpy as np

import sim1_killtest as S1
import round3_audit_checks as R3  # adversarial_projection_traj, dual_drift_sup, proj_onto_Ps

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


def check_rank2():
    out = []
    worst_ratio = 0.0
    viol = 0
    for trial in range(12):
        # random unit vectors in R^2 (lines), keep delta_T up
        m = int(rng.integers(3, 7))
        angs = np.sort(rng.uniform(0, np.pi, size=m))
        T = np.array([[np.cos(a), np.sin(a)] for a in angs]).T
        dT = S1.delta_T(T)
        if dT < 0.15:
            continue
        best = 0.0
        for _ in range(6):
            pts = R3.adversarial_projection_traj(T, 120)
            sup = R3.dual_drift_sup(T, pts)
            if sup is not None:
                best = max(best, sup)
        bound = 2.0 / dT  # r/δ with r=2
        ratio = best / bound
        worst_ratio = max(worst_ratio, ratio)
        if best > bound + 1e-3:
            viol += 1
        out.append({"m": m, "delta_T": round(float(dT), 4), "sup": round(best, 3),
                    "r/delta=2/delta": round(bound, 3), "ok(<=)": best <= bound + 1e-3})
    return {"cases": out, "worst_sup_over_bound": round(float(worst_ratio), 4), "violations": viol}


def check_contraction():
    """Random full-rank spanning blocks of T-spanned flats; check ‖Q‖ ≤ β_k."""
    worst_excess = -np.inf
    viol = 0
    for _ in range(200):
        r = int(rng.integers(2, 6))
        T = S1.family_random_independent(r, r, 0.25)
        if T is None:
            continue
        dT = S1.delta_T(T); K = 2 * r / dT
        # build a spanning block of flats H_i = span of a random subset of T (each dim>=1)
        n = r + int(rng.integers(0, 3))
        Ms = []
        union_rank = 0
        cols_seen = []
        for _ in range(n):
            sz = int(rng.integers(1, r))
            idx = rng.choice(r, size=sz, replace=False)
            H = T[:, idx]
            Q, _ = np.linalg.qr(H)
            Q = Q[:, :np.linalg.matrix_rank(H)]
            PH = Q @ Q.T
            Ms.append(np.eye(r) - PH)  # P_{H^⊥}
            cols_seen.extend(list(idx))
        if len(set(cols_seen)) < r:
            continue  # not spanning
        Q = np.eye(r)
        for M in Ms:
            Q = M @ Q
        normQ = float(np.linalg.svd(Q, compute_uv=False)[0])
        k = r
        beta_k = 1.0 / np.sqrt(1 + K**(-2*(k-1)))
        worst_excess = max(worst_excess, normQ - beta_k)
        if normQ > beta_k + 1e-6:
            viol += 1
    return {"worst (||Q||-beta_k)": round(float(worst_excess), 6), "violations": int(viol),
            "note": "<=0 confirms ||Q||<=beta_k (the block contraction)"}


def check_twoflat():
    worst_ratio = -np.inf
    viol = 0
    for _ in range(400):
        r = int(rng.integers(2, 6))
        T = S1.family_random_independent(r, r, 0.25)
        if T is None:
            continue
        dT = S1.delta_T(T); K = 2 * r / dT
        ia = rng.choice(r, size=int(rng.integers(1, r)), replace=False)
        ib = rng.choice(r, size=int(rng.integers(1, r)), replace=False)
        A = T[:, ia]; B = T[:, ib]
        QA, _ = np.linalg.qr(A); QA = QA[:, :np.linalg.matrix_rank(A)]
        QB, _ = np.linalg.qr(B); QB = QB[:, :np.linalg.matrix_rank(B)]
        Aperp = np.eye(r) - QA @ QA.T
        Bperp = np.eye(r) - QB @ QB.T
        # A^perp ∩ B^perp = (A+B)^perp
        AB = np.column_stack([A, B])
        QAB, _ = np.linalg.qr(AB); QAB = QAB[:, :np.linalg.matrix_rank(AB)]
        ABperp = np.eye(r) - QAB @ QAB.T
        x = rng.standard_normal(r)
        dM = np.linalg.norm(Aperp @ x)  # d_{(A^perp)^perp}=d_A? careful: d_{A^⊥}(x)=‖P_A x‖
        # d_{A^⊥}(x) = distance from x to A^⊥ = ‖P_A x‖
        dA = np.linalg.norm(QA @ (QA.T @ x))
        dB = np.linalg.norm(QB @ (QB.T @ x))
        # d_{A^⊥∩B^⊥}(x)=‖P_{A+B} x‖
        dAB = np.linalg.norm(QAB @ (QAB.T @ x))
        rhs = K * max(dA, dB)
        if rhs > 1e-12:
            worst_ratio = max(worst_ratio, dAB / rhs)
        if dAB > rhs + 1e-6:
            viol += 1
    return {"worst dAB/(K*max)": round(float(worst_ratio), 4), "violations": int(viol),
            "note": "<=1 confirms two-flat regularity (eq 1)"}


def check_cocycle_probe():
    """Closed cyclic chamber blocks: A_B(p)=Q_B p + b_B; check ‖(I−Q_B)^† b_B‖ stays bounded (no super-poly cycle)."""
    out = []
    for r in [2, 3]:
        T = S1.family_random_independent(r, r, 0.25)
        if T is None:
            continue
        dT = S1.delta_T(T)
        A = T
        worst = 0.0
        for _ in range(30):
            # random cyclic itinerary of chambers from a closed-ish trajectory
            pts = R3.adversarial_projection_traj(T, int(rng.integers(8, 25)))
            seq = []
            for y in pts:
                s = np.sign(A.T @ y); s[s == 0] = 1
                seq.append(s)
            # make it a closed block: append reverse to return near start chamber
            seq = seq + seq[::-1]
            # affine map of the block: A_B(p) = run dual updates; linear in p
            def run(p0):
                p = p0.copy()
                for s in seq:
                    V = A * s
                    if (V.T @ p).min() < 1 - 1e-6:
                        p = R3.proj_onto_Ps(p, V, warm=p)
                return p
            b_B = run(np.zeros(r))
            # linear part columns
            QB = np.zeros((r, r))
            for i in range(r):
                ei = np.zeros(r); ei[i] = 1.0
                QB[:, i] = run(ei) - b_B
            ImQ = np.eye(r) - QB
            fix = np.linalg.pinv(ImQ) @ b_B
            worst = max(worst, float(np.linalg.norm(fix)))
        out.append({"r": r, "delta_T": round(float(dT), 4), "r/delta": round(r/dT, 2),
                    "worst ||(I-Q_B)^+ b_B||": round(worst, 3)})
    return out


def run():
    print("=== Round-5 audit numeric checks ===\n")
    R2 = check_rank2()
    print("RANK2 (§3 closure sup<=r/δ):")
    for c in R2["cases"]:
        print("   ", c)
    print("   worst sup/bound:", R2["worst_sup_over_bound"], "violations:", R2["violations"], "\n")
    CT = check_contraction(); print("CONTRACT (§2 ‖Q‖<=β_k):", CT, "\n")
    TF = check_twoflat(); print("TWOFLAT (§2 eq1):", TF, "\n")
    CO = check_cocycle_probe()
    print("COCYCLE probe (closed blocks ‖(I-Q_B)^+ b_B‖ — super-poly?):")
    for c in CO:
        print("   ", c)
    def _conv(o):
        return o.item() if hasattr(o, "item") else str(o)
    with open(os.path.join(_HERE, "round5_audit_results.json"), "w") as f:
        json.dump({"RANK2": R2, "CONTRACT": CT, "TWOFLAT": TF, "COCYCLE": CO}, f, indent=2, default=_conv)
    print("\nFrozen -> code/round5_audit_results.json")


if __name__ == "__main__":
    run()
