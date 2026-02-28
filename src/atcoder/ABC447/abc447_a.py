n,m=map(int,input().split())
if (n%2==1 and (n+1)//2>=m) or (n%2==0 and n//2>=m):
    print("Yes")
else:
    print("No")