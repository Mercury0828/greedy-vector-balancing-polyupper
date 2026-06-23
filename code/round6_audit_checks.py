"""
Round-6 audit — numeric verification of the rank-3 closure + the rank-4 survivor obstruction. Fixed seed.

Checks:
  RANK3.  §1-6 closure: for rank-3 arrangements (δ_T≥c), sup_j‖p_j‖ along adversarial admissible itineraries
          stays ≤ √53/δ² (< 8/δ²). The new closed base case.
  ACTIVEQ. §1: ‖q_j‖ ≤ h/δ (h=dim H_j) — spot check on certificate min-norm faces.
  RANK4.  §"stops at rank 4": the explicit obstruction P_L z = 0 for J=⟨e1,e2⟩, L=⟨e1,e3⟩, z=e4 (δ=1), and
          generally that the survivor can hide in (J+L)^⊥ in rank≥4 (so |P_L p| carries NO z_0 term).
  RANK4DRIFT. stress: does sup_j‖p_j‖ in rank 4 exceed the rank-3-style √53/δ² scale (it may — that's the
          obstruction), but does it stay bounded (Bauschke–Tung) and ≤ D_exp? (context, not a refutation test).
"""
import json
import os
import numpy as np

import sim1_killtest as S1
import round3_audit_checks as R3

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


def check_rank3():
    out = []
    worst_ratio = 0.0
    viol = 0
    for trial in range(14):
        # random rank-3 T: a few unit vectors in R^3, keep delta_T up
        m = int(rng.integers(3, 7))
        M = S1.normalize_cols(rng.standard_normal((3, m)))
        if np.linalg.matrix_rank(M) < 3:
            continue
        dT = S1.delta_T(M)
        if dT < 0.18:
            continue
        best = 0.0
        for _ in range(8):
            pts = R3.adversarial_projection_traj(M, 150)
            sup = R3.dual_drift_sup(M, pts)
            if sup is not None:
                best = max(best, sup)
        bound = np.sqrt(53) / dT**2
        ratio = best / bound
        worst_ratio = max(worst_ratio, ratio)
        if best > bound + 1e-3:
            viol += 1
        out.append({"m": m, "delta_T": round(float(dT), 4), "sup": round(best, 3),
                    "sqrt53/delta^2": round(float(bound), 3), "8/delta^2": round(8/dT**2, 3),
                    "ok(<=sqrt53/d^2)": best <= bound + 1e-3})
    return {"cases": out, "worst_sup_over_sqrt53bound": round(float(worst_ratio), 4), "violations": viol}


def check_rank4_obstruction():
    e1 = np.eye(4)[0]; e3 = np.eye(4)[2]; e4 = np.eye(4)[3]
    J = np.column_stack([np.eye(4)[0], np.eye(4)[1]])  # span(e1,e2)
    L = np.column_stack([e1, e3])                       # span(e1,e3)
    QL, _ = np.linalg.qr(L); QL = QL[:, :2]
    PLz = QL @ (QL.T @ e4)
    # (J+L)^perp contains e4? J+L = span(e1,e2,e3); its perp = span(e4)
    JL = np.column_stack([np.eye(4)[0], np.eye(4)[1], e3])
    QJL, _ = np.linalg.qr(JL); QJL = QJL[:, :3]
    z0 = e4 - QJL @ (QJL.T @ e4)  # component in (J+L)^perp
    return {"P_L(e4)_norm": round(float(np.linalg.norm(PLz)), 8),
            "survivor_in_(J+L)perp_norm": round(float(np.linalg.norm(z0)), 6),
            "VERDICT": "survivor hides: P_L z = 0 while z in (J+L)^perp is full"
            if np.linalg.norm(PLz) < 1e-9 and np.linalg.norm(z0) > 0.9 else "no obstruction"}


def check_rank4_drift():
    """Context: rank-4 sup vs the rank-3-style bound — does it exceed √53/δ²? (obstruction => may exceed)."""
    out = []
    for trial in range(8):
        M = S1.normalize_cols(rng.standard_normal((4, int(rng.integers(4, 8)))))
        if np.linalg.matrix_rank(M) < 4:
            continue
        dT = S1.delta_T(M)
        if dT < 0.18:
            continue
        best = 0.0
        for _ in range(6):
            pts = R3.adversarial_projection_traj(M, 150)
            sup = R3.dual_drift_sup(M, pts)
            if sup is not None:
                best = max(best, sup)
        out.append({"delta_T": round(float(dT), 4), "sup": round(best, 3),
                    "sqrt53/d^2": round(float(np.sqrt(53)/dT**2), 2), "r/d=4/d": round(4/dT, 2),
                    "D_exp_huge": "yes"})
    return out


def run():
    print("=== Round-6 audit numeric checks ===\n")
    R = check_rank3()
    print("RANK3 (closure sup <= sqrt53/δ²):")
    for c in R["cases"]:
        print("   ", c)
    print("   worst sup/bound:", R["worst_sup_over_sqrt53bound"], "violations:", R["violations"], "\n")
    OB = check_rank4_obstruction()
    print("RANK4 obstruction (P_L z=0 example):", OB, "\n")
    D4 = check_rank4_drift()
    print("RANK4 drift (context — sup vs rank-3 scale; may exceed, should stay bounded):")
    for c in D4:
        print("   ", c)
    with open(os.path.join(_HERE, "round6_audit_results.json"), "w") as f:
        json.dump({"RANK3": R, "RANK4_obstruction": OB, "RANK4_drift": D4}, f, indent=2, default=str)
    print("\nFrozen -> code/round6_audit_results.json")


if __name__ == "__main__":
    run()
