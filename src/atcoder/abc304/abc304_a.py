# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
slist=[]
alist=[]
ans=0
for i in range(n):
    s,a=input().split()
    alist.append(int(a))
    slist.append(s)

x=-1
for i in range(n):
    if alist[i]==min(alist):
        x=i
        break

for i in range(n):
    y=(i+x)%n
    print(slist[y])
