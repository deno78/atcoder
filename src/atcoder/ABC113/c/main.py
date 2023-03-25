n,m=map(int,input().split())
pylist=[]
pymap={}
for i in range(m):
    p,y=map(int,input().split())
    pylist.append(str(p)+"-"+str(y))
    if p not in pymap.keys():
        pymap[p]=[]
    pymap[p].append(y)

pymap2={}
for p in sorted(pymap.keys()):
    ylist=sorted(pymap[p])
    for i in range(len(ylist)):
        y=ylist[i]
        py=str(p) + "-" + str(y)
        code="{:0>6}{:0>6}".format(p,i+1)
        pymap2[py]=code

for py in pylist:
    print(pymap2[py])
