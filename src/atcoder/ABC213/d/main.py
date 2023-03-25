import heapq

n=int(input())
route={}
for i in range(1,n+1):
    route[i]=[]

for i in range(n-1):
    a,b=map(int,input().split())
    route[a].append(b)
    route[b].append(a)

for v in route.values():
    v.sort()

v=[0]*n
v[0]=-1
p=1
passed=[]

while True:
    passed.append(str(p))
#    print(route)
    if p==1 and len(route[p])==0:
        break

    if len(route[p])>0:
        n=route[p][0]
        v[n-1]=p
        route[p].remove(n)
        route[n].remove(p)
        p=n
    else:
        p=v[p-1]

print(" ".join(passed))
