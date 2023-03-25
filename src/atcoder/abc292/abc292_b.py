# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())

xlist=[0]*(n+1)

for i in range(q):
    c,x=map(int,input().split())
    if c==1:
        xlist[x]+=1
    elif c==2:
        xlist[x]=2
    elif c==3:
        if xlist[x]>=2:
            print("Yes")
        else:
            print("No")
