# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist= list(map(int, input().split()))
wlist= list(map(int, input().split()))

# solve
wdict={}
adict={}
for i in range(n):
    a=alist[i]
    w=wlist[i]
    wdict[i]=w
    if a not in adict.keys():
        adict[a]=[]
    adict[a].append(w)

ans=0
for a in adict.keys():
    l=adict[a]
#    print(l)
    ans+=sum(l)
    ans-=max(l)

# answer
print("{}".format(ans))
