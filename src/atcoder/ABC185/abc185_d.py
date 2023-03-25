import math
nm = input('').split()
n = int(nm[0])
m = int(nm[1])

alist = list(map(int,input('').split()))
alist.sort()
alist.append(n+1)
blist=[]
pos=1
for a in alist:
    if a-pos > 0:
        blist.append(a-pos)
    pos=a+1

#print(blist)

if len(blist) == 0:
    print(0)
else:
    sz=min(blist)
    cnt=0
    for p in blist:
        if p>0:
            rec=math.ceil(p/sz)
            cnt+=rec
#            print("p:{} sz:{} ->cnt+={}".format(p,sz,rec))
    print(cnt)