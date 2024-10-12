# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
xy=[]
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])

xy.append([0,0])
x1=0
y1=0
# solve
ans=0
for i in range(n+1):
    x2,y2=xy[i]
    d1=(x2-x1)**2+(y2-y1)**2
    ans+=d1**0.5
    x1,y1=x2,y2

# answer
print("{}".format(ans))
