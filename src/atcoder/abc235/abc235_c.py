# TODO edit the code

# param
n,q = map(int,input().split())
alist=list(map(int,input().split()))
qlist=[]
for _ in range(q):
    qlist.append(list(map(int,input().split())))

ndic={}
for i in range(n):
    a=alist[i]
    if a not in ndic.keys():
        ndic[a]=[]
    ndic[a].append(i)

# solve

for x,k in qlist:
    if x in ndic.keys():
        nlist=ndic[x]
        if k<len(nlist)+1:
            y=nlist[k-1]
            print(y+1)
        else:
            print(-1)
    else:
        print(-1)
