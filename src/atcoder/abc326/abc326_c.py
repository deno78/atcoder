# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
# solve
adict={}
wk=0
for i in range(n):
    a=alist[i]
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1
alist2=list(adict.keys())
alist2.sort()
n2=len(alist2)
alist3=[0]
wk=0
for i in range(n2):
    a=alist2[i]
    wk+=adict[a]
    alist3.append(wk)

ans=0
for i in range(n2):
    a1=alist2[i]
    a2=a1+m
    i2=bisect.bisect_left(alist2,a2)
    w=alist3[i2]-alist3[i]
#    print("{}-{} : {}".format(a1,a2,w))
    ans=max(ans,w)

# answer
print(ans)
