# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from functools import cmp_to_key

def check(x,y):
    a1=x[1]
    b1=x[2]
    a2=y[1]
    b2=y[2]
    v1=a1*(a2+b2)
    v2=a2*(a1+b1)
#    print("{}/{} {}/{}".format(x,y,v1,v2))
    if v1>v2:
        return 1
    elif v2>v1:
        return -1
    else:
        return 0
   
# param
n = int(input())

ab=[]
for i in range(n):
    a,b = map(int, input().split())
    ab.append([str(i+1),a,b])

lst=sorted(ab,key=cmp_to_key(check),reverse=True) 

ans=[]
for i in range(n):
    l=lst[i]
    ans.append(l[0])

print(" ".join(ans))