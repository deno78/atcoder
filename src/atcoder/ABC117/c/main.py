n,m=map(int,input().split())
xlist=list(map(int,input().split()))
if n>=m:
    print(0)
    exit()

xlist.sort()

ylist=[]
for i in range(1,m):
    ylist.append(xlist[i]-xlist[i-1])
ylist.sort()

print(sum(ylist[:min(m-n,m)]))