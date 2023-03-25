from itertools import permutations
s = input('')

l = min(3,len(s))
slist = list(permutations(s,l))
for c in slist:
    n = int("".join(c))
    if n%8==0:
        print('Yes')
        exit()

print('No')