import sys


def solve() -> None:
    n, k = map(int, sys.stdin.readline().split())

    possible = [bytearray(k + 1) for _ in range(n + 2)]
    possible[n + 1][0] = 1

    for pos in range(n, 0, -1):
        dp = possible[pos + 1][:]
        for s in range(pos, k + 1):
            if dp[s - pos]:
                dp[s] = 1
        possible[pos] = dp

    cur = [0] * n
    out = []

    def dfs(pos: int, rem: int) -> None:
        if pos == n + 1:
            if rem == 0:
                out.append(" ".join(map(str, cur)))
            return

        limit = rem // pos
        for x in range(limit + 1):
            nxt = rem - x * pos
            if possible[pos + 1][nxt]:
                cur[pos - 1] = x
                dfs(pos + 1, nxt)

    dfs(1, k)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

