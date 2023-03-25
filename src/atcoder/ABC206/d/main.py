n=int(input())
alist=list(map(int,input().split()))

# 1件の場合は無条件にOK
if len(alist)==1:
    print(0)
    exit()

# 違う列とその数字の組み合わせを求める
dmap={} # キー：数字、値：インデックス
nset=set([]) # 違う位置全体を示すセット
for i in range(n//2):
    a1=alist[i]
    a2=alist[len(alist)-i-1]
    if a1!=a2:
        nset.add(i)
        if a1 not in dmap.keys():
            dmap[a1]=[]
        dmap[a1].append(i)
        if a2 not in dmap.keys():
            dmap[a2]=[]        
        dmap[a2].append(i)


dmap2={}
for k,v in dmap.items():
    dmap2[k]=len(v)
dlist=sorted(dmap2.items(),key=lambda i:i[1])
#print(dlist)
cnt=0
for k,v in dlist:
    if len(nset)==0:
        print(cnt)
        exit()
    vals=dmap[k]
    print(nset)
    for v in vals:
        if v in nset:
            nset.remove(v)
    cnt+=1