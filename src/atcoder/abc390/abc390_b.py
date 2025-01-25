# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
x=alist[1]/alist[0]
for i in range(2,n):
#    print("{} {}".format(i*x,alist[i]))
    if alist[i]!=x*alist[i-1]:
        print("No")
        exit(0)

# answer
print("Yes")