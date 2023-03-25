n,m=map(int,input().split())

# 食べ物毎の件数をゼロで初期化
mlist=[0]*m
for i in range(n):
    ka=list(map(int,input().split()))
    k=ka[0]
    # i番目の人が好きな食べ物の件数を足していく
    alist=ka[1:]
    for a in alist:
        mlist[a-1]+=1

ans=0
for i in range(m):
    # 好きな人の件数がn==総人数と合致したらカウント
    if mlist[i]==n:
        ans+=1
print(ans)
