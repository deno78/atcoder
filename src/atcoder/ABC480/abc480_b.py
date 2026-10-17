n,m=map(int,input().split())
slist=[]
sset=set()
for i in range(n):
    s=input()
    slist.append(s)
    sset.add(s)
tlist=[]
for i in range(m):
    tlist.append(input())

adict={}
for i in range(n):
    adict[slist[i]]=0

for i in range(m):
    t=tlist[i]
    if t in sset:
        adict[t]+=1
    else:
        matched=[]
        for j in range(n):
            if len(slist[j])==len(t):
                wrong=0
                for k in range(len(slist[j])):
                    if slist[j][k] != t[k]:
                        wrong+=1
                if wrong<=1:
                    matched.append(slist[j])
        if len(matched)==1:
            adict[matched[0]]+=1

for i in range(n):
    print(adict[slist[i]])