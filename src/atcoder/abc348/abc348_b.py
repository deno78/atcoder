# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
xy=[]
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])

# solve
ans=[]
for i in range(n):
    x1,y1=xy[i]
    wk=0
    p=-1
    for j in range(n):
        x2,y2=xy[j]
        l=(x1-x2)**2+(y1-y2)**2
        if l>wk:
            p=j+1
            wk=l
    ans.append(p)

# answer
for p in ans:
    print(p)
