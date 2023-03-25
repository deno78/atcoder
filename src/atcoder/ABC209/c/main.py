n=int(input())
clist=list(map(int,input().split()))

MOD=10**9+7
clist.sort()
x=1
for i in range(n):
    x=x*(clist[i]-i)%MOD

print(x)