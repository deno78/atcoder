# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
alist.sort()
# solve
for i in range(1,n):
    if alist[i-1]+1 != alist[i]:
        print(alist[i]-1)
        exit()
