# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
x,y,z = map(int, input().split())
s = input()

# solve
ans = 0

dp=[]
for i in range(len(s)):
    dp.append([0]*2)

if s[0]=="a":
    dp[0][0]=x
    dp[0][1]=z+y
else:
    dp[0][0]=y
    dp[0][1]=z+x

for i in range(1,len(s)):
    c=s[i]
    if c=="a":
        dp[i][0]=min(dp[i-1][0]+x,dp[i-1][1]+z+x)
        dp[i][1]=min(dp[i-1][0]+z+y,dp[i-1][1]+y)
    else:
        # Large A
        dp[i][0]=min(dp[i-1][0]+y,dp[i-1][1]+z+y)
        dp[i][1]=min(dp[i-1][0]+z+x,dp[i-1][1]+x)

#print(dp)
# answer
print(min(dp[-1]))


