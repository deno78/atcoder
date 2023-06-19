# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
xy=[]
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])

# solve
dp=[]
for i in range(n+1):
    dp.append([0]*2)


for i in range(n):
    x,y=xy[i]
 #   print("{} {}".format(x,y))
    if x==0:
        dp[i][0]=max(dp[i-1][0],dp[i-1][0]+y,dp[i-1][1]+y)
        dp[i][1]=dp[i-1][1]
    elif x==1:
        dp[i][0]=dp[i-1][0]
        dp[i][1]=max(dp[i-1][0]+y,dp[i-1][1])

#for d in dp:
#    print(d)

# answer
print(max(dp[-2]))