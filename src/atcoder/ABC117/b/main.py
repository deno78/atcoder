n=int(input())
llist=list(map(int,input().split()))

if max(llist) >= (sum(llist)-max(llist)):
    print('No')
else:
    print('Yes')