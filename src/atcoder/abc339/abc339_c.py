# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
blist=[]
wk=0
for i in range(n):
    wk+=alist[i]
    blist.append(wk)
x=min(blist)
ans=blist[-1]+ max(0,(-1*x))
# answer
print(ans)