# TODO edit the code

# param
n = int(input())
slist=[]

for i in range(n):
    slist.append(input())

# solve
ans = float('INF')
nmap={}
for i in range(10):
    nmap[i]=[]
for i in range(10):
    clist=[0]*10
    for s in slist:
        t=0
        p=s.index(str(i))
        c=clist[p]
        nmap[i].append(p + c*10 )
        clist[p]+=1
#print(nmap)
for k,v in nmap.items():
    v.sort()
    a1=v[0]
    t=a1
    for i in range(1,len(v)):
        a2=v[i]
        t+=a2-a1
        a1=a2
    ans=min(ans,t)

# answer
print(ans)
