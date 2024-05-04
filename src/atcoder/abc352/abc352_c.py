# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
ab=[]
all=0
clist=[]
for i in range(n):
    a,b = map(int, input().split())
    c=b-a
    clist.append(c)
    all+=a
    ab.append([a,b,c])

# solve
ans = all+max(clist)

# answer
print("{}".format(ans))
