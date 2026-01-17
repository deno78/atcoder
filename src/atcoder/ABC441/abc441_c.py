n, k, x = map(int, input().split())
alist = sorted(map(int, input().split()))

if x <= 0:
    print(1)
    exit()

prefix = [0]
for value in alist:
    prefix.append(prefix[-1] + value)

def can(count: int) -> bool:
    if count <= 0 or count > n:
        return False
    forced = k + count - n
    if forced <= 0:
        return False
    start = n - count
    end = start + forced
    return prefix[end] - prefix[start] >= x

lo, hi = 1, n + 1
while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

if lo == n + 1:
    print(-1)
else:
    print(lo)