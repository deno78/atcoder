import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n=int(input())
tlist=[]
for i in range(n):
    tlist.append(int(input()))

ans=tlist[0]
for i in range(1,n):
    t=tlist[i]
    ans=lcm(t,ans)

print(ans)