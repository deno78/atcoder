n,k,t=map(int,input().split())
a=list(map(int,input().split()))

# 青木君が押す時刻を昇順にソート
a.sort()

# 青木君によってお湯が出ている区間 [a_i, a_i + k] をマージ
merged = []
for x in a:
    if not merged:
        merged.append([x, x + k])
    else:
        if x <= merged[-1][1]:
            merged[-1][1] = x + k
        else:
            merged.append([x, x + k])
            
cur = 0
ans = 0

# 各青木君のお湯が出ている区間との間の隙間を埋める
for s, e in merged:
    if cur >= t:
        break
    if s > cur:
        gap = min(s, t) - cur
        ans += (gap + k - 1) // k
        if s >= t:
            cur = t
            break
    cur = max(cur, e)
    
# 時刻 T までにまだ隙間が残っている場合
if cur < t:
    gap = t - cur
    ans += (gap + k - 1) // k
    cur = t
    
print(ans)

