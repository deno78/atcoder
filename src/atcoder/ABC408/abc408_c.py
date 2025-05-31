n,m=map(int,input().split())
lr=[]
wset=set([1,n+1])
ldict={}
rdict={}
for i in range(m):
    l,r=map(int, input().split())
    wset.add(l)
    r+=1
    wset.add(r)
    if l not in ldict.keys():
        ldict[l]=0
    ldict[l]+=1
    if r not in rdict.keys():
        rdict[r]=0
    rdict[r]+=1

wlist=list(wset)
wlist.sort()
wlist2=[]
wk=0
for w in wlist:
    if w in ldict.keys():
        wk+=ldict[w]
    if w in rdict.keys():
        wk-=rdict[w]
    wlist2.append(wk)

#for i in range(len(wlist)):
#    print("{} {} {}".format(i,wlist[i],wlist2[i]))
print(min(wlist2[:-1]))
