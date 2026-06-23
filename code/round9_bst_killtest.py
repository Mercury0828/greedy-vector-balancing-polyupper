"""
Round-9 — BST KILL TEST (the cleanest direct probe of (★), from the FINAL fresh-context round).

Response 2 reduced the whole open core to the BASIS level: for a well-conditioned basis T={t_1..t_r},
G=A^T A (A=[t_i], unit columns), with (G^{-1})_{ii} ≤ δ^{-2}, the adversarial coordinate-descent orbit
  c_{k+1} = c_k + (ε_k − (G c_k)_{i_k}) e_{i_k},  ε_k∈{±1}
has energy  E_k = c_k^T G c_k = ‖A c_k‖² = ‖p_k‖²  with the update  E_{k+1} = E_k + 1 − (G c_k)_{i_k}²  (eq 6).
**Basis Switching Theorem (BST):** sup_k E_k ≤ poly(r, 1/δ).  (★) holds iff BST holds (this IS the core).

This is a clean r×r dynamical system — we can attack it adversarially to LARGE r (unlike the chamber sims).
PRE-REGISTERED:
  * BST/(★) TRUE  ⟹  sup_k ‖p_k‖ = sqrt(sup E) grows POLYNOMIALLY in r at fixed δ.
  * REFUTATION    ⟹  a constant-δ well-conditioned basis with sup_k ‖p_k‖ super-polynomial in r
                     (would refute (★): the truth is the exponential side).
Adversary: pick the coordinate with smallest |(Gc)_i| (max energy gain 1−(Gc)_i²) + a sign-lookahead;
beam search + stochastic restarts. We report the adversarial MAXIMUM.

Also: verify the NEW root-system/graphical theorem (Response 1 / §6): the dispersion potential D(x)=Σ_{i<j}
|x_i−x_j| drops by ≥ ‖step‖·√2 per edge-projection ⟹ TV ≤ (n choose 2)·‖x_0‖.
"""
import json
import os
import numpy as np

rng = np.random.default_rng(20260623)
_HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------- BST setup ----------------
def well_conditioned_basis(r, delta_min, tries=3000):
    """Return G=A^T A for r unit vectors with δ = min_i 1/sqrt((G^{-1})_{ii}) ≥ delta_min, else best."""
    best_G, best_delta = None, -1.0
    for _ in range(tries):
        A = rng.standard_normal((r, r))
        A /= np.linalg.norm(A, axis=0, keepdims=True)
        if np.linalg.matrix_rank(A) < r:
            continue
        G = A.T @ A
        try:
            Ginv = np.linalg.inv(G)
        except np.linalg.LinAlgError:
            continue
        delta = 1.0 / np.sqrt(np.max(np.diag(Ginv)))
        if delta > best_delta:
            best_delta, best_G = delta, G
        if delta >= delta_min:
            return G, delta
    return best_G, best_delta


def bst_adversary(G, beam_width=40, restarts=24, max_steps=None):
    """Maximize sup_k c^T G c over adversarial (i_k, ε_k). Returns sqrt(sup E) = sup ‖p_k‖."""
    r = G.shape[0]
    if max_steps is None:
        max_steps = max(60, 30 * r)
    best_E = 0.0

    def step(c, i, eps):
        gc_i = (G @ c)[i]
        c2 = c.copy()
        c2[i] += (eps - gc_i)
        return c2

    # ---- beam search over states c, scored by energy; expand by productive coords & both signs ----
    beam = [np.zeros(r)]
    for _ in range(max_steps):
        cand = []
        for c in beam:
            gc = G @ c
            gain = 1.0 - gc**2          # energy gain if we pick coord i
            prod = np.where(gain > 1e-12)[0]
            if prod.size == 0:
                continue
            order = prod[np.argsort(-gain[prod])][:6]   # top productive coords
            for i in order:
                for eps in (+1.0, -1.0):
                    cand.append(step(c, i, eps))
        if not cand:
            break
        Es = [float(c @ (G @ c)) for c in cand]
        best_E = max(best_E, max(Es))
        idx = np.argsort(Es)[::-1]
        newbeam, seen = [], []
        for j in idx:
            cc = cand[j]
            if any(np.linalg.norm(cc - s) < 1e-6 for s in seen):
                continue
            seen.append(cc); newbeam.append(cc)
            if len(newbeam) >= beam_width:
                break
        beam = newbeam

    # ---- stochastic restarts ----
    for _ in range(restarts):
        c = np.zeros(r)
        for _ in range(max_steps):
            gc = G @ c
            gain = 1.0 - gc**2
            prod = np.where(gain > 1e-12)[0]
            if prod.size == 0:
                break
            w = gain[prod] / gain[prod].sum()
            i = prod[rng.choice(len(prod), p=w)]
            eps = rng.choice([-1.0, 1.0])
            c[i] += (eps - gc[i])
            best_E = max(best_E, float(c @ (G @ c)))
    return np.sqrt(best_E)


