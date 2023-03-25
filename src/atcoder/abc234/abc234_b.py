import math
# TODO edit the code

# param
n = int(input())
xy=[]
for _ in range(n):
    xy.append(list(map(int,input().split())))

ans=-1
for i in range(n-1):
    for j in range(i,n):
        x1=xy[i][0]
        y1=xy[i][1]
        x2=xy[j][0]
        y2=xy[j][1]
        l=(x1-x2)**2 + (y1-y2)**2
        ans=max(ans,l)

# answer
print(math.sqrt(ans))
