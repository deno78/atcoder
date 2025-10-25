n,m=map(int,input().split())
alist=list(map(int,input().split()))

s=sum(alist)

for i in range(n):
    if s-alist[i]==m:
        print("Yes")
        exit()

print("No")