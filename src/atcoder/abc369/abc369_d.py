# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
dp=[]
for i in range(n+1):
    dp.append([0]*2)

dp[0][0]=0
dp[0][1]=alist[0]

for i in range(1,n):
    a=alist[i]
    dp[i][0]=max(dp[i-1][0],dp[i-1][1]+a*2)
    dp[i][1]=max(dp[i-1][1],dp[i-1][0]+a)


# answer
print(max(dp[-2]))