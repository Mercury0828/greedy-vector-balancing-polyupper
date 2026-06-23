"""
Round-10 numeric — probe the PINNED hard region of BST (Round-10 solvers). Fixed seed; scipy.

Checks:
  HAD.   BST adversary on the signed Sylvester-Hadamard family G_r=I+(H_r-D_r)/(4√r) (well-conditioned,
         constant δ, but comparison-stable fails by Θ(√r)) — the concrete OPEN test. sup‖p‖ vs r=4..64.
  PCT.   Adversarially MINIMIZE the cycle-gap γ(R)=1−‖P_{i_m}…P_{i_1}‖² over full words (all coords) on the
         Hadamard family + random well-conditioned bases. If γ can be driven super-poly small at constant δ
         ⟹ (via the palindrome mechanism) a BST REFUTATION lead; if γ ≥ ~poly^{-1} ⟹ supports BST.
  THM1.  Comparison-stable sanity: diagonally-dominant G, sup‖p‖ ≤ r/η.
  THM2.  Equicorrelation G_α: c^T G c ≤ 2r³/δ²+r².
"""
import json
import os
import numpy as np
from scipy.linalg import hadamard

import round9_bst_killtest as R9

rng = np.random.default_rng(20260623)
_HERE = os.path.dirname(os.path.abspath(__file__))


def hadamard_G(m):
    r = 2 ** m
    H = hadamard(r).astype(float)
    G = np.eye(r) + (H - np.diag(np.diag(H))) / (4 * np.sqrt(r))
    return G, r


def delta_of_G(G):
    return 1.0 / np.sqrt(np.max(np.diag(np.linalg.inv(G))))


def check_hadamard():
    rows = []
    print("=== BST on signed-Hadamard family (well-conditioned, comparison fails Θ(√r)) ===")
    print(f"{'r':>4} {'lam_min':>8} {'delta':>7} {'rho|G-I|':>9} {'sup||p||':>9} {'r/δ':>8} {'r^2/δ^2':>10}")
    for m in [2, 3, 4, 5, 6]:
        G, r = hadamard_G(m)
        lam = float(np.linalg.eigvalsh(G)[0])
        delta = delta_of_G(G)
        rho = float(np.max(np.abs(np.linalg.eigvals(np.abs(G - np.eye(r))))))
        sup = R9.bst_adversary(G, beam_width=40, restarts=20)
        rows.append({"r": r, "lam_min": round(lam, 4), "delta": round(float(delta), 4),
                     "rho_absGmI": round(rho, 3), "sup_norm": round(float(sup), 3),
                     "r_over_delta": round(r/delta, 2), "r2_over_d2": round(r**2/delta**2, 1)})
        print(f"{r:>4} {lam:>8.4f} {delta:>7.4f} {rho:>9.3f} {sup:>9.3f} {r/delta:>8.2f} {r**2/delta**2:>10.1f}")
    ds = np.array([x["r"] for x in rows], float)
    ys = np.array([max(x["sup_norm"], 1e-9) for x in rows], float)
    slope = float(np.polyfit(np.log(ds), np.log(ys), 1)[0])
    print(f"   log-log(r) slope = {slope:.3f}  (sub-linear/√r ⟹ BST-consistent on the hard family)")
    return {"rows": rows, "loglog_slope": round(slope, 3)}


def pct_min_gap(G, extra=2):
    """Adversarially MINIMIZE γ(R)=1−‖R‖² over a full word: keep the product near-isometric by, at each step,
    projecting along the t_i least aligned with the current top right-singular vector. Returns γ."""
    r = G.shape[0]
    A = np.linalg.cholesky(G).T  # columns = t_i (G=A^T A)... use A with A^T A = G
    # ensure unit columns: cholesky of G gives upper R with R^T R=G; columns of R are NOT the t_i.
    # Build t_i explicitly: any A with A^T A=G; use A = chol(G)^T (lower). Columns have norm sqrt(G_ii)=1.
    L = np.linalg.cholesky(G)  # G = L L^T ; then t_i = L[:,i]? (L L^T)_{ij}=<L_i row...>. Use A=L^T: A^T A=L L^T=G
    A = L.T
    t = [A[:, i] / np.linalg.norm(A[:, i]) for i in range(r)]
    M = np.eye(r)
    used = set()
    word = []
    steps = r + extra * r
    for _ in range(steps):
        # top right-singular vector of M
        U, s, Vt = np.linalg.svd(M)
        w = Vt[0]
        # pick coord least aligned with w (least contraction of the top direction), prefer unused to cover all
        scores = [abs(t[i] @ w) for i in range(r)]
        order = sorted(range(r), key=lambda i: (i in used, scores[i]))  # unused first, then small alignment
        i = order[0]
        Pi = np.eye(r) - np.outer(t[i], t[i])
        M = Pi @ M
        used.add(i); word.append(i)
        if len(used) == r and len(word) >= r:
            break
    # extend a bit more greedily to try to raise ‖M‖
    for _ in range(2 * r):
        U, s, Vt = np.linalg.svd(M)
        w = Vt[0]
        i = min(range(r), key=lambda i: abs(t[i] @ w))
        M = (np.eye(r) - np.outer(t[i], t[i])) @ M
    gamma = 1.0 - float(np.linalg.svd(M, compute_uv=False)[0])**2
    return gamma


