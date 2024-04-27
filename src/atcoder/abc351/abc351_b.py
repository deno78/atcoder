# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
amap=[]
bmap=[]
for i in range(n):
    amap.append(list(input()))
for i in range(n):
    bmap.append(list(input()))


# solve
for i in range(n):
    for j in range(n):
        if amap[i][j]!=bmap[i][j]:
            print("{} {}".format(i+1,j+1))
            exit()

