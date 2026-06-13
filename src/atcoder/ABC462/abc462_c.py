import sys


input = sys.stdin.buffer.readline
n = int(input())

y_at_x = [0] * (n + 1)
for _ in range(n):
    x, y = map(int, input().split())
    y_at_x[x] = y

ans = 0
min_y = n + 1
for x in range(1, n + 1):
    y = y_at_x[x]
    if y < min_y:
        ans += 1
        min_y = y

print(ans)



