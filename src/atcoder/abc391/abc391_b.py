# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
smap=[]
for i in range(n):
    smap.append(list(input()))
tmap=[]
for i in range(m):
    tmap.append(list(input()))

# solve
for a in range(n-m+1):
    for b in range(n-m+1):
        ok=True
        for i in range(m):
            for j in range(m):
                if smap[a+i][b+j]!=tmap[i][j]:
                    ok=False
                    break
        if ok:
            print("{} {}".format(a+1,b+1))
            exit()
                