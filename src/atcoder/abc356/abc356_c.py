# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m,k = map(int, input().split())
clist=[]
rlist=[]
alist=[]
for i in range(m):
    wk=input().split()
    c=int(wk[0])
    r=wk[-1]
    a=[]
    for i in wk[1:-1]:
        a.append(int(i)-1)
    clist.append(c)
    rlist.append(r)
    alist.append(a)
ans=0
for i in range(2**n):
    bag=[0]*n
    for j in range(n):
        if ((i>>j)&1):
            bag[j]=1
#    print(bag)
    ok=True
    for j in range(m):
        c=clist[j]
        r=rlist[j]
        a=alist[j]
        w=0
        for l in range(int(c)):
            x=int(a[l])
            if bag[x]==1:
                w+=1
        if w>=k and r=="x":
            ok=False
            break
        if w<k and r=="o":
            ok=False
            break
    if ok:
        ans+=1

print(ans)
