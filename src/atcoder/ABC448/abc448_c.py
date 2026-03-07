import sys


class SegmentTreeMin:
    def __init__(self, arr):
        n = len(arr)
        size = 1
        while size < n:
            size <<= 1
        self.n = n
        self.size = size
        self.inf = 10**18
        self.data = [self.inf] * (2 * size)

        for i, v in enumerate(arr):
            self.data[size + i] = v
        for i in range(size - 1, 0, -1):
            self.data[i] = min(self.data[i << 1], self.data[i << 1 | 1])

    def set_value(self, idx, value):
        pos = self.size + idx
        self.data[pos] = value
        pos >>= 1
        while pos:
            self.data[pos] = min(self.data[pos << 1], self.data[pos << 1 | 1])
            pos >>= 1

    def all_min(self):
        return self.data[1]


it = iter(map(int, sys.stdin.buffer.read().split()))
n = next(it)
q = next(it)
alist = [next(it) for _ in range(n)]

seg = SegmentTreeMin(alist)
INF = 10**18
out = []

for _ in range(q):
    k = next(it)
    removed = [next(it) - 1 for _ in range(k)]  # 1-indexed -> 0-indexed

    for idx in removed:
        seg.set_value(idx, INF)

    out.append(str(seg.all_min()))

    for idx in removed:
        seg.set_value(idx, alist[idx])

sys.stdout.write("\n".join(out))
