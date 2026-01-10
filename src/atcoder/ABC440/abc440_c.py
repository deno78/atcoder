import sys


t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    clist = list(map(int, input().split()))
    span = 2 * w
    diff = [0] * (span + 1)
    for idx, val in enumerate(clist):
        start = (-idx - 1) % span
        end = start + w
        if end < span:
            diff[start] += val
            diff[end] -= val
        else:
            diff[start] += val
            diff[span] -= val
            diff[0] += val
            diff[end % span] -= val
    cur = 0
    ans = float("inf")
    for x in range(span):
        cur += diff[x]
        if abs(cur) < ans:
            ans = abs(cur)
    print(ans)
