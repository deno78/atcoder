# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
m=[]
for i in range(h):
    m.append(list(input()))

# solve
for y in range(h):
    for x in range(w):
        cnt=0
        if m[y][x]==".":
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                x1=x+dx
                y1=y+dy
                if y1 >=0 and x1>=0 and y1<h and x1<w:
                    if m[y1][x1]=="#":
                        cnt+=1
#            print("{} {} {}".format(x,y,cnt))
            if cnt > 1:
                print("{} {}".format(y+1,x+1))
                exit(0)
