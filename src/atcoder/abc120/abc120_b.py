
a,b,k=map(int,input().split())

ans=[]
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        ans.append(i)
ans.sort(reverse=True)
print(ans[k-1])