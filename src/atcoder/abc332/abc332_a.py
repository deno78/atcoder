# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,s,k = map(int, input().split())
pq = []
for i in range(n):
    p,q=map(int,input().split())
    pq.append([p,q])

# solve
ans = 0
for i in range(n):
    p,q=pq[i]
    ans+=p*q


# answer
if ans>=s:
    print(ans)
else:
    print(ans+k)
