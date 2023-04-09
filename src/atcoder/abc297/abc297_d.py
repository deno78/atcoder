a,b=map(int,input().split())

a,b=sorted([a,b])
if a==b:
    print("0")
    exit()

ans=0
while a!=b and b!=0 and a!=0:
    ans+=b//a
    t=b%a
    b=a
    a=t

print(ans-1)