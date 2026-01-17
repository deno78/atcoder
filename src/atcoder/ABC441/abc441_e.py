N=int(input())
S=input()

class FenwickTree:
	def __init__(self, size: int) -> None:
		self.n = size
		self.bit = [0] * (size + 1)

	def add(self, index: int, value: int) -> None:
		while index <= self.n:
			self.bit[index] += value
			index += index & -index

	def prefix_sum(self, index: int) -> int:
		total = 0
		while index > 0:
			total += self.bit[index]
			index -= index & -index
		return total


prefix_vals = [0]
diff = 0
for ch in S:
    if ch == 'A':
        diff += 1
    elif ch == 'B':
        diff -= 1
    prefix_vals.append(diff)

unique = sorted(set(prefix_vals))
index_map = {value: idx for idx, value in enumerate(unique, 1)}
bit = FenwickTree(len(unique))

answer = 0
for value in prefix_vals:
    idx = index_map[value]
    answer += bit.prefix_sum(idx - 1)
    bit.add(idx, 1)

print(answer)
