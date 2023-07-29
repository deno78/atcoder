# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
slist=[]
for i in range(n):
    slist.append(input())

# solve
ans=[]
for x1 in range(n-8):
    for y1 in range(m-8):
        ok = True
        for x,y in [[x1,y1],[x1+6,y1+6]]:
            for i in range(3):
                for j in range(3):
                    if slist[x+i][y+j]!= "#":
                        ok=False
                        break
        if ok:
            for i in range(4):
                if slist[x1+i][y1+3]!=".":
                    ok=False
                    break
            for i in range(4):
                if slist[x1+3][y1+i]!=".":
                    ok=False
                    break
            for i in range(4):
                if slist[x1+5+i][y1+5]!=".":
                    ok=False
                    break
            for i in range(4):
                if slist[x1+5][y1+5+i]!=".":
                    ok=False
                    break
        if ok==True:
            ans.append([x1,y1])

for x,y in ans:
    print("{} {}".format(x+1,y+1))