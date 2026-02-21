n = int(input())
alist = list(map(int, input().split()))

# best[x] = 「値 x で終わる」条件を満たす部分列の最長長さ
best = {}
ans = 0
for value in alist:
    current = best.get(value - 1, 0) + 1
    if current > best.get(value, 0):
        best[value] = current
    if best[value] > ans:
        ans = best[value]

print(ans)