q=int(input())
qlist=[]
for i in range(q):
    qlist.append(list(map(int,input().split())))

ans=[]
for q in qlist:
    if q[0]==1:
        ans.append(q[1])
    elif q[0]==2:
        p=ans.pop(0)
        print(p)



