# TODO edit this code

# param
x,y,n=map(int,input().split())

# solve
ans=float('INF')
for i in range(0,n//3+1):
    if i*3 <=n:
        ans=min(ans,i*y+(n-i*3)*x)

print(ans)
