# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
amap=[]
for i in range(9):
    amap.append(list(map(int,input().split())))

# solve
ok=True
for i in range(9):
    if len(set(amap[i]))!=9:
        print("No")
        exit()

for i in range(9):
    wk=[]
    for j in range(9):
        wk.append(amap[j][i])
    if len(set(wk))!=9:
        print("No")
        exit()

for i in range(9):
    wk=[]
    wk2=[]
    x=(i%3)*3
    y=(i//3)*3
    for j in range(3):
        for k in range(3):
            wk.append(amap[x+j][y+k])
    if len(set(wk))!=9:
        print("No")
        exit()


# answer
print("Yes")
