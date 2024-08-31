# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
aslist=[]
l=-1
r=-1
for i in range(n):
    a,s= input().split()
    if l==-1 and s=="L":
        l=int(a)
    if r==-1 and s=="R":
        r=int(a)
    aslist.append([a,s])

# solve
ans=0
for i in range(n):
    a=int(aslist[i][0])
    s=aslist[i][1]
    if s=="L":
        if l==-1:
            l=a
        ans+=abs(l-a)
        l=a
    else:
        if r==-1:
            r=a
        ans+=abs(r-a)
        r=a
# answer
print("{}".format(ans))