def check_pct():
    out = []
    print("\n=== PCT cycle-gap γ=1−‖R‖² (adversarially MINIMIZED); γ ≥ poly^{-1} supports BST ===")
    for m in [2, 3, 4, 5]:
        G, r = hadamard_G(m)
        delta = delta_of_G(G)
        g = pct_min_gap(G)
        out.append({"family": "hadamard", "r": r, "delta": round(float(delta), 4),
                    "min_gamma": float(f"{g:.3e}"), "perm_lb_d2/r3": float(f"{delta**2/r**3:.3e}")})
        print(f"   hadamard r={r}: min γ={g:.3e}   permutation LB δ²/r³={delta**2/r**3:.3e}")
    for r in [4, 6, 8, 12]:
        G, d = R9.well_conditioned_basis(r, 0.25)
        if G is None:
            continue
        delta = delta_of_G(G)
        g = pct_min_gap(G)
        out.append({"family": "random", "r": r, "delta": round(float(delta), 4),
                    "min_gamma": float(f"{g:.3e}"), "perm_lb_d2/r3": float(f"{delta**2/r**3:.3e}")})
        print(f"   random  r={r}: min γ={g:.3e}   permutation LB δ²/r³={delta**2/r**3:.3e}")
    return out


def check_thm1_thm2():
    # Thm1: diagonally dominant G (comparison-stable)
    r = 8
    M = rng.standard_normal((r, r)) * 0.05
    B = np.abs(M); np.fill_diagonal(B, 0)
    # scale so row sums < 1
    rs = B.sum(axis=1).max()
    if rs > 0:
        B *= 0.5 / rs
    G = np.eye(r) + (B + B.T) / 2 * 0  # build PD comparison-stable G directly:
    Off = (M + M.T) / 2; np.fill_diagonal(Off, 0)
    Off *= 0.4 / max(np.abs(Off).sum(axis=1).max(), 1e-9)
    G = np.eye(r) + Off
    G = (G + G.T) / 2
    if np.linalg.eigvalsh(G)[0] <= 0:
        G = np.eye(r) + Off * 0.3
    Babs = np.abs(G - np.eye(r))
    eta = 1 - np.max(np.abs(np.linalg.eigvals(Babs)))
    sup = R9.bst_adversary(G)
    thm1 = {"r": r, "eta": round(float(eta), 4), "sup_norm": round(float(sup), 3),
            "bound_r/eta": round(r/eta, 2), "ok": bool(sup <= r/eta + 1e-3)}
    # Thm2: equicorrelation
    r2 = 8; alpha = 0.3
    Ga = (1 - alpha) * np.eye(r2) + alpha * np.ones((r2, r2))
    delta2 = delta_of_G(Ga)
    sup2 = R9.bst_adversary(Ga)
    bound2 = 2 * r2**3 / delta2**2 + r2**2
    thm2 = {"r": r2, "alpha": alpha, "delta": round(float(delta2), 4), "sup_E": round(float(sup2**2), 2),
            "bound_2r3/d2+r2": round(float(bound2), 1), "ok": bool(sup2**2 <= bound2 + 1e-3)}
    return {"THM1": thm1, "THM2": thm2}


def run():
    print("=== Round-10 numeric: pinned hard region (Hadamard / PCT) + Thm1/Thm2 sanity ===\n")
    HAD = check_hadamard()
    PCT = check_pct()
    TH = check_thm1_thm2()
    print("\nTHM1 (comparison-stable):", TH["THM1"])
    print("THM2 (equicorrelation):", TH["THM2"])
    with open(os.path.join(_HERE, "round10_results.json"), "w") as f:
        json.dump({"hadamard_BST": HAD, "PCT_min_gap": PCT, "theorems": TH}, f, indent=2,
                  default=lambda o: bool(o) if isinstance(o, np.bool_) else float(o) if isinstance(o, np.floating) else str(o))
    print("\nFrozen -> code/round10_results.json")


if __name__ == "__main__":
    run()
