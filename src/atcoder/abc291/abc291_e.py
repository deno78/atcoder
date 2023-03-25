# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
xy=[]
for i in range(m):
    x,y=map(int, input().split())
    x-=1
    y-=1
    xy.append([x,y])

# solve
alist=[0]*n

for x,y in xy:
    if alist[x]==0 and alist[y]==0:
        alist[y]=1
    elif alist[x]==0 and alist[y]!=0:
        alist[x]=alist[x]-1
    elif alist[y]==0 and alist[x]!=0:
        alist[y]=alist[x]+1
    else:
        if alist[x]>alist[y]:
            print("No")
            exit()

print(alist)

# answer
