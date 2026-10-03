n,m=map(int,input().split())
nlist=[0]*n
for i in range(m):
    nlist[i%n]+=1

for i in range(n):
    print(nlist[i])