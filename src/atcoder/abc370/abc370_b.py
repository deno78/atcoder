# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist=[]
for i in range(n):
    alist.append([-1]*n)


for i in range(n):
    a=list(map(int, input().split()))
    for j in range(n):
        if j<=i:
            alist[i][j]=a[j]-1

x=0
for i in range(n):
    if x>i:
        x=alist[x][i]
    else:
        x=alist[i][x]

# solve
print(x+1)
