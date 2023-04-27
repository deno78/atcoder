n,t=map(int,input().split())
clist = list(map(int,input().split()))
rlist = list(map(int,input().split()))

ans=-1
val=-1
if t not in clist:
    t=clist[0]
    ans=0

for i in range(n):
    c=clist[i]
    r=rlist[i]
    if c==t:
        if r>val:
            ans=i
            val=r

print(ans+1)

