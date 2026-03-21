from collections import deque


def count_inner_components(wdict, h, w):
    points = set()
    for x, ys in wdict.items():
        for y in ys:
            points.add((x, y))

    def is_outer(x, y):
        return x == 0 or x == h - 1 or y == 0 or y == w - 1

    visited = set()
    ans = 0

    for sx, sy in points:
        if (sx, sy) in visited:
            continue

        q = deque([(sx, sy)])
        visited.add((sx, sy))
        touches_outer = is_outer(sx, sy)

        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if (nx, ny) not in points or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny))
                if is_outer(nx, ny):
                    touches_outer = True

        if not touches_outer:
            ans += 1

    return ans


h, w = map(int, input().split())
smap = [input().strip() for _ in range(h)]

wdict = {}
for i in range(h):
    for j in range(w):
        if smap[i][j] == ".":
            if i not in wdict:
                wdict[i] = []
            wdict[i].append(j)

print(count_inner_components(wdict, h, w))



