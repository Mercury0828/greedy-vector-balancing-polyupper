"""
Round-1 audit — numeric verification of GPT-5.5-Pro's load-bearing claims (orchestrator's own check).
Independent of the fresh-context audit agent. Fixed seed.

Claims checked:
  A. The "unit-WLOG" reduction is FALSE: counterexample T={u,v}, δ_T=1/4, unit-only max-norm = 1 but
     scaled model reaches 4.
  B. Refined P2: ‖P_{H(x)} x‖ ≤ q/(2δ_T), q = dim span N(x).
  C. Principal-angle lemma: sinθ(H,K) ≥ δ_T/r for T-spanned flats H,K.
  D. P3-revival bridge: κ_A ≤ 1/δ_A for UNIT columns (κ_A = circuit imbalance measure).
  E. Static B/δ counterexample (HS2 break-point): ‖P_{J+⟨t⟩}x‖ = B/δ while ‖P_J x‖=B, ⟨t,x⟩=0.
"""
import itertools
import os
import numpy as np

import sim1_killtest as S1  # delta_T, families, adversary

rng = np.random.default_rng(20260622)
_HERE = os.path.dirname(os.path.abspath(__file__))


# ---------- A. counterexample: unit-WLOG is false ----------
def check_A():
    c = np.sqrt(15) / 4
    u = np.array([0.0, 1.0])
    v = np.array([0.25, -c])
    T = np.column_stack([u, v])
    dT = S1.delta_T(T)
    # unit-only adversary (sim1 only sends full unit vectors) -> should be ~1
    unit_only = S1.adversary_beam(T, beam_width=64, restarts=40)
    # explicit scaled trajectory from GPT: x_m=(m/4)e1 ; send c*u then full v
    def greedy_add(S, w):
        # greedy sign so that s*w has non-positive inner product with S
        s = -np.sign(w @ S) if abs(w @ S) > 1e-15 else 1.0
        return S + s * w
    S = np.array([0.0, 0.0])
    maxn = 0.0
    for m in range(16):
        S = greedy_add(S, c * u)          # scaled steering move (orthogonal -> added)
        maxn = max(maxn, np.linalg.norm(S))
        S = greedy_add(S, v)              # full v (added since inner product <=0)
        maxn = max(maxn, np.linalg.norm(S))
    scaled_norm = np.linalg.norm(S)
    return {"delta_T": round(float(dT), 4),
            "unit_only_maxnorm": round(float(unit_only), 4),
            "scaled_explicit_final_norm": round(float(scaled_norm), 4),
            "scaled_maxnorm_along_traj": round(float(maxn), 4),
            "VERDICT": "scaled > unit-only" if scaled_norm > unit_only + 1e-6 else "NO GAP"}


# ---------- B. refined P2 ----------
def check_B(families):
    worst = -np.inf
    viol = 0
    for name, T in families:
        d, n = T.shape
        r = np.linalg.matrix_rank(T)
        dT = S1.delta_T(T)
        for _ in range(400):
            x = rng.standard_normal(d)
            x = x / np.linalg.norm(x) * rng.uniform(0.1, 4.0) * r / (2 * dT)
            ips = np.abs(T.T @ x)
            Nx = T[:, ips < 0.5]
            if Nx.shape[1] == 0:
                continue
            # projector onto H(x)=span N(x)
            U, s, _ = np.linalg.svd(Nx, full_matrices=False)
            Uk = U[:, s > 1e-9]
            q = Uk.shape[1]
            PHx = Uk @ (Uk.T @ x)
            lhs = np.linalg.norm(PHx)
            rhs = q / (2 * dT)
            ratio = lhs / rhs if rhs > 0 else 0
            worst = max(worst, ratio)
            if lhs > rhs + 1e-7:
                viol += 1
    return {"worst_ratio_lhs_over_bound": round(float(worst), 4), "violations": int(viol),
            "note": "ratio<=1 means refined P2 holds"}


# ---------- C. principal-angle lemma ----------
def principal_angles(Q1, Q2):
    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    s = np.clip(s, -1, 1)
    return np.arccos(s)  # principal angles ascending in cos => angles descending; sorted later

def check_C(families):
    worst_slack = np.inf
    viol = 0
    checked = 0
    for name, T in families:
        d, n = T.shape
        r = np.linalg.matrix_rank(T)
        dT = S1.delta_T(T)
        cols = list(range(n))
        subsets = []
        for k in range(1, min(r, 4) + 1):
            subsets += list(itertools.combinations(cols, k))
        if len(subsets) > 60:
            idx = rng.choice(len(subsets), 60, replace=False)
            subsets = [subsets[i] for i in idx]
        for a in range(len(subsets)):
            for b in range(a + 1, len(subsets)):
                A = T[:, list(subsets[a])]
                Bm = T[:, list(subsets[b])]
                QA, _ = np.linalg.qr(A)
                QB, _ = np.linalg.qr(Bm)
                # orthonormal bases of the two flats
                rA = np.linalg.matrix_rank(A); rB = np.linalg.matrix_rank(Bm)
                QA = QA[:, :rA]; QB = QB[:, :rB]
                ang = principal_angles(QA, QB)
                pos = ang[ang > 1e-7]  # smallest positive principal angle
                if pos.size == 0:
                    continue
                theta = pos.min()
                sintheta = np.sin(theta)
                bound = dT / r
                checked += 1
                slack = sintheta / bound if bound > 0 else np.inf
                worst_slack = min(worst_slack, slack)
                if sintheta < bound - 1e-7:
                    viol += 1
    return {"pairs_checked": int(checked), "worst_ratio_sin_over_bound": round(float(worst_slack), 4),
            "violations": int(viol), "note": "ratio>=1 means sinθ>=δ_T/r holds"}


