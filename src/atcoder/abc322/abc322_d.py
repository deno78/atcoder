# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
p1=[]
p2=[]
p3=[]

for i in range(4):
    p1.append(list(input()))
for i in range(4):
    p2.append(list(input()))
for i in range(4):
    p3.append(list(input()))

# solve
g1=[]
g2=[]
g3=[]
for i in range(4):
    for j in range(4):
        if p1[i][j]=="#":
            g1.append([i,j])
        if p2[i][j]=="#":
            g2.append([i,j])
        if p3[i][j]=="#":
            g3.append([i,j])


g2a=[]
g2b=[]
g2c=[]
for x,y in g2:
    g2a.append([3-y,x])
    g2b.append([3-x,3-y])
    g2c.append([y,3-x])

g3a=[]
g3b=[]
g3c=[]
for x,y in g3:
    g3a.append([3-y,x])
    g3b.append([3-x,3-y])
    g3c.append([y,3-x])

for g2x in [g2,g2a,g2b,g2c]:
    for g3x in [g3,g3a,g3b,g3c]:
        for x1 in range(7):
            for y1 in range(7):
                for x2 in range(7):
                    for y2 in range(7):
                        for x3 in range(7):
                            for y3 in range(7):
                                ans=[]
                                for i in range(10):
                                    ans.append([0]*10)
                                for x,y in g1:
                                    ans[x+x1][y+y1]+=1
                                for x,y in g2x:
                                    ans[x+x2][y+y2]+=1
                                for x,y in g3x:
                                    ans[x+x3][y+y3]+=1
                                ok=True
                                for i in range(10):
                                    for j in range(10):
                                        if (i>=3 and i<=6) and (j>=3 and j<=6):
                                            if ans[i][j]==0:
                                                ok=False
                                                break
                                            elif ans[i][j]>1:
                                                ok=False
                                                break
                                        else:
                                            if ans[i][j]>0:
                                                ok=False
                                                break
                                    if ok==False:
                                        break
                                if ok:
                                    print("Yes")
                                    exit()
print("No")
