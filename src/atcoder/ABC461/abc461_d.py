import sys

input = sys.stdin.buffer.readline

h, w, k = map(int, input().split())
grid = [[ch & 1 for ch in input().strip()] for _ in range(h)]

if h > w:
    # We enumerate all row-pairs, so keep h as the smaller dimension.
    grid = [list(row) for row in zip(*grid)]
    h, w = w, h

max_sum = h * w
counts = [0] * (max_sum + 1)
seen = [0] * (max_sum + 1)
stamp = 0

answer = 0
K = k
seen_arr = seen
counts_arr = counts

for top in range(h):
    column_sums = [0] * w
    for bottom in range(top, h):
        row = grid[bottom]
        col_sums = column_sums
        for col in range(w):
            col_sums[col] += row[col]

        # Count subarrays with sum k in O(w) using prefix-sum frequencies.
        stamp += 1
        prefix = 0
        seen_arr[0] = stamp
        counts_arr[0] = 1

        for value in col_sums:
            prefix += value
            target = prefix - K
            if target >= 0 and seen_arr[target] == stamp:
                answer += counts_arr[target]

            if seen_arr[prefix] != stamp:
                seen_arr[prefix] = stamp
                counts_arr[prefix] = 1
            else:
                counts_arr[prefix] += 1

print(answer)

