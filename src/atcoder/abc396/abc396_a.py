# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
for i in range(n-2):
    a1 = alist[i]
    a2 = alist[i+1]
    a3 = alist[i+2]
    if a1==a2 and a2==a3:
        print("Yes")
        exit()

# answer
print("No")