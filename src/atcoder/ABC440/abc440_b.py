n=int(input())
tlist=list(map(int,input().split()))

slist=sorted(tlist)
tdict={}
for i in range(n):
    tdict[tlist[i]]=i

ans=[]
for i in range(3):
    ans.append(str(tdict[slist[i]]+1))

print(" ".join(ans))