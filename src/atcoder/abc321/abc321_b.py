# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,x = map(int, input().split())
alist=list(map(int,input().split()))

# solve
s=sum(alist)
s1=max(alist)
s2=min(alist)

# answer
for i in range(0,101):
    if i>=s1:
        a=s-s2
        if a>=x:
            print(i)
            exit()
    elif i<=s2:
        a=s-s1
        if a>=x:
            print(i)
            exit()
    else:
        a=s-s1-s2+i
        if a>=x:
            print(i)
            exit()

print(-1)