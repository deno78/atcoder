
s=input()
word="chokudai"
MOD=10**9+7

dp=[]
for i in range(len(s)+1):
    dp.append([0]* (len(word)+1))
dp[0][0]=1
for i in range(len(s)):
    for j in range(len(word)):
        dp[i][j]%=MOD
        dp[i+1][j] += dp[i][j]
        if word[j]==s[i]:
            dp[i+1][j+1] += dp[i][j]
for d in dp:
    print(d)
print(dp[-1][-2])