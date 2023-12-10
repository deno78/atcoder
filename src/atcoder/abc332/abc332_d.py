# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
amap=[]
for i in range(h):
    amap.append(input().split())
bmap=[]
for i in range(h):
    bmap.append(input().split())

# solve
ans=0
wk1=set([])
wk2=set([])
for i in range(h):
    al="-".join(sorted(amap[i]))
    for j in range(h):
        bl="-".join(sorted(bmap[j]))
        if al==bl:
            wk1.add(i-j)
            for k in range(w):
                a=amap[i][k]
                for l in range(w):
                    b=bmap[j][l]
                    if a==b:
                        wk2.add(k-l)

print(wk1)

print(wk2)
# answer
print("{}".format(ans//2))
