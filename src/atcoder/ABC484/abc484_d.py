from collections import defaultdict
import sys

# sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    n = int(input())
    alist = list(map(int, input().split()))

    # 元の列 A 自身は j = i で必ず作れるため 1 通りから数える
    ans = 1
    cnt = defaultdict(int)
    cnt[alist[0]] += 1

    for r in range(1, n):
        # A[r-1] != A[r] のとき、A[l] != A[r] を満たす左端 l (0 <= l < r) ごとに
        # 一意な (l, r) の組（最初と最後の不一致位置）が定まる
        if alist[r - 1] != alist[r]:
            ans += r - cnt[alist[r]]
        cnt[alist[r]] += 1

    print(ans)


if __name__ == "__main__":
    main()
