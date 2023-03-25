n=int(input())
alist=list(map(int,input().split()))

alist.sort()
for i in range(n):
    if alist[i]!=i+1:
        print('No')
        exit()
print('Yes')