# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
blist = list(map(int, input().split()))
wlist = list(map(int, input().split()))

# solve
blist.sort(reverse=True)
wlist.sort(reverse=True)
ans=0
i1=0
i2=0
wk=0
while i2<m:
    if  i1<n and blist[i1]>=0:
        wk+=blist[i1]
        i1+=1
    else:
        if wlist[i2]>=0 and i1>i2 and i2<m:
            wk+=wlist[i2]
            i2+=1
        elif i1<n:
            wk+=blist[i1]
            i1+=1
        else:
            wk+=wlist[i2]
            i2+=1
            if i1<i2:
                break
    ans=max(ans,wk)
#    print("{}/{} {}".format(i1,i2,wk))

# answer
print(ans)
