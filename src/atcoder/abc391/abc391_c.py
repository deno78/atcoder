# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
qlist=[]
for i in range(q):
    qlist.append(input().split())

# solve
plist=[]
hdict={}
for i in range(n):
    plist.append(i)
for i in range(n):
    hdict[i]=[]
    hdict[i].append(i)

ans=0

for i in range(q):
    q=qlist[i]
    if q[0]=="1":
        p=int(q[1])-1
        h2=int(q[2])-1
        h1=plist[p]
        plist[p]=h2
        hdict[h2].append(p)
        hdict[h1].remove(p)
        if len(hdict[h2])==2:
            ans+=1
        if len(hdict[h1])==1:
            ans-=1
    elif q[0]=="2":
        print(ans)

