# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m,k = map(int, input().split())
abdic={}
for i in range(n):
    abdic[i]=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    abdic[a].append(b)
    abdic[b].append(a)

ph=[]
for i in range(k):
    p,h=map(int,input().split())
    ph.append([p-1,h])

# solve
ans=[-1]*n
wk=[]

for p,h in ph:
    wk.append(p)
    ans[p]=h
while len(wk)>0:
    w=wk.pop(0)
    ht=ans[w]
    next = abdic[w]
    for i in next:
        if ans[i]<ht:
            wk.append(i)
            ans[i]=ht-1

# answer
ans2=[]
for i in range(n):
    if ans[i] >=0:
        ans2.append(str(i+1))

print(len(ans2))
print(" ".join(ans2))
