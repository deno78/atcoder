import sys

# sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    n = int(input())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))

    l = 0
    while l < n and alist[l] == blist[l]:
        l += 1

    if l == n:
        # すでに一致している場合（同位置への挿入不可なら any(alist[i] == alist[i + 1] for i in range(n - 1))）
        ok = True
    else:
        r = 0
        while r < n - l and alist[n - 1 - r] == blist[n - 1 - r]:
            r += 1
        end = n - 1 - r

        # alist[l] を end 番目へ移動する、または alist[end] を l 番目へ移動する
        case1 = alist[l] == blist[end] and alist[l + 1 : end + 1] == blist[l:end]
        case2 = blist[l] == alist[end] and blist[l + 1 : end + 1] == alist[l:end]
        ok = case1 or case2

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
