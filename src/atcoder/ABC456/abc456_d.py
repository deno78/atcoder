MOD = 998244353


s = input().strip()

# dp[i]: 有効な(空でない)部分列のうち、末尾文字が chars[i] の個数
dp = [0, 0, 0]  # a, b, c

for ch in s:
    if ch == "a":
        idx = 0
    elif ch == "b":
        idx = 1
    else:
        idx = 2

    add = 1
    for i in range(3):
        if i != idx:
            add += dp[i]

    dp[idx] = (dp[idx] + add) % MOD

print(sum(dp) % MOD)



