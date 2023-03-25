n=int(input())
alist=list(map(int,input().split()))
q=int(input())
queries=[]
for i in range(q):
    queries.append(list(map(int,input().split())))

for query in queries:
    mode=query[0]
    if mode==1:
        k=query[1]-1
        x=query[2]
        alist[k]=x
    elif mode==2:
        k=query[1]-1
        print(alist[k])

