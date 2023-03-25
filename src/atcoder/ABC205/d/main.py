def is_ok(arg,k):
    if blist[arg][0] <= k and blist[arg][1] > k:
        return True
    else:
        return False

def bisect(ng,ok,k):
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if is_ok(mid,k):
            ok=mid
        else:
            ng=mid
    return ok

nq=input().split()
n=int(nq[0])
q=int(nq[1])

alist=list(map(int,input().split()))
alist.sort()

blist=[]
blist.append([0,alist[0]])
for i in range(1,len(alist)-1):
    blist.append([alist[i-1],alist[i]])
print(blist)

for i in range(q):
    k=int(input())
    ans= bisect(0,len(blist),k)
    print("k:{} blist:{} ans:{}".format(k,blist,ans))
    print(ans)
