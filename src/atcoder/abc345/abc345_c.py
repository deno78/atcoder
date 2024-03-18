# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
l=len(s)
# solve
ans=l*(l-1)//2
cdict={}
for i in range(l):
    c=s[i]
    if c not in cdict.keys():
        cdict[c]=0
    cdict[c]+=1
dupli=False
for k,v in cdict.items():
    a=v*(v-1)//2
    ans-=a
    if a>0:
        dupli=True

if dupli:
    ans+=1
# answer
print("{}".format(ans))

# aaab
# 12 aaab o
# 13 aaab x
# 14 baaa o
# 23 aaab x
# 24 abaa o
# 34 aaba o
