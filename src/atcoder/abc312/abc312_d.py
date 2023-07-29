# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math
from math import factorial as fct
def rl(a):  # run length of the list 
  a.sort()
  ret, l = [], 1
  for i in range(1,len(a)):
    if a[i] != a[i-1]:
      ret.append(l)
      l = 1
    else: l += 1
  ret.append(l)
  return ret

def dperm(a): # num of distinct permutation 
  ret = fct(len(a))
  for r in rl(a):
    ret //= fct(r)
  return ret 

# param
s = input()

MOD=998244353

if s.count("?")==0:
    print(0)
    exit()

# solve
ans=1
wk=0
for s1 in s.split("("):
    for s2 in s1.split(")"):
        c1=len(s2)//2
        c2=len(s2)//2
        l1=[0]*c1
        l2=[1]*c2
        l1.extend(l2)
        p=dperm(l1)
        if len(s2)>0 and len(s2)%2==0:
           p*=(len(s2))//2
           wk+=1
#           print((len(s2)-1))
#        print("[{}]len:{} pattern:[{}] ans:{}".format(s2,len(s2),p,ans))
        ans*=p
        ans%=MOD

# answer
print(ans)
