n=int(input())
slist=[]
for i in range(n):
    slist.append(input())

sdict={}
for s in slist:
    if s not in sdict.keys():
        sdict[s]=0
    sdict[s]+=1

ans=""
ansCount=0
for s,c in sdict.items():
    if ansCount<c:
        ans=s
        ansCount=c

print(ans)