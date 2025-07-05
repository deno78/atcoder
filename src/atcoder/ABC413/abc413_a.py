n,m=map(int,input().split())
alist=list(map(int,input().split()))
if sum(alist)>m:
    print("No")
else:
    print("Yes")