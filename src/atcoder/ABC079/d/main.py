h,w = map(int,input().split())

alist=[]
clist=[]
for i in range(10):
    clist.append(list(map(int,input().split())))
for i in range(h):
    alist.append(list(map(int,input().split())))


for k in range(10):
    for i in range(10):
        for j in range(10):
            if i!=j:
                clist[i][j]=min(clist[i][k]+clist[k][j],clist[i][j])

ans=0
for a in alist:
    for n in a:
        if n!=-1 and n!=1:
            ans+=clist[n][1]
print(ans)
