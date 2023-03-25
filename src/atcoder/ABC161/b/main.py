n,m=map(int,input().split())
alist = list(map(int,input().split()))

alist.sort(reverse=True)
s=sum(alist)
l=s/(4*m)
cnt=0
for i in range(m):
    a=alist[i]
    if a<l:
        print('No')
        exit()
print('Yes')

