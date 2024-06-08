# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
hlist = list(map(int, input().split()))

# solve
ans=0
for i in range(n):
    if m>=hlist[i]:
        ans+=1
        m-=hlist[i]
    else:
        break

# answer
print("{}".format(ans))
