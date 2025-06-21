n=int(input())
dlist=list(map(int,input().split()))

slist=[]
slist.append(0)
t=0
for i in range(n-1):
    t+=dlist[i]
    slist.append(t)

for i in range(n-1):
    wk=[]
    for j in range(i+1,n):
        d1=slist[i]
        d2=slist[j]
        wk.append(d2-d1)
    print(" ".join(map(str,wk)))
