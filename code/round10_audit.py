import numpy as np
from itertools import product, permutations
rng = np.random.default_rng(12345)

def random_basis(r, cond_target=None):
    # random unit columns A (r x r), G = A^T A unit diag
    A = rng.standard_normal((r, r))
    A = A / np.linalg.norm(A, axis=0, keepdims=True)
    return A

def Gfrom(A):
    G = A.T @ A
    d = np.sqrt(np.diag(G))
    G = G / np.outer(d, d)
    return G

def delta_of(G):
    Ginv = np.linalg.inv(G)
    return 1.0/np.sqrt(np.max(np.diag(Ginv)))

# ---------------- Orbit simulator ----------------
def run_orbit(G, schedule_idx, schedule_eps):
    r = G.shape[0]
    c = np.zeros(r)
    maxnorm2 = 0.0
    for i, eps in zip(schedule_idx, schedule_eps):
        Gc = G @ c
        c = c + (eps - Gc[i]) * np.eye(r)[i]
        e2 = c @ G @ c
        maxnorm2 = max(maxnorm2, e2)
    return maxnorm2, c

# ---------------- CLAIM 1: PCT gaps ----------------
def P_i(A, i):
    t = A[:, i]
    return np.eye(A.shape[0]) - np.outer(t, t)

def word_R(A, word):
    R = np.eye(A.shape[0])
    for i in word:  # apply P_{i_1} first => R = P_im...P_i1, so multiply on left
        R = P_i(A, i) @ R
    return R

def gamma_word(A, word):
    R = word_R(A, word)
    return 1 - np.linalg.norm(R, 2)**2

print("=== CLAIM 1(a): Bessel identity I - R^T R = sum v_k v_k^T ===")
for trial in range(3):
    r = 4
    A = random_basis(r)
    word = [0,1,2,3,1,0]  # all coords appear
    R = word_R(A, word)
    lhs = np.eye(r) - R.T @ R
    # v_k = P_{i_1}...P_{i_{k-1}} t_{i_k}
    rhs = np.zeros((r,r))
    for k in range(len(word)):
        pref = np.eye(r)
        for j in range(k):  # P_{i_1}...P_{i_{k-1}}, applied with i_1 leftmost
            pref = P_i(A, word[j]) @ pref
        # careful ordering: P_{i_1}...P_{i_{k-1}} means leftmost is i_1
        v = pref @ A[:, word[k]]
        rhs += np.outer(v, v)
    print(f"  trial {trial}: max|lhs-rhs| = {np.max(np.abs(lhs-rhs)):.2e}")

print("\n=== CLAIM 1(b): universal gap gamma >= delta^{2r}/r^{r-1} ===")
viol = 0
for trial in range(2000):
    r = rng.integers(2,5)
    A = random_basis(r)
    G = Gfrom(A)
    d = delta_of(G)
    # build a full word: a random permutation plus some repeats
    perm = list(rng.permutation(r))
    extra = list(rng.integers(0,r,size=rng.integers(0,4)))
    word = extra + perm  # ensures all coords appear (perm covers all)
    g = gamma_word(A, word)
    bound = d**(2*r)/r**(r-1)
    if g < bound - 1e-12:
        viol += 1
print(f"  violations of (b) over 2000 trials: {viol}")

print("\n=== CLAIM 1(c): permutation gap gamma >= delta^2 / r^3 ===")
viol = 0
minratio = np.inf
for trial in range(5000):
    r = rng.integers(2,6)
    A = random_basis(r)
    G = Gfrom(A)
    d = delta_of(G)
    perm = list(rng.permutation(r))
    g = gamma_word(A, perm)
    bound = d**2/r**3
    minratio = min(minratio, g/bound)
    if g < bound - 1e-12:
        viol += 1
print(f"  violations of (c): {viol}, min ratio gamma/(delta^2/r^3) = {minratio:.3f}")

print("\n=== CLAIM 1(d): palindrome identities ===")
# Q = R^T R, BB^T = I - Q^2, x_eta = (I-Q)^{-1} B eta, E|x|^2 = tr[(I+Q)(I-Q)^{-1}]
for trial in range(3):
    r = 3
    A = random_basis(r)
    word = [0,1,2,1]
    R = word_R(A, word)
    Q = R.T @ R
    # check eigs of Q in [0,1]
    ev = np.linalg.eigvalsh(Q)
    # BB^T = I - Q^2
    M = np.eye(r) - Q@Q
    eM = np.linalg.eigvalsh(M)
    # trace identity
    Iq = np.eye(r)
    tr = np.trace((Iq+Q) @ np.linalg.inv(Iq-Q)) if np.max(ev)<1-1e-9 else np.inf
    gam = 1-np.max(ev)
    print(f"  trial {trial}: eig(Q) in [{ev.min():.3f},{ev.max():.3f}], min eig(I-Q^2)={eM.min():.3e}, tr[(I+Q)(I-Q)^-1]={tr:.3f}, (2-g)/g={(2-gam)/gam:.3f}")

print("\n=== CLAIM 1(d) full palindrome orbit Monte Carlo: E|x|^2 vs (2-g)/g ===")
# F_eta(x) = Q x + B eta with BB^T = I - Q^2, eta = +-1 scalar? B is r x m
# Actual claim: repeating signed palindrome -> x_eta=(I-Q)^{-1} B eta. Check via orbit.
# We instead verify the SPECTRAL lower bound interpretation numerically with the real orbit later.

