# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
adict={}
blist=[]

# solve
for i in range(n):
    a=alist[i]
    if a in adict.keys():
        blist.append(adict[a])
        adict[a]=i+1
    else:
        blist.append(-1)
        adict[a]=i+1

# answer
blist2=[]
for i in range(len(blist)):
    blist2.append(str(blist[i]))
print(" ".join(blist2))