import sys


it = iter(sys.stdin.buffer.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    s = next(it).decode()
    x = [int(next(it)) for _ in range(n)]
    y = [int(next(it)) for _ in range(n - 1)]

    # dp_s: i日目を晴れ(S)にしたときの最大嬉しさ
    # dp_r: i日目を雨れ(R)にしたときの最大嬉しさ
    dp_s = 0 if s[0] == "S" else -x[0]
    dp_r = 0 if s[0] == "R" else -x[0]

    for i in range(1, n):
        cost_s = 0 if s[i] == "S" else -x[i]
        cost_r = 0 if s[i] == "R" else -x[i]

        # (前日R, 当日S) のときだけ y[i-1] を加算
        ndp_s = max(dp_s, dp_r + y[i - 1]) + cost_s
        ndp_r = max(dp_r, dp_s) + cost_r

        dp_s, dp_r = ndp_s, ndp_r

    print(str(max(dp_s, dp_r)))

