# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
slist=[]
for i in range(n):
    s = input()
    slist.append(s)

# solve
ans=float("INF")
for i in range(2**n):
    bag=[]
    for j in range(n):
        if ((i>>j)&1):
            bag.append(j)
    wk=[0]*m
    for j in range(len(bag)):
        b=bag[j]
        for k in range(m):
            if slist[b][k]=="o":
                wk[k]+=1
#    print("{} {}".format(bag,wk))
    if min(wk)>0:
        ans=min(ans,len(bag))

# answer
print("{}".format(ans))
