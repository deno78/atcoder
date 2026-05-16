import heapq
x = int(input())
q = int(input())

# left: 中央値以下(最大ヒープ), right: 中央値以上(最小ヒープ)
left = []
right = []
median = x


def add_value(v: int) -> None:
    global median

    if v <= median:
        heapq.heappush(left, -v)
    else:
        heapq.heappush(right, v)

    # 常に left と right の要素数を揃える
    if len(left) > len(right):
        heapq.heappush(right, median)
        median = -heapq.heappop(left)
    elif len(left) < len(right):
        heapq.heappush(left, -median)
        median = heapq.heappop(right)


for _ in range(q):
    a, b = map(int, input().split())
    add_value(a)
    add_value(b)
    print(median)
