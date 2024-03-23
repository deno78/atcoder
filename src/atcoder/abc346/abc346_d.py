# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()
clist = list(map(int, input().split()))

# solve
ans = float("INF")

for i in range(1,n):
    wk1=0
    wk2=0
    for j in range(n):
        if j<i:
            x1=j%2
            x2=(j+1)%2
        elif j>=i:
            x1=(j+1)%2
            x2=j%2
        if s[j]!=str(x1):
            wk1+=clist[j]
        if s[j]!=str(x2):
            wk2+=clist[j]
    ans=min(ans,wk1,wk2)

# answer
print("{}".format(ans))

