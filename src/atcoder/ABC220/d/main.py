n=int(input())
alist=list(map(int,input().split()))

dp=[]
for i in range(n+1):
    dp.append([0]*10)

s1=(alist[0]+alist[1])%10
s2=(alist[0]*alist[1])%10

dp[0][s1]=1
dp[0][s2]=dp[0][s2]+1

DIV=998244353

for i in range(1,n-1):
    for j in range(10):
        x1=(j+alist[i+1])%10
        x2=(j*alist[i+1])%10
        dp[i][x1]=(dp[i][x1]+dp[i-1][j])%DIV
        dp[i][x2]=(dp[i][x2]+dp[i-1][j])%DIV

for d in dp[n-2]:
    print(d)