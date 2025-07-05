import bisect

t=int(input())
tlist=[]
nlist=[]
for i in range(t):
    nlist.append(int(input()))
    tlist.append(list(map(int, input().split())))

for wk in tlist:
    wk.sort()
    tset=set(wk)
    idxzero=bisect.bisect_left(wk,0)
    if idxzero==len(wk):
        t1=wk[idxzero-1]
        t2=wk[idxzero-2]
    else:
        t1=wk[idxzero]
        if min(wk)<0:
            t2=wk[idxzero-1]
        else:
            t2=wk[idxzero+1]
        if abs(t1)>abs(t2):
            twk=t2
            t2=t1
            t1=twk
    ok=True
    x=t1
#    print(wk,idxzero,t1,t2)
    for i in range(1,len(wk)):
        x=x*t2/t1
        if x.is_integer and int(x) not in tset:
            ok=False
            print("No")
            break
    if ok:
        print("Yes")
