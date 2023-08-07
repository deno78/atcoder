a,b,c=map(int,input().split())

if c==a+b and c==a-b:
    print("?")
elif c==a+b:
    print("+")
elif c==a-b:
    print("-")
else:
    print("!")