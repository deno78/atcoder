# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
lr=[]
for i in range(n):
    l,r = map(int, input().split())
    lr.append([l,r])

# solve
pos=0
neg=0
for l,r in lr:
    pos+=r
    neg+=l

#print("{} {}".format(pos,neg))
if neg<=0 and pos>=0:
    ans=[]
    t=-1*neg
    for l,r in lr:
        if t>0:
            p=min(r-l,t)
            ans.append(str(l+p))
            t-=p
        else:
            ans.append(str(l))
    print("Yes")
    print(" ".join(ans))
else:
    print("No")
