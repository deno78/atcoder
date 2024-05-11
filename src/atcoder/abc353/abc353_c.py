# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
alist.sort()
# solve
MOD=10**8
ans=sum(alist)*(n-1)
x=0
x1=0
x2=1
while x1<n-1:
    a=alist[x1]+alist[x2]
    if a>MOD:
        x+=a//MOD
    if x2<n:
        x2+=1
    else:
        x1+=1


print("{}".format(ans-x*MOD))


