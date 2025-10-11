def f(n):
    a=0
    s=str(n)
    for c in s:
        a+=int(c)
    return a

n=int(input())

ans=1
for i in range(1,n):
    w=f(ans)
    ans+=w
#    print(i,w,ans)
print(ans)