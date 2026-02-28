import sys


MOD = 998244353


class RollbackParityDSU:
	def __init__(self, n: int) -> None:
		self.parent = [-1] * n
		self.parity = [0] * n
		self.cnt0 = [1] * n
		self.cnt1 = [0] * n
		self.components = n
		self.roots_with_both = 0
		self.bad = 0
		self.history = []

	def find(self, x: int):
		p = 0
		while self.parent[x] >= 0:
			p ^= self.parity[x]
			x = self.parent[x]
		return x, p

	def snapshot(self) -> int:
		return len(self.history)

	def rollback(self, snap: int) -> None:
		while len(self.history) > snap:
			rec = self.history.pop()
			if rec[0] == 0:
				self.bad -= 1
				continue

			_, ra, rb, par_ra, cnt0_ra, cnt1_ra, par_rb, cnt0_rb, cnt1_rb, comp_prev, both_prev = rec
			self.parent[ra] = par_ra
			self.cnt0[ra] = cnt0_ra
			self.cnt1[ra] = cnt1_ra
			self.parent[rb] = par_rb
			self.cnt0[rb] = cnt0_rb
			self.cnt1[rb] = cnt1_rb
			self.components = comp_prev
			self.roots_with_both = both_prev

	def can_separate(self) -> bool:
		return self.components > 1 or self.roots_with_both > 0

	def add_constraint(self, a: int, b: int, w: int) -> bool:
		ra, pa = self.find(a)
		rb, pb = self.find(b)

		if ra == rb:
			if (pa ^ pb) != w:
				self.bad += 1
				self.history.append((0,))
				return False
			self.history.append((2,))
			return True

		if -self.parent[ra] < -self.parent[rb]:
			ra, rb = rb, ra
			pa, pb = pb, pa

		t = pa ^ pb ^ w

		self.history.append((
			1,
			ra,
			rb,
			self.parent[ra],
			self.cnt0[ra],
			self.cnt1[ra],
			self.parent[rb],
			self.cnt0[rb],
			self.cnt1[rb],
			self.components,
			self.roots_with_both,
		))

		if self.cnt0[ra] > 0 and self.cnt1[ra] > 0:
			self.roots_with_both -= 1
		if self.cnt0[rb] > 0 and self.cnt1[rb] > 0:
			self.roots_with_both -= 1

		self.parent[ra] += self.parent[rb]
		self.parent[rb] = ra
		self.parity[rb] = t

		if t == 0:
			self.cnt0[ra] += self.cnt0[rb]
			self.cnt1[ra] += self.cnt1[rb]
		else:
			self.cnt0[ra] += self.cnt1[rb]
			self.cnt1[ra] += self.cnt0[rb]

		if self.cnt0[ra] > 0 and self.cnt1[ra] > 0:
			self.roots_with_both += 1

		self.components -= 1
		return True


def main() -> None:
	input = sys.stdin.readline
	n, m = map(int, input().split())
	edges = [None] * (m + 1)
	for i in range(1, m + 1):
		u, v = map(int, input().split())
		edges[i] = (u - 1, v - 1)

	pow2 = [1] * (m + 1)
	for i in range(1, m + 1):
		pow2[i] = (pow2[i - 1] * 2) % MOD

	dsu = RollbackParityDSU(n)
	ans = 0

	for i in range(m, 0, -1):
		u, v = edges[i]

		snap = dsu.snapshot()
		ok = dsu.add_constraint(u, v, 0)

		if ok and dsu.bad == 0 and dsu.can_separate():
			continue

		dsu.rollback(snap)
		dsu.add_constraint(u, v, 1)
		ans += pow2[i]
		if ans >= MOD:
			ans -= MOD

	print(ans)


if __name__ == "__main__":
	main()
