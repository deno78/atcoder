# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
s = input()
lr=[]
for i in range(q):
    l,r=map(int,input().split())
    l-=1
    r-=1
    lr.append([l,r])

# solve
slist=[]
wk=0
slist.append(0)
for i in range(n-1):
    if s[i]==s[i+1]:
        wk+=1
    slist.append(wk)

# answer
for l,r in lr:
    print(slist[r]-slist[l])
