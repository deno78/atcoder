import bisect


def count_in_range(sorted_vals, left, right):
    return bisect.bisect_right(sorted_vals, right) - bisect.bisect_left(sorted_vals, left)


l, r, d, u = map(int, input().split())

# bad points = points where max(|x|, |y|) is odd.
# For odd k, the boundary ring max(|x|, |y|)=k contributes:
#   x=±k with y in [-k, k]   -> 4k+2 points
#   y=±k with x in [-(k-1), k-1] -> 4k points
# total = 8k+2
# Intersect this ring with the given rectangle in O(1) per odd k,
# and sum over odd k that can appear.

all_points = (r - l + 1) * (u - d + 1)

max_abs = max(abs(l), abs(r), abs(d), abs(u))
odd_max = max_abs if max_abs % 2 == 1 else max_abs - 1

bad = 0
for k in range(1, odd_max + 1, 2):
    y_vals = [-k, k]
    x_vals = [-k, k]

    # x = ±k, y in [-k, k]
    xs = count_in_range(x_vals, l, r)
    ys = max(0, min(u, k) - max(d, -k) + 1)
    bad += xs * ys

    # y = ±k, x in [-(k-1), k-1]
    ys = count_in_range(y_vals, d, u)
    xs = max(0, min(r, k - 1) - max(l, -k + 1) + 1)
    bad += ys * xs

print(all_points - bad)
