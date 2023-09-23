# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n,m,p = map(int, input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

blist.sort()
blist2=[]
wk=0
blist2.append(0)
for i in range(m):
    wk+=blist[i]
    blist2.append(wk)
# solve
ans=0
for i in range(n):
    a=alist[i]
    x=p-a
    idx=bisect.bisect(blist,x)
#    print("{} {} {}".format(blist2[idx-1],a*idx,(m-idx)*p))
    ans+=blist2[idx]+a*idx+(m-idx)*p

# answer
print("{}".format(ans))
