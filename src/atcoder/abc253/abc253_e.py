# TODO edit the code

# param
n,m,k=map(int,input().split())

# solve
dp=[]
for i in range(n+1):
    dp.append([0]*(m+1))

for i in  range(1,m+1):
    dp[0][i]=1

for i in range(n-1):
    for j in range(1,m+1):
        for a in range(1,j-k+1):
            dp[i+1][a]+=dp[i][j]
        for a in range(j+k,m+1):
            dp[i+1][a]+=dp[i][j]

# answer
print(sum(dp[-2]))
