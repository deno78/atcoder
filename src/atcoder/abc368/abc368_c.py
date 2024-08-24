# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
hlist = list(map(int, input().split()))

# solve
t=0
for i in range(n):
    t0=t
    h=hlist[i]
    for j in range(3):
        if t%3==0:
            break
        t+=1
        if (t-1)%3==2:
            h-=3
        else:
            h-=1
#        print("[{}]\tt:{} h:{}".format(i,t,h))
        if h<=0:
            break
    d1=0
    d2=0
    if h>0:
        d1=(h//5)*3
        d2=min(h%5,3)
        t+=(d1+d2)
#    print("[{}] T:{}-{} H:{} D1:{} D2:{}".format(i,t0,t,h,d1,d2))

# answer
print("{}".format(t))
