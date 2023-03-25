# TODO edit the code

# param
h,w=map(int,input().split())
slist=[]
for i in range(h):
    slist.append(list(input()))

# solve
xylist=[]
for x in range(h):
    for y in range(w):
        if slist[x][y]=='o':
            xylist.append([x,y])

ans=abs(xylist[0][0] - xylist[1][0]) + abs(xylist[0][1] - xylist[1][1])

# answer
print(ans)
