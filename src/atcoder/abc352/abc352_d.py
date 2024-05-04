# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,k = map(int, input().split())
plist = list(map(int, input().split()))

pdict={}
for i in range(n):
    p=plist[i]
    pdict[p]=i

# solve
ans=0
i1=float("INF")
ik=0
wk=deque()
for i in range(1,k+1):
    i1=min(i1,pdict[i])
    ik=max(ik,pdict[i])
    wk.append(pdict[i])
ans=ik-i1
# print("{} {}-{} [{}]".format(wk,i1,ik,ans))

for i in range(1,n-k+1):
    ip=wk.popleft()
    i2=pdict[i+k]
    wk.append(i2)
    if ip==i1:
        i1=min(wk)
    elif ip==ik:
        ik=max(wk)
    if i2<i1:
        i1=i2
    elif i2>ik:
        ik=i2
    ans=min(ans,(ik-i1))
#    print("{} {}-{}".format(wk,i1,ik))
# answer
print(ans)