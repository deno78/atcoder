

nq=input().split()
n=int(nq[0])
q=int(nq[1])

abdic={}
badic={}
for i in range(n):
    abdic[i]=set([i])

for i in range(n-1):
    ab=list(map(int,input().split()))
    a=ab[0]-1
    b=ab[1]-1
    abdic[a].add(b)
    badic[b]=a

pxdic={}
for i in range(q):
    px=list(map(int,input().split()))
    p=px[0]-1
    x=px[1]
    if p not in pxdic.keys():
        pxdic[p]=0
    pxdic[p]+=x

#print(abdic)
for a in sorted(badic.keys(),reverse=True):
    b = badic[a]
    abdic[b].update(abdic[a])

#print(abdic)
scores=[0]*n
for p,x in pxdic.items():
    for i in abdic[p]:
        scores[i]+=x

result=""
for s in scores:
    result += str(s) + " "
print(result)
