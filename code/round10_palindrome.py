import numpy as np
rng=np.random.default_rng(99)

def random_basis(r):
    A=rng.standard_normal((r,r)); return A/np.linalg.norm(A,axis=0,keepdims=True)
def Gfrom(A):
    G=A.T@A; d=np.sqrt(np.diag(G)); return G/np.outer(d,d)
def delta_of(G):
    return 1/np.sqrt(np.max(np.diag(np.linalg.inv(G))))
def run_orbit(G,idx,eps):
    r=G.shape[0]; c=np.zeros(r); mx=0.0
    for i,e in zip(idx,eps):
        Gc=G@c; c=c+(e-Gc[i])*np.eye(r)[i]; mx=max(mx,c@G@c)
    return mx,c

# ---- CLAIM 1(d): does a small cycle-gap gamma really force a large BST orbit? ----
# The reduction: take full word R (all coords), append its reversal to make a palindrome word
# P = (i_1..i_m, i_m..i_1). Repeat P with a fixed sign pattern eta chosen to maximize growth.
# Claim: sup_k |p_k|^2 >= (2-gamma)/gamma roughly, where gamma=1-||R||^2.
# We don't have the exact B/eta machinery, but we can numerically search: build a basis with
# small gamma and check whether SOME periodic schedule produces a large orbit ~ 1/gamma.

print("=== palindrome reduction: small gamma -> large orbit? ===")
print(f"{'r':>2} {'gamma':>10} {'(2-g)/g':>10} {'best_orbit2':>12} {'ratio':>8}")
for trial in range(12):
    r=rng.integers(2,4)
    A=random_basis(r)
    G=Gfrom(A)
    # full word = permutation (gamma ~ delta^2/r^3, can be smallish)
    perm=list(rng.permutation(r))
    # palindrome word
    pal=perm+perm[::-1]
    # compute gamma of the BASE word R = product over pal? The reduction uses R=word, Q=R^TR.
    # Actually palindrome of R means Q=R^T R; the relevant contraction is lambda_max(Q)=||R||^2.
    def Pmat(i):
        t=A[:,i]; return np.eye(r)-np.outer(t,t)
    R=np.eye(r)
    for i in perm: R=Pmat(i)@R
    gamma=1-np.linalg.norm(R,2)**2
    # search periodic sign schedules over the palindrome word, repeated many times
    best=0
    for s in range(200):
        nrep=30
        idx=pal*nrep
        eps=rng.choice([-1,1],size=len(idx))
        m2,_=run_orbit(G,idx,eps)
        best=max(best,m2)
    target=(2-gamma)/gamma
    print(f"{r:>2} {gamma:>10.4f} {target:>10.2f} {best:>12.2f} {best/target:>8.3f}")

# ---- CLAIM 4: nested-palindrome amplifier, does delta collapse exponentially? ----
print("\n=== CLAIM 4: nested palindrome amplifier eigenvalue & delta collapse ===")
# Mechanism described: S_+ = (S (+) I) P_t (S (+) I), lambda_+ = 1 - a^2(1-lambda^2).
# Build a 2D near-parallel projection gadget and nest. Track product norm gap vs delta of basis.
# We construct a basis explicitly: at each level add a vector nearly in the span (controlled by a).
def gap_and_delta(A):
    G=Gfrom(A); d=delta_of(G)
    return d
# build nested: start r=2 with angle, each level appends a vector at small angle to existing span
print("Tracking: as we nest m levels with amplification param a, does delta ~ a^m?")
for a in [0.5,0.7,0.9]:
    deltas=[]
    for m in range(2,8):
        # construct m vectors where each new one is mostly in previous span, residual ~ prod a
        # crude model: t_k = sqrt(1-rk^2)*u_k_in_span + rk*e_new, rk = a^(k-1)
        r=m
        A=np.zeros((r,r))
        A[0,0]=1
        for k in range(1,r):
            # in-span part = random combo of previous columns (unit), residual along new axis
            combo=rng.standard_normal(k); v=A[:k,:k]@combo if k>0 else np.zeros(0)
            vec=np.zeros(r)
            vec[:k]=v/ (np.linalg.norm(v)+1e-12)
            res=a**k
            vec=np.sqrt(max(1-res**2,0))*vec
            vec[k]=res
            vec=vec/np.linalg.norm(vec)
            A[:,k]=vec
        d=gap_and_delta(A)
        deltas.append(d)
    print(f"  a={a}: delta over m=2..7 =", [f"{x:.2e}" for x in deltas], " ratio to a^m:", f"{deltas[-1]/a**7:.2f}")
