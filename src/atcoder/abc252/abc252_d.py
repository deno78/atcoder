# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

dp={}
for i in list(set(alist)):
    dp[i]=[0]*n
# solve
dp[alist[0]][0]=1
for i in range(1,n):
    for j in dp.keys():
        dp[j][i]=dp[j][i-1]
    a=alist[i]
    dp[a][i]=dp[a][i-1]+1

#print(dp)
ans=0
for j in range(1,n-1):
    aj=alist[j]
#            print("i:{} j:{} rest:{}".format(i,j,n-j-1))
    ans+=(n-j-1)*(j-1)
#            print(" di:{}-{} dj:{}-{}".format(dp[ai][-1] , dp[ai][j],dp[ai][-1] , dp[ai][j]))
    ans -= dp[aj][j-1] - dp[aj][0]
    ans -= dp[aj][-1] - dp[aj][j]

# answer
print(ans)
