n,m=map(int,input().split())
xlists=[]
for i in range(n):
    l=int(input())
    xlist=list(map(int,input().split()))
    xlists.append(xlist)

ans=[0]*n
mlist=[0]*m
for i in range(n):
    xlist=xlists[i]
    for x in xlist:
        if mlist[x-1]==0:
            ans[i]=x
            mlist[x-1]=1
            break

for i in range(n):
    print(str(ans[i]))
