from collections import deque


h, w, k = map(int, input().split())
slist = [input() for _ in range(h)]

row_has_bomb = [False] * h
col_has_bomb = [False] * w
for i in range(h):
    for j in range(w):
        if slist[i][j] == "#":
            row_has_bomb[i] = True
            col_has_bomb[j] = True

distance = [[-1] * w for _ in range(h)]
queue = deque()

for i in range(h):
    if row_has_bomb[i]:
        continue
    for j in range(w):
        if slist[i][j] == "." and not col_has_bomb[j]:
            distance[i][j] = 0
            queue.append((i, j))

answer = 0
while queue:
    i, j = queue.popleft()
    current_distance = distance[i][j]
    if current_distance > k:
        continue
    answer += 1
    if current_distance == k:
        continue

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = i + di
        nj = j + dj
        if (
            0 <= ni < h
            and 0 <= nj < w
            and slist[ni][nj] == "."
            and distance[ni][nj] == -1
        ):
            distance[ni][nj] = current_distance + 1
            queue.append((ni, nj))

print(answer)
