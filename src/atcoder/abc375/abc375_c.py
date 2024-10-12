# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
amap=[]
for i in range(n):
    amap.append(list(input()))

# solve
c=(n//2+1)%4
for i in range(c):
    g2g=list(zip(*(amap[::-1])))    
    for x in range(i,n-i):
        for y in range(i,n-i):
            amap[x][y]=g2g[x][y]
    # print("[{}]--------------------".format(i))
    # for a in amap:
    #     print("".join(a))


# answer
for a in amap:
    print("".join(a))
