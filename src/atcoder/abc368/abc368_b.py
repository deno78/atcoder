# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
ans=0
while True:
    alist.sort(reverse=True)
    alist[0]-=1
    alist[1]-=1
    cnt=0
    ans+=1
    for a in alist:
        if a>0:
            cnt+=1
    if cnt<=1:
        break

# answer
print("{}".format(ans))
