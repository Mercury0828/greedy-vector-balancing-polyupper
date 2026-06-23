"""
AUDITOR follow-up: the decisive questions for Claim 1.

Finding so far: Q_B = P_{K^perp} ONLY when some step's active face = the FULL flat K (dim 3).
Otherwise slope on L can be exactly 1 (pure translation) or a contraction in (0,1).

Q1: Can slope be EXACTLY 1 with NONZERO translation a_B simultaneously? (=> would break absorbing)
    A face-word with slope 1 uses only L-fixing faces. Does such a word produce nonzero P_L b_B?
    b_B = sum_j (P_{H_N^perp}...P_{H_{j+1}^perp}) q_j, q_j in H_j, ||q_j||<=dimH_j/delta.
    P_L b_B = sum_j P_L(tail q_j). If all H_j fix L (L subset H_j^perp), then... compute.

Q2: If NOT every admissible excursion hits a full-K face, the slope is generally a CONTRACTION
    c<1 (per-step <1 whenever an L-moving face is used). Then absorbing radius ~ M_3/(1-c).
    What is the WORST-case (largest) per-return slope strictly below 1 achievable, and is 1-c
    bounded below by poly(delta)? If c can be 1 exactly with nonzero a_B => GAP/refutation.
"""
import itertools
import numpy as np

s26, s30 = np.sqrt(26), np.sqrt(30)
a = np.array([1.0, 0, 0, 0]); b = np.array([0, 1.0, 0, 0])
c = np.array([3, 1, 4, 0]) / s26; d = np.array([1, 3, -2, 4]) / s30; e = np.array([-2, 1, -3, -4]) / s30
VEC = {"a": a, "b": b, "c": c, "d": d, "e": e}
J = np.column_stack([a, b]); K = np.column_stack([a, b, e])

def proj_onto(cols):
    Q, _ = np.linalg.qr(cols); return Q @ Q.T
def proj_perp(cols): return np.eye(4) - proj_onto(cols)
def face_perp(active): return proj_perp(np.column_stack([VEC[k] for k in active]))

P_J = proj_onto(J)
eL = np.array([0, 0, -0.6, -0.8])  # from prior run, spans L = K cap J^perp

# K-confined faces (subsets of {a,b,e} that are linearly independent, nonempty)
Kfaces = []
for r in range(1, 4):
    for combo in itertools.combinations(["a","b","e"], r):
        Kfaces.append(list(combo))

print("K-confined faces:", Kfaces)
delta = np.sqrt(242/1875)

def q_min_norm(active):
    """affine min-norm point q_B of the face affine hull {p: signed normals . p = 1}: M^T (MM^T)^-1 1.
       Use unsigned normals (sign doesn't affect L-component magnitude bound analysis)."""
    M = np.column_stack([VEC[k] for k in active]).T  # k x 4
    G = M @ M.T
    return M.T @ np.linalg.solve(G, np.ones(M.shape[0]))

print("\n=== Q1: words with slope EXACTLY 1 on L -- is P_L b_B forced to 0? ===")
# L-fixing faces = those whose perp fixes eL i.e. eL in H^perp i.e. H subset J-side (a,b only)
Lfixing = [f for f in Kfaces if abs(eL @ (face_perp(f) @ eL) - 1) < 1e-9]
print("L-fixing K-faces (slope 1 each):", Lfixing)
# build all words length<=4 of L-fixing faces, compute P_L b_B
worst_aB = 0.0
for L_ in range(1, 5):
    for word in itertools.product(Lfixing, repeat=L_):
        Q = np.eye(4); bB = np.zeros(4)
        # b_B = sum_j tail_{>j} q_j ; iterate building affine map
        Lin = np.eye(4); off = np.zeros(4)
        for active in word:
            Pp = face_perp(active); qq = q_min_norm(active)
            off = Pp @ off + qq
            Lin = Pp @ Lin
        slope = eL @ (Lin @ eL)
        aB = eL @ off
        worst_aB = max(worst_aB, abs(aB))
        if abs(slope-1) < 1e-9 and abs(aB) > 1e-9 and L_ <= 2:
            print(f"  word={word} slope={slope:.4f}  a_B=P_L b_B = {aB:+.4f}  *** SLOPE 1 + NONZERO TRANSLATION ***")
print(f"worst |a_B| among all-L-fixing words (len<=4): {worst_aB:.4f}")

print("\n=== Q2: strict contraction -- worst per-step slope <1 for L-moving faces ===")
Lmoving = [f for f in Kfaces if abs(eL @ (face_perp(f) @ eL) - 1) > 1e-9]
for f in Lmoving:
    sl = eL @ (face_perp(f) @ eL)
    print(f"  H={f!s:12s} single-step slope on L = {sl:+.4f}  (1-slope={1-abs(sl):.4f})")
print(f"\ndelta_T = {delta:.4f},  delta^2/r at r=3 ~ {delta**2/3:.4f}")

print("\n=== Q3: does an L-moving face force STRICT contraction bounded below by poly(delta)? ===")
print("The full-K face {a,b,e} gives slope EXACTLY 0 (kills L) -> reset.")
print("Faces containing e but not full-K ({e},{a,e},{b,e}) give slope in (0,1) (partial contraction).")
print("KEY QUESTION (admissibility): must every admissible CLOSED RETURN excursion that genuinely")
print("PROMOTES J->K and returns contain a step whose active face spans all of K, OR at least one")
print("L-moving face? If a closed return can use ONLY L-fixing faces (a,b,ab) with nonzero a_B,")
print("the slope is exactly 1 and translations ACCUMULATE -> GAP.")
