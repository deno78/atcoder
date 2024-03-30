# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist = list(map(int, input().split()))

# solve
ans=[]
for i in range(n):
    a=alist[i]
    if a%k==0:
        ans.append(str(a//k))

# answer
print(" ".join(ans))
