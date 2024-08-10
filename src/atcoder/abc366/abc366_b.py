# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import re

# param
n = int(input())
slist=[]
x=-1
for i in range(n):
    s=input()
    x=max(len(s),x)
    slist.append(s)

tlist=[]
for i in range(x):
    tlist.append(["*"]*(n))
# solve
for i in range(n):
    s=slist[i]
    for j in range(len(s)):
        tlist[j][i]=s[j]
# answer
for i in range(len(tlist)):
    t2=reversed(tlist[i])
    s2="".join(t2)
    s3=re.sub("\*+$","",s2)
    print(s3)