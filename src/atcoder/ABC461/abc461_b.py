n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

for i in range(n):
    if i!=blist[alist[i]-1]-1:
        print("No")
        exit()
print("Yes")