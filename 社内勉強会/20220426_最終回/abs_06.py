n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    x=0
    for c in list(str(i)):
        x+=int(c)
#    print("{} {}".format(i,x))
    if a<=x and x<=b:
        ans+=i
print(ans)
