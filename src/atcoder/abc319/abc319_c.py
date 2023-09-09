# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
# 0 1 2
# 3 4 5
# 6 7 8

def check(x,y):
    # vertical
    w=[]
    for i in range(3):
        if x!=i and used[i][y]==0:
            w.append(cmap[i][y])
    if len(w)>1 and w[0]==w[1]:
        return False
    # horizontal
    w=[]
    for i in range(3):
        if y!=i and used[x][i]:
            w.append(cmap[x][i])
    if len(w)>1 and w[0]==w[1]:
        return False
    if x==0 and y==0:
        if used[1][1]==1 and used[2][2]==1 and cmap[1][1]==cmap[2][2]:
            return False
    if x==1 and y==1:
        if used[0][0]==1 and used[2][2]==1 and cmap[0][0]==cmap[2][2]:
            return False
        if used[2][0]==1 and used[0][2]==1 and cmap[2][0]==cmap[0][2]:
            return False
    if x==2 and y==2:
        if used[1][1]==1 and used[0][0]==1 and cmap[1][1]==cmap[0][0]:
            return False
    if x==2 and y==0:
        if used[1][1]==1 and used[0][2]==1 and cmap[1][1]==cmap[0][2]:
            return False
    if x==0 and y==2:
        if used[1][1]==1 and used[2][0]==1 and cmap[1][1]==cmap[2][0]:
            return False
    return True

def search():
    all=True
    for u1 in used:
        if 0 in u1:
            all=False
            break
    if all:
        return 1
    else:
        ret=0
        for i in range(9):
            x=i//3
            y=i%3
            if used[x][y]==0:
                if check(x,y):
                    used[x][y]=1
                    ret+=search()
                    used[x][y]=0
    return ret

# param
cmap=[]
for i in range(3):
    cmap.append(list(map(int, input().split())))

used=[]
for i in range(3):
    used.append([0]*3)

ALL=9*8*7*6*5*4*3*2
ans = search()

print(ans/ALL)