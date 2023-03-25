nm = input('').split()
n = int(nm[0])
m = int(nm[1])

mx=0
friends={}

for i in range(n):
    friends[i+1] = set([i+1])

for i in range(m):
    ab=input('').split()
    a = int(ab[0])
    b = int(ab[1])
    friends[a].add(b)
    friends[b].add(a)
    for f in friends[a]:
        friends[f].add(b)
        friends[b].add(f)
    for f in friends[b]:
        friends[f].add(a)
        friends[a].add(f)

for f in friends.values():
    len_f=len(f)
    if len_f > mx:
        mx=len_f
#print(friends)
print(mx)