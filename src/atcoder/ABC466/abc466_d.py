n,m=map(int,input().split())
rc=[]
for i in range(m):
    r,c=map(int,input().split())
    rc.append((r,c))

last_row={}
last_col={}
for i,(r,c) in enumerate(rc):
    last_row[r]=i
    last_col[c]=i

ans=0
for i,(r,c) in enumerate(rc):
    if last_row[r]==i and last_col[c]==i:
        ans+=1
print(ans)

