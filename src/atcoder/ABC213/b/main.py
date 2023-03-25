n=int(input())
alist=list(map(int,input().split()))
adic={}
for i in range(n):
    adic[alist[i]]=i

alist.sort()

print(adic[alist[-2]]+1)