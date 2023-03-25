import bisect
n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist=list(map(int,input().split()))

alist.sort()
blist.sort()
clist.sort()
ans=0
for b in blist:
    idx1=bisect.bisect_left(alist,b)
    idx2=bisect.bisect_right(clist,b)
    #print("a[{}] in {} -> {}".format(alist,b,idx1))
    #print("c[{}] in {} -> {}".format(clist,b,idx2))
    ans+=idx1*(n-idx2)

print(ans)