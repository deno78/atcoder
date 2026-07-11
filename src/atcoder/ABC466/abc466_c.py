import sys


def ask(i: int, j: int) -> bool:
    print(f"? {i} {j}", flush=True)
    res = sys.stdin.readline().strip()
    if res == "Yes":
        return True
    if res == "No":
        return False
    # ジャッジから異常応答が来た場合は即終了する。
    sys.exit(0)


n = int(sys.stdin.readline())

ans = 0
r = 1

# 各 i について、条件を満たす最大の右端 r を尺取りで更新する。
for i in range(1, n + 1):
    if r < i:
        r = i
    while r + 1 <= n and ask(i, r + 1):
        r += 1
    ans += r - i

print(f"! {ans}", flush=True)
