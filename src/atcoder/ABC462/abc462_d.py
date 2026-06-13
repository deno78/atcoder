import sys

input = sys.stdin.buffer.readline

n, d = map(int, input().split())
ranges = []
max_r = 0

for _ in range(n):
    s, t = map(int, input().split())
    r = t - d
    if r < s:
        continue
    ranges.append((s, r))
    if r > max_r:
        max_r = r

if not ranges:
    print(0)
    exit()

diff = [0] * (max_r + 3)
for l, r in ranges:
    diff[l] += 1
    diff[r + 1] -= 1

ans = 0
cur = 0
for x in range(1, max_r + 1):
    cur += diff[x]
    if cur >= 2:
        ans += cur * (cur - 1) // 2

print(ans)
