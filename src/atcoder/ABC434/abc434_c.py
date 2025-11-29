t=int(input())
cases=[]
for _ in range(t):
    n,h=map(int,input().split())
    tlu=[]
    for _ in range(n):
        t,l,u=map(int,input().split())
        tlu.append((t,l,u))
    cases.append([n,h,tlu])

for n,h,tlu in cases:
    hu=h
    hl=h
    t0=0
    ok=True
    for t,l,u in tlu:
        w=t-t0
        t0=t
        if hu+w<l or hl-w>u:
            ok=False
            break
        hu=min(u,hu+w)
        hl=max(l,hl-w)
    if ok:
        print("Yes")
    else:
        print("No")
