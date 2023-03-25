n=int(input())

alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

print(max(0,min(blist)-max(alist)+1))