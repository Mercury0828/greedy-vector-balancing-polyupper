import numpy as np
rng=np.random.default_rng(11)

# --- 1(b) sigma_min bound: sigma_min(W) >= |det W| / ||W||_F^{r-1} ? ---
# Standard: prod sigma_i = |det W|; each sigma_i <= ||W||_2 <= ||W||_F.
# sigma_min = |det|/prod_{i>min} sigma_i >= |det|/ ||W||_F^{r-1}. Claim uses ||W||_F^{r-1}. Check numerically.
print("=== 1(b) sigma_min(W) >= |detW|/||W||_F^{r-1} ===")
viol=0; mr=np.inf
for _ in range(20000):
    r=rng.integers(2,7)
    W=rng.standard_normal((r,r))
    smin=np.linalg.svd(W,compute_uv=False).min()
    bound=abs(np.linalg.det(W))/np.linalg.norm(W,'fro')**(r-1)
    mr=min(mr,smin/bound)
    if smin<bound-1e-9: viol+=1
print(f"  violations={viol}, min ratio={mr:.3f}")

# --- 1(b) <u_j, w_j> = dist(t_pi_j, span earlier) >= delta ---
# w_j = first-occurrence vector = (projected) t at first occurrence; u_j Gram-Schmidt of t's.
# dist(t_j, span of earlier t's) >= delta is the DISTANCE PROPERTY definition. Check delta = min dist.
print("\n=== delta = min_i dist(t_i, span others) and dist(t_pi_j, span earlier)>=delta ===")
def random_unit_cols(r):
    A=rng.standard_normal((r,r)); return A/np.linalg.norm(A,axis=0,keepdims=True)
viol=0
for _ in range(3000):
    r=rng.integers(2,6)
    A=random_unit_cols(r)
    G=A.T@A; d=np.sqrt(np.diag(G)); G=G/np.outer(d,d)
    An=A/np.linalg.norm(A,axis=0,keepdims=True)
    delta=1/np.sqrt(np.max(np.diag(np.linalg.inv(G))))
    # dist(t_i, span others)
    for i in range(r):
        others=np.delete(An,i,axis=1)
        Pr=others@np.linalg.pinv(others)
        di=np.linalg.norm(An[:,i]-Pr@An[:,i])
        if di < delta-1e-9: viol+=1
    # dist to span of EARLIER (subset) >= dist to span of ALL others >= delta. monotone OK.
print(f"  dist(t_i,span others) < delta violations: {viol}  (delta=min over i of these by def of G^-1 diag)")
# verify delta = min_i dist exactly
A=random_unit_cols(4); G=A.T@A; dd=np.sqrt(np.diag(G)); G=G/np.outer(dd,dd)
An=A/np.linalg.norm(A,axis=0,keepdims=True)
delta=1/np.sqrt(np.max(np.diag(np.linalg.inv(G))))
dists=[np.linalg.norm(An[:,i]-(np.delete(An,i,1)@np.linalg.pinv(np.delete(An,i,1)))@An[:,i]) for i in range(4)]
print(f"  delta={delta:.5f}, min_i dist={min(dists):.5f}, match={np.isclose(delta,min(dists))}")

# --- Claim 2(iii): symmetric B>=0 entrywise, rho(B)<=1-eta => (I-B)^{-1}>=0 and ||(I-B)^{-1}||_2<=1/eta ---
print("\n=== 2(iii) (I-B)^{-1}>=0 entrywise & ||(I-B)^{-1}||_2 <= 1/eta ===")
viol=0
for _ in range(3000):
    r=rng.integers(2,6)
    M=np.abs(rng.standard_normal((r,r))); M=(M+M.T)/2; np.fill_diagonal(M,0)
    rho=max(abs(np.linalg.eigvals(M)))
    M=M/rho*rng.uniform(0.1,0.95)   # scale so rho<1
    rho=max(abs(np.linalg.eigvals(M)).real)
    eta=1-rho
    inv=np.linalg.inv(np.eye(r)-M)
    nonneg = (inv>=-1e-9).all()
    nrm=np.linalg.norm(inv,2)
    # for symmetric B, ||(I-B)^{-1}||_2 = 1/(1-lambda_max(B)). lambda_max(B)<=rho(B). eta=1-rho.
    ok = nrm <= 1/eta + 1e-6
    if not (nonneg and ok): viol+=1
print(f"  violations: {viol}")
# Note: for symmetric B, ||(I-B)^{-1}||_2 = 1/(1-lambda_max). But eta defined via rho=spectral radius
# = max|lambda|. If B has a very negative eigenvalue, lambda_max < rho, so 1/(1-lambda_max) could be
# LESS than 1/eta -> still fine. BUT B=|G-I|>=0 entrywise (Perron-Frobenius) => rho=lambda_max>=0. So OK.
print("  (B=|G-I| entrywise >=0 => Perron-Frobenius: rho(B)=lambda_max(B), so 1/eta is exact 2-norm.)")

# --- Claim 1(e): round-partitioned schedule bound. Verify sup|p| stays poly under round schedules ---
print("\n=== 1(e) round-partitioned schedule: sup|p| <= 4r^4/delta^3 + 2r/delta ? ===")
def run(G,idx,eps):
    r=G.shape[0];c=np.zeros(r);mx=0
    for i,e in zip(idx,eps):
        c=c+(e-(G@c)[i])*np.eye(r)[i];mx=max(mx,c@G@c)
    return mx
worst=0
for _ in range(300):
    r=rng.integers(2,6)
    A=random_unit_cols(r);G=A.T@A;dd=np.sqrt(np.diag(G));G=G/np.outer(dd,dd)
    delta=1/np.sqrt(np.max(np.diag(np.linalg.inv(G))))
    best=0
    for s in range(30):
        idx=[];eps=[]
        for rnd in range(20):
            perm=list(rng.permutation(r)); idx+=perm; eps+=list(rng.choice([-1,1],size=r))
        best=max(best,run(G,idx,eps))
    sup_p=np.sqrt(best); bound=4*r**4/delta**3+2*r/delta
    worst=max(worst, sup_p/bound)
print(f"  worst sup|p|/bound over round schedules = {worst:.4f}  (must be <=1)")
