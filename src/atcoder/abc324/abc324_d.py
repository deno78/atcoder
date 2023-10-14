# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math

# param
n = int(input())
s = input()

s2=list(s)
s2.sort(reverse=True)
n2=int("".join(s2))
# solve
roots=[]
for i in range(int(math.sqrt(n2))+1):
    r=list(str(i**2).zfill(n))
    r.sort(reverse=True)
    roots.append("".join(r))
#    print("{} -> {} / {} ".format(i**2,"".join(r),str(n2)))

ans=0
for r in roots:
    if r==str(n2):
        ans+=1

# answer
print(ans)