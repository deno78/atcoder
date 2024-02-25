# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
plist=list(map(int,input().split()))
q = int(input())
ab=[]
for i in range(q):
    a,b = map(int, input().split())
    ab.append([a,b])

pdict={}
for i in range(n):
    p=plist[i]
    pdict[p]=i

# solve
for i in range(q):
    a,b=ab[i]
    ai=pdict[a]
    bi=pdict[b]
    if ai > bi:
        print(b)
    else:
        print(a)
