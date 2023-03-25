from collections import deque,Counter

n,m=map(int,input().split())

alist=[]
for i in range(m):
    k=input()
    alist.append(list(map(int,input().split())))
aidx=[0]*m

nidx=[-1]*(n+1)

while n>0:
    ok=False
    for i in range(m):
        if aidx[i]<len(alist[i]):
            a1=alist[i][aidx[i]]
            if nidx[a1]==-1:
                nidx[a1]=i
            elif nidx[a1]==i:
                pass
            else:
                i2=nidx[a1]
                aidx[i]+=1
                aidx[i2]+=1
                n-=1
                ok=True
                break
    if ok==False:
        print('No')
        exit()

print('Yes')