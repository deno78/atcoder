q = int(input())
s = input()
t = input()

pref = [0] * (len(s) + 1)

for i in range(len(s) - len(t) + 1):
    pref[i + 1] = pref[i]
    if s[i:i + len(t)] == t:
        pref[i + 1] += 1

for _ in range(q):
    l, r = map(int, input().split())

    left = l - 1
    right = r - len(t)

    if right >= left and pref[right + 1] - pref[left] > 0:
        print("Yes")
    else:
        print("No")