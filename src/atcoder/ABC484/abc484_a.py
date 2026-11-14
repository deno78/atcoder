import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    b,r = map(int, input().split())
    print((30-b)*(30-r))


if __name__ == "__main__":
    main()
