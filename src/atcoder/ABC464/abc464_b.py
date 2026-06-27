h,w=map(int,input().split())
cmap=[]
for i in range(h):
    cmap.append(input())

x1=0
y1=0
x2=h-1
y2=w-1

for i in range(h):
    cnt=0
    for j in range(w):
        if cmap[i][j]=="#":
            cnt+=1
    if cnt>0:
        x1=i
        break

for i in range(h):
    cnt=0
    for j in range(w):
        if cmap[h-i-1][j]=="#":
            cnt+=1
    if cnt>0:
        x2=h-i-1
        break

for j in range(w):
    cnt=0
    for i in range(h):
        if cmap[i][j]=="#":
            cnt+=1
    if cnt>0:
        y1=j
        break

for j in range(w):
    cnt=0
    for i in range(h):
        if cmap[i][w-j-1]=="#":
            cnt+=1
    if cnt>0:
        y2=w-j-1
        break
    
ans=[]
for i in range(x1,x2+1):
    ans.append(cmap[i][y1:y2+1])
for a in ans :
    print("".join(a))