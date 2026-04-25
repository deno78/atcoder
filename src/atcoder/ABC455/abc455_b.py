h, w = map(int, input().split())
slist = [input().strip() for _ in range(h)]

ans = 0

# X, Y are doubled-center coordinates in 0-indexed grid: row+row', col+col'
for x in range(2 * h - 1):
    top_min = max(0, x - (h - 1))
    top_max = min(h - 1, x // 2)
    if top_min > top_max:
        continue

    for y in range(2 * w - 1):
        left_min_bound = max(0, y - (w - 1))
        left_max = min(w - 1, y // 2)
        if left_min_bound > left_max:
            continue

        need_left = left_min_bound

        # Expand vertically from the center (inner -> outer).
        for top in range(top_max, top_min - 1, -1):
            bottom = x - top

            interval_ok = True
            pair_need_left = left_max + 1
            for left in range(left_max, left_min_bound - 1, -1):
                right = y - left
                if slist[top][left] != slist[bottom][right]:
                    interval_ok = False
                if left != right and slist[top][right] != slist[bottom][left]:
                    interval_ok = False
                if interval_ok:
                    pair_need_left = left

            if pair_need_left > need_left:
                need_left = pair_need_left

            if need_left <= left_max:
                ans += left_max - need_left + 1

print(ans)
