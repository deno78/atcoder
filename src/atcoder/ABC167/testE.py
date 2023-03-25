n = int(input(''))
alist = list(map(int, input().split()))

heights = {}
for i in range(n):
    a = alist[i]
    if not a in heights.keys():
        heights[a] = []
    heights[a].append(i)

from itertools import permutations, combinations,combinations_with_replacement,product
ablist = list(combinations(alist,2))

for a,b in ablist:
    