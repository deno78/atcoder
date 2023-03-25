# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,x,m = map(int, input().split())

a%=m
# solve
ans=1
wk=1
for i in range(x-1):
    wk*=a
    ans+=wk
    ans%=m

# answer
print(ans)