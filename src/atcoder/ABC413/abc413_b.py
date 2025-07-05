n=int(input())
slist=[]
for i in range(n):
    slist.append(input())

sset=set([])
for i in range(n):
    for j in range(n):
        if i!=j:
            s1=slist[i]
            s2=slist[j]
            sset.add(s1+s2)

print(len(sset))