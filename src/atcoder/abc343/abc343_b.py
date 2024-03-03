# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
amap=[]
for i in range(n):
    a=list(map(int,input().split()))
    amap.append(a)

# solve
for i in range(n):
    ans=[]
    for j in range(n):
        if amap[i][j]==1:
            ans.append(str(j+1))
    print(" ".join(ans))

# answer
