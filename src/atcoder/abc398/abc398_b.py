alist=list(map(int,input().split()))

d={}
for a in alist:
    if a not in d.keys():
        d[a]=0
    d[a]+=1

ok1=False
ok2=False
for k,v in d.items():
    if v>=3:
        if ok1==False:
            ok1=True
        else:
            ok2=True
    elif v>=2:
        ok2=True

if ok1 and ok2 :
    print("Yes")
else:
    print("No")