n=int(input())
ab={}
for i in range(n):
    ab[i]=[]
for i in range(n-1):
    a,b=map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

for a,b in ab.items():
    if len(b)==n-1:
        print('Yes')
        exit()

print('No')