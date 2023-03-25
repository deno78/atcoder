def read(sz):
    s = set()
    for x in range(sz):
        line = input()
        for y in range(len(line)):
            if line[y]=="#":
                s.add((x,y))
    return s

n=int(input())
S = read(n)
T = read(n)

print(S)
print(min(S))

for _ in range(4):
    dx,dy=min(S)