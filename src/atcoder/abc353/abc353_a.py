
# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
hlist = list(map(int, input().split()))

# solve
for i in range(n):
    if hlist[i]>hlist[0]:
        print(i+1)
        exit()

# answer
print(-1)