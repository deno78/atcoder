n=int(input())
alist=list(map(int,input().split()))
for i in range(n):
    print(sum(alist[i*7:i*7+7]))