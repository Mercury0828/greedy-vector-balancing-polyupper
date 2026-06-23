"""
Round-7 audit — numeric verification of the explicit rank-4 refutation of the POINT-valued holonomy.
Fixed (exact) construction. The point-cocycle was the orchestrator's Round-7 conjecture; the solver refutes
it with two excursions A,B from the same (J,ω) state with same linear part Q but different translations.

Checks:
  ARR.   The arrangement: a,b,c,d,e unit; δ_T²=242/1875; J⊂K⊊E (ranks 2,3,4); p_0∈P_{s_0}, active face=J.
  MAPS.  Compose the face projectors along the stated active faces ⟹ A_A=Q p+b_A, A_B=Q p+b_B; verify
         SAME Q (projector onto K^⊥=ℝn) and b_A≠b_B (matching eq 7), so NO common c_{J,ω} exists.
  CYL.   The invariant cylinder C: A_A(C)⊆C and A_B(C)⊆C (bounded hysteresis ⟹ no drift ⟹ NOT a refutation of ★).
"""
import json
import os
import numpy as np

import sim1_killtest as S1

_HERE = os.path.dirname(os.path.abspath(__file__))

s26, s30 = np.sqrt(26), np.sqrt(30)
a = np.array([1.0, 0, 0, 0]); b = np.array([0, 1.0, 0, 0])
c = np.array([3, 1, 4, 0]) / s26; d = np.array([1, 3, -2, 4]) / s30; e = np.array([-2, 1, -3, -4]) / s30
VEC = {"a": a, "b": b, "c": c, "d": d, "e": e}
T = np.column_stack([a, b, c, d, e])


def check_arr():
    units = {k: round(float(np.linalg.norm(v)), 8) for k, v in VEC.items()}
    dT = S1.delta_T(T)
    J = np.column_stack([a, b]); K = np.column_stack([a, b, e])
    s0 = {"a": 1, "b": 1, "c": 1, "d": -1, "e": -1}
    p0 = np.array([1.0, 1, 6, 0])
    signed_vals = {k: round(float(s0[k] * (VEC[k] @ p0)), 4) for k in VEC}
    in_P = all(s0[k] * (VEC[k] @ p0) >= 1 - 1e-9 for k in VEC)
    return {"units": units, "delta_T": round(float(dT), 6), "claim_sqrt(242/1875)": round(float(np.sqrt(242/1875)), 6),
            "rank_J": int(np.linalg.matrix_rank(J)), "rank_K": int(np.linalg.matrix_rank(K)), "rank_E": int(np.linalg.matrix_rank(T)),
            "p0_signed_vals": signed_vals, "p0_in_P_s0": bool(in_P), "||p0||": round(float(np.linalg.norm(p0)), 4)}


def face_proj_map(active_signed):
    """Return (Lin, off) for Π_M(p)=(I−Mᵀ(MMᵀ)⁻¹M)p + Mᵀ(MMᵀ)⁻¹1, M rows = signed active normals."""
    M = np.array(active_signed)  # k x 4
    G = M @ M.T
    Ginv = np.linalg.inv(G)
    Lin = np.eye(4) - M.T @ Ginv @ M
    off = M.T @ Ginv @ np.ones(M.shape[0])
    return Lin, off


def compose(faces):
    """faces: list of (dest_chamber_dict, active_set list). Compose Π's left-to-right (step1 first)."""
    Lin = np.eye(4); off = np.zeros(4)
    for chamber, active in faces:
        signed = [chamber[k] * VEC[k] for k in active]
        L, o = face_proj_map(signed)
        # new map = (L,o) ∘ (Lin,off): p -> L(Lin p+off)+o
        off = L @ off + o
        Lin = L @ Lin
    return Lin, off


def chamber(t): return dict(zip("abcde", t))


