# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def check(x,y,hist):
    ret=0
    if len(hist)==k+1:
#        print(hist)
        return 1
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x2=x+dx
        y2=y+dy
        xy="{},{}".format(x2,y2)
        if 0<=x2 and x2<w and 0<=y2 and y2<h:
            if s[y2][x2]=="." and xy not in hist:
                hist.append(xy)
                ret+=check(x2,y2,hist)
                hist.pop(-1)
    return ret

# param
h,w,k = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

# solve
wk=[]
for x in range(w):
    for y in range(h):
        if s[y][x]==".":
            xy="{},{}".format(x,y)
            wk.append([x,y,[xy]])
ans=0
for x,y,hist in wk:
    ans+=check(x,y,hist)

print(ans)