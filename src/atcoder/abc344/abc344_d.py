# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
t = input()
n = int(input())
slist=[]
for i in range(n):
    s=input().split()
    slist.append(s)

# solve
dp = []
l=len(t)
for i in range(n):
    dp.append([float("INF")]*(l+1))

for i in range(n):
    if i>0:
        for j in range(l):
            dp[i][j]=dp[i-1][j]
    for j in range(1,len(slist[i])):
        s=slist[i][j]
        # print("[{}][{}:{}]".format(i,j,s))
        idx=-1
        while True:
            idx = t.find(s,idx+1)
            if idx==-1:
                break
            else:
                l2=len(s)
                if i==0:
                    if idx==0:
                        # print("[{}][{}:{}]:{}-{}".format(i,j,s,idx,idx+l2))
                        dp[i][idx+l2]=1
                else:
                    if dp[i-1][idx]>0 and idx+l2<=l+1:
                        # print("[{}][{}:{}]:{}-{}".format(i,j,s,idx,idx+l2))
                        dp[i][idx+l2]=min(dp[i][idx+l2],dp[i-1][idx]+1)
                    elif idx==0 and idx+l2<=l+1:
                        dp[i][idx+l2]=1
    # print(dp[i])

# print("=================")
# for d in dp:
#     print(d)

# answer
if dp[-1][-1]==float("INF"):
    print(-1)
else:
    print(dp[-1][-1])
