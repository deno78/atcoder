# TODO edit the code

# param
n,a,b =map(int,input().split())

# solve

# answer
for i in range(a*n):
    l=[]
    for j in range(b*n):
        x=i//a
        y=j//b
        if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
            l.extend(["."])
        else:
            l.extend(["#"])
    print("".join(l))

