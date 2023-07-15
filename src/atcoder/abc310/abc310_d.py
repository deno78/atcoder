# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
def factorial_for(num):
    val = 1
    for i in range(num, 1, -1):
        val *= i
    return val

# param
n,t,m = map(int, input().split())
ab={}
for i in range(n):
    ab[i]=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab[a].append(b)
    ab[b].append(a)

# solve
dp=[]
for i in range(n+1):
    dp.append([0]*t)

dp[0][0]=1

for i in range(n):
    for j in range(t):
        if j not in ab[i]:
            dp[i+1][j]=dp[i+1][j]+dp[i][j]

print(dp)
