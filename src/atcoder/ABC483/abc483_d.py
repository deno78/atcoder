n = int(input())
alist = list(map(int, input().split()))

# 累積座標列 S を作成 (S[0] = 0, S[1] = A[0], S[2] = A[0]+A[1], ...)
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + alist[i]

# 前方からの min, max
pref_min = [0] * (n + 1)
pref_max = [0] * (n + 1)
pref_min[0] = s[0]
pref_max[0] = s[0]
for i in range(1, n + 1):
    pref_min[i] = min(pref_min[i - 1], s[i])
    pref_max[i] = max(pref_max[i - 1], s[i])

# 後方からの min, max
suff_min = [0] * (n + 1)
suff_max = [0] * (n + 1)
suff_min[n] = s[n]
suff_max[n] = s[n]
for i in range(n - 1, -1, -1):
    suff_min[i] = min(suff_min[i + 1], s[i])
    suff_max[i] = max(suff_max[i + 1], s[i])

# 1. 反転しない場合
ans = pref_max[n] - pref_min[n] + 1

# 2. alist[i] を反転する場合 (i = 0, 1, ..., n-1)
# alist[i] の反転によって影響を受けるのは s[i+1] 以降
for i in range(n):
    diff = -2 * alist[i]
    
    # 前半: s[0] ~ s[i] (変化なし)
    # 後半: s[i+1] ~ s[n] (すべて + diff)
    cur_max = max(pref_max[i], suff_max[i + 1] + diff)
    cur_min = min(pref_min[i], suff_min[i + 1] + diff)
    
    ans = max(ans, cur_max - cur_min + 1)

print(ans)