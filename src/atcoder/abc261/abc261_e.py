# TODO edit the code

# param
n,c=map(int,input().split())
talist=[]
for i in range(n):
    t,a=map(int,input().split())
    talist.append([t,a])

# solvepyt
ans=[]
x = c
for i in range(n):
    for j in range(i+1):
        t,a=talist[j]
        if t == 1:
            x=x & a
        elif t == 2:
            x= x| a
        elif t == 3:
            x=x ^ a
    ans.append(x)

for a in ans:
    print(a)