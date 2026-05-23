
from collections import Counter
import heapq
import sys

def build_rearrangement(s: str):
    count = Counter(s)
    n = len(s)
    if max(count.values()) > (n + 1) // 2:
        return None

    heap = [(-cnt, ch) for ch, cnt in count.items()]
    heapq.heapify(heap)

    result = []
    prev_cnt = 0
    prev_ch = ""

    while heap:
        cnt, ch = heapq.heappop(heap)
        result.append(ch)
        cnt += 1

        if prev_cnt < 0:
            heapq.heappush(heap, (prev_cnt, prev_ch))

        prev_cnt = cnt
        prev_ch = ch

    return "".join(result)


input = sys.stdin.readline
t = int(input())
answers = []

for _ in range(t):
    s = input().strip()
    rearranged = build_rearrangement(s)
    if rearranged is None:
        answers.append("No")
    else:
        answers.append("Yes")
        answers.append(rearranged)

print("\n".join(answers))


