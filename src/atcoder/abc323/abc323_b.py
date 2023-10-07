# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
slist=[]
for i in range(n):
    slist.append(input())

# solve
ans={}
for i in range(n):
    c=slist[i].count("o")
    if c not in ans.keys():
        ans[c]=[]
    ans[c].append(i)

keys=[]
for k in ans.keys():
    keys.append(k)
keys.sort(reverse=True)

ans2=[]
for k in keys:
    l=ans[k]
    for c in l:
        ans2.append(str(c+1))

print(" ".join(ans2))
