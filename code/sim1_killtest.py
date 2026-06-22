"""
Sim 1 — the KILL TEST for `greedy-vector-balancing-polyupper` (Phase 0, guide ��Evaluation).

ADVERSARIAL INPUT ONLY. A clean plot on random T is NOT evidence; we search for the worst T and the
worst arrival sequence and report the adversarial MAXIMUM (not the mean).

Model (anchor arXiv:2606.17991, Theorem 1.2, full-text confirmed 2026-06-21):
  finite T subset of the unit sphere S^{d-1}; the scaled universe is [-1,1]T = {a*t : a in [-1,1], t in T}.
  Vectors arrive adversarially (with repetition). Greedy picks sign s_k in {+-1} so that s_k*v_k has
  NON-POSITIVE inner product with S_{k-1} = sum_{i<k} s_i v_i.  G(T) = sup_k ||S_k||.

Reduction used by the adversary (derived, documented):
  For an arriving vector v = a*t (t unit, a in [-1,1]) greedy sets s = -sign(<v,S>), giving
    ||S + s v||^2 = ||S||^2 + a^2 - 2|a|*|<t,S>|.
  As a function of u=|a| in [0,1] this is convex, so its max is at an endpoint: u=0 (no change) or
  u=1 (gain 1 - 2|<t,S>|). Hence the norm-MAXIMIZING adversary only ever sends FULL unit vectors t with
  |<t,S>| < 1/2 (the "productive" set N(S) of guide P2). So WLOG the adversary plays unit vectors from T.

delta_T (anchor Definition 1.1): min over t in T, U subset of T with t not in span(U), of dist(t, span(U)).
  - If T is linearly independent, no subset U of T\{t} has t in its span, and the largest span (= span of
    all the others) gives the smallest distance, so delta_T = min_t dist(t, span(T\{t})) (fast path).
  - General case: exact enumeration over subsets (capped n).

PRE-REGISTERED (before running):
  * If the B-side is TRUE: adversarial max ||S_k|| grows POLYNOMIALLY in d at fixed delta (e.g. ~ sqrt(d)/delta,
    matching the anchor's own Omega(sqrt(d)/delta_T) lower bound; certainly << (2/delta)^{d-1}).
  * FALSIFIER (=> RED death-evidence for the exponential A-side): a constant-delta family whose adversarial
    max ||S_k|| grows CLEARLY SUPER-POLYNOMIALLY in d. A numeric adversary is decisive evidence, not a proof.

NOTE on direction of evidence: a simulation can only LOWER-bound G(T) (by exhibiting sequences). So
  "we searched hard and found only polynomial growth" is GREEN-supporting (consistent with B); it is the
  attacker's job to PROVE poly. Finding super-poly would be the RED falsifier.
"""

import itertools
import json
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20260621
rng = np.random.default_rng(SEED)

# --------------------------------------------------------------------------------------------------
# delta_T
# --------------------------------------------------------------------------------------------------

def dist_to_span(t, U):
    """Euclidean distance from unit vector t to span of columns of U (U: d x m, possibly empty)."""
    if U.shape[1] == 0:
        return np.linalg.norm(t)
    # least squares projection residual
    coef, *_ = np.linalg.lstsq(U, t, rcond=None)
    return float(np.linalg.norm(t - U @ coef))

def is_independent(T):
    return np.linalg.matrix_rank(T) == T.shape[1]

def delta_T_independent(T):
    """delta_T for linearly independent T (columns). Fast exact path."""
    d, n = T.shape
    best = np.inf
    for i in range(n):
        others = np.delete(T, i, axis=1)
        best = min(best, dist_to_span(T[:, i], others))
    return best

def delta_T_exact(T, subset_cap=13):
    """Exact delta_T by subset enumeration. Works for any T but enumerates 2^(n-1); cap n."""
    d, n = T.shape
    if n > subset_cap:
        raise ValueError(f"n={n} exceeds subset_cap={subset_cap} for exact delta_T")
    if is_independent(T):
        return delta_T_independent(T)
    best = np.inf
    idx = list(range(n))
    for i in idx:
        rest = [j for j in idx if j != i]
        t = T[:, i]
        # enumerate all subsets U of rest with t NOT in span(U); track smallest dist
        for r in range(0, len(rest) + 1):
            for combo in itertools.combinations(rest, r):
                U = T[:, list(combo)] if combo else np.zeros((d, 0))
                dd = dist_to_span(t, U)
                if dd > 1e-9:  # t not in span(U)
                    best = min(best, dd)
    return best

def delta_T(T, subset_cap=13):
    return delta_T_independent(T) if is_independent(T) else delta_T_exact(T, subset_cap)

# --------------------------------------------------------------------------------------------------
# Greedy + adversary
# --------------------------------------------------------------------------------------------------

def productive_gain(T, S):
    """For each unit column t of T, the norm^2 gain of sending full t: 1 - 2|<t,S>| (only if > 0)."""
    ips = np.abs(T.T @ S)            # |<t_i, S>|
    gains = 1.0 - 2.0 * ips
    return gains, ips

