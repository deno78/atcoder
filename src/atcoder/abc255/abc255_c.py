x,a,d,n=map(int,input().split())

if d==0:
    print(abs(x-a))
    exit()

c=(x-a)//d
c=min(c,n-1)
c=max(0,c)

ans=float('inf')
for i in range(-3,3):
    c1=c+i
    c1 = min(c1,n-1)
    c1 = max(c1,0)
    x2 = a+c1*d
#    print("[{}] {} ->{}".format(c1,x2,abs(x-x2)))
    ans=min(ans,abs(x-x2))

print(ans)