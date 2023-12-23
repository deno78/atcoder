# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect


# param
n,q = map(int, input().split())
rlist =list(map(int,input().split()))
qlist=[]
for i in range(q):
    qlist.append(int(input()))

# solve
rlist.sort()
rlist2=[]
rlist2.append(0)
wk=0
for i in range(n):
    wk+=rlist[i]
    rlist2.append(wk)


# answer
for q in qlist:
    idx = bisect.bisect_right(rlist2,q)
    print(idx-1)
