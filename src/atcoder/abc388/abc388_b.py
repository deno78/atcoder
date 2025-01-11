# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,d = map(int,input().split())
tl=[]
for i in range(n):
    t,l = map(int, input().split())
    tl.append([t,l])

# solve
for k in range(1,d+1):
    ans=-1
    for i in range(n):
        t,l=tl[i]
        ans=max(ans,t*(l+k))
    print(ans)
