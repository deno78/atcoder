# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
llist=list(map(int,input().split()))

# solve
ans1 = sum(llist)//m
ans=ans1
wk=0
for i in range(n):
    wk+=llist[i]
    if wk>ans1:
        ans=max(ans,wk)
        wk=0
    else:
        wk+=1
        if wk>ans1:
            wk=0
# answer
print("{}".format(ans))
