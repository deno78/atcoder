# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,r = map(int, input().split())

da=[]
for i in range(n):
    d,a = map(int, input().split())
    da.append([d,a])

# solve
for i in range(n):
    d,a = da[i]
    if d==1:
        if 1600<=r and r<=2799:
            r+=a
    else:
        if 1200<=r and r<=2399:
            r+=a

# answer
print(r)
