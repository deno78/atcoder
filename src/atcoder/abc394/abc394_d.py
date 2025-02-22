# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import sys
sys.setrecursionlimit(10**8)

def check(l,r):
    ret=0
#    print("[{}] {}-{} {} ".format(i,l,r,s))
    s1=s[l]
    s2=s[r]
    if (s1=="[" and s2=="]") or (s1=="(" and s2==")") or (s1=="<" and s2==">"):
        s[l]=1
        s[r]=1
        l2=-1
        r2=-1
        ret+=2
        for j in range(sz):
            if l2==-1 and l-j>=0 and s[l-j]!=1:
                l2=l-j
            if r2==-1 and r+j<sz-1 and s[r+j]!=1:
                r2=r+j
            if l2!=-1 and r2!=-1:
                break
        if l>=0 and r<sz:
            ret+=check(l2,r2)
    return ret

# param
s = list(input())
ans=0
# solve
sz=len(s)
for i in range(sz-1):
    ans+=check(i,i+1)

# answer
if ans==sz:
    print("Yes")
else:
    print("No")
