n, q = map(int, input().split())


class Fenwick:
    def __init__(self, size):
        self.n = size
        self.bit = [0] * (size + 1)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


# wk[i] は「生の加算回数」。実際の値は wk[i] - all_offset。
wk = [0] * n
max_raw = q
freq = [0] * (max_raw + 2)
freq[0] = n

fw = Fenwick(max_raw + 2)
fw.add(1, n)  # raw=0 の人数

min_raw = 0
all_offset = 0

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        idx = query[1] - 1
        old = wk[idx]
        new = old + 1
        wk[idx] = new

        freq[old] -= 1
        freq[new] += 1
        fw.add(old + 1, -1)
        fw.add(new + 1, 1)

        while min_raw <= max_raw and freq[min_raw] == 0:
            min_raw += 1

        # 全員の実値が 1 以上なら、全員から 1 を引く操作を遅延評価で反映。
        if min_raw >= all_offset + 1:
            all_offset += 1

    else:
        x = query[1]
        threshold = x + all_offset

        if threshold <= 0:
            print(n)
            continue
        if threshold > max_raw:
            print(0)
            continue

        less_than_threshold = fw.sum(threshold)
        print(n - less_than_threshold)
