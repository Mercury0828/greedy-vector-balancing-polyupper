import numpy as np
rng=np.random.default_rng(2024)

# The crux question for CLAIM 1(d): the reduction maps PCT failure -> BST counterexample.
# Answer-1 models the per-block dynamics as an affine map F_eta(x)=Qx+B eta with Q=R^T R,
# BB^T = I - Q^2, and asserts the BST orbit's block-to-block map realizes this, with fixed
# point x_eta=(I-Q)^{-1} B eta and E||x||^2 = tr[(I+Q)(I-Q)^{-1}] >= (2-gamma)/gamma.
#
# Is the BST block map ACTUALLY x -> Qx + (something)? Let's derive the exact block map.
# One greedy step at coord i with sign eps: c -> c + (eps - (Gc)_i) e_i.
# In the p-coordinates (p = A c), or work in c. A full pass of the word with signs:
# This is an AFFINE map c -> M c + v(eps) for fixed word, where M = product of (I - e_i e_i^T G).
# Let's compute M for a palindrome word and compare its symmetrized contraction to Q.

def random_basis(r):
    A=rng.standard_normal((r,r)); return A/np.linalg.norm(A,axis=0,keepdims=True)
def Gfrom(A):
    G=A.T@A; d=np.sqrt(np.diag(G)); return G/np.outer(d,d)

def block_map(G, word):
    # returns M, and affine offset as function: c_out = M c_in + b(eps)
    r=G.shape[0]
    M=np.eye(r)
    # offset linear in eps: c -> c + (eps_i - (Gc)_i)e_i = (I - e_i e_i^T G) c + eps_i e_i
    # compose: track M and the eps->offset matrix N (so offset = N @ eps_vector_per_step? )
    # Simpler: M = prod (I - e_i e_i^T G)
    for i in word:
        E=np.zeros((r,r));
        P=np.eye(r)-np.outer(np.eye(r)[i], G[i,:])
        M=P@M
    return M

# Compare ||M|| (BST block contraction in c-energy) to ||R||=sqrt(1-gamma).
# In ENERGY norm ||c||_G^2 = c^T G c. The map M in G-energy: contraction = ||G^{1/2} M G^{-1/2}||.
print("Compare BST block-map energy-contraction to projection-product ||R||:")
print(f"{'r':>2} {'||R||(proj)':>12} {'energyContr(M)':>15} {'equal?':>8}")
for trial in range(8):
    r=rng.integers(2,5)
    A=random_basis(r); G=Gfrom(A)
    perm=list(rng.permutation(r))
    # projection product R = P_im..P_i1 in the WHITENED space:
    # p = A c. A greedy step projects p? Let's check: p_{k+1}=p_k + (eps-(p_k.t_i))t_i,
    # the HOMOGENEOUS part (eps=0): p -> p - (p.t_i) t_i = P_i p. YES! homogeneous step = P_i in p-space.
    # So homogeneous block map in p-space = R = P_im..P_i1. ||R|| is the p-energy contraction.
    Pmat=lambda i: np.eye(r)-np.outer(A[:,i],A[:,i])
    R=np.eye(r)
    for i in perm: R=Pmat(i)@R
    nR=np.linalg.norm(R,2)
    # M in c-space, energy contraction = ||G^{1/2} M G^{-1/2}|| ; and p=Ac so p-space map = A M A^{-1}
    M=block_map(G,perm)
    pmap=A@M@np.linalg.inv(A)
    contr=np.linalg.norm(pmap,2)
    print(f"{r:>2} {nR:>12.5f} {contr:>15.5f} {np.isclose(nR,contr):>8}")

print("\n=> Homogeneous BST block map in p-space IS exactly R=P_im...P_i1.")
print("   So Q=R^T R governs homogeneous contraction; gamma=1-||R||^2 is real BST contraction deficit.")
print("   The translations B*eta come from the eps terms. Need BB^T=I-Q^2 to be the ACTUAL noise.")

# Now check: is the per-block translation covariance actually I - Q^2 ?
# Block map p -> R p + w(eps). The reduction APPENDS the reversal so word=perm+reversed(perm),
# making the homogeneous map R_pal = R^T R = Q (since reversed projection product = R^T for symmetric P).
print("\nCheck reversed-word homogeneous map = R^T (so palindrome block = R^T R = Q):")
for trial in range(5):
    r=rng.integers(2,5)
    A=random_basis(r)
    perm=list(rng.permutation(r))
    Pmat=lambda i: np.eye(r)-np.outer(A[:,i],A[:,i])
    R=np.eye(r)
    for i in perm: R=Pmat(i)@R
    Rrev=np.eye(r)
    for i in perm[::-1]: Rrev=Pmat(i)@Rrev
    print(f"  r={r}: ||Rrev - R^T|| = {np.linalg.norm(Rrev-R.T):.2e}")

# The translation: each greedy step at coord i adds (eps_i)*t_i to p AFTER projecting?
# p -> P_i p + eps_i t_i. So over a word, w(eps)=sum of (partial-projected) eps_i t_i.
# Covariance over random signs E[w w^T] = sum_k (P_after_k t_{i_k})(...)^T.
# For the PALINDROME, the claim BB^T = I - Q^2 should hold. Let's test E[w w^T] vs I-Q^2.
print("\nCheck translation covariance E[w w^T] vs I - Q^2 for palindrome (random +-1 signs):")
for trial in range(4):
    r=rng.integers(2,4)
    A=random_basis(r)
    perm=list(rng.permutation(r))
    pal=perm+perm[::-1]
    Pmat=lambda i: np.eye(r)-np.outer(A[:,i],A[:,i])
    # homogeneous Q
    Q=np.eye(r)
    for i in pal: Q=Pmat(i)@Q
    # translation operator: p_out = Q p_in + sum_k (P_{i_L}...P_{i_{k+1}}) eps_k t_{i_k}
    # build columns b_k = (P after step k) t_{i_k}
    cols=[]
    for k in range(len(pal)):
        suf=np.eye(r)
        for j in range(k+1,len(pal)):
            suf=Pmat(pal[j])@suf
        cols.append(suf@A[:,pal[k]])
    Bm=np.array(cols).T   # r x len(pal)
    cov=Bm@Bm.T
    print(f"  r={r}: ||E[ww^T] - (I-Q^2)|| = {np.linalg.norm(cov-(np.eye(r)-Q@Q)):.3e}, ||I-Q^2||={np.linalg.norm(np.eye(r)-Q@Q):.3f}")
