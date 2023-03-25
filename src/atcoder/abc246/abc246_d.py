n=int(input())
if n==0:
    print(0)
    exit()

xr=int(n**(1/3))

ans=10**18
for x in range(xr):
    y=xr-x+1
    z=x**3 + y**3 + (x**2)*y + (y**2)*x
    if z > n:
        ans=min(ans,z)

print(ans)