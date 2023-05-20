# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
slist=[]
for i in range(n):
    slist.append(input())

# solve
ans={}
for i in range(n):
    ans[i]=[]

for i in range(n-1):
    for j in range(i,n):
        d=0
        for k in range(m):
            if slist[i][k]!=slist[j][k]:
                d+=1
        if d==1:
            ans[i].append(j)
            ans[j].append(i)


for x in range(n):
    wk=[]
    wk.append([x])
    while len(wk)>0:
        w=wk.pop()
        for a in ans[w[-1]]:
            if a not in w:
                w2=list(w)
                w2.append(a)
                if len(w2)==n:
                    print("Yes")
                    exit()
                wk.append(w2)


print("No")


