import sys
input=sys.stdin.readline

def solve():
    x,y,k=map(int,input().split())
    if x==y:
        print(0)
        return
    def get_anc(v):
        anc=[]
        while v>0:
            anc.append(v)
            v//=k
        anc.append(0)
        return anc
    ax=get_anc(x)
    ay=get_anc(y)
    dx=len(ax)-1
    dy=len(ay)-1
    ix=iy=0
    steps=0
    if dx>dy:
        diff=dx-dy
        steps+=diff
        ix=diff
    else:
        diff=dy-dx
        steps+=diff
        iy=diff
    while ax[ix]!=ay[iy]:
        ix+=1
        iy+=1
        steps+=2
    print(steps)

t=int(input())
for _ in range(t):
    solve()
