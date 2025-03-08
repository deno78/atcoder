# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
pile=[0]*100
Q = int(input())
query=[]
for i in range(Q):
    x=list(map(int,input().split()))
    query.append(x)

for i in range(Q):
    x=query[i]
    if len(x)==1:
        p=pile.pop(-1)
        print(p)
    else:
        x1=x[1]
        pile.append(x1)

