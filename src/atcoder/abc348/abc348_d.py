# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
amap=[]
S=[]
E=[]
for i in range(h):
    a=list(input())
    amap.append(a)
    if "S" in a:
        S=[i,a.index("S")]   
n = int(input())
emap=[]
for i in range(h):
    emap.append([0]*w)
for i in range(n):
    r,c,e=map(int,input().split())
    r-=1
    c-=1
    emap[r][c]=e

# solve

wk=[]
wk.append([S[0],S[1],0])
while len(wk)>0:
    item=wk.pop(0)
    y=item[0]
    x=item[1]
    e=item[2]
    if e>0:
        amap[y][x]=e
        # print("X:{} Y:{} E:{}".format(x,y,e))
        # for a in amap:
        #     print(a)
        # print("----------------")
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            x2=x+dx
            y2=y+dy
            if 0<=x2 and x2<w and 0<=y2 and y2<h:
                p=amap[y2][x2]
                if p=="T":
                    print("Yes")
                    exit()
                elif p==".":
                    if emap[y][x]>0:
                        e=max(e-1,emap[y][x])
                        emap[y][x]==0
                    wk.append([y2,x2,e])
                elif p!="#":
                    if int(amap[y2][x2])<e-1 or emap[y][x]>0:
                        e2=max(int(amap[y2][x2]),e-1,emap[y][x])
                        wk.append([y2,x2,e2])


print("No")