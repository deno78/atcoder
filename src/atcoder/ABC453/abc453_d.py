from array import array
from collections import deque


h, w = map(int, input().split())
grid = [input() for _ in range(h)]

start = (-1, -1)
goal = (-1, -1)
for row in range(h):
    for col in range(w):
        if grid[row][col] == "S":
            start = (row, col)
        elif grid[row][col] == "G":
            goal = (row, col)

sr, sc = start
gr, gc = goal

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
move_char = "UDLR"

state_count = h * w * 4
parent = array("i", [-2]) * state_count
queue = deque()
found = -1

for direction in range(4):
    nr = sr + dr[direction]
    nc = sc + dc[direction]
    if not (0 <= nr < h and 0 <= nc < w):
        continue
    if grid[nr][nc] == "#":
        continue

    next_state = ((nr * w + nc) << 2) | direction
    if parent[next_state] != -2:
        continue

    parent[next_state] = -1
    if nr == gr and nc == gc:
        found = next_state
        break
    queue.append(next_state)

while queue and found == -1:
    state = queue.popleft()
    pos = state >> 2
    row = pos // w
    col = pos % w
    last_direction = state & 3
    cell = grid[row][col]

    if cell == "o":
        directions = (last_direction,)
    elif cell == "x":
        directions = (0, 1, 2, 3)
    else:
        directions = (0, 1, 2, 3)

    for direction in directions:
        if cell == "x" and direction == last_direction:
            continue

        nr = row + dr[direction]
        nc = col + dc[direction]
        if not (0 <= nr < h and 0 <= nc < w):
            continue
        if grid[nr][nc] == "#":
            continue

        next_state = ((nr * w + nc) << 2) | direction
        if parent[next_state] != -2:
            continue

        parent[next_state] = state
        if nr == gr and nc == gc:
            found = next_state
            break
        queue.append(next_state)

if found == -1:
    print("No")
else:
    path = []
    state = found
    while state != -1:
        path.append(move_char[state & 3])
        state = parent[state]
    path.reverse()

    print("Yes")
    print("".join(path))


