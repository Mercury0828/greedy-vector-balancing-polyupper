"""
Round-10 DECISIVE test (auditor's flagged open quantity): can DEFICIENT-block full words drive the PCT
cycle-gap γ(R)=1−‖P_{i_m}…P_{i_1}‖² super-polynomially small on the well-conditioned hard family?

Per the palindrome reduction: a constant-δ family with γ → r^{-ω(1)} ⟹ explicit BST (hence (★)) COUNTEREXAMPLE
(orbit² ≈ 2/γ). Per Answer-1 §5 the danger is specifically DEFICIENT blocks (repeated/subset coords before the
last missing coordinate). So: strong adversary that MAXIMIZES ‖R‖ (minimizes γ) over full words, allowed to be
long/deficient — on the signed-Hadamard family (the pinned hard region) + random well-conditioned bases.

PRE-REGISTERED:
  * γ stays ≥ ~1/poly(r) at constant δ ⟹ no refutation; BST essentially confirmed on the hard region.
  * γ → super-poly small ⟹ explicit BST/(★) COUNTEREXAMPLE (pivot to the exponential A-side).
Adversary: beam search maximizing σ_max of the running projection product (defer the damaging coords; pile up
the near-orthogonal ones), then force-complete coverage of all coords with the least-damaging order.
"""
import json
import os
import numpy as np
from scipy.linalg import hadamard

import round9_bst_killtest as R9

rng = np.random.default_rng(20260623)
_HERE = os.path.dirname(os.path.abspath(__file__))


def top_sv(M):
    """Robust top singular value + right singular vector via eigh(M^T M) (avoids SVD non-convergence)."""
    w, V = np.linalg.eigh(M.T @ M)
    lam = max(w[-1], 0.0)
    return np.sqrt(lam), V[:, -1]


def vectors_of_G(G):
    L = np.linalg.cholesky(G)
    A = L.T
    r = G.shape[0]
    return [A[:, i] / np.linalg.norm(A[:, i]) for i in range(r)]


def min_gamma_deficient(t, beam_width=24, horizon=None):
    """Maximize σ_max(R) over full words (allowing deficiency), beam search; force-complete coverage."""
    r = len(t)
    if horizon is None:
        horizon = 6 * r
    P = [np.eye(r) - np.outer(t[i], t[i]) for i in range(r)]
    # state: (M, frozenset(used)); score σ_max(M). start at identity.
    beam = [(np.eye(r), frozenset())]
    best_full = 0.0   # best σ_max among states that cover all coords (after completion)

    def complete(M, used):
        """apply missing coords in least-damaging order; return σ_max of the completed product."""
        M2 = M.copy(); u = set(used)
        while len(u) < r:
            # top right-singular vector
            _sv, w = top_sv(M2)
            missing = [i for i in range(r) if i not in u]
            i = min(missing, key=lambda i: abs(t[i] @ w))
            M2 = P[i] @ M2
            u.add(i)
        return float(top_sv(M2)[0])

    for _ in range(horizon):
        # evaluate completion of current beam
        for M, used in beam:
            best_full = max(best_full, complete(M, used))
        cand = []
        for M, used in beam:
            _sv, w = top_sv(M)
            # expand by the coords least aligned with w (defer damage) + a couple aligned (to make progress)
            order = sorted(range(r), key=lambda i: abs(t[i] @ w))
            for i in order[:8]:
                cand.append((P[i] @ M, used | {i}))
        if not cand:
            break
        cand.sort(key=lambda s: -float(top_sv(s[0])[0]))
        # dedup-ish by σ_max + used
        newbeam, seen = [], []
        for M, used in cand:
            key = (round(float(top_sv(M)[0]), 6), used)
            if key in seen:
                continue
            seen.append(key); newbeam.append((M, used))
            if len(newbeam) >= beam_width:
                break
        beam = newbeam
    return 1.0 - best_full**2


def hadamard_G(m):
    r = 2 ** m
    H = hadamard(r).astype(float)
    return np.eye(r) + (H - np.diag(np.diag(H))) / (4 * np.sqrt(r)), r


def delta_of_G(G):
    return 1.0 / np.sqrt(np.max(np.diag(np.linalg.inv(G))))


def run():
    print("=== DEFICIENT-block PCT cycle-gap γ (adversarially minimized) — the decisive refutation test ===\n")
    rows = []
    print("signed-Hadamard family (pinned hard region):")
    for m in [2, 3, 4, 5]:
        G, r = hadamard_G(m)
        delta = delta_of_G(G)
        t = vectors_of_G(G)
        g = min_gamma_deficient(t)
        polylb = delta**2 / r**3
        rows.append({"family": "hadamard", "r": r, "delta": round(float(delta), 4),
                     "min_gamma_deficient": float(f"{g:.4e}"), "perm_LB_d2/r3": float(f"{polylb:.2e}"),
                     "1/r^2": float(f"{1/r**2:.2e}")})
        print(f"   r={r:>2} δ={delta:.3f}: min γ(deficient)={g:.4e}   (perm LB δ²/r³={polylb:.2e}, 1/r²={1/r**2:.2e})")
    print("\nrandom well-conditioned bases (δ≥0.25):")
    for r in [4, 6, 8, 10]:
        G, _ = R9.well_conditioned_basis(r, 0.25)
        if G is None:
            continue
        delta = delta_of_G(G)
        t = vectors_of_G(G)
        g = min_gamma_deficient(t)
        rows.append({"family": "random", "r": r, "delta": round(float(delta), 4),
                     "min_gamma_deficient": float(f"{g:.4e}"), "perm_LB_d2/r3": float(f"{delta**2/r**3:.2e}"),
                     "1/r^2": float(f"{1/r**2:.2e}")})
        print(f"   r={r:>2} δ={delta:.3f}: min γ(deficient)={g:.4e}   (perm LB δ²/r³={delta**2/r**3:.2e}, 1/r²={1/r**2:.2e})")

    gammas = [x["min_gamma_deficient"] for x in rows]
    rs = [x["r"] for x in rows]
    # does γ decay polynomially (≥1/poly) or collapse? fit log γ vs log r on hadamard
    had = [(x["r"], x["min_gamma_deficient"]) for x in rows if x["family"] == "hadamard"]
    slope = float(np.polyfit(np.log([h[0] for h in had]), np.log([h[1] for h in had]), 1)[0]) if len(had) >= 2 else 0.0
    verdict = ("γ stays ≥ ~1/poly (no super-poly collapse) ⟹ NO refutation; BST supported on the hard region"
               if min(gammas) > 1e-3 and slope > -4 else
               "γ COLLAPSING ⟹ possible BST/(★) COUNTEREXAMPLE — INVESTIGATE")
    print(f"\nHadamard log-log(γ vs r) slope = {slope:.3f}   min γ overall = {min(gammas):.4e}")
    print("VERDICT:", verdict)
    with open(os.path.join(_HERE, "round10_deficient_results.json"), "w") as f:
        json.dump({"rows": rows, "hadamard_loglog_slope": round(slope, 3), "min_gamma": min(gammas),
                   "verdict": verdict}, f, indent=2)
    print("Frozen -> code/round10_deficient_results.json")


if __name__ == "__main__":
    run()
