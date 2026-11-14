import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    n = int(input())
    alist = list(map(int, input().split()))
    if 9 not in alist:
        print(-1)
    else:
        print(min(alist))


if __name__ == "__main__":
    main()
