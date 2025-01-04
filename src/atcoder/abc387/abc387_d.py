# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
slist1=[]
slist2=[]
start=[]
goal=[]
for i in range(h):
    s=input()
    if "S" in s:
        start=[i,s.index("S")]
    if "G" in s:
        goal=[i,s.index("G")]
    slist1.append(list(s))
    slist2.append(list(s))

# solve
ans=0
#print(start)
#print(goal)
x1=start[0]
y1=start[1]
x2=goal[0]
y2=goal[1]
slist1[x1][y1]=0
slist2[x1][y1]=0
ans=float("INF")
for direction in [0,1]:
    if direction==0:
        wlist=slist1
    else:
        wlist=slist2
    wlist[x1][y1]=0
    wk=[]
    wk.append(start)
    while len(wk)>0:
#        print(wk)
        now=wk.pop(0)
        if now==goal:
            break
        x=now[0]
        y=now[1]
        step=wlist[x][y]
        if step%2==direction:
            for dx,dy in [[1,0],[-1,0]]:
                if x+dx>=0 and x+dx<h and y+dy>=0 and y+dy<w and (wlist[x+dx][y+dy]=="." or wlist[x+dx][y+dy]=="G"):
                    wk.append([x+dx,y+dy])
                    wlist[x+dx][y+dy]=step+1
        else:
            for dx,dy in [[0,1],[0,-1]]:
                if x+dx>=0 and x+dx<h and y+dy>=0 and y+dy<w and (wlist[x+dx][y+dy]=="." or wlist[x+dx][y+dy]=="G"):
                    wk.append([x+dx,y+dy])
                    wlist[x+dx][y+dy]=step+1
#    print(wlist[x2][y2])
    if wlist[x2][y2]!="G":
        ans=min(ans,wlist[x2][y2])

# answer
if ans==float("INF"):
    print(-1)
else:
    print("{}".format(ans))
