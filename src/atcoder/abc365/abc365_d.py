# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

slist=[]
l="RPS"
for i in range(n):
    slist.append(l.index(s[i]))

# solve
ans=0

dp=[]
for i in range(n):
    dp.append([0]*3)

s1=(slist[0]+1)%3
s2=(slist[0]-1)%3
dp[0][s1]=1
dp[0][s2]=-1
for i in range(1,n):
    s0=slist[i]
    s1=(slist[i]+1)%3
    s2=(slist[i]-1)%3
    dp[i][s0]=max(dp[i][s0], dp[i-1][s1], dp[i-1][s2])
    dp[i][s1]=max(dp[i][s1], dp[i-1][s0]+1, dp[i-1][s2]+1)
    dp[i][s2]=-1
#    print(dp)
# answer
print("{}".format(max(dp[-1])))
