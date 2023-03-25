a,b=map(int,input().split())

if a*2==b or a*2+1 == b:
    print("Yes")
else:
    print("No")

if b//a==2:
    print("Yes")
else:
    print("No")