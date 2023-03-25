n=int(input())

xylist=[]
xdic={}

for i in range(n):
    x,y=map(int,input().split())
    if x not in xdic.keys():
        xdic[x]=[]
    xdic[x].append(y)
    xylist.append([x,y])

cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=xylist[i]
        x2,y2=xylist[j]
        if x1!=x2 and y1!=y2:
            if y2 in xdic[x1] and y1 in xdic[x2]:
                cnt+=1
print(cnt//2)
