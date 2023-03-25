n,k=map(int,input().split())
clist=list(map(int,input().split()))

d={}
for i in range(k):
    c=clist[i]
    if c in d.keys():
        d[c]+=1
    else:
        d[c]=1

cnt=len(d.keys())
if n==k:
    print(len(d.keys()))
    exit()

for i in range(1,n-k+1):
    c1=clist[i-1]
    c2=clist[i+k-1]
    if d[c1]==1:
        del d[c1]
    else:
        d[c1]-=1
    if c2 in d.keys():
        d[c2]+=1
    else:
        d[c2]=1
#    print("[{}] c1:{},c2:{} =>{}".format(i,c1,c2,d))
    cnt=max(cnt,len(d.keys()))

print(cnt)
