# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
ab={}
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if a not in ab.keys():
        ab[a]=[]
    if b not in ab.keys():
        ab[b]=[]
    ab[a].append(b)
    ab[b].append(a)
vlist=list(map(int,input().split()))
vlist2=[]
for v in vlist:
    vlist2.append(v-1)
vlist=vlist2

# solve
v0=vlist[0]
wk=[]
wk.append([v0,[]])

hist=[0]*n
xset=set([])
xset.add(v0)
while len(wk)>0:
    w=wk.pop(0)
    w1=w[0]
    h=w[1]
    h.append(w1)
    hist[w1]=1
    if w1 in ab.keys():
        for a in ab[w1]:
            if hist[a]==0:
                if a in vlist:
                    for x in h:
                        xset.add(x)
                    xset.add(a)
    #                    print("Hit:{}".format(w+[a]))
                wk.append([a,h])
                hist[a]=1
#print(xset)
# answer
print("{}".format(len(xset)))
