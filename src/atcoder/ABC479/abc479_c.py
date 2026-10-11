n,w=map(int,input().split())
ablist=[]
for _ in range(n):
    a,b=map(int,input().split())
    ablist.append((a,b))

ans=0
for i in range(1 << n):
    total = 0
    weight=0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            total += ablist[j][0]
            weight += ablist[j][1]
    if (weight <= w):
        ans = max(ans, total)
print(ans)