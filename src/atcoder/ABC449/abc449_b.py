h,w,q=map(int,input().split())
queries=[]
for i in range(q):
    queries.append(list(map(int,input().split())))

for query in queries:
    if query[0]==1:
        r=query[1]
        print(r*w)
        h-=r
    elif query[0]==2:
        c=query[1]
        print(c*h)
        w-=c
#    print("#",h,w)