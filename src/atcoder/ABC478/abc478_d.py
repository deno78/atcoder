from collections import defaultdict
import sys

input = sys.stdin.buffer.readline

n, q = map(int, input().split())
intervals_by_x = defaultdict(list)

for _ in range(q):
    left, right, x = map(int, input().split())
    intervals_by_x[x].append((left - 1, right))

diff = [0] * (n + 1)

for intervals in intervals_by_x.values():
    intervals.sort()
    merged_left, merged_right = intervals[0]

    for left, right in intervals[1:]:
        if left <= merged_right:
            merged_right = max(merged_right, right)
        else:
            diff[merged_left] += 1
            diff[merged_right] -= 1
            merged_left, merged_right = left, right

    diff[merged_left] += 1
    diff[merged_right] -= 1

answer = []
count = 0
for i in range(n):
    count += diff[i]
    answer.append(str(count))

print(" ".join(answer))