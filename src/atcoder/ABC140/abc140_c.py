n=int(input())
blist=list(map(int,input().split()))

ans=0
for i in range(n-2):
    ans+=blist[i]-blist[i+1]
print(ans)

#b0+b1+b2 =a0+a1+a2+a3

#b0=a0+a1
#b1=   a1+a2
#b2=      a2+a3

#b0-b1=a0+a2
#b1-b2=a1+a3