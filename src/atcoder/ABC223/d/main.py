n,m=map(int,input().split())
abdic={}
for i in range(m):
    a,b=map(int,input().split())
    if b not in abdic.keys():
        abdic[b]=[]
    abdic[b].append(a)
    if a in abdic.keys() and b in abdic[a]:
        print(-1)
        exit()

#print(abdic)
nlist=[]
for i in range(1,n+1):
    if i in abdic.keys():
        blist=abdic[i]
        blist.sort()
        for b in blist:
            if b not in nlist:
                nlist.append(b)
        nlist.append(i)
    else:
        if i not in nlist:
            nlist.append(i)

slist=[str(n) for n in nlist]
print(" ".join(slist))