# ---------- D. circuit imbalance vs 1/δ_A ----------
def circuit_imbalance(A, tol=1e-7):
    """κ_A = max over circuits (minimal dependent column sets) of max_{i,j in supp}|g_i/g_j|,
    g = kernel vector of the circuit. Returns (kappa, n_circuits). Enumerative; small n only."""
    d, n = A.shape
    r = np.linalg.matrix_rank(A)
    kappa = 1.0
    n_circ = 0
    # a circuit has size s with 2<=s<=r+1; columns dependent but every proper subset independent
    for s in range(2, r + 2):
        for combo in itertools.combinations(range(n), s):
            M = A[:, combo]
            if np.linalg.matrix_rank(M, tol=tol) == s:
                continue  # independent, not dependent
            # minimal? every (s-1)-subset independent
            minimal = all(np.linalg.matrix_rank(A[:, list(cc)], tol=tol) == s - 1
                          for cc in itertools.combinations(combo, s - 1))
            if not minimal:
                continue
            # kernel vector
            _, sv, Vt = np.linalg.svd(M)
            g = Vt[-1]
            supp = np.abs(g) > tol
            if supp.sum() < 2:
                continue
            vals = np.abs(g[supp])
            kappa = max(kappa, vals.max() / vals.min())
            n_circ += 1
    return kappa, n_circ

def check_D():
    out = []
    # unit-column matrices WITH dependencies (so circuits exist)
    cases = []
    cases.append(("dep_pairs(d=4,k=2)", S1.family_dependent_pairs(4, 2)))
    cases.append(("dep_pairs(d=6,k=3)", S1.family_dependent_pairs(6, 3)))
    # random overcomplete unit vectors
    for (d, n) in [(3, 5), (4, 6), (4, 7), (5, 7)]:
        M = S1.normalize_cols(rng.standard_normal((d, n)))
        cases.append((f"rand_unit(d={d},n={n})", M))
    # a near-dependent triple to stress the bound
    eps = 0.3
    M = np.column_stack([np.array([1, 0, 0]), np.array([0, 1, 0]),
                         S1.normalize_cols((np.array([1.0, 1.0, eps]))[:, None])[:, 0]])
    cases.append(("near_dep_triple", M))
    worst_violation = None
    for name, A in cases:
        try:
            dA = S1.delta_T(A)
        except Exception:
            dA = float("nan")
        kappa, ncirc = circuit_imbalance(A)
        bound = 1.0 / dA if dA > 0 else np.inf
        holds = kappa <= bound + 1e-6
        out.append({"name": name, "delta_A": round(float(dA), 4), "kappa_A": round(float(kappa), 4),
                    "1/delta_A": round(float(bound), 4), "circuits": int(ncirc),
                    "kappa<=1/delta_A": bool(holds)})
        if not holds:
            worst_violation = name
    return {"cases": out, "any_violation": worst_violation}


# ---------- E. static B/δ counterexample ----------
def check_E(delta=0.25, B=10.0):
    e1 = np.array([1.0, 0.0]);
    t = np.array([np.sqrt(1 - delta**2), delta])
    x = B * e1 - (np.sqrt(1 - delta**2) / delta) * B * np.array([0.0, 1.0])
    PJx = abs(x[0])  # projection onto span(e1)
    ip = t @ x
    normx = np.linalg.norm(x)  # = ‖P_{J+⟨t⟩}x‖ since both span R^2
    return {"||P_J x||": round(float(PJx), 4), "<t,x>": round(float(ip), 6),
            "||P_{J+<t>}x||": round(float(normx), 4), "B/delta": round(B / delta, 4),
            "VERDICT": "static additive switch lemma FALSE" if normx > PJx + 1.0 else "no jump"}


def run():
    theta = np.arcsin(0.25)
    families = [
        ("gadgets(dim=6)", S1.family_orthogonal_gadgets(3, theta)),
        ("rand_indep(d=6)", S1.family_random_independent(6, 6, 0.25)),
        ("dep_pairs(d=6,k=2)", S1.family_dependent_pairs(6, 2)),
    ]
    families = [(n, T) for n, T in families if T is not None]

    print("=== Round-1 audit numeric checks ===\n")
    A = check_A(); print("A (unit-WLOG false):", A, "\n")
    B = check_B(families); print("B (refined P2):", B, "\n")
    C = check_C(families); print("C (principal-angle lemma):", C, "\n")
    D = check_D()
    print("D (kappa_A <= 1/delta_A for unit columns):")
    for row in D["cases"]:
        print("   ", row)
    print("   any_violation:", D["any_violation"], "\n")
    E = check_E(); print("E (static B/delta counterexample):", E, "\n")

    import json
    with open(os.path.join(_HERE, "round1_audit_results.json"), "w") as f:
        json.dump({"A": A, "B": B, "C": C, "D": D, "E": E}, f, indent=2)
    print("Frozen -> code/round1_audit_results.json")


if __name__ == "__main__":
    run()
