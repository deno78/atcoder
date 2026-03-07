import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

mp = {}
dup = 0
ans = [0] * n

st = [(0, -1, 0)]
while st:
    v, p, t = st.pop()

    if t == 0:
        x = a[v]
        c = mp.get(x, 0) + 1
        mp[x] = c
        if c == 2:
            dup += 1

        if dup > 0:
            ans[v] = 1

        st.append((v, p, 1))
        for nv in g[v]:
            if nv == p:
                continue
            st.append((nv, v, 0))
    else:
        x = a[v]
        c = mp[x]
        if c == 2:
            dup -= 1
        if c == 1:
            del mp[x]
        else:
            mp[x] = c - 1

out = ["Yes" if x == 1 else "No" for x in ans]
print("\n".join(out))


