# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist= list(map(int, input().split()))
blist= list(map(int, input().split()))

alist.sort()
blist.sort()

# solve
ans=0
i1=0
i2=0
while i1<n and i2<m:
    a=alist[i1]
    b=blist[i2]
    if a>=b:
        ans+=a
        i1+=1
        i2+=1
    else:
        i1+=1
# answer
if i2==m:
    print("{}".format(ans))
else:
    print(-1)
