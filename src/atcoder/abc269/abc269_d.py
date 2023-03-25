XYs=[
    [-1,-1],
    [-1,0],[0,-1],
    [0,1],[1,0],
    [1,1]
    ]

def check(a1,b1,a2,b2):
    for dx,dy in XYs:
        if a1+dx==a2 and b1+dy==b2:
            return True
    return False

n=int(input())
xy=[]
for i in range(n):
    x,y=map(int,input().split())
    xy.append([x,y])

ans=[]
for i in range(n):
    ans.append(str(i))

for i in range(n):
    x1,y1=xy[i]
    for j in range(n):
        x2,y2=xy[j]
        if check(x1,y1,x2,y2):
            for k in range(n):
                if ans[k]==ans[j]:
                    ans[k]=ans[i]

print(len(set(ans)))