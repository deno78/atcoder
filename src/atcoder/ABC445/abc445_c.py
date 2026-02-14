n = int(input())
alist = list(map(int, input().split()))
next_nodes = [a - 1 for a in alist]

K = 10 ** 100

visited = [0] * n
depth = [0] * n
cycle_id = [-1] * n
cycle_index = [0] * n
entry = [0] * n
cycles = []

for start in range(n):
    if visited[start]:
        continue

    cur = start
    stack = []
    pos = {}

    while True:
        if visited[cur] == 0:
            visited[cur] = 1
            pos[cur] = len(stack)
            stack.append(cur)
            cur = next_nodes[cur]
            continue

        if visited[cur] == 1 and cur in pos:
            cycle_nodes = stack[pos[cur]:]
            cid = len(cycles)
            cycles.append(cycle_nodes)
            for idx, node in enumerate(cycle_nodes):
                cycle_id[node] = cid
                cycle_index[node] = idx
                entry[node] = node
                depth[node] = 0
        break

    while stack:
        node = stack.pop()
        visited[node] = 2
        if cycle_id[node] != -1:
            continue
        nxt = next_nodes[node]
        cycle_id[node] = cycle_id[nxt]
        cycle_index[node] = cycle_index[nxt]
        entry[node] = entry[nxt]
        depth[node] = depth[nxt] + 1

result = []
for s in range(n):
    cid = cycle_id[s]
    cycle_nodes = cycles[cid]
    cycle_len = len(cycle_nodes)
    steps_to_cycle = depth[s]

    if K < steps_to_cycle:
        steps = K
        node = s
        while steps:
            node = next_nodes[node]
            steps -= 1
        final = node
    else:
        offset = (K - steps_to_cycle) % cycle_len
        idx = (cycle_index[s] + offset) % cycle_len
        final = cycle_nodes[idx]

    result.append(str(final + 1))

print(" ".join(result))
