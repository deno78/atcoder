# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
smap=[]
for i in range(h):
    smap.append(input())

# solve
bx1=h
bx2=0
by1=w
by2=0
whites=[]
for y in range(h):
    for x in range(w):
        if smap[y][x]=="#":
            bx1=min(bx1,x)
            bx2=max(bx2,x)
            by1=min(by1,y)
            by2=max(by2,y)
        elif smap[y][x]==".":
            whites.append([x,y])
#print("{}-{},{}-{}".format(bx1,bx2,by1,by2))
#print(whites)
for x,y in whites:
    if bx1<=x and x<=bx2 and by1<=y and y<=by2:
#       print("{},{} is bad.".format(x,y))
        print("No")
        exit(0)

print("Yes")