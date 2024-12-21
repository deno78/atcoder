# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
hlist = list(map(int, input().split()))

# solve
hdict={}
for i in range(n):
    h=hlist[i]
    if h not in hdict.keys():
        hdict[h]=[]
    hdict[h].append(i)

ans=1
for k,v in hdict.items():
    if len(v)<2:
        continue
    vset=set(v)
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            w=2
            d=v[j]-v[i]
            dx=v[j]+d
            # print("{} {} {}".format(v[i],v[j],d))
            while dx<n:
                # print("{} {} {} {}".format(v[i],v[j],d,dx))
                if dx in vset:
                    dx+=d
                    w+=1
                else:
                    break
            ans=max(ans,w)

# answer
print(ans)