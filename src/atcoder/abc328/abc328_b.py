# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
dlist = list(map(int, input().split()))

# solve
ans = 0

for m in range(1,n+1):
    for d in range(1,dlist[m-1]+1):
        s="{}{}".format(m,d)
        if len(list(set(list(s))))==1:
            ans+=1

# answer
print("{}".format(ans))
