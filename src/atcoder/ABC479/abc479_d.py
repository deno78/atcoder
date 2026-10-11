import sys

input = sys.stdin.buffer.readline

n, q = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

inf = 10**30
right_prefix_min = [inf]
for cost in right:
    right_prefix_min.append(min(right_prefix_min[-1], cost))

left_suffix_min = [inf] * n
for i in range(n - 2, -1, -1):
    left_suffix_min[i] = min(left[i], left_suffix_min[i + 1])

answers = []
for _ in range(q):
    s, t = map(int, input().split())

    if s < t:
        answer = right[s - 1]
        if s > 1:
            answer = min(answer, left[s - 2] + right_prefix_min[s - 1])
    else:
        answer = left[s - 2]
        if s < n:
            answer = min(answer, right[s - 1] + left_suffix_min[s - 1])

    answers.append(str(answer))

print("\n".join(answers))
