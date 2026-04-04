s = input().strip()
t = input().strip()

n = len(s)
m = len(t)

# best[k]: これまでに見た prefix で、T[:k] を部分列として作れるときの
# 「先頭位置の最大値」。作れない場合は -1。
best = [-1] * (m + 1)

# 各文字が T のどの位置に現れるか（1-indexed の k を保持）
pos = [[] for _ in range(26)]
for k, ch in enumerate(t, start=1):
    pos[ord(ch) - ord("a")].append(k)

good = 0

for i, ch in enumerate(s):
    cidx = ord(ch) - ord("a")

    # 同じ文字で 1 文字中に複数回遷移しないよう、k は降順で更新
    for k in reversed(pos[cidx]):
        if k == 1:
            if i > best[1]:
                best[1] = i
        else:
            prev = best[k - 1]
            if prev > best[k]:
                best[k] = prev

    if best[m] != -1:
        good += best[m] + 1

total = n * (n + 1) // 2
print(total - good)
