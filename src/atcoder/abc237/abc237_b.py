h,w=map(int,input().split())

a=[]
for i in range(h):
    a.append(list(map(int,input().split())))

ans=[]
for i in range(w):
    ans.append([])
    for j in range(h):
        ans[i].append(str(a[j][i]))

for i in range(w):
    print(" ".join(ans[i]))