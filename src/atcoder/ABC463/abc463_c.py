from bisect import bisect_right
import sys


input = sys.stdin.readline

n = int(input())
h = [0] * n
l = [0] * n

for i in range(n):
    hi, li = map(int, input().split())
    h[i] = hi
    l[i] = li

# suffix_max[i] = max(H_i, H_{i+1}, ..., H_{n-1})
suffix_max = [0] * n
suffix_max[-1] = h[-1]
for i in range(n - 2, -1, -1):
    suffix_max[i] = max(h[i], suffix_max[i + 1])

q = int(input())
t_list = list(map(int, input().split()))

ans = []
for t in t_list:
    # L_i > t の最初の位置を二分探索で求める
    idx = bisect_right(l, t)
    ans.append(str(suffix_max[idx]))

sys.stdout.write("\n".join(ans))



