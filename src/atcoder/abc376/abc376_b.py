# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
ht=[]
for i in range(q):
    ht.append(input().split())

l=1
r=2

# solve
ans = 0
for i in range(q):
    h,t=ht[i]
    t=int(t)
    if h=="L" and t!=l:
        if (r<t and t<l) or (l<t and t<r) or (t<l and l<r) or (r<l and l<t):
            ans+=abs(l-t)
        else:
            ans+=n-abs(l-t)
        l=t
    elif h=="R" and t!=r:
        if (r<t and t<l) or (l<t and t<r) or (t<r and r<l) or (l<r and r<t):
            ans+=abs(r-t)
        else:
            ans+=n-abs(r-t)
        r=t
#    print("{} {} {}".format(h,t,ans))

# answer
print("{}".format(ans))

# ltr RL
# rtl RL
# lrt R
# rlt L

# tlr L
# trl R