import itertools

n,m=map(int,input().split())
xlist=list(map(int,input().split()))
xlist.sort()
xlist=list(set(xlist))
if m >= len(xlist):
    print(0)
    exit()

# 差分リストを作成
diffs = []
for i in range(1, len(xlist)):
    diffs.append((xlist[i] - xlist[i-1], i))

# 差分が大きい順にm-1個選ぶ
diffs.sort(reverse=True)
cut_indices = sorted(idx for _, idx in diffs[:m-1])

ans=float("inf")
# グループ化して合計を計算
ans = 0
prev = 0
for idx in cut_indices:
    group = xlist[prev:idx]
    ans += group[-1] - group[0]
    prev = idx
group = xlist[prev:]
ans += group[-1] - group[0]

print(ans)