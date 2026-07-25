
import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

rank_p = -1
rank_q = -1

for i, perm in enumerate(itertools.permutations(range(1, n + 1))):
    if perm == p:
        rank_p = i
    if perm == q:
        rank_q = i
    if rank_p != -1 and rank_q != -1:
        break

if rank_p < rank_q:
    print(rank_q - rank_p - 1)
else:
    print(0)

