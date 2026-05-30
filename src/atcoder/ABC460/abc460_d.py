from collections import deque
import sys


input = sys.stdin.readline
h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]

# 証明メモ:
# 1 回目終了時点の黒集合を B1 とする。
# t>=1 の各時刻で黒集合を Bt とすると、規則より
# Bt+1 = N8(Bt) \ Bt  (N8 は 8 近傍閉包) が成り立つ。
# したがって「黒が 1 手で広がる波面」が進み、
# 各マス v は B1 からの 8 近傍距離 d(v) が最小の時刻 t=d(v)+1 で初めて黒になる。
# その後は毎手で反転するため、t>=d(v)+1 では色は t の偶奇で決まる。
# つまり t 時刻で黒 <=> (t-1-d(v)) が偶数。
# 今回 T=10^100 は偶数なので T-1 は奇数、最終時刻で黒なのは d(v) が奇数のマス。

# 1 回操作後の黒マス集合 B1 を作る。
# 以降は B1 を始点に「最短距離の偶奇」で色が決まる。
first_black = [[False] * w for _ in range(h)]
q = deque()

for i in range(h):
    row = s[i]
    for j in range(w):
        if row[j] != '.':
            continue
        ok = False
        for di in (-1, 0, 1):
            ni = i + di
            if ni < 0 or ni >= h:
                continue
            nrow = s[ni]
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                nj = j + dj
                if 0 <= nj < w and nrow[nj] == '#':
                    ok = True
                    break
            if ok:
                break
        if ok:
            first_black[i][j] = True
            q.append((i, j))

# B1 が空なら、以降ずっと白。
if not q:
    out = ['.' * w for _ in range(h)]
    sys.stdout.write('\n'.join(out))
    sys.exit()

# B1 から 8 近傍での最短距離を BFS。
dist = [[-1] * w for _ in range(h)]
for i, j in q:
    dist[i][j] = 0

while q:
    i, j = q.popleft()
    nd = dist[i][j] + 1
    for di in (-1, 0, 1):
        ni = i + di
        if ni < 0 or ni >= h:
            continue
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            nj = j + dj
            if 0 <= nj < w and dist[ni][nj] == -1:
                dist[ni][nj] = nd
                q.append((ni, nj))

# T = 10^100 は偶数。T-1 は奇数なので、最終的に d が奇数のマスが黒。
out = []
for i in range(h):
    line = ['#' if (dist[i][j] & 1) == 1 else '.' for j in range(w)]
    out.append(''.join(line))

sys.stdout.write('\n'.join(out))


