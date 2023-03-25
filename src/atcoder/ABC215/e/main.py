n=int(input())
s=list(input())
CT="ABCDEFGHIJ"
sx=[]
for c in s:
    sx.append(CT.index(c))

print(sx)

dp=[]
for i in range(n):
    dp.append([0]*n)

dp[0][0]=1
for i in range(n):
    