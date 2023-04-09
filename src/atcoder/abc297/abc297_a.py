# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,d = map(int, input().split())
tlist=list(map(int,input().split()))

# solve
for i in range(1,n):
    if tlist[i] - tlist[i-1]<=d:
        print(tlist[i])
        exit()

# answer
print(-1)