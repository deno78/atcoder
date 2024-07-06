# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist = list(map(int, input().split()))
alist.sort()


# solve
ans=float("INF")
for i in range(k+1):
    x=i+n-k-1
    ans=min(ans,alist[x]-alist[i])
#    print("{}: {} - {}".format(alist[i:x],alist[x],alist[i]))

# answer
print("{}".format(ans))
