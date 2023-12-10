# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
s = input()

# solve
ans=0
wk1=0
wk=0
for i in range(n):
    c = s[i]
    if c=="0":
        ans=max(ans,wk)
        wk1=0
        wk=0
    elif c=="1":
        wk1+=1
        if wk1>m:
            wk+=1
    elif c=="2":
        wk+=1

ans=max(ans,wk)

# answer
print("{}".format(ans))
