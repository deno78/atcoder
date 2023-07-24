n=int(input())
alist=list(map(int,input().split()))

adict={}
for i in range(n):
    adict[i]=[]
for i in range(n):
    a=alist[i]
    adict[i].append(a-1)

acheck=[0]*n
for i in range(n):
    wk=[]
    wk.append([i])
    while len(wk)>0:
        w=wk.pop(0)
        for x in adict[w[-1]]:
            if acheck[x]==0:
                acheck[x]=1
                if x==w[0]:
                    ans=[]
                    for y in w:
                        ans.append(str(y+1))
                    print(" ".join(ans))
                    exit()
                else:
                    if x not in w:
                        wk.append(w+[x])
