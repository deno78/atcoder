import math

l,r=map(int,input().split())

ans=-1
for x in range(l,r):
    for y in reversed(range(x,r+1)):
            if math.gcd(x,y)==1:
                ans=max(ans,y-x)

print(ans)