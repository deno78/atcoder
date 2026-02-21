from array import array

m, a, b = map(int, input().split())
m1 = m - 1
n = m1 * m1

if n == 0:
    print(0)
    exit()

a_mul = [(a * (v + 1)) % m for v in range(m1)]
b_mul = [(b * (u + 1)) % m for u in range(m1)]

# 0: 未訪問, 1: 探索中, 2: 安全, 3: 不安全
state = bytearray(n)
seen_run = array("I", [0]) * n
seen_pos = array("I", [0]) * n
run_id = 0

for start in range(n):
    if state[start] != 0:
        continue

    run_id += 1
    path = []
    cur = start
    cycle_found = False
    terminal = 3

    while True:
        if cur == -1:
            terminal = 3
            break

        st = state[cur]
        if st == 0:
            state[cur] = 1
            seen_run[cur] = run_id
            seen_pos[cur] = len(path)
            path.append(cur)

            u_idx, v_idx = divmod(cur, m1)
            w = (a_mul[v_idx] + b_mul[u_idx]) % m
            if w == 0:
                cur = -1
            else:
                cur = v_idx * m1 + (w - 1)
            continue

        if st == 1 and seen_run[cur] == run_id:
            cycle_found = True
            break

        terminal = 2 if st == 2 else 3
        break

    if cycle_found:
        for node in path:
            state[node] = 2
    else:
        for node in reversed(path):
            state[node] = terminal

print(state.count(2))
