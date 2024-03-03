# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
alist=list(map(int,input().split()))
query=[]
for i in range(q):
    query.append(input().split())

alist2=[]
adict2={}
alist2.append({})
for i in range(n):
    a=alist[i]
    if a not in adict2.keys():
        adict2[a]=0
    adict2[a]+=1
    alist2.append(adict2.copy())

adict3={}

# solve
for i in range(q):
    q=query[i]
    if q[0]=="1":
        p=int(q[1])-1
        x=int(q[2])
        a=alist[p]
        if p not in adict3.keys():
            adict3[p]=[]
        adict3[p].append([a,x])
        alist[p]=x
        # for d in alist2:
        #     print("[{}]\t{}".format(i,d))
    else:
        l=int(q[1])-1
        r=int(q[2])
        wk={}
        for k,v in alist2[r].items():
            wk[k]=v
        for k,v in alist2[l].items():
            if k in wk.keys():
                wk[k]-=v
        for k,v in adict3.items():
            if l<=k and k<=r:
                for j in range(len(v)):
                    p,x = v[j]
                    if p in wk.keys():
                        wk[p]-=1
                    if x in wk.keys():
                        wk[x]+=1
        ary=[]
        for k,v in wk.items():
            if v>0:
                ary.append(k)
        ary.sort(reverse=True)
        if len(ary)<2:
            print(0)
        else:
            print(wk[ary[1]])




