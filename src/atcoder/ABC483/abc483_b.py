n,q=map(int,input().split())
klist=list(map(int,input().split()))

alist=[]
blist=[]
for i in range(n):
    alist.append(str(i+1))
    blist.append(0)

for k in klist:
    wk=[]
    wk2=[]
    for i in range(k):
        wk.append(alist.pop(0))
        wk2.append((blist.pop(0)+1)%2)
    for i in range(k):
        alist.insert(0,wk.pop(0))
        blist.insert(0,wk2.pop(0))
#    print(alist)
#    print(blist)

for i in range(n):
    if blist[i]==0:
        print(alist[i])
    else:
        print("-"+alist[i])