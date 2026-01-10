from bisect import bisect_left

n, q = map(int, input().split())
alist = sorted(set(map(int, input().split())))
m = len(alist)
prefix = [0] * m
for i, value in enumerate(alist):
    prefix[i] = value - (i + 1)


for _ in range(q):
    x, y = map(int, input().split())
    if m == 0:
        print(x + y - 1)
        continue
    idx = bisect_left(alist, x)
    missing_before_x = (x - 1) - idx
    target = missing_before_x + y
    i = bisect_left(prefix, target)
    if i == m:
        ans = alist[-1] + (target - prefix[-1])
    elif i == 0:
        ans = target
    else:
        ans = alist[i - 1] + (target - prefix[i - 1])
    print(ans)

