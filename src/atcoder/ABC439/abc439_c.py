n=int(input())

from collections import Counter
count = Counter()
ans = set()
# 0 < x < y かつ x² + y² ≤ n を満たす組み合わせを探す
max_y = int(n**0.5) + 1
for y in range(2, max_y):
    y2 = y**2
    if y2 >= n:
        break
    for x in range(1, y):
        x2 = x**2
        w = x2 + y2
        if w > n:
            break
        count[w] += 1
        if count[w] == 1:
            ans.add(w)
        elif count[w] == 2:
            ans.discard(w)

print(len(ans))
print(" ".join(map(str,sorted(ans))))