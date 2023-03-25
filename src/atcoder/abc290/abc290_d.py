# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def makelist(x,y):
    z=0
    ret=[0]
    flg=[0]*x
    flg[0]=1
    for i in range(n-1):
        z=(z+y)%x
        if 0 in flg[z:]:
            z=z+flg[z:].index(0)
        elif 0 in flg[:z]:
            z=flg.index(0)
        else:
            break
        flg[z]=1
        ret.append(z)
    return ret

# param
t = int(input())
tlist=[]
ndxdict={}
for i in range(t):
    n,d,k=map(int,input().split())
    nd="{}/{}".format(n,d)
    tlist.append([nd,k])
    if nd not in ndxdict.keys():
        xlist=makelist(n,d)
        ndxdict[nd]=xlist

for nd,k in tlist:
    xlist=ndxdict[nd]
    ix=(k-1)%len(xlist)
    print(xlist[ix])
