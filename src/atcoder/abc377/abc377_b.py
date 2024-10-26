# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
smap=[]
for i in range(8):
    s=list(input())
    smap.append(s)

xflags=[]
yflags=[]

for i in range(8):
    if "#" in smap[i]:
        yflags.append(i)
        for j in range(8):
            if smap[i][j]=="#":
                xflags.append(j)

ans=0
for i in range(8):
    for j in range(8):
        if i not in xflags and j not in yflags:
            ans+=1

# answer
print("{}".format(ans))
