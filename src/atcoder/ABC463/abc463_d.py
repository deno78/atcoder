import sys


def main() -> None:
    input = sys.stdin.readline
    n, k = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    # 区間スケジューリングと同様に、右端が早い順で見るのが最適。
    intervals.sort(key=lambda x: x[1])

    def can(score: int) -> bool:
        cnt = 0
        last_end = -10**30
        for l, r in intervals:
            if l >= last_end:
                cnt += 1
                last_end = r + score
                if cnt >= k:
                    return True
        return False

    # score=1 が不可能なら、そもそも K 枚を互いに重ならずに選べない。
    if not can(1):
        print(-1)
        return

    lo, hi = 1, 10**9 + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid

    print(lo)


if __name__ == "__main__":
    main()

