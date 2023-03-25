n=int(input())
ans=0
for i in range(n):
    x,u=input().split()
    if u=="JPY":
        ans+=float(x)
    else:
        ans+=380000*float(x)
print(ans)