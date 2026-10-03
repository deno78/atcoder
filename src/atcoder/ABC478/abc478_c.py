from collections import deque
import sys

input = sys.stdin.buffer.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# prefix[i]: a[0:i+1] が昇順か
prefix = [True] * n
for i in range(1, n):
    prefix[i] = prefix[i - 1] and a[i - 1] <= a[i]

# suffix[i]: a[i:n] が昇順か
suffix = [True] * n
for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] and a[i] <= a[i + 1]

min_q = deque()
max_q = deque()

for i in range(n):
    while min_q and a[min_q[-1]] >= a[i]:
        min_q.pop()
    min_q.append(i)

    while max_q and a[max_q[-1]] <= a[i]:
        max_q.pop()
    max_q.append(i)

    # 直近 K 個の範囲から外れた添字を取り除く
    left = i - k + 1
    while min_q[0] < left:
        min_q.popleft()
    while max_q[0] < left:
        max_q.popleft()

    if left < 0:
        continue

    right = i

    # 区間外の部分が昇順か確認
    if left > 0 and not prefix[left - 1]:
        continue
    if right < n - 1 and not suffix[right + 1]:
        continue

    # 区間と左右の境界を確認
    if left > 0 and a[left - 1] > a[min_q[0]]:
        continue
    if right < n - 1 and a[max_q[0]] > a[right + 1]:
        continue

    print("Yes")
    break
else:
    print("No")
