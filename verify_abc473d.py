import itertools
import subprocess
import sys

for n in range(1, 8):
    for k in range(0, 25):
        expected = []
        for vals in itertools.product(range(0, k + 1), repeat=n):
            if sum(i * v for i, v in enumerate(vals, start=1)) == k:
                expected.append(vals)

        proc = subprocess.run(
            [sys.executable, 'src/atcoder/ABC473/abc473_d.py'],
            input=f'{n} {k}\n',
            text=True,
            capture_output=True,
            check=False,
        )
        got = []
        if proc.stdout.strip():
            for line in proc.stdout.strip().splitlines():
                got.append(tuple(map(int, line.split())))

        if expected != got:
            print('Mismatch! n=', n, 'k=', k)
            print('expected=', expected)
            print('got=', got)
            raise SystemExit(1)

print('all_ok')
