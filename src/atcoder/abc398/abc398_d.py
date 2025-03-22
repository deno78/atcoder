n,r,c=map(int,input().split())
s=input()

bx=0
by=0

wk=[]

DDICT={}
DDICT["N"]=[-1,0]
DDICT["W"]=[0,-1]
DDICT["S"]=[1,0]
DDICT["E"]=[0,1]

wk={}
wk[0]={}
wk[0][0]=1

ans=[]

for i in range(n):
    d=DDICT[s[i]]
    r-=d[0]
    c-=d[1]
    by-=d[0]
    bx-=d[1]
    a="0"
    if by not in wk.keys():
        wk[by]={}
    wk[by][bx]=1
    if r in wk.keys() and c in wk[r].keys() and wk[r][c]==1:
        a="1"
#    print(wk)
    ans.append(a)

print("".join(ans))