# ---------------- CLAIM 2: Theorem 1 comparison-stable ----------------
print("\n=== CLAIM 2: Theorem 1 comparison-stable sup|p| <= r/eta ===")
viol=0; worst=0
for trial in range(3000):
    r = rng.integers(2,6)
    # construct diagonally dominant-ish G to get rho(B)<1
    A = random_basis(r)
    G = Gfrom(A)
    B = np.abs(G - np.eye(r))
    rho = max(np.abs(np.linalg.eigvals(B)))
    eta = 1 - rho
    if eta <= 0.02:
        continue
    # adversarial-ish random schedule, try to maximize
    best = 0
    for s in range(40):
        L = rng.integers(2*r, 12*r)
        idx = rng.integers(0,r,size=L)
        eps = rng.choice([-1,1], size=L)
        m2,_ = run_orbit(G, idx, eps)
        best=max(best, m2)
    sup_p = np.sqrt(best)
    bound = r/eta
    worst = max(worst, sup_p/bound)
    if sup_p > bound + 1e-9:
        viol+=1
print(f"  Thm1 violations: {viol}, worst sup|p|/(r/eta) = {worst:.3f}")

# ---------------- CLAIM 2 corollary lambda_min(G) >= delta^2/r ----------------
print("\n=== CLAIM 2 corollary: lambda_min(G) >= delta^2/r ===")
viol=0; minr=np.inf
for trial in range(5000):
    r=rng.integers(2,8)
    A=random_basis(r)
    G=Gfrom(A)
    d=delta_of(G)
    lm=np.linalg.eigvalsh(G).min()
    minr=min(minr, lm/(d**2/r))
    if lm < d**2/r - 1e-12:
        viol+=1
print(f"  violations: {viol}, min lambda_min/(delta^2/r) = {minr:.3f}")

# ---------------- CLAIM 3: Theorem 2 equicorrelation ----------------
print("\n=== CLAIM 3: Theorem 2 equicorrelation G_alpha ===")
def Galpha(r, alpha):
    return (1-alpha)*np.eye(r) + alpha*np.ones((r,r))
viol=0; worst=0
for trial in range(400):
    r=rng.integers(2,7)
    alpha=rng.uniform(0.0, 0.95)/ (1) # need PD: alpha in (-1/(r-1),1)
    if alpha >= 1: continue
    G=Galpha(r,alpha)
    # unit diagonal? diag = 1-alpha+alpha=1 yes
    d=delta_of(G)
    best=0
    for s in range(60):
        L=rng.integers(2*r,14*r)
        idx=rng.integers(0,r,size=L)
        eps=rng.choice([-1,1],size=L)
        m2,_=run_orbit(G,idx,eps)
        best=max(best,m2)
    bound = r**3/(1-alpha)+alpha*r**2
    bound2 = 2*r**3/d**2 + r**2
    worst=max(worst, best/bound)
    if best > bound + 1e-6:
        viol+=1
    # also check delta^2 <= 2(1-alpha)
print(f"  Thm2 violations of c^TGc<=r^3/(1-a)+a r^2: {viol}, worst ratio={worst:.3f}")

# check recursion F_s = 1 + (1-a)F_{s-1} + a F_{r-s} with F_s = s(1+a(r-1-s))/(1-a)
print("\n=== CLAIM 3: recursion F_s = 1 + (1-a)F_{s-1} + a F_{r-s} ===")
def Fs(s,r,a):
    return s*(1+a*(r-1-s))/(1-a)
maxerr=0
for trial in range(2000):
    r=rng.integers(2,10); a=rng.uniform(0,0.99)
    for s in range(1,r+1):
        lhs=Fs(s,r,a)
        rhs=1+(1-a)*Fs(s-1,r,a)+a*Fs(r-s,r,a)
        maxerr=max(maxerr, abs(lhs-rhs))
print(f"  max recursion residual = {maxerr:.3e}")
# check F_r = r
print("  F_r - r samples:", [round(Fs(r,r,a)-r,9) for (r,a) in [(5,0.3),(7,0.8),(3,0.1)]])
# check F_1 = (1+a(r-2))/(1-a) <= r/(1-a)?
print("  F_1 vs r/(1-a):", [(round(Fs(1,r,a),3), round(r/(1-a),3)) for (r,a) in [(5,0.3),(7,0.8)]])

# delta^2 <= 2(1-alpha) for G_alpha
print("\n=== CLAIM 3: delta^2 <= 2(1-alpha) ===")
viol=0
for trial in range(3000):
    r=rng.integers(2,12); a=rng.uniform(0,0.99)
    G=Galpha(r,a); d=delta_of(G)
    if d**2 > 2*(1-a)+1e-9: viol+=1
print(f"  violations: {viol}")

# ---------------- CLAIM 5: Hadamard family ----------------
print("\n=== CLAIM 5: Hadamard family ===")
def hadamard(n):
    H=np.array([[1.0]])
    while H.shape[0]<n:
        H=np.block([[H,H],[H,-H]])
    return H
for k in [1,2,3,4,5,6]:
    r=2**k
    H=hadamard(r)
    D=np.diag(np.diag(H))
    G=np.eye(r)+(H-D)/(4*np.sqrt(r))
    diag=np.diag(G)
    lm=np.linalg.eigvalsh(G).min()
    d=delta_of(G) if lm>0 else float('nan')
    B=np.abs(G-np.eye(r))
    rho=max(np.abs(np.linalg.eigvals(B)))
    print(f"  r={r}: unit_diag={np.allclose(diag,1)}, lambda_min={lm:.4f} (>=5/8? {lm>=5/8-1e-9}), delta={d:.4f}, rho(|G-I|)={rho:.4f}, (r-1)/(4sqrt r)={(r-1)/(4*np.sqrt(r)):.4f}, PD={lm>0}")
