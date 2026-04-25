import sys
from sys import stdin
input = stdin.readline

n,q=map(int,input().split())
# above[i] = カードiの真下にあるカード（i自身なら山の底）
above = list(range(n))

for _ in range(q):
    c,p=map(int,input().split())
    c-=1
    p-=1
    # カードcの真下にpを接続
    above[c] = p

# 各カードについて山の底（根）を求める（経路圧縮付き）
root = list(range(n))
def find(x):
    while above[x] != x:
        above[x] = above[above[x]]  # path compression
        x = above[x]
    return x

# 根ごとにカウント
count = [0] * n
for i in range(n):
    count[find(i)] += 1

ans = []
for i in range(n):
    if find(i) == i:
        ans.append(count[i])
    else:
        ans.append(0)

print(*ans)

