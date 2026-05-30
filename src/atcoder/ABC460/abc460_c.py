n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.sort()
blist.sort()

ans = 0
j = 0

for a in alist:
    if j < m and blist[j] <= 2 * a:
        ans += 1
        j += 1

print(ans)