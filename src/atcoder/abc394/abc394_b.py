# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
sdict={}
for i in range(n):
    s=input()
    sdict[len(s)]=s

# solve
llist=[]
for l in sdict.keys():
    llist.append(l)
llist.sort()
ans=[]
for l in llist:
    ans.append(sdict[l])

# answer
print("".join(ans))