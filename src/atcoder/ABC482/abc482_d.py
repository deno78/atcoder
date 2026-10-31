import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    xlist = [int(x) for x in data[1:]]

    if n == 1:
        print(0)
        return

    ans = []
    for i in range(n):
        if i == 0 or i == n - 1:
            ans.append((xlist[-1] - xlist[0]) // 2)
        else:
            # 負の方向に最初動く（人 i-1 とまず接触する）
            t_left = max((xlist[i] - xlist[0]) // 2, (xlist[-1] - xlist[i - 1]) // 2)
            # 正の方向に最初動く（人 i+1 とまず接触する）
            t_right = max((xlist[i + 1] - xlist[0]) // 2, (xlist[-1] - xlist[i]) // 2)
            ans.append(min(t_left, t_right))

    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
