# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def calc(x,y,dx,dy):
    x2=x+dx
    y2=y+dy
    x2=max(x2,0)
    y2=max(y2,0)
    x2=min(x2,n-1)
    y2=min(y2,n-1)
    if smap[y2][x2]=="#":
        x2=x
        y2=y
    return [x2,y2]


# param
n = int(input())
smap=[]
p=[]
for i in range(n):
    s = input()
    smap.append(list(s))

for i in range(n):
    for j in range(n):
        if smap[j][i]=="P":
            p.append(i)
            p.append(j)

ans=[]
for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
    for dx2,dy2 in [[-1,0],[1,0],[0,-1],[0,1]]:
        if dx!=dx2 and dy!=dy2:
#            print("{} {} {} {}".format(dx,dy,dx2,dy2))
            x1=p[0]
            y1=p[1]
            x2=p[2]
            y2=p[3]
            flg=False
            c=0
            while (x1!=x2 or y1!=y2):
                if flg==False:
                    x12,y12=calc(x1,y1,dx,dy)
                    x22,y22=calc(x2,y2,dx,dy)
                else:
                    x12,y12=calc(x1,y1,dx2,dy2)
                    x22,y22=calc(x2,y2,dx2,dy2)
#                print("{} {} {} {}".format(x12,y12,x22,y22))
                c+=1
                if flg==False and (x12==x22 or y12==y22):
                    flg=True
                if x12==x22 and y12==y22:
                    break
                if x1==x12 and x2==x22 and y1==y12 and y2==y22:
                    c=-1
                    break
                x1=x12
                y1=y12
                x2=x22
                y2=y22
            ans.append(c)
# solve
# answer
if max(ans)==-1:
    print(-1)
else:
    ans2=[]
    for a in ans:
        if a>0:
            ans2.append(a)
    print(min(ans2))
