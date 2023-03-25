import heapq

q=int(input())
a=[]
heapq.heapify(a)
up=0
for i in range(q):
    query=input().split()
    c=query[0]
    if c=='1':
        x=int(query[1])
        heapq.heappush(a,x-up)
    elif c=='2':
        up+=int(query[1])
    elif c=='3':
        b = heapq.heappop(a)
        print(b+up)
