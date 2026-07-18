import sys


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	n, _m = data[0], data[1]
	a = data[2 : 2 + n]
	b = data[2 + n : 2 + n + (n - 1)]

	# C 問題の制約は M=2。
	# x[i] を A[i] に加える回数の偶奇 (0/1) とすると、
	# (A[i]+x[i] + A[i+1]+x[i+1]) mod 2 = B[i] より
	# x[i] xor x[i+1] = B[i] xor A[i] xor A[i+1] になる。
	# x[0] を 0/1 の2通り試し、1 の個数が小さい方が最小操作回数。
	c = [b[i] ^ a[i] ^ a[i + 1] for i in range(n - 1)]

	x = 0
	cnt0 = 0
	if x == 1:
		cnt0 += 1
	for i in range(n - 1):
		x ^= c[i]
		if x == 1:
			cnt0 += 1

	cnt1 = n - cnt0
	print(min(cnt0, cnt1))


if __name__ == "__main__":
	main()
