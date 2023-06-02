n,k,q=map(int,input().split())

alist=[]
for i in range(q):
    alist.append(int(input()))

nlist=[0]*n

for a in alist:
    nlist[a-1]+=1
for i in nlist:
    if i+k>q:
        print('Yes')
    else:
        print('No')