def adversary_beam(T, beam_width=48, max_steps=None, restarts=16):
    """
    Strong adversarial-arrival search. Returns the maximum ||S_k|| found.
    Combines: (1) deterministic beam search by norm, (2) stochastic random-restart rollouts.
    All sends are full unit vectors from T (justified by the convexity reduction above).
    """
    d, n = T.shape
    if max_steps is None:
        max_steps = max(40, 10 * d)

    best_norm = 0.0

    # ---- (1) beam search ----
    # state = S vector; expand by every productive direction (both signs handled by greedy rule).
    beam = [np.zeros(d)]
    for _ in range(max_steps):
        cand = []
        for S in beam:
            gains, ips = productive_gain(T, S)
            prod = np.where(gains > 1e-12)[0]
            if prod.size == 0:
                continue
            for i in prod:
                t = T[:, i]
                s = -np.sign(T[:, i] @ S) if abs(T[:, i] @ S) > 0 else 1.0
                Snew = S + s * t
                cand.append(Snew)
        if not cand:
            break
        norms = [np.linalg.norm(c) for c in cand]
        best_norm = max(best_norm, max(norms))
        # keep top beam_width distinct-ish states by norm
        order = np.argsort(norms)[::-1]
        newbeam, seen = [], []
        for o in order:
            c = cand[o]
            if any(np.linalg.norm(c - x) < 1e-6 for x in seen):
                continue
            seen.append(c)
            newbeam.append(c)
            if len(newbeam) >= beam_width:
                break
        beam = newbeam

    # ---- (2) stochastic random-restart rollouts (escape beam's myopia/cycles) ----
    for _ in range(restarts):
        S = np.zeros(d)
        local_best = 0.0
        for _ in range(max_steps):
            gains, ips = productive_gain(T, S)
            prod = np.where(gains > 1e-12)[0]
            if prod.size == 0:
                break
            # stochastic: weight by gain^2 to favor big steps but allow exploration
            w = gains[prod] ** 2
            w = w / w.sum()
            i = prod[rng.choice(len(prod), p=w)]
            t = T[:, i]
            s = -np.sign(t @ S) if abs(t @ S) > 0 else 1.0
            S = S + s * t
            local_best = max(local_best, np.linalg.norm(S))
        best_norm = max(best_norm, local_best)

    return best_norm

# --------------------------------------------------------------------------------------------------
# T families (adversarial constructions)
# --------------------------------------------------------------------------------------------------

def normalize_cols(M):
    return M / np.linalg.norm(M, axis=0, keepdims=True)

def family_orthogonal_gadgets(d_pairs, theta):
    """Anchor-style lower-bound construction: d_pairs near-parallel pairs in mutually orthogonal 2-planes.
    Dimension = 2*d_pairs. Each pair: e_{2j}, cos(theta) e_{2j} + sin(theta) e_{2j+1}. delta = sin(theta)."""
    d = 2 * d_pairs
    cols = []
    for j in range(d_pairs):
        a = np.zeros(d); a[2*j] = 1.0
        b = np.zeros(d); b[2*j] = np.cos(theta); b[2*j+1] = np.sin(theta)
        cols.append(a); cols.append(b)
    return np.array(cols).T

def family_random_independent(d, n, delta_min, tries=4000):
    """Random independent T (n<=d) with delta_T >= delta_min by rejection."""
    best = None
    for _ in range(tries):
        M = normalize_cols(rng.standard_normal((d, n)))
        if np.linalg.matrix_rank(M) < n:
            continue
        if delta_T_independent(M) >= delta_min:
            return M
        if best is None:
            best = M
    return best  # may be None / sub-threshold; caller checks

def family_dependent_pairs(d, k):
    """Deterministic 'exact-dependency danger zone' (fact-1 probe): orthonormal basis e_1..e_d PLUS
    k extra vectors (e_{2i-1}+e_{2i})/sqrt(2). Each extra lies in the span of two basis vectors, so the
    set has GENUINE exact dependencies (n=d+k > d, rank d), yet delta_T stays ~1/sqrt(2) >> 1/4 — i.e.
    constant delta WITH exact dependencies, exactly the regime fact-1 says cannot chain-amplify.
    n = d + k (kept small so exact delta_T enumeration is cheap)."""
    cols = [np.eye(d)[:, i] for i in range(d)]
    for i in range(k):
        a, b = 2 * i, 2 * i + 1
        if b >= d:
            break
        v = (np.eye(d)[:, a] + np.eye(d)[:, b]) / np.sqrt(2.0)
        cols.append(v)
    return np.array(cols).T

def family_near_dependency_chain(d, gap):
    """Klee-Minty-flavored probe of fact-1: a chain of vectors each slightly tilted off the previous
    span. Tilt 'gap' controls delta_T. Tests whether near-dependencies can chain-amplify (fact-1 says no)."""
    cols = [np.eye(d)[:, 0]]
    for k in range(1, d):
        v = np.zeros(d)
        v[k] = gap
        v[:k] = np.sqrt(1 - gap**2) / np.sqrt(k)  # spread mass on previous coords
        cols.append(v / np.linalg.norm(v))
    return normalize_cols(np.array(cols).T)

