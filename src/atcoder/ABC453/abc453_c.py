n = int(input())
llist = list(map(int, input().split()))

dp = {0: 0}

for move in llist:
	ndp = {}
	for pos, count in dp.items():
		for nxt in (pos - move, pos + move):
			add = 1 if (pos >= 0) != (nxt >= 0) else 0
			best = count + add
			if nxt not in ndp or ndp[nxt] < best:
				ndp[nxt] = best
	dp = ndp

print(max(dp.values(), default=0))