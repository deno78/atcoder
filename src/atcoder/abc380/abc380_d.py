# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
q = int(input())
klist=list(map(int,input().split()))

wk=[0]
for i in range(max(klist)//len(s)+1):
    x=len(wk)
    for i in range(x):
        wk.append((wk[i]+1)%2)

print(wk)
# solve
ans=[]
for i in range(q):
    k=klist[i]
    k-=1
    k1=k//len(s)
    k2=k%len(s)

    if wk[k1]==0:
        ans.append(s[k2])
    else:
        ans.append(s[k2].swapcase())
#    print("[{}] {} = {} + {} ->{}".format(i,k,k1,k2,ans[-1]))

print(" ".join(ans))
