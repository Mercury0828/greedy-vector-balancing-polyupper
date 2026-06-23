"""
AUDITOR decisive test: across ALL K-confined face-words (mixed), is the implication
    slope_on_L == 1   ==>   a_B = P_L b_B == 0
TRUE?  If yes, the "no-accumulation" conclusion HOLDS even though the linear part is NOT
always P_{K^perp} (the solver's stated reason is WRONG, but the CONCLUSION survives via:
slope=1 forces zero L-translation; slope<1 gives geometric absorption).

Also: when slope in (0,1), is 1-slope bounded below by a poly(delta) so absorbing radius
M_3/(1-slope) stays poly? Report worst (largest) slope strictly below 1 over all words.
"""
import itertools
import numpy as np

s26, s30 = np.sqrt(26), np.sqrt(30)
a = np.array([1.0, 0, 0, 0]); b = np.array([0, 1.0, 0, 0])
c = np.array([3, 1, 4, 0]) / s26; d = np.array([1, 3, -2, 4]) / s30; e = np.array([-2, 1, -3, -4]) / s30
VEC = {"a": a, "b": b, "c": c, "d": d, "e": e}
J = np.column_stack([a, b])

def proj_onto(cols):
    Q, _ = np.linalg.qr(cols); return Q @ Q.T
def proj_perp(cols): return np.eye(4) - proj_onto(cols)
def face_perp(active): return proj_perp(np.column_stack([VEC[k] for k in active]))
def q_min_norm(active):
    M = np.column_stack([VEC[k] for k in active]).T
    return M.T @ np.linalg.solve(M @ M.T, np.ones(M.shape[0]))

eL = np.array([0, 0, -0.6, -0.8])
Kfaces = [["a"],["b"],["e"],["a","b"],["a","e"],["b","e"],["a","b","e"]]

viol = 0
worst_slope_below1 = 0.0
max_aB_when_slope1 = 0.0
n_words = 0
for L_ in range(1, 6):
    for word in itertools.product(Kfaces, repeat=L_):
        n_words += 1
        Lin = np.eye(4); off = np.zeros(4)
        for active in word:
            Pp = face_perp(active); qq = q_min_norm(active)
            off = Pp @ off + qq
            Lin = Pp @ Lin
        slope = eL @ (Lin @ eL)
        aB = eL @ off
        if abs(slope - 1) < 1e-9:
            max_aB_when_slope1 = max(max_aB_when_slope1, abs(aB))
            if abs(aB) > 1e-7:
                viol += 1
                if viol <= 5:
                    print(f"VIOLATION: word={word} slope=1 but a_B={aB:+.5f}")
        elif slope < 1 - 1e-9:
            worst_slope_below1 = max(worst_slope_below1, abs(slope))

print(f"\nwords tested (len<=5): {n_words}")
print(f"max |a_B| when slope==1 : {max_aB_when_slope1:.3e}   (should be ~0)")
print(f"VIOLATIONS (slope=1 & a_B!=0): {viol}")
print(f"worst slope strictly <1 : {worst_slope_below1:.6f}   (1-it = {1-worst_slope_below1:.6f})")

print("\n=== ANALYTIC explanation check ===")
print("q_j in H_j subset K. If H_j is L-fixing (subset of J), then q_j... is q_j perp L?")
for f in [["a"],["b"],["a","b"]]:
    qq = q_min_norm(f)
    print(f"  H={f!s:10s} q_min={qq}  <q,eL>={qq@eL:+.4e}  (L-fixing => q perp L?)")
print("If H_j L-fixing => P_{H_j^perp} fixes L AND q_j perp L. So those steps add 0 to P_L b_B")
print("and fix slope. Only an L-MOVING step injects L-translation AND drops slope below 1.")
print("=> slope=1 (all steps L-fixing) FORCES a_B=0. No exact-1-slope-with-drift case exists.")