def check_maps():
    # Excursion A destinations + active sets
    A_dests = [(+1,+1,+1,-1,+1),(+1,-1,+1,-1,+1),(+1,-1,+1,-1,-1),(-1,-1,+1,-1,-1),
               (-1,-1,+1,-1,+1),(-1,-1,+1,-1,-1),(+1,-1,+1,-1,-1),(+1,+1,+1,-1,-1)]
    A_active = [["a","e"],["a","b","e"],["e"],["a","e"],["e"],["a","e"],["a"],["a","b"]]
    B_dests = [(+1,+1,+1,-1,+1),(-1,+1,+1,-1,+1),(-1,-1,+1,-1,+1),(-1,+1,+1,-1,+1),
               (-1,+1,+1,-1,-1),(-1,-1,+1,-1,-1),(+1,-1,+1,-1,-1),(+1,+1,+1,-1,-1)]
    B_active = [["a","e"],["a"],["a","b"],["a","b"],["a","b","e"],["a","b"],["a","b"],["a","b"]]
    QA, bA = compose([(chamber(t), ac) for t, ac in zip(A_dests, A_active)])
    QB, bB = compose([(chamber(t), ac) for t, ac in zip(B_dests, B_active)])
    m = np.array([0, 0, 3.0, 4]); n = np.array([0, 0, 4.0, -3])
    # expected Q = projector onto ℝn
    Qexp = np.outer(n, n) / (n @ n)
    bA_exp = np.array([1.0, 1, 0, 0]) + ((11 + 12*np.sqrt(30))/325) * m
    bB_exp = np.array([1.0, 1, 0, 0]) + ((3 + np.sqrt(30))/25) * m
    return {"Q_A==Q_B": round(float(np.abs(QA - QB).max()), 8),
            "Q==proj_onto_n": round(float(np.abs(QA - Qexp).max()), 6),
            "b_A_matches_eq7": round(float(np.linalg.norm(bA - bA_exp)), 6),
            "b_B_matches_eq7": round(float(np.linalg.norm(bB - bB_exp)), 6),
            "||b_A - b_B||": round(float(np.linalg.norm(bA - bB)), 6),
            "b_A!=b_B (no common c)": bool(np.linalg.norm(bA - bB) > 1e-6),
            "bA": [round(float(x), 4) for x in bA], "bB": [round(float(x), 4) for x in bB]}


def check_cylinder():
    m = np.array([0, 0, 3.0, 4]); n = np.array([0, 0, 4.0, -3])
    base = np.array([1.0, 1, 0, 0])
    t0 = (11 + 12*np.sqrt(30))/325; t1 = (3 + np.sqrt(30))/25
    # rebuild maps
    mm = check_maps()  # ensures consistency; recompute maps here
    A_dests = [(+1,+1,+1,-1,+1),(+1,-1,+1,-1,+1),(+1,-1,+1,-1,-1),(-1,-1,+1,-1,-1),
               (-1,-1,+1,-1,+1),(-1,-1,+1,-1,-1),(+1,-1,+1,-1,-1),(+1,+1,+1,-1,-1)]
    A_active = [["a","e"],["a","b","e"],["e"],["a","e"],["e"],["a","e"],["a"],["a","b"]]
    B_dests = [(+1,+1,+1,-1,+1),(-1,+1,+1,-1,+1),(-1,-1,+1,-1,+1),(-1,+1,+1,-1,+1),
               (-1,+1,+1,-1,-1),(-1,-1,+1,-1,-1),(+1,-1,+1,-1,-1),(+1,+1,+1,-1,-1)]
    B_active = [["a","e"],["a"],["a","b"],["a","b"],["a","b","e"],["a","b"],["a","b"],["a","b"]]
    QA, bA = compose([(chamber(t), ac) for t, ac in zip(A_dests, A_active)])
    QB, bB = compose([(chamber(t), ac) for t, ac in zip(B_dests, B_active)])
    # sample cylinder points base + s*m + u*n, s in [t0,t1], u in [-3,3]
    rng = np.random.default_rng(7)
    max_excursA = 0.0; max_excursB = 0.0
    for _ in range(2000):
        s = rng.uniform(min(t0, t1), max(t0, t1)); u = rng.uniform(-3, 3)
        p = base + s*m + u*n
        for (Q, bb, tag) in [(QA, bA, "A"), (QB, bB, "B")]:
            q = Q @ p + bb
            # decompose q-base into m,n coords; check m-coord in [t0,t1]
            sc = ((q - base) @ m) / (m @ m)
            dev = (sc - np.clip(sc, min(t0, t1), max(t0, t1)))
            if tag == "A":
                max_excursA = max(max_excursA, abs(dev))
            else:
                max_excursB = max(max_excursB, abs(dev))
    return {"m_coord_interval": [round(min(t0, t1), 4), round(max(t0, t1), 4)],
            "max_m_excursion_A": round(float(max_excursA), 8), "max_m_excursion_B": round(float(max_excursB), 8),
            "cylinder_invariant(both)": bool(max_excursA < 1e-6 and max_excursB < 1e-6)}


def run():
    print("=== Round-7 audit numeric checks ===\n")
    AR = check_arr(); print("ARR:", json.dumps(AR), "\n")
    MP = check_maps(); print("MAPS:", json.dumps(MP), "\n")
    CY = check_cylinder(); print("CYL:", json.dumps(CY), "\n")
    with open(os.path.join(_HERE, "round7_audit_results.json"), "w") as f:
        json.dump({"ARR": AR, "MAPS": MP, "CYL": CY}, f, indent=2, default=str)
    print("Frozen -> code/round7_audit_results.json")


if __name__ == "__main__":
    run()
