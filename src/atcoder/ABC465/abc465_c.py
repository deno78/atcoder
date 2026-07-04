from collections import deque

n = int(input())
s = input().strip()

d = deque()
rev = False

for i, ch in enumerate(s, start=1):
    if rev:
        d.appendleft(i)
    else:
        d.append(i)

    if ch == "o":
        rev = not rev

if rev:
    d.reverse()

print(" ".join(map(str, d)))
