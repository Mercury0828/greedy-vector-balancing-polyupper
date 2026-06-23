import numpy as np
rng = np.random.default_rng(7)

def random_basis(r):
    A = rng.standard_normal((r, r))
    return A / np.linalg.norm(A, axis=0, keepdims=True)

def P_i(A,i):
    t=A[:,i]; return np.eye(A.shape[0])-np.outer(t,t)

# Telescoping identity for orthogonal projections:
# For S_k = P_{i_k} P_{i_{k-1}} ... P_{i_1}, since P^T=P, P^2=P:
#   S_{k-1}^T S_{k-1} - S_k^T S_k = S_{k-1}^T (I - P_{i_k}) S_{k-1}
#   = S_{k-1}^T t_{i_k} t_{i_k}^T S_{k-1} = w_k w_k^T,  w_k = S_{k-1}^T t_{i_k}
# Sum telescopes: I - R^T R = sum_k w_k w_k^T, with w_k = (P_{i_1}...P_{i_{k-1}}) t_{i_k}
#   (since S_{k-1}^T = P_{i_1}...P_{i_{k-1}} because each P symmetric, reverse order)
r=4
A=random_basis(r)
word=[0,1,2,3,1,0]
# R = P_im...P_i1
R=np.eye(r)
for i in word:
    R=P_i(A,i)@R
lhs=np.eye(r)-R.T@R

# w_k = S_{k-1}^T t_{i_k}; S_{k-1}=P_{i_{k-1}}...P_{i_1}; S_{k-1}^T = P_{i_1}...P_{i_{k-1}}
rhs=np.zeros((r,r))
for k in range(len(word)):
    Skm1=np.eye(r)
    for j in range(k):
        Skm1=P_i(A,word[j])@Skm1          # S_{k-1}=P_{i_{k-1}}...P_{i_1}
    w=Skm1.T@A[:,word[k]]
    rhs+=np.outer(w,w)
print("Telescoping (w_k=S_{k-1}^T t): max|lhs-rhs|=",np.max(np.abs(lhs-rhs)))

# Now the version as I first coded: v_k = (P_{i_1}...P_{i_{k-1}}) t with i_1 LEFTMOST
rhs2=np.zeros((r,r))
for k in range(len(word)):
    pref=np.eye(r)
    for j in range(k):
        pref=pref@P_i(A,word[j])          # P_{i_1} P_{i_2} ... (i_1 leftmost)
    v=pref@A[:,word[k]]
    rhs2+=np.outer(v,v)
print("v_k = P_{i_1}P_{i_2}...P_{i_{k-1}} t (i_1 leftmost): max|lhs-rhs|=",np.max(np.abs(lhs-rhs2)))

# Note S_{k-1}^T = (P_{i_{k-1}}...P_{i_1})^T = P_{i_1}...P_{i_{k-1}} (i_1 leftmost) since symmetric.
# So rhs and rhs2 should be IDENTICAL. Check:
print("rhs vs rhs2 identical:", np.allclose(rhs,rhs2))

# So which matches lhs? Let's also test the claim text literally: v_k=P_{i_1}...P_{i_{k-1}} t_{i_k}
# meaning the operator P_{i_1}...P_{i_{k-1}} -- with i_1 applied... ambiguous. Both rhs/rhs2 equal.
# The telescoping DERIVATION above is rigorous. Let me re-derive sign.
# S_k^T S_k = S_{k-1}^T P_{i_k}^T P_{i_k} S_{k-1} = S_{k-1}^T P_{i_k} S_{k-1} (proj)
# S_{k-1}^T S_{k-1} - S_k^T S_k = S_{k-1}^T (I-P_{i_k}) S_{k-1} = (S_{k-1}^T t)(t^T S_{k-1}) = w_k w_k^T. OK
# telescope from k=1..m: S_0=I so S_0^T S_0=I; R=S_m. I - R^TR = sum w_k w_k^T. Rigorous.
print("\nConclusion: the rigorous w_k = S_{k-1}^T t_{i_k} = (P_{i_1}...P_{i_{k-1}}) t_{i_k}.")
print("matches lhs?", np.allclose(lhs,rhs))
