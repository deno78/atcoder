
import heapq

# TODO edit the code

# param
n,k = map(int,input().split())
plist=list(map(int,input().split()))
ans=[]
alist=[]

alist=plist[0:k-1]
heapq.heapify(alist)
t=0
for i in range(k-1,n):
#    print("{}:{}".format(plist[i],alist))
    heapq.heappush(alist,plist[i])
    t2=heapq.heappop(alist)
    t=max(t,t2)

    ans.append(t)

# answer
for a in ans:
    print(a)
