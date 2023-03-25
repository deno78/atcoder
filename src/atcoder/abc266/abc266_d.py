# TODO edit this code

# param
n = int(input())
txa={}
tlist=[]
tlist.append(0)
for i in range(n):
    t,x,a=map(int,input().split())
    if t not in txa.keys():
        txa[t]={}
    txa[t][x]=a
    tlist.append(t)

# solve
dp=[]
for i in range(len(txa.keys())+2):
    dp.append([0]*5)

dp[0][0]=0
for i in range(1,5):
    dp[0][i]=-1

for i in range(len(tlist)):
    t=tlist[i]
    wt=tlist[i]-tlist[i-1]
    for j in range(5):
        if dp[i][j]!=-1:
            for k in range(5):
                if abs(j-k)<=wt:
                    if t in txa.keys() and j in txa[t].keys():
                        dp[i+1][k]=max(dp[i+1][k],dp[i][j]+txa[t][j])
                    else:
                        dp[i+1][k]=max(dp[i+1][k],dp[i][j])
                else:
                    dp[i+1][k]=dp[i][k]


for d in dp:
    print(d)

# answer
print(max(dp[-1]))