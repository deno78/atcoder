import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])

C = [0] * (n + 1)
trans = [{} for _ in range(n + 1)]

idx = 2
for _ in range(m):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    idx += 2
    C[a] += 1
    trans[a][b] = trans[a].get(b, 0) + 1
    
sorted_c = sorted(range(1, n + 1), key=lambda c: (-C[c], c))

out = []
for k in range(1, n + 1):
    best_a = None
    for c, cnt in trans[k].items():
        score = (C[c] + cnt, -c)
        if best_a is None or score > best_a:
            best_a = score
    best_b = None
    for c in sorted_c:
        if c != k and c not in trans[k]:
            best_b = (C[c], -c)
            break
    if best_a is None:
        winner = -best_b[1]
    elif best_b is None:
        winner = -best_a[1]
    else:
        winner = -max(best_a, best_b)[1]
    out.append(str(winner))
    
print('\n'.join(out))

