import numpy as np
rng=np.random.default_rng(33)
def run(G,idx,eps,c0=None):
    r=G.shape[0];c=np.zeros(r) if c0 is None else c0.copy();mx=0
    cs=[c.copy()]
    for i,e in zip(idx,eps):
        c=c+(e-(G@c)[i])*np.eye(r)[i];mx=max(mx,c@G@c);cs.append(c.copy())
    return mx,c,cs

# --- Claim 2 corollary: sign flip D=diag(+-1), DGD doesn't change BST orbit norms ---
print("=== obtuse corollary: G vs DGD give same orbit energies (under sign-conjugated schedule) ===")
for _ in range(6):
    r=rng.integers(2,5)
    A=rng.standard_normal((r,r));A=A/np.linalg.norm(A,axis=0,keepdims=True)
    G=A.T@A;dd=np.sqrt(np.diag(G));G=G/np.outer(dd,dd)
    D=np.diag(rng.choice([-1,1],size=r))
    Gp=D@G@D
    L=40;idx=rng.integers(0,r,size=L);eps=rng.choice([-1,1],size=L)
    mx1,_,_=run(G,idx,eps)
    # transform: c'=Dc, eps'=D_ii eps. Energy c^TGc=c'^T Gp c'. Update for Gp with eps'=D_ii eps.
    epsp=np.array([D[i,i]*e for i,e in zip(idx,eps)])
    mx2,_,_=run(Gp,idx,epsp)
    print(f"  r={r}: energy(G)={mx1:.4f}, energy(DGD)={mx2:.4f}, match={np.isclose(mx1,mx2)}")

# --- Claim 3 equicorrelation: update overwrites c_i = eps - alpha*sum_{j!=i} c_j ; subset-sum bound ---
print("\n=== Thm2 update: c_i <- eps - alpha*sum_{j!=i}c_j (since (G_a c)_i = c_i + alpha*sum_{j!=i}c_j) ===")
def Ga(r,a): return (1-a)*np.eye(r)+a*np.ones((r,r))
for _ in range(4):
    r=rng.integers(3,6); a=rng.uniform(0,0.9)
    G=Ga(r,a); c=rng.standard_normal(r); i=rng.integers(r); e=rng.choice([-1,1])
    cnew=c+(e-(G@c)[i])*np.eye(r)[i]
    pred=e-a*(c.sum()-c[i])
    print(f"  r={r}: c_i_new={cnew[i]:.5f}, eps-a*sum_others={pred:.5f}, match={np.isclose(cnew[i],pred)}")

# verify subset-sum invariant polytope closure numerically: |sum_{S} c_j| <= F_{|S|}
print("\n=== Thm2 invariant polytope: orbit stays within |sum_S c|<=F_{|S|} ===")
from itertools import combinations
def Fs(s,r,a): return s*(1+a*(r-1-s))/(1-a)
for _ in range(20):
    r=rng.integers(2,6); a=rng.uniform(0,0.85)
    G=Ga(r,a)
    L=200;idx=rng.integers(0,r,size=L);eps=rng.choice([-1,1],size=L)
    _,_,cs=run(G,idx,eps)
    bad=False
    for c in cs:
        for s in range(1,r+1):
            for S in combinations(range(r),s):
                if abs(sum(c[j] for j in S)) > Fs(s,r,a)+1e-6:
                    bad=True
    if bad: print(f"  r={r},a={a:.2f}: VIOLATION")
print("  (no VIOLATION lines printed => polytope invariant holds)")

# --- Claim 2 (ii)/(iv): total variation V <= b + BV transfer. End-to-end: sup|p|<=r/eta verified earlier.
# Spot check the path-length / homogeneous->affine on a comparison-stable G with adversarial search.
print("\n=== Thm1 end-to-end adversarial (greedy worst-sign) sup|p| vs r/eta ===")
worst=0
for _ in range(200):
    r=rng.integers(2,6)
    A=rng.standard_normal((r,r));A=A/np.linalg.norm(A,axis=0,keepdims=True)
    G=A.T@A;dd=np.sqrt(np.diag(G));G=G/np.outer(dd,dd)
    B=np.abs(G-np.eye(r));rho=max(abs(np.linalg.eigvals(B)));eta=1-rho
    if eta<=0.05: continue
    # greedy worst-sign orbit (pick eps each step to maximize next energy)
    c=np.zeros(r);mx=0
    for step in range(400):
        i=rng.integers(r)
        be=None;bv=-1
        for e in (-1,1):
            cn=c+(e-(G@c)[i])*np.eye(r)[i];v=cn@G@cn
            if v>bv:bv=v;be=e
        c=c+(be-(G@c)[i])*np.eye(r)[i];mx=max(mx,c@G@c)
    worst=max(worst,np.sqrt(mx)/(r/eta))
print(f"  worst sup|p|/(r/eta) = {worst:.3f}  (<=1 required)")
