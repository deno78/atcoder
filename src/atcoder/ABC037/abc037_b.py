n,q=map(int,input().split())

lrt=[]
for i in range(q):
    l,r,t=map(int,input().split())
    l-=1
    r-=1
    lrt.append([l,r,t])


ans=[0]*n

for l,r,t in lrt:
    for i in range(l,r+1):
        ans[i]=t

ans2=[]
for i in ans:
    ans2.append(str(i))

print(" ".join(ans2))