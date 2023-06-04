# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from bisect import bisect_left

# param
w,h = map(int, input().split())
n=int(input())
pq=[]
for i in range(n):
    p,q=map(int,input().split())
    pq.append([p,q])

a=int(input())
alist=list(map(int,input().split()))
b=int(input())
blist=list(map(int,input().split()))

# solve
ans={}
c=0
M=0
m=float("INF")
for p,q in pq:
    x=bisect_left(alist,p)
    y=bisect_left(blist,q)
    if y not in ans.keys():
        ans[y]={}
    if x not in ans[y].keys():
        ans[y][x]=0
        c+=1
    ans[y][x]+=1

for v1 in ans.values():
    M=max(max(v1.values()),M)
    m=min(min(v1.values()),m)

if c<((a+1)*(b+1)):
    m=0

# answer
print("{} {}".format(m,M))