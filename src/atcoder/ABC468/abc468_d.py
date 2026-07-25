def count_from_center(s: str, left: int, right: int) -> int:
    n = len(s)
    mismatch = 0
    cnt = 0

    while 0 <= left and right < n:
        if s[left] != s[right]:
            mismatch += 1
            if mismatch > 1:
                break
        cnt += 1
        left -= 1
        right += 1

    return cnt


s = input().strip()
n = len(s)
ans = 0

for c in range(n):
    # odd length palindromes centered at c
    ans += count_from_center(s, c, c)
    # even length palindromes centered between c and c+1
    ans += count_from_center(s, c, c + 1)

print(ans)