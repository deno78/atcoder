# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
nlist=list(map(int,input().split()))
nlist.sort()

# solve
ans=sum(nlist[n:-1*n])/(3*n)

# answer
print(ans)
