# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,h,w = map(int, input().split())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])

# solve
all=h*w
bags=[]
for i in range(2**n):
    bag=[]
    sz=0
    for j in range(n):
        if (i>>j)&1:
            bag.append(j)
            a,b=ab[j]
            sz+=a*b
    if sz==all:
        bags.append(bag)

# answer
if len(bags)==0:
    print("No")
else:
    print(bags)
    for bag in bags:
        chk=[]
        for i in range(h):
            chk.append([0]*w)
        lines=[]
        for i in bag:
            a=ab[i][0]
            b=ab[i][1]
            lines.append()


