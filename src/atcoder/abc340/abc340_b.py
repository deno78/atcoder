# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
q = int(input())
query=[]
for i in range(q):
    x,y = map(int, input().split())
    query.append([x,y])

a=[]
for i in range(q):
    x,y = query[i]
    if x==1:
        a.append(y)
    elif x==2:
        print(a[-1*y])

# solve

# answer
