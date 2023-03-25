# TODO edit the code

n = int(input())
xyp=[]
for i in range(n):
    x,y,p=map(int,input().split())
    xyp.append([x,y,p])

# solve
ans=float('INF')
for i in range(n):
    s=0
    x1,y1,p1=xyp[i]
    for j in range(n):
        if i!=j:
            x2,y2,p2=xyp[j]
            d=abs(x1-x2)+abs(y1-y2)
            p=max(p1,p2)
            s=max(s,d//p)
            print("[{}-{}] d={} p={},{} s=({},{})".format(i,j,d,p1,p2,d//p1,d//p2))
    print("[{}]:{}".format(i,s))
    ans=min(ans,s)

# answer
print(ans)
