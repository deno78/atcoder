# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
q = int(input())
qlist=[]
for i in range(q):
    y = list(map(int, input().split()))
    qlist.append(y)

# solve
bag={}
for i in range(q):
    y = qlist[i]
    n = y[0]
    if n==1:
        x=y[1]
        if x not in bag.keys():
            bag[x]=0
        bag[x]+=1
    elif n==2:
        x=y[1]
        bag[x]-=1
        if bag[x]==0:
            del bag[x]
    elif n==3:
        print(len(bag.keys()))
