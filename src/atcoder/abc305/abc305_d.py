# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from bisect import bisect_left

# param
n = int(input())
alist=list(map(int,input().split()))
q=int(input())
lr=[]
for i in range(q):
    l,r = map(int, input().split())
    lr.append([l,r])

# solve
bdict={}
wk=0
bdict[0]=0
for i in range(1,n):
    if i%2==0:
        wk+=alist[i]-alist[i-1]
    bdict[alist[i]]=wk

for l,r in lr:
    val_l=0
    val_r=0
    idx_l = bisect_left(alist,l)
    idx_r = bisect_left(alist,r)
    al=alist[idx_l]
    ar=alist[idx_r-1]
    val_l=bdict[al]
    val_r=bdict[ar]
    t1=0
    t2=0
    if idx_l%2==0:
        t1=al-l
    if idx_r%2==0:
        t2=r-ar
#    print("{} {}  {} {} {}".format(al,ar,(val_r-val_l),t1,t2))
    print(val_r-val_l+t1+t2)