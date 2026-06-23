"""
INDEPENDENT AUDITOR — Round 8 / rank-4 zero-slope claim (Claim 1, load-bearing).

The CLAIM: for every K-confined closed return excursion B (all H_j subset of K, dim K=3),
the affine return map A_B(p)=Q_B p + b_B has Q_B = P_{K^perp} EXACTLY, hence the induced
scalar map on L=K cap J^perp (dim 1) is f_B(t)=a_B with slope EXACTLY 0.

We test:
  (T0) R7 example: L = K cap J^perp; is Q|_L = 0? Is Q = P_{K^perp} exactly?
  (T1) The user's counter-pressure 1(b): an excursion that uses ONLY the face H=J (span of
       J's normals) gives Q_B|_L = identity (slope 1). Q_B = product of P_{H_j^perp}. If some
       H_j = J then P_{J^perp} FIXES L (L subset J^perp). So Q_B|_L = identity, slope 1.
       => Q_B != P_{K^perp} in general. We exhibit this explicitly.
  (T2) General: enumerate Q_B = prod P_{H_j^perp} for H_j ranging over the FACES that appear
       (faces are spans of subsets of T, all subset of K). For which face-words is Q_B|_L = 0?
       For which is slope 1? Is slope strictly < 1 forced for "promotions"?
"""
import itertools
import numpy as np

np.set_printoptions(precision=4, suppress=True)

s26, s30 = np.sqrt(26), np.sqrt(30)
a = np.array([1.0, 0, 0, 0]); b = np.array([0, 1.0, 0, 0])
c = np.array([3, 1, 4, 0]) / s26; d = np.array([1, 3, -2, 4]) / s30; e = np.array([-2, 1, -3, -4]) / s30
VEC = {"a": a, "b": b, "c": c, "d": d, "e": e}

J = np.column_stack([a, b])            # dim 2
K = np.column_stack([a, b, e])         # dim 3

def proj_onto(cols):
    """orthogonal projector onto column span."""
    Q, _ = np.linalg.qr(cols)
    return Q @ Q.T

def proj_perp(cols):
    return np.eye(4) - proj_onto(cols)

# subspaces
P_K = proj_onto(K)
P_Kperp = np.eye(4) - P_K
P_J = proj_onto(J)
# L = K cap J^perp : within K, complement of J
# basis: project a vector of K onto J^perp, take the part inside K
P_Jperp = np.eye(4) - P_J
# L = range(P_K @ P_Jperp) intersect... compute L explicitly: vectors in K and in J^perp
# K cap J^perp = { x : x in K, x perp J }. Since J subset K, this is the orthocomplement of J within K.
# basis of K:
QK, _ = np.linalg.qr(K)  # 4x3 orthonormal basis of K
# within K coords, remove J component:
# express: L = K cap J^perp. Project QK columns to J^perp, the 1-dim leftover.
M = P_Jperp @ QK   # 4x3, columns in J^perp but maybe not in K... actually P_Jperp@(K basis) stays in span? no.
# Cleaner: L = orthocomplement of J inside K. Take P_K, restrict to J^perp:
# operator P_K restricted then remove J -> use SVD of (I-P_J) acting on K basis projected back into K
# Simplest: nullspace approach. x in K: x = QK @ y. x perp J: J^T x = 0 => J^T QK y = 0.
JT_QK = J.T @ QK    # 2x3
u, sgrid, vh = np.linalg.svd(JT_QK)
# nullspace of JT_QK : right singular vectors with zero singular value (3-2=1 dim)
null_mask = np.concatenate([sgrid, np.zeros(vh.shape[0]-len(sgrid))]) < 1e-9
Lbasis_y = vh[null_mask].T   # 3x1
Lbasis = QK @ Lbasis_y       # 4x1, unit vector spanning L
eL = Lbasis[:, 0] / np.linalg.norm(Lbasis[:, 0])
print("eL (spans L = K cap J^perp):", eL)
print("  in K? ", np.linalg.norm(P_K @ eL - eL) < 1e-9)
print("  perp J?", abs(J.T @ eL).max() < 1e-9)

m = np.array([0, 0, 3.0, 4]); n = np.array([0, 0, 4.0, -3])
print("\nm=(0,0,3,4) normalized:", m/np.linalg.norm(m), " | parallel to eL?",
      abs(abs((m/np.linalg.norm(m)) @ eL) - 1) < 1e-9)
print("n=(0,0,4,-3) normalized:", n/np.linalg.norm(n))
print("n in K^perp?", np.linalg.norm(P_Kperp @ (n/np.linalg.norm(n)) - n/np.linalg.norm(n)) < 1e-9)

# ---- reconstruct R7 Q via product of P_{H_j^perp} along excursion A active faces ----
def face_perp(active):
    cols = np.column_stack([VEC[k] for k in active])
    return proj_perp(cols)

A_active = [["a","e"],["a","b","e"],["e"],["a","e"],["e"],["a","e"],["a"],["a","b"]]
# Q_B = product P_{H_N^perp} ... P_{H_1^perp}  (last applied first in p-update? compose order)
def compose_Q(active_list):
    Q = np.eye(4)
    for active in active_list:        # step1 first; new = Pperp @ old
        Q = face_perp(active) @ Q
    return Q
QA = compose_Q(A_active)
print("\n=== R7 excursion A ===")
print("Q_A == P_{K^perp}?  max|Q_A - P_Kperp| =", np.abs(QA - P_Kperp).max())
print("Q_A @ eL (should be 0 if claim holds):", QA @ eL, " norm=", np.linalg.norm(QA @ eL))
print("slope on L = <Q_A eL, eL> =", eL @ (QA @ eL))

print("\n=== TEST T1: the user's counter-pressure 1(b) ===")
print("Excursion using ONLY face H=J (=span{a,b}). Then every P_{H_j^perp}=P_{J^perp}.")
QJ = face_perp(["a","b"])
print("P_{J^perp} @ eL =", QJ @ eL, " (eL in J^perp so FIXED) -> slope =", eL @ (QJ @ eL))
print("Q_B for a word of all-J faces == P_{J^perp} != P_{K^perp}.  max|P_Jperp - P_Kperp| =",
      np.abs(QJ - P_Kperp).max())

print("\n=== TEST T2: enumerate single-face linear parts, slope on L ===")
faces = [["a"],["b"],["e"],["a","b"],["a","e"],["b","e"],["a","b","e"]]
for f in faces:
    Pp = face_perp(f)
    sl = eL @ (Pp @ eL)
    contains_L_dir = abs(sl - 1) < 1e-9
    kills_L = abs(sl) < 1e-9
    print(f"  H={f!s:12s} slope_on_L={sl:+.4f}  fixesL={contains_L_dir} killsL={kills_L}")

print("\n=== TEST T3: which 2-step words give slope exactly 0 vs 1 ? ===")
for f1, f2 in itertools.product(faces, repeat=2):
    Q = face_perp(f2) @ face_perp(f1)
    sl = eL @ (Q @ eL)
    if abs(sl) < 1e-9 or abs(sl-1) < 1e-9:
        tag = "ZERO" if abs(sl) < 1e-9 else "ONE(slope1!)"
        print(f"  {f1!s:10s} then {f2!s:10s} slope={sl:+.4f}  {tag}")
