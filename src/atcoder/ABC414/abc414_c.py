def is_palindrome_base_n(x, n):
    digits = []
    if x == 0:
        return True
    while x > 0:
        digits.append(x % n)
        x //= n
    return digits == digits[::-1]

a=int(input())
n=int(input())
ans=0

# 桁数ごとに回文を生成
for length in range(1, len(str(n)) + 1):
    half = (length + 1) // 2
    start = 10**(half - 1)
    end = 10**half
    for first_half in range(start, end):
        s = str(first_half)
        # 偶数桁・奇数桁で回文の作り方を分ける
        if length % 2 == 0:
            pal = int(s + s[::-1])
        else:
            pal = int(s + s[-2::-1])
        if pal > n:
            break
        if is_palindrome_base_n(pal,a):
            ans+=pal
#            print(pal,p2)

print(ans)