n,m=map(int,input().split())
alist=list(map(int,input().split()))
blist=[0]*m
for a in alist:
    blist[a-1]+=1
if min(blist)==0:
    print(0)
    exit()

for i in range(1,n+1):
    a=alist[-1*i]
    blist[a-1]-=1
    if blist[a-1]==0:
        print(i)
        exit()