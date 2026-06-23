import numpy as np
rng=np.random.default_rng(5)
# Show a DIRECTED sign schedule (aligned to the slow eigenvector of Q) achieves ~ (2-gamma)/gamma,
# confirming small gamma => large BST orbit (1d conclusion). Use a controlled small-gamma basis (r=2).
def basis_angle(theta):
    # two unit vectors at angle theta; small theta => near-parallel => projections barely contract along..
    return np.array([[1,np.cos(theta)],[0,np.sin(theta)]])
for theta in [0.6,0.3,0.15,0.08]:
    A=basis_angle(theta)
    r=2
    Pmat=lambda i: np.eye(r)-np.outer(A[:,i],A[:,i])
    perm=[0,1]
    pal=perm+perm[::-1]   # 0,1,1,0
    Q=np.eye(r)
    for i in pal: Q=Pmat(i)@Q
    ev,evec=np.linalg.eigh(Q)
    lam=ev.max(); gamma=1-lam
    target=(2-gamma)/gamma
    # directed schedule: run the palindrome word repeatedly; choose eps each step to push p along slow dir.
    G=A.T@A; d=np.sqrt(np.diag(G)); G=G/np.outer(d,d)
    An=A/np.linalg.norm(A,axis=0,keepdims=True)
    Gn=An.T@An
    c=np.zeros(r); mx=0
    slow=evec[:,np.argmax(ev)]   # in p-space
    for rep in range(4000):
        for i in pal:
            p=An@c
            # choose sign to increase alignment of resulting p with slow dir
            best_e=None;best_val=-1e9
            for e in (-1,1):
                cn=c+(e-(Gn@c)[i])*np.eye(r)[i]
                pn=An@cn
                val=abs(pn@slow)
                if val>best_val: best_val=val;best_e=e
            c=c+(best_e-(Gn@c)[i])*np.eye(r)[i]
            mx=max(mx,c@Gn@c)
    print(f"theta={theta}: gamma={gamma:.4f}, (2-g)/g={target:.2f}, achieved orbit^2={mx:.2f}, ratio={mx/target:.3f}")
