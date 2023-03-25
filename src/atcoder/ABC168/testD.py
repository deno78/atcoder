nm = input('')
n = int(nm.split()[0])
m = int(nm.split()[1])

root={}

for i in range(m):
    ab = input('')
    a = int(ab.split()[0])
    b = int(ab.split()[0])
    if not a in root.keys():
        root[a]=[]
    root[a].append(b)
    if not b in root.keys():
        root[b]=[]
    root[b].append(a)

print(root)

max_count=-1

course = []
pos = 1
for i in range(m):
    nexts = root[pos]
    for n in nexts:
        course