def check_bst():
    DELTA = 0.25
    rows = []
    print(f"=== BST kill test (δ≥{DELTA}); sup‖p‖ vs r ===")
    print(f"{'r':>3} {'delta':>7} {'sup||p||':>9} {'r/δ':>7} {'r^2/δ^2':>9} {'(2/δ)^(r-1)':>13}")
    for r in [4, 6, 8, 10, 14, 18, 24, 30]:
        G, delta = well_conditioned_basis(r, DELTA)
        if G is None:
            continue
        sup = bst_adversary(G)
        expo = (2.0 / delta) ** (r - 1)
        rows.append({"r": r, "delta": round(float(delta), 4), "sup_norm": round(float(sup), 3),
                     "r_over_delta": round(r/delta, 2), "r2_over_d2": round(r**2/delta**2, 1),
                     "exp_bound": expo})
        print(f"{r:>3} {delta:>7.4f} {sup:>9.3f} {r/delta:>7.2f} {r**2/delta**2:>9.1f} {expo:>13.2e}")
    ds = np.array([x["r"] for x in rows], float)
    ys = np.array([max(x["sup_norm"], 1e-9) for x in rows], float)
    poly_slope = float(np.polyfit(np.log(ds), np.log(ys), 1)[0])
    exp_slope = float(np.polyfit(ds, np.log(ys), 1)[0])
    print(f"growth: log-log(r) slope (poly exponent) = {poly_slope:.3f}   semilog(r) slope = {exp_slope:.3f}")
    verdict = ("BOUNDED/POLY in r ⟹ BST/(★)-consistent (no refutation)"
               if poly_slope < 3.0 and exp_slope < 0.25 else
               "SUPER-POLY GROWTH ⟹ possible REFUTATION, INVESTIGATE")
    print("VERDICT:", verdict)
    return {"rows": rows, "loglog_poly_slope": round(poly_slope, 3),
            "semilog_exp_slope": round(exp_slope, 3), "verdict": verdict}


# ---------------- root-system / graphical theorem check ----------------
def graphical_T(edges, n):
    cols = []
    for (u, v) in edges:
        e = np.zeros(n); e[u] = 1; e[v] = -1
        cols.append(e / np.sqrt(2))
    return np.array(cols).T  # n x |E|


def check_graphical():
    out = []
    graphs = {
        "path6": ([(i, i+1) for i in range(5)], 6),
        "cycle6": ([(i, (i+1) % 6) for i in range(6)], 6),
        "complete5": ([(i, j) for i in range(5) for j in range(i+1, 5)], 5),
    }
    for name, (edges, n) in graphs.items():
        T = graphical_T(edges, n)
        m = T.shape[1]
        worst_ratio = 0.0
        for _ in range(200):
            y = rng.standard_normal(n); y -= y.mean()  # in 1^perp
            y0n = np.linalg.norm(y)
            tv = 0.0
            D = lambda z: sum(abs(z[i]-z[j]) for i in range(n) for j in range(i+1, n))
            D0 = D(y)
            for _ in range(40 * m):
                # adversary: pick edge with largest |x_u - x_v|
                ips = np.abs(T.T @ y)
                if ips.max() < 1e-9:
                    break
                k = int(np.argmax(ips))
                step = ips[k]
                y = y - (T[:, k] @ y) * T[:, k]
                tv += step
            ratio = tv / y0n
            worst_ratio = max(worst_ratio, ratio)
        bound = n*(n-1)/2
        out.append({"graph": name, "n": n, "edges": m, "worst_TV/||y0||": round(float(worst_ratio), 3),
                    "C(n,2)_bound": bound, "ok(<=)": worst_ratio <= bound + 1e-6})
    return out


def run():
    print("=== Round-9 numeric: BST kill-test + root-system theorem ===\n")
    BST = check_bst()
    print("\nGraphical/root-system theorem (TV ≤ C(n,2)·‖y0‖):")
    GR = check_graphical()
    for row in GR:
        print("   ", row)
    with open(os.path.join(_HERE, "round9_results.json"), "w") as f:
        json.dump({"BST": BST, "graphical": GR}, f, indent=2, default=lambda o: bool(o) if isinstance(o, np.bool_) else str(o))
    print("\nFrozen -> code/round9_results.json")


if __name__ == "__main__":
    run()
