n=int(input())
plist=list(map(int,input().split()))

d=[]
for i in range(len(plist)):
    if i==plist[i]-1:
        d.append(i)

ans=0
for i in d:
    if i>0 and plist[i-1]!=i and plist[i]!=i-1:
        ans+=1
    if i<n-1 and plist[i+1]!=i and plist[i]!=i+1:
        ans+=1
print(ans)
