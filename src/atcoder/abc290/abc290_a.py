# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

# solve

ans=0
for i in range(m):
    b=blist[i]-1
    ans+=alist[b]

# answer
print(ans)
