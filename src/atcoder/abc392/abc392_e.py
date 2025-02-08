# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
abdict={}
for i in range(m):
    a,b = map(int, input().split())
    a-=1
    b-=1
    if a not in abdict.keys():
        abdict[a]=[]
    if b not in abdict.keys():
        abdict[b]=[]
    abdict[a].append(b)
    abdict[b].append(a)

# solve
nlist=[-1]*n
bdict={}

for i in range(n):
    if nlist[i]==-1:
        wk=[i]
        nlist[i]=i
        while len(wk)>0:
            w=wk.pop(0)
            if w in abdict.keys():
                for b in abdict[w]:
                    if nlist[b]==-1:
                        nlist[b]=i
                        wk.append(b)
                    else:
                        if i not in bdict.keys():
                            bdict[i]=[]
                        wb="{}={}".format(w,b)
                        if wb not in bdict[i]:
                            bdict[i].append(wb)

print(nlist)
print(bdict)
