n = int(input())
alist = list(map(int,input().split()))

s=sum(alist)//2+1

dp=[]
for i in range(n):
    dp.append([0]*n)
dp[0]=0

print(sum(alist)-ans)

