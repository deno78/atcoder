# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math

# param
k = int(input())
clist = list(map(int, input().split()))
MOD=998244353
# solve

wk=[]

wk.append(0,clist)

ans=0
while len(wk)>0:
    w=wk.pop(0)
    wa=w[0]
    wc=w[1]
    if wa
    for i in range(len(wc)):
        if wc[i]>0:
            wc2=[]
            for x in wc:
                wc2.append(x)
            wc2[i]-=1

            





# answer
print("{}".format(ans))
