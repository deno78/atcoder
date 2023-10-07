# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,x = map(int, input().split())
tlist=list(map(int,input().split()))

MOD=998244353

# solve
wk=[]
ans1=0
ans2=0
wk.append(0)

y=n** ((x+1)//min(tlist))

while len(wk)>0:
    w=wk.pop(0)
    for i in range(n):
        t=tlist[i]
        print("{} -> {} ({}/{})".format(w,t,ans1,y))
        if w+t<x+1:
            wk.append(w+t)
        else:
            if i==0:
                ans1+=1
            ans2+=1

# answer 
print("{}".format((ans1/y)%MOD))
