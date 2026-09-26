n, d = map(int, input().split())
xlist = list(map(int, input().split()))

sorted_x = sorted((x, i) for i, x in enumerate(xlist))
ans = []

for i, (x, original_index) in enumerate(sorted_x):
    left_ok = i == 0 or x - sorted_x[i - 1][0] >= d
    right_ok = i == n - 1 or sorted_x[i + 1][0] - x >= d

    if left_ok and right_ok:
        ans.append(original_index + 1)

ans.sort()
print(len(ans))
print(*ans)