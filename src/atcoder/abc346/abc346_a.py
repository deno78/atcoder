# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
ans=[]

for i in range(n-1):
    ans.append(str(alist[i]*alist[i+1]))

# answer
print(" ".join(ans))
