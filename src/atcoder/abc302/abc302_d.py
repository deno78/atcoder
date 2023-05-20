# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n,m,d = map(int, input().split())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

alist.sort()
blist.sort()

# solve
ans=-1
i=-1
j=-1
di=i
dj=j
while True:
    a=alist[i]
    b=blist[j]
#    print("{} {} {} {}".format(a,i,b,j))
    if abs(a-b)<=d:
        print(a+b)
        exit()
    else:
        if a < b:
            j=bisect.bisect_right(blist,a+d)-1
#            print("{}<- {} = {}".format(blist,a,j))
            j=min(j,m-1)
        else:
            i=bisect.bisect_right(alist,b+d)-1
#            print("{}<- {} = {}".format(alist,b,i))
            i=min(i,n-1)
    if i==di and j==dj:
        break
    di=i
    dj=j

# answer
print(-1)