# --------------------------------------------------------------------------------------------------
# Main experiment
# --------------------------------------------------------------------------------------------------

def local_optimize_T(T, delta_min, iters=12, step=0.15):
    """Hill-climb: perturb columns to increase adversarial max-norm while keeping delta_T >= delta_min.
    Independent-T path only (fast delta_T). Light search inside the loop; one full eval at the end."""
    d, n = T.shape
    best_T = T.copy()
    best_val = adversary_beam(best_T, beam_width=24, restarts=6)
    for _ in range(iters):
        cand = best_T + step * rng.standard_normal((d, n))
        cand = normalize_cols(cand)
        if np.linalg.matrix_rank(cand) < n:
            continue
        if delta_T_independent(cand) < delta_min:
            continue
        val = adversary_beam(cand, beam_width=24, restarts=6)
        if val > best_val:
            best_val, best_T = val, cand
    return best_T, adversary_beam(best_T)

def run():
    DELTA = 0.25  # constant delta = 1/4 (guide c = 1/4)
    results = {"seed": SEED, "delta": DELTA, "per_d": []}
    print(f"=== Sim 1 kill test ===  seed={SEED}  delta>={DELTA}\n")
    print(f"{'d':>3} {'best_maxnorm':>13} {'sqrt(d)/delta':>13} {'(2/delta)^(d-1)':>16}  winner")

    # theta for the orthogonal-gadget family so that sin(theta) ~ delta
    theta = np.arcsin(DELTA)

    for d in range(2, 11):
        candidates = {}

        # (a) anchor-style orthogonal gadgets in dimension d (use d_pairs = d//2)
        if d >= 2:
            dp = max(1, d // 2)
            Tg = family_orthogonal_gadgets(dp, theta)
            candidates[f"gadgets(dp={dp},dim={2*dp})"] = Tg

        # (b) random independent, n=d
        Tind = family_random_independent(d, d, DELTA)
        if Tind is not None and is_independent(Tind) and delta_T_independent(Tind) >= DELTA:
            # local optimize
            Topt, _ = local_optimize_T(Tind, DELTA)
            candidates[f"rand_indep(n={d})+opt"] = Topt

        # (c) deterministic dependent family (exact-dependency danger zone, fact-1 probe)
        kpairs = min(2, d // 2)
        if kpairs >= 1:
            Tdep = family_dependent_pairs(d, kpairs)
            candidates[f"dep_pairs(k={kpairs},n={d+kpairs})"] = Tdep

        # (d) near-dependency chain
        Tchain = family_near_dependency_chain(d, DELTA)
        if delta_T_independent(Tchain) >= DELTA - 1e-6:
            candidates[f"near_dep_chain"] = Tchain

        best_val, best_name, best_delta = 0.0, None, None
        per_fam = {}
        for name, T in candidates.items():
            try:
                dt = delta_T(T)
            except Exception:
                dt = float("nan")
            val = adversary_beam(T)
            per_fam[name] = {"maxnorm": round(val, 4), "delta_T": round(float(dt), 4),
                             "dim": T.shape[0], "n": T.shape[1]}
            if val > best_val:
                best_val, best_name, best_delta = val, name, dt

        sqrtd = np.sqrt(d) / DELTA
        expo = (2.0 / DELTA) ** (d - 1)
        print(f"{d:>3} {best_val:>13.4f} {sqrtd:>13.4f} {expo:>16.1f}  {best_name} (dT={best_delta:.3f})")
        results["per_d"].append({"d": d, "best_maxnorm": round(best_val, 4),
                                 "sqrt_d_over_delta": round(sqrtd, 4),
                                 "exp_bound": round(expo, 2),
                                 "winner": best_name, "families": per_fam})

    # growth diagnostic: fit log(maxnorm) vs log(d) (poly slope) and vs d (exp slope)
    ds = np.array([r["d"] for r in results["per_d"]], float)
    ys = np.array([max(r["best_maxnorm"], 1e-9) for r in results["per_d"]], float)
    poly_slope = np.polyfit(np.log(ds), np.log(ys), 1)[0]      # log y ~ slope*log d  => y ~ d^slope
    exp_slope = np.polyfit(ds, np.log(ys), 1)[0]               # log y ~ slope*d       => y ~ e^{slope d}
    results["fit"] = {"poly_loglog_slope": round(float(poly_slope), 4),
                      "exp_semilog_slope": round(float(exp_slope), 4)}
    print(f"\nGrowth fit:  log-log slope (poly exponent) = {poly_slope:.3f}"
          f"   |   semilog slope (exp rate) = {exp_slope:.3f}")
    print("Interpretation: poly exponent small & stable => polynomial (B-side consistent);"
          " a growing/large exp rate with poor poly fit => super-poly (RED falsifier).")

    with open(os.path.join(_HERE, "sim1_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\nFrozen -> code/sim1_results.json")
    return results

if __name__ == "__main__":
    run()
