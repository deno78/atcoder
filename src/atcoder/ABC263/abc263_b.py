n=int(input())
plist=list(map(int,input().split()))
pdict={}
for i in range(1,n):
    pdict[i]=plist[i]-1

ans=0
x=n-1
while x!=0:
    x=pdict[x]
    ans+=1

print(ans)