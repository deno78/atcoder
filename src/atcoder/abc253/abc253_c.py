# TODO edit the code

# param
q = int(input())
qlist=[]
for i in range(q):
    qlist.append(input().split())

# solve
sdic={}
smax=-1
smin=10**9
for q in qlist:
#    print("{}/{}".format(smin,smax))
    if q[0]=="1":
        x=int(q[1])
        if x not in sdic.keys():
            sdic[x]=0
            if x >= smax:
                smax=x
            if x <= smin:
                smin=x
        sdic[x]+=1
    elif q[0]=="2":
        x=int(q[1])
        c=int(q[2])
        if x in sdic.keys():
            sdic[x]= sdic[x] - c
            if sdic[x] <= 0:
                sdic.pop(x,None)
                if smax==x:
                    smax=max(sdic.keys(),default=0)
                if smin==x:
                    smin=min(sdic.keys(),default=10**9)
    elif q[0]=="3":
        print(smax-smin)
