import sys
input = sys.stdin.readline

n, k = map(int, input().split())
alist = list(map(int, input().split()))

# 各要素の剰余の種類だけが重要
remainders = sorted(set(a % k for a in alist))

m = len(remainders)
if m <= 1:
    # 全要素が同じ剰余 → 全て同じ値にできる
    print(0)
else:
    # 円周 k 上での隣接剰余間の最大ギャップを求める
    # 答え = k - 最大ギャップ
    max_gap = remainders[0] + k - remainders[-1]  # wrap-around
    for i in range(1, m):
        gap = remainders[i] - remainders[i - 1]
        if gap > max_gap:
            max_gap = gap
    print(k - max_gap)

