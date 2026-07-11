n=int(input())
xlist=list(map(int,input().split()))
if max(xlist)<0:
    print("Yes")
else:
    print("No")