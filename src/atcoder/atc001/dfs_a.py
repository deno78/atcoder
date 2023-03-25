# TODO edit the code

# param
h,w = map(int,input().split())
c=[]
s=[]
g=[]
for i in range(h):
    c.append(input().split())
    for j in range(w):
        if c[j]=="s":
            s=[i,j]
        elif c[j]=="g":
            g=[i,j]




# solve
ans = n

# answer
print(ans)
