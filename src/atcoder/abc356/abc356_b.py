# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
x=[]
for i in range(n):
    w=list(map(int,input().split()))
    x.append(w)

# solve
for i in range(n):
    for j in range(m):
        b=x[i][j]
        alist[j]-=b

for i in range(m):
    if alist[i]>0:
        print("No")
        exit()
print("Yes")
