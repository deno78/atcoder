n=int(input())
slist=[]
for i in range(n):
    slist.append(input())
m=int(input())
tlist=[]
for i in range(m):
    tlist.append(input())

ans={}
for s in slist:
    if s not in ans.keys():
        ans[s]=0
    ans[s]+=1
for t in tlist:
    if t not in ans.keys():
        ans[t]=0
    ans[t]-=1

print(max(0,max(ans.values())))
