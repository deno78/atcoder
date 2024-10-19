# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())

ab={}
for i in range(n):
    ab[i]=[]

for i in range(m):
    a,b = map(int, input().split())
    a-=1
    b-=1
    ab[a].append(b)
    ab[b].append(a)

ans=[0]*n

# solve
wk=[]
ans[0]=1
wk.append([0])

while len(wk)>0:
    w=wk.pop(0)
    print("[{}] {}".format(w,ans))
    for b in ab[w[-1]]:
        if b not in w:
            ans[b]=ans[w]+1
            w.append(b)
            wk.append(b)

# answer
print(ab[0])
for b in ab[0]:
    print(ans[b])