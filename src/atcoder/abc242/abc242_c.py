# param
n = int(input())

MOD=998244353

# solve
ans=[]
for i in range(n):
    ans.append([0]*10)

for i in range(1,10):
    ans[0][i]=1
for i in range(n-1):
    for j in range(1,10):
#        print(j)
        if j>1:
            ans[i+1][j-1]+=ans[i][j]
            ans[i+1][j-1]%=MOD
        if j<9:
            ans[i+1][j+1]+=ans[i][j]
            ans[i+1][j+1]%=MOD
        ans[i+1][j]+=ans[i][j]
        ans[i+1][j]%=MOD
#    print(ans)

print(sum(ans[-1])%MOD)
