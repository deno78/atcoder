n, k = map(int, input().split())
a = list(map(int, input().split()))

# 操作: 最小の a[i] を a[i] + (i+1) に更新（1-indexed で +j）
# c[i] 回操作を当てた後の値: a[i] + c[i] * (i+1)
# 答えを二分探索: 最小値が X 以上にできるか?
# 必要操作数 = sum( ceil((X - a[i]) / (i+1)) ) for a[i] < X
def feasible(X):
    total = 0
    for i in range(n):
        if a[i] < X:
            total += (X - a[i] + i) // (i + 1)
            if total > k:
                return False
    return True

lo = min(a)
hi = 3 * 10**23  # 十分大きな上限

while lo < hi:
    mid = (lo + hi + 1) // 2
    if feasible(mid):
        lo = mid
    else:
        hi = mid - 1

print(lo)

