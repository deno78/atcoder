s = input().strip()

count_a = 0
count_ab = 0
ans = 0

for ch in s:
    if ch == "A":
        count_a += 1
    elif ch == "B":
        if count_a > 0:
            count_a -= 1
            count_ab += 1
    elif ch == "C":
        if count_ab > 0:
            count_ab -= 1
            ans += 1

print(ans)
