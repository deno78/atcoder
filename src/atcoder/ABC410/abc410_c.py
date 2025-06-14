n,q=map(int,input().split())
query=[]
for i in range(q):
    query.append(input().split())

alist=[]
for i in range(n):
    alist.append(i+1)

zero=0
for q in query:
    if q[0]=="1":
        p=int(q[1])-1
        x=int(q[2])
        idx=(zero+p)%n
        alist[idx]=x
    elif q[0]=="2":
        p=int(q[1])-1
        idx=(zero+p)%n
        print(alist[idx])
    elif q[0]=="3":
        k=int(q[1])
        zero+=k
        zero%=n
