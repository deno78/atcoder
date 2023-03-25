# TODO edit the code

# param
n,k=map(int,input().split())

alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

# solve
m=max(alist)
alist2=[]
for i in range(n):
    if alist[i]==m:
        alist2.append(i+1)

for a in alist2:
    if a in blist:
        print('Yes')
        exit()

print('No')