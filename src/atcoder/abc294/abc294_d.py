import heapq

n,q=map(int,input().split())

q1=1
q2=[]
heapq.heapify(q2)
dlist=[]
for i in range(q):
    ev=input().split()
    if ev[0]=="1":
        heapq.heappush(q2,q1)
        q1+=1
    elif ev[0]=="2":
        x=int(ev[1])
        dlist.append(x)
    elif ev[0]=="3":
        for i in range(len(q2)):
            if q2[i]
        print(min(q2))
