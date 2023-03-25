# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
dp=[]
for i in range(n):
    dp.append([0]*n)

for i in range(n):
    i2=(i+1)%n
    dp[i][i]=min(dp[i][i],dp[i][i])

print(dp)
