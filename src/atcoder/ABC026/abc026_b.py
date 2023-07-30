import math
n=int(input())
rlist=[]
for i in range(n):
    rlist.append(int(input()))
rlist.sort(reverse=True)
ans=0
for i in range(n):
    r=rlist[i]
    if i%2==0:
        ans+=r**2
    else:
        ans-=r**2

print(ans*math.pi)