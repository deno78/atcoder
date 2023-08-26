# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,h,x= map(int, input().split())
plist=list(map(int,input().split()))

# solve
for i in range(n):
    if h+plist[i]>=x:
        print(i+1)
        exit()

