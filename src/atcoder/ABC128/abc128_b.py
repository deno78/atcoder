n=int(input())
pdict={}
sp={}
slist=[]
for i in range(n):
    s,p=map(str,input().split())
    if s not in sp.keys():
        sp[s]=[]
        slist.append(s)
    sp[s].append(int(p))
    pdict[int(p)]=i+1

slist.sort()
for s in slist:
    plist=sp[s]
    plist.sort(reverse=True)
    for p in plist:
#        print("{} {} {}".format(s,p,pdict[p]))
        print(pdict[p])