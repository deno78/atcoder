n,k=map(int,input().split())
alist=list(map(int,input().split()))

all=sum(alist)
kdict={}
for i in range(n):
    a=alist[i]
    if a not in kdict.keys():
        kdict[a]=0
    kdict[a]+=1

klist=[]
for key,val in kdict.items():
    klist.append(key*val)
klist.sort(reverse=True)
print(all-sum(klist[:k]))