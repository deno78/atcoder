m,d=map(int,input().split())
s=input()

chk=[0]*m

for i in range(m):
    if s[i]=="G":
        for j in range(d+1):
            idx1=max(i-j,0)
            idx2=min(i+j,m-1)
            chk[idx1]+=1
            chk[idx2]+=1

ans=0
for i in range(m):
    if chk[i]==0:
        ans+=1
print(ans)