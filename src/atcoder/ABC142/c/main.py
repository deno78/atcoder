n=int(input())
alist=list(map(int,input().split()))

adic={}
for i in range(n):
    a=alist[i]
    adic[a]=i
ans=[]
for i in range(n):
    ans.append(str(adic[i+1]+1))
print(" ".join(ans))