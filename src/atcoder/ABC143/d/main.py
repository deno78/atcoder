import bisect

n=int(input())
llist=list(map(int,input().split()))
llist.sort()

#print(llist)
ans=0
for i in range(n):
    for j in range(i+1,n):
        idx=bisect.bisect_left(llist,llist[i]+llist[j])
        #print("[{}-{}]->{}".format(i,j,idx))
        ans+=max(0,idx-j-1)

print